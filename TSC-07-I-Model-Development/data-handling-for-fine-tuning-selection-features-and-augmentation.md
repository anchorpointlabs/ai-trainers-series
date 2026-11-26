---
id: 07.02.I.K8
tsc: 7
level: Intermediate
code: K8
title: Data handling for fine-tuning: selection, features and augmentation
---

# Data handling for fine-tuning: selection, features and augmentation

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K8**


> **Framework text (verbatim):** "Data handling techniques for model fine tuning (e.g., feature engineering and selection methods, data augmentation strategies for generative models)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 8 of 17

**One-line version:** The model imitates exactly what you show it, form included — so the dataset is the specification, not the fuel.

## What it is

Everything between "we have data" and "we have a training set": selecting which examples to keep, engineering the fields the model sees, augmenting what is scarce, and formatting the result so training matches inference. For generative fine-tuning this work decides more of the final quality than any hyperparameter, because the model copies style, structure and mistakes with equal fidelity.

## Deep expansion

### The concept

A fine-tune is a curriculum, and the model learns both what to say and how to say it. That has a consequence learners find surprising: formatting errors propagate faster than content errors. Show it replies that always open with "Certainly!" and every output will. Show it one malformed JSON example in fifty and you will get malformed JSON at a predictable rate. Selection therefore favours *consistency and coverage* over volume, and augmentation must preserve the property the model is supposed to learn.

### The sub-concepts

**Selection.** Exact and near-duplicate removal first — MinHash or embedding similarity — because duplicates silently up-weight one pattern. Then quality filtering (length, language, refusal templates, garbled text), diversity sampling (cluster the corpus, sample across clusters rather than from the top), and decontamination: check whether any evaluation item leaked into training. Duplicates are also the cheapest source of overfitting.

**Feature engineering and selection.** For tabular or hybrid tasks, decide what the model should see rather than infer: normalise dates and currencies, encode categorical fields, and drop high-cardinality identifiers that let the model memorise rows. Target encoding leaks the label if computed before the split; the rule is always fit on train, apply to validation.

**Augmentation.** Paraphrase and back-translation for linguistic variety; counterfactual swaps (names, currency, dates) to stop spurious attribute binding; instruction reformulation so the model sees the same task asked several ways; and for images, geometric and colour augmentation for robustness. The invariant: augmentation must not change the correct answer. Rephrasing an instruction is safe; rewriting the target reply is authoring new data.

**Formatting.** Use the model's own chat template, mask the loss on prompt tokens so the model is graded on its answer, decide the truncation policy explicitly, pack short sequences if your trainer supports it, and keep the training distribution identical to what production will send.

### How it connects to the rest of the framework

`TSC7-Basic-K4` is preprocessing and cleaning at the entry level; `TSC7-Intermediate-K9` is synthetic data as an augmentation source; `TSC7-Intermediate-K10` and `TSC7-Intermediate-K5` are the fine-tuning and optimisation these datasets feed; `TSC7-Advanced-K8` and `TSC7-Advanced-A4` scale the same work to distributed pipelines; `TSC7-Intermediate-K4` says which metric proves the curation helped.

### What is current as of November 2026

- **Data work is now the stated differentiator.** Labs and vendors talk about curation, filtering and instruction diversity rather than architecture, and the same shift is visible in in-house teams building on the GPT-6 generation, Claude 5.5 or Gemini 3.1 Pro.
- **Synthetic augmentation is routine and audited.** Generating paraphrases and edge cases is standard, with a real-data holdout used to check the generator did not narrow the distribution.
- **Provenance and licensing became procurement questions.** Buyers ask where fine-tuning data came from, whether consent covers it, and whether it can leave the country under PDPA obligations.

### Common misconceptions

- *"More data is always better."* Beyond a point, more of the same teaches the model to imitate your templates harder, not to generalise.
- *"Augmentation can't hurt."* Flip the label by accident and you have taught the model a false rule at scale.
- *"Deduplication is housekeeping."* Duplicates are weighted examples; ten near-copies of one case is a deliberate decision to overfit it.
- *"It came from the CRM, so it's clean."* CRM exports carry test records, duplicated contacts, placeholder text and staff notes that were never meant for a customer to see.

## How a student should understand it

**Mental model:** the central kitchen. Ingredients are washed, cut to a consistent size and portioned before they reach any stall. A bad cut cannot be rescued by a better wok.

**Three things they can do after this bullet:**
1. Build a deduplicated, decontaminated, split dataset with a documented selection rule.
2. Choose an augmentation that provably preserves the label.
3. Explain why formatting consistency matters more than dataset size.

**Misconceptions to kill:** that volume beats curation, that augmentation is free, and that source systems are clean.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The central kitchen.** Every stall gets ingredients washed, cut and portioned to a standard. The stall with the best wok still fails if the chicken arrived cut wrong, and nobody at the stall can tell — the defect was baked in three steps earlier. Where it breaks: the central kitchen has a taster at the pass; a fine-tuning run has none unless you built an evaluation, which is why a cutting-step defect surfaces only in production.

**Assessment books with only one question type.** Five hundred questions that all ask the same thing teach a pattern, not a subject. A learner scoring full marks on that book fails the exam that asks the same content differently — the exact behaviour of a model trained on near-duplicates. Where it breaks: the student can be taught the missing question types; a model given near-duplicates has no way of telling you which variation it never saw.

### Worked example with a real tool

A learner has 12,000 support conversations exported as JSONL and a 200-item internal eval set. Type this into a coding assistant:

```
Write a Python data-prep script for support.jsonl:
  fields: ticket_id, customer_msg, agent_reply, created_at, channel

1. Drop rows with empty replies, agent-internal notes (lines starting
   with "NOTE:"), and replies under 20 characters.
2. Near-duplicate removal: MinHash on customer_msg + reply, threshold
   0.9, reporting how many rows were removed and why.
3. Contamination check: flag any row whose customer_msg shares a
   25-token shingle with anything in eval.jsonl (report count).
4. Split by ticket_id into train/val/test 80/10/10, stratified by
   channel, and assert no ticket_id appears twice.
5. Write chat-format JSONL using a placeholder for the template, and
   print token-length percentiles for the reply field.
```

Point at step 2 (duplicates are the quiet cause of "it memorised the training set"), step 3 (contamination makes every later metric a lie), step 4 (splitting by row rather than entity leaks the same customer across splits), and the percentiles — they tell you where truncation will silently cut answers.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two fine-tunes, same base model, one trained on a deduplicated set.
2. **State the objective** — produce a defensible dataset and say why it is defensible.
3. **Recall prior learning** — cleaning and preprocessing from the Basic level.
4. **Present the content** — selection, features, augmentation, formatting.
5. **Guide** — run the duplicate report on a sample together and read it.
6. **Elicit performance** — teams write their selection rule in five lines.
7. **Give feedback** — debrief: which rule would you defend to an auditor?
8. **Transfer** — apply the checklist to each learner's real corpus next week.

## What the framework doesn't mention but trainers need to know

- **Consent and licensing travel with the data.** A fine-tune on customer conversations needs a basis for that use, and the answer is usually in the contract, not the technical team.
- **Personal data must be handled before training, not after.** Masking names and identifiers is a preprocessing step; removing them from weights later is not possible.
- **Split by entity, not by row.** The same customer, thread or document in both train and test produces impressive metrics and a useless model.
- **Label noise needs measurement.** Sample a hundred examples, have two people grade them, and record the disagreement rate; it sets the ceiling on your evaluation.

## Watch out

- **Do not demo augmentation that shifts the answer.** It looks clever and teaches a false rule.
- **Do not present a clean dataset without the selection rule.** "We cleaned it" is not reproducible.
- **Do not skip the contamination check.** A benchmark win on leaked data is the most expensive kind of embarrassment.
- **The stale claim to retire:** "we'll clean the data at the end." In November 2026 the dataset is the design, and the end is too late.
