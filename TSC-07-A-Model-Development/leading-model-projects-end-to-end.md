---
id: 07.03.A.A2
tsc: 7
level: Advanced
code: A2
title: Leading a model project: the seven gates from idea to production
as_at: 2026-11-26
review_by: 2027-02-25
---

# Leading a model project: the seven gates from idea to production

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A2**


> **Framework text (verbatim):** "Lead and manage generative AI projects from conception to deployment."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 13 of 20

**One-line version:** A generative AI project fails in the same seven places every time, and each one has a gate you can put in front of it.

## What it is

This ability is running a model project end to end: framing the problem so that a generative approach is justified, proving data feasibility before promising a model, designing the evaluation before training, and taking the thing to production with monitoring, ownership and a retirement plan. It is a management ability with technical teeth.

## Deep expansion

### The concept

The seven gates, in order, each cheap to pass or fail and expensive to skip:

1. **Problem framing.** Is the task well-defined enough to be scored? "Improve customer experience" is not; "route these 400 ticket types to the right queue with 90% agreement with human routing" is. If you cannot write the scoring rule, stop.
2. **Baseline.** The dumbest thing that works — keyword rules, a small model, a human with a checklist. Without a baseline you cannot demonstrate value, only activity.
3. **Data feasibility.** Do the examples exist, may you use them, and are they labelled consistently? This gate kills more projects than modelling does.
4. **Proof of concept.** Small, on real data, with the evaluation defined up front. Its purpose is to fail cheaply.
5. **Evaluation design.** A frozen set, a rubric or metric, a human review sample, and an agreed threshold that means "ship".
6. **Pilot.** Real users, real volume, monitored, with a rollback. Success criteria written before launch.
7. **Production and ownership.** Serving, cost control, drift monitoring, incident process, and a named owner with a deprecation date.

Most failures are gate 3 or gate 5 being waved through, because both are boring and both are someone else's job until they are not.

### The sub-concepts

**Scope as an engineering artefact.** Write the model card and the non-goals at the same time. "Not for legal advice" is a deliverable.

**The risk register.** Data rights, evaluation validity, cost overrun, vendor dependence, and reputational exposure to a bad output. Each needs an owner and a trigger, not a paragraph.

**Honest status reporting.** Report the metric and its interval, the sample size, and what the last negative result was. A project that has never had a negative result is not being measured.

**Vendor and build decisions.** Buy the model, own the pipeline. The differentiator is rarely the base model; it is the data, the evaluation and the integration.

**Governance checkpoints.** Personal data, sectoral rules and internal policy review are gates, not paperwork; run them at framing and again before pilot.

### How it connects to the rest of the framework

`TSC7-Advanced-A7` and `A8` cover the research side; this bullet is the delivery side. `TSC5-Advanced-A3` covers leading evaluation projects specifically. `TSC6-Intermediate-A2` covers the integration workflows a project must produce, and `TSC8-Intermediate-K6` is the governance layer that gates 1 and 6 must satisfy.

### What is current as of November 2026

Project economics have shifted toward smaller, cheaper, fine-tuned models with a strong evaluation harness, because the marginal gain from a frontier model on a narrow task is often small while the cost difference is large. The late-2026 frontier releases — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and 4 Argon — are all positioned on reliability over long tasks, which raises stakeholder expectations: they assume agents can be trusted with multi-step work, and a project lead has to set the actual reliability bar with evidence. Expect more scrutiny of evaluation claims than of model choice.

### Common misconceptions

- *"We will define success criteria after the prototype."* Then the prototype defines them, and it always succeeds.
- *"The hard part is the model."* The hard parts are data rights, evaluation validity and the last mile of integration.
- *"A pilot that nobody complains about is a success."* Silence is not adoption; measure usage and override rate.
- *"Deployment is the end."* Deployment is the start of the drift clock.

## How a student should understand it

**Mental model:** a BTO flat. Milestones, inspections and a handover with a defects list — not a heroic sprint to a key.

**Three things they can do after this bullet:**
1. Write a framing statement with a scoring rule, a baseline and a non-goal.
2. Run a data-feasibility check in a week rather than a quarter.
3. Present status with intervals, sample sizes and the last negative result.

**Misconceptions to kill:** that evaluation comes after building, that a pilot without complaints is a success, and that deployment closes the project.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**BTO milestones.** Foundation, structure, fittings, inspection, handover. You cannot skip the inspection because the tiles look nice. Where it breaks: a flat has one owner and one deadline; a model project has stakeholders who want the tiles moved after handover.

**The hawker licence.** You do not open the stall and then apply; the licence, the hygiene grade and the gas certification come first, and everyone in the trade knows it.

### Worked example with a real tool

Get the framing written in fifteen minutes:

```
We want to use AI to reduce time spent on procurement queries.
Budget: one quarter, two engineers, no new headcount.

1. Rewrite the objective so it can be scored, with a metric and
   a threshold that means "ship".
2. Give me the baseline we must beat, and why it is fair.
3. List the five data-feasibility questions we must answer before
   writing any model code, in the order that kills the project
   fastest.
4. Write three non-goals for the model card.
5. Name the gate most likely to fail and the evidence that would
   tell us in week two.
```

What to point at afterwards: question 3 is where the room learns something. Most learners list technical questions; the lethal ones are about rights, label consistency and whether the answer even exists in the data. Point out that a project can be killed in week two for a good reason, and that this is a success.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a project timeline with the data gate failed at week nine, after the demo.
2. **State the objective** — produce a framed brief with gates, baseline and non-goals.
3. **Recall prior learning** — evaluation design from `TSC5-Intermediate-K4`.
4. **Present the content** — the seven gates and the two that usually fail.
5. **Guide** — complete the procurement framing together.
6. **Elicit performance** — teams write a one-page brief for a project they know.
7. **Give feedback** — peer review against the gate questions.
8. **Transfer** — each learner books the data-feasibility conversation with a real colleague.

## What the framework doesn't mention but trainers need to know

- **Budget for the evaluation harness at 20–30% of effort.** It is not optional and it is not free.
- **The vendor can change the model under you.** Pin versions, and keep a golden set to detect silent behaviour change.
- **Adoption is a product problem.** A model behind a bad interface is a failed project with a good metric.
- **Write the deprecation plan at launch.** Models are retired; a system with no plan becomes an unmaintained liability.

## Watch out

- **Do not teach project management generically.** Every gate must be tied to a model-specific failure.
- **Do not let a success story stand without its negative result.** It trains the room to hide bad news.
- **Do not equate a demo with a proof of concept.** The difference is real data and a defined metric.
- **The stale claim to retire:** "we will pick the model once we see the results." In 2026 model choice is a late, cheap decision; the data and evaluation are the project.
