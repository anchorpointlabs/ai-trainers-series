---
id: 06.02.I.K1
tsc: 6
level: Intermediate
code: K1
title: Software integration: making two systems behave like one
---

# Software integration: making two systems behave like one

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Knowledge K1**


> **Framework text (verbatim):** "Concepts of software integration."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Knowledge · Bullet 1 of 12

**One-line version:** Integration is not "connecting two things" — it is agreeing on a contract, then surviving the day one side changes without telling the other.

## What it is

Software integration is the practice of making two independently built systems exchange work reliably: one asks, the other answers, and each keeps its own internal rules. The core concepts are the interface, the contract and the failure model. Every generative AI application is an integration project before it is an AI project.

## Deep expansion

### The concept

Two systems can each be perfect and still fail together. The failure is almost never inside either system — it is at the seam. Integration thinking is therefore a shift of attention: away from "what does my model do" and toward "what does it promise the system calling it, and what happens when that promise breaks".

The promise has three parts: **shape** (the format), **timing** (synchronous, asynchronous or batched), and **failure behaviour** (what happens when the answer never comes, comes twice, or comes malformed). A model call adds a fourth, because the reply can be perfectly-formed nonsense — so the design validates content, not just structure.

### The sub-concepts

**The contract.** The published description of the interface: endpoints, fields, error codes, limits. Written down and versioned, it lets two teams work in parallel. Held in someone's head, every change is an outage.

**Coupling.** Reaching into another system's database is fast to build and impossible to change; calling a documented endpoint costs a little more and survives replacement of either side. Prefer loose around models, which get swapped every few months.

**Synchronous versus asynchronous.** A chat window must answer in seconds; a nightly re-embedding of 40,000 documents must not be synchronous, because a dropped connection at document 31,000 forces a restart. Choosing wrongly is the most common architectural mistake in AI applications.

**Idempotency.** The same request received twice must not do the work twice. Networks retry; queues redeliver. Without an idempotency key, retries become duplicate emails and double charges.

**Authentication and observability.** Who is calling, what they may touch, and a correlation ID threaded through every hop so one user report can be traced across four services and one model call.

### How it connects to the rest of the framework

This bullet is the substrate for the level. `TSC6-Intermediate-K5` is integration applied to a sequence of stages; `TSC6-Intermediate-A2` applies it to batch, API and orchestration; `TSC6-Intermediate-A5` is what happens when the contract drifts. At Basic level, `TSC6-Basic-K6` ("will it run here") is the step below this one.

### What is current as of November 2026

Two shifts. Nearly every provider now exposes an OpenAI-compatible chat endpoint, so switching models is often a change of base URL and model name — loose coupling is cheap in a way it was not in 2024. And the seam itself has standardised: the Model Context Protocol is now the common way to attach tools and data to an assistant. The skill has therefore moved up a level, from "how do I call an API" to "how do I govern the contracts between six services and three models".

### Common misconceptions

- *"Integration is an IT problem, not an AI problem."* Every AI failure a user sees is either a model failure or an integration failure, and the second is more common and easier to fix.
- *"If it works in my notebook, it's integrated."* A notebook has no auth, no retry, no timeout, no rate limit and one user. That is a demo.

## How a student should understand it

**Mental model:** the MRT interchange. Each line runs perfectly on its own, and passengers still get stranded when the platform link breaks, the fares do not reconcile, or the walk between platforms is longer than anyone will tolerate.

**Three things they can do after this bullet:**
1. Draw the seam between two systems they own and label the contract in three parts.
2. Say whether a task should be synchronous, asynchronous or batched, and justify it in one sentence.
3. Point at where a retry would duplicate work if the same request arrived twice.

**Misconceptions to kill:** that integration is plumbing rather than design, that a working demo is a working system, and that retries are free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT interchange.** Two lines, one platform link. When it works, nobody notices; when it fails, both lines report normal service and thousands of people are late. Where it breaks: an interchange has one operator and one change calendar; a real integration usually has two organisations and no shared boss.

**The order chit at a zi char stall.** The waiter writes a fixed format — table number, dish code, quantity, special instructions — and the kitchen reads only the chit. Change the layout without telling the kitchen and the right dish goes to the wrong table. The chit is the contract; the table number is the correlation ID.

### Worked example with a real tool

Ask a model to draft the integration, then read it as a reviewer. In Claude or ChatGPT:

```
Write a Python script that reads rows from a Google Sheet of customer
feedback, sends each row to an LLM to classify sentiment, and writes
the label back into a new column.

Requirements: retry failed calls 3 times with backoff, do not
reprocess rows that already have a label, and log every failure with
the row number.
```

What to point at afterwards: "do not reprocess rows that already have a label" is idempotency — the only thing between a crashed run and 400 duplicate API charges. The retry clause is the failure model; the row number is the correlation ID. Generated scripts get the first two and forget the third, which is the gap between code that runs and code you can operate.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two systems that each pass their own tests, and one customer complaint caused entirely by the seam.
2. **State the objective** — you will name the contract, the timing and the failure behaviour for any integration you build.
3. **Recall prior learning** — they have called an API or used a no-code connector; this is what was actually happening.
4. **Present the content** — contract, coupling, sync versus async, idempotency, auth, observability.
5. **Guide** — label each line of the generated script against the concepts.
6. **Elicit performance** — pairs sketch two boxes and write the three-part contract on the arrow between them.
7. **Give feedback** — the common miss is timing: learners default to synchronous for everything, including overnight batch work.
8. **Transfer** — they add the contract note to the next feature they ship.

## What the framework doesn't mention but trainers need to know

- **The model is the easiest thing to blame.** When an app misbehaves, check the seam first — auth, timeouts, schema, encoding — because those failures are common, cheap to find and boring.
- **Contracts rot silently.** A provider deprecates a model, a field changes type, a rate limit drops. Nothing throws until traffic arrives. Version pinning plus a smoke test on every deploy is the cheap insurance.
- **Cost is an integration property.** Retries, fan-out and duplicated batch runs multiply spend. A learner who understands idempotency understands half of AI cost control.

## Watch out

- **Do not teach this as a coding lesson.** The concepts survive any language; once the room starts debugging syntax, the integration thinking stops.
- **Do not demo only the happy path.** The teaching moment is the 429, the timeout and the truncated response.
- **The stale claim to retire:** "we'll harden the integration later." In practice the seam is what ships, and the model gets swapped underneath it.
