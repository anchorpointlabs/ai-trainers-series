---
id: 07.02.I.A1
tsc: 7
level: Intermediate
code: A1
title: Building a custom generative model for one task and one domain
as_at: 2026-11-26
review_by: 2027-02-25
---

# Building a custom generative model for one task and one domain

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A1**


> **Framework text (verbatim):** "Construct custom generative models for specific tasks and domains."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 11 of 17

**One-line version:** Custom means fitted to your task and your data — not invented from nothing, and not the biggest model you can rent.

## What it is

Constructing a custom generative model is the work of turning a vague business need into a specified task, choosing and adapting an architecture that suits it, and wrapping the result in constraints and evaluation so it behaves in production. Almost always it starts from an existing model. The custom part is the framing, the data, the conditioning and the guardrails around it.

## Deep expansion

### The concept

Twelve years ago "build a model" meant architecture design. Now the architecture is a commodity and the differentiation is in specification: what exactly goes in, what exactly comes out, what counts as failure, and what the system must never do. A learner who can write that specification — and then pick the smallest base model that meets it — is more valuable than one who can recite transformer variants. The discipline is to start with a baseline you can beat: a prompt-only solution, then retrieval, then an adapter, and only then a more ambitious build.

### The sub-concepts

**Framing the task.** Name the input type (text, image, audio, tabular row), the output type (free text, structured JSON, an image, a decision), the ambiguity in between, and the cost of each error class. Structured output changes everything downstream: a schema gives you a verifier, and a verifier gives you a metric.

**Choosing a base.** Match the base to the constraint that actually binds — latency, on-premises hosting, cost per call, language coverage, licence. A small specialised model that fits on your own hardware sometimes beats a frontier API for a narrow repeatable task, and the reverse is true the moment the task widens.

**Constraints as design.** Most production reliability comes from outside the weights: constrained decoding against a grammar, required citations, deterministic post-processing, tool calls instead of free-form answers, and refusal paths that route to a human. Learners routinely try to fix with training what a schema would fix in an afternoon.

**The evaluation loop.** A regression set built from real cases, a task metric, a human review cadence, and a rule that data changes get tried before architecture changes. The loop is the method; the model is the current output of it.

### How it connects to the rest of the framework

`TSC7-Intermediate-K2` supplies the architecture families and their hardware; `TSC7-Intermediate-K8` is the dataset construction this depends on; `TSC7-Intermediate-K4` defines the metric panel; `TSC7-Intermediate-A5` and `TSC7-Intermediate-A7` are the tuning and pre-training abilities used inside the build; `TSC6` covers the application layer that will call the model.

### What is current as of November 2026

- **Custom work is post-training plus plumbing.** Most "custom models" built on current frontier models are an adapter, a schema, a retrieval index and a guardrail — not a new architecture.
- **Small specialised models became viable again.** Distillation from a strong API model into a small open-weight model now produces domain assistants that run cheaply on-prem.
- **Constrained decoding is standard.** Grammar-based output and function calling have made "the model returns exactly this shape" an engineering default rather than a research hope.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Custom means from scratch."* From scratch needs a corpus and a compute budget you do not have; adapting does not.
- *"Bigger base, better result."* For a narrow task with clean data, a well-tuned small model often wins on cost and latency at equal quality.
- *"The model should handle every case."* Post-processing, schemas and escalation paths handle edge cases better and cheaper than more training.
- *"We'll define success after we see the output."* Without a definition first, every output looks acceptable and nothing can be rejected.

## How a student should understand it

**Mental model:** tailoring a uniform. You do not weave the cloth or grow the cotton; you take a good base fabric, cut it to this unit's measurements, and add the badges that make it theirs.

**Three things they can do after this bullet:**
1. Write a one-page task specification with input, output, failure classes and metric.
2. Choose a base model and adaptation strategy that fits the binding constraint.
3. Build a regression set from real cases before writing training code.

**Misconceptions to kill:** that custom means from scratch, that size equals quality, and that the model must own the edge cases.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The school uniform tailor.** Uniforms come from a standard fabric and a standard pattern; the tailor takes measurements, adjusts the cut and sews on the school badge. Nobody expects the tailor to spin the thread. Where it breaks: a bad measurement is visible immediately on a uniform, while a bad task specification only shows up after training.

**The zi char stall's house special.** The stall does not invent a new cuisine; it takes a familiar technique and adjusts the seasoning to the estate's taste, then keeps a small notebook of what customers send back. That notebook is the regression set. Where it breaks: the stall hears every complaint at the counter; a deployed model hears only the failures somebody bothers to report, which is a much thinner notebook.

### Worked example with a real tool

A learner wants to turn free-text clinic referral notes into a fixed JSON record. Type this into a coding assistant:

```
I need a spec and a first implementation for a custom model that
converts referral notes into this schema:
{patient_age, condition, urgency: [routine|soon|urgent],
 requested_tests: [..], referring_dept}

1. Write the task specification: input, output, the five failure
   classes I should measure, and what "urgent" must never be wrong on.
2. Write a baseline using a frontier API with a strict JSON schema
   and few-shot examples; evaluate on 50 held-out notes.
3. If the baseline misses the bar on urgency, write a LoRA SFT
   script on my 800 labelled notes with the same schema, and an
   evaluation that compares both on the same 50.
4. Add a post-processing validation step that rejects any record
   where urgency is 'urgent' and condition is missing, routing it
   to a human queue.
```

Point at step 1 (the failure classes drive everything), step 2 (the baseline is the bar, not a formality), and step 4 — the rejection path is part of the model design, not an afterthought.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a custom model that fails on the one case the business cares about.
2. **State the objective** — write a task spec and a baseline plan in one hour.
3. **Recall prior learning** — architectures, datasets, metrics from the earlier bullets.
4. **Present the content** — framing, base choice, constraints, evaluation loop.
5. **Guide** — turn one vague request into a specification together.
6. **Elicit performance** — teams write specs for their own use cases.
7. **Give feedback** — critique: is every failure class measurable?
8. **Transfer** — each learner runs the prompt-only baseline this week.

## What the framework doesn't mention but trainers need to know

- **The requirements conversation is the hard part.** Most failed builds solved the wrong problem precisely; the interview with the user matters more than the architecture choice.
- **Small models have a quality cliff.** They excel inside the distribution and fall off sharply outside it, so the escalation path is not optional.
- **Iteration cost is dominated by evaluation, not training.** Budget the labelling time for the regression set before you budget GPU hours.
- **Data rights follow the model.** A custom model trained on customer data inherits obligations about that data, including where it may be hosted.

## Watch out

- **Do not demo training a transformer from scratch on a few hundred rows.** It teaches the wrong instinct and produces a useless artefact.
- **Do not skip the prompt-only baseline.** Without it, nobody can say whether the custom build earned its cost.
- **Do not treat the schema as decoration.** It is the cheapest reliability you will ever add.
- **The stale claim to retire:** "we need a custom model for that." In November 2026 the first question is whether a prompt, a schema and a retrieval index already solve it.
