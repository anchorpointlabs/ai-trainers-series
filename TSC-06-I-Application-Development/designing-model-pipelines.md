---
id: 06.02.I.K5
tsc: 6
level: Intermediate
code: K5
title: Designing a model pipeline: where each stage earns its place
as_at: 2026-11-26
review_by: 2027-02-25
---

# Designing a model pipeline: where each stage earns its place

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Knowledge K5**


> **Framework text (verbatim):** "Designs of model pipelines."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Knowledge · Bullet 5 of 12

**One-line version:** A pipeline is a chain of small promises — and the design work is deciding which stage may fail quietly and which must stop the line.

## What it is

A model pipeline is an ordered set of stages, each taking a defined input and producing a defined output, where one or more stages call a model. It is how a task too large or too unreliable for a single prompt gets broken into steps you can test, trace, retry and price. Pipeline design is the craft of choosing those steps and the contracts between them.

## Deep expansion

### The concept

One giant prompt — "read this, extract that, decide, then write the email" — is easy to write and impossible to debug. When it fails, you cannot tell whether the reading, the extraction, the decision or the writing was wrong, and you cannot fix one without risking the others.

A pipeline trades a little latency and a little glue code for **attribution**: each stage's output is inspectable, so a failure has an address. That is the whole reason pipelines exist. The design question is not "how do I split this up" but "where do I need to see the intermediate result".

The typical sequence runs ingest → normalise → chunk → retrieve → build prompt → generate → validate → post-process → log. Most stages are deterministic code; usually only two or three call a model, and keeping that number small is the discipline. Every model call is variance, latency and cost; every deterministic stage is reliability.

### The sub-concepts

**Stage contracts.** Each stage declares its input and output shape, with a validator at the boundary. The failure is then caught where it happened instead of three stages later.

**Deterministic before probabilistic.** Clean, deduplicate, filter and template in code. A model should do the part that needs judgement, not the part a regex does for free and perfectly.

**Fan-out and fan-in.** Many documents summarised in parallel, then one synthesis over the summaries — the standard way to handle input larger than any context window, and the standard way to blow a budget if the fan-out is unbounded.

**Validation gates.** A stage that checks the previous one — schema valid, citations present, numbers in range — then repairs or stops. The gate is where quality is enforced, and it is usually cheap.

**Human checkpoint placement.** Some pipelines must stop for a person: before sending, before approving, before publishing. Where that gate sits is a design decision, not an afterthought.

**Tracing and replay.** Every run reconstructable: which prompt version, which chunks, which model, which tokens. Without replay you cannot improve a pipeline, only guess at it.

**Prompt as code.** Prompts are versioned, reviewed and deployed like any other artefact. A prompt edited live with no history is an outage waiting for a quiet Friday.

### How it connects to the rest of the framework

`TSC6-Intermediate-K1` supplies the contract thinking; `TSC6-Intermediate-K2` decides which model sits in which stage; `TSC6-Intermediate-A2` is the workflow that executes the pipeline. `TSC5` is where each stage gets evaluated, and `TSC6-Advanced-A1` is this bullet at scale, with several models composed deliberately.

### What is current as of November 2026

Pipelines have become cheaper to build and harder to reason about. Graph-based orchestration — state machines that declare stages, transitions and retry policy — replaced ad-hoc chaining for anything with a branch, because a plain chain cannot express "validate, and if it fails go back to retrieval". Structured outputs made validation gates practical, so more stages are safe to automate. And observability became a product category: you now read a trace of every stage, token and latency rather than grepping application logs.

### Common misconceptions

- *"More stages means better quality."* Each stage adds latency, cost and a failure mode. A stage must earn its place with a specific error it prevents.
- *"The pipeline is just the prompt chain."* The chain is the visible part. Retrieval, validation, caching and logging are where reliability lives.
- *"If the final output looks right, the pipeline is fine."* It may be right for the wrong reason, and it will break on the next input.

## How a student should understand it

**Mental model:** the prep line in a hawker kitchen. Wash, chop, blanch, wok, plate — the wok is the glamorous station, but a missed chop jams everything downstream.

**Three things they can do after this bullet:**
1. Take a one-prompt task and split it into stages, naming the contract at each boundary.
2. Say which stage is most likely to be wrong, and where the validation gate goes.
3. Point at the one place a human must approve before anything leaves the building.

**Misconceptions to kill:** more stages is better, the pipeline is the prompt chain, and a good final output proves a good pipeline.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The zi char prep line.** One station, one job, fixed hand-offs. When a dish comes out wrong you know which station to look at — that is attribution, and it is the entire value of a pipeline. Where it breaks: a kitchen mistake is visible immediately, while a model stage that errs produces fluent output that looks fine until it reaches the customer.

**PSLE marking.** Scripts collected, names masked, marked, moderated, checked. Nobody marks and moderates in the same pass, because a marker cannot reliably audit their own judgement. That is the validation gate and the human checkpoint in one.

### Worked example with a real tool

Run the same job twice — once as one prompt, once as three — and compare where the error enters. Single-shot, in ChatGPT or Claude:

```
Read this 40-page annual report and: summarise the financial position,
extract every action item management committed to, and draft a
200-word email to the board.
```

Then as three prompts in sequence: (1) summarise each section with page citations; (2) from the summaries, extract commitments into a table with page references; (3) write the email using only the table. What to point at afterwards: in the single-shot output you cannot tell which of the three jobs failed when a commitment is missing. In the pipeline version the table shows exactly which section dropped it, and the page numbers make it checkable. That is attribution — and it is what the extra two calls buy.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a one-prompt output that is subtly wrong, and the question of which part of the prompt caused it.
2. **State the objective** — you will design a staged pipeline with contracts and a validation gate, and justify each stage.
3. **Recall prior learning** — they have written multi-part prompts and know retrieval; this is the architecture around both.
4. **Present the content** — the reference sequence, then contracts, gates, fan-out, tracing.
5. **Guide** — convert the annual-report task into a pipeline on the board, stage by stage.
6. **Elicit performance** — pairs draw their own pipeline, marking model stages and gates.
7. **Give feedback** — the recurring error is a stage with no validator, or a fan-out with no ceiling.
8. **Transfer** — they add a stage diagram to their next build, before writing prompt one.

## What the framework doesn't mention but trainers need to know

- **Latency budget is a constraint, not a measurement.** Decide the ceiling first, then allocate seconds per stage, or you end up with four stages that cannot fit in a chat UI.
- **Cost multiplies through fan-out, not through stages.** Ten documents times a 2,000-token prompt is twenty thousand tokens per run, times users, times retries. Show the arithmetic.
- **Pipelines drift.** Someone adds a stage, someone edits a prompt, and the eval set no longer matches the system. A stage list in the repository keeps the diagram honest.
- **The best pipeline is usually shorter than the first draft.** Ask of every stage: what specific error does this prevent? "It might help" is not a reason.

## Watch out

- **Do not teach a framework's node graph as the concept.** The concept is contracts, gates and attribution; the library changes annually.
- **Do not demo a pipeline with no failure.** Break stage two deliberately and show the validator catching it, or the room concludes the gates are decoration.
- **Do not skip the cost arithmetic.** It is the number that decides whether the design ships.
- **The stale claim to retire:** "chain-of-thought prompting is a pipeline." It is one call with visible reasoning; a pipeline is separable contracts you can inspect, retry and price.
