---
id: 04.03.A.K2
tsc: 4
level: Advanced
code: K2
title: Architectures, training strategies, and optimisation
as_at: 2026-11-26
review_by: 2027-02-25
---

# Architectures, training strategies, and optimisation

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K2**

> **Framework text (verbatim):** "Concepts in generative AI, including model architectures, training strategies, and optimisation techniques (including pre-training vs fine-tuning for specialised tasks or domains)."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Knowledge · Bullet 2 of 8

**One-line version:** Pre-training buys general competence at enormous cost; fine-tuning buys a narrow behaviour at modest cost; optimisation is how you make either one affordable to run.

## What it is

Three decisions hide inside this bullet. **Architecture** is the shape of the network — how it reads text, how many parameters it has, whether every parameter fires for every token. **Training strategy** is the sequence of stages that turns raw text into a usable assistant: pre-training, instruction tuning, preference alignment, sometimes reasoning training. **Optimisation** is everything done afterwards to make the result cheaper, smaller or faster without giving back the quality you need.

## Deep expansion

### The concept

Pre-training is self-supervised next-token prediction over trillions of tokens of web text, code and books. Nobody labels it; the text labels itself. The output is a **base model**, which knows a great deal about language and the world but only knows how to *continue a document*. Ask a base model "What is the capital of France?" and it may answer "What is the capital of Germany? What is the capital of Spain?" — it has decided you are writing a quiz.

Fine-tuning starts from that base and continues training on a much smaller, curated dataset. Its purpose is not to add knowledge but to shape **behaviour**: formatting, tone, refusals, adherence to a schema, a house style. That distinction is the load-bearing idea of the whole bullet. Pre-training supplies capability; fine-tuning supplies conduct.

The cost asymmetry is severe: pre-training is a data-centre-scale project measured in weeks and millions; fine-tuning a small adapter on a few thousand examples is an afternoon on one GPU. Choosing pre-training for an enterprise task is almost always a category error.

### The sub-concepts

**Encoder, decoder, and both.** Encoder-only models (the BERT family, embedding models) read bidirectionally and build dense representations — perfect for classification, extraction, reranking and vector search, useless for fluent generation. Decoder-only models generate one token at a time and are what everyone means by "an LLM". Encoder-decoder models map one sequence onto another and survive in speech-to-text and translation. The rule that follows: never use a huge generative model to sort a million support tickets into five buckets when a small encoder does it faster and far cheaper.

**Dense versus mixture-of-experts.** A dense model activates every parameter for every token. A mixture-of-experts model routes each token through a small subset of expert sub-networks. The operational consequence is peculiar: an MoE model has the **memory footprint of a giant** (all experts resident) but the **per-token compute of a small model** (only active experts multiply). That is why some very large models are cheap to run and expensive to host.

**The four training stages.** Pre-training gives world knowledge and grammar. Supervised fine-tuning on instruction–response pairs gives assistant behaviour and formatting habits. Preference alignment — reinforcement learning from human feedback, or the simpler direct preference optimisation — gives tone, helpfulness and safety refusals, at the price of an **alignment tax**: over-tuned models refuse benign requests and drift into **sycophancy**, agreeing with a user who is plainly wrong. Reasoning post-training, reinforcement learning against verifiable rewards such as maths answers or unit tests, buys multi-step logic at the cost of thousands of hidden thinking tokens before the first visible word.

**Optimisation is four techniques, not one.** *Quantisation* stores weights at lower precision — sixteen-bit down to eight or four — shrinking memory roughly in proportion and costing a little accuracy on hard reasoning. *Distillation* trains a small student on a large teacher's outputs, compressing a five-thousand-token prompt into a fifty-token one. *LoRA and QLoRA* freeze the base weights and train small low-rank adapters, cutting training memory by more than half. *Speculative decoding* has a tiny draft model propose tokens that the large model verifies in one pass, speeding generation with no change to output quality.

### How it connects to the rest of the framework

`TSC4-Advanced-K1` is the hardware side of the same story — MoE's memory profile is a serving constraint before it is an architecture fact. `TSC4-Advanced-K3` turns these stages into a deployment workflow. `TSC4-Advanced-K4` prices the lifecycle. `TSC4-Intermediate-K5` is the input side: none of these stages work if the data is dirty. And `TSC4-Advanced-A1` is the practical question this bullet exists to answer — prompt, retrieve, or fine-tune.

### What is current as of November 2026

The 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon — is uniformly decoder-only and overwhelmingly mixture-of-experts at the top end. Three things have shifted for trainers:

- **Reasoning training became a product tier, not a research curiosity.** Vendors sell a "thinking" mode beside a fast mode of nominally the same model. Selection now includes choosing the mode.
- **Open-weight fine-tuning became routine.** Adapter tuning on a mid-sized open model is a normal line item in a Singapore project budget, where five years ago it was a research project.
- **Quantised deployment went mainstream.** Four-bit serving of a large open model is the default assumption rather than a compromise, and the loss is small enough that most evaluators cannot detect it on ordinary tasks.

### Common misconceptions

- *"Fine-tuning teaches the model our documents."* It teaches form, not facts. Facts belong in retrieval; a fine-tune on policy PDFs produces confident blends with no page citations.
- *"Pre-training is the thorough option."* It is the ruinous option, and it inherits every bias in the corpus you scrape.
- *"More parameters means a better model for my task."* More parameters means broader general capability. Narrow tasks saturate at small sizes.
- *"Quantisation is free."* It is cheap, not free — a one to three point drop on hard reasoning benchmarks is typical and must be measured.

## How a student should understand it

**Mental model:** hiring a fresh graduate, then sending them to bootcamp, then giving them a desk manual. Pre-training is the degree; fine-tuning is the induction that teaches your forms and your tone; retrieval is the manual they look things up in. Nobody sends a graduate back to university because the leave policy changed.

**Things they can do after this bullet:**
1. Explain the training stages and what each one actually buys.
2. Choose between encoder and decoder architectures for a given task shape.
3. Name an optimisation technique and state what it costs in quality or engineering effort.

**Misconceptions to kill:** that fine-tuning injects facts, that pre-training is the safe default, and that optimisation is someone else's problem.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The NUS graduate and the company bootcamp.** Sixteen years of education (pre-training) produces someone who can read, reason and write. A three-month in-house programme (fine-tuning) produces someone who fills in *your* claim form correctly and answers the phone in *your* tone. An open-book SOP on the desk (retrieval) is how they answer "what is the current reimbursement cap". Where it breaks: a graduate remembers what they were taught and can explain it; a fine-tuned model has no memory of its training examples and cannot cite them.

**The recipe book versus the chef's hands.** Architecture is the kitchen; training is what the chef practised; optimisation is pre-chopping and portioning so service is fast. Pre-chopped ingredients are not worse — unless the dish depends on freshness.

### Worked example with a real tool

The question that exposes the whole bullet:

```text
We have 4,000 pages of internal HR policy that change every quarter,
and we want an assistant that answers staff questions in our formal
corporate tone. Should we pre-train, fine-tune, or use retrieval?
Answer in four sentences and name what each option costs us.
```

What to point at afterwards: a good answer separates the two goals — the *facts* change quarterly, so they belong in retrieval; the *tone* is stable, so it can be taught by fine-tuning or simply by a system prompt with two examples. Then push: "which of those is cheaper to maintain?" The room should land on "the prompt, until the tone problem is worth an adapter".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a base model completing a question as if it were a quiz. The room laughs; the point lands.
2. **State the objective** — by the end you can choose between pre-train, fine-tune, prompt and retrieve, and defend it.
3. **Recall prior learning** — tokens and next-token prediction from the Intermediate bullet.
4. **Present the content** — architecture families, the four training stages, the optimisation toolbox.
5. **Guide** — work the graduate analogy through one real policy question together.
6. **Elicit performance** — teams of three get a scenario card and must pick a route with a one-line justification.
7. **Give feedback** — debrief, correcting "fine-tune on the PDFs" every time it appears.
8. **Transfer** — each learner writes the route they would take for one task in their own job, plus its maintenance cost.

## What the framework doesn't mention but trainers need to know

- **Fine-tuning is a commitment, not a purchase.** An adapter is bound to one exact base model. Upgrade the base and you retrain. That is why portability matters more than a quality point in any build-versus-buy table.
- **Distillation is the quiet workhorse of cost reduction.** Most "we cut our AI bill by 90%" stories are distillation stories: a big model generates verified outputs, a small model learns to imitate them.
- **Catastrophic forgetting is easy to trigger.** Aggressive fine-tuning on a narrow dataset degrades general reasoning. Always evaluate the tuned model on a general set, not only the target task.
- **The alignment tax is a selection criterion.** A model that refuses to discuss medical terminology is unusable in a clinic. Test false refusals before you fall in love with a safety score.
- **Optimisation order matters.** Prompt and retrieve first, then distil, then quantise. Teams that quantise first spend weeks tuning a model that was the wrong size to begin with.

## Watch out

- **Do not teach parameter counts as facts.** They are round numbers that shift every generation; teach the tiers (edge, small, mid, frontier) and what each is for.
- **Do not demo fine-tuning in a beginner room.** The tooling is easy; the mental model is not there yet, and the room concludes that model training is the point of AI.
- **Do not claim quantisation is lossless.** It is close enough for most tasks and visibly not close for hard reasoning. Say so.
- **The stale claim to retire:** "you need a PhD and a GPU cluster to customise a model." In November 2026 a competent engineer can adapter-tune an open model in an afternoon.
