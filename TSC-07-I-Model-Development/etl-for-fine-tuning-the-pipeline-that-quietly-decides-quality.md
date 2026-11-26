---
id: 07.02.I.A4
tsc: 7
level: Intermediate
code: A4
title: ETL for fine-tuning: the pipeline that quietly decides quality
as_at: 2026-11-26
review_by: 2027-02-25
---

# ETL for fine-tuning: the pipeline that quietly decides quality

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A4**


> **Framework text (verbatim):** "Develop data pipelines (e.g. extract transform load) to create fine tuning datasets."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 14 of 17

**One-line version:** A fine-tuning dataset is a build artefact — if you cannot rebuild it exactly, you cannot explain your model's score.

## What it is

A data pipeline that extracts raw records from source systems, transforms them into training format, and loads them into a versioned dataset store, with validation at every step. The output is not a file somebody made once; it is a reproducible artefact with a manifest, a schema and a lineage trail.

## Deep expansion

### The concept

The pipeline is a contract. A given source snapshot, transformation code and configuration should produce the same dataset — same rows, same order-independent hash, same split assignment. That reproducibility is what makes a training result attributable: without it, a re-run with "the same" data that scores differently leaves you unable to tell whether you changed the code, the data, or the world. Most quality regressions at this level are not model regressions; they are pipeline changes nobody recorded.

### The sub-concepts

**Extract.** Know each source's quirks: CRM exports carry test records and internal notes, ticket systems carry attachments, call transcripts arrive with ASR errors, PDFs need parsing that silently drops tables. Snapshot raw inputs before transformation so a bad step can be debugged against the original. Record consent and PII flags at extraction, not later.

**Transform.** Parse, normalise, deduplicate, filter, redact personal data, and format into the model's chat template with loss masked on the prompt. Split by entity — customer, thread, document — never by row. Every step should be idempotent and should log how many rows it removed and why, because silent row loss is the most common invisible bug.

**Load and version.** Store as parquet or through a dataset library, pin the version by hash, and write a manifest: row counts per split, source snapshot IDs, transformation commit, filter statistics. A short datasheet alongside it — where the data came from, what was removed, known gaps — turns a folder into something an auditor will accept.

**Orchestration.** Airflow, Dagster or Prefect if the team already runs one; a Makefile plus Python if not. Either way: a schema check on load, assertions on row counts and label distribution, and an alert when a run produces a suspiciously different dataset.

### How it connects to the rest of the framework

`TSC7-Intermediate-K8` is the data craft the pipeline encodes; `TSC7-Intermediate-A6` covers the transformation techniques in depth; `TSC7-Intermediate-A7` is the checkpoint-based pipeline that reuses the same infrastructure; `TSC7-Advanced-K8` and `TSC7-Advanced-A4` scale it to distributed frameworks; `TSC6` is where the same discipline appears on the application side.

### What is current as of November 2026

- **Dataset versioning became ordinary.** Training-data revision pinning is standard in teams that ship, and lakehouse formats are common for the larger sets.
- **Pipelines now contain generation stages.** Synthetic augmentation from a strong model sits as a step with its own validation, which means the pipeline must record model and prompt versions too.
- **Data contracts are being asked for.** Upstream teams increasingly publish schema and quality guarantees, because downstream training breaks silently when an export column changes meaning.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"ETL is a one-off script."* A script that ran once is an artefact; a pipeline is something that runs next month without you.
- *"More transformation steps means better data."* Each step is a chance to lose rows silently; the count reconciliation matters more than the step count.
- *"The pipeline is done when it runs."* It is done when it validates, fails loudly, and can be rebuilt from a manifest.
- *"Splitting is a formality."* Splitting by row rather than entity leaks the same customer into train and test and inflates every metric you report.

## How a student should understand it

**Mental model:** the supply chain that gets fish from Jurong Fishery Port to the stall by four in the morning. Sourcing, icing, cutting, delivery, and a chit at every handover. One broken link and the stall opens with nothing to sell.

**Three things they can do after this bullet:**
1. Write a pipeline that fails loudly when an input schema changes.
2. Produce a manifest that lets someone else rebuild the exact dataset.
3. Reconcile row counts across every stage and explain the losses.

**Misconceptions to kill:** that a notebook is a pipeline, that silent row loss is acceptable, and that splitting is housekeeping.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The fishery port supply chain.** The stall's fish passes through auction, ice, transport and cutting. Each handover has a chit; if the morning delivery is short, somebody can trace which link lost it. A fine-tuning dataset without a manifest is a stall that cannot tell whether the fish was short or the ice melted. Where it breaks: the port keeps a chit at every handover; most teams log only the stages that failed, so the missing rows stay unexplained.

**The banquet kitchen's prep sheet.** A banquet for 300 does not run on memory; it runs on a prep sheet with quantities, timings and a checking step. Scale changes the discipline, not the cooking. Where it breaks: a banquet kitchen tastes as it scales; a pipeline that scales a hundredfold cannot taste every row, so the checks must be sampled and automated.

### Worked example with a real tool

A learner rebuilds the dataset by hand every month. Type this into a coding assistant:

```
Write a pipeline (plain Python + Makefile, no orchestrator) that:

1. extract: pull tickets and agent replies from export/tickets_*.csv,
   snapshot raw files to data/raw/<date>/ unmodified.
2. transform: drop internal notes, redact emails/phone/NRIC patterns,
   near-dedup at 0.9, split by customer_id, format chat JSONL.
3. load: write parquet to data/processed/<version>/ with a manifest.json
   containing source file hashes, row counts per stage, params, git sha.
4. assertions: fail the run if any split is empty, if label balance
   drifts more than 5% from the previous run, or if rows removed
   by any stage exceed 30% without a --force flag.
5. print a summary table of rows in/out per stage.
```

Point at the 30% guard — it is what catches a parser that broke silently — and the manifest's git sha plus source hashes, which is what lets you say "this exact dataset produced this exact score".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a model whose score dropped because an export column changed.
2. **State the objective** — build a pipeline that fails loudly and rebuilds exactly.
3. **Recall prior learning** — cleaning, dedup and splitting from K8.
4. **Present the content** — extract, transform, load, orchestrate, validate.
5. **Guide** — add one assertion to an existing script together.
6. **Elicit performance** — teams write the stage list and assertions for their own data.
7. **Give feedback** — debrief: which failure would slip through the current checks?
8. **Transfer** — each learner versioned their dataset once, this week.

## What the framework doesn't mention but trainers need to know

- **Consent and PII belong in extract, not in a later clean-up.** What never enters the pipeline cannot leak from it.
- **Re-run cost is a design constraint.** A pipeline that takes nine hours to rebuild will not be re-run when someone suspects a bug.
- **Drift is inevitable.** Source systems change; the pipeline needs a distribution check, not just a schema check.
- **Ownership must be named.** A pipeline without an owner rots within two quarters and nobody notices until a model fails an audit.

## Watch out

- **Do not demo a notebook and call it a pipeline.** It teaches the wrong artefact and the room copies it.
- **Do not skip the row reconciliation.** Silent losses are the failure learners never see in a demo.
- **Do not over-engineer the orchestrator.** A Makefile beats a half-configured Airflow install for a two-person team.
- **The stale claim to retire:** "we'll just rebuild it manually." In November 2026 the manifest is the deliverable, and manual rebuilds are how models become unexplainable.
