---
id: 07.01.B.A5
tsc: 7
level: Basic
code: A5
title: "Naming a model's limits and proposing the first fix"
---

# Naming a model's limits and proposing the first fix

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Ability A5**


> **Framework text (verbatim):** "Identify limitations and propose initial improvements to models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Ability · Bullet 15 of 15

**One-line version:** "It is not good enough" is not a finding; "it drops the second clause in 6 of 20 samples, and here is the cheapest change that would fix that" is.

## What it is

This is the ability to look at a model's actual failures, sort them into categories, work out which category matters most, and propose a specific, proportionate first improvement. It is the final bullet of the Basic TSC for a reason: it is the point where everything earlier — data, loss, metrics, fine-tuning — becomes a diagnosis rather than a procedure.

## Deep expansion

### The concept

A limitation is a *pattern* of failure, not a single bad output. Finding patterns requires sampling systematically and reading with a rubric, which is why this skill is harder than it looks and why it is so rarely done properly.

The working method:

1. **Collect a fixed sample.** Twenty to fifty outputs from a defined input set. Not the worst ones, not the best — a sample.
2. **Read them against criteria** you wrote down beforehand: correctness, completeness, format, tone, refusal behaviour, length.
3. **Tag each failure** with a short code. Free text produces a mess; five codes produce a chart.
4. **Count.** Which category dominates? Is the count stable if you re-sample?
5. **Localise.** Is the failure in the data (the model never saw this case), the prompt (the instruction was ambiguous), the decoding (temperature too high), or the model's capability (it cannot do this at this size)?
6. **Propose the cheapest fix first** that addresses the dominant category.

The discipline is in step 6. Learners want to propose fine-tuning because it is the most impressive-sounding option. The honest ladder starts cheaper: clarify the prompt, add a schema, adjust decoding, add retrieval, then fine-tune, then change the model, and only then change the architecture.

### The sub-concepts

**Error taxonomy.** Five or six stable codes reused across samples: wrong fact, missing element, wrong format, wrong tone, hallucinated citation, refuses a legitimate request. Reuse is what makes counting possible.

**Severity weighting.** A rare failure that breaks a payment is worse than a common one that reads slightly stiff. Count and severity are two axes, not one.

**Stratified review.** Check whether failures concentrate in one input type — long inputs, Singlish, tables, numbers. Concentration usually points at data coverage.

**Capability versus configuration.** A model that can do the task but is prompted badly is a different problem from one that has never seen the pattern. Distinguishing them determines which fix is even possible.

**The proportionate fix.** The smallest change that would move the dominant category. Anything larger needs evidence you do not yet have.

**The re-test.** Apply the fix, rerun the same sample, recount. Without a re-test the improvement is a hypothesis.

### How it connects to the rest of the framework

`TSC7-Basic-K6` gives the metrics that tell you *whether* something is wrong; this bullet tells you *what*. `TSC7-Basic-K4` explains why a data-shaped failure exists. `TSC7-Basic-K8` is one of the fixes on the ladder, not the only one. `TSC5-Basic-A4`/`A5` are the evaluator's version of the same discipline. And `TSC6-Basic-K1` is the retrieval fix that Basic learners most often overlook.

### What is current as of November 2026

Two shifts make this skill more valuable, not less. First, **frontier models fail differently than they used to**: fewer outright grammatical collapses, more plausible-but-wrong specifics, more silent omission of a constraint in a long instruction. The taxonomy has moved from "broken output" to "confidently incomplete output". Second, **model-assisted review is cheap enough to be routine** — a strong model can tag a few hundred outputs against your rubric in minutes, which means the bottleneck is now writing the rubric and auditing the tags, not reading every output.

The practical implication for a Basic class: error analysis is no longer the slow part of the work, so there is no excuse for skipping it before proposing a fix.

### Common misconceptions

- *"It hallucinates, so we need to fine-tune."* Hallucination is a category, not a diagnosis. Retrieval fixes some, data fixes others, and fine-tuning can make it worse.
- *"One bad output proves a limitation."* One output proves one output. A pattern needs a sample and a count.
- *"More data will fix it."* More of the same data fixes coverage gaps and worsens everything else.
- *"A bigger model is the improvement."* Sometimes. It is also the most expensive option and the least informative experiment.
- *"The fix has to be technical."* A rewritten instruction fixes a large share of real failures, at zero training cost.

## How a student should understand it

**Mental model:** a food hygiene inspection report. It does not say "the kitchen is bad"; it names the specific faults, ranks them, and says what would raise the grade. That is what a limitation analysis looks like.

**Three things they can do after this bullet:**
1. Sample twenty outputs, tag them with five reusable codes, and report the distribution.
2. Distinguish a data gap from a prompt gap from a capability gap, with evidence.
3. Propose the cheapest fix for the dominant category and say how they would test whether it worked.

**Misconceptions to kill:** that one bad output is a finding, that fine-tuning is the default fix, and that a fix is done when it is applied rather than when it is re-tested.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food hygiene grade.** A "B" is not a vague judgement — it comes with a list of specific faults and the specific changes that would raise it. A model review should read the same way.

**The clinic, not the pharmacy.** A patient who says "I feel terrible" gets questions before medicine. The questions are the analysis; the medicine is one of several possible fixes and often not the first one tried.

### Worked example with a real tool

Take twenty real inputs, generate answers, and tag them in a spreadsheet — then count in pandas:

```python
import pandas as pd
df = pd.read_csv("review.csv")   # columns: input, output, tag, severity

print(df["tag"].value_counts())
print(df.groupby("tag")["severity"].mean().sort_values(ascending=False))
print(df[df.tag == "missing_clause"].head(3)[["input", "output"]])
```

With a real prompt to produce the outputs:

```
You are drafting replies to customer emails for a tuition centre.
For each email, reply in under 90 words, name the specific class
and time, and end with one question. Do not invent a policy.
```

What to point at afterwards: the count table, then the three examples of the dominant category. Ask the room which fix they would try first, and force them to defend it against the cheaper option. The answer is usually "the prompt did not say which clause to keep", not "we need to fine-tune".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show one bad output and one good one, then ask whether the model is good. The room will split, which is the lesson.
2. **State the objective** — by the end you can produce a tagged failure sample and defend one proportionate fix.
3. **Recall prior learning** — from K6 they know the metric; now they find the cause.
4. **Present the content** — the six-step method, the taxonomy, the fix ladder, the re-test.
5. **Guide** — tag ten outputs together on screen, arguing about codes as you go.
6. **Elicit performance** — pairs tag twenty outputs from their own domain and write a one-paragraph finding.
7. **Give feedback** — challenge every finding that lacks a count, and every fix that starts at fine-tuning.
8. **Transfer** — each learner writes the one failure category they would investigate first in their own work, and why.

## What the framework doesn't mention but trainers need to know

- **The rubric is the real artefact.** Criteria written after seeing outputs are criteria fitted to the outputs. Write them first.
- **Counts change minds, adjectives do not.** "Six of twenty" survives a meeting; "a bit unreliable" does not.
- **Sample from the hard cases too.** Random sampling over a friendly input set produces a flattering distribution. Stratify by input type.
- **Improvements can regress.** A prompt change that fixes format often breaks tone. Always rerun the full sample, not just the failing cases.

## Watch out

- **Do not let "identify limitations" become a complaint session.** Require a count and a proposed fix for every limitation named.
- **Do not accept fine-tuning as the first answer.** Ask what the cheapest change would be; make them rule it out with evidence.
- **Do not treat a model's self-report as analysis.** Asking the model why it failed produces plausible fiction.
- **The stale claim to retire:** "we need a bigger model." In November 2026, most narrow-task failures in a well-scoped system are data coverage, prompt specification or retrieval — and a bigger model fixes none of those.
