---
id: 04.03.A.K3
tsc: 4
level: Advanced
code: K3
title: Deploying and fine-tuning AI models
as_at: 2026-11-26
review_by: 2027-02-25
---

# Deploying and fine-tuning AI models

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K3**

> **Framework text (verbatim):** "Workflow of deploying and fine-tuning AI models."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Knowledge · Bullet 3 of 8

**One-line version:** Fine-tuning and deployment are one lifecycle, not two events — data in, adapter trained, evidence gathered, version pinned, behaviour watched.

## What it is

The workflow runs in a fixed order: define the constraints, prepare and clean the data, choose a base model, fine-tune, evaluate against a held-out set, deploy behind a gateway with an immutable version, then monitor. Each step has an exit condition. Skipping the exit condition is how teams end up with a model in production that nobody can explain, reproduce or roll back.

## Deep expansion

### The concept

The sequence is chronological for a reason: every later step inherits the defects of the earlier ones. Bad data produces a model that fails evaluation; a missing evaluation produces a deployment that fails silently; an unpinned deployment produces a system whose behaviour changes overnight with no code change and no incident ticket.

The framework says "workflow", which understates it. In practice the loop does not close — it keeps running. Production failures get promoted back into the evaluation set, the evaluation set triggers a retrain, the retrain ships through the same gate. Teams that treat deployment as the finish line run the loop blind.

### The sub-concepts

**Step 1 — constraints before candidates.** Write down the immovable boundaries: may the data leave Singapore, which modality is needed, what latency the interface demands, what the unit cost ceiling is. This single step eliminates most of the market and prevents the expensive habit of falling in love with a model you are not allowed to use.

**Step 2 — data preparation is most of the work.** Fine-tuning needs clean, consistent, human-verified input–output pairs. Deduplicate, strip personal data, fix labels, and hold back a test split *before* you look at the data. A surprising share of disappointing fine-tunes are data problems wearing a model costume.

**Step 3 — fine-tune, then evaluate against a set you did not train on.** Evaluate the tuned model on two things: the target task, and a general capability set. The second one catches catastrophic forgetting, which is invisible if you only test what you trained.

**Step 4 — deploy pinned.** Six artefacts determine behaviour and all six must be versioned: the exact model snapshot (never a floating alias), the prompt template, the sampling settings, the tool schemas, the retrieval configuration, and the guardrail thresholds. A pin on the model alone is not a pin.

**Step 5 — roll out gradually.** Shadow traffic first — duplicate live requests to the new version, score offline, keep users on the old one. Then canary at a small percentage with automatic rollback triggers on latency, failure rate or retry rate. Full traffic last.

**Step 6 — monitor, and close the loop.** Watch quality, latency, cost and refusal rate. Sample production traces for review, and promote every genuine failure into the regression set so it can never silently return.

### How it connects to the rest of the framework

`TSC4-Advanced-K2` supplies the training stages this workflow operationalises. `TSC4-Advanced-K4` prices it across its lifetime. `TSC4-Advanced-A4` is the question of whether this workflow can run for twenty models instead of one. `TSC4-Advanced-A3` supplies the reliability test that monitoring is meant to satisfy, and `TSC4-Intermediate-A6` supplies the comparison method for "is the new version actually better".

### What is current as of November 2026

The model tier that makes this workflow matter — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — all ship as dated snapshots behind floating aliases. Two practical shifts:

- **Vendors retire snapshots on short notice, typically within a year.** A workflow with no pin and no fallback template is a scheduled outage waiting for a date.
- **Fine-tuning and adapter hosting became a first-class product on vendor platforms.** You no longer need your own GPUs to run the fine-tune step, which removes the last excuse for skipping evaluation before deployment.

### Common misconceptions

- *"Deployment is the last step."* It is the step that starts the monitoring obligation. The lifecycle has no end while the system is live.
- *"If the code did not change, the behaviour did not change."* In generative systems, an alias update, a guardrail threshold tweak or a re-indexed document store all change behaviour without a commit.
- *"Evaluate after launch, with real users."* Real users are not a test set; they are the people who absorb the failures.
- *"A fine-tune is a finished asset."* It is bound to a base model snapshot. When the base is retired, the adapter dies with it.

## How a student should understand it

**Mental model:** opening a hawker stall. You do not just cook well — you get the licence, buy from a supplier you trust, taste the first batch, price the dish, and then stand at the stall every day watching what comes back uneaten.

**Things they can do after this bullet:**
1. Put the six workflow steps in order and state the exit condition for each.
2. List the artefacts that must be versioned, and why the model alias alone is not enough.
3. Explain what shadow and canary rollout protect against.

**Misconceptions to kill:** that deployment ends the project, that evaluation is optional after tuning, and that "no code change" means "no behaviour change".

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The HDB renovation.** You cannot choose tiles before you know the renovation permit rules (constraints). You do not move in before the inspection (evaluation). You do not sign off the contractor on a verbal promise — you keep the drawings (version pin), because the next contractor needs to know what is behind the wall. Where it breaks: a flat is finished once; a model keeps changing under you.

**The hawker licence and the tasting.** Cooking well is the fine-tune. The licence, the supplier, the first taste and the daily queue-watching are everything else.

### Worked example with a real tool

Give the room six shuffled steps and make them order it, then defend the order:

```text
Put these in order and explain each transition:
deploy, prepare data, pin version, evaluate, fine-tune, monitor.
```

Then ask the second question, which is the one that separates understanding from recall:

```text
Our support bot was fine-tuned on 3,000 resolved tickets. Six weeks
after launch the answers got worse and no code changed. List three
possible causes.
```

What to point at afterwards: the answer should include a floating model alias updated by the vendor, a policy change that made the training data stale, and a retrieval index that drifted. All three are workflow failures, not model failures.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — tell a two-line story: "the model changed on a Tuesday and nobody touched the code."
2. **State the objective** — by the end you can sequence the workflow and name what each gate protects.
3. **Recall prior learning** — fine-tuning versus retrieval, from the previous bullet.
4. **Present the content** — the six steps with their exit conditions, the six artefacts.
5. **Guide** — walk the ordering exercise together on the board.
6. **Elicit performance** — pairs diagnose the "it got worse and no code changed" scenario.
7. **Give feedback** — debrief, surfacing the alias, the stale data and the drifting index.
8. **Transfer** — each learner writes the two gates their own project is most likely to skip.

## What the framework doesn't mention but trainers need to know

- **The evaluation harness is the expensive part, not the fine-tune.** Data curation, rubrics and human review cost more engineering hours than the training run itself. Budget accordingly or the project stalls at "we have a tuned model and no evidence".
- **Prompt templates are not portable across model families.** A fallback model needs its own tuned prompt, or failover produces worse output than the outage.
- **Rollback is a data problem as well as a code problem.** Rolling back the model while the retrieval index has moved forward can leave you in a state that never existed.
- **Approval gates live in the organisation, not the pipeline.** InfoSec, Legal and the data protection officer all have vetoes; involve them at step one, not at launch.
- **Small models make this workflow cheaper, not easier.** Every step still applies; only the cost of the training run falls.

## Watch out

- **Do not present the workflow as linear-and-done on a slide.** Draw it as a loop with the production failures feeding back into the dataset, or the room will treat launch as graduation.
- **Do not demo a fine-tune without showing the held-out test.** A model that looks good on its training examples teaches the exact wrong lesson.
- **Do not let "pin the version" become "pin the model name".** The alias is the thing that moves; the dated snapshot is the thing that does not.
- **The stale claim to retire:** "we will evaluate it once it is live." Live is the most expensive place to discover a defect.
