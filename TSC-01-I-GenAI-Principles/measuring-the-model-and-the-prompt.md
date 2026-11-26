---
id: 01.02.I.A4
tsc: 1
level: Intermediate
code: A4
title: "Measuring the model and the prompt: what a change actually bought you"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Measuring the model and the prompt: what a change actually bought you

> **TSC #1 Generative AI Principles and Applications · Intermediate · Ability A4**


> **Framework text (verbatim):** "Analyse generative AI models' performance metrics and evaluate the influence of prompt variations."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Ability · Bullet 9 of 10

**One-line version:** You do not need a research team to know whether a change helped — you need twenty frozen items, three criteria, one variable at a time, and the discipline to record the result before you get attached to the new prompt.

## What it is

The ability to build a small evaluation, choose metrics that fit the task, and run a controlled comparison between prompt variations or model tiers. Done at practitioner level it takes an afternoon and replaces the two most common workplace claims — "this prompt is much better" and "the new model seems worse" — with a number you can defend.

## Deep expansion

### The concept

An evaluation is three things: a **fixed set** of items with known-good answers or a rubric, **criteria** that can be applied consistently, and a **protocol** that changes one thing at a time. The set is the asset. Prompts are cheap and models change quarterly; the set is what lets you re-test in an hour instead of re-arguing for a week.

Metrics follow the task type (`TSC1-Intermediate-A02`). Extraction: field accuracy, exact match on numbers and dates, and the rate of invented values. Classification: precision and recall on the outcome that costs most — usually false negatives. Summarisation: coverage of the required points, faithfulness (no claims outside the source), and length compliance, scored against a checklist. Drafting: rubric scores for tone, structure and factual traceability, plus a pairwise human preference. Anything with a hard requirement — a schema, a format, a statutory phrase — gets a pass/fail, not a rating.

Then the discipline: vary the prompt only, hold model, temperature, context and tools constant, run each variant several times, and record the spread. The number that matters is not the best run; it is the distribution.

### The sub-concepts

**The golden set.** Twenty to fifty real items, including the ugly ones: the scanned page, the unusual name, the document with no answer, the table with a missing row. Freeze it, version it, and never tune on it. If you tune on the test, you are measuring memory.

**Criteria before scoring.** "Rate 1–5" without anchors produces noise. Write the checklist: "names the decision, names the owner, contains no fact absent from the source, stays under 150 words." Four binary checks beat one vague score.

**Variance.** The same prompt, five times, gives five outputs. Report the spread — "4 of 5 correct" is a different claim from "correct". A prompt that wins once has not won.

**LLM-as-judge, and its biases.** Using a model to score outputs is now standard and useful at scale. It carries known biases: it prefers longer answers, it is sensitive to the order of the options, and it favours its own family's style. Mitigations: pairwise comparison with the order swapped, a rubric in the judge prompt, and a human spot-check of twenty judgements.

**Confounds.** Model version, decoding settings, context length, retrieval on/off, system prompt, and the order of instructions. Change one, log the rest. Most "the model got worse" reports are a silent change in one of these.

**What prompt variation actually moves.** Format compliance, coverage, verbosity and refusal rate respond strongly. Knowledge, arithmetic reliability and calibration respond weakly. Expecting a prompt to fix a knowledge gap is the most common misallocation of effort.

**Cost and latency as metrics.** Token price, thinking budget and added latency change the business case. A variant that is two points better and four times slower is a decision, not a win.

### How it connects to the rest of the framework

`TSC1-Intermediate-K03` is the theory of what a prompt changes; this is the measurement. `TSC1-Intermediate-A02` sets the metric per task type. `TSC1-Intermediate-A01` decides whether the use case is worth evaluating at all. `TSC5` is the full evaluation discipline — statistical tests, fairness metrics, human studies — and this entry is deliberately its practitioner-sized precursor.

### What is current as of November 2026

Structured outputs have made format compliance measurable and largely solved: a schema either validates or it does not, which removes a whole category of prompt iteration. Reasoning modes have added a cost dimension that did not exist before — effort settings change accuracy and token spend together, so evaluations now need a cost-per-accepted-output column.

Judge models are embedded in vendor tooling and in internal pipelines, and the honest practice is to disclose which model judged which outputs. Public benchmarks have become less informative as models are trained against them, which strengthens the case for the small private set. None of this changes the method; it changes what you have to record.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A higher benchmark score means a better model for us."* Benchmarks measure exam questions written by someone else, on documents that are not yours.
- *"One great output proves the prompt works."* One output proves one sample. Run it five times on ten items.
- *"Temperature zero makes it deterministic."* Largely, and not guaranteed across providers, batching or hardware. Do not build a compliance claim on it.
- *"Human rating is objective."* Two reviewers disagree about tone constantly; that is why moderation and anchors exist.
- *"We do not have time to evaluate."* You are already evaluating, informally, with worse evidence and no record.

## How a student should understand it

**Mental model:** the checklist at the factory gate. You do not grade the whole factory; you sample the output against a specification, every day, and you keep the specification fixed while you change the line.

**Things they can do after this bullet:**
1. Build a twenty-item golden set from their own work in under an hour.
2. Write three binary criteria per task type and score two prompt variants against them.
3. Report a result with a spread, a cost and the variable they changed.

**Misconceptions to kill:** benchmark scores transfer, one good output is evidence, and evaluation is a specialist activity.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The PSLE oral exam.** Two examiners, a rubric with bands, and a moderation process — precisely because a single examiner's "8 out of 10" is unreliable. If your evaluation has one judge and no rubric, you have built the thing moderation exists to fix.

**The NEA grade.** A checklist audit with spot checks, re-run periodically, because a stall that passed in March can fail in June. Your golden set is the checklist; the quarterly re-run is the audit.

### Worked example with a real tool

Extraction from invoices, in ChatGPT or Claude, ten invoices prepared beforehand:

```
Variant A: "Extract the invoice number, date, vendor and total from this invoice."
```

```
Variant B: "Extract four fields from the invoice text below and return a JSON
object with keys: invoice_no, date (YYYY-MM-DD), vendor, total_sgd (number,
two decimals). If a field is not printed, use null. Do not infer or calculate
a value that is not printed."
```

What to point at: score both on the same ten invoices for field accuracy, then count the nulls. A guessed total is an invisible error; a null is an honest gap, and the difference in the null rate between A and B tells you what the schema did. Run each variant five times and show the spread changing between runs. Then swap to a cheaper model tier and watch accuracy drop in a specific, nameable way rather than uniformly — which is the point: measure where it drops, not whether it "feels worse".

### Live demo or exercise

**Two prompts, one set.** Pairs receive a ten-item set, two prompt variants and a blank score sheet with three binary criteria. Twenty minutes, then report: variant, score, spread, and the one item they argued about. The argument about the single item is where the criteria get sharpened, which is the real learning.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two outputs and ask which is better; watch the room split.
2. **State the objective** — by the end you can settle that argument with a score sheet.
3. **Recall prior learning** — what prompt changes do and do not move.
4. **Present the content** — set, criteria, protocol, variance, judge bias, cost.
5. **Guide** — build the score sheet for extraction together.
6. **Elicit performance** — pairs score two variants on ten items.
7. **Give feedback** — compare sheets; fix criteria that two people read differently.
8. **Transfer** — each learner freezes a ten-item set for their highest-volume task and puts the prompt in version control.

## What the framework doesn't mention but trainers need to know

- **The set needs an owner and a refresh date.** Stale evaluation sets quietly pass bad systems. Add a quarterly review, plus every incident.
- **Measure the human's time, not just the model's accuracy.** Time per accepted output and rework rate decide adoption more often than a two-point accuracy difference.
- **Single runs produce confident nonsense.** Any claim with no spread attached should be treated as an anecdote, including your own.
- **Offline scores do not predict user satisfaction for drafting.** Pair the set with five real users reading five outputs; it is cheap and it catches everything the rubric missed.

## Watch out

- **Do not publish results from five samples.** State the sample size or say nothing.
- **Do not let a vendor's model judge its own family undisclosed.** Swap order, use a mixed judge panel, and spot-check by hand.
- **Do not tune on the evaluation set.** Hold one out, even twenty items, and touch it once.
- **The stale claim to retire:** "we will know it is working when it feels better." Feelings are what the score sheet exists to replace.
