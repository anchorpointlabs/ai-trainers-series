---
id: 07.01.B.A3
tsc: 7
level: Basic
code: A3
title: "Preparing a training set: clean it, shape it, split it, prove it"
---

# Preparing a training set: clean it, shape it, split it, prove it

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Ability A3**


> **Framework text (verbatim):** "Preprocess and prepare data for generative training (e.g., clean and format datasets, use libraries (e.g., Pandas, NumPy) for data manipulation, split data into training, validation and test sets)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Ability · Bullet 13 of 15

**One-line version:** The deliverable is not a clean dataframe — it is three files you can defend, with a written record of every row you removed and why.

## What it is

This is the doing-version of data preparation: taking a raw file, applying the cleaning and formatting steps, splitting it into training, validation and test sets, and producing artefacts a colleague could rerun. The observable outcome is three files plus a short log — row counts before and after each step, and the reason for each filter. If you cannot show that log, you have not prepared data; you have edited some.

## Deep expansion

### The concept

A preparation pipeline is a sequence of decisions, each of which removes rows. The professional habit is to make each removal **countable and reversible**. Countable, because a filter that drops 40% of your corpus has changed what the model will learn and you need to see that number. Reversible, because six weeks later someone will ask why a category is missing from the output, and "I don't know, the script did something" is not an answer.

The split is where the ability is actually tested:

- **Training set** — what the model learns from. Typically the largest portion.
- **Validation set** — used during development to make decisions: when to stop, which setting to keep. It is allowed to influence you.
- **Test set** — touched once, at the end. Every peek erodes its value, and repeated peeking turns it into a validation set with extra ceremony.

Splitting must also prevent **leakage**. If one customer's five support tickets land in both training and test, the model can memorise the customer and score well without generalising. The fix is to split by group — by customer, by document, by date — not by row.

### The sub-concepts

**Row-level versus group-level splits.** Row-level is the default and is wrong whenever rows are not independent. Group by the entity that generated them.

**Temporal splits.** For anything time-based, train on the past and test on the future. Random splits let the model see the future, which flatters it and embarrasses you in production.

**Stratification.** Keeping the class or category balance similar across splits, so a rare category is not entirely in the test set.

**Formatting for the trainer.** Producing the columns the training code expects — usually a `messages` array or a `text` field — and validating that every row conforms.

**Determinism.** A fixed seed, so the split is reproducible. Without one, two runs of the same script produce different numbers.

**The audit log.** Counts and reasons, saved next to the data. This is the artefact that makes the work reviewable.

### How it connects to the rest of the framework

`TSC7-Basic-K4` is the theory of cleaning and de-duplication; this is the execution. `TSC7-Basic-K9` defines the format you are producing. `TSC7-Basic-A4` trains on what you produce here, and `TSC7-Basic-A5` interprets the failures that a bad split would hide. `TSC5-Basic-K3` (evaluating outputs) assumes the test set is genuinely unseen — this bullet is what makes that assumption true.

### What is current as of November 2026

The tooling has consolidated around two layers: pandas or Polars for tabular manipulation, and the Hugging Face `datasets` library for anything that will be fed to a trainer. `datasets` handles streaming, caching and Arrow-backed storage, which matters once files exceed memory, and its `train_test_split` supports stratification and seeding directly.

Two practical shifts. First, **near-duplicate detection is now a standard pipeline stage** rather than a research nicety, because contaminated splits are a known cause of inflated results. Second, **Polars has become a credible default for large files** where pandas is slow or memory-hungry, though the operations are the same in spirit. For a Basic class, pandas remains the right teaching tool — the concepts transfer directly.

### Common misconceptions

- *"Cleaning means deleting bad rows."* Cleaning means making a decision about each category of badness and recording it. Deleting is one of several options, and sometimes the wrong one.
- *"A random split is always fine."* It is fine only when rows are independent. Support tickets, patient records and documents are not.
- *"The test set is just the leftover 10%."* It is the only unbiased estimate you will get. It deserves care, not leftovers.
- *"Validation and test are the same thing."* Validation is for decisions; test is for the final claim. Mixing them is how teams report numbers they cannot reproduce.
- *"If the code runs, the data is ready."* The code runs on garbage too.

## How a student should understand it

**Mental model:** setting an exam paper. You write the questions, keep a separate set for the mock exam, and lock the actual paper in a drawer. A teacher who lets the class see the paper has not measured anything.

**Three things they can do after this bullet:**
1. Produce train, validation and test files from a raw dataset with a fixed seed and a printed row count for each.
2. Split by group or by date where rows are not independent, and explain the choice.
3. Hand a colleague a log showing every filter applied and how many rows each removed.

**Misconceptions to kill:** that a random split is always valid, that the test set is disposable, and that preparation is done when the script stops erroring.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The exam paper in the drawer.** The teacher who previews the actual paper with the class gets wonderful scores and no information. The value of the test set comes entirely from it being unseen, and it is spent the first time you look.

**The same family in both queues.** If one family sends five members to the training queue and one to the test queue, the model can learn the family rather than the task. Split by family, not by person.

### Worked example with a real tool

An end-to-end preparation cell that produces three files and a log:

```python
import pandas as pd, json
from sklearn.model_selection import train_test_split

df = pd.read_json("raw_tickets.jsonl", lines=True)
log = [("raw", len(df))]

df["text"] = df["text"].str.replace(r"\s+", " ", regex=True).str.strip()
df = df[df["text"].str.len() > 50];              log.append(("min_len", len(df)))
df = df.drop_duplicates(subset=["text"]);        log.append(("dedup", len(df)))

# split by customer so the same customer never spans sets
customers = df["customer_id"].unique()
tr_c, tmp_c = train_test_split(customers, test_size=0.2, random_state=42)
va_c, te_c = train_test_split(tmp_c, test_size=0.5, random_state=42)

for name, ids in [("train", tr_c), ("val", va_c), ("test", te_c)]:
    part = df[df["customer_id"].isin(ids)]
    part[["text"]].to_json(f"{name}.jsonl", orient="records", lines=True)
    log.append((name, len(part)))

print(log)
```

What to point at afterwards: the log, and the assertion that no `customer_id` appears in two files. Run that assertion out loud — three lines of set intersection — because the point of the exercise is proof, not output.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a model with 98% test accuracy and 60% in production, then reveal the duplicate leakage.
2. **State the objective** — by the end you can produce three defensible files and a log that explains them.
3. **Recall prior learning** — from K4 they know what to remove; now they build the pipeline.
4. **Present the content** — the three splits, group and temporal splits, leakage, determinism, the log.
5. **Guide** — run the cell together, then break it by removing `random_state` and rerunning.
6. **Elicit performance** — pairs prepare a small dataset of their own with a written log.
7. **Give feedback** — check every pair's split for leakage; the group split is the one most will skip.
8. **Transfer** — each learner writes the split rule their own data would need and why.

## What the framework doesn't mention but trainers need to know

- **The split rule is a modelling decision.** Group and temporal splits often make scores worse and the model better. Say that before learners see the drop, or they will revert.
- **Never prepare test data twice.** Build it once, freeze it, and log a hash. Regenerating it after seeing results is how contamination creeps in.
- **Small data punishes careless splits.** With 200 rows, one leaked group can move the score by ten points.
- **Write the log to a file.** A printed log vanishes when the notebook closes; a `prep_log.json` next to the data survives the project.

## Watch out

- **Do not use a dataset with unclear provenance in a demo.** Learners copy the demo, and the licence travels with the copy.
- **Do not skip the leakage check.** It is the difference between a demonstration and a lesson in how to fool yourself.
- **Do not let pandas syntax eat the session.** The concepts are the split and the log; the one-liners can be looked up.
- **The stale claim to retire:** "80/10/10 random split, always." In November 2026, with grouped and time-ordered data everywhere, an unexamined random split is a known source of results that do not survive deployment.
