---
id: 04.02.I.K5
tsc: 4
level: Intermediate
code: K5
title: Dataset quality and the training pipeline
---

# Dataset quality and the training pipeline

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K5**

> **Framework text (verbatim):** "Significance of dataset quality and model training, including data management (e.g., extract, transform and load process)."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Knowledge · Bullet 5 of 11

**One-line version:** A model cannot be better than the data it learned from, and the pipeline that turns raw records into training data is where that quality is won or lost.

## What it is

Data management for AI runs through **ETL**: extract from sources, transform into a clean and consistent form, load into the store that training or retrieval reads. Each stage has failure modes, and each failure mode surfaces later as a model defect. For selection, the practical consequence is that a model's published quality is a claim about its training data — and a fine-tune's quality is a claim about yours.

## Deep expansion

### The concept

The oldest line in computing applies with unusual force here: garbage in, garbage out. But generative training adds a twist — the model does not merely reproduce the garbage, it generalises from it. Duplicated rows teach over-representation. Mislabelled examples teach confident errors. Missing fields teach the model to invent plausible values rather than admit absence.

So the pipeline is not plumbing; it is the specification of the model's behaviour. Two teams with the same base model and the same fine-tuning recipe will get different results purely from data discipline, and that difference is usually larger than the difference between adjacent model tiers.

### The sub-concepts

**Extract: know what you are pulling.** Sources differ in reliability. A scraped web corpus carries undated claims, marketing language and duplicated pages. A structured internal system carries consistent fields and stale conventions. Extraction also has to respect consent and licensing — a dataset assembled from sources you may not use is a liability with a training run attached.

**Transform: the stage that decides everything.** Deduplication, normalisation, redaction of personal data, label correction, language identification, and removal of near-duplicates that would otherwise dominate the sample. For a Singapore deployment, transformation also means handling the real spelling of local names, addresses and code-switched phrasing, not silently "correcting" them into American English.

**Load: keep provenance.** Every record should carry where it came from and which version of the pipeline produced it. Without provenance you cannot answer "why does the model behave like this on refunds", and without a versioned snapshot you cannot reproduce a training run.

**Splits are part of the pipeline.** Train, validation and test must be separated before you look, and near-duplicates must be separated across splits too — otherwise a model that has memorised a record appears to generalise.

**Synthetic data lowers cost and raises risk.** Generating examples with a larger model is now standard practice for cold-start datasets. It inherits the generator's blind spots and mistakes, so human review is mandatory before synthetic data gates a release.

**Contamination is a quiet inflation.** If test questions were in the training data, the score measures recall, not capability. This is why static public benchmarks flatter models and why fresh, dated evaluation sets are worth the effort.

### How it connects to the rest of the framework

`TSC4-Advanced-K2` places these stages in the training sequence. `TSC4-Advanced-K3` requires the data preparation step before fine-tuning. `TSC4-Advanced-A2` is where a deliberately diverse evaluation set is built — the same discipline applied to testing rather than training. `TSC4-Intermediate-A4` is the output check that catches what the data taught. `TSC4-Advanced-K4` prices the curation labour, which is usually the largest line in a fine-tuning budget.

### What is current as of November 2026

For the 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — data quality has become the differentiator for organisations, precisely because model quality has converged:

- **Fine-tuning tools are commoditised; datasets are not.** Anyone can run an adapter job in an afternoon. Very few teams have a curated, deduplicated, reviewed set of a few thousand domain examples.
- **Synthetic data generation is a standard first step.** Use it to bootstrap, then have a domain expert rewrite the outputs. Unreviewed synthetic sets are the most common cause of a fine-tune that looks good in the notebook and fails in production.
- **Data protection expectations tightened.** Personal data in a training set is a PDPA issue with a retention clock; redaction at the transform stage is now normal practice, not optional hygiene.

### Common misconceptions

- *"More data is always better."* More *duplicated* data teaches repetition. Quality, deduplication and coverage beat volume.
- *"A model's quality is independent of its data."* The quality is the data, compressed.
- *"We will clean it later."* Cleaning after training means retraining. The transform stage is where the cost is lowest.
- *"Synthetic data is free data."* It is cheap to produce and expensive to trust.

## How a student should understand it

**Mental model:** a kitchen. Extract is the market run, transform is the prep — washing, trimming, portioning — and load is the fridge. Nobody believes a dish is better because the fridge is full; it is better because the prep was careful.

**Things they can do after this bullet:**
1. Name the three ETL stages and one failure mode of each.
2. Spot three data-quality risks in a described dataset.
3. Explain why a contaminated benchmark flatters a model.

**Misconceptions to kill:** that data volume substitutes for data quality, that cleaning is a later step, and that synthetic data is a shortcut around curation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker's prep.** The same recipe with wilted vegetables and yesterday's oil produces a different dish. The wok is not the variable; the prep is.

**The tuition-centre worksheet.** A worksheet with wrong answer keys teaches wrong answers confidently. A worksheet with the same question printed forty times teaches that question and nothing else. Both look like "a lot of practice".

### Worked example with a real tool

Make the room reason about consequences rather than definitions:

```text
A training dataset has duplicate rows and missing labels.
List two ways the resulting model could misbehave, and for each,
name the check that would have caught it before training.
```

What to point at afterwards: duplication leads to over-representation — the model becomes confidently wrong on the repeated pattern and fails on unseen variations; the catch is a deduplication count per category. Missing labels lead to invented fields — the model fills gaps plausibly; the catch is a completeness report per field before training begins. Then extend to contamination:

```text
Our evaluation set was assembled from the same source as the training
set. What does our 94% score actually tell us?
```

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two answer keys, one wrong, one repeated; ask which teaches more.
2. **State the objective** — by the end you can name what breaks a dataset and which check catches it.
3. **Recall prior learning** — pre-training versus fine-tuning, and what each learns.
4. **Present the content** — extract, transform, load; splits; synthetic data; contamination.
5. **Guide** — walk a small messy customer dataset together and list its defects.
6. **Elicit performance** — teams build a five-item pre-training checklist.
7. **Give feedback** — debrief, converting vague "clean the data" into specific checks.
8. **Transfer** — each learner applies the checklist to a dataset they actually hold.

## What the framework doesn't mention but trainers need to know

- **Data curation is the real cost of fine-tuning.** Not the training run. Weeks of expert labelling usually dwarf the compute bill.
- **Local language handling is a data decision.** If your corpus has been spell-corrected into standard English, your model will be worse at real Singapore input. Preserve the natural variation you expect to see at inference.
- **Provenance is an audit requirement, not a nicety.** When someone asks why the model produced a particular output, "we do not know which data taught it" is not an acceptable answer.
- **Retention and deletion obligations apply to training data.** A model trained on a record you were later required to delete cannot be selectively unlearned cheaply. Design for that before training.
- **Evaluation data deserves the same rigour as training data.** Many teams curate one and improvise the other.

## Watch out

- **Do not let the room think data work is junior work.** It is the highest-leverage engineering in the discipline and it is usually done badly.
- **Do not demo with real customer data.** Use synthetic or public examples; the ethics lesson is part of the content.
- **Do not claim a fine-tune "learned our business" without a held-out test.** It learned the shape of your examples.
- **The stale claim to retire:** "we have plenty of data." You have plenty of rows; you may have very few usable examples.
