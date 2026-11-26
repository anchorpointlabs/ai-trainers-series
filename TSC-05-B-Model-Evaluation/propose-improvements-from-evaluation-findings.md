---
id: 05.01.B.A3
tsc: 5
level: Basic
code: A3
title: Propose improvements from evaluation findings
as_at: 2026-11-26
review_by: 2027-02-25
---

# Propose improvements from evaluation findings

> **TSC #5 Generative AI Model Evaluation · Basic · Ability A3**


> **Framework text (verbatim):** "Propose initial improvements based on evaluation findings."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Ability · Bullet 9 of 11

**One-line version:** An evaluation that ends at "here is what is wrong" is half a job — the skill is turning each finding into a specific, testable change aimed at the right layer.

## What it is

This is the ability to convert evaluation findings into proposed fixes: given "the output is incoherent" or "the diversity is low", name what to change and at which layer — the prompt, the data, the model, or the workflow around it. The proposals are *initial*: reasoned first moves to try, not guaranteed cures, and each one should be testable against the same evaluation that found the problem.

## Deep expansion

### The concept

Findings describe the symptom; proposals name the treatment. The crucial skill is matching the symptom to the right layer, because the same failure can have different causes. Low relevance could be a bad prompt (fix the prompt), missing context (fix the retrieval), a stale model (fix the model), or a wrong task for the tool (fix the workflow). Proposing well means diagnosing *where* the failure lives before prescribing *what* to change — and always tying the proposed fix back to a measurable re-test.

### The sub-concepts

**Layer one: the prompt.** Most Basic-level failures are prompt failures. Vague instructions, missing context, the wrong criterion emphasised. The cheapest first proposal is almost always "restate the task precisely and give it the context it needs."

**Layer two: the context and data.** If the model lacks facts, the fix is retrieval or supplying the right source material — not retraining. This is the fix for most "the model doesn't know our business" findings.

**Layer three: the model or its settings.** Changing the model, the size, or sampling settings (temperature) is a fix for diversity, latency and cost findings — and it is the layer learners reach for first when they should reach for it last.

**Layer four: the workflow.** Sometimes the right fix is not in the model at all — add a human check, change who uses the output, or stop using AI for this task entirely. Proposing "don't use it here" is a legitimate, often the best, improvement.

### How it connects to the rest of the framework

This is the closing link in the Basic loop: `TSC5-Basic-A1` (collect feedback) → `TSC5-Basic-A2` (interpret metrics) → **A3** (propose the fix). It draws on `TSC5-Basic-K4` (limitations), because the right layer is usually dictated by *which* limitation caused the failure. It also reaches into `TSC4` (model selection) — a proposal to switch models is the moment Basic evaluation touches model selection — and `TSC2` (prompt design), since layer-one fixes are prompt fixes.

### What is current as of November 2026

The discipline has shifted from "try things until it works" to **"propose the cheapest fix that could work, then measure."** Because late-2026 models are all fluent and broadly capable, the most common failures are context and workflow failures rather than raw model-capability failures — which means the highest-value proposal is usually "give it the right context" or "put a human check on the risky step", not "buy a bigger model". A good Basic practitioner proposes from the cheapest layer up.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The fix is always a better prompt."* Often, but not always. A fact the model does not have cannot be prompted into existence — that needs retrieval, not better wording.
- *"If it underperforms, get a bigger model."* The most expensive fix, and usually the wrong first move. Try prompt, then context, then workflow, before spending on a bigger model.
- *"A proposal is a promise."* A proposal is a hypothesis to test. It only becomes an improvement when the re-evaluation confirms it.

## How a student should understand it

**Mental model:** a doctor's visit. The symptom is "headache"; the good doctor does not reach for the strongest drug — she asks where it hurts and proposes the cheapest plausible cause first (sleep, water, glasses), escalating only if the re-check shows no change. Evaluation findings are symptoms; proposals are the treatment plan, from least to most invasive.

**Three things they can do after this bullet:**
1. Given one evaluation finding, name which layer the failure lives in (prompt, context, model, workflow) and why.
2. Propose the cheapest fix first and say how they would re-test it.
3. Recognise when the right proposal is "stop using AI for this task", and say it.

**Misconceptions to kill:** fix = always prompt, underperform = bigger model, and proposal = promise.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The four-floor repair.** In his own training-and-QA framing: a complaint goes to the right floor. Is the problem the instruction given (the prompt), the materials on hand (the context), the tool itself (the model), or the process around it (the workflow)? Sending a plumbing complaint to the carpentry floor wastes everyone's time — and proposing a new tool when the instruction was wrong is the same error.

**The car that won't start.** You do not replace the engine first. You check the battery, then the fuel, then the starter — cheapest and most likely cause first. Proposing improvements follows the same ladder, and "replace the engine" (a new model) is the last rung, not the first.

### Worked example with a real tool

Give the room a finding, then make them propose the ladder. Start with a live failure:

```
Ask the model: "Summarise our leave policy for the staff handbook."
(You have given it no policy document.)
```

What to point at afterwards: the model either invents a policy or asks for it — either way the *finding* is "relevance failure". Walk the four layers: is it the prompt (mostly fine), the context (yes — no policy was supplied), the model (no), the workflow (possibly — a summarise task should have the source attached). The correct proposal is layer two: attach the actual policy text, then re-test. That is the whole ability in one worked example — and the moment learners stop reaching for "get a better model".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a confident, wrong output and ask "what do we do about it?" Collect "get a better model" answers.
2. **State the objective** — you will turn any finding into a proposal aimed at the right layer, cheapest first.
3. **Recall prior learning** — they know the limitations (K4); the right layer is set by which limitation caused the failure.
4. **Present the content** — the four layers, cheapest-first, proposal-as-hypothesis.
5. **Guide** — work the leave-policy failure through all four layers together.
6. **Elicit performance** — each learner takes one finding from their own work and proposes a layer-one fix plus a re-test.
7. **Give feedback** — correct the learner who proposed a model switch for what was a missing-context problem.
8. **Transfer** — on their next AI task that underperforms, they write the four-layer ladder and pick the cheapest plausible fix.

## What the framework doesn't mention but trainers need to know

- **"Stop using AI" is a valid proposal.** The framework assumes improvement; the honest trainer teaches that sometimes the correct improvement is to not use the tool for that task at all. It is the most under-proposed fix and often the best one.
- **One change at a time.** Proposing three fixes at once makes the re-test uninterpretable — you will not know which one worked. Teach "one change, one re-test" as the discipline.
- **The proposal must be testable.** A fix with no way to measure whether it worked is not a proposal, it is a wish. The re-test is part of the proposal, not an afterthought.

## Watch out

- **Do not let the room skip to "buy a bigger model".** That is the most expensive and least thoughtful proposal, and it is the default reflex of novices. The four-layer ladder exists precisely to block it.
- **Do not present proposals as certainties.** Say "propose" and "hypothesis" and "re-test", not "fix". A learner who believes they have *solved* it on paper will not re-measure, and unverified fixes are how bad changes ship.
- **The stale claim to retire:** "we evaluated it, so we're done." Evaluation is the diagnosis; without a proposal and a re-test it changes nothing. Findings that do not become proposals are just expensive opinions.
