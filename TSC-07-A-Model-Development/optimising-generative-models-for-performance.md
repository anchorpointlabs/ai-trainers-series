---
id: 07.03.A.A3
tsc: 7
level: Advanced
code: A3
title: Optimising a generative model: latency, throughput and cost are not one problem
as_at: 2026-11-26
review_by: 2027-02-25
---

# Optimising a generative model: latency, throughput and cost are not one problem

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A3**


> **Framework text (verbatim):** "Optimise complex generative models for performance and efficiency."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 14 of 20

**One-line version:** Measure which of the four — latency, throughput, cost, quality — is actually failing, because the fix for each one can make the others worse.

## What it is

This ability is the disciplined optimisation of a generative system under a real constraint. It begins with instrumentation, separates the four objectives, and applies levers in order of cost: cheaper prompts, better serving, smaller models, then retraining. Optimisation without measurement is just churn with a performance dashboard.

## Deep expansion

### The concept

Generation has two phases with different economics. **Prefill** processes the input — compute-bound and roughly linear in prompt length. **Decode** produces output tokens one at a time — memory-bandwidth bound and roughly linear in output length. Nearly every "the model is slow" complaint resolves into one of these phases, and they respond to different levers.

The four objectives pull against each other:

- **Latency** — time to first token and time per output token. Improved by smaller models, shorter prompts, speculative decoding and streaming.
- **Throughput** — tokens per second per device across all users. Improved by batching, which usually worsens per-request latency.
- **Cost** — money per accepted output. Improved by caching, routing, quantisation and shorter outputs.
- **Quality** — the thing you are not allowed to lose. Every lever must be evaluated against a frozen set.

A team that optimises throughput and calls it performance will ship a faster system that users find slower, because time to first token got worse.

### The sub-concepts

**Instrumentation first.** Percentiles, not averages: p50, p95, p99 for latency, plus queue time, prefill time and decode time as separate spans. If you cannot attribute 200 ms to a component, you cannot optimise it.

**Caching at three levels.** Exact-match response cache, prefix cache for shared system prompts, and semantic cache for near-duplicate queries with a similarity threshold. Semantic caching is the risky one: it trades correctness for speed, so its threshold needs its own evaluation.

**Output length is the biggest lever nobody pulls.** In chat workloads, output tokens dominate cost and perceived latency. Instruction discipline, max-token limits and structured output formats often beat any infrastructure change.

**Routing and cascades.** Send easy requests to a small model, escalate on low confidence or failed validation. A good router can move most traffic to a much cheaper model with no measurable quality loss.

**Model-level levers, last.** Quantisation, distillation and speculative decoding — covered in `TSC7-Advanced-K6` — are powerful but require retraining or careful evaluation. Exhaust prompt and serving-side options first.

### How it connects to the rest of the framework

`TSC7-Advanced-K6` is the theory of the efficiency techniques used here; `TSC7-Advanced-K3` explains why a kernel change can beat a model change. `TSC6-Advanced-A2` (serving infrastructure) is the deployment side, and `TSC5-Intermediate-A3` is the evaluation discipline that proves an optimisation did not cost quality.

### What is current as of November 2026

Serving has become the competitive battleground. Prefix caching, paged KV caches, speculative decoding and 8-bit or 4-bit weights are defaults in current serving stacks rather than clever tricks, and most providers price by cached versus uncached input tokens, which makes prompt structure a cost decision. The late-2026 frontier models — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and 4 Argon — are marketed heavily on latency and price per token, so a team that has not instrumented its own p95 is negotiating blind.

### Common misconceptions

- *"Lower average latency means a better experience."* Users feel the tail. p95 is the number that generates complaints.
- *"Batching is free speed."* It raises throughput and hurts interactive latency.
- *"Quantise first, it is the easiest win."* Prompt and output-length fixes are cheaper, reversible and often larger.
- *"Caching is safe if the threshold is high."* Every cache is a correctness decision; semantic caches need their own evaluation set.

## How a student should understand it

**Mental model:** a clinic queue. Throughput is patients per hour; latency is how long one patient waits; cost is cost per consultation; quality is the diagnosis. Adding chairs improves one number and hides another.

**Three things they can do after this bullet:**
1. Build a trace that separates queue, prefill and decode time.
2. Pick the cheapest lever for a stated bottleneck and predict its side effect.
3. Prove an optimisation did not degrade quality on a frozen set.

**Misconceptions to kill:** that average equals experience, that batching is free, and that quantisation is the first thing to try.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The polyclinic.** Seeing more patients per hour is throughput. Each patient's wait is latency. A doctor who sees forty patients quickly but leaves the last ten waiting two hours has optimised the wrong number, and the complaints prove it.

**The express lane at the supermarket.** Ten items or fewer moves the queue — until half the shoppers have eleven items and the express lane becomes the slow one. Routing has exactly this failure.

### Worked example with a real tool

Start from a measurement, not a hunch:

```
Our document assistant: p50 first token 1.8s, p95 9.4s, average
output 900 tokens, system prompt 2,400 tokens repeated on every
call, 3k requests/day on a frontier model.

Propose an optimisation plan:
1. Which of latency, throughput, cost or quality is most likely
   the real business problem, and what would you ask to confirm?
2. Rank five levers by (expected gain / effort / risk), cheapest
   first, and state what each one breaks.
3. Which lever requires an evaluation run before shipping, and
   which evaluation?
4. What do you expect p95 to look like after the top two levers?
```

What to point at afterwards: the fix with the best ratio is usually shrinking the repeated system prompt and capping output length, not changing models. Learners consistently propose switching to a smaller model first, which is the most expensive and riskiest lever. The p95-to-p50 gap also reveals queueing that no model change fixes.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a dashboard with a good average and a terrible p95; ask which customer wrote the complaint.
2. **State the objective** — attribute latency to a phase and choose a lever with a predicted side effect.
3. **Recall prior learning** — prefill versus decode from `TSC7-Advanced-K6`.
4. **Present the content** — the four objectives, three cache levels, output length, routing.
5. **Guide** — walk the document-assistant plan.
6. **Elicit performance** — teams instrument a small local endpoint and report percentiles.
7. **Give feedback** — compare predictions against measurements.
8. **Transfer** — each learner writes the p95 target their own system should meet.

## What the framework doesn't mention but trainers need to know

- **Time to first token is the perceived-speed metric.** Streaming makes a slow model feel acceptable and a fast one feel instant.
- **Prompt structure is a billing decision.** Cached prefixes are often priced differently; stable prompts at the front save real money.
- **Optimise the request shape before the model.** Retrieval over-fetching and verbose history are the usual culprits.
- **Keep a regression suite that runs on every optimisation.** Otherwise the fourth change silently undoes the first.

## Watch out

- **Do not optimise on a laptop.** Cold caches and no batching give numbers that do not transfer.
- **Do not present cost savings without quality evidence.** The cheapest system is the one that answers nothing.
- **Do not chase benchmark latency.** Vendor benchmarks use favourable prompt and output lengths.
- **The stale claim to retire:** "a smaller model will be faster and cheaper." In 2026 a smaller model that needs retries is often slower and dearer.
