---
id: 05.02.I.K6
tsc: 5
level: Intermediate
code: K6
title: "Is the difference real? Hypothesis testing for model evaluation"
---

# Is the difference real? Hypothesis testing for model evaluation

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K6**


> **Framework text (verbatim):** "Statistical analysis and hypothesis testing."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 6 of 12

**One-line version:** Two models scoring 84% and 86% on forty prompts is not a finding, it is a coin landing heads — statistics is how you tell a real difference from the wobble of a small test set.

## What it is

Statistical analysis in model evaluation is the set of methods for deciding whether an observed difference — between two models, two prompts, two versions — is larger than the variation you would expect from sampling alone. In practice that means confidence intervals rather than bare scores, paired comparisons on the same test set, resampling methods that do not assume a distribution, correction when you test many slices, and effect sizes so that a real but trivial difference does not win an argument.

## Deep expansion

### The concept

Your evaluation is a sample. Forty emails stand in for four million. Every number computed on those forty carries sampling error, and the smaller the test set, the wider the error. A difference of two percentage points on forty prompts is roughly one and a half prompts — well within what a different random draw of forty would produce.

Most evaluation arguments in industry are not about models at all. They are one person quoting a mean and another person quoting a mean, with nobody asking how much of the gap is noise. The statistical habit at this level is small and unglamorous: report the interval, compare on the same items, and do not test twenty slices and celebrate the one that came out at p < 0.05.

### The sub-concepts

**The unit of analysis.** Usually the prompt, not the token, not the sentence. Decide it explicitly, because every subsequent test depends on it. If you evaluate five outputs per prompt and average them, your effective sample size is the number of prompts, not the number of outputs.

**Paired comparisons.** Run both models on the *same* test set and compare item by item. Model A and Model B are then measured under identical conditions, which removes a large part of the variation and makes the test far more sensitive. This is the single highest-value habit in the list, and it costs nothing but discipline.

**McNemar's test for pass/fail.** When each item is a pass or a fail, you do not need means — you need the discordant pairs: items A passed and B failed, versus B passed and A failed. McNemar tests whether that 2×2 table is lopsided by more than chance.

**Bootstrap confidence intervals.** Resample your test set with replacement a few thousand times, recompute the metric each time, and take the 2.5th and 97.5th percentiles. No distributional assumptions, works for almost any metric including judge scores and FID, and gives an interval a manager can read. For a paired comparison, bootstrap the *difference*, not the two scores separately.

**Permutation tests.** Shuffle the pairing between outputs and models, recompute the difference, repeat. If the real difference sits inside the shuffled distribution, it is not distinguishable from noise. Useful when the metric is weird or the sample is small.

**Significance is not importance.** A 0.4-point gain that is statistically solid is still not worth double the price or an extra second of latency. Always report the effect size alongside the interval, and put the cost next to it.

**Multiple comparisons.** Test twenty slices and one will clear p < 0.05 by chance alone. Either pre-register the two or three slices that matter, or apply a correction (Bonferroni for a handful, Benjamini–Hochberg when you are screening many).

**Power.** A test set of forty cannot detect a five-point difference reliably. If a difference of five points would change your decision, you need a test set sized to see it — worked out before the run, not after an inconclusive one.

**Human agreement statistics.** When two raters score the same outputs, raw agreement overstates reliability: two people agreeing 80% of the time on a task with two outcomes may be barely better than chance. Cohen's kappa (two raters, categorical) or Krippendorff's alpha (many raters, ordinal) is the honest number.

### How it connects to the rest of the framework

`TSC5-Intermediate-K1` establishes that a result is a sample; this bullet quantifies it. `K2` supplies the metrics whose intervals you compute; `K3` draws them as bands; `A2` is the distributional reading; `A3` depends on not chasing noise — most wasted tuning effort is a response to a two-point wobble. `TSC5-Basic-A2` (interpret metrics) already asks "is this difference meaningful"; here it becomes arithmetic. `TSC4-Intermediate-*` uses these tests to choose between candidate models.

### What is current as of November 2026

Bootstrap intervals have become the default in serious evaluation tooling, and leaderboards increasingly print them — which immediately revealed that many adjacent rankings were inside the noise. Judge models introduced a second variance source, so teams now re-run the judge several times per item and average, and report judge stability as a property of the instrument. With frontier models of late 2026 (the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon) often within a couple of points of each other on a given task, the honest conclusion in many evaluations is "these are indistinguishable on my test set" — and that is a finding, not a failure.

### Common misconceptions

- *"A bigger test set always makes it significant."* It shrinks the interval, but only if the sample is representative; a large biased sample is precisely wrong.
- *"p < 0.05 means important."* It means unlikely under the null. Importance is the effect size against the cost.
- *"We ran it once and got 88%."* One run with no interval is an anecdote with a decimal point.
- *"Our raters agree 80% of the time, so the labels are reliable."* On a two-category task that can be close to chance agreement.

## How a student should understand it

**Mental model:** a 70% chance of rain. One dry day does not disprove the forecast and one wet day does not prove it. A probability is verified over many days; a model difference is verified over many prompts.

**Three things they can do after this bullet:**
1. Attach a confidence interval to any score, and say what it implies for a decision.
2. Design a paired comparison instead of two independent runs.
3. Look at a table of twenty slice results and refuse to celebrate the smallest p-value.

**Misconceptions to kill:** one run is a result, significance equals importance, and more slices equals more insight.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The kopi taste test.** Ten sips and stall A wins; two hundred sips and the gap closes to nothing. Nobody concludes anything from ten sips, yet teams conclude everything from forty prompts. The analogy transfers almost without translation.

**The PSLE banding.** A child scoring 74 and a child scoring 76 may be in different bands and in the same ability range. The band is a decision rule, not a measurement of the child. Model league tables work the same way, minus the moderation.

### Worked example with a real tool

Two moves, one prompt and one script. The prompt first:

```
I have two AI models and 60 test prompts. Model A passed 47, model B
passed 52. On 9 prompts A passed and B failed; on 14 prompts B passed
and A failed.

1. Is that difference likely to be real, or sampling noise? Explain in
   plain English, no formulas.
2. What would you need to be confident?
3. Rewrite my result as a sentence I could put in front of a manager.
```

Then the arithmetic that makes it repeatable — note the paired difference vector, which is the whole trick:

```python
import numpy as np
rng = np.random.default_rng(7)
a = np.array(pass_a)   # 1 = pass, 0 = fail, one row per test prompt
b = np.array(pass_b)
d = b - a                      # paired differences: +1, 0, -1
boot = [rng.choice(d, size=len(d), replace=True).mean() for _ in range(10000)]
print(d.mean(), np.percentile(boot, [2.5, 97.5]))
```

What to point at afterwards: the interval, not the point estimate. If it straddles zero, the honest sentence in the report is "no detectable difference at this sample size", and the next decision is about sample size or about which slice matters — not about which model is better.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two scores 84% and 86% on 40 items and ask who wins. Collect confident answers, then show the bootstrap interval.
2. **State the objective** — you will report any comparison with an interval and know when to say "indistinguishable".
3. **Recall prior learning** — Basic A2 mentioned variance; now they compute it.
4. **Present the content** — unit of analysis, pairing, McNemar, bootstrap, effect size, multiple comparisons, rater agreement.
5. **Guide** — bootstrap the shared example on the projector, once with an unpaired and once with a paired design.
6. **Elicit performance** — each learner writes the confidence-interval sentence for their own last evaluation.
7. **Give feedback** — correct "significant" used as "important", and any sentence that reports a mean without a sample size.
8. **Transfer** — they add an interval column to their eval report template.

## What the framework doesn't mention but trainers need to know

- **Judge noise is not sampling noise.** Re-running a judge on the same item gives different scores; that variance is an instrument property, not a property of your test set. Measure both, or your interval is too narrow.
- **Pre-register the slices.** Choosing which slice to report after seeing the results is how a null result becomes a headline.
- **The threshold is a business decision.** Statistics tells you whether a difference is real; it cannot tell you whether 1.5 points is worth the migration cost. Say that out loud in class.
- **Small samples are not a scandal, they are a budget.** Forty prompts with an interval and an honest conclusion beats four hundred prompts nobody had time to read, as long as nobody pretends the interval is narrow.

## Watch out

- **Do not teach the maths for its own sake.** Learners need the reading and the two-line bootstrap, not a derivation of the t-distribution.
- **Do not use a p-value as a verdict.** With a small test set, "not significant" often means "underpowered", not "no difference".
- **Do not let anyone compare scores across different test sets** and then apply a statistical test as if the samples were paired.
- **The stale claim to retire:** "we don't need statistics, we can see it's better." You can see it is different. Whether it is better is a decision; whether the difference is real is a measurement.
