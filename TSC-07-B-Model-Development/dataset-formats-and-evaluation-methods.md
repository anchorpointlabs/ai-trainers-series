---
id: 07.01.B.K9
tsc: 7
level: Basic
code: K9
title: "Dataset formats and evaluation methods for generative tasks"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Dataset formats and evaluation methods for generative tasks

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K9**


> **Framework text (verbatim):** "Common dataset formats and evaluation methodologies for generative tasks."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 9 of 15

**One-line version:** The format decides whether the model can learn from your data at all, and the evaluation method decides whether you can tell that it did.

## What it is

Dataset formats are the on-disk conventions training tools expect — JSON Lines, CSV, Parquet, or a Hugging Face `datasets` object with defined columns. Evaluation methodologies are the ways you judge a generative model's output: held-out loss, benchmark suites, task-specific scoring, model-as-judge, and structured human review. Both halves of this bullet are unglamorous and both are where projects quietly go wrong.

## Deep expansion

### The concept

A generative training pipeline is a chain of expectations. The loader expects a file. The formatter expects fields. The tokeniser expects strings. The loss expects labels aligned to tokens. If any link disagrees, the run either crashes — which is kind — or trains on the wrong thing, which is not.

Formats, in practice:

- **JSON Lines (`.jsonl`).** One JSON object per line. The default for fine-tuning uploads and for most open tooling, because it streams well and survives a corrupt line without losing the file.
- **CSV.** Familiar, fragile. Quoting, embedded newlines and encoding break it in ways that are hard to see.
- **Parquet.** Columnar and compressed. What large pipelines and Arrow-backed `datasets` use under the hood.
- **Chat format.** A list of messages with roles (`system`, `user`, `assistant`). This is what instruction-tuned models are trained on and what most APIs accept.

Evaluation methods, in practice: **held-out loss**, **benchmark suites**, **task-specific metrics**, **model-as-judge**, and **human review against a rubric**. They answer different questions and a serious evaluation uses at least two.

### The sub-concepts

**One record, one example.** A training row should be a single complete example of the behaviour you want. Rows that concatenate three unrelated things teach the model that unrelated things follow each other.

**Schema stability.** If some rows have `"input"` and `"output"` and others have `"prompt"` and `"response"`, the loader silently drops or misaligns. Validate the schema before training, not after.

**The chat template.** Instruction models expect special tokens marking who is speaking. Doing this by hand is a reliable source of subtle breakage; use the tokeniser's `apply_chat_template`.

**Held-out evaluation.** The same metric on data the model never saw. Cheap, necessary, and not sufficient.

**Benchmarks.** Standard suites that allow comparison with published work. Useful for a sanity check, dangerous as a target, and frequently contaminated.

**Model-as-judge.** A strong model scores or compares outputs against a rubric. Fast, scalable, and biased in characteristic ways — it prefers length, confidence and its own style.

**Human review.** Slow, expensive, and still the reference standard for anything a customer will read.

### How it connects to the rest of the framework

`TSC7-Basic-K4` produces clean content; this bullet decides the shape it ships in. `TSC7-Basic-K6` covers the loss and metric definitions; this bullet covers the *methodology* — which data, which comparison, which judge. `TSC7-Basic-A3` is the split performed in code, `TSC7-Basic-A4` is training on a benchmark, and `TSC5-Basic-K2`/`K3` are the evaluator's fuller treatment. If TSC #5 is "how to judge a model you did not build", this bullet is "how to judge one you did".

### What is current as of November 2026

Two shifts. First, **JSONL with a messages array has become the lingua franca** for fine-tuning uploads, and most providers now accept the same shape, which makes portability between current frontier models and open-weight tooling far better than it was a few years ago. Second, **model-as-judge is now standard practice and standard liability**: practitioner teams use a strong model to score thousands of outputs against a written rubric, then audit a sample by hand. The failure mode is well known — judges reward verbose, confident answers — so the rubric and the audit are what make it credible.

Benchmark contamination has also become a mainstream concern: models trained on data that overlaps public test sets can appear better than they are, which is why serious teams keep a private, freshly collected evaluation set.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Any CSV will load."* Encoding, quoting and embedded newlines routinely break CSV. JSONL exists for a reason.
- *"The format is a technicality."* The format determines which tokens get trained. It is the model's specification.
- *"High benchmark score means a good model for us."* Benchmarks measure the benchmark. Your task needs your own evaluation set.
- *"An LLM judge is objective."* It is a cheaper rater with known biases. Useful, not neutral.
- *"One evaluation is enough."* One number, one view. Use at least a metric and a rubric, on data the model has not seen.

## How a student should understand it

**Mental model:** an order chit at a hawker centre. The stall can cook anything, but only if the chit is legible and uses the columns the kitchen reads. A perfectly good order written on the wrong form gets cooked wrong or not at all.

**Three things they can do after this bullet:**
1. Convert a spreadsheet of examples into valid JSONL in the chat-message schema, and validate every row.
2. Choose two evaluation methods for a stated task and say what each one misses.
3. Explain why a benchmark score is not evidence that the model works on your data.

**Misconceptions to kill:** that formats are a formality, that benchmarks transfer, and that one evaluation number settles a decision.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The order chit.** Every stall has a pad with columns: table, dish, remarks, time. Write in the wrong column and the kitchen reads "no chilli" as a table number. Data format is the pad, and the kitchen does not complain — it just cooks the wrong thing.

**The food hygiene grade versus the taste test.** A grade is standardised, published and cheap to check. The taste test is what the customer actually experiences. Benchmarks are the grade; your own evaluation set is the taste test. You need both, and they disagree often.

### Worked example with a real tool

Build a four-row dataset in the exact format a fine-tuning job expects, then load and validate it:

```python
import json
rows = [
  {"messages": [
     {"role": "system", "content": "You write replies for a tuition centre."},
     {"role": "user", "content": "Parent asks to change lesson slot."},
     {"role": "assistant", "content": "Sure — which day suits? We have Tue 5pm and Sat 10am."}]},
]
with open("train.jsonl", "w") as f:
    for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")

from datasets import load_dataset
ds = load_dataset("json", data_files="train.jsonl", split="train")
print(ds.column_names, len(ds))
print(ds[0]["messages"][-1]["content"])
```

What to point at afterwards: the column is `messages`, not `text`, and the answer sits under `assistant`. Then show what happens when a row uses `response` instead — the trainer either errors or, worse, drops it silently.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — paste a broken JSONL line and a working one side by side and ask what differs.
2. **State the objective** — by the end you can produce a valid training file and pick two evaluation methods for a task.
3. **Recall prior learning** — from K4 they cleaned data; now they package it.
4. **Present the content** — four formats, the chat schema, five evaluation methods, contamination.
5. **Guide** — build and load the file together, deliberately introducing one schema error.
6. **Elicit performance** — pairs convert five rows from a spreadsheet into JSONL and validate with `load_dataset`.
7. **Give feedback** — run every pair's file through the loader on screen; the errors teach more than the successes.
8. **Transfer** — each learner specifies their own evaluation set: how many rows, who writes them, what the rubric checks.

## What the framework doesn't mention but trainers need to know

- **Validation is a two-line habit.** Load the file, print the count, print one record. Most dataset disasters are caught here.
- **Your evaluation set is an asset.** Private, freshly written, and small beats public and contaminated. Tell learners to build it before they train.
- **Judge bias is predictable.** Length, confidence, formatting and self-similarity all inflate scores. Randomise order, hide the model identity, and audit a sample by hand.
- **Keep a regression file.** Twenty rows the model must always get right. Rerun after every change. It is the cheapest quality infrastructure there is.

## Watch out

- **Do not use a public benchmark as your only evidence.** It is the demo that impresses and the decision that fails.
- **Do not hand-build chat templates.** Use the tokeniser's template; hand-built markers are wrong in ways that do not error.
- **Do not run a judge without a rubric.** "Which is better" produces noise dressed as data.
- **The stale claim to retire:** "we scored well on the benchmark, so we ship." In November 2026, contamination and benchmark overfitting are common enough that no serious team releases on a public score alone.
