---
id: 06.02.I.K2
tsc: 6
level: Intermediate
code: K2
title: One application, several models: why teams mix them and where it breaks
---

# One application, several models: why teams mix them and where it breaks

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Knowledge K2**


> **Framework text (verbatim):** "Concepts of integrating multiple generative AI models, including common compatibility and integration issues."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Knowledge · Bullet 2 of 12

**One-line version:** Mixing models buys capability and costs coherence — the application must expect three different personalities, three different error formats and three different bills.

## What it is

Integrating multiple generative AI models means one application routes work to more than one model: a cheap small model for classification, a frontier model for reasoning, an embedding model for retrieval, a speech model for transcription. The knowledge here is why you would do that, and the compatibility problems that appear the moment the second model arrives.

## Deep expansion

### The concept

A single model is a single set of trade-offs — quality, latency, price, context size, hallucination rate — and no model is best at all of them. Real applications assemble a small team, each member chosen for the job it does cheaply and well.

The team takes one of four shapes:

1. **Router.** A small fast model reads the request and picks the specialist. Cheap, predictable, and most traffic never reaches the expensive model.
2. **Cascade.** Try the cheap model, escalate when a validation or confidence check fails.
3. **Ensemble.** Ask two models and compare or merge — expensive, worth it where a wrong answer costs more than a call.
4. **Specialist pipeline.** Different stages, different models: transcribe, reason, embed.

The question is never "which model is best" but "which model is best *for this step, at this budget, with this latency ceiling*" — and then how the application behaves when that choice is wrong.

### The sub-concepts

**Message format.** Most providers accept an OpenAI-style `messages` array, but features are not portable: system-prompt handling, image encoding, tool-call schemas and structured-output guarantees differ. A prompt that works on one provider can silently drop its system instruction on another.

**Context budget per hop.** A pipeline that hands 200 pages to a long-context model and a chunk to a small-context model fails on the second leg. Every stage needs its own allowance.

**Tokenisers.** Tokens are not a universal unit. The same text costs a different number on different models, so a cost estimate built on one tokeniser is wrong for the other.

**Rate limits.** Limits are per organisation, per model, per region. A router that doubles throughput on model A does nothing for a bottleneck on model B.

**Error taxonomy.** One provider returns 429 with `retry_after`; another returns 200 with an error object in the body. A shared handler must normalise both, or the monitoring lies.

**Structured output.** If stage two needs JSON, stage one must guarantee it. Where schema-constrained output is unavailable, the application needs a validator and a repair loop.

### How it connects to the rest of the framework

`TSC6-Intermediate-K1` gives the integration vocabulary; this bullet applies it to models. `TSC6-Intermediate-K5` is the pipeline that houses the mix, `TSC6-Intermediate-A2` the workflow shapes that switch between them. Upstream, `TSC4` is choosing each member; this is what happens after the choice.

### What is current as of November 2026

The market has settled into tiers rather than a single leader: a frontier reasoning tier (OpenAI's GPT-6 generation — Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber — Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon), a cheap fast tier, and specialised models for embedding, speech and image. Interoperability improved at the surface but not underneath: the wire format is portable, the behaviour is not — tool-calling reliability and refusal style still differ per model. Routing itself became infrastructure, with gateways in front of several providers carrying spend caps and failover.

### Common misconceptions

- *"Using two models doubles the quality."* It doubles the surface area. Quality improves only where the second model is genuinely better at that step.
- *"If both are OpenAI-compatible, I can swap freely."* Compatibility covers the envelope, not the letter. Test tool calls and structured output on each model.
- *"Cost is the price per token."* Cost is tokens, times retries, times how often the router guesses wrong.

## How a student should understand it

**Mental model:** a polyclinic. A nurse triages in two minutes, a GP handles most cases, a specialist gets the referral — and the system works because the referral note carries the right information.

**Three things they can do after this bullet:**
1. Draw a two-model design and say which step goes where, and why.
2. Name three things that break when the second model is added.
3. Write the validation step that decides whether a cascade should escalate.

**Misconceptions to kill:** more models means better, compatibility means interchangeability, and fallback is automatically safer.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The polyclinic.** Triage, GP, specialist: cheap and fast at the front, expensive and slow at the back, and everything depends on a legible referral note. Where it breaks: a clinic has one boss and one patient record; a multi-model app has several vendors, several bills and no shared memory unless you build it.

**A multimodal commute.** Bus, MRT, walk. Each leg is efficient alone; the trip fails at the transfer. Latency stacking is the transfer time, and no amount of speed on the MRT fixes a bus that comes every twenty minutes.

### Worked example with a real tool

Run the same structured task on two models and compare the envelope, not the prose. In each provider's playground:

```
Classify this customer message into exactly one of:
BILLING, DELIVERY, PRODUCT_QUALITY, OTHER.

Return only JSON: {"category": "...", "confidence": 0.0-1.0, "reason": "..."}

Message: "The rice cooker I ordered last Tuesday still hasn't arrived
and nobody has called me back."
```

What to point at afterwards: one model returns bare JSON, one wraps it in a markdown fence, one adds a friendly sentence first. All three are correct; only one is safe to pipe into stage two without a parser. That is the compatibility problem in miniature, and the reason every hop needs a validator.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a support bot answering in three different formats on three consecutive messages.
2. **State the objective** — you will choose which model handles which step and name the compatibility risks you accept.
3. **Recall prior learning** — they know single-model integration (K1) and selection criteria (TSC4).
4. **Present the content** — the four shapes and the compatibility issues.
5. **Guide** — design a router plus specialist for the classification task on the whiteboard.
6. **Elicit performance** — pairs design a two-model workflow from their own work and write the escalation rule.
7. **Give feedback** — the usual error is a cascade with no validation step, so it escalates on nothing or everything.
8. **Transfer** — they add a "which model, which step, what if it fails" line to their design doc.

## What the framework doesn't mention but trainers need to know

- **Every additional model is another contract to monitor.** Uptime, deprecation, price and behaviour all multiply. A dependency list with an owner per line beats any architecture diagram.
- **Disagreement between models is data.** When a router's choice and a validator's verdict differ, that is the best signal in the system for finding bad prompts. Log it.
- **Most traffic belongs on the cheap model.** Learners over-index on the frontier model because that is what the news covers; the engineering is in the routing.

## Watch out

- **Do not compare prose quality in the demo.** The room will argue about taste. Compare envelopes, latency and cost per call — those are decidable.
- **Do not teach switching models as a strategy.** Swapping to chase a leaderboard is how teams accumulate four half-tested integrations.
- **The stale claim to retire:** "one model to rule them all." In November 2026 the practical architecture is a small team behind a router, and the craft is the routing rules.
