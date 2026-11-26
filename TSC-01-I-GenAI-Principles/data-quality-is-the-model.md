---
id: 01.02.I.K5
tsc: 1
level: Intermediate
code: K5
title: "Data quality is the model: preprocessing, pipeline and inherited bias"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Data quality is the model: preprocessing, pipeline and inherited bias

> **TSC #1 Generative AI Principles and Applications · Intermediate · Knowledge K5**


> **Framework text (verbatim):** "Importance of data quality, preprocessing, model pipeline and model training (e.g., impact of data bias from training data)."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Knowledge · Bullet 5 of 10

**One-line version:** A generative model is a compressed average of its data, so every cleaning decision, duplicated page and missing group ends up in the output — and in most enterprises the decisive data problem sits in your own pipeline, not the vendor's.

## What it is

Data quality is decided in three places: the corpus the model was pre-trained on, the curated examples used in post-training, and the documents and pipelines your organisation wires up at inference time. Bias is not a separate topic bolted on — it is what happens when a group is under-represented, historically mislabelled, measured badly, or when a small error concentrates on the same people at deployment.

## Deep expansion

### The concept

Training is compression with a loss function. Whatever is frequent becomes the default, whatever is duplicated is over-weighted, and whatever is thin is smoothed away. None of this is malfeasance; it is what fitting a distribution does. The professional consequence is that "we used a good model" is not a quality statement, and "the data was clean" is a claim needing an owner and a method.

For an Intermediate practitioner the useful discipline is knowing **which stage a symptom belongs to**. A model that writes generic Singapore English has a corpus coverage problem, which you cannot fix. One that misses the footnote in your scanned contract has a preprocessing problem, which you can. One that answers in the wrong tone for your ministry has a post-training problem, which a good brief usually patches. Confusing the three is the most expensive habit in enterprise AI.

### The sub-concepts

**Coverage versus correctness.** A corpus can be clean and unrepresentative. Local names, dialects, small languages and jargon are thinly covered, so the model regresses to the international default. Coverage and correctness fail differently.

**Duplication and contamination.** Repeated text is learned more strongly. If your test questions appeared in training, your benchmark score is a memory test, not a capability test — which is why public leaderboards predict so little about your documents.

**Labelling and instructions.** Post-training data is written by people, and ambiguity in one example teaches ambiguity. An unclear instruction repeated five thousand times teaches a model to be unclear in a very confident voice.

**Preprocessing in your own pipeline.** This is where most enterprise failures live: OCR that drops a decimal point, PDF extraction that reorders a table's columns, chunking that splits a header from its rows. The model is then blamed for a transcription error it never saw.

**The four bias mechanisms.** *Representation* — a group is rare in the data. *Historical* — the labels encode a past decision, including a discriminatory one. *Measurement* — the proxy recorded is a poor stand-in. *Deployment* — the model is applied to a population it was not built for. Only the last is usually visible to the people affected.

**Pipelines need versioning.** A frozen evaluation set, a dated data snapshot and a record of which documents were in scope. Without them, "it worked last month" is not reproducible.

### How it connects to the rest of the framework

`TSC1-Intermediate-K02` describes the stages this entry is about. `TSC1-Intermediate-A03` is the analysis skill that detects the resulting bias in output. `TSC1-Basic-A03` and `TSC1-Basic-A04` cover finding and masking sensitive data before it reaches a model. `TSC7` (Model Development) has the pipeline engineering depth, and `TSC8` covers the governance obligations.

### What is current as of November 2026

**Synthetic data** is now ordinary in post-training and increasingly present in pre-training, which introduces a question practitioners must discuss honestly: training on model output can narrow the distribution over successive generations. The risk is real and debated in magnitude — quote no figure.

**Licensing has become operational.** Content deals and opt-out mechanisms mean two vendors' models are no longer equivalent on provenance, and procurement now asks. And the **enterprise centre of gravity moved from the model to the data layer**: retrieval, document hygiene and evaluation sets are where the work now sits. Fine-tuning a small model on a few thousand well-curated examples is a routine first experiment for a narrow task, because curated data beats a bigger generic model on a house format.

### Common misconceptions

- *"More data is always better."* Duplicated, mislabelled or irrelevant data lowers quality. Curation beats volume.
- *"Bias is the model's fault."* Representation and history live in the data; deployment lives in your decision about where to point the model. Both are yours to govern.
- *"If the PDF looks right on screen, the extraction is fine."* Copy a table out of a PDF once and watch the columns collapse. Then imagine four thousand of them.
- *"The model knows when it is missing data."* It fills gaps fluently. Absence is invisible unless you build a check for it.

## How a student should understand it

**Mental model:** a stock cube made from everything in the pot. If the pot had too much salt, every dish from that cube is salty — and no skill at the stove fixes it.

**Things they can do after this bullet:**
1. Trace a wrong output to corpus coverage, post-training or their own preprocessing, with evidence.
2. Name which of the four bias mechanisms is operating in a given case.
3. Write the three data checks their pipeline needs before a model sees a document.

**Misconceptions to kill:** more data is better, bias is only the vendor's problem, and extraction is not part of the model.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Factory kaya versus your grandmother's.** Mass-produced kaya is consistent, safe and tastes like the average of every kaya ever made. The pandan from your grandmother's garden is not in it, because nobody wrote it down. Where it breaks: a recipe can be corrected by one person; a training corpus cannot.

**The PSLE marking team.** If two markers score the same script differently, the model trained on those scores learns the disagreement, and the inconsistency surfaces years later as a policy that cannot explain itself.

### Worked example with a real tool

Upload a scanned or table-heavy PDF — a quarterly outlet P&L is ideal — to ChatGPT or Claude:

```
Attached is our outlet P&L for last quarter (scanned PDF).
1. List every outlet with revenue and gross margin.
2. Mark any figure you could not read clearly as UNREADABLE instead of estimating.
3. Tell me which three outlets improved margin most, and show the subtraction
   for each before the ranking.
```

What to point at: whether UNREADABLE ever appears (usually not, even when a figure is genuinely illegible); whether the arithmetic shown matches the figures above it; and how one dropped decimal changes the ranking. The failure is in the pipeline — scanning and extraction — and the model has no way to know. Then ask how many of their monthly reports are built this way.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a fluent summary of a document with one silently wrong figure.
2. **State the objective** — by the end you can locate a data defect and name its owner.
3. **Recall prior learning** — pre-training, post-training, inference.
4. **Present the content** — the four data stages, the four bias mechanisms, versioning.
5. **Guide** — trace one defect end to end, out loud.
6. **Elicit performance** — pairs diagnose a broken document and draft the rule that would have caught it.
7. **Give feedback** — debrief; every diagnosis must name a stage and a check.
8. **Transfer** — each learner lists their three highest-volume document types and their extraction risk.

## What the framework doesn't mention but trainers need to know

- **The evaluation set is the real asset.** Twenty to fifty items with expected answers, including the nasty cases, frozen and versioned. It is the only defence against both bad data and bad prompts.
- **Data lineage is a governance deliverable.** Which documents fed which decision, with dates. Without it, a dispute cannot be answered.
- **Table and figure handling is the last mile.** Structured extraction from tables is where real documents fail, and it is a preprocessing problem far more often than a model problem.

## Watch out

- **Do not demo with real customer data.** Use a synthetic or redacted document, and say that you have.
- **Do not overclaim cleaning as bias removal.** Cleaning removes errors; it does not create representation.
- **The stale claim to retire:** "the model is only as good as its data, so wait for better models." The actionable half is your own pipeline, and that is fixable this quarter.
