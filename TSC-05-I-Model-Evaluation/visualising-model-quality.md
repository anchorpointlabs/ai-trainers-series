---
id: 05.02.I.K3
tsc: 5
level: Intermediate
code: K3
title: "Visualising model quality: the charts that show what an average hides"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Visualising model quality: the charts that show what an average hides

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K3**


> **Framework text (verbatim):** "Data visualisation techniques for evaluating generative outputs."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 3 of 12

**One-line version:** An average is a single number pretending to be a description; a chart is where the distribution, the tail, the slice and the trade-off become visible in time to act on them.

## What it is

Data visualisation for generative evaluation is the practice of choosing charts that expose the shape of model behaviour rather than summarising it away: the spread of scores, the worst-case tail, the per-slice breakdown, the quality-cost-latency trade-off, and the qualitative view of what the outputs actually look like. It is a design skill, not a chart-type list — the wrong chart is worse than no chart because it looks like evidence.

## Deep expansion

### The concept

Every evaluation reduces a distribution to numbers, and every number loses shape. An average of 82 loses the fact that half the outputs scored 95 and half scored 69 — which is a completely different model behaviour and calls for a completely different fix. Visualisation is the recovery step: it puts the shape back so a decision-maker can see *how* the model is failing, not just *how much*.

The chart is also a user interface, which is why this bullet sits next to `K7` in the framework's logic. Whoever reads the report is making a decision under time pressure with limited attention. A chart that requires ten minutes of study will be replaced by the number in the caption, and the number is the thing you were trying to escape.

### The sub-concepts

**Plot the distribution, not the mean.** Histograms, ECDFs and violin plots answer "where is the mass". Start with an ECDF when comparing two models — the curve crossing tells you which model wins at which threshold, which a mean cannot.

**Slice before you summarise.** Scores by document type, language, input length, customer segment or channel. A heatmap of slice against score, or small multiples of the same chart repeated per slice, is the standard move. The finding is almost always in the slice, not the aggregate.

**Show the tail.** p50 hides p95. For quality, plot the worst 5% separately and add a failure gallery: eight real outputs that failed, verbatim. One bad example in front of a decision-maker does more than a distribution curve.

**Show the trade-off.** Scatter quality against latency and cost, one point per model configuration, with a Pareto frontier drawn by hand. This single chart changes more procurement conversations than any table of scores.

**Show the uncertainty.** Error bars, bootstrap bands, or per-seed spread. A bar chart with no interval invites the reading "B is better" when B is inside A's noise.

**Show the shape of the output space.** Project embeddings down to two dimensions to see whether the model produces one cluster (mode collapse) or a spread; lay out generated images as a contact sheet; for text, show repeated n-grams or near-duplicate clusters. These are not scores, they are evidence.

**Chart honesty.** Truncated axes, dual axes, cherry-picked examples, and 3D bars all manufacture conclusions. The test: could a sceptic reconstruct your claim from the chart alone, including what would have disproved it?

### How it connects to the rest of the framework

`TSC5-Intermediate-K1` explains why a scalar needs unpacking; `K2` supplies the scalars; `K6` supplies the intervals you draw as bands; `A2` is the analytical reading of the same distributions. `TSC5-Basic-A2` (interpret metrics) is the precursor skill — reading one number well. `TSC5-Intermediate-K7` is where the report becomes an interface, and `A1` is the pipeline that produces the data these charts consume.

### What is current as of November 2026

Evaluation reporting has moved from slide decks to live dashboards, and the good ones default to per-slice views with drift tracked over time rather than a single headline score. Blind side-by-side comparison interfaces — hide the model name, randomise which side is which — have become the standard way to present text quality, partly because they also suit judge models. Multimodal evaluation has pushed visual reporting forward: contact sheets and filmstrips for image and video output, overlaid diff views for edited images. The failure gallery, once an afterthought, is now a fixture of serious eval reports.

### Common misconceptions

- *"A chart is objective."* Every chart is a set of choices: what to aggregate, what to exclude, which axis to start at.
- *"One good chart is enough."* Distribution, slice, tail and trade-off answer different questions; a report needs at least three.
- *"If the average didn't move, nothing changed."* Bimodal-to-unimodal at the same mean is a large improvement or a large regression depending on which mode you wanted.
- *"More charts means more rigour."* Twelve charts nobody reads is less rigorous than three that decide something.

## How a student should understand it

**Mental model:** the MRT crowding average. "Average 60% full" describes no actual train — the 8am service is jammed and the 11am one is empty. The average is true and useless; the graph is what gets you a change in headway.

**Three things they can do after this bullet:**
1. Take any evaluation table and choose the three charts that would expose its hidden shape.
2. Build a failure gallery of eight real outputs alongside the score.
3. Spot a chart that is technically true and rhetorically dishonest.

**Misconceptions to kill:** charts are neutral, averages are summaries, and more charts equals more rigour.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The HDB resale price index.** The index says prices rose 2% this quarter. Your block fell 4%, because the index averages across towns, flat types and lease ages. Nobody buys "the index"; they buy a block. Slice before you conclude.

**The 3-hour PSI.** A daily average PSI of 60 sounds tolerable until you see the three-hour reading hit 180 at lunchtime, which is when people were outside. The average describes the day; the spike describes the harm. Tails are where the decisions are.

### Worked example with a real tool

Give the room a small results table in a chat tool and make them choose the picture, not just read the number:

```
Here are evaluation results for three candidate models on 200 support
replies. Columns: model, mean_quality (0-5), p05_quality, cost_per_1k,
median_latency_s, and the share of replies that were flagged unsafe.

Model A: 4.1 | 2.4 | $2.10 | 3.4s | 0.4%
Model B: 3.9 | 3.3 | $0.40 | 1.1s | 0.2%
Model C: 4.2 | 1.1 | $4.80 | 6.9s | 1.1%

We are drafting replies to delivery complaints; a wrong reply costs us a
refund. Draw the three charts that would let a manager decide, and tell me
which model you would put forward and why.
```

What to point at afterwards: the mean ranks C first and B last; the p05 (the worst 5%) reverses that completely, and the cost column reverses it again. Three charts — distributions by model, a quality-versus-cost scatter, and a bar of unsafe-flag rates — turn a one-line answer into a defensible decision. Then ask what a fourth chart would add: slices by complaint type.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two datasets with the same mean and wildly different shapes; ask which model is safer.
2. **State the objective** — you will choose and build the charts that expose distribution, tail, slice and trade-off.
3. **Recall prior learning** — they can already read a metric (Basic A2); now they show it.
4. **Present the content** — the six chart jobs; honest-charting tests; the failure gallery.
5. **Guide** — work the three-model table together and draw the scatter on the board.
6. **Elicit performance** — each pair takes their own eval results and sketches three charts on paper first.
7. **Give feedback** — critique the sketches: what does each one let a sceptic conclude?
8. **Transfer** — they rebuild the charts in their own tool (a spreadsheet, pandas, a dashboard) for next session.

## What the framework doesn't mention but trainers need to know

- **Small slices lie loudly.** A violin plot of nine examples looks like a distribution and is not one. Either merge slices or annotate n on every panel — and teach learners to read n before shape.
- **Colour is a design decision, not decoration.** Roughly one in twelve men has a colour-vision deficiency; red-green quality scales are the common failure. Use position and lightness, not hue alone.
- **Dashboards invite over-reading.** A live number with no interval and no sample size gets treated as truth by the third week. Put the test-set size and date on the chart.
- **The report is a decision document.** End with a recommendation and the condition under which it would change. Charts support a decision; they are not the deliverable.

## Watch out

- **Do not demo an average-only chart and call it visualisation.** If the chart could be replaced by a number, it is not doing the work.
- **Do not use a canned dataset with no story.** Use results from the learners' own task, or a scenario they recognise.
- **Do not let a beautiful chart outrank a boring finding.** The best chart in the room is the one that made someone change the plan.
- **The stale claim to retire:** "we'll put it in a table, the numbers speak for themselves." Numbers do not speak; they are quoted out of context by whoever is in the meeting.
