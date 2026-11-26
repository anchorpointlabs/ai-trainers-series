---
id: 07.01.B.K4
tsc: 7
level: Basic
code: K4
title: "Data preparation: cleaning, de-duplication and what a training set must contain"
---

# Data preparation: cleaning, de-duplication and what a training set must contain

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K4**


> **Framework text (verbatim):** "Data pre-processing, de-duplication and cleaning techniques (including understanding of training data requirements for AI models, common data quality issues)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 4 of 15

**One-line version:** The model is a mirror of the data you feed it — so the job is to decide what belongs in the mirror before you spend a single GPU-hour.

## What it is

Data preparation is everything you do to raw material before it becomes a training set: deciding what to collect, stripping what should not be there, removing repeats, fixing encoding, and splitting the result into training, validation and test portions. It is unglamorous, it is where most projects actually fail, and at Basic level it is the single highest-leverage skill in the whole TSC. A model trained on badly prepared data does not just underperform; it learns the defects.

## Deep expansion

### The concept

A generative model learns the statistical shape of whatever it is shown. Show it duplicated documents and it becomes confident about the duplicated content. Show it unclosed HTML tags and it will eventually produce them. Show it only formal English and it will not write like a hawker centre. There is no separate "quality" module you can bolt on afterwards — the data *is* the specification.

Training data requirements, stated plainly: **enough** (volume to cover the patterns), **representative** (the distribution you actually care about), **clean** (free of boilerplate and corruption), **non-duplicated** (so frequency means importance rather than copy count), **lawful** (licensed or permitted for this use), and **separated** (no leakage between the sets you train on and the sets you judge with).

### The sub-concepts

**Collection and licensing.** Where the text or images came from, and whether the licence permits training. This is a legal question before it is a technical one, and it is the question most beginners skip.

**Cleaning.** Removing HTML, navigation boilerplate, repeated headers, control characters, broken encodings and truncated records. A cleaned corpus is shorter and better; both are improvements.

**De-duplication.** Exact duplicates (identical strings) and near-duplicates (same article with a different byline). Near-duplicate removal usually uses hashing of overlapping word shingles — MinHash is the standard technique. Duplicates distort the loss: the model spends capacity memorising one document it has seen forty times.

**Quality filtering.** Heuristics (length, language identification, proportion of symbols), classifier-based scoring, and removal of toxic or personal content. Every filter encodes a judgement, and that judgement lands in the model.

**PII and sensitive content.** Names, NRIC numbers, addresses, phone numbers. If you would not put it on a slide, do not put it in the corpus.

**The three splits.** Training (learn), validation (tune decisions while training), test (judge once, at the end). Contamination happens when test examples were in the training data — the model looks brilliant and is actually reciting.

### How it connects to the rest of the framework

`TSC7-Basic-K5` (tokenisation) turns cleaned text into the actual training input; cleaning determines what gets tokenised. `TSC7-Basic-K6` (loss) is where duplication shows up as a misleadingly low training number. `TSC7-Basic-A3` is this bullet performed with code. `TSC7-Intermediate-K8` and `K9` extend it to feature engineering, augmentation and synthetic data. And `TSC8-Basic` is where the fairness consequences of your filtering choices get assessed.

### What is current as of November 2026

The frontier conversation has moved from "more data" to "better-chosen data". Labs serving the GPT-6 generation, Claude 5.5 and Gemini 4 Argon describe their advantage less in raw volume and more in curation, synthetic data mixtures and post-training data — and open-weight fine-tuning practice has followed: small, carefully cleaned, task-specific sets now beat large scraped ones for most adaptation work.

Two practical shifts for a Basic class. First, **duplication detection is a standard step, not an advanced one** — most modern training pipelines run near-duplicate removal by default. Second, **synthetic data is now a normal ingredient**, which means the trainer must teach the failure mode: a model trained on another model's output inherits and amplifies its errors. "Model collapse" is the shorthand.

### Common misconceptions

- *"More data is always better."* Beyond a point, unfiltered data adds noise, cost and legal exposure without adding capability.
- *"Cleaning is optional if the model is big."* A bigger model memorises your duplicates more thoroughly.
- *"De-duplication means removing exact copies."* Near-duplicates do most of the damage and are invisible to a `drop_duplicates` call.
- *"Test data can be the leftover slice."* If the test set came from the same scrape as the training set, it may already be contaminated.
- *"Any public data is fair game."* Publicly visible is not the same as licensed for training.

## How a student should understand it

**Mental model:** a wet-market fish counter. The fish is the same fish; the grading is the job. Nobody buys ungraded fish at a restaurant, and no model should be trained on an ungraded corpus.

**Three things they can do after this bullet:**
1. Write down the six requirements for a training set and check a real dataset against each.
2. Run exact and near-duplicate detection on a small corpus and report the reduction.
3. Explain why a contaminated test set produces a model that looks better than it is.

**Misconceptions to kill:** that volume substitutes for quality, that cleaning is a preprocessing afterthought, and that de-duplication only means identical strings.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Photocopying the worksheet forty times.** If a teacher photocopies one worksheet forty times into the revision pack, the student concludes that topic is 80% of the exam. The syllabus did not change; the pack did. Duplicates in a corpus are that revision pack.

**The prep kitchen at a zi char stall.** Before service, someone washes, trims and portions. Skip it and every dish that night carries the same grit. The prep is not the cooking, and it decides the cooking.

### Worked example with a real tool

A five-line cleanup on a JSONL file, in Colab with pandas. Real code, real output:

```python
import pandas as pd, re
df = pd.read_json("reviews.jsonl", lines=True)
print("raw rows:", len(df))

df["text"] = (df["text"]
    .str.replace(r"<[^>]+>", " ", regex=True)   # strip HTML
    .str.replace(r"\s+", " ", regex=True)       # collapse whitespace
    .str.strip())
df = df[df["text"].str.len().between(80, 4000)]  # drop stubs and dumps
df = df.drop_duplicates(subset=["text"])
print("after clean+dedup:", len(df))
```

What to point at afterwards: the two numbers. Ask the room what the gap represents, and whether those were bad rows or a misleading training signal. Then search the file for the same sentence twice — near-duplicates usually survive this code, which is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a model output that repeats one sentence three times, then reveal the duplicate-heavy corpus behind it.
2. **State the objective** — by the end you can audit a dataset against six requirements and run a cleaning pass.
3. **Recall prior learning** — from TSC #1 they know data bias matters; now they handle it.
4. **Present the content** — the six requirements, the four cleaning operations, and the three splits.
5. **Guide** — run the snippet together, predicting the row counts before executing.
6. **Elicit performance** — pairs take a small messy dataset and produce a cleaned version plus a one-line audit.
7. **Give feedback** — compare pairs; the common error is over-filtering, which silently removes a dialect or a whole category.
8. **Transfer** — each learner lists the data they already hold and whether they are allowed to train on it.

## What the framework doesn't mention but trainers need to know

- **Licensing sits above technique.** A perfectly cleaned corpus you had no right to use is a liability. Teach learners to ask "where did this come from and what does the licence say" before any code.
- **Over-cleaning is a real failure.** Aggressive language or length filters remove Singlish, dialects and short-form content, and the model then cannot serve those users. Every filter has a constituency it erases.
- **Near-duplicate detection is cheap and rarely taught.** A MinHash pass over a few thousand rows takes minutes and teaches more than any lecture on data quality.
- **Contamination is invisible without a check.** Teach one concrete test: search your training file for exact strings from your test set.

## Watch out

- **Do not demo on a scraped dataset of unclear provenance.** Use a licensed or self-collected sample, and say why.
- **Do not present cleaning as a linear checklist.** It is iterative: cleaning changes the distribution, which changes what counts as dirty.
- **Do not let "de-duplication" become only the pandas one-liner.** That is exact matching; the damage is usually near-duplicates.
- **The stale claim to retire:** "just get more data." In November 2026 the differentiator in almost every credible pipeline is curation, not crawl volume.
