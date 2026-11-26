---
id: 06.03.A.K1
tsc: 6
level: Advanced
code: K1
title: "Compute efficiency: the same model at three different bills"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Compute efficiency: the same model at three different bills

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Knowledge K1**


> **Framework text (verbatim):** "Concepts behind compute efficiency (e.g., quantisation, similar efficiency techniques)."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Knowledge · Bullet 1 of 12

**One-line version:** Compute efficiency is the craft of serving the same answer on less silicon — and every technique is a trade you have to price before you make it.

## What it is

Compute efficiency is the set of techniques that reduce the memory and arithmetic needed to run a generative model, so one machine serves more users, answers sooner, or costs less per token. Quantisation is the example everyone names: storing weights at 8 or 4 bits instead of 16. The Advanced skill is not reciting the techniques; it is predicting what each one costs in quality, latency and engineering time *before* committing the architecture to it.

## Deep expansion

### The concept

Most generative AI cost is inference, not training. Every live request re-reads the weights and grows a key-value cache, and that traffic — not the mathematics — is usually what limits throughput. Generation is memory-bandwidth bound: the arithmetic units spend much of their time waiting for bytes to arrive. That fact explains nearly every efficiency technique. If you are limited by bytes moved rather than sums computed, then moving fewer bytes (quantisation), reusing bytes already moved (caching), or moving them for several users at once (batching) all buy speed without changing the model's logic.

So there are three levers and one ledger. Fewer bits per weight; less work per token (smaller model, distillation, routing, speculative decoding); more tokens per pass (batching, prefix caching, paged attention). The ledger is the part learners skip — each lever trades accuracy on edge cases, latency predictability, engineering time, or a new class of bug. An Advanced practitioner writes the ledger down before choosing: option, saving, risk, and the test that would catch the risk.

### The sub-concepts

**Precision.** bfloat16 is the reference; int8 halves the footprint; 4-bit formats (GPTQ, AWQ, the GGUF family) quarter it. Weight-only quantisation is gentlest; quantising activations as well saves more and risks more. A 4-bit large model usually beats a 16-bit small one at the same memory — but "usually" carries the weight, and your own prompts are the only test that counts.

**KV cache arithmetic.** Memory is roughly parameter count × bytes per parameter, plus context length × layers × heads × head dimension × batch × bytes. The weights are fixed; the cache grows with the conversation and with concurrency. That is why "paste the whole manual" and "serve fifty users" fight each other.

**Batching.** Throughput and latency pull apart. Continuous batching keeps the device fed as requests arrive and leave; watch the ninety-fifth percentile, because the mean hides the user who waited nine seconds.

**Caching.** A shared system prompt need not be recomputed forty times a day. The hazard is a sloppy cache key returning yesterday's answer to today's question.

**Distillation and routing.** Train a small model on a large one's outputs, or send easy requests to the cheap tier and escalate the hard ones. Often the largest real saving, and the least discussed, because it is work rather than a purchase.

### How it connects to the rest of the framework

`TSC6-Advanced-A2` is where these levers are actually set: tensor parallelism, maximum sequence length, memory utilisation and concurrency limits are efficiency decisions expressed as serving flags. `TSC6-Advanced-K2` shares the same budget — every guardrail costs tokens and milliseconds, so safeguards and efficiency are one design conversation. `TSC7-Advanced-K6` is the framework's near-duplicate of this bullet from the model-development side; teach application consequences here, training consequences there, and say openly that the framework repeats itself.

### What is current as of November 2026

- **4-bit is the default for self-hosted open weights**, not an experiment. Instruction-tuned models in the 8B–70B range are routinely served at 4-bit on one device; the quality loss on ordinary tasks is often small, task-dependent, and never quoted without your own evaluation.
- **Serving stacks already do the easy wins.** vLLM, TGI and peers ship continuous batching, paged attention and prefix caching by default, so hand-rolled batching is rarely worth building now.
- **Frontier capability keeps getting cheaper per token.** Current frontier models compete on price and latency as much as capability, so a local deployment justified on cost alone needs re-checking annually.
- **Small on-device models are credible for narrow tasks**, which moves some features from server to phone — and moves the privacy question with them.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Quantisation means worse answers."* It means possibly worse answers on some tasks. Measure on your own set; accept neither the vendor's claim nor a colleague's anecdote.
- *"Efficiency is the infrastructure team's problem."* The application developer sets context length, prompt size, retry behaviour and model tier. Most of the bill is decided there.
- *"A bigger GPU is cheaper than optimising."* That confuses cost per hour with cost per token. An idle large GPU is the most expensive object in the room.
- *"The context window is big, so context is free."* Prefill is charged, the cache occupies memory, and long prompts raise latency for everyone in the batch.

## How a student should understand it

**Mental model:** the same pot of curry sold in three portions. The recipe does not change; what you pay and what you get change with the portion. Efficiency work is deciding the portion per customer — and refusing to sell the catering pot to one person.

**Three things they can do after this bullet:**
1. Estimate on paper whether a model fits a device at 16, 8 and 4 bits, cache included.
2. Name the three levers and say which applies to a stated symptom — slow first token, low throughput, large bill.
3. Write a ledger for a proposed optimisation: saving, risk, and the test that would catch the risk.

**Misconceptions to kill:** that quantisation is automatically a quality loss, that efficiency belongs to someone else, and that context is free because the window is wide.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**MP3 versus CD.** Most people cannot tell a well-encoded compressed track from the original in a noisy room; put on a choir recording and the artefacts appear. Quantisation is compression for weights: fine for ordinary use, exposed by demanding material, always worth an A/B on your own material. Where it breaks: audio compression degrades predictably, while quantisation errors can be spiky and task-specific.

**The zi char wok station.** One wok, many portion sizes. Batching is cooking four plates of the same dish in one pass — cheaper per plate, and the fourth plate waits. Throughput versus latency in one image, and every ops person recognises it.

### Worked example with a real tool

Ask an assistant to do the arithmetic, then check it:

```
I have one rented GPU with 24 GB of memory. I want to serve a 70B
parameter instruction model with a 16k context for about 20 concurrent
users.

1. Does it fit at 16-bit? At 8-bit? At 4-bit? Show the arithmetic.
2. What does the KV cache cost per concurrent request at 16k context?
3. If it does not fit, list the options in order of least quality risk
   and say what you would measure to confirm each was safe.
```

What to point at afterwards: 70B × 2 bytes is about 140 GB, and × 0.5 bytes is about 35 GB — the easy part. The assistant will sometimes get the cache term wrong or omit it. The lesson is the method: size the weights, add the cache, then choose. When a learner says "so 4-bit halves it", make them redo it with the cache included. That is the moment the bullet lands.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two bills for the same application, one built naively and one after four changes. Ask which change paid for itself.
2. **State the objective** — you will size a deployment and justify each efficiency choice with a risk and a test.
3. **Recall prior learning** — they know a model predicts tokens; now they see what each token costs.
4. **Present the content** — the three levers, the ledger, and why inference is bandwidth-bound.
5. **Guide** — work the 24 GB calculation together, including the cache term.
6. **Elicit performance** — pairs size their own use case and write a three-line ledger.
7. **Give feedback** — correct the pair who forgot concurrency, and the pair who quantised without evaluating.
8. **Transfer** — on their next build, they produce the ledger as a one-page decision note before provisioning anything.

## What the framework doesn't mention but trainers need to know

- **Quantise, then evaluate.** A model that passes your test set at 8-bit and fails at 4-bit has answered the question for you, and no benchmark table substitutes.
- **Cold start is an efficiency cost too.** An autoscaler that scales to zero makes the first user of the morning wait; warm pools and smaller models are the usual answers.
- **Output tokens usually cost more than input tokens**, which makes concision a genuine optimisation: a prompt demanding two-sentence answers is cheaper and often better than one inviting essays.
- **The framework repeats itself across TSC 6 and TSC 7** on this bullet. Say so; learners notice duplication and assume they missed something.

## Watch out

- **Do not quote benchmark numbers you cannot source this quarter.** Quantisation quality varies by model, format and task; a number from a blog post is a liability in front of a client.
- **Do not demo a quantised model without the unquantised one beside it.** The comparison is the teaching; its absence teaches "trust me", which is the opposite of Advanced practice.
- **Do not conflate training compute with inference compute.** Learners routinely do, and the advice that follows ("we need a cluster") is wrong by an order of magnitude.
- **The stale claim to retire:** "you need a GPU farm to do this properly." In November 2026 a single 24 GB device serves a useful application, and a well-routed API call serves most of the rest.
