---
id: 06.02.I.A2
tsc: 6
level: Intermediate
code: A2
title: Three integration workflows: batch, API, and multi-model orchestration
---

# Three integration workflows: batch, API, and multi-model orchestration

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Ability A2**


> **Framework text (verbatim):** "Design integration workflows between AI models and systems, such as batch processing, API integration, and multi-model orchestration."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Ability · Bullet 9 of 12

**One-line version:** Every AI workflow is one of three shapes — a queue, a conversation, or a conductor — and choosing the wrong shape is the defect no amount of prompt tuning fixes.

## What it is

This is the ability to look at a business task and design the workflow that carries it: synchronous API calls for interaction, batch jobs for volume, orchestration when more than one model or system must cooperate. The deliverable is a diagram plus the operational rules — retries, checkpoints, budgets — that make it survivable.

## Deep expansion

### The concept

The framework names three workflow patterns, and they answer three different questions.

**API integration — "the user is waiting."** A request arrives, the application calls a model, the answer returns. Everything is optimised for latency and for failing gracefully in front of a human: short timeouts, few retries, and an error message that is part of the product.

**Batch processing — "the user is not waiting."** Ten thousand documents, four hundred feedback rows, a nightly re-embedding. The target flips to throughput and cost: cheaper asynchronous endpoints, checkpointed progress, idempotent steps, and a report at the end rather than a response.

**Multi-model orchestration — "several things must cooperate."** A router picks a model, a chain passes output forward, a fan-out summarises then synthesises, an evaluator scores and sends work back. The design question is control flow: who decides, what happens on disagreement, and where the loop terminates.

Choosing the shape is the design act. Learners routinely build interactive workflows for batch work — slow, expensive, brittle — or batch workflows for interactive work, where users conclude the app is broken.

### The sub-concepts

**Idempotency keys.** The same row must never be processed twice. An explicit key per unit of work turns retries into no-ops instead of duplicates.

**Checkpointing and resume.** Write progress after each unit. A job that dies at 80% and restarts from zero is a job that will die again next month.

**Backoff with jitter and a cap.** Retry storms are self-inflicted outages. Exponential backoff, randomised, with a maximum attempt count and a dead-letter path for what still fails.

**Dead-letter queue.** Failures that exhaust retries land somewhere a human can inspect, with the input attached. Without it, the missing 3% is invisible.

**Rate-limit budgeting.** Know the tokens-per-minute and requests-per-minute ceilings per key, and schedule the batch inside them. Most production 429s are self-inflicted by a batch job sharing a key with the live app.

**Cost ceiling per job.** Compute maximum spend before launching: units × average tokens × price. A job with no ceiling is a job that can produce a surprising invoice.

**Termination conditions.** Any loop — evaluator-optimiser, retry-until-valid, agent-reflects — needs an explicit stop: max iterations, a quality threshold, a cost cap, a wall clock.

### How it connects to the rest of the framework

`TSC6-Intermediate-K1` supplies the contract concepts, `TSC6-Intermediate-K5` is the pipeline these workflows execute, and `TSC6-Intermediate-K2` decides which model sits at which node. `TSC6-Intermediate-A1` is how you find out the workflow is failing; `TSC6-Basic-A2` is a specific orchestration pattern at Basic level.

### What is current as of November 2026

The three shapes have not changed; the tooling around them has. Batch endpoints are now a first-class product on the major providers, priced well below synchronous calls, so "does this have to be now" has become a budget question with a clear answer. Orchestration moved from chained calls to state machines that declare stages, transitions and retry policy, because a plain chain cannot express "validate, and if it fails go back to retrieval". And tool protocols standardised the far side: MCP means the system a workflow talks to is often a tool server rather than bespoke code, which reduces glue and moves the failure modes into the tool layer.

### Common misconceptions

- *"Batch is just a loop."* A loop has no checkpoint, no idempotency, no dead-letter and no cost ceiling. A batch job has all four, and that is the whole difference.
- *"Orchestration means more models."* It means more control flow. One model behind a router with a fallback is orchestration.
- *"Retries make it reliable."* Retries make it eventually reliable if they are bounded, idempotent and observable. Otherwise they make it worse.

## How a student should understand it

**Mental model:** MRT, taxi, delivery van. The MRT is batch — fixed schedule, everyone aboard, cheap per head, and you wait. The taxi is a synchronous API — immediate, metered, one passenger. The van with a route sheet is async with a queue and a manifest.

**Three things they can do after this bullet:**
1. Given a task, choose batch, sync or orchestrated, and defend it on cost and latency.
2. Write the four operational rules for a batch job: idempotency key, checkpoint, retry policy, dead-letter.
3. Draw an orchestration with an explicit termination condition.

**Misconceptions to kill:** batch is a loop, orchestration means more models, and retries equal reliability.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**MRT versus taxi versus catering order.** MRT is batch: cheap, scheduled, you do not control the timing. Taxi is sync: immediate, metered, one at a time. A catering order for 200 lunchboxes is async batch with a manifest — and if the count is wrong, the failure is discovered at the venue, not the kitchen. Where it breaks: the MRT never loses a passenger, while a batch job can absolutely lose row 3,847 without telling you.

**The zi char order chit, for orchestration.** One chit to the wok, one to the BBQ station, one to drinks. Nobody finishes in isolation: the dishes must arrive together, so if the BBQ is slow the wok has to be paced. That pacing rule is the orchestration logic, and it is the part everyone forgets to write down.

### Worked example with a real tool

Design the batch job for a real corpus. In Claude:

```
Write a Python script that processes a CSV of 400 customer feedback
rows through an LLM that labels sentiment and topic.

Rules:
- Skip rows that already have a label (resume from a crash).
- Retry 3 times with exponential backoff on 429 and 5xx.
- Write failures to failed.csv with the row id and error.
- Print total tokens used and an estimated cost at the end.
- Never exceed 60 requests per minute.
```

What to point at afterwards: "skip rows that already have a label" is resume plus idempotency; `failed.csv` is the dead-letter queue; the retry clause is the backoff policy; the 60-per-minute cap is the rate-limit budget; the cost print is the ceiling check. Five lines, five rules — and a generated script that omits them will fail at row 300 and leave the team guessing how much was done.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a batch run that died at 80% and re-billed the whole corpus on restart.
2. **State the objective** — you will choose a workflow shape and specify its operational rules.
3. **Recall prior learning** — they know the pipeline stages (K5) and the API contract (K1); this is the schedule and control flow on top.
4. **Present the content** — the three shapes, then the operational rules.
5. **Guide** — sort six scenarios into batch, sync or orchestrated, arguing each.
6. **Elicit performance** — pairs design the workflow for a task from their own work, on one page, with the rules listed.
7. **Give feedback** — the recurring miss is the termination condition; loops get designed with no stop.
8. **Transfer** — they add the four batch rules to their team's job template.

## What the framework doesn't mention but trainers need to know

- **Most AI spend is batch-shaped work done synchronously.** A nightly re-summarisation run through an interactive endpoint costs several times what the batch endpoint does, and nobody notices because it is one line of code.
- **Checkpointing is the cheapest reliability you will ever buy.** Ten lines of code, skipped because the first run works.
- **Orchestration is where cost explosions live.** Fan-out times retries times escalation to the bigger model can multiply unit cost by an order of magnitude with no visible change to output.
- **The workflow diagram is a governance artefact.** It shows where data goes, which model sees it, and where a human is in the loop — which is what a risk officer needs (K6).

## Watch out

- **Do not let the session become a framework comparison.** The shapes are the lesson; the library is packaging.
- **Do not demo a batch job on ten rows.** Scale is the point: at ten rows nothing fails, at ten thousand everything does.
- **Do not skip the cost arithmetic.** Learners consistently underestimate fan-out; make them multiply on the whiteboard.
- **The stale claim to retire:** "we'll process it in real time to keep it simple." In November 2026 real time is the expensive, brittle choice for work with no user waiting.
