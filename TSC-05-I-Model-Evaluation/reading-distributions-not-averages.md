---
id: 05.02.I.A2
tsc: 5
level: Intermediate
code: A2
title: "Reading distributions, not averages: analysing model outputs"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Reading distributions, not averages: analysing model outputs

> **TSC #5 Generative AI Model Evaluation · Intermediate · Ability A2**


> **Framework text (verbatim):** "Analyse complex data distributions and model outputs."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Ability · Bullet 10 of 12

**One-line version:** The job is not to compute the mean, it is to find out what shape the outputs make — where they cluster, where they pile up at the bottom, and which slice is carrying the failure.

## What it is

This is the analytical ability to take a set of model outputs and their scores and describe the *distribution*: its shape, spread, tails, joint relationships and change over time. It means being able to say "the model is bimodal — it either nails the reply or misses the policy entirely, and there is nothing in between", which is a diagnosis, rather than "the model scores 3.8", which is a summary.

## Deep expansion

### The concept

A generative model produces a cloud of outputs, not an output. Some prompts it handles effortlessly, some it fails completely, and the interesting structure is almost always in how those two populations separate. The average collapses that structure into a single point and, in doing so, hides the two facts a decision needs: how bad is the bad case, and who is in it.

Distributional analysis is therefore mostly a matter of asking better questions of the same data. Is the score distribution one hump or two? Is the left tail fat? Does quality fall with input length? Does the model pad when it is unsure? Does it produce the same answer every time, and is that a good sign or mode collapse? Are the failures concentrated in one language, one document type, one customer segment?

### The sub-concepts

**Shape.** Plot the histogram or ECDF. A bimodal distribution usually means two populations of inputs — in-scope and out-of-scope, or short and long — that behave differently and should be evaluated separately. A spike at the top with a thin tail means the model is mostly fine and occasionally catastrophic; a spike at the bottom with a thin tail means the opposite.

**Tail.** Compute p05 or the failure rate rather than the mean, and read the failures individually. The tail is where refunds, escalations and incidents live, and it is invisible in every average.

**Spread across repeated runs.** Same prompt, five runs. High variance means the model is unreliable in a way that a single-run score cannot show — and for a business process, variance is often worse than a slightly lower mean.

**Joint relationships.** Quality against output length (does it pad?), quality against input length (does it degrade past a certain context size?), quality against latency, quality against the model's own stated confidence if it gives one. Scatter plots, not tables.

**Distribution in embedding space.** Project the outputs of many runs into two dimensions. One dense blob means the model produces variations of one answer — mode collapse, or an over-tuned model. Well-separated clusters by prompt type mean the model is sensitive to the input, which is usually what you want. Nearest-neighbour distance to the training corpus is a rough regurgitation check.

**Stratified distributions.** The same analysis repeated per slice: language, dialect, document type, input length band, customer segment. The finding is almost always that one slice has a different shape, not a different mean.

**Drift.** Distribution over time. Compare this week's outputs on the same test set with last month's; compare this week's production inputs with the test set. Input drift and model drift are different problems with different fixes.

### How it connects to the rest of the framework

`TSC5-Intermediate-K3` is the visual vocabulary this ability uses; `K6` supplies the intervals that keep you from over-reading a small slice; `K4` defines the dimensions being distributed. `A1` produces the data, `A3` turns a distributional finding into a root cause, and `A4` acts on a slice that is unfairly served. `TSC5-Basic-K2`'s diversity criterion is the conceptual ancestor of the embedding-space view.

### What is current as of November 2026

Long-context behaviour remains an active area: quality does not degrade uniformly with input length, and the drop is often concentrated in material placed in the middle of a long document — which is a distributional fact you can only see by plotting quality against where the relevant passage sat. Multimodal evaluation has made the same analysis routine for image and video output, with per-category and per-style breakdowns. In production, output distributions have become a monitoring signal in their own right: a shift in the shape of generated text is often the first evidence that an upstream data or prompt change has gone wrong.

### Common misconceptions

- *"The average is the summary."* It is one statistic among many, and the least informative for decisions.
- *"Delete the outliers and re-run."* The outliers are the finding. Deleting them is how a failing model gets certified.
- *"Same average means same behaviour."* Two models at 3.8 can be a steady performer and a coin flip between excellent and useless.
- *"Diversity means randomness."* Diversity is variation that is appropriate to the input; randomness is variation that is not.

## How a student should understand it

**Mental model:** taxi waiting times at Changi. "Average wait eight minutes" describes nobody — most people wait three, and a substantial group waits thirty-five at shift change. One number, two completely different experiences.

**Three things they can do after this bullet:**
1. Plot and name the shape of a score distribution, and say what the shape implies about the inputs.
2. Find the slice carrying the failure using a stratified comparison.
3. Distinguish instability (high spread across runs) from weakness (low mean).

**Misconceptions to kill:** the mean is the summary, outliers are noise, and identical averages mean identical behaviour.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Taxi waiting time at Changi.** The mean hides a bimodal reality: the queue is short most of the evening and brutal after the last train. If you are planning staffing, the mean is the wrong number and the 11pm spike is the whole job.

**The 3-hour PSI.** A daily average of 60 is comfortable; the three-hour reading at lunchtime is what people actually breathed. Distributions have a time axis, and the average erases it.

### Worked example with a real tool

Take a results file and interrogate the shape before anyone computes a mean:

```
Here are 200 scored outputs. Columns: score_1to5, slice, input_tokens,
output_tokens, repeated_run_id (1-3 per prompt).

1. Describe the shape of score_1to5: one hump or two? Where is the mass?
2. Which slice has the worst tail (lowest 5th percentile), and how big is
   that slice? Tell me if it is large enough to conclude anything.
3. Is score related to output_tokens? Does the model pad when unsure?
4. Rank the prompts by how much their score varied across the three runs.
   What do the most variable ones have in common?
5. Give me the three plots that would show a manager what you just said.
```

Then the two lines that do most of the work in practice:

```python
import pandas as pd
df = pd.read_csv("scores.csv")
print(df.groupby("slice")["score"].describe(percentiles=[.05, .5, .95]))
print(df.groupby("prompt_id")["score"].std().sort_values(ascending=False).head(10))
```

What to point at afterwards: the describe table shows a mean of about 3.8 for every slice — and a p05 that ranges from 1.0 to 3.6. The averages are indistinguishable; the fifth percentiles are not. That is the entire argument for distributional analysis in one screen.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two datasets, same mean, one bimodal; ask which is safer to deploy.
2. **State the objective** — you will describe the shape, find the worst slice, and detect instability.
3. **Recall prior learning** — the rubric dimensions from K4; each becomes a distribution to examine.
4. **Present the content** — shape, tail, spread, joint plots, embedding views, slices, drift.
5. **Guide** — run the interrogation on the shared file and mark the bimodality live.
6. **Elicit performance** — each learner analyses their own results and writes a three-sentence finding.
7. **Give feedback** — sentence-level: "the model is worse on long inputs" becomes "p05 falls from 3.6 to 1.9 beyond 800 tokens, n=31".
8. **Transfer** — they add a p05 column and a per-slice table to their standing report.

## What the framework doesn't mention but trainers need to know

- **Variance is a product feature.** A support bot that is excellent two times in three is worse than one that is good every time, because the process around it cannot plan. Report spread as a first-class metric.
- **Small slices produce confident nonsense.** Under about thirty items, report the count and refuse the percentile.
- **Watch the length relationship.** Models that pad, or that truncate when unsure, produce distributions that look fine in the middle and are systematically wrong at the extremes.
- **Production inputs are a distribution too.** Half of "the model got worse" turns out to be "the customers changed" — compare the input distribution, not just the outputs.

## Watch out

- **Do not let the room compute a mean first.** Order matters; start with the shape and the tail.
- **Do not use a two-decimal average to compare models.** With a small test set the second decimal is noise — see `K6`.
- **Do not show a violin plot of nine items.** It teaches learners to trust shape from samples that have none.
- **The stale claim to retire:** "we track the average quality score weekly." A weekly mean of a bimodal distribution tracks the mix of inputs, not the model.
