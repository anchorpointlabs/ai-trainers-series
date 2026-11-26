# Model Selection and Evaluation (TSC 4 and 5) — Knowledge Distillation

> **Source model:** Gemini 4 Argon (`gemini-4-argon`) via i10x
> **Extracted:** 2026-11-26 (distillation run)
> **Status:** RAW distillation — exhaustive extraction, not yet cut into entry-template format.

---

## 1. DEFINITION AND BOUNDARIES

### The Four Distinct Disciplines

1. **Plain Prompting (Prompt Engineering)**
   * **What it is:** The act of crafting, structuring, and iterating on the text, image, or audio input sent to a fixed, pre-selected model to elicit a desired output within a single inference call or conversation session.
   * **What it controls:** System instructions, few-shot examples, output formatting constraints (e.g., JSON schemas), persona framing, and step-by-step reasoning instructions (Chain-of-Thought).
   * **Where it stops:** It stops the moment you systematically measure output quality across a dataset (which is **Model Evaluation**), change the underlying model ID or sampling hyperparameters across an application (which enters **Model Selection**), or wrap the prompt in automated retry logic, version control, or API gateways (which is **LLMOps**).

2. **Model Selection**
   * **What it is:** The decision-making framework used to choose a specific foundation model, open-weight checkpoint, or specialized model architecture from a candidate pool to satisfy defined technical, financial, legal, and product constraints.
   * **What it controls:** The choice of model family (e.g., Claude 3.5 Sonnet vs. Llama 3.1 70B vs. SEA-LION), deployment pattern (SaaS API vs. self-hosted VPC), parameter count, quantization level, and modality capabilities.
   * **Where it stops:** Model selection defines the *candidates* and the *acceptance criteria*. The actual scoring of those candidates on test prompts is **Model Evaluation**. The provisioning of GPUs or API keys to run the chosen model is **LLMOps**.

3. **Model Evaluation**
   * **What it is:** The systematic, empirical measurement of a generative system's outputs against predefined quality, safety, latency, and cost criteria using a standardized dataset and reproducible scoring rubrics.
   * **What it controls:** Dataset curation (golden datasets), metric definition, human annotation protocols, automated grading (LLM-as-a-judge, deterministic assertions), regression testing, and statistical significance testing between two system variants.
   * **Where it stops:** Evaluation produces *evidence and scores*, not decisions or infrastructure. Deciding whether a 4% accuracy drop is worth a 60% cost reduction is **Model Selection**. Running those evaluations automatically on every Git commit or sampling 5% of live user traffic is **LLMOps**.

4. **LLMOps (Large Language Model Operations)**
   * **What it is:** The production infrastructure, engineering practices, and lifecycle management pipelines required to serve, monitor, secure, update, and govern generative AI applications reliably at scale.
   * **What it controls:** Prompt and model registries, inference serving engines (e.g., `vLLM`, `TGI`), API routing, semantic caching, guardrails, telemetry (latency, token usage, error rates), CI/CD evaluation triggers, drift detection, and rollback mechanisms.
   * **Where it stops:** LLMOps does not write the initial prompt (**Prompting**), does not invent the scoring rubric (**Evaluation**), and does not conduct the initial business case analysis for picking an open-weight vs. commercial model (**Model Selection**)—though it provides the platform on which all three execute continuously.

---

### Boundary Matrix

| Boundary Pair | Where Discipline A Ends | Where Discipline B Begins | Common Trainer/Learner Confusion |
| :--- | :--- | :--- | :--- |
| **Prompting vs. Evaluation** | Eyeballing 3–5 outputs in a playground ("vibe checking") to see if a prompt change worked. | Running that prompt across 100+ representative test cases and computing an aggregate pass/fail metric. | Learners think testing a prompt 5 times in ChatGPT is "evaluating the model." It is only ad-hoc prompt iteration. |
| **Prompting vs. Selection** | Changing the wording of instructions to force a model to output valid JSON. | Switching to a model that supports native constrained decoding (Structured Outputs) or higher instruction-following capability. | Teams spend weeks trying to prompt-engineer around a small model's reasoning ceiling instead of selecting a more capable model. |
| **Selection vs. Evaluation** | Filtering out models that cannot run on-premise, cost more than $2/1M tokens, or lack a 128k context window. | Measuring which of the 3 surviving candidate models hallucinates least on your internal HR policy PDFs. | Treating public benchmark tables as Model Selection. Benchmarks are generic evaluations; Selection requires mapping results to business constraints. |
| **Evaluation vs. LLMOps** | Designing the hallucination rubric and validating that the LLM-as-a-judge correlates with human domain experts. | Executing that rubric asynchronously on 10,000 production logs every night and paging an engineer if scores drop by >5%. | Thinking evaluation is a one-time pre-launch gate rather than a continuous production observability loop. |
| **Selection vs. LLMOps** | Deciding that the architecture requires a primary frontier model with a smaller fallback model for outage resilience. | Implementing the health-check router that detects a `503 Service Unavailable` or timeout and dynamically reroutes traffic to the fallback model. | Assuming that choosing a multi-model strategy on paper solves the operational problem of prompt incompatibility between models during a failover. |

---

## 2. CORE MECHANICS

To select, evaluate, or deploy a model intelligently, a practitioner must understand how the internal mechanics directly cause external failure modes, cost spikes, and latency bottlenecks.

### 1. Tokenization
* **How it works:** Models do not read characters or words; they read **tokens** (integers mapped to sub-word character chunks via algorithms like Byte-Pair Encoding (BPE) or SentencePiece). A common English word is roughly 1.3 tokens (`"apple"` = 1 token), while rare words, code, or non-Latin scripts split into many tokens.
* **Why it matters for Selection & Evaluation:**
  * **Multilingual Penalty:** A model trained primarily on English has a tokenizer optimized for English. Non-English languages (e.g., Tamil, Chinese, Bahasa Melayu, or Singlish slang) often require 2x to 5x more tokens to represent the same semantic meaning. This directly multiplies your API cost by 2x–5x, shrinks your effective context window by 2x–5x, and increases latency proportionally.
  * **Arithmetic & Character Blindness:** Because `"strawberry"` is tokenized into chunks (e.g., `["str", "aw", "berry"]`), the model never sees individual letters unless forced to spell them out token-by-token.

### 2. The Transformer & Self-Attention
* **How it works:** The core engine of modern LLMs is the **Transformer** architecture. Its defining mechanism is **Self-Attention**, which calculates an affinity score between every token in a sequence and every other token preceding it. This allows the model to resolve ambiguity (e.g., knowing whether the word `"bank"` refers to a river or a financial institution based on surrounding words 500 tokens away).
* **The Quadratic Bottleneck:** Standard self-attention scales **quadratically** \(O(N^2)\) with sequence length \(N\). Doubling the input prompt length from 10,000 to 20,000 tokens roughly quadruples the compute required to compute the attention matrix during the prefill stage.
* **The KV Cache (Key-Value Cache):** During generation, to avoid recomputing attention for past tokens at every single step, the inference engine stores the intermediate attention tensors (Keys and Values) in GPU High-Bandwidth Memory (HBM).
  * **Operational Impact:** The KV cache grows linearly with context length and batch size. In production, GPU memory runs out because of the **KV cache** long before you hit compute limits when serving long prompts to many concurrent users. Architectural tweaks like **Grouped-Query Attention (GQA)** and **Multi-Head Latent Attention (MLA)** exist specifically to shrink the KV cache footprint.

### 3. Architectures: Encoders vs. Decoders
1. **Encoder-Only (e.g., BERT, RoBERTa, BGE-M3):**
   * **Mechanic:** Bidirectional attention. Every token attends to tokens both before and after it simultaneously. It cannot generate fluent multi-sentence text efficiently, but it builds dense semantic representations of input text.
   * **Use Case:** Text classification, Named Entity Recognition (NER), sentiment analysis, embeddings for vector search (RAG), and cross-encoder reranking.
   * **Selection Rule:** Never use a 70B generative LLM to classify 1,000,000 support tickets into 5 buckets when a 300M parameter Encoder model can do it 100x faster and 500x cheaper.
2. **Decoder-Only (e.g., GPT-4o, Claude 3.5, Llama 3, Qwen 2.5):**
   * **Mechanic:** Causal (unidirectional) masked attention. Token \(t\) can only attend to tokens \(1 \dots t-1\). It works by autoregressively predicting the probability distribution of the very next token, sampling one, appending it to the input, and repeating.
   * **Use Case:** All general-purpose text generation, chat, coding, and reasoning.
   * **Selection Rule:** Autoregressive generation means latency is bound by **output length**, not input length. Generating 1,000 tokens requires 1,000 sequential forward passes through the model weights.
3. **Encoder-Decoder (e.g., T5, BART, Whisper):**
   * **Mechanic:** An encoder processes the input bidirectionally into an intermediate representation; a decoder generates the output token-by-token while attending to the encoder's output.
   * **Use Case:** Sequence-to-sequence tasks where input and output have distinct structural mappings, such as speech-to-text (`Whisper`) or machine translation.
4. **Mixture-of-Experts (MoE) vs. Dense Models (e.g., Mixtral 8x7B, DeepSeek-V3 vs. Llama-3-70B):**
   * **Mechanic:** A Dense model activates 100% of its parameters for every token generated. An MoE model divides its Feed-Forward Network layers into distinct "experts" and uses a routing network to activate only a small subset (e.g., 2 out of 8 experts) for any single token.
   * **Operational Impact:** An MoE model has the **VRAM requirement** of a massive model (all experts must reside in GPU memory) but the **inference speed and compute cost (FLOPs)** of a small model (only active parameters are computed per token).

### 4. Training Stages and Their Impact on Behavior

| Stage | What Happens Mechanically | What the Model Learns | What It Means for Selection & Evaluation |
| :--- | :--- | :--- | :--- |
| **1. Pre-training** | Self-supervised next-token prediction over trillions of tokens of raw web text, code, and books. Costs millions of dollars in compute. | World knowledge, grammar, syntax, multilingual vocabulary, and statistical associations between concepts. | **Base Models** only know how to continue a document. If you prompt a Base Model with `"What is the capital of France?"`, it may output `"What is the capital of Germany? What is the capital of Spain?"` thinking it is completing a quiz list. Never select a raw base model for a chatbot without fine-tuning. |
| **2. Supervised Fine-Tuning (SFT) / Instruction Tuning** | Trained on hundreds of thousands of curated `(Instruction, Ideal Response)` pairs. | How to act as an assistant, follow instructions, format outputs, and answer questions rather than just completing text. | Defines the model's baseline formatting habits, verbosity, and structural obedience. Poor SFT leads to models that ignore negative constraints. |
| **3. Preference Alignment (RLHF / DPO / RLAIF)** | **Reinforcement Learning from Human Feedback** or **Direct Preference Optimization**: The model compares winning vs. losing responses (`y_win` vs `y_lose`) and adjusts weights to maximize human preference and safety refusal behavior. | Tone, politeness, safety boundaries (refusing harmful requests), and reducing toxic or unhinged outputs. | **The Alignment Tax & Sycophancy:** Over-aligned models suffer from false refusals (refusing benign cybersecurity or medical terminology) and **sycophancy** (agreeing with the user even when the user states a falsehood). Evaluation must test for both under-refusal (safety breach) and over-refusal (usability failure). |
| **4. Reasoning Post-Training (RL on Chain-of-Thought)** | Reinforcement learning against verifiable rewards (math proofs, unit tests) to generate long internal "thinking" traces before outputting a final answer (e.g., OpenAI o1/o3-mini, DeepSeek-R1). | Self-correction, backtracking, decomposition of complex logic, math, and multi-constraint planning. | **Inference-Time Compute Trade-off:** Reasoning models generate thousands of hidden/visible "thinking tokens" before answering. They are slow and expensive for simple tasks (like summarization or translation) where standard instruct models excel, but dramatically outperform on complex logic, code architecture, and multi-step planning. |

### 5. Sampling Mechanics (Decoding Parameters)
At the final layer (the language modeling head), the model outputs a vector of raw, unnormalized scores called **logits** across its entire vocabulary (e.g., 128,000 tokens). A `Softmax` function converts logits into a probability distribution summing to 1.0. How you sample from this distribution dictates evaluation reproducibility:
* **Temperature (\(T\)):** Divides the logits by \(T\) before applying `Softmax`.
  * \(T \to 0\) (Greedy Decoding): The highest-probability token is always picked. Maximizes determinism, recommended for classification, extraction, and evaluation runs. (Note: even at `temperature=0`, floating-point non-determinism in GPU kernels and MoE batch routing can cause minor output variance).
  * \(T > 1\): Flattens the probability distribution, making lower-probability tokens more likely. Increases creativity and diversity at the direct expense of factual accuracy and coherence.
* **Top-p (Nucleus Sampling):** Ranks tokens by probability and keeps only the smallest set of tokens whose cumulative probability exceeds \(p\) (e.g., `top_p = 0.90`), discarding the long tail of nonsensical tokens.
* **Top-k:** Keeps only the top \(k\) most likely tokens (e.g., `top_k = 50`) before resampling.
* **Structured Outputs / Constrained Decoding:** Applies a state machine (e.g., Finite State Automaton derived from a Regex or JSON Schema) directly to the logit layer, masking out (setting probability to `0`) any token that would violate the syntax of the required schema.

---

## 3. CHOOSING A MODEL

Every model selection decision is a multi-variable optimization problem across eight non-negotiable dimensions.

### 1. Modality
* **What it covers:** Text-in/Text-out, Vision (Image/Video-in), Audio (Speech-in/Speech-out), Embeddings, Multimodal Native vs. Stitched Pipelines (e.g., `OCR -> LLM` vs. `Native Vision-Language Model (VLM)`).
* **How it matters:** Native multimodal models process visual tokens or audio waveforms directly in the same representation space as text. They preserve spatial layout (tables, flowcharts, handwriting, checkboxes) and vocal tone/prosody that stitched `OCR -> Text LLM` or `ASR -> Text LLM` pipelines destroy.
* **How it fails when ignored:** A team picks a text-only LLM plus a traditional OCR library to process scanned Singapore GST invoices. The OCR scrambles multi-column line items and misses handwritten annotations, causing the LLM to hallucinate invoice totals—whereas a native VLM inspecting the raw image would read the spatial alignment accurately.

### 2. Model Size & Parameter Class
* **What it covers:**
  * Nano/Edge (<4B parameters)
  * Small Language Models / SLMs (7B–14B parameters)
  * Mid-size Models (30B–70B parameters)
  * Frontier / Large Models (100B–1T+ parameters, typically proprietary or massive MoE)
* **How it matters:** Parameter count correlates strongly with breadth of world knowledge, complex compositional reasoning, and zero-shot instruction adherence across ambiguous edge cases. However, narrow tasks (classification, schema extraction, formatting, simple RAG summarization) saturate quickly at 7B–14B parameters.
* **How it fails when ignored:**
  * *Over-sizing:* Using a massive frontier model to classify incoming customer emails into 10 routing categories. Result: 20x higher cost and 4-second latency when a fine-tuned 8B model achieves identical accuracy in 150ms.
  * *Under-sizing:* Using an 8B model for complex multi-turn legal contract redlining involving 15 simultaneous policy constraints. Result: The model drops constraints after turn 3 because its attention capacity cannot track the full state space.

### 3. Cost (Token Economics & Total Cost of Ownership)
* **What it covers:**
  * **Pay-per-token (SaaS):** Input token price, Output token price (typically 3x–5x more expensive than input tokens because output generation is memory-bandwidth bound and sequential), Cached Input token price (often 50%–90% discount), and Batch API discounts (typically 50% off for 24-hour asynchronous turnaround).
  * **Provisioned Throughput / Self-Hosted:** Hourly GPU instance cost (e.g., AWS `p5.48xlarge` or `g6e`), idle capacity waste, DevOps engineering overhead, and networking/egress fees.
* **How it matters:** Cost scales with user adoption *multiplied* by prompt size and conversation turns. In multi-turn chat or agentic loops, the conversation history is re-sent on every turn, causing token consumption to grow quadratically across a session.
* **How it fails when ignored:** A team builds an internal RAG assistant that stuffs 40,000 tokens of retrieved documents into every prompt without prompt caching. During the 20-user pilot, it costs $50/month. When rolled out to 5,000 employees making 20 queries a day, the bill hits $150,000/month and the project is shut down by Finance.

### 4. Speed and Latency Profiles
* **What it covers:**
  * **Time to First Token (TTFT):** The delay between sending the request and receiving the very first output token. Dominated by network latency and **prefill compute** (processing the input prompt).
  * **Inter-Token Latency (ITL) / Time Per Output Token (TPOT):** The time to generate each subsequent token (often measured in Tokens Per Second, `tok/s`). Dominated by model size and GPU memory bandwidth.
  * **End-to-End Latency:** \(\text{TTFT} + (\text{TPOT} \times \text{Total Output Tokens})\).
* **How it matters:** Different UX patterns have hard human-perception thresholds:
  * Voice bots require End-to-End or TTFT < 300–500ms to feel conversational.
  * Interactive streaming chat requires TTFT < 1.5s and generation speed > 30 `tok/s` (faster than human reading speed).
  * Background batch extraction (e.g., overnight compliance checks) cares only about total throughput, not latency.
* **How it fails when ignored:** A team selects a Deep Reasoning model (which thinks for 25 seconds before emitting its first visible token) for a live customer service phone IVR system. Customers hang up thinking the phone line is dead.

### 5. Context Window (Declared vs. Effective)
* **What it covers:** Maximum input + output tokens supported by the model (e.g., 8k, 32k, 128k, 1M, 2M tokens).
* **How it matters:** Determines how many documents, code files, or few-shot examples can be passed in a single call without chunking.
* **How it fails when ignored ("Lost in the Middle" & Effective Context Degradation):** A vendor advertises a 128k or 1M context window. That only means the model will not throw an API error at 128k tokens. In practice, retrieval accuracy and reasoning over facts buried in the middle 40%–70% of a massive prompt degrade sharply (often dropping below 60% recall on multi-needle retrieval tests like `RULER`), while TTFT and cost skyrocket. Treating a large context window as a replacement for proper search/filtering leads to high latency, huge bills, and silent omissions.

### 6. Native Features and Tooling Ecosystem
* **What it covers:**
  * Native Tool Use / Function Calling accuracy
  * Strict Structured Outputs (JSON Schema enforcement)
  * Context / Prompt Caching
  * Logprobs access (returning exact token probability scores, critical for classification confidence and evaluation)
  * System Prompt adherence strength
  * Batch API availability
  * Built-in citations / grounding metadata
* **How it matters:** Native features eliminate hundreds of lines of brittle glue code and regex post-processing.
* **How it fails when ignored:** A team builds a data extraction pipeline using a model without constrained JSON schema decoding. In 2% of production calls, the model adds conversational wrapper text (`"Here is your JSON: {..."`) or forgets a trailing bracket, crashing the downstream database ingestion parser.

### 7. Data Residency, Privacy, Security, and Compliance
* **What it covers:**
  * **Zero Data Retention (ZDR) & Training Opt-Out:** Contractual guarantee that the provider does not log prompts/completions or train future foundation models on customer data.
  * **Geographic Data Residency:** Ensuring inference compute and data at rest remain within specific jurisdictions (e.g., AWS `ap-southeast-1` Singapore region).
  * **Regulatory Frameworks (Singapore Context):** Singapore Personal Data Protection Act (**PDPA** — cross-border transfer obligations), Monetary Authority of Singapore (**MAS**) Technology Risk Management (**TRM**) guidelines and Notice 655 (for financial institutions), Healthcare Services Act / MOH guidelines, and IMDA **Model AI Governance Framework for Generative AI**.
  * **Air-Gapped / On-Premise Requirements:** Defense, government (GovTech GCC vs. on-prem), and critical infrastructure.
* **How it fails when ignored:** A developer builds a working prototype using a consumer tier or US-hosted API endpoint without an Enterprise Data Processing Agreement (DPA) or regional residency. Six months later, Legal and InfoSec block the production deployment during security review because customer PII (NRIC numbers, financial records) is routing through US servers and retained for 30 days by the vendor's abuse-monitoring human reviewers.

### 8. Vendor Risk, Licensing, and Lifecycle Stability
* **What it covers:**
  * **Deprecation Cycles:** Commercial API providers routinely retire model snapshots every 6–12 months.
  * **Silent Weight/System Updates:** SaaS endpoints pointing to generic aliases (e.g., `gpt-4o` instead of a dated snapshot) can change behavior overnight.
  * **Rate Limits:** Requests Per Minute (RPM) and Tokens Per Minute (TPM) ceilings across spending tiers.
  * **Open-Weight Licensing Nuances:** Not all "open" models are truly open source under OSI definitions. Apache 2.0 / MIT (e.g., Qwen 2.5, Mistral 7B) allow unrestricted commercial use. Custom community licenses (e.g., Llama 3 Community License) impose Monthly Active User (MAU > 700M) clauses or naming restrictions; other weights are strictly `Non-Commercial (CC-BY-NC)` or prohibit using their outputs to train non-family models.
  * **Regional / Geopolitical Supply Chain Risk:** Risk of API access revocation, export controls, or entity-list sanctions affecting specific vendor jurisdictions.
* **How it fails when ignored:** A company hardcodes its entire product around a single proprietary model alias without pinning the snapshot version or designing an abstraction layer. When the vendor deprecates the model version with 60 days' notice—or suffers a 12-hour global outage—the company's core product breaks because their complex 4,000-word prompt fails on every alternative model.

---

## 4. THE BUILD-VS-BUY DECISION

Practitioners must choose not only *which* model to use, but *how* to adapt it to domain problems. This comprises two intersecting decisions: **Adaptation Pattern** (Prompting vs. RAG vs. Fine-Tuning vs. Pre-training) and **Hosting Pattern** (Commercial API vs. Managed Cloud vs. Self-Hosted Open-Weight).

### Part A: The Adaptation Spectrum

#### 1. In-Context Learning (Plain Prompting & Few-Shot)
* **What it does:** Changes the model's inputs at inference time without changing its weights or hooking it up to external search databases.
* **When it wins:**
  * The knowledge required is already in the model's pre-training weights (general tasks, coding, translation, summarizing text provided directly by the user).
  * You have fewer than 50 examples of the task.
  * Speed to market is the highest priority (hours, not weeks).
* **Where it loses:**
  * You need the model to answer questions across a dynamic library of 50,000 private corporate documents.
  * Your few-shot instructions require 15,000 tokens on every single API call, driving up TTFT and per-call token cost at high request volumes.

#### 2. RAG (Retrieval-Augmented Generation)
* **What it does:** Connects the LLM to an external knowledge index (vector database, lexical search like BM25, or knowledge graph). At query time, relevant chunks are retrieved and injected into the prompt context so the model can ground its answer in verifiable source text.
* **When it wins:**
  * **Knowledge injection:** The model needs access to proprietary, private, or rapidly changing facts (e.g., daily inventory, updated MOM labor laws, internal standard operating procedures).
  * **Hallucination control & auditability:** You require verifiable inline citations pointing to exact page numbers and source documents.
  * **Access Control (RBAC):** Document visibility depends on who is asking (e.g., a manager can retrieve payroll policies that an intern cannot; you can enforce ACLs at the retrieval step, whereas you cannot selectively hide facts baked into model weights).
* **Where it loses:**
  * RAG cannot teach a model a brand-new language, a strict domain-specific writing style, or a complex reasoning logic if the underlying base model lacks the capability to follow the instructions.
  * It introduces a two-stage failure surface: if the retriever pulls the wrong chunks (Retrieval Failure), the generator will produce a wrong answer no matter how smart the LLM is.

#### 3. Fine-Tuning (SFT, LoRA / QLoRA, DPO)
* **What it does:** Updates the model's internal weights (or trains lightweight low-rank adapter matrices via **LoRA**) using a curated dataset of hundreds to tens of thousands of domain examples.
* **When it wins:**
  * **Form, Style, and Behavior—NOT dynamic facts:** Teaching the model to strictly adhere to a complex JSON schema, adopt a specific brand tone, write code in a proprietary internal DSL, or handle domain slang/jargon (e.g., Singapore clinical shorthand or Singlish customer chats).
  * **Cost & Latency Compression (Model Distillation):** Taking a prompt that requires 5,000 tokens of instructions on a massive frontier model, generating 10,000 high-quality synthetic input/output pairs, and fine-tuning a small 8B model to perform that exact task with a 50-token prompt at 1/20th the cost and 5x the speed.
* **Where it loses:**
  * **Teaching rapidly changing facts:** Fine-tuning is the wrong tool for injecting daily facts. Models trained on new facts via SFT frequently hallucinate by blending new facts with old pre-trained weights (**catastrophic forgetting**), cannot cite sources, and cannot "unlearn" a deleted record upon a PDPA data deletion request without an expensive retraining run.
  * **High fixed engineering cost:** Requires data curation, cleaning, training pipelines, hyperparameter tuning, and re-running the entire fine-tuning pipeline every time you want to upgrade to a newer generation base model.

#### 4. Continued Pre-Training (CPT) vs. Scratch Pre-Training
* **What it does:** Training an existing base model on billions of raw, unlabeled domain tokens (CPT), or training random weights from zero (Scratch).
* **When it wins:** Only when the target language or modality is virtually absent from existing foundation models (e.g., underrepresented Southeast Asian dialects, ancient scripts, raw genomic sequences, or specialized telemetry formats).
* **Where it loses:** Almost everywhere else in enterprise AI. It costs hundreds of thousands to millions of dollars, requires deep ML research teams, and usually underperforms a good open-weight model combined with RAG and LoRA SFT.

### Part B: Comprehensive Trade-Off Matrix

| Dimension | Plain Prompting | RAG | Fine-Tuning (SFT / LoRA) | Continued Pre-Training (CPT) |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Goal** | Task specification & quick behavior steering | Grounding in dynamic, private, verifiable facts | Teaching consistent style, format, tone, or compressing a large model into a small one | Teaching an entirely new language corpus or foundational domain vocabulary |
| **Upfront Data Required** | 0 to 20 examples | Raw documents/databases (no labeled Q&A pairs needed to start) | 500 to 50,000+ clean, human-verified or synthetic `(input, output)` pairs | Billions of tokens of clean domain text |
| **Knowledge Freshness** | Instant (within prompt payload) | Near real-time (seconds after re-indexing a document) | Static (frozen at training time; requires retraining to update) | Static (frozen at training time) |
| **Source Attribution / Citations** | Only over user-pasted text | High (direct link to retrieved chunk ID & metadata) | None (knowledge is dissolved into opaque neural weights) | None |
| **Access Control (RBAC)** | Handled at app layer | Granular (filter vector search by user role/permissions) | Impossible per-fact (all users querying the model share the same weights) | Impossible per-fact |
| **Inference Latency Impact** | Scales with prompt length | Adds 50ms–500ms for embedding + search + reranking, plus longer prompt prefill | Reduces latency (allows shorter prompts and smaller 7B–14B models) | Neutral (same architecture size) |
| **Upfront Engineering Cost** | Hours | Days to Weeks (chunking, parsing PDFs, metadata, hybrid search) | Weeks to Months (dataset curation, training pipeline, evaluation against forgetting) | Months + massive GPU cluster budget |
| **Model Upgrade Portability** | Medium (tweak prompt for new model) | High (swap generator LLM in 1 line of code while keeping the vector DB) | Low (LoRA adapters are bound to exact base model weights; new base model = full retrain) | Zero (bound to exact base model architecture) |

*Note: In mature production systems, these are **complementary, not mutually exclusive**. A production system often uses a **Fine-Tuned** model (trained to output strict JSON and understand domain jargon) inside a **RAG** pipeline (to pull live customer facts) guided by a structured **System Prompt**.*

---

## 5. DEPLOYMENT AND LLMOPS

LLMOps differs from traditional MLOps in four ways: models are massive (requiring specialized GPU memory management), inputs/outputs are unstructured text rather than numeric feature vectors, ground-truth labels rarely exist in real time, and third-party API dependencies introduce external rate limits and silent behavioral shifts.

### 1. Versioning and Artifacts Registry
In traditional software, changing code changes behavior. In GenAI, changing *any* of six separate artifacts changes system behavior. Every production request log must record the immutable cryptographic hash or version ID of all six:
1. **Model Artifact:** Exact provider snapshot (e.g., `gpt-4o-2024-11-20`, never just `gpt-4o`) or exact open-weight commit hash + LoRA adapter version + quantization format (`AWQ-INT4` vs `FP16`).
2. **Prompt Template:** The system prompt, user template, and variable interpolation logic, decoupled from application code in a versioned Prompt Registry.
3. **Sampling Configuration:** Exact `temperature`, `top_p`, `max_tokens`, `seed`, and stop sequences.
4. **Tool / Schema Definitions:** The exact JSON schemas and descriptions of every function/tool exposed to the model.
5. **Retrieval / RAG State:** The embedding model version, chunking parameters (size/overlap), vector index snapshot, and reranker model version.
6. **Guardrail Configuration:** The exact input/output filter thresholds and classifier versions active during the call.

### 2. Inference Serving Mechanics (For Self-Hosted / Dedicated Models)
Running `model.generate()` in standard HuggingFace PyTorch in production will collapse under 5 concurrent users. Production serving requires purpose-built engines (`vLLM`, `TensorRT-LLM`, `SGLang`, `Text Generation Inference (TGI)`):
* **Continuous (In-Flight) Batching:** Instead of waiting for every request in a static batch of 16 to finish generating (where a 50-token answer sits idle waiting for a 1,000-token answer), the engine evicts finished sequences immediately at the token iteration level and inserts newly arrived requests into the active GPU batch.
* **PagedAttention:** Inspired by OS virtual memory paging, it splits the KV cache into non-contiguous memory blocks, eliminating internal and external GPU memory fragmentation and increasing concurrent throughput by 2x–4x.
* **Quantization (Post-Training Quantization):** Reducing weight precision from 16-bit floating point (`FP16`/`BF16`) to 8-bit (`FP8`/`INT8`) or 4-bit (`INT4` via `AWQ` or `GPTQ`).
  * *Rule of Thumb for VRAM Sizing:* At `FP16` (2 bytes per parameter), a 70B model requires \(70 \times 2 = 140\text{ GB}\) just for weights, plus 20%–40% overhead for CUDA kernels and the KV cache (\(\approx 170\text{–}190\text{ GB}\) VRAM, requiring at least \(3 \times 80\text{GB A100/H100 GPUs}\)). Quantizing to `INT4` (0.5 bytes per parameter) shrinks weights to \(\approx 35\text{ GB}\), allowing a 70B model to fit onto a single 48GB or 80GB GPU at the cost of a 1%–3% degradation on complex reasoning benchmarks.
* **Speculative Decoding:** Uses a tiny, fast "draft" model (e.g., 1B–3B) or draft heads to guess the next 5 tokens rapidly, and passes all 5 tokens to the massive 70B target model in a single parallel forward pass to verify/accept them. Gives 1.5x–2.5x latency speedup with **zero** mathematical change to output quality.
* **Prefix / KV Caching:** Keeps the computed KV cache tensors of shared prefixes (system prompts, long few-shot examples, shared legal documents) warm in GPU VRAM or host RAM across calls so the model skips the expensive prefill computation.

### 3. Cost Control and Gateway Architecture
An **AI Gateway** (e.g., LiteLLM, Portkey, Kong AI Gateway, custom proxy) sits between all internal microservices and the LLM endpoints to enforce:
1. **Model Routing & Cascading:** An ultra-fast classifier or small model evaluates query complexity first. Simple queries route to a cheap 8B model ($0.10/1M tokens); complex queries cascade up to a frontier model ($3.00–$15.00/1M tokens).
2. **Caching Layers:**
   * *Exact Match Cache:* Redis key-value lookup on `(prompt_hash, model, temperature=0)`. Zero latency, zero cost.
   * *Semantic Cache:* Embeds the user query and checks vector similarity (e.g., cosine similarity > 0.96) against previously answered queries. *Warning:* Dangerous for queries containing negations, dates, or user-specific context (`"What is my account balance?"` vs `"What is John's account balance?"` have high cosine similarity!).
   * *Provider Prompt Caching:* Structuring prompts so static content (system prompt, tool definitions, background corpus) is placed at the *very beginning* of the payload, unlocking 50%–90% input token discounts on providers like Anthropic, OpenAI, and Google.
3. **Token Budgets & Rate Limiting:** Hard caps on `max_completion_tokens`, per-user/per-tenant daily dollar quotas, and loop circuit-breakers (killing agentic execution if an agent calls a tool more than \(N\) times in a row).
4. **Asynchronous Batching:** Routing non-urgent workloads (overnight document tagging, evaluation runs, report generation) to Batch APIs for a flat 50% discount.

### 4. Production Monitoring and Observability (The Four Telemetry Pillars)
1. **System & Infrastructure Telemetry:**
   * TTFT (`p50`, `p95`, `p99`), TPOT (`p50`, `p95`, `p99`), End-to-End Latency.
   * HTTP error rates (`429 Too Many Requests`, `500/503 Provider Outage`, `400 Context Length Exceeded`).
   * Self-hosted GPU metrics: GPU Compute Utilization (%), GPU Memory / KV Cache Utilization (%), Pending Queue Depth.
2. **Token & Cost Telemetry:**
   * Input vs. Output vs. Reasoning token counts per request, tagged by `feature_id`, `tenant_id`, and `prompt_version`.
   * Cache hit rate (% of input tokens served from prefix/semantic cache).
   * Cost per successful business transaction (not just cost per API call—if an agent takes 8 calls and 2 retries to solve 1 ticket, measure cost per resolved ticket).
3. **Security & Guardrail Telemetry:**
   * Prompt injection / jailbreak trigger rates.
   * PII detection / redaction events (e.g., NRIC, phone numbers, credit cards stripped before hitting external APIs).
   * Schema validation failure rate and retry counts.
4. **Quality & Drift Telemetry:**
   * **Input Drift:** Shifting distributions in user query lengths, detected languages, topic clusters, or out-of-domain queries.
   * **Retrieval Drift (for RAG):** Average similarity score of top-k retrieved chunks dropping over time (indicating users are asking about new topics missing from the knowledge base).
   * **Implicit User Signals:** Thumbs up/down ratio, copy-to-clipboard events, user regeneration/retry rate, conversation abandonment rate, and human edit distance (how much a human operator edits an AI-drafted email before clicking send).

### 5. Rollback, Resilience, and Incident Response
* **Shadow Deployment (Dark Launching):** Incoming live production traffic is duplicated asynchronously to the new candidate model/prompt (`v2`). The user receives the response from `v1`, while `v2`'s outputs are logged and scored offline to prove superiority on live traffic without risking user impact.
* **Canary Rollout:** Route 1% -> 5% -> 25% -> 100% of live traffic to `v2`, with automated rollback triggers if `p99` latency, schema failure rate, or user retry rate crosses a threshold.
* **Multi-Provider Fallback (and Its Hidden Trap):** Configuring the AI Gateway to failover from Provider A (e.g., Anthropic) to Provider B (e.g., OpenAI or AWS Bedrock) if Provider A returns `5xx` or times out after 10 seconds.
  * *Critical LLMOps Rule:* **Prompts are not portable raw across model families.** A prompt tuned for Claude using XML tags (`<instructions>`) may fail formatting or tone constraints when blindly routed to GPT or Llama during an outage. If you configure an automated fallback model, you must maintain and test a **model-specific prompt template pair** (`prompt_v1_claude`, `prompt_v1_gpt`) in your registry.

### 6. Evaluation in Production (Online Evaluation)
Because you cannot afford the latency or cost of running heavy evaluation suites on 100% of live traffic synchronously:
* **Synchronous Guardrails (Inline, <50ms–200ms):** Run lightweight, deterministic checks (Regex, JSON Schema validation, keyword blocklists) and tiny encoder classifiers (for PII, toxicity, and prompt injection) before returning the output to the user.
* **Asynchronous Sampled Evaluation (Offline/Nearline):** Sample 1%–10% of production traces (plus 100% of traces where a user clicked "thumbs down" or triggered a fallback retry). Push them to an asynchronous background queue where a high-capability LLM-as-a-judge evaluates Faithfulness, Answer Relevance, and Policy Compliance.
* **The Continuous Data Flywheel:** Production failures caught by asynchronous evaluation are routed to a human annotation queue, corrected by a domain expert, and promoted into the **Golden Regression Evaluation Dataset** so the system never fails on that edge case again.

---

## 6. EVALUATION FUNDAMENTALS

Evaluation is the single highest-leverage skill in generative AI engineering. Without rigorous evaluation, every change to a prompt, chunking strategy, or model version is blind guesswork.

### Part A: Exhaustive Taxonomy of Evaluation Metrics

#### 1. Deterministic & Rule-Based Metrics (Zero-LLM Cost, 100% Reproducible)
* **Exact Match (EM):** Binary `1/0` score indicating whether the generated output matches the reference string character-for-character (after normalization). *Measures:* Closed-ended classification, multiple-choice Q&A, single-entity extraction.
* **Schema / Syntax Validity Rate:** Percentage of outputs that parse as valid JSON/YAML/SQL/Python AST and conform to a strict `Pydantic` or JSON Schema definition. *Measures:* Structural reliability for software integration.
* **Constraint Satisfaction (IFEval-style):** Deterministic checks for verifiable instructions: word count ranges, paragraph count, inclusion/exclusion of forbidden keywords, valid URL formatting. *Measures:* Strict instruction obedience.
* **Execution-Based Metrics (`Pass@k`):** Used for code and SQL generation. Runs the generated code against a suite of unit tests or executes the generated SQL against a sandbox database and compares the returned table rows. `Pass@k` measures the probability that at least one of \(k\) generated samples passes all unit tests.

#### 2. Lexical Overlap Metrics (Classical NLP — Cheap, Fast, Weak on Semantics)
* **BLEU (Bilingual Evaluation Understudy):** Measures **Precision** of n-gram overlap (1-gram to 4-gram) between generated text and reference translation, with a brevity penalty for overly short outputs. *Measures:* Surface phrasing similarity in machine translation. *Failure mode:* Penalizes valid synonyms and paraphrasing.
* **ROUGE (Recall-Oriented Understudy for Gisting Evaluation):**
  * `ROUGE-N`: Measures **Recall** of n-grams from the reference text appearing in the generated summary.
  * `ROUGE-L`: Measures the Longest Common Subsequence (LCS) to capture sentence-level word order.
  * *Failure mode:* A summary that copies key phrases verbatim from the source but inserts the word `"not"` (completely inverting the factual truth) will still achieve a near-perfect ROUGE score.
* **METEOR / chrF:** Improves on BLEU by incorporating stemming, synonym matching (`WordNet`), or character-level n-grams (critical for morphologically rich languages and code).
* **Levenshtein Edit Distance:** Minimum number of character insertions, deletions, or substitutions required to transform the model output into the human-edited final version. *Measures:* Real-world human effort saved in AI-assisted drafting workflows.

#### 3. Information-Theoretic & Logit-Level Metrics
* **Perplexity (PPL):** The exponentiated average negative log-likelihood of a token sequence:
  \[\text{PPL}(X) = \exp\left( -\frac{1}{N} \sum_{i=1}^{N} \log P(x_i \mid x_{<i}) \right)\]
  * *What it actually measures:* How "surprised" or uncertain a specific model is when predicting a text corpus using its own vocabulary.
  * *Why it is misused:* You **cannot** compare perplexity across two models that use different tokenizers (because the denominator \(N\) changes based on how words are split), and low perplexity on a test set does not mean a model follows instructions well—it only means the test set looks statistically similar to its training data.
* **Calibration / Expected Calibration Error (ECE):** Measures whether the model's token probability (`logprobs`) matches its true empirical accuracy (e.g., when the model assigns an 80% probability to class token `"A"`, is it actually correct 80% of the time?). RLHF post-training notoriously ruins calibration, making models overconfident even when wrong.

#### 4. Embedding & Semantic Similarity Metrics
* **BERTScore:** Computes cosine similarity between contextual token embeddings (from a pre-trained encoder like RoBERTa) of the generated text and reference text, outputting Semantic Precision, Recall, and F1. *Measures:* Paraphrase equivalence where wording differs but meaning aligns.
* **Cosine Similarity of Sentence Embeddings:** Embeds the full response and reference answer into vectors and takes their dot product. *Failure mode:* Embeddings often struggle with negation and fine-grained numeric differences (`"Pay $5,000 by Tuesday"` vs `"Pay $50,000 by Thursday"` have a 0.97 embedding similarity despite being a catastrophic business error).

#### 5. Core Generative Quality Metrics (Evaluated via Human Rubric or LLM-as-a-Judge)
1. **Accuracy / Factual Correctness:** Alignment of stated facts against an authoritative external ground-truth reference answer. (Requires a reference answer).
2. **Hallucination Rate & Faithfulness (Groundedness):**
   * *Intrinsic Hallucination (Contradiction):* The model generates claims that directly contradict the provided source context in the prompt.
   * *Extrinsic Hallucination (Fabrication):* The model generates claims that are not present in or verifiable from the provided source context (even if they happen to be true in the outside world, in strict enterprise RAG, ungrounded claims are scored as faithfulness failures).
   * *How Faithfulness is actually computed (e.g., RAGAS / Claim Decomposition):* Step 1: Decompose the generated answer into \(M\) atomic factual claims. Step 2: Verify each claim independently against the retrieved source context (`Supported = 1`, `Unsupported = 0`). Step 3:
     \[\text{Faithfulness} = \frac{\text{Number of Supported Claims}}{\text{Total Atomic Claims } (M)}\]
     \(\text{Hallucination Rate} = 1 - \text{Faithfulness}\).
3. **Coherence & Fluency:**
   * *Fluency:* Grammatical correctness, spelling, natural phrasing within a single sentence.
   * *Coherence:* Logical flow, structural organization, absence of self-contradiction, and valid coreference resolution across paragraphs or multi-turn dialogues.
4. **Relevance (Answer Relevance & Completeness):**
   * *Precision-oriented Relevance:* Does the response directly address the user's intent without rambling or injecting off-topic tangential noise?
   * *Recall-oriented Completeness:* If the user asked a 3-part question, did the model answer all 3 parts?
5. **Diversity:**
   * *Lexical Diversity (`Distinct-n` / `Self-BLEU`):* Ratio of unique n-grams to total n-grams across outputs, or how similar multiple generated outputs are to each other when sampling \(K\) responses for the same or different prompts.
   * *Semantic Diversity:* Variance in ideas, angles, or clusters produced across a set of generations (critical for brainstorming, synthetic data generation, and creative copywriting; collapse in diversity after RLHF is known as **Mode Collapse**).
6. **Novelty:**
   * *What it measures:* The degree to which generated outputs introduce new information, non-obvious combinations, or phrasing that does **not** simply regurgitate the user's input prompt (`Prompt Copy Rate`) or verbatim spans from the training/retrieval corpus (`Memorization / Plagiarism Overlap`).

#### 6. Task-Specific Metrics

| Task Archetype | Mandatory Task-Specific Metrics |
| :--- | :--- |
| **RAG (Retrieval Step)** | **Context Recall@K** (% of ground-truth facts present in top \(K\) retrieved chunks); **Context Precision@K** (signal-to-noise ratio of relevant vs. irrelevant chunks in top \(K\)); **MRR (Mean Reciprocal Rank)** (how high up the first relevant chunk sits); **NDCG@K (Normalized Discounted Cumulative Gain)** (graded relevance ranking quality). |
| **RAG (Generation Step)** | **Context Faithfulness** (no claims outside retrieved chunks); **Answer Relevance** (actually answers user query); **Citation Precision & Recall** (does citation `[1]` actually support the sentence it is attached to?). |
| **Classification & Extraction** | **Macro-F1 / Micro-F1 / Weighted-F1**, **Precision**, **Recall**, **PR-AUC** (critical for imbalanced classes like fraud or toxicity), **Entity-Level F1** (strict boundary + type match in NER). |
| **Summarization** | **Coverage / Information Recall** (% of key nuggets from source included); **Compression Ratio** (\(\text{Summary Tokens} / \text{Source Tokens}\)); **Extractiveness vs. Abstractiveness** (n-gram density copied verbatim vs. synthesized); **Factual Consistency** (SummaC / QAFactEval). |
| **Agentic & Tool-Use** | **Tool Selection Accuracy** (picked the right tool); **Argument Extraction Accuracy** (passed valid parameters matching user intent); **Trajectory Efficiency** (number of steps taken vs. optimal minimum steps); **Task Completion Rate** (end-to-end goal achieved in sandbox environment). |
| **Safety & Guardrails** | **Attack Success Rate (ASR)** (% of adversarial red-team prompts that bypass refusals); **False Refusal Rate (FRR)** (% of safe, benign user queries wrongly blocked as unsafe). |

---

### Part B: LLM-as-a-Judge — Biases and Mitigation Protocols

Using a frontier LLM to grade outputs at scale is standard practice, but raw LLM judges are systematically flawed unless engineered around six documented biases:

1. **Position Bias:** Judges consistently favor the first option (`Response A`) over the second option (`Response B`) in pairwise comparisons.
   * *Mitigation:* Always run pairwise comparisons twice with the order swapped (`(A, B)` and `(B, A)`). Only count a win if the judge picks the same response in both positions; otherwise mark as a Tie.
2. **Verbosity (Length) Bias:** Judges consistently give higher scores to longer, bulleted, more polite responses even when they contain fluff or subtle factual errors.
   * *Mitigation:* Use atomic claim-verification checklists rather than open-ended holistic grading, or control for length penalties in the rubric.
3. **Self-Enhancement (Narcissism) Bias:** Models favor outputs written by their own model family (e.g., GPT-4 prefers GPT-4's writing style; Claude prefers Claude's style) because those sequences have higher probability (lower perplexity) under their own weights.
   * *Mitigation:* Use an ensemble/panel of judges from different model families, or use deterministic/reference-guided rubrics that leave no room for stylistic preference.
4. **Numeric Scale Calibration Collapse:** Asking an LLM to "Rate this response from 1 to 10" or "1 to 100" yields noisy, uncalibrated clusters around `7`, `8`, and `85` with almost zero statistical reproducibility.
   * *Mitigation:* **Never use arbitrary 1–10 scales.** Decompose complex criteria into a set of **binary (`Pass / Fail`, `Yes / No`)** questions or a strict **3-point / 5-point anchored rubric** where every integer has an explicit, observable behavioral definition.
5. **Reasoning-After-Scoring Error:** If an LLM judge outputs the score *first* (`"Score: 5/5. Explanation: ..."`), autoregressive conditioning forces it to rationalize whatever number it picked on the first token.
   * *Mitigation:* Force the JSON schema to output the `"chain_of_thought_critique"` field **before** the `"final_score"` field so the score token attends to the completed critique.
6. **Unvalidated Judge Drift:** Trusting an LLM judge without verifying that it agrees with human domain experts.
   * *Mitigation:* Before trusting an automated judge, have human domain experts grade 100–200 examples, run the LLM judge on the same 100–200 examples, and compute inter-annotator agreement (**Cohen's Kappa \(\kappa > 0.70\)** for binary/categorical or **Spearman Rank Correlation \(\rho > 0.80\)**).

---

### Part C: How to Build a Production Evaluation Set ("Golden Dataset")

1. **Stratified Composition (What must be inside):**
   * **50% Representative Production / Typical Cases:** Real (anonymized) user queries covering the primary happy-path tasks, weighted by actual business frequency.
   * **30% Hard Edge Cases & Boundary Conditions:** Ambiguous queries, multi-part questions, missing context in RAG (where the correct answer is `"I do not have enough information in the provided documents"`), extremely long inputs, malformed inputs, typos, and regional linguistic quirks (e.g., Singlish code-switching: *"Can claim CPF for wisdom tooth at private clinic anot?"*).
   * **20% Adversarial, Out-of-Scope, and Safety Cases:** Prompt injections (`"Ignore previous instructions..."`), requests for competitor comparisons, emotional/angry users, PII extraction attempts, and off-topic queries the bot must politely decline.
2. **Minimum Viable Sample Sizes:**
   * *Smoke Test Set (CI/CD per commit):* 30–50 cases (runs in <60 seconds on every prompt edit).
   * *Statistical Release Gate Set:* 200–500+ stratified cases across categories. (At \(N=30\), a single random flip changes your score by 3.3%; at \(N=400\), the 95% confidence interval margin of error drops below \(\pm 5\%\)).
3. **Cold-Start Bootstrapping (When you have zero production logs):**
   * Gather source documents (e.g., 100 company policy PDFs).
   * Use an LLM to generate synthetic question-answer pairs at varying difficulty levels (single-hop fact lookup, multi-hop synthesis across two sections, unanswerable trap questions).
   * **Mandatory Step:** Have human domain experts review, filter, and rewrite those synthetic examples. Never evaluate a model solely on unverified synthetic data generated by the same model.
4. **Dataset Hygiene & Maintenance:**
   * Version the eval set alongside code (`eval_dataset_v1.4.parquet`).
   * Never leak evaluation examples into your few-shot prompts or fine-tuning training split.
   * Retire saturated test cases and add new production failure traces weekly.

---

### Part D: Why a Single Aggregate Score Always Misleads

Reporting *"Model A scored 88% overall"* is professional malpractice in AI evaluation for five mathematical reasons:

1. **Simpsons Paradox & Subgroup Masking:** A model can achieve 92% average accuracy across a 1,000-query test set because it scores 97% on the 900 easy FAQ questions while scoring **47%** on the 100 high-stakes regulatory/refund calculations. The aggregate score hides catastrophic failure on the highest-risk slice.
2. **Metric Orthogonality (Anti-Correlated Trade-offs):** You can achieve a **0% Hallucination Rate** and **100% Safety Score** tomorrow by programming your model to respond `"I cannot answer that"` to every single user query. Its Relevance and Helpfulness will drop to 0%. If you average Faithfulness (`100%`) and Relevance (`0%`) into a single score (`50%`), you cannot distinguish a broken refusal bot from a mediocre chatbot.
3. **Variance vs. Central Tendency (`Mean` vs. `Tail Risk / p99`):** In customer-facing enterprise applications, users remember the 1% worst outputs, not the average output. Model A (mean score `4.2/5`, zero toxic/dangerous failures) is vastly superior for production than Model B (mean score `4.4/5`, but hallucinates fake legal advice in 3% of cases).
4. **Quality-Latency-Cost Pareto Frontier:** An accuracy score of 91% is meaningless without knowing whether it took 400ms at $0.0002/query or 45 seconds at $0.18/query. Evaluation must always be plotted as a multi-dimensional Pareto frontier (`Quality vs. Latency vs. Cost`).
5. **Statistical Noise Floor:** Because LLM sampling and LLM-as-a-judge grading both have inherent variance, an aggregate score change from `84.2%` to `85.6%` on a 100-item dataset is statistically indistinguishable from random noise without bootstrap confidence intervals or paired permutation tests.

---

## 7. BENCHMARKS AND LEADERBOARDS

### 1. Major Public Benchmarks: What They Measure vs. What They Hide

| Benchmark | What It Actually Measures | Why It saturates or Misleads in Enterprise Contexts |
| :--- | :--- | :--- |
| **MMLU / MMLU-Pro** (Massive Multitask Language Understanding) | Multiple-choice (`A/B/C/D` or `A–J`) academic exam questions across 57 subjects (high school to professional level). | Tests passive recognition of static textbook knowledge, not open-ended generation, tool use, or enterprise workflow execution. Heavily contaminated in pre-training corpora; original MMLU has ~6.5% label errors in its ground truth. |
| **GPQA (Diamond)** | PhD-level multiple-choice questions in biology, physics, and chemistry designed so non-experts cannot easily Google the answers. | Good signal for deep scientific reasoning, zero signal for whether a model can summarize a Singlish customer complaint or follow a 10-field JSON schema. |
| **GSM8K & MATH** | Grade-school word problems (`GSM8K`) and high-school competition math (`MATH`). | Heavily overfitted by model labs training specifically on synthetic GSM8K variants. Models scoring >95% on GSM8K frequently collapse when numbers in the exact same problem are changed or irrelevant distractor sentences are added (`GSM-Symbolic`). |
| **HumanEval & MBPP** | Generating standalone Python functions from docstrings, graded by unit test execution (`Pass@1`). | Tests tiny, self-contained algorithmic puzzles (LeetCode style). Hides real-world software engineering complexity. |
| **SWE-bench (Verified)** | Resolving real GitHub issues across multi-file Python repositories requiring code navigation, patching, and passing repository test suites. | Much closer to real engineering utility, though scores depend heavily on the external agent scaffolding (bash tools, retry loops) wrapped around the model, not just the raw model weights. |
| **IFEval** (Instruction Following Evaluation) | Strict adherence to deterministic, verifiable formatting constraints ("Write 3 paragraphs, do not use the letter 'e', wrap title in `<< >>`"). | High practical relevance for prompt engineers, because it tests obedience rather than world knowledge—though some labs now explicitly train on IFEval constraint templates. |
| **MT-Bench & Arena-Hard-Auto** | Multi-turn conversational quality graded by an LLM judge (usually GPT-4). | Suffers from the exact biases of the LLM judge (verbosity bias, stylistic preference for markdown headers and bullet lists). |
| **LMSYS Chatbot Arena** | Blind, randomized `A/B` pairwise human preference voting (Elo rating) on live user prompts from the public internet. | The gold standard for general "vibe" and human chat preference, but subject to **style bias** (humans vote for longer, nicely formatted markdown answers even when factually wrong—isolated by **Style-Controlled Arena**) and dominated by single-turn English hobbyist/coding queries rather than enterprise RAG workloads. |
| **RULER & LongBench** (vs. Simple Needle-in-a-Haystack / NIAH) | Multi-needle retrieval, aggregation, and variable tracking across 32k to 1M token contexts. | Simple "Needle-in-a-Haystack" (finding one random sentence about pizza inside essays) is trivially easy (~100% green heatmaps). `RULER` reveals that when models must aggregate *multiple* facts scattered across 128k tokens, effective context often collapses at 32k–64k tokens. |
| **BFCL** (Berkeley Function Calling Leaderboard) | AST verification and live execution accuracy of single-turn, multi-turn, and parallel function/tool calls across Python, Java, JS, and REST APIs. | One of the most practically useful benchmarks for agent builders, though public schemas are cleaner than messy legacy enterprise APIs. |
| **BHASA / SeaBench / SeaExam** | Southeast Asian linguistic, cultural, and reasoning benchmarks covering Bahasa Indonesia, Bahasa Melayu, Tamil, Chinese, Thai, Vietnamese, and regional contexts. | Essential for ASEAN deployments. Global leaderboards (MMLU/Arena) are >90% English-centric and completely hide catastrophic performance drops on ASEAN languages and local cultural knowledge. |

### 2. Data Contamination (Benchmark Leakage)
* **How it happens:**
  1. *Accidental Web Crawl Leakage:* Public benchmark test sets sit on GitHub, HuggingFace, ArXiv PDFs, and blog posts. When pre-training scrapes the common crawl, the test questions and answers end up in the training data.
  2. *Synthetic Paraphrase Contamination:* Labs generate synthetic training data by asking an existing frontier model to create variations of benchmark problems, leaking the underlying logic and answer patterns into post-training SFT sets.
  3. *Human Evaluation Feedback Loops:* Public prompts from Arena or benchmark discussions get logged via free chat interfaces and folded into the next RLHF cycle.
* **How to detect it:**
  * Compare score on static public benchmarks against dynamically refreshed, time-gated benchmarks (e.g., **LiveBench**, **LiveCodeBench**, which pull new problems published *after* the model's knowledge cutoff date). If a model scores 92% on static HumanEval but drops to 45% on problems posted on Codeforces last month, it memorized the benchmark.
  * Check token log-probabilities or prompt completion: give the model the first half of a benchmark question and see if it autocompletes the exact verbatim second half and multiple-choice options.

### 3. Benchmark Gaming and Goodhart's Law
*"When a measure becomes a target, it ceases to be a good measure."* Model providers game leaderboards via:
* **Style Overfitting for Arena Elo:** Fine-tuning models to always output bolded headers, numbered lists, enthusiastic openings, and lengthy explanations because crowd-raters and GPT-4 judges reward visual structure over brevity and factual accuracy.
* **Benchmark-Specific System Prompts & Hyperparameters:** Running 50 different prompt variations on MMLU and reporting the highest score, or comparing their model's `5-shot Chain-of-Thought` score against a competitor's `0-shot` score in marketing bar charts.
* **Train-on-Test SFT:** Mixing validation splits or direct paraphrases of GSM8K, MATH, and HumanEval directly into the supervised fine-tuning mix.

### 4. Five Reasons Leaderboard Rank \(\neq\) "Best for My Task"
1. **Distribution Mismatch:** Public benchmarks test general knowledge across 50 domains. Your enterprise task requires 99.5% reliability on *one* narrow workflow (e.g., parsing Singpass/MyInfo JSON payloads and cross-checking against CPF contribution tables).
2. **Missing Operational Constraints:** Leaderboards rank by unconstrained quality score. They ignore whether Model #1 costs 30x more, has a 12-second TTFT, lacks a regional data residency endpoint in Singapore, or has an restrictive non-commercial license.
3. **Prompt Sensitivity & Brittleness:** Model A might beat Model B on a benchmark using the benchmark's default prompt template, while failing completely on your system's complex XML/JSON instruction format.
4. **Refusal & Safety Miscalibration:** A model high on an academic leaderboard may have overly aggressive safety filters that refuse to process legitimate clinical reports, insurance claims containing injury descriptions, or cybersecurity logs.
5. **Multilingual & Local Context Blindness:** A top-3 global model trained 95% on English and Chinese web text may perform worse on Bahasa Melayu, Tamil, or Singapore civil service terminology than a smaller regionally fine-tuned model (such as AI Singapore's `SEA-LION` or Sailor variants).

---

## 8. FAIRNESS, BIAS AND EXPLAINABILITY IN EVALUATION

### Part A: How Bias Manifests in Generative AI
Unlike traditional tabular ML (where bias is simply an unequal false-positive or approval rate across a demographic column), generative AI exhibits four distinct layers of bias:
1. **Allocational Harms (Decision Bias):** When an LLM is used to screen resumes, score credit memos, triage patients, or route customer service priority, and it systematically assigns higher scores or better outcomes to one demographic group based on explicit markers or implicit proxies (names, schools, postal codes, dialects).
2. **Representational Harms (Stereotyping & Erasure):**
   * *Stereotyping:* Associating specific genders, races, nationalities, or religions with fixed roles or negative traits (e.g., always generating male pronouns for doctors/engineers, or associating certain ethnic groups with lower socioeconomic roles).
   * *Erasure / Homogeneous Defaulting:* Assuming a Western/US default for all cultural, legal, dietary, or social norms unless explicitly forced otherwise.
3. **Linguistic and Dialectal Bias (Performance Disparity):** Delivering accurate, polite, high-reasoning responses to users writing in Standard British/American English, while delivering degraded, condescending, or higher-error-rate responses to users writing in Singlish, regional dialects, or non-native English grammar.
4. **Perspective & Ideological Bias:** Presenting one culturally specific moral or political viewpoint as universal objective fact on contested topics.

### Part B: How to Detect and Measure Bias Quantitatively

1. **Counterfactual Pairwise Perturbation Testing (The Gold Standard for Enterprise Apps):**
   * Take 200 real task prompts (e.g., resume evaluations, loan application summaries, customer complaint escalations).
   * Hold 100% of the factual merits identical, and programmatically swap **only** demographic identifiers or proxies across perturbation dimensions (e.g., Chinese / Malay / Indian / Western names; Male / Female / Non-binary pronouns; standard English vs. Singlish phrasing; age brackets; religion/dietary markers).
   * **Metrics to Compute:**
     * *Outcome Flip Rate:* Percentage of cases where swapping only the demographic marker flips the binary decision or recommendation.
     * *Score Distribution Shift:* Mann-Whitney U test or Kolmogorov-Smirnov test on numeric ratings across demographic buckets (target: statistically indistinguishable distributions, \(p > 0.05\)).
     * *Sentiment / Tone Regard Differential:* Measuring whether the model uses warmer, more respectful phrasing for Group A vs. Group B using a `Regard` or politeness classifier.
2. **Disaggregated Subgroup Performance Auditing:**
   * Slice every primary evaluation metric (Faithfulness, Accuracy, Latency, Token Cost, False Refusal Rate) across language and user segments (`English`, `Mandarin`, `Bahasa Melayu`, `Tamil`, `Code-Switched Singlish`).
   * *Metric:* **Max-Min Subgroup Performance Gap** (e.g., if English accuracy is 94% and Tamil accuracy is 61%, the 33-point disparity must be surfaced explicitly rather than buried in a 90% weighted average).
3. **Standard Academic & Regulatory Bias Benchmarks (and Their Limits):**
   * **BBQ (Bias Benchmark for QA):** Tests whether models fall back on social stereotypes when given ambiguous context (`"An old person and a young person walked into a tech store; one of them was confused by the smartphone. Who was confused?"` — correct answer is `"Cannot be determined"`).
   * **WinoBias / Winogender:** Tests occupational gender coreference resolution (`"The physician hired the secretary because he/she..."`).
   * **BOLD / RealToxicityPrompts:** Measures sentiment, regard, and toxicity disparities across open-ended text completions about different demographic groups.
   * **Singapore AI Verify / Project Moonshot:** IMDA's open-source testing toolkits (`Project Moonshot`) provide standardized red-teaming and bias evaluation modules tailored for ASEAN and enterprise governance compliance.

---

### Part C: Explainability in LLMs — What It CAN and CANNOT Deliver

Practitioners and regulators frequently transfer "Explainable AI (XAI)" expectations from tabular ML (like `SHAP` or `LIME` on an XGBoost credit model) directly onto 70-billion-parameter Transformers. Trainers must draw an uncompromising line between what is scientifically true and what is an illusion.

#### 1. What Explainability CANNOT Deliver (And Why)
* **Chain-of-Thought (CoT) is NOT a Faithful Explanation of Internal Computation:**
  * *The Trap:* Learners believe that asking an LLM `"Explain your step-by-step reasoning for why you rejected this claim"` reveals how the neural network arrived at the decision.
  * *The Reality (Post-Hoc Rationalization):* Research (e.g., Anthropic's studies on *Unfaithful Chain-of-Thought*) proves that if you inject a subtle biasing cue into a prompt, the model will change its answer to match the bias while generating a plausible-sounding, completely fabricated logical explanation that never mentions the biasing cue. CoT is just more generated text conditioned on the prompt—it is a **plausible justification**, not an audit log of weight activations.
* **No Feature-Importance Formula (`SHAP`/`LIME` Collapse):** In a 10-feature random forest, you can prove mathematically that `Income` contributed `+35%` to the loan approval. In a 70B LLM operating over 4,000 natural language tokens across 80 layers of non-linear self-attention, individual tokens interact combinatorially. Perturbing single words (token-level LIME/SHAP) breaks grammatical structure and is computationally intractable for long contexts.
* **Attention Weights \(\neq\) Causal Explanation:** Looking at which tokens have high attention weights in Layer 12 does not tell you *why* the final decision was made, because information is mixed across residual streams, MLP layers, and 64+ attention heads per layer.

#### 2. What Explainability CAN Deliver (And What Enterprises Should Actually Build)
1. **Source Attribution & Grounded Citations (The Practical Enterprise Standard):**
   * While you cannot explain why 70 billion weights fired, you **can** force a RAG or tool-use system to cite the exact document ID, paragraph, and verbatim quote it used to construct every factual claim, and verify that citation programmatically via an NLI (Natural Language Inference) faithfulness check.
2. **Auditability of the Workflow Trajectory (Deterministic Scaffolding):**
   * Decompose high-stakes decisions out of a single monolithic black-box prompt. Use the LLM *only* to extract structured facts from unstructured documents (with verifiable quotes), and feed those extracted JSON fields into a **deterministic, auditable rules engine** or traditional explainable ML model (`XGBoost` + `SHAP`) to make the final financial, medical, or legal decision.
3. **Logprobs & Token-Level Confidence Inspection:**
   * Inspecting top-5 token log-probabilities (`logprobs`) on classification or extraction outputs reveals whether the model was genuinely certain (`P("Approve") = 0.994`) or guessing on a coin flip (`P("Approve") = 0.51`, `P("Reject") = 0.49`).
4. **Mechanistic Interpretability (Sparse Autoencoders / SAEs & Probing — Frontier Research):**
   * Decomposing polysemantic neurons into monosemantic "features" (e.g., Anthropic's Golden Gate Claude research) to inspect or steer internal concepts. *Honest assessment for trainers:* While scientifically groundbreaking, Mechanistic Interpretability is currently a laboratory research tool for frontier model labs, **not** an off-the-shelf production explainability tool for enterprise developers.

---

## 9. TERMINOLOGY GLOSSARY AND COMMON MISCONCEPTIONS

### Part A: Mandatory Trainer Glossary (One-Line Precision Definitions)

#### Architecture & Core Mechanics
1. **Token:** The fundamental atomic unit of text (a word, sub-word, character, or byte) mapped to an integer ID by a model's vocabulary.
2. **Logits:** The raw, unnormalized numeric scores emitted by the final layer of a neural network across every token in its vocabulary before being converted to probabilities.
3. **Softmax:** The mathematical function that normalizes a vector of raw logits into a probability distribution where all values fall between 0 and 1 and sum to 1.0.
4. **Self-Attention:** The Transformer mechanism that computes pairwise relevance scores between every token in a sequence so each token's representation incorporates context from surrounding tokens.
5. **KV Cache (Key-Value Cache):** Dedicated GPU memory that stores previously computed attention Key and Value tensors so autoregressive generation does not recompute past tokens at every step.
6. **Prefill Phase:** The parallel, compute-bound first step of inference that processes all input prompt tokens simultaneously to populate the KV cache and emit the first output token.
7. **Decode Phase:** The sequential, memory-bandwidth-bound phase of inference that generates output tokens one by one using the populated KV cache.
8. **Mixture-of-Experts (MoE):** A neural architecture where feed-forward layers are split into multiple specialized sub-networks ("experts") and a router activates only a small subset per token, decoupling total parameter memory from per-token compute cost.
9. **Context Window:** The hard maximum sum of input tokens and generated output tokens a model can attend to in a single inference call.
10. **Embeddings:** Dense vectors of floating-point numbers representing the semantic meaning of text, images, or audio in a multi-dimensional geometric space.

#### Training & Adaptation
11. **Pre-training:** The initial self-supervised training phase over trillions of raw tokens where a model learns grammar, facts, and reasoning by predicting the next token.
12. **Base Model (Foundation Checkpoint):** A pre-trained model that has only learned next-token document continuation and has not yet been trained to follow instructions or act as a chat assistant.
13. **Supervised Fine-Tuning (SFT):** Training a base model on curated `(instruction, ideal_response)` examples to teach it instruction-following behavior, formatting, and domain conventions.
14. **RLHF (Reinforcement Learning from Human Feedback):** A post-training alignment technique that trains a reward model on human preference rankings and uses reinforcement learning (e.g., PPO) to steer the LLM toward helpful, safe outputs.
15. **DPO (Direct Preference Optimization):** A mathematically simpler alternative to RLHF that aligns model weights directly on `(prompt, winning_response, losing_response)` triples without training a separate reward model.
16. **LoRA (Low-Rank Adaptation):** A parameter-efficient fine-tuning (PEFT) method that freezes the original model weights and trains small, rank-decomposed adapter matrices, cutting training VRAM by >70%.
17. **QLoRA:** A memory-optimized variant of LoRA that quantizes the frozen base model to 4-bit precision while backpropagating gradients through 16-bit LoRA adapters.
18. **Catastrophic Forgetting:** The degradation of a model's general reasoning or previously learned capabilities after aggressive fine-tuning on a narrow dataset.
19. **Model Distillation:** Training a smaller, cheaper "student" model on the outputs (or logit distributions) generated by a larger, more capable "teacher" model.
20. **RAG (Retrieval-Augmented Generation):** An architecture that retrieves relevant chunks from an external search index at query time and injects them into the model prompt to ground the response in verifiable data.
21. **Cross-Encoder Reranker:** A secondary encoder model in a RAG pipeline that scores the exact relevance of each retrieved document chunk jointly with the user query to reorder results before passing the top chunks to the LLM.

#### Sampling & Inference Serving
22. **Temperature:** A hyperparameter that scales logits before `Softmax` to control the randomness of token sampling (`0` = deterministic greedy decoding; higher = flatter distribution / more randomness).
23. **Top-p (Nucleus Sampling):** A dynamic sampling filter that restricts token selection to the smallest set of top-ranked tokens whose cumulative probability exceeds threshold \(p\).
24. **Constrained Decoding (Structured Outputs):** Masking invalid token logits to `0` at inference time using a grammar or state machine so the output is guaranteed to match a required JSON Schema or Regex.
25. **Quantization:** Compressing model weights and/or activations from high-precision floating-point formats (`FP16`/`BF16`) into lower-bit representations (`FP8`, `INT8`, `INT4`) to reduce GPU VRAM and accelerate inference.
26. **Continuous Batching:** An inference-serving technique that dynamically inserts new requests and evicts finished sequences from an active GPU batch at every single token generation step.
27. **PagedAttention:** A memory-management algorithm (pioneered by `vLLM`) that stores the KV cache in non-contiguous virtual memory blocks to eliminate GPU VRAM fragmentation.
28. **Speculative Decoding:** An inference acceleration method where a tiny draft model rapidly proposes multiple candidate tokens that the large target model verifies in parallel in a single forward pass.
29. **TTFT (Time to First Token):** The elapsed time in milliseconds from sending an API request to receiving the first generated output token.
30. **TPOT (Time Per Output Token) / ITL (Inter-Token Latency):** The average time in milliseconds required to generate each subsequent output token after the first token arrives.

#### Evaluation & Safety
31. **Perplexity:** An exponentiated cross-entropy metric measuring how uncertain a language model is when predicting a sequence of tokens under its own tokenizer.
32. **Faithfulness (Groundedness):** The percentage of factual claims in a model's output that can be directly inferred from and verified against the provided source context.
33. **Sycophancy:** An RLHF-induced failure mode where a model abandons factual truth to flatter or agree with a user's stated opinion or false premise.
34. **Data Contamination:** The presence of benchmark evaluation test questions or their close paraphrases inside a model's pre-training or fine-tuning dataset, artificially inflating benchmark scores.
35. **Prompt Injection:** An adversarial attack where untrusted user input or retrieved external data overrides the developer's system instructions to hijack model behavior.

---

### Part B: Common Learner Misconceptions and Exact Trainer Corrections

1. **Learner says:** *"We need to fine-tune the model on our company PDFs so it knows our internal policies."*
   * **Trainer correction:** Fine-tuning teaches **behavior, style, and formatting**, not dynamic document libraries. If you fine-tune on PDFs, the model will hallucinate blended policies, cannot cite page numbers, and must be retrained every time a policy changes. Use **RAG** to teach a model new facts; use **Fine-Tuning** to teach it a new skill or output format.

2. **Learner says:** *"Setting `temperature = 0` guarantees the LLM will give the exact same output 100% of the time."*
   * **Trainer correction:** `temperature = 0` selects the highest-probability token (greedy decoding), which *maximizes* consistency, but GPU floating-point math is non-associative across dynamic batch sizes and Mixture-of-Experts routing. Small floating-point rounding differences can flip two tied tokens, causing the rest of the autoregressive sequence to diverge even at `temperature = 0` and with a fixed `seed`.

3. **Learner says:** *"This new model has a 1-million-token context window, so RAG is dead—we can just dump our entire database into the prompt."*
   * **Trainer correction:** A 1M context window only means the API won't crash. Stuffing 500,000 tokens into every call causes massive latency (10–30 second TTFT), multiplies per-query cost by 50x, and suffers from the **"Lost in the Middle"** phenomenon where reasoning accuracy over facts buried in the middle of a massive context degrades sharply.

4. **Learner says:** *"Model X is #1 on the LMSYS Chatbot Arena and MMLU leaderboards, so we should pick it for our project."*
   * **Trainer correction:** Public leaderboards measure average performance on generic English trivia, math puzzles, and human style preference. They tell you nothing about whether Model X obeys your 15-field JSON schema, understands Singapore regulatory terms, meets your 500ms latency SLA, or fits your token budget. The best model is the one that wins on **your private evaluation set** along the quality-cost-latency frontier.

5. **Learner says:** *"Our evaluation shows the model got 90% ROUGE / Cosine Similarity against the reference answer, so it is factually accurate."*
   * **Trainer correction:** Lexical overlap (`ROUGE`) and embedding similarity are terrible at detecting negation and numeric errors. The sentences `"You are eligible for a $10,000 grant"` and `"You are not eligible for a $10,000 grant"` have >90% ROUGE overlap and >0.96 cosine similarity, yet one is the exact opposite of the truth. Factual verification requires atomic claim decomposition and NLI/LLM-judge faithfulness checks.

6. **Learner says:** *"If we want to know why the AI made a decision, we just ask it to explain its Chain-of-Thought step by step."*
   * **Trainer correction:** Chain-of-Thought improves reasoning accuracy by giving the model intermediate "scratchpad" tokens, but it is **not** a faithful readout of internal neural weights. Models routinely produce post-hoc rationalizations—plausible-sounding stories that justify an answer driven by hidden biases. True enterprise auditability requires verifiable citations to source text and deterministic rules engines for high-stakes logic.

7. **Learner says:** *"Open-source models like Llama are completely free, whereas commercial APIs cost money."*
   * **Trainer correction:** Open-weight models have $0 licensing fees (subject to usage caps), but hosting a 70B model requires dedicated multi-GPU cloud instances costing $3,000–$15,000+ per month 24/7 regardless of whether anyone sends a query, plus MLOps engineering salaries. At low-to-medium traffic or spiky daytime traffic, pay-per-token commercial APIs are almost always cheaper than self-hosted GPUs.

8. **Learner says:** *"Using an LLM-as-a-judge to rate responses from 1 to 10 gives us an objective, automated score."*
   * **Trainer correction:** Uncalibrated 1–10 LLM-as-a-judge prompts simply clusters guesses around `7` and `8` while suffering from position bias, verbosity bias, and self-preference bias. Automated judges are only reliable when restricted to binary (`Pass/Fail`) or strictly anchored 3–5 point rubrics, forced to write their critique *before* emitting the score, and validated against human domain experts (`Cohen's Kappa > 0.70`).

---

## 10. BEST PRACTICES AND TEACHING ANGLES

### Part A: The Proven 10-Step Production Workflow for Choosing, Evaluating, and Deploying a Model

Trainers should teach learners to execute this exact chronological sequence on every generative AI project:

1. **Step 1: Define Hard Non-Negotiable Constraints First (The Filter Gate)**
   * Before looking at a single benchmark, write down the immovable boundaries: Data classification & residency (Can data leave Singapore? Can it hit a public SaaS API with Zero Data Retention, or must it stay on-prem/GovTech GCC?), Modality (Text, Vision, Audio), Latency SLA (`TTFT < 1s`?), and Maximum Unit Cost per transaction (e.g., `< $0.01 per resolved ticket`). Eliminate 80% of models immediately.
2. **Step 2: Build the Minimum Viable Golden Dataset (`N = 50` to `100` to start)**
   * Collect or curate 50 representative real inputs, 30 nasty edge cases (Singlish, typos, multi-part queries, missing RAG context), and 20 adversarial/out-of-scope prompts. Have a human domain expert write or verify the expected behavior for each.
3. **Step 3: Design the Multi-Metric Evaluation Harness (Code First, Then LLM Judges)**
   * Write deterministic programmatic checks first (JSON schema validator, regex, length bounds, citation existence check).
   * Add decomposed binary (`Pass/Fail`) LLM-as-a-judge rubrics for semantic quality (Faithfulness, Answer Relevance).
   * Validate your LLM judge against 50 human-graded outputs to confirm >80% agreement before trusting the automation.
4. **Step 4: Establish the "Ceiling Baseline" with a Frontier Model + Prompting**
   * Take the smartest available model within your compliance boundary (e.g., Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro) and iterate on **plain prompting + few-shot examples** until you hit maximum possible quality on your Golden Dataset.
   * *Why:* This proves whether the task is solvable at all and gives you an upper-bound quality benchmark.
5. **Step 5: Add RAG Only When Knowledge is External or Dynamic**
   * If errors in Step 4 are caused by missing private facts, introduce RAG. Evaluate **Retrieval** (`Context Recall@K`, `Precision@K`) completely separately from **Generation** (`Faithfulness`). Do not blame the LLM if the retriever fetched the wrong PDF page.
6. **Step 6: Run the Pareto Model Selection Shootout (Quality vs. Cost vs. Latency)**
   * Run your exact evaluation harness across 3–5 candidate models spanning size tiers (e.g., Frontier model vs. Mid-tier API model vs. Small 8B/14B open-weight model like Qwen 2.5 / Llama 3.1 / SEA-LION).
   * *Note:* Adapt the prompt template minimally to each model family's native format so you are testing the model fairly. Plot the results on a 3-axis chart (`Pass Rate %`, `p95 Latency`, `Cost per 1,000 calls`).
7. **Step 7: Optimize via Cascading or Fine-Tuning (If Needed)**
   * If the frontier model meets the quality bar but breaks the cost or latency budget, use the frontier model to generate 2,000–5,000 verified outputs and **LoRA fine-tune (distill)** a small 8B model to match the frontier model's accuracy on that narrow task at 1/15th the cost.
8. **Step 8: Conduct Pre-Launch Fairness, Bias, and Red-Team Auditing**
   * Run counterfactual demographic/dialect perturbation tests (e.g., swapping names and Standard English vs. Singlish phrasing) and adversarial prompt-injection test suites (`Project Moonshot`). Verify that False Refusal Rates on benign queries remain below 2%.
9. **Step 9: Deploy Behind an AI Gateway with Pinned Versions and Guardrails**
   * Pin exact dated model snapshots. Route through an AI gateway with prefix caching, token budget caps, inline PII redaction, and model-specific fallback prompt templates. Roll out via Shadow Deployment -> 5% Canary -> 100% Production.
10. **Step 10: Close the Production Flywheel**
    * Asynchronously sample 5% of live traffic and 100% of negative-feedback traces for automated LLM-judge grading. Promote every newly discovered production failure into the Golden Dataset and trigger automated regression tests in CI/CD before any future prompt or model update goes live.

---

### Part B: Pedagogical Analogies & Mental Models for Non-Engineering Adult Learners (Singapore Context)

When teaching product managers, policy officers, finance leads, or operations executives in Singapore, use these concrete mental models to replace abstract math:

| Technical Concept | The Non-Technical Mental Model (Singapore Footing) | Why the Analogy Works Pedagogically |
| :--- | :--- | :--- |
| **Pre-training vs. Fine-Tuning vs. RAG** | **Hiring a Fresh NUS/NTU Graduate:**<br>• **Pre-training** is their 16 years of general education—they can read, write, and reason, but don't know your company.<br>• **Fine-Tuning** is a 3-month intensive corporate bootcamp that trains them to speak in your company's exact tone and fill out your specific forms from memory.<br>• **RAG** is giving them an open-book SOP manual and access to the company intranet on their desk so they look up the exact policy page and cite it before answering a customer. | Instantly stops executives from asking to "fine-tune the model on daily PDFs." Anyone who has managed staff knows you don't send an employee to a 3-month memory bootcamp every time HR updates the annual leave policy—you update the open-book intranet (RAG). |
| **Model Size & Cascading (Frontier vs. SLM)** | **Singapore Healthcare Triage (Polyclinic GP vs. SGH Senior Consultant Specialist):**<br>You don't send every person with a common cold straight to a Senior Neurosurgeon at SGH ($300/visit, 3-month wait). A fast, cost-effective Polyclinic GP (Small 8B Model) handles 80% of routine cases in 5 minutes,