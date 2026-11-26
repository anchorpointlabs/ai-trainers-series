---
id: 04.03.A.A2
tsc: 4
level: Advanced
code: A2
title: Assess models against diverse datasets and scenarios
---

# Assess models against diverse datasets and scenarios

> **TSC #4 Generative AI Model Selection · Advanced · Ability A2**

> **Framework text (verbatim):** "Assess the effectiveness of models against diverse datasets and scenarios."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Ability · Bullet 6 of 8

**One-line version:** A model's score is a property of the test set, not of the model — change the set and you change the verdict.

## What it is

Assessing effectiveness means running a candidate model across several genuinely different datasets and scenarios and reading where performance falls off. "Diverse" is doing real work in that sentence: different languages, different domains, different document shapes, different user behaviours, different registers, and the adversarial edge where the model should refuse rather than guess.

## Deep expansion

### The concept

An aggregate accuracy figure hides its own denominator. A model can score impressively overall because it is excellent on the easy majority and catastrophic on the slice that carries the risk. This is not a statistical nicety — it is the normal shape of failure in enterprise AI, where ninety per cent of queries are routine and the ten per cent that matter are the ones the average conceals.

The discipline is therefore: **slice before you summarise.** Report per-segment numbers, find the maximum-minus-minimum gap, and treat the gap as a finding in its own right.

### The sub-concepts

**Distribution shift is the whole problem.** Benchmarks sample the general web; your workload samples your customers. A model tuned mostly on English web text can be strong on a general leaderboard and noticeably weaker on Tamil, Bahasa Melayu, code-switched Singlish, or Singapore civil-service terminology. That gap is invisible in the global average and decisive in the deployment.

**Build the test set deliberately, in three strata.** Roughly half representative production cases weighted by real frequency; roughly a third hard edge cases — ambiguous requests, multi-part questions, missing context, malformed input, regional phrasing; roughly a fifth adversarial and out-of-scope prompts, including injection attempts and requests the assistant must politely decline. Without that last stratum you are measuring fluency, not judgement.

**Respect sample size.** Thirty cases is a smoke test for continuous integration, not a release gate — one flipped case moves the score by over three points. A few hundred stratified cases is where a comparison starts to mean anything. Say this to the room before they argue about a two-point difference.

**Counterfactual testing is the sharpest tool.** Take real prompts and change one thing at a time — a name, a dialect, a pronoun, a postcode — holding all merits identical. If the recommendation flips, you have found a bias that no aggregate score would reveal. It is also the cheapest fairness audit available to a small team.

**Diverse does not mean exotic.** The most valuable diversity is usually within the same task: the same question asked politely, rudely, in shorthand, with a typo, and by someone who does not know the domain vocabulary.

### How it connects to the rest of the framework

`TSC4-Advanced-A3` is the time dimension of the same assessment — this bullet varies the *inputs*, that one varies the *hours*. `TSC4-Intermediate-A6` is the narrower version: comparing two variants on one task. `TSC4-Advanced-A4` asks whether the harness itself can run at scale. `TSC4-Intermediate-K5` explains why a model's published quality is really a statement about its training data, and `TSC4-Advanced-K2` supplies the vocabulary for the subgroups.

### What is current as of November 2026

The 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — has made public leaderboards less informative, not more:

- **Top models cluster tightly on the classic benchmarks.** The differences that decide a procurement are in latency, price, refusal behaviour and non-English performance, none of which the leaderboard headlines.
- **Static benchmarks are contaminated by construction.** Test questions have been on the public web for years and are in the training corpora. A high score may measure recall of the answers.
- **Regional benchmarks finally exist and should be used.** Southeast Asian language and culture evaluations are the honest way to check whether a global number survives contact with a Singapore user base.

### Common misconceptions

- *"It scored 92 per cent, so it works."* Ninety-two per cent of what? Name the slices, or the number is decoration.
- *"We tested it on our data, so we are covered."* If your data is all happy-path English, you tested the easy half.
- *"Diverse testing is a fairness box-tick."* It is a defect-finding technique that also happens to be the fairness audit.
- *"Synthetic test data is fine if it is realistic."* Synthetic data inherits the generator's blind spots and must be human-reviewed before it gates a release.

## How a student should understand it

**Mental model:** a health screening, not a weigh-in. The scale gives one number and tells you almost nothing; the panel of tests finds the one thing that is going wrong.

**Things they can do after this bullet:**
1. Build a three-strata test set for a stated task in under an hour.
2. Compute and report a subgroup gap rather than a single average.
3. Design a counterfactual swap to test for a dialect or name bias.

**Misconceptions to kill:** that one benchmark proves fitness, that aggregate accuracy is a summary rather than a concealment, and that diversity means adding a foreign-language sample and calling it done.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The PSLE average.** A class average of 75 tells you nothing about whether three pupils cannot read the question. Parents understand instantly that the average is the least interesting number in the room.

**The polyclinic versus the A&E.** A general practice that handles 95 per cent of walk-ins well can still be the wrong place for a heart attack. Aggregate throughput is not capability on the case that matters.

### Worked example with a real tool

Give the room one task and make them build the slices:

```text
We are deploying a customer-service assistant for a Singapore retailer.
List three diverse scenarios you would test it on, and for each, name
one thing that would count as failure.
```

What to point at afterwards: strong answers name Singlish and code-switching, local policy references (returns under the Consumer Protection (Fair Trading) Act, GST-inclusive pricing), and elderly customers writing in short fragments — each paired with a concrete failure, not "it might be wrong". Then push the counterfactual:

```text
The same complaint arrives from "Tan Wei Ming" and from "Rajesh Kumar".
Design a test that would detect whether the reply changes unfairly.
```

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show one aggregate score and three subgroup scores that contradict it.
2. **State the objective** — by the end you can build a sliced test set and defend the slices.
3. **Recall prior learning** — what an evaluation set is, from the Intermediate bullets.
4. **Present the content** — the three strata, the max-min gap, counterfactual swaps, sample sizes.
5. **Guide** — build one stratum together for a task the room knows.
6. **Elicit performance** — teams build the remaining two strata and a counterfactual.
7. **Give feedback** — debrief, converting vague failures into observable ones.
8. **Transfer** — each learner names the slice their current system most likely fails.

## What the framework doesn't mention but trainers need to know

- **The slice that matters is usually the one with the least data.** High-risk, low-frequency cases are exactly what a random test set under-samples. Oversample them deliberately.
- **A test set ages.** Once a failure is fixed and promoted into the set, the set gets easier. Retire saturated cases and add fresh production failures.
- **Report the gap, not just the average, in the procurement document.** The gap is what the risk committee needs to see.
- **Latency and cost are subgroups too.** A model that is accurate but p99-slow on long inputs fails a different slice. Slice those as well.
- **Do not let a vendor's benchmark table into the room as evidence.** It is a marketing artefact about a different distribution.

## Watch out

- **Do not present a single number as a conclusion.** Any slide that says "accuracy: 94%" without a breakdown teaches the wrong habit.
- **Do not equate diversity with translation.** Dialect, register, urgency, typo density and domain vocabulary are all more informative than a second language sample.
- **Do not run the fairness test only on the sensitive attribute you thought of.** Names, schools, postcodes and dialect all act as proxies.
- **The stale claim to retire:** "the leaderboard says it is the best model, so it is the best for us." In November 2026 the leaderboard is a starting filter, nothing more.
