---
id: 07.03.A.K9
tsc: 7
level: Advanced
code: K9
title: Statistical inference for generative models: sampling, uncertainty, calibration
as_at: 2026-11-26
review_by: 2027-02-25
---

# Statistical inference for generative models: sampling, uncertainty, calibration

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K9**


> **Framework text (verbatim):** "Advanced statistical inference techniques for generative tasks."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 9 of 20

**One-line version:** A generative model does not produce an answer; it produces a distribution you sample from once — and every serious engineering decision downstream depends on remembering that.

## What it is

Statistical inference for generative tasks covers both directions: how you draw from the model (sampling and decoding), and how you reason about the results (uncertainty, confidence intervals, significance). It is the discipline that stops a team from shipping a change because one comparison looked better, and stops a product from presenting a sampled answer as a fact.

## Deep expansion

### The concept

The output layer of a language model is a probability distribution over the next token. Decoding chooses one — greedily, or by sampling with temperature, top-k, top-p or min-p filtering. Each choice changes the distribution of outputs for the same input, which means the same prompt evaluated twice can give two different answers. Any claim of the form "our model scores X" is therefore a claim about a *sample*, and needs the usual apparatus: a variance estimate, a sample size, and a test.

The second half is calibration. Token probabilities are not probabilities that the statement is true. A model can emit "the policy expires in March" with high per-token confidence and be wrong, because confidence measures fluency under the model's distribution, not correspondence with the world. Treating logprobs as accuracy is the single most common statistical error in applied generative AI.

### The sub-concepts

**Decoding as a statistical choice.** Temperature reshapes the distribution; top-p truncates it to a cumulative mass; min-p keeps tokens relative to the most likely one. For evaluation you usually want the *distribution* of outcomes, so fix a seed, run many samples, and report the spread rather than a single run.

**Uncertainty that is actually about correctness.** Three practical proxies: agreement across independent samples (self-consistency), semantic entropy over meaning clusters rather than tokens, and a held-out conformal calibration that maps a score to a coverage guarantee. All three let a system abstain, which is often worth more than a small accuracy gain.

**Comparison tests for generated output.** Paired comparisons on the same items need paired tests — McNemar for binary outcomes, bootstrap over items for continuous scores. Reporting an unpaired confidence interval on paired data overstates uncertainty; reporting a point estimate with no interval overstates confidence.

**Clustered and dependent samples.** If twenty outputs come from one source document, they are not twenty independent observations. Cluster at the document or user level or the interval will be too narrow.

**Multiple comparisons.** Test twelve prompt variants and one will look best by chance. Pre-register the comparison, or correct for the number of looks.

### How it connects to the rest of the framework

`TSC7-Advanced-K1` explains why the output is a distribution; this bullet is what you do about it. `TSC5-Advanced-A1` (A/B tests and user studies) is the human-facing version, and `TSC5-Intermediate-K6` covers hypothesis testing for evaluation. `TSC7-Advanced-A3` uses these methods to decide whether an optimisation actually helped.

### What is current as of November 2026

Uncertainty has become a product feature rather than an evaluation nicety: assistants now surface confidence, ask clarifying questions or route to a human when a sample is unstable. Reasoning-style models complicate the statistics, because their output distribution is sharper — many samples agree — without necessarily being more correct, so agreement alone overstates confidence on hard items. Calibration against a held-out set remains the only honest check, and it is the part most teams still skip.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Temperature 0 makes it deterministic."* It makes it nearly so on one stack; batching, kernels and hardware can still change the output.
- *"The logprob was 0.98, so it is 98% likely to be right."* That number is about the next token, not the claim.
- *"We improved the score by three points, so we improved the model."* Without an interval and a paired test, that is noise with a decimal point.
- *"More samples always give a better estimate."* More samples tighten the estimate of the *wrong* quantity if the prompt or the rubric is biased.

## How a student should understand it

**Mental model:** a weather forecaster who gives you one day's weather, not the climate — ask for the forecast distribution, then check the forecast against what happened.

**Three things they can do after this bullet:**
1. Set up an evaluation that reports a distribution and an interval, not a single number.
2. Choose a paired test appropriate to their comparison.
3. Design an abstention rule from sample agreement or calibrated scores.

**Misconceptions to kill:** that a fixed seed makes results comparable across stacks, that logprobs are correctness probabilities, and that a point estimate is a result.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The taxi uncle's estimate.** Ask one uncle the fare to the airport and you get a number; ask five and you get a range, plus a sense of which route they all avoid. One sample is an anecdote, five is a distribution.

**The 4D result.** Nobody buys a ticket on one number drawn once. The draw is the product; the odds are the engineering. Where it breaks: 4D outcomes are independent, and model samples are correlated through the prompt.

### Worked example with a real tool

Make the class confront sampling variance directly:

```
I am comparing two prompts for extracting dates from contracts.

Prompt A scored 0.81 exact match on 150 documents.
Prompt B scored 0.84 on the same 150 documents.

Tell me:
1. Whether that difference is worth acting on, and what test you
   would run (be specific about paired vs unpaired).
2. What the confidence interval depends on, and what would make
   it narrower without collecting more documents.
3. How sampling temperature changes the variance of both scores.
4. One way this comparison could be silently invalid.
```

What to point at afterwards: run both prompts three times each with temperature above zero and watch the ranking move. Then run McNemar on the paired per-document outcomes. The lesson lands: a three-point gap with 150 items and stochastic decoding is usually not a finding.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — the same prompt, five runs, five different scores on screen.
2. **State the objective** — report a comparison with an interval and the right test.
3. **Recall prior learning** — the model as a distribution from `TSC7-Advanced-K1`.
4. **Present the content** — decoding, calibration, paired tests, clustering, multiple comparisons.
5. **Guide** — run the A/B prompt comparison live.
6. **Elicit performance** — pairs compute an interval and a paired test on supplied data.
7. **Give feedback** — debrief the invalid comparisons the class produced.
8. **Transfer** — each learner writes the evaluation protocol for their next model change.

## What the framework doesn't mention but trainers need to know

- **Variance from prompt templates often exceeds variance from model choice.** Fix the template before comparing models.
- **Abstention is a feature.** A system that says "I am not sure" is more trustworthy than one that is confidently wrong at the same accuracy.
- **Report the spread, not just the mean.** Stakeholders understand error bars faster than they understand p-values.
- **Keep the evaluation set frozen and versioned.** Statistical rigour on a moving test set is theatre.

## Watch out

- **Do not teach p-values without teaching what they are not.** The misinterpretation is universal and expensive.
- **Do not demo with temperature above zero and present one run as the result.** It is the error you are trying to teach against.
- **Do not overclaim calibration from a small set.** A conformal guarantee on forty items is a very wide guarantee.
- **The stale claim to retire:** "the model said it confidently, so it must be right." In 2026 confidence is a style, and calibration is a measurement.
