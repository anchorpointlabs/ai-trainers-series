---
id: 07.02.I.A7
tsc: 7
level: Intermediate
code: A7
title: Continuing pre-training from a checkpoint: the pipeline and its traps
as_at: 2026-11-26
review_by: 2027-02-25
---

# Continuing pre-training from a checkpoint: the pipeline and its traps

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A7**


> **Framework text (verbatim):** "Develop training pipeline to continue pre-training from an existing model checkpoint."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 17 of 17

**One-line version:** Most of a continued pre-training pipeline is checkpoint plumbing and data scale discipline; the training loop is the smallest part.

## What it is

The engineering that takes a public checkpoint and runs further unsupervised next-token training on a domain corpus: acquiring and converting the weights, preparing a corpus at scale, configuring a stable low-learning-rate run with replay, checkpointing and evaluating, and handing the result to supervised fine-tuning. This is the ability version of the concept in K10 — the sequence, not the theory.

## Deep expansion

### The concept

Continuing pre-training inherits everything: the architecture, the tokeniser, the licence and the behaviour of the base model. That inheritance is the point — you are not building a model, you are extending one — and it is also the trap, because nothing in the pipeline forces you to notice that you have damaged what you inherited. So the pipeline is built around two invariants: *the corpus is reproducible* and *the capability regression is measured*, at every checkpoint, not at the end.

### The sub-concepts

**Checkpoint acquisition and sharding.** You need weights, tokeniser and config together; a mismatch here produces fluent-looking garbage. Convert between formats — Hugging Face, FSDP, Megatron-style — and reshard to your topology, which is a real cost before training starts. Verify with a forward pass on a known prompt and compare against the original model's output before spending a GPU-hour. Check the licence: permission to use weights is not permission to redistribute derivatives.

**Corpus preparation at scale.** Deduplicate at corpus scale rather than at file scale; filter for quality and language; mark document boundaries so the model does not learn that one policy ends by starting another; pack sequences to a fixed length to avoid padding waste; and shuffle across shards so data order does not encode source order. If the domain uses a new script or notation, extend the tokeniser and resize the embedding matrix — a separate operation with its own evaluation.

**Training configuration.** A low learning rate with a long warmup, a replay mixture of general data in every batch, gradient checkpointing to fit memory, FSDP or ZeRO for sharding, checkpoints on a rotation with tested resume, and evaluation hooks that report domain perplexity by slice alongside a general capability test.

**Handover.** The output is a checkpoint plus a record: tokens seen, mixture ratios, source snapshot, commit hash. Supervised fine-tuning then starts from it, and the regression test travels with it.

### How it connects to the rest of the framework

`TSC7-Intermediate-K10` is the concept this operationalises; `TSC7-Intermediate-A4` is the pipeline discipline being reused; `TSC7-Intermediate-K8` is the data craft; `TSC7-Intermediate-A2` is the monitoring that keeps the run alive; `TSC7-Intermediate-A5` is the SFT stage that follows; `TSC7-Advanced-K10` goes deeper into advanced and continuous pre-training techniques.

### What is current as of November 2026

- **Mid-training is a named stage.** Recipes behind the GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro / Gemini 4 Argon describe a middle stage that is neither pre-training nor fine-tuning, and in-house teams now copy the shape.
- **Long-context extension happens here.** Extending context length is a continued pre-training job with its own curriculum, not a config flag.
- **Sharded training is default tooling.** FSDP and ZeRO-class setups are ordinary, and safetensors formats have made checkpoint handling less fragile than it was.

### Common misconceptions

- *"Continued pre-training is fine-tuning with more data."* It is unlabelled, document-level, and its risk is forgetting rather than overfitting.
- *"Point the trainer at our PDFs."* Without packing, boundary markers, deduplication and replay, that produces a model that writes like a badly concatenated manual.
- *"Resume means restart."* Resuming restores optimiser state and data position; a restart with the same config is a different run.
- *"Its loss is comparable to the base model's pre-training loss."* Different data and different distribution — the number is only meaningful against your own baseline.

## How a student should understand it

**Mental model:** renovating an HDB flat. You inherit the pipes, wiring and structure; the work is extending and adapting them. Nobody renovating a flat rebuilds the block — and nobody expects the neighbours to be unaffected if you cut a structural wall.

**Three things they can do after this bullet:**
1. Take a public checkpoint to a running, resumable training job.
2. Build a corpus with boundaries, packing and a replay mixture.
3. Prove that the result did not lose general capability.

**Misconceptions to kill:** that this is a bigger fine-tune, that the corpus needs no engineering, and that a lower training loss means success.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Teaching a fluent reader a specialist register.** A graduate who already reads English well is given years of court judgments to read, not a grammar textbook. They become fluent in the register — and if that is all they read for a year, they start writing like a judgment even in a text message. The replay mixture is the weekly newspaper that keeps them conversational. Where it breaks: the reader can put the judgments down; a model trained on them carries the register into everything it writes, which is why the replay mixture is not optional.

**Renovating versus rebuilding.** You inherit the pipes and wiring, so the work is extension rather than construction — cheap and fast, and the old plumbing is now your problem. Where it breaks: remove one wall to improve the layout and the whole block's structure is affected, which is what a high learning rate does to the model's existing ability.

### Worked example with a real tool

A learner has a 60 GB legal corpus and wants a legal-register model. Type this into a coding assistant:

```
Build a continued pre-training pipeline on an open-weight checkpoint:

1. Prepare corpus: dedupe at document level, filter by language ID,
   insert an end-of-document token, pack to 8,192 tokens, shuffle
   across shards, and write a manifest with token counts.
2. Mixture: 90% legal, 10% general web text, sampled per batch.
3. Train with FSDP across available GPUs, lr 1e-5, 500-step warmup,
   cosine decay, bf16, gradient checkpointing, checkpoint every
   500 steps with rotation and a resume test in CI.
4. Eval hooks every 1,000 steps: domain perplexity on a held-out
   legal slice, plus a 100-item general capability test; log both
   to the same dashboard.
5. Emit a handover card: tokens seen, mixture, base checkpoint,
   eval table before and after.
```

Point at step 1's manifest — tokens seen, not file sizes, is the unit of progress — step 3's resume test in CI, and step 4: without the general capability line on the same chart, nobody notices the forgetting until users do.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a model that writes beautiful judgments and cannot hold a conversation.
2. **State the objective** — stand up a resumable run with a measured regression.
3. **Recall prior learning** — SFT versus CPT from K10, pipelines from A4.
4. **Present the content** — checkpoint handling, corpus prep, config, handover.
5. **Guide** — walk a sample document from raw text to packed tokens.
6. **Elicit performance** — teams write the pipeline stages and eval hooks.
7. **Give feedback** — debrief: where would forgetting hide in this design?
8. **Transfer** — each learner estimates cost for their own corpus size.

## What the framework doesn't mention but trainers need to know

- **Cost scales with tokens, not documents.** A tidy-looking 10 GB corpus can be hundreds of millions of tokens; estimate before you commit the budget.
- **Checkpoint handling is where runs break.** Format conversion, sharding and resume are the fragile parts, not the optimiser.
- **Contamination cuts both ways.** Benchmark text inside a domain corpus inflates every later evaluation and is very hard to remove afterwards.
- **The handover card is the deliverable.** A checkpoint without its mixture and token count cannot be defended or reproduced.

## Watch out

- **Do not undersell the cost.** Continued pre-training on a domain corpus is measured in GPU-days even at small scale.
- **Do not skip the replay mixture.** It is the cheapest insurance against a model that forgets how to be useful.
- **Do not claim competitive results from CPT alone.** It shifts register; benchmark parity claims need the full post-training recipe.
- **The stale claim to retire:** "we'll continue pre-training on our documents and it will know them." In November 2026 it will *sound* like them, and still need retrieval to be right.
