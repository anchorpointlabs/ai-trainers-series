---
id: 07.03.A.A7
tsc: 7
level: Advanced
code: A7
title: Independent research: how to run an experiment that means something
as_at: 2026-11-26
review_by: 2027-02-25
---

# Independent research: how to run an experiment that means something

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A7**


> **Framework text (verbatim):** "Conduct independent research and contribute to the advancement of generative AI."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 18 of 20

**One-line version:** A result is only a result if a sceptic could reproduce it from what you wrote down — so write the experiment before you run it, and keep the run that failed.

## What it is

This ability is doing research rather than consuming it: framing a question the field has not settled, designing a controlled comparison, measuring it honestly, and reporting it in a form someone else can repeat. It includes the unglamorous disciplines — baselines, seeds, ablations, error analysis, artefact release — that separate a finding from an anecdote.

## Deep expansion

### The concept

Six steps, and the discipline is that each one can end the project:

1. **Question and prior work.** What exactly is unknown, and what has already been tried? A literature pass that takes a day saves a month.
2. **Hypothesis with a falsifier.** "Method X improves extraction accuracy on messy invoices by more than noise, measured by exact match on a held-out set" — with the threshold that would make you abandon it.
3. **Baseline.** The simplest thing that could work, tuned fairly. Untuned baselines are the most common way to manufacture a result.
4. **Controlled comparison.** One variable at a time, identical data, identical evaluation code, multiple seeds where randomness exists.
5. **Measurement.** A frozen test set you did not look at while designing, plus an error analysis that reads actual failures rather than only counting them.
6. **Replication and release.** Re-run from a clean environment; release code, prompts, data or a synthetic stand-in, and the rejected runs.

The reason generative AI research is unusually error-prone is that the variance is high (sampling, seeds, data ordering), the metrics are often proxies, and the test sets are frequently in the pre-training corpus. Each of those has a standard mitigation, and skipping any of them turns a project into marketing.

### The sub-concepts

**Contamination control.** Any public benchmark may be memorised. Build your own held-out set, keep it private, and check whether the model can answer it from memory when the evidence is removed.

**Ablation.** Remove one component at a time and measure. An ablation table is more convincing than a headline number because it shows which part did the work — and it often reveals the gain came from a detail nobody intended.

**Negative results.** Report the configurations that failed, the hyperparameters that broke training, the prompt that made things worse. This is the part of the record that saves other people the same month.

**Error analysis over metric optimisation.** Read fifty failures and classify them. The taxonomy is usually more valuable than a two-point improvement, and it tells you what to build next.

**Reproducibility hygiene.** Pinned environments, recorded seeds, data snapshots with hashes, and a script that regenerates every table.

### How it connects to the rest of the framework

`TSC7-Advanced-A8` is the collaborative version of the same work, and `TSC7-Advanced-A9` is what happens when it ships. `TSC5-Advanced-A4` covers the evaluation-research side specifically. `TSC7-Advanced-K9` supplies the statistics, and `TSC5-Intermediate-K6` covers hypothesis testing for evaluation.

### What is current as of November 2026

The publication norm has shifted toward artefact-first research: papers increasingly arrive with code, evaluation harnesses and data cards, and reviewers ask for contamination checks as a matter of course. Model-as-judge evaluation has made cheap large-scale comparison possible and introduced a new failure mode — judges that prefer the style of their own family of models — so judge validation is now part of a credible methods section. The frontier models of late 2026 are also strong enough that a small team's contribution is usually a domain, a dataset or an evaluation, not an architecture.

### Common misconceptions

- *"Research means a novel architecture."* Most useful contributions are datasets, evaluations, analyses and careful replications.
- *"A higher score is a finding."* Without a baseline, seeds and an interval, it is a sample.
- *"Negative results are failures."* They are the most reusable part of the record.
- *"More compute makes research better."* It makes the sweeps wider and the errors faster if the design is wrong.

## How a student should understand it

**Mental model:** a court case, not a sales pitch. You are trying to establish a claim that survives cross-examination, and the defence gets to see your evidence.

**Three things they can do after this bullet:**
1. Write a hypothesis with an explicit falsifier before running anything.
2. Produce an ablation table and a failure taxonomy for their own experiment.
3. Publish enough for someone else to re-run it in a day.

**Misconceptions to kill:** that novelty equals contribution, that a score equals a finding, and that negative results should be hidden.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker hygiene grade.** A stall does not get an A because it says so; an inspector checks specific things against a published standard, and the grade is only meaningful because the checks are known in advance. Pre-registration is the same idea.

**The school science practical.** Method, apparatus, results, sources of error. The "sources of error" section is where the marks are, and it is the section students skip.

### Worked example with a real tool

Make the design precede the run:

```
Claim to test: adding a retrieval step improves our model's
accuracy on questions about our internal policies.

Write the experiment plan:
1. Hypothesis with a falsifier and the threshold that would make
   us abandon it.
2. Baseline, including how we tune it fairly.
3. Test set construction, and how we know it is not contaminated.
4. Seeds, sample size and the statistical test we will run.
5. The ablation table we expect to publish, with its columns.
6. What we will do if the result is negative.
```

What to point at afterwards: question 3 is where most plans collapse — learners propose a test set built from the same documents they used to build retrieval. Question 6 is the cultural one: a plan with a real answer for a negative result is a research plan; one without it is a pitch. The ablation columns are usually the moment the room realises they have been reporting a single number.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two papers claiming opposite results on the same task; what differed?
2. **State the objective** — produce a pre-registered plan with a falsifier and an ablation table.
3. **Recall prior learning** — paired tests and intervals from `TSC7-Advanced-K9`.
4. **Present the content** — the six steps, contamination, ablation, error analysis, release.
5. **Guide** — write the retrieval experiment plan together.
6. **Elicit performance** — each learner plans an experiment from their own domain.
7. **Give feedback** — adversarial review: how would you fake this result?
8. **Transfer** — run the smallest version of the plan within two weeks and report the failure taxonomy.

## What the framework doesn't mention but trainers need to know

- **Freeze the test set before you look.** The first look is the last honest one.
- **Keep a lab notebook that timestamps decisions.** Memory reconstructs intent generously.
- **Compute is a real constraint.** Design experiments that fit the hardware you have, not the hardware in the paper.
- **Ethics review is part of the method** when humans or personal data are involved, and it takes longer than expected.

## Watch out

- **Do not teach research as paper-reading.** The ability is producing evidence, not summarising it.
- **Do not let learners tune on the test set "just to check".** It is the error the whole bullet exists to prevent.
- **Do not celebrate a single successful run.** Ask for the seeds.
- **The stale claim to retire:** "only labs can do research now." In 2026 domain data and a rigorous protocol are a viable contribution.
