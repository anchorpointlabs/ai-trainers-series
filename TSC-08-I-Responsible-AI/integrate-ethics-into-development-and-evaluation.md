---
id: 08.02.I.A8
tsc: 8
level: Intermediate
code: A8
title: Integrate ethics into development and evaluation
as_at: 2026-11-26
review_by: 2027-02-25
---

# Integrate ethics into development and evaluation

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A8**

> **Framework text (verbatim):** "Develop strategies to integrate ethics into AI development and evaluation of AI systems."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 13 of 14

**One-line version:** Ethics that is not in the definition of done is a hobby — the strategy is gates, artefacts and tests that fail the build.

## What it is

Integrating ethics means designing the lifecycle so that ethical requirements are stages rather than sentiments: a risk tier at intake, an impact assessment before data work, disaggregated evaluation before release, disclosure copy before launch, and a monitored owner after it. Evaluation is where most of it becomes measurable, which is why the bullet pairs the two.

## Deep expansion

### The concept

Integration is a design problem about friction. Make the ethical step an extra meeting and it will be skipped under deadline; make it a failing test in the pipeline and it will be fixed, because the pipeline does not argue. The strategy, therefore, is to convert each requirement into something with an owner, an artefact and a failure condition.

The second design constraint is proportionality. If every internal prototype needs a committee, engineering routes around governance — building outside the sanctioned path, using consumer tools, and creating the shadow AI problem the governance function was meant to prevent. The workable structure is a fast lane for low-risk use (approved tool, no personal data, no customer exposure, no autonomous action) and a deep lane for the rest. Governance credibility comes from being fast where it can be.

The third constraint is that evaluation must be specific. "Evaluate the model for fairness" produces a screenshot. "Run the disaggregated suite, report true-positive rate by group, block release below the agreed threshold, and record the result in the model card" produces a control.

### The sub-concepts

**Gates and artefacts.** Intake: risk tier and prohibited-use check. Design: impact assessment, data lineage, chosen fairness metric, oversight model. Pre-release: model card, evaluation report, guardrail configuration, kill switch tested. Post-release: monitoring, drift and override rates, periodic re-validation. Each gate has a named approver, and the approval is recorded.

**Evaluation as code.** Adversarial prompts, bias slices, grounding checks and regression cases live in a test suite that runs on every change. Singapore's Project Moonshot and AI Verify are the obvious starting points; the principle is that a known failure becomes a test the same week it is found.

**The definition of done.** Bias slices reported, disclosure copy written, escalation path documented, owner named. If it is not on the ticket, it does not happen.

**Change management.** A model version swap, a corpus refresh or a system prompt change re-opens the gate. This is the control most organisations lack, and it is the one that invalidates every earlier approval.

**Independent challenge with actual authority.** The second line validates and can veto. A governance function that can only advise is a suggestion box with a calendar.

**Monitoring as part of evaluation.** Evaluation does not end at launch. Override rates, refusal rates, complaint patterns and drift are evaluation data.

### How it connects to the rest of the framework

`TSC8-Intermediate-A1` is the stage-by-stage check this bullet institutionalises; `TSC8-Intermediate-A3` and `TSC8-Intermediate-A4` are the mitigation and trade-off decisions the gates are there to capture; `TSC8-Intermediate-A7` is how you choose the framework the gates implement. `TSC8-Intermediate-K5` supplies the obligations that make some gates legally mandatory rather than merely wise.

### What is current as of November 2026

The tooling has caught up with the idea. Evaluation harnesses run in CI, red-team suites are versioned alongside code, and providers publish evaluations you can use as a baseline — the GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon each ship capability and safety documentation with their releases.

The new gap is agentic change management. An agent's behaviour depends on its tool permissions and its prompt as much as its weights, so a permissions change is a model change and should re-open the gate. Most pipelines do not track that yet, and the omission is where incidents will come from. Model version pinning — knowing exactly which version is live and refusing a silent upgrade — is the cheapest control available and the one most often missing.

### Common misconceptions

- *"We have an ethics review meeting."* Meetings do not fail builds. Tests do.
- *"Evaluation means accuracy on a test set."* Accuracy is one dimension; slices, calibration, grounding, refusal behaviour and robustness are the others.
- *"One gate at launch is enough."* Every material change re-opens it, which is why change management is the senior skill here.
- *"Governance has to be slow to be credible."* Slow governance is bypassed governance.

## How a student should understand it

**Mental model:** seatbelts engineered into the chassis, not inspected at the factory exit. The control exists where the work happens, or it does not exist.

**Things they can do after this bullet:**
1. Place the four gates on a lifecycle and name the artefact for each.
2. Turn one known failure into a regression test in the suite.
3. Write the change-control rule for model, prompt and permission changes.

**Misconceptions to kill:** that a meeting is a control, that evaluation is one number, and that launch approval is permanent.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The BTO inspection stages.** Foundation, structural, then TOP. You cannot inspect the foundation after the flat is finished — the sequence is the control, not the paperwork. Where it breaks: a building's stages are fixed and slow; a model can change weekly, so the gates must be triggered by change rather than by calendar.

**The live-firing safety check before the outfield exercise.** Nobody argues that it slows the exercise down; the check is why the exercise is allowed to happen. Governance bought with a checklist is cheaper than governance bought with an incident.

### Worked example with a real tool

```text
We are building a document-summarisation assistant for a law firm's internal knowledge base.
Draft the integration plan.

1. Risk tier, with the reason.
2. Four gates, and for each: the artefact required, who approves, and what would cause a fail.
3. The evaluation suite: six test categories, with one concrete example prompt per category.
4. The change-control rule: which changes re-open which gate.
5. The three metrics that would tell us, 90 days after launch, that the integration is working
   rather than being theatre.
```

What to point at afterwards: the model will write a clean gate table and then produce metrics that measure activity (reviews completed) rather than effect (defects caught before release, override rate, incidents). Point at question 5 — activity metrics are how integration decays quietly.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a post-incident timeline and mark where each gate would have caught it.
2. **State the objective** — by the end you can design gates and an evaluation suite for your project.
3. **Recall prior learning** — return to the checkpoints from A1 and the tiering idea.
4. **Present the content** — four gates, artefacts, evaluation as code, change management, fast lane.
5. **Guide** — draft the summarisation plan together.
6. **Elicit performance** — teams design gates for their own project.
7. **Give feedback** — mark any gate without a failure condition.
8. **Transfer** — each learner adds the change-control rule to their release checklist.

## What the framework doesn't mention but trainers need to know

- **The fastest way to be bypassed is to be slow.** Publish the fast-lane criteria or engineers will invent their own.
- **Automate the evidence.** If the model card is written by hand at the end, it will be written by whoever is least busy, and it will be optimistic.
- **Make the gate fail loudly.** A warning that can be ignored is a warning that will be.
- **Ethics sign-off must not sit with the delivery manager** who is measured on shipping date.

## Watch out

- **Do not design a gate nobody can pass.** It teaches the organisation to route around governance.
- **Do not treat a green dashboard as proof.** Dashboards show what was instrumented.
- **Do not skip the kill switch.** Test that you can turn it off in minutes, not that you have a document saying you could.
- **The stale claim to retire:** "we do ethics at the end of the project." In November 2026 it is a pipeline stage, and the pipeline runs on every commit.
