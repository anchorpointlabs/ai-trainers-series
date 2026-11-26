---
id: 05.03.A.K3
tsc: 5
level: Advanced
code: K3
title: "Counterfactuals and explainable evaluation: where the research frontier sits"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Counterfactuals and explainable evaluation: where the research frontier sits

> **TSC #5 Generative AI Model Evaluation · Advanced · Knowledge K3**


> **Framework text (verbatim):** "Frontiers of generative AI evaluation research (e.g., counterfactual effect, explainable evaluation)."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Knowledge · Bullet 3 of 13

**One-line version:** The frontier moved from "how good is the output" to "what caused it, and can we show our working".

## What it is

This bullet names a direction of travel rather than a settled body of knowledge. Two strands lead it. *Counterfactual effect* treats evaluation as an experiment: change exactly one thing in the input, hold everything else fixed, measure what moved. *Explainable evaluation* insists that a score arrive with an account of itself — which items failed, on what grounds, under which rubric clause — so the result can be audited rather than ranked.

## Deep expansion

### The concept

Evaluation spent a decade asking whether a model could answer a fixed question well. That question is being exhausted: public benchmarks saturate, they leak into training data, and a model tuned on the benchmark answers the benchmark rather than the task. The frontier response is to stop treating evaluation as a fixed exam and treat it as a causal question about a system in a distribution.

Three ideas carry the shift. **Construct validity**: does the score measure the thing you named? A "helpfulness" score produced by a judge that prefers long answers measures length. **Contamination**: once a benchmark is public it is training data, so the answer is not a better public benchmark but a process — held-out items, rotated on a schedule, provenance recorded. **Counterfactual sensitivity**: a system that changes its answer when you change a relevant fact is responsive; one that changes when you change a name or reorder two bullets is brittle. Measuring both — sensitivity to signal, insensitivity to noise — is the most informative single test available, and it generalises across text, image and audio.

### The sub-concepts

**Counterfactual pairs.** Two inputs differing in one documented attribute. The difference in output is the effect of that attribute. The discipline is in "everything else byte-identical".

**Explainable evaluation.** Every failing item carries a rubric clause, a quoted span and a short rationale. The report is a table of diagnoses, not a leaderboard position.

**Error taxonomies over scores.** Naming failure modes — hallucinated citation, ignored constraint, wrong register — yields a distribution of failures, far more actionable than a mean.

**Slice-level reporting.** Aggregates hide the tail. Disaggregation by language, document type and task difficulty is where deployment decisions actually get made.

**Trajectory evaluation.** For agents the unit is a sequence: wrong turn, recovery, steps to completion, stopping. Step-level scoring is an open problem, not a solved one.

**Dynamic and adversarial benchmarks.** Items generated against the current model, refreshed as capability moves, never released.

### How it connects to the rest of the framework

`05.03.A.K2` supplies the explanation machinery this depends on; `05.03.A.K4` is the method toolbox that makes it practical. `05.02.I.K6` gives the statistics for claiming an effect is real rather than noise — counterfactual work without it produces anecdotes with charts. `05.03.A.A5` is the operational question: which of these ideas is cheap enough to run weekly.

### What is current as of November 2026

Public leaderboards have lost authority in procurement; private, rotated, human-anchored evaluation has replaced them at organisations that buy seriously. The three flagship lines are now marketed on evaluation practice as much as score: published rubrics, disclosed judge models, per-slice results. Two research preoccupations dominate: agentic trajectory scoring, where nobody is confident the metrics are right, and evaluation of evaluations, where the judge's reliability is measured before its verdicts are used. "Eval-aware" behaviour — a model performing differently when it detects a test — has moved from speculation to documented nuisance.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A counterfactual is just a hypothetical."* A hypothetical is a story. A counterfactual is a controlled change with everything else held fixed, and the discipline is in the "held fixed".
- *"If the benchmark is public, at least it is fair."* Public means contaminated. Fairness between vendors comes from a protocol both sides can inspect.
- *"Higher average means better system."* Averages hide the tail, and the tail is where deployment fails.

## How a student should understand it

**Mental model:** moving from an exam to a driving test. The exam marks one script; the driving test changes the conditions — rain, a cyclist, a narrow lane — and asks what the driver did differently each time.

**Three things they can do after this bullet:**
1. Turn a vague quality complaint into a counterfactual pair with exactly one changed attribute.
2. Write a report whose failing items carry diagnoses rather than a single score.
3. Say which of their current metrics is contaminated, saturated, or measuring the wrong construct.

**Misconceptions to kill:** that public benchmarks are neutral referees, that a mean summarises a distribution, and that explanation is a narrative added after scoring.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The driving test in the rain.** Same driver, same route, one condition changed. Failing only in rain tells you something a single pass mark never could. It breaks because real systems change many conditions at once.

**The food-hygiene grade.** One letter for the stall, but the inspection sheet behind it lists which surfaces were checked and what failed. Two stalls can share a grade with very different problems. Explainable evaluation is the sheet; the letter is the leaderboard.

### Worked example with a real tool

A team runs a grant-drafting assistant and cannot tell whether rejections are about content or tone. Paste this into Claude with one anonymised draft:

```
Below is a draft section of a grant application and a reviewer comment.

1. Extract the reviewer's complaint as one rubric clause: "The draft must ___ so that ___".
2. Produce two variants. Variant A changes ONLY the supporting evidence (adds one
   number already implied in the text). Variant B changes ONLY the register (formal
   to plain). Everything else byte-identical, including headings and line breaks.
3. For each variant: state what should change if the complaint is about content, and
   what should change if it is about tone. Then say which variant moved which way.

Do not rewrite the whole draft.
```

What to point at afterwards: step 1. Learners want to jump to rewriting; the value is that a complaint became a testable claim. Then check whether variant B moved the register without touching the facts — if not, the two problems are not separable in one prompt.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a leaderboard where the top model loses on the room's own documents.
2. **State the objective** — learners can convert one quality complaint into a counterfactual pair and a rubric clause.
3. **Recall prior learning** — the Intermediate rubric work; ask what the rubric cannot see.
4. **Present the content** — construct and ecological validity, contamination, counterfactual design, explainable reporting.
5. **Guide** — build the grant-draft probe together, arguing about what counts as "only one change".
6. **Elicit performance** — pairs write a counterfactual pair for their own system.
7. **Give feedback** — review for hidden second changes; that is where nearly all of them fail.
8. **Transfer** — each learner picks one number they report upward and states what it does not measure.

## What the framework doesn't mention but trainers need to know

- **Counterfactual work is an editorial discipline.** The cost is writing and maintaining paired items; ten well-built pairs beat a thousand scraped ones.
- **Contamination is an organisational problem.** Once an eval set is used in a demo it is in a prompt log, and prompt logs travel. Version control, access limits and rotation are the real controls.
- **Trajectory metrics are immature — say so.** Teaching a step-level score as settled will date within a year.
- **Eval-awareness breaks the link between offline and online.** If a system behaves differently under test, the divergence is itself worth measuring.

## Watch out

- **Do not present a single counterfactual as causal proof.** One pair is an observation; causation needs replication across items and a design that rules out confounds.
- **Do not chase the newest benchmark.** Benchmarks are consumables. Teach the process that produces a private set.
- **Do not let explainable evaluation become verbose evaluation.** A five-paragraph rationale per item is unreadable, and unreadable artefacts go unused.
- **Do not evaluate the demo, the model and the product as one thing.** The system includes retrieval, guardrails and interface, and the frontier work is increasingly about the system.
- **The stale claim to retire:** "we will know it works when the benchmark score goes up." In November 2026 the benchmark is the least informative evidence in the room.
