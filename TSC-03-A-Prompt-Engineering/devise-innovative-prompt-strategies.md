---
id: 03.03.A.A6
tsc: 3
level: Advanced
code: A6
title: Devise innovative prompt strategies
as_at: 2026-11-26
review_by: 2027-02-25
---

# Devise innovative prompt strategies

> **TSC #3 Prompt Engineering · Advanced · Ability A6**

> **Framework text (verbatim):** "Devise innovative prompt strategies that enhance generative AI capabilities."
>
> **TSC #3** Prompt Engineering · **Advanced** · Ability · Bullet 13 of 13

**One-line version:** Innovation here is composition — splitting a hard task into stages and giving each stage the technique and the check it needs — not discovering a new magic phrase.

## What it is

A strategy is a sequence of prompts, each with a single job, wired so that one stage's output becomes the next stage's input — with a verification step somewhere in the middle or at the end. Devising one is four moves: decompose the task, assign a technique to each stage, build the check, define the handoff format. The creativity lives in the decomposition and in finding a verification signal that is not the model's own opinion.

## Deep expansion

### The concept

A single prompt is one forward pass of text generation. That makes it good at one job and bad at six, because six jobs in one instruction compete for attention and the model silently drops the ones it is least sure about. The symptom is familiar: accuracy plateaus around two-thirds no matter how the wording is tuned, and fixing one part breaks another.

Decomposition changes the shape of the problem. Extract, then check, then format. Draft, then verify, then revise. Plan, then execute, then test. Each stage is small enough to be specified, cheap enough to be tested alone, and debuggable — when the pipeline is wrong you can see which stage produced the wrong output, instead of staring at one output and guessing.

What makes this "innovative" rather than merely tidy is the third move: **verification**. A pipeline of three generative stages is three chances to be plausible and wrong. The strategy that enhances capability is the one where at least one stage compares output against something that is not the model's judgement — the source document, a calculation, a schema, a tool result. That is where the real engineering is, and it is where most classroom designs stop short.

### The sub-concepts

**One job per stage.** "Extract the clauses, judge compliance and draft an email" is three stages pretending to be one. Each stage should have a verb, an input and a checkable output.

**The handoff is a contract.** Stage two receives stage one's output, so that output must be structured — a list, a table, JSON with named fields. Free prose between stages is where facts get lost.

**Error propagation is the tax.** If stage one misses a clause, stages two and three build on the gap and the final answer is confidently wrong. Mitigate with explicit "not found" values rather than silence, and with a check on the stage that can fail quietly.

**Verification must be external.** A stage that asks the model to check its own work produces agreement. Use the source document, a recomputation, a schema validator, or a second prompt given only the claim and the evidence — not the draft.

**Novelty is not complexity.** The best strategy for most tasks is two stages and a check. Adding stages buys capability at the cost of latency, tokens and failure surface; every added stage must earn its place with a named failure it prevents.

**Compose what you already know.** Few-shot for the boundary case, chain-of-thought for the calculation, structured output for the handoff, an abstention clause for the gap. Innovation is arrangement, not invention.

### How it connects to the rest of the framework

This bullet composes the rest. Bullet 5 (`TSC3-Advanced-K5`) supplies retrieval and tools as stages; Bullet 4 (`K4`) supplies reasoning stages; Bullet 3 (`K3`) supplies the ordering and the one-variable discipline; Bullet 12 (`A5`) is the refine-or-extend decision each stage will face; Bullet 10 (`A3`) is how the whole pipeline is judged. `TSC6` is where the pipeline becomes software.

### What is current as of November 2026

- **Staged pipelines became the default architecture.** With current frontier models, generating several candidates, checking them against a source and selecting is cheap enough to be routine — the multi-stage strategy that once required engineering is now a few API calls.
- **Structured output made handoffs reliable.** Enforced schemas removed the parsing failures that used to make stage boundaries brittle, which shifted the difficulty from plumbing to deciding what each stage should guarantee.
- **The innovation frontier moved to verification.** Because anyone can chain three prompts, the designs that stand out are the ones with a real check: entailment against the cited passage, recomputation of a figure, a schema that cannot be satisfied by a guess.
- **Agents collapsed some pipelines into loops.** Where the model can call tools itself, part of the staging moves inside one agentic loop — better on open-ended tasks, harder to audit, and a reason to keep the verification step outside the loop.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A cleverer single prompt beats a pipeline."* Sometimes, for simple tasks. For six-job tasks the plateau is real and no wording passes it.
- *"Innovation means a new technique."* It means a new arrangement of known techniques for your specific problem.
- *"More stages is more advanced."* Two stages and a check beats five stages and a hope.
- *"The model can verify itself if I ask firmly."* Self-checking produces agreement unless it is anchored to something external.
- *"If the pipeline works on one case, it works."* Each stage needs its own test set, and the pipeline needs an end-to-end one.

## How a student should understand it

**Mental model:** the zi char kitchen. One station fries, one steams, one plates — and nothing leaves the pass until the expediter has looked at it against the order slip. The expediter is the verification stage, and without that station the kitchen is just fast.

**Things they can do after this bullet:**
1. Decompose a hard task into stages with one job each.
2. Assign a technique to each stage and justify the choice.
3. Build a verification step that uses something external, and explain what it catches.

**Misconceptions to kill:** that one great prompt is the goal; that stages are free; that the model can be its own auditor.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The zi char pass.** Four woks, one expediter, one order slip. The expediter does not cook; they compare what arrives against what was ordered and send it back. Where it breaks: a human expediter can taste; your verification stage can only compare, so it needs the evidence placed in front of it.

**The two-marker rule at an exam.** One marker scores, a second checks against the scheme. It works because the second marker sees the scheme and the script, not the first marker's reasoning. Where it breaks: examiners are trained and moderated; your checking prompt inherits its biases from its model, so the rubric must be explicit and the evidence supplied.

### Worked example with a real tool

```text
Task: check whether a supplier contract complies with 5 clauses.
Design a 3-stage prompt:
(1) extract the clauses from the contract,
(2) check each against the contract,
(3) output a compliance table with a 'verify me' column.
```

Then build it properly. Stage 1 returns a JSON list with clause id, verbatim quote and page. Stage 2 receives that list and one clause at a time, and must answer "complies / does not comply / not found" with the quote it relied on — the abstention option is what stops invention. Stage 3 formats a table with a column holding the verbatim quote, so a human can check each row in five seconds.

Point at stage 2's abstention and stage 3's quote column: those two design choices are the innovation, not the three stages. Then remove the abstention and re-run on a contract missing one clause — the pipeline reports compliance for a clause that is not there, with a fabricated quote. That failure, visible in the table, is why the verification column exists.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — present a task that defeats a single prompt; show the plateau, not just a failure.
2. **State the objective** — decompose a task into stages, assign techniques, and build one external check.
3. **Recall prior learning** — how a kitchen, an audit or a marking process divides work and checks it at a pass.
4. **Present the content** — the four moves; one job per stage; handoff contracts; external verification; the cost of stages.
5. **Guide** — build the contract-compliance pipeline together, then break it by removing the abstention.
6. **Elicit performance** — groups design a staged strategy for a real task from their organisation and pitch it in three minutes.
7. **Give feedback** — the room votes on the strongest design, and must say which stage carries the verification and what it catches.
8. **Transfer** — each learner drafts stage one of their strategy and the check it will be measured against.

## What the framework doesn't mention but trainers need to know

- **Design the check before the stages.** Deciding what would prove the output right tells you what each stage must produce. Teams that design stages first end up with a pipeline nobody can verify.
- **Stage contracts prevent silent corruption.** Missing values must be explicit (`null`, `NOT_FOUND`), never blank — a blank is read as "fine" downstream.
- **The pipeline needs an owner and an end-to-end test.** Stage tests catch stage bugs; only an end-to-end set catches the interactions.
- **Cost accumulates invisibly.** Five stages times two candidates times a thousand runs is a different budget class from one prompt. Model the volume before building.
- **Human checkpoints belong where the cost of error is asymmetric.** A compliance table gets a human sign-off; a draft email does not. Put the checkpoint where the money is.

## Watch out

- **Do not reward complexity in the pitch.** Ask what each stage prevents, and cut the ones that cannot answer.
- **Do not let "innovative" mean unmeasured.** A novel strategy with no test set is a demo.
- **Do not build three stages when one works.** Prove the plateau before decomposing.
- **Do not let the model audit itself.** Self-review produces agreement; verification needs evidence.
- **The stale claim to retire:** "the best prompt is one giant prompt." In November 2026 the reliable designs are small stages with explicit handoffs and a check at the end.
