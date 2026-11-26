---
id: 07.03.A.A1
tsc: 7
level: Advanced
code: A1
title: Inventing the method: solving tasks no model was built for
as_at: 2026-11-26
review_by: 2027-02-25
---

# Inventing the method: solving tasks no model was built for

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A1**


> **Framework text (verbatim):** "Develop innovative methodologies for solving tasks with generative models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 12 of 20

**One-line version:** Innovation here is not a new architecture; it is recombining a small set of primitives — decompose, sample, verify, revise, constrain — against a diagnosed weakness.

## What it is

This ability is the design of a *method*: given a task with a hard requirement and a model that fails it naively, construct the surrounding procedure that makes it succeed — decomposition, sampling and selection, verification, retrieval, tool use, constrained decoding, or a learned adapter. The output is a pipeline you can defend, not a clever prompt.

## Deep expansion

### The concept

Every generative method is an answer to one question: *where does the correctness come from?* A model alone supplies plausibility. A method supplies one of four things on top of it:

1. **Decomposition** — split the task until each part is within the model's competence, then compose. Long computations, multi-document reasoning, and long-form generation all respond to this.
2. **Search** — generate many candidates and select with a scorer. Improvement is bounded by the scorer's quality, which is why a verifier matters more than the sampler.
3. **Verification** — a checker outside the model: a schema validator, a unit test, a calculator, a solver, a second model with a different prompt. Rejection sampling is the simplest useful form.
4. **Constraint** — restrict the output space so invalid answers cannot be produced: grammars, JSON schemas, typed function calls, enumerations.

A practical designer works backwards. Write down the failure, ask which of the four addresses it, and only then pick a technique. Teams that start from a technique ("let us use a multi-agent framework") produce elaborate systems that fail for the original reason.

### The sub-concepts

**Self-consistency and best-of-n.** Sample several reasoning paths, take the majority answer or the highest-scoring one. Cheap, effective on tasks with a discrete answer, useless where every answer is unique prose.

**Generate-and-verify with an external oracle.** Write code, run the tests, repair the failures; propose a schedule, check the constraints. This is the strongest pattern available and it is why code and mathematics improved fastest.

**Critic–reviser loops.** One pass critiques, another rewrites. Works when the critique has a rubric; degenerates into stylistic churn when it does not. Cap the iterations and require measurable improvement.

**Retrieval-grounded generation.** Attach the evidence and require citation of a retrieved span. Converts a knowledge problem into a reading-comprehension problem, which models do better.

**Constrained decoding and tool calls.** Grammar-constrained output guarantees parseability; tool calls move arithmetic and lookups outside the model entirely.

**Learned components.** When the failure is stylistic or structural and stable across inputs, a LoRA adapter is a legitimate method component — the last resort, not the first.

### How it connects to the rest of the framework

`TSC7-Advanced-A2` is the project that contains this work; `TSC7-Advanced-K4` is where the primitives come from in the literature. `TSC6-Advanced-A1` is the application-level equivalent, and `TSC5-Intermediate-A3` is how you prove the method actually fixed the failure. `TSC7-Advanced-A5` extends the method into agency.

### What is current as of November 2026

Two primitives have become much stronger. First, reasoning-style inference means the model itself now performs internal search, so methods that used to need explicit sampling loops can be handled inside one call — but the verification step has become more important, not less, because confident internal reasoning is still unverified. Second, agent protocols have made tool-augmented methods routine, so a designer's edge has shifted from "can I call a tool" to "which tool is a trustworthy oracle". Frontier systems of late 2026 — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and 4 Argon — are reliable enough at structured output that constraint-based methods now work in production rather than in demos.

### Common misconceptions

- *"A better prompt is a method."* A prompt is one component; without verification it is a hope.
- *"Ensembling models is always better."* Correlated models share failures; diversity of *method* beats diversity of vendor.
- *"More agents means more capability."* More agents means more compounding error unless each one is checked.
- *"If it works on my ten examples, the method generalises."* Ten examples test the demo, not the distribution.

## How a student should understand it

**Mental model:** a kitchen brigade. One cook can do a dish; a brigade with a pass, a checker and a plating standard can do three hundred identical dishes. The pass is the verifier.

**Three things they can do after this bullet:**
1. Take a failing task and name which of the four primitives addresses the failure.
2. Build a generate-verify loop with a real oracle.
3. State the cost and latency of the method and defend it against a simpler baseline.

**Misconceptions to kill:** that method design is prompt engineering, that more components mean more capability, and that a demo is evidence.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The exam script with a marking scheme.** A student who checks their work against the scheme does better than one who writes more. The scheme is the verifier; the extra writing is sampling without selection.

**The zi-char pass.** Dishes are checked before they leave the kitchen. Nobody plates and prays.

### Worked example with a real tool

Have learners design against a hard requirement:

```
Task: extract line items (description, quantity, unit price, GST)
from scanned invoices. Downstream accounting system rejects any
record that does not balance to the printed total.

Requirements: 99%+ field accuracy on balanced records, and never
emit a record that fails the balance check.

Design the method:
1. Which primitives you use, in what order, and what each fixes.
2. The verifier that enforces the balance rule, and why it is
   outside the model.
3. What happens when the model and the verifier disagree.
4. The failure path: how a rejected invoice reaches a human with
   the evidence attached.
```

What to point at afterwards: the balance check is a genuine oracle — the arithmetic either reconciles or it does not — so the method can refuse rather than guess. Learners who design "ask the model to double-check" have produced a correlated verifier, which is the same failure wearing a hat.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a model that is 92% accurate per field and 40% accurate per document; why?
2. **State the objective** — design a method with an external verifier and a refusal path.
3. **Recall prior learning** — error accounting from `TSC7-Advanced-K1`.
4. **Present the content** — the four primitives and working backwards from failure.
5. **Guide** — sketch the invoice method together.
6. **Elicit performance** — teams redesign a task from their own work.
7. **Give feedback** — test each design by asking "what does the verifier not catch?"
8. **Transfer** — each learner implements one primitive in a notebook before the next session.

## What the framework doesn't mention but trainers need to know

- **Per-step accuracy compounds.** Ninety-five percent at five steps is seventy-seven percent overall; decomposition must reduce steps or add checks.
- **Correlated verification is the most common design error.** A second sample from the same model is not an independent check.
- **Every method needs a refusal path.** Systems that cannot say "I could not" fail loudly in production.
- **Latency is a design constraint.** Best-of-32 is a research technique, not a product feature, at interactive speeds.

## Watch out

- **Do not let the class build a multi-agent system on day one.** It hides the failure they are meant to diagnose.
- **Do not equate novelty with quality.** A boring generate-verify loop usually beats an elegant architecture.
- **Do not skip cost accounting.** A method that triples inference cost needs a justification beyond accuracy.
- **The stale claim to retire:** "prompt engineering is dead, it is all agents now." In 2026 the primitives are the skill; agents are one arrangement of them.
