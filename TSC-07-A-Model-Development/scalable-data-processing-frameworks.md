---
id: 07.03.A.K8
tsc: 7
level: Advanced
code: K8
title: Scalable data processing: what changes when the corpus is ten terabytes
---

# Scalable data processing: what changes when the corpus is ten terabytes

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K8**


> **Framework text (verbatim):** "Scalable data processing frameworks."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 8 of 20

**One-line version:** At a few gigabytes you write a script; at ten terabytes you write a job that can fail halfway, resume, and produce the same output twice — and that difference is the whole subject.

## What it is

Scalable data processing frameworks are the tools that turn a corpus too large for one machine into a repeatable pipeline: Polars, DuckDB and Arrow for single-node columnar work, Apache Spark for cluster-scale batch, Ray Data for ML-native streaming batches, Dask for Python-parallel workloads, plus the storage formats — Parquet, record shards, compressed archives — that make any of it fast.

## Deep expansion

### The concept

The transition from local scripting to scalable processing is not about volume as such; it is about *failure modes changing shape*. On one machine, an out-of-memory error tells you where you are. On a cluster, a worker dies silently, a shuffle spills to disk, one partition holds half the data, and the job still reports success with subtly wrong output.

Four properties separate a scalable pipeline from a script:

1. **Deterministic and idempotent.** Re-running the job on the same input produces byte-identical output. Without this you cannot tell a data bug from a re-run.
2. **Checkpointed.** Work is written in immutable shards, so a failure costs one shard, not the night.
3. **Partition-aware.** The unit of parallelism matches the unit of storage, and skew is measured rather than discovered.
4. **Cost-observable.** You know the cost per million documents before you process a billion.

Deduplication deserves separate mention because it is where most beginner pipelines quietly fail: near-duplicates defeat exact hashing, so you normalise aggressively (whitespace, boilerplate, encoding), hash, then run locality-sensitive matching such as MinHash over shingles to catch the rest. Train a model on a corpus with 30% near-duplicates and you have taught it repetition, which shows up as degenerate output later.

### The sub-concepts

**Columnar and Arrow-native tooling.** Polars and DuckDB put a huge amount of work on one machine because they avoid materialising rows in Python. Before reaching for a cluster, most teams should fix their format and their single-node tool.

**Distributed batch.** Spark's model is map/shuffle/reduce over partitions; the expensive operation is always the shuffle. Design so the shuffle is small or avoidable, and remember that reading 10 TB of small JSON files is slower than reading 10 TB of Parquet.

**ML-native streaming.** Ray Data and equivalents stream batches into training without a full materialisation step, which is how you avoid paying for storage twice.

**Tokenisation and packing at scale.** For language models the real cost is the tokeniser and the sequence packing. Tokenise once, cache to disk as token IDs, and pack sequences to a fixed length so the GPU is not padding.

**Quality and safety filters as pipeline stages.** Language identification, deduplication, toxicity and PII filters, and perplexity-based quality scoring all run as distributed stages, each with its own rejection log.

### How it connects to the rest of the framework

`TSC7-Advanced-A4` is the ability that uses all of this. `TSC7-Basic-K4` covers cleaning at small scale; `TSC7-Advanced-K7` produces synthetic volumes that must flow through this pipeline; `TSC7-Intermediate-A4` covers the ETL pattern for fine-tuning datasets. `TSC7-Advanced-K10` consumes the output.

### What is current as of November 2026

The interesting shift is that single-node tools got good enough for most teams. Polars and DuckDB now handle corpora that needed a cluster a few years ago, and GPU-accelerated dataframe engines have made filtering cheap. Cluster frameworks remain necessary for genuine multi-terabyte shuffles and for teams already standardised on Spark. Meanwhile the pre-training stacks behind the late-2026 frontier models — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and 4 Argon — all treat data pipelines as first-class engineering, with dataset versioning and reproducible mixtures, which is the practice worth copying at any scale.

### Common misconceptions

- *"Big data means I need a cluster."* Most "big data" problems are a bad format and a missing index.
- *"Deduplication is a `drop_duplicates()` call."* Exact duplicates are trivial; near-duplicates are the ones that hurt training.
- *"The job finished, so the data is right."* Silent partition loss and encoding errors both end in a green tick.
- *"More workers means faster."* Skew and shuffle cost can make more workers slower.

## How a student should understand it

**Mental model:** a banquet kitchen. One talented cook can serve a table; three hundred covers need stations, a pass, tickets and a rule for what happens when a burner dies.

**Three things they can do after this bullet:**
1. Choose between single-node and distributed processing with a reason.
2. Design a pipeline whose re-run is provably identical.
3. Measure skew and dedupe rate before trusting a corpus.

**Misconceptions to kill:** that scale requires a cluster, that dedupe is a one-liner, and that a completed job is a correct job.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The zi-char stall at dinner rush.** One wok cannot serve the queue; the fix is stations and a pass, not a bigger wok. And one table ordering a hundred bowls of the same noodle is skew — the station handling it becomes the bottleneck no matter how many other stations you add.

**The library stocktake.** You do not recount every shelf when one shelf is wrong; you count by shelf, record it, and reconcile. Checkpointing is counting by shelf.

### Worked example with a real tool

Have learners design before they execute:

```
We have 4 TB of scraped support documents: 30M JSON files,
average 130 KB, mixed English/Malay/Chinese, roughly 25% near-
duplicate after boilerplate removal.

Design the pipeline to produce a 40B-token training corpus:
1. Storage format and shard size, with a reason.
2. The stages, in order, and which ones need a shuffle.
3. How you deduplicate near-duplicates cheaply, and what you
   normalise first.
4. What you checkpoint, and how you prove a re-run is identical.
5. The one metric you put on a dashboard for the whole run.
```

What to point at afterwards: most first drafts put dedupe after tokenisation (expensive and irreversible) and skip normalisation entirely. The correction is to normalise and dedupe on text, keep the raw shards immutable, and tokenise last with a cache.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a pipeline bill showing a shuffle that cost more than the model training.
2. **State the objective** — design a deterministic, checkpointed, skew-aware pipeline.
3. **Recall prior learning** — Pandas cleaning from `TSC7-Basic-K4`.
4. **Present the content** — the four properties, formats, dedupe, filters, packing.
5. **Guide** — build the support-corpus design together.
6. **Elicit performance** — teams design for their own data volume.
7. **Give feedback** — peer review for idempotency and shuffle cost.
8. **Transfer** — each learner measures the cost per million documents for one job.

## What the framework doesn't mention but trainers need to know

- **Data versioning is the discipline that makes everything else repeatable.** Without immutable snapshots, no result is reproducible.
- **The rejection log is a deliverable.** What you filtered out, and why, is the audit trail for safety and quality claims.
- **PII removal must run before storage, not before training.** Corpora that sit around for months are the ones that leak.
- **Cost per token of cleaned data is a planning number.** It usually dominates fine-tuning cost.

## Watch out

- **Do not demo Spark on a laptop.** It teaches the wrong intuition and hides the shuffle cost that matters.
- **Do not present dedupe percentages as quality.** Removing duplicates is hygiene, not curation.
- **Do not skip the encoding discussion.** Mixed-language corpora with broken encodings produce garbage tokens that survive every other filter.
- **The stale claim to retire:** "we need a cluster." In 2026, fix the format and try Polars or DuckDB first.
