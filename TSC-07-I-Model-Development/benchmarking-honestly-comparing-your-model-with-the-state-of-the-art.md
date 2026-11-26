---
id: 07.02.I.A3
tsc: 7
level: Intermediate
code: A3
title: Benchmarking honestly: comparing your model with the state of the art
as_at: 2026-11-26
review_by: 2027-02-25
---

# Benchmarking honestly: comparing your model with the state of the art

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A3**


> **Framework text (verbatim):** "Analyse generative models against state-of-the-art benchmarks."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 13 of 17

**One-line version:** A benchmark only means something when two systems were measured by the same ruler on the same day — and the useful comparison is usually the thing you would otherwise deploy.

## What it is

Analysing a model against the state of the art means placing it in context: how it compares with published results, with strong open baselines, and with the commercial alternative your organisation would actually use. The technical work is matching conditions, checking that the benchmark measures what your users care about, and reporting the result with enough statistical honesty that a decision can be made from it.

## Deep expansion

### The concept

A benchmark score is a measurement, and measurements are only comparable within a protocol. Change the prompt template, the number of few-shot examples, the decoding parameters, the preprocessing or the sample count, and the number moves — often by more than the difference you are trying to detect. So the first question is never "what is SOTA" but "what decision am I supporting". For an internal model, the decision is usually "keep the API call or switch to this fine-tune", and the correct comparison is against the API under your own prompts, not against a leaderboard.

### The sub-concepts

**Choosing the comparison set.** Three candidates: the deployed alternative, the strongest open baseline at a similar size, and the claimed state of the art. Report all three if you can, and be explicit that the first is the one that matters for the decision.

**Matched conditions.** Same harness, same prompt template, same few-shot examples, same decoding parameters, same preprocessing, comparable sample counts. Where that is impossible — a closed model that will not expose logits — say so, because it limits what you can conclude.

**Benchmark validity.** Public benchmarks saturate and leak: training data scraped from the web frequently contains the test items, and a benchmark that everyone has optimised for stops discriminating. A private, held-out set drawn from your own traffic is slow to build and worth more than any public leaderboard, because it cannot be contaminated by everyone else.

**Reporting.** Confidence intervals, several seeds where the run is stochastic, per-slice results (by language, length, difficulty, customer segment), and negative results. A comparison without an interval invites a decision the data cannot support.

### How it connects to the rest of the framework

`TSC7-Intermediate-K4` supplies the metric definitions and their failure modes; `TSC7-Intermediate-A2` covers the monitoring that produces these numbers during training; `TSC5` is the wider evaluation discipline; `TSC7-Advanced-K9` is the statistical inference needed to claim a difference; `TSC7-Intermediate-A1` is the build being judged.

### What is current as of November 2026

- **Public benchmarks saturate fast.** New models from the GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro / Gemini 4 Argon converge at the top of the standard suites within weeks of release, which is why vendors increasingly lead with private evaluations and task-specific results.
- **Harness standardisation helped and did not solve it.** Running the same open harness is now normal practice, but prompt templates still differ between reports, so cross-paper comparisons remain unreliable.
- **Crowd preference arenas became a primary signal.** Pairwise human votes on anonymised outputs are widely cited, with the known caveats of style bias, length bias and self-selection.

### Common misconceptions

- *"Higher score on a public benchmark means a better product."* It means better on that benchmark's distribution, prompt format and scoring rule.
- *"We beat GPT-6 on this test."* Almost always a different prompt, a different sample count or a subset of the test set.
- *"SOTA claims are verified."* Many are self-reported, some are on tuned subsets, and few include intervals.
- *"One benchmark is enough."* A single number hides the slice where your model is worse than the alternative.

## How a student should understand it

**Mental model:** two schools comparing exam results. If one sat a different paper, marked by a different teacher, with a different number of practice papers beforehand, the comparison is a conversation, not a measurement.

**Three things they can do after this bullet:**
1. Define the comparison set and the decision rule before running anything.
2. Run an evaluation with matched conditions and report intervals.
3. Explain to a manager why a leaderboard position is not a product claim.

**Misconceptions to kill:** that public benchmarks predict product quality, that cross-report comparisons are valid, and that one number decides.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Two tuition centres' claims.** Both advertise "90% of students improved". Different intake, different papers, different definition of improved. Neither number is false; the comparison is meaningless. Benchmark reports behave identically. Where it breaks: a tuition centre can publish its intake; a benchmark table rarely tells you which test prompts were tuned on.

**The hawker rating apps.** A stall with 4.8 stars on one app and 3.9 on another has not changed its char kway teow — the raters and the rubric did. Where it breaks: a model's score can also change because the test set leaked into training, which has no food analogue except a stall that knows the inspector's route.

### Worked example with a real tool

A learner must justify keeping their fine-tune instead of a frontier API. Type this into a coding assistant:

```
Build a fair comparison between three systems on my 300-case
private test set (tests.jsonl: instruction, reference, slice):

1. Systems: (a) frontier API with our production prompt,
   (b) our LoRA fine-tune, (c) base open model with the same prompt.
2. Fix decoding: temperature 0, same max tokens, same prompt
   template for (a) and (c); use the fine-tune's trained template.
3. Score with: exact-match where applicable, an embedding
   similarity, and a judge model with the rubric inline.
4. Report per-slice means with bootstrap 95% intervals, and a
   cost-per-1000-requests column using current list prices.
5. Flag any slice where the interval overlaps zero.
```

Point at step 2 — matching the template is the single biggest source of fake wins — step 4's cost column, because a two-point quality gain at ten times the price is a business decision, and step 5: overlapping intervals mean "no measurable difference", which is a legitimate and useful finding.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two "SOTA" claims that collapse when the protocol is inspected.
2. **State the objective** — run one defensible comparison and write the decision rule.
3. **Recall prior learning** — metrics from K4, monitoring from A2.
4. **Present the content** — comparison set, matched conditions, validity, reporting.
5. **Guide** — audit a published benchmark table together for missing detail.
6. **Elicit performance** — teams draft their own comparison protocol.
7. **Give feedback** — debrief: which conditions were unmatched?
8. **Transfer** — each learner runs the private-set comparison for their project.

## What the framework doesn't mention but trainers need to know

- **Cost and latency belong in the table.** Quality per dollar and quality per second are usually the actual decision variables.
- **Contamination auditing is real work.** Check for n-gram overlap between your test set and any corpus you trained on; assume public test sets are contaminated until shown otherwise.
- **Benchmarks measure the wrong thing for most products.** A support-deflection model is judged by resolution rate, not by an academic suite.
- **Publishing negative results is a service.** A well-run comparison that shows "no improvement" saves the next team a month.

## Watch out

- **Do not quote benchmark numbers from memory.** They change monthly; teach the protocol and let learners look up the current figures.
- **Do not compare across harnesses.** Different prompt formats produce differences larger than the effect being measured.
- **Do not let the judge model be the only scorer.** It shares biases with the systems it is grading.
- **The stale claim to retire:** "we beat the leaderboard." In November 2026 the defensible claim is "on our private set, with matched conditions, system A is better by this much, at this cost, on these slices".
