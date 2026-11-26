---
id: 01.01.B.K3
tsc: 1
level: Basic
code: K3
title: What exists in November 2026, and what machine learning has to do with it
as_at: 2026-11-26
review_by: 2027-02-25
---

# What exists in November 2026, and what machine learning has to do with it

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K3**


> **Framework text (verbatim):** "Introduction to popular generative AI models and how they work, including machine learning."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 3 of 13

**One-line version:** Generative AI is one branch of machine learning, and the products you can buy in November 2026 are three frontier families, a handful of open-weight families, and separate model families for image, video and voice.

## What it is

Machine learning is the practice of getting behaviour from data instead of from instructions written by a programmer. Generative AI is the part of machine learning that produces content rather than a label. The models a trainer actually names in class belong to a small number of vendor families, each with a different price, context size and temperament.

## Deep expansion

### The concept

The nesting is simple and worth drawing on a whiteboard. **Artificial intelligence** is the ambition. **Machine learning** is one way to get there: show examples, adjust parameters, let the pattern emerge. **Deep learning** is machine learning with many-layered neural networks, which is what made image and language tasks work. **Generative AI** is deep learning trained to produce content — text, images, audio, video, code.

The distinction that matters commercially is not the nesting but the output type. A model that returns a label or a number (fraud, churn, demand) is a predictive model; a model that returns content is generative. `TSC1-Basic-K05` takes that difference apart. This bullet is about the members of the generative family and how to tell them apart in a room full of people who have only used one.

### The sub-concepts

**The three frontier families.** These are the vendors with the largest training runs, and they are not interchangeable.

- **OpenAI, GPT-6 generation.** The broadest product surface: ChatGPT for consumers and offices, an API, image and voice models, agents. Release cadence is fast — Astra in September 2026, then Sol, Luna, 6.1 Sol, 6.1 Terra, and GPT-6 Cyber for security work in November. Strength: ecosystem and breadth. Cost of that breadth: deprecation. The o1 and o3-mini reasoning models and legacy GPT-3.5 snapshots were switched off on 23 October 2026; GPT-4o and GPT-4.1 API snapshots follow on 14 January 2027.
- **Anthropic, Claude 5.5 line.** Four models — Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5 — all with a 1M-token context window and knowledge cutoff June 2026. Adaptive thinking is on by default on Fable and Opus. Strength: long documents, careful writing, coding through Claude Code, and an unusually explicit price ladder.
- **Google, Gemini.** Gemini 3.1 Pro (February 2026), Gemini 3 Flash as the cheap fast tier, and Gemini 4 Argon in use since around October. Strength: Workspace and Google Cloud integration, multimodal breadth, competitive small models. Vertex AI is the enterprise door; AI Studio the developer sandbox.

**Open-weight families.** Meta's Llama family and Mistral's models. The point is not that they are worse. The point is that the weights can be downloaded, so the model can run on your own infrastructure. That makes open weights a **data-residency answer**, not a quality answer, and it is the argument that wins with a cautious Singapore client.

**Media families.** Image: GPT Image 2.6 and Google's `gemini-3-pro-image` and `gemini-3.1-flash-image`. Video: Veo 3.1, Kling 3.0, Seedance, Runway Gen-4.5. Voice: GPT-Live-1 for full-duplex conversation, dedicated TTS models for narration. These are separate models with separate interfaces, not modes of the chatbot, and their failure patterns are visual rather than factual.

**How to choose.** Six questions, in order: what output do I need; how much context does the task carry; what does the price per million tokens do to my monthly cost; what do the data terms say; how much latency can the user tolerate; and how painful is it if this model is retired in six months. Quality is only the first question.

### How it connects to the rest of the framework

`TSC1-Basic-K02` is the mechanism these models implement. `TSC1-Basic-K04` is where each family is worth deploying. `TSC1-Basic-K06` lists the failures that no vendor has solved. `TSC1-Basic-K08` governs whether you may send data to a hosted model at all.

### What is current as of November 2026

Three facts to hold: the price range within a single vendor is now about 100x (Claude Fable 5.1 at $10/$50 per million input/output tokens against Haiku 5.5 from $0.10/$0.50, with a 50% batch discount and cache reads at 10% of input price); context windows at the top of the market are a million tokens; and model lifetimes are short. GPT-5.5 was retired from ChatGPT on 14 October 2026. DALL·E was shut down on 12 May 2026. Whisper has been superseded by GPT Transcribe. Any list of model names has a shelf life measured in months.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"AI, machine learning and generative AI are the same thing."* They nest. Most AI in a bank is not generative.
- *"The biggest model is the best choice."* For extraction and classification, a small fast model is often more accurate after tuning and always cheaper.
- *"Open source means free and worse."* Open weights cost money to run and can be excellent; the trade is control for convenience.
- *"The version numbers tell you which is better."* They tell you which is newer. Benchmarks do not transfer to your documents.

## How a student should understand it

**Mental model:** a shelf of appliances, not a single machine. You would not use a blender for everything in the kitchen; you would not use a frontier reasoning model to classify 4,000 invoices.

**Three things they can do:** place any tool they meet on the ML-to-generative ladder; name the three frontier families and one trade-off each; justify a model choice with a cost and a data answer, not a vibe.

**Misconceptions to kill:** that there is one best model, that version numbers imply quality, and that open weights are a compromise.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The three kopitiam chains.** Toast Box, Ya Kun and Killiney all sell kaya toast and kopi. All three are good. They differ in price, in how many outlets they have, and in whether they will deliver to your office. Asking "which is best" is the wrong question; asking "which for this morning, at this budget" is the right one. That is model selection in one sentence.

**The zi char kitchen.** One stall, one wok, many dishes. The same kitchen produces hor fun, cereal prawns and mee goreng — different outputs, same underlying skill. Generative AI is that kitchen: text, image, audio and code come from the same family of technique, but each dish is plated by a different cook.

### Worked example with a real tool

Task: summarise 1,000 supplier contracts a month, 15,000 input tokens each, 800-token summaries. Compare two tiers of the same vendor, using the published list prices.

Claude Fable 5.1 at $10 input / $50 output per million tokens: 15,000 tokens × $10/1M = $0.15, plus 800 × $50/1M = $0.04. About **$0.19 per document**, or $190 for the thousand.

Claude Haiku 5.5 at $0.10 / $0.50: 15,000 × $0.10/1M = $0.0015, plus 800 × $0.50/1M = $0.0004. About **$0.002 per document**, or $2 for the thousand.

Same task, same window, roughly 100x the bill. Then ask the room the useful question: on a sample of twenty contracts, is the expensive model's summary ninety-five times better? Usually not. What it is better at is the two contracts with a cross-reference you did not anticipate. That is what you are paying for, and it is a decision, not a default.

### Live demo or exercise

**One question, three tools.** Open ChatGPT, Claude and Gemini side by side. Ask each the same Singapore-specific question with a checkable answer — "Under the CPF Ordinary Account, what does the interest rate depend on?" or "What does an AI Verify testing report actually cover?" Read the three answers aloud. The room will see different structure, different confidence and occasionally different facts. The lesson is not which won; it is that three vendors trained differently do not agree, so the verification step is yours.

## What the framework doesn't mention but trainers need to know

- **Deprecation is a planning problem.** OpenAI's 2026 shutdowns stranded integrations built on 2024 models. Any organisation building on an API needs a register of which model version sits behind which workflow.
- **Rate limits bite before price does.** A pilot that works for five users can fail at fifty because of requests per minute, not cost.
- **Benchmarks do not transfer.** Public leaderboards measure exam questions. Your contracts, your dialect, your house format are the only test that counts.
- **Model routing is normal.** Mature deployments send easy work to a cheap tier and hard work to a frontier model, then escalate on failure. Teach the concept even at Basic.
- **The regulator cares which model.** A credit decision model and a drafting assistant carry different obligations under MAS guidance; "we used AI" is not a sufficient description.

## Watch out

- **Do not teach the model list as knowledge.** It is a snapshot. Teach the families, the trade-offs and the six questions.
- **Do not declare a winner.** Vendor preference in a Singapore classroom is often a procurement decision wearing a technical costume.
- **Do not present Sora 2 as a current product.** Its status is unverified; if it comes up, say so.
- **Do not say "open source" when you mean open weight.** The licence terms differ and the distinction matters to a client's legal team.
- **Do not confuse the chat product with the model.** ChatGPT, Claude and Gemini are products wrapping models, with memory, tools and pricing of their own.
