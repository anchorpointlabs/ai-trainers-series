---
id: 05.01.B.A2
tsc: 5
level: Basic
code: A2
title: Interpret evaluation metrics for generative tasks
as_at: 2026-11-26
review_by: 2027-02-25
---

# Interpret evaluation metrics for generative tasks

> **TSC #5 Generative AI Model Evaluation · Basic · Ability A2**


> **Framework text (verbatim):** "Interpret evaluation metrics for generative tasks."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Ability · Bullet 8 of 11

**One-line version:** A metric is not a verdict — it is a clue, and interpreting it means knowing what it actually measures, what it cannot see, and what the number means *for this task* rather than in the abstract.

## What it is

This is the ability to read an evaluation result and say what it actually tells you: whether a score is good or bad *for the specific task*, which metric matters for that task, and where the metric is misleading you. It is the difference between seeing "92%" and knowing whether 92% is success, failure, or noise.

## Deep expansion

### The concept

Metrics are compressed, lossy summaries. Every one of them throws away most of what is true about an output in order to produce a single number, and each metric throws away *different* things. Interpreting a metric therefore means reversing that compression: asking "what did this measure, what did it ignore, and what does the number mean here?" A practitioner who can compute a metric but not interpret it is dangerous — they will act confidently on a number that is quietly wrong.

### The sub-concepts

**What the metric measures.** Accuracy measures factual match, coherence measures logical flow, diversity measures spread across outputs, novelty measures departure from the input. A number is only interpretable if you know which of these it is a proxy for.

**What the metric ignores.** Every metric has a blind spot. A high accuracy score says nothing about coherence; a high diversity score says nothing about whether any of the varied outputs is *right*. Interpreting means naming the blind spot aloud.

**Task matters more than the number.** 85% accuracy is a disaster for a medical or compliance task and a triumph for open-ended creative work. There is no universal "good score" — the threshold is set by what happens when the model is wrong.

**Variance and noise.** A score that moved from 84% to 86% on a small test set may be meaningless wobble. Interpretation includes asking whether the difference is real or just sampling noise.

### How it connects to the rest of the framework

This is the ability that operationalises `TSC5-Basic-K2` (the four criteria) — K2 is *what* the metrics mean, A2 is *reading the numbers* in practice. It feeds `TSC5-Basic-A3` (propose improvements), because you cannot propose a fix until you have correctly read what broke. At Intermediate level this same skill grows teeth: `TSC5-Intermediate-K2` (BLEU, FID, Inception Score) and `K6` (statistics and hypothesis testing) are what you reach for when "is this difference real?" needs a rigorous answer.

### What is current as of November 2026

The field has consolidated on a caution: **single-number leaderboard scores are treated as marketing, not evidence.** Practitioners now read metrics *in context* — accuracy against *your* task, latency and cost alongside quality, and the p95 worst case rather than the average. The other shift is that **LLM-as-a-judge has partly replaced human scoring**, which means interpreting a metric now often means interpreting a *judge's* score — and knowing the judge's biases (from `TSC5-Basic-K5`) is part of reading it correctly.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A higher score is a better model."* Only if the metric measures what the task needs and the test set matches reality. A model can top a benchmark and fail your actual job.
- *"One number tells the story."* No single metric captures accuracy, coherence, diversity and novelty at once. Reading one number as "the quality" is the most common interpretation error.
- *"If the score didn't change, nothing changed."* The *distribution* may have changed while the average held — a model that is better on easy cases and worse on hard ones can keep the same mean score.

## How a student should understand it

**Mental model:** a car's fuel-efficiency number. "18 km/litre" means something only if you know it was measured on the highway, in a lab, or in heavy traffic — and only if you know what you actually need it for. The number is real; the interpretation is everything around it.

**Three things they can do after this bullet:**
1. Given a metric and a task, say in one sentence what the metric measures and what it cannot see.
2. State the threshold at which a score becomes "too low to ship" for a task where being wrong is costly.
3. Distinguish "this difference is meaningful" from "this difference is noise" in a before-and-after score.

**Misconceptions to kill:** higher = better, one number = the story, and unchanged mean = nothing changed.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The PSLE aggregate score.** A single T-score tells you a child did well *overall*, but it hides that she aced English and nearly failed Maths. The teacher who only reads the aggregate cannot help her; the teacher who reads the *sub-scores* can. Model evaluation is the same: the aggregate is a headline, the sub-scores are where the work happens.

**The restaurant rating.** A 4.8-star rating for a hawker stall tells you people were happy — but it does not tell you the queue is 40 minutes, or that the vegetarian options are terrible, or that the rating came from 200 tourists who only ordered the signature dish. Interpreting the rating means asking what is behind it.

### Worked example with a real tool

Give the room a small made-up results table and make them read it, not just see it:

```
Model A:  92% accuracy  ·  88% coherence  ·  low diversity
Model B:  84% accuracy  ·  84% coherence  ·  high diversity
Task:     write 20 slogan variations for a brand brainstorm
```

What to point at afterwards: for *this* task (brainstorming), Model B may actually be the better choice — its diversity matters more than Model A's accuracy edge, because slogans will be human-picked anyway. Swap the task to "summarise compliance rules" and the answer flips to A. The point is not which model won — it is that the *task* decides which metric to read, and the same numbers mean different things.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a single headline score and ask "is this model good?" Collect the yeses, then complicate them.
2. **State the objective** — you will read any metric and say what it means *for the task*, not in the abstract.
3. **Recall prior learning** — they know the four criteria (K2); each metric maps to one of them.
4. **Present the content** — what it measures, what it ignores, task-dependent thresholds, variance.
5. **Guide** — work the Model A/B table together, twice, with two different tasks.
6. **Elicit performance** — each learner takes one metric from their own work and states what it ignores.
7. **Give feedback** — catch the learner who reads "higher = better" without asking "for which task?"
8. **Transfer** — when they next see a model's benchmark score, they ask "measured on what, and does it matter for my job?"

## What the framework doesn't mention but trainers need to know

- **Thresholds are task-set, not universal.** There is no global "good accuracy". The trainer's job is to make learners state *their* threshold — "if it is wrong here, someone files a wrong claim" — before any number means anything.
- **Report the worst case, not just the average.** A model that is excellent on average and catastrophic 3% of the time is worse in production than a mediocre-but-safe model. Basic learners rarely ask about the tail; teach them to.
- **A metric can be gamed.** Once a number becomes the target, it stops being a good measure (Goodhart's law). Learners should be suspicious of a score that is *too* clean, and always ask what the metric would miss if someone optimised for it.

## Watch out

- **Do not teach metric formulas at Basic level.** Interpreting is not computing. The learner needs to know what a number means and what it hides — BLEU's maths is Intermediate.
- **Do not present any metric as "the truth".** Every number is a lossy proxy. If the room leaves believing there is a single correct quality score, the lesson has failed.
- **The stale claim to retire:** "this model scores 90% on the benchmark, so it is the best." The benchmark measures *a* task, not *your* task — and a score without a task and a threshold is just a number.
