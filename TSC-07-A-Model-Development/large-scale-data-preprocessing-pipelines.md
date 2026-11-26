---
id: 07.03.A.A4
tsc: 7
level: Advanced
code: A4
title: Pre-processing at scale: pipelines, custom algorithms, distributed compute
---

# Pre-processing at scale: pipelines, custom algorithms, distributed compute

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A4**


> **Framework text (verbatim):** "Develop innovative pre-processing methodologies for complex and large-scale data sets (e.g., architect large-scale data pre-processing pipelines, develop custom pre-processing algorithms, optimise pre-processing for distributed computing environments)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 15 of 20

**One-line version:** Pre-processing at scale is design under a budget — every stage you add multiplies the cost of every future re-run, so the innovator is the one who removes stages, not the one who adds them.

## What it is

This ability is building data pipelines for corpora too large and too messy for scripts: layered storage, stage ordering that puts cheap filters first, custom cleaning algorithms for a specific domain, and distribution that survives skew and partial failure. The deliverable is a pipeline whose cost per million documents is known and whose output is reproducible from a snapshot.

## Deep expansion

### The concept

Three design decisions determine almost everything downstream.

**Layering.** Keep raw data immutable (`bronze`), write each transformation as a new immutable layer (`silver`), and produce task-ready datasets from those (`gold`). Nothing overwrites anything. This is what makes a re-run possible after a bug, and it is the difference between a week of work and a lost month.

**Ordering by cost.** Filters should run from cheapest to most expensive: byte length, encoding validity, exact hash dedupe, language identification, boilerplate removal, near-duplicate detection, model-based quality scoring, PII redaction. Reversing this order is the most common architectural mistake — running a classifier over documents that a length filter would have dropped is pure waste, repeated on every run.

**Determinism.** Each stage keyed by (input snapshot, code version, parameters), each output shard named by that key. With this, a stale shard is detectable rather than mysterious.

### The sub-concepts

**Custom pre-processing algorithms.** Domain specifics beat generic cleaning: HTML boilerplate extraction that understands a site's template, OCR post-correction for scanned government forms, normalisation for mixed-script text (Chinese, Jawi, Tamil), Singlish-aware handling where a spelling corrector would destroy the signal. The innovation is usually in domain knowledge encoded as rules, not in a bigger model.

**Near-duplicate detection.** Normalise (whitespace, casing, boilerplate), hash exactly, then run locality-sensitive matching — MinHash over shingles or SimHash with a Hamming threshold — and cluster. Choose the threshold on a labelled sample; small changes move the removal rate a lot.

**Quality filtering.** A small classifier or a perplexity score, applied to a sample first to calibrate a threshold, then to the corpus. Keep the rejection log with the reason code; it is the audit trail for every quality claim you later make.

**Distributed execution.** Partition by a hash of the document ID so work is balanced and re-runs are stable; split oversized records into sub-shards; cap per-worker memory and stream batches rather than loading partitions. The bottleneck is usually shuffle volume or per-document Python overhead, not CPU.

**PII and rights handling.** Redaction and licence metadata belong in the pipeline, not in a spreadsheet. If a document's licence is unknown, the pipeline should mark it, and training should exclude it by that mark.

### How it connects to the rest of the framework

`TSC7-Advanced-K8` is the framework and tooling layer; this bullet is the design work on top. `TSC7-Basic-K4` covers cleaning at small scale, `TSC7-Basic-A3` the train/validation/test split discipline, and `TSC7-Advanced-K10` consumes the gold layer. `TSC9-Intermediate-K5` covers the data-protection obligations the redaction stage satisfies.

### What is current as of November 2026

Two shifts. First, GPU-accelerated dataframe and tokenisation libraries have moved the expensive stages — tokenising, embedding for dedupe, classifier scoring — onto accelerators, changing the economics of a re-run. Second, documentation of pre-training data mixtures has become a differentiator for the labs, and the practical lesson for everyone else is that dataset versioning and per-stage rejection logs are now expected engineering practice rather than good intentions.

### Common misconceptions

- *"Cleaning is a one-off job before training."* It is a pipeline that runs every time the corpus or the model changes.
- *"More filters mean better data."* Every filter costs money and removes signal; each one needs evidence it improves the final evaluation.
- *"Near-duplicate detection is a solved problem."* Thresholds are domain-specific and drift as the crawl changes.
- *"Distributed means faster."* It means failure is partial and skew is invisible unless you measure it.

## How a student should understand it

**Mental model:** a fish-processing line. Gut, scale, fillet, inspect, pack — in that order, because inspecting a fish you were going to reject anyway wastes the inspector.

**Three things they can do after this bullet:**
1. Draw a five-stage pipeline ordered by cost with a rejection log at each stage.
2. Write one domain-specific cleaning rule and measure its effect.
3. Estimate cost per million documents before running the job.

**Misconceptions to kill:** that cleaning is one-off, that more filters are better, and that a cluster is automatically faster.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The fishmonger's line.** Gut before you fillet; you do not wrap a fish you are going to throw away. Order is the whole craft.

**The condominium's recycling chute.** Sorted at source, it is cheap; sorted at the plant, it is expensive and half of it is contamination. Filtering early is sorting at source.

### Worked example with a real tool

Design before coding:

```
Corpus: 8M web pages, mixed English/Chinese, from 40 sites with
strong templates, 60% are near-duplicates of each other, plus
200k scanned PDFs with OCR text.

1. Give the stage order with the expected rejection rate at each
   stage, cheapest first, and say what each stage costs to run.
2. Write two custom cleaning rules specific to this corpus that a
   generic cleaner would miss.
3. Where do you sample to calibrate the near-duplicate threshold,
   and what do you look for?
4. What breaks if one site contributes 70% of the pages?
```

What to point at afterwards: question 2 reliably produces the strongest learning — template stripping before dedupe changes the duplicate rate dramatically, and OCR garbage needs length-and-dictionary filters that would be wrong for web text. Question 4 is skew, and the answer is per-domain caps plus a per-site metric, not more workers.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a duplicate rate that halves after one boilerplate rule; ask what else is hiding.
2. **State the objective** — design a cost-ordered pipeline with per-stage rejection logs.
3. **Recall prior learning** — formats and sharding from `TSC7-Advanced-K8`.
4. **Present the content** — layering, ordering, custom rules, dedupe, skew.
5. **Guide** — walk the 8M-page design together.
6. **Elicit performance** — teams design for their own corpus.
7. **Give feedback** — peer review for order and for unmeasured stages.
8. **Transfer** — each learner instruments their existing pipeline with one rejection counter.

## What the framework doesn't mention but trainers need to know

- **Store the rejection reason, not just the count.** You will be asked why a document was dropped six months later.
- **Do the expensive stages on a sample first.** Calibrate, then commit.
- **Licence and PII metadata must survive every join.** Losing provenance is unrecoverable.
- **The cost of a re-run is the real design constraint.** Simpler pipelines get fixed more often.

## Watch out

- **Do not build a giant bespoke pipeline for a small corpus.** Match the machinery to the volume.
- **Do not present dedupe rate as quality.** It is hygiene; curation is separate.
- **Do not skip the skew analysis.** It is the most common silent failure at scale.
- **The stale claim to retire:** "clean the data once, then train." In 2026 the pipeline is the asset and it runs continuously.
