---
id: 07.03.A.K6
tsc: 7
level: Advanced
code: K6
title: Compute efficiency: how a model gets smaller without getting dumber
as_at: 2026-11-26
review_by: 2027-02-25
---

# Compute efficiency: how a model gets smaller without getting dumber

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K6**


> **Framework text (verbatim):** "Concepts of compute efficiency, (e.g., quantisation and similar efficiency techniques)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 6 of 20

**One-line version:** Efficiency work buys the same output for less money, and it always costs something — the craft is knowing which cost your task can absorb, and measuring it rather than assuming it.

## What it is

Compute efficiency is the family of techniques that reduce the memory, latency or cost of training and running a generative model without retraining it from scratch: quantisation, distillation, pruning, mixture-of-experts routing, KV-cache optimisation, speculative decoding and better batching. Each trades something — accuracy on the tail, engineering complexity, throughput at low load — for a resource you are short of.

## Deep expansion

### The concept

Inference economics are dominated by two numbers: how many bytes must be read to produce a token, and how many tokens must be produced. A decoder-only model generating text re-reads its weights for every token, so it is memory-bandwidth bound, not arithmetic bound. That single fact explains why quantisation — storing weights in fewer bits — gives near-linear speedups at small batch, and why batching improves throughput but not latency.

Quantisation comes in two flavours. **Post-training quantisation** converts weights (and optionally activations) after training, with a small calibration set to choose scaling factors; it is cheap and works well down to 8-bit, usually acceptable at 4-bit. **Quantisation-aware training** simulates the rounding during training so the model adapts; it costs a training run and buys accuracy where post-training quantisation breaks.

### The sub-concepts

**Precision as a dial.** fp32 → bf16 → fp8 → int8 → 4-bit is a ladder of memory savings. Each rung needs an accuracy test on *your* task, because degradation concentrates on long-tail knowledge, arithmetic, structured output and non-English text — exactly the places a generic benchmark will not catch.

**Distillation.** A smaller student model is trained to match a larger teacher's outputs, often on soft distributions rather than hard labels. It is the only technique here that reduces the model itself rather than its storage, and it requires data and a training run.

**KV cache and attention efficiency.** Grouped-query attention, paged cache allocation and IO-aware attention kernels reduce the memory that grows with context. For long-context serving this matters more than weight precision.

**Speculative decoding and routing.** A small draft model proposes tokens that the large model verifies in one pass; a router sends easy queries to a cheap model and hard ones to an expensive one. Both improve cost per token without changing the model's knowledge.

**Sparsity and mixture-of-experts.** Only a fraction of parameters activate per token. Great for capacity per unit of compute, harder to serve because memory must hold all experts while compute uses few.

### How it connects to the rest of the framework

`TSC7-Advanced-K3` (hardware libraries) is whether these techniques have fast kernels on your accelerator. `TSC6-Advanced-K1` states the same bullet from the application side; `TSC5-Intermediate-K4` is the evaluation discipline you must apply after every efficiency change. `TSC7-Advanced-A3` is efficiency under a production deadline.

### What is current as of November 2026

Efficiency has become the main competitive axis rather than a cost-saving afterthought. Serving stacks now treat 8-bit and 4-bit weights, paged KV caches and speculative decoding as defaults, and the late-2026 frontier releases — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and 4 Argon — compete as much on price per useful token and latency as on capability. On the open-weight side, a small model fine-tuned on your domain and quantised for your hardware routinely beats a large general model on cost at equal quality for narrow tasks.

### Common misconceptions

- *"Quantising to 4-bit is free."* It is free on benchmarks and not free on your tail cases. Test before and after on data you care about.
- *"Smaller models are always cheaper."* A small model that needs three retries per acceptable answer can cost more than one call to a large model.
- *"Distillation is just training a small model."* It is matching a teacher's behaviour; without the teacher's outputs the student has no advantage.
- *"Batching makes responses faster."* It raises throughput and usually worsens per-request latency.

## How a student should understand it

**Mental model:** shrink-wrapping luggage. You can compress a lot before anything breaks, but the fragile items are the ones you notice at the destination.

**Three things they can do after this bullet:**
1. Choose a precision level and design the before/after evaluation that justifies it.
2. Explain the difference between latency, throughput and cost per acceptable output.
3. Say which efficiency technique applies to a given bottleneck.

**Misconceptions to kill:** that quantisation is lossless, that smaller is cheaper, and that a throughput win is a user-experience win.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker's chilli.** Same recipe, less chilli — most customers cannot tell, and the ones who can are your regulars. Where it breaks: with models, the "regulars" are your edge cases and they are usually the ones that matter commercially.

**MP3 versus WAV.** Aggressive compression is inaudible on pop and obvious on a cymbal. Model quantisation behaves the same way: fine on chat, audible on arithmetic and rare scripts.

### Worked example with a real tool

Run the comparison rather than argue about it:

```
I have a 7B instruction-tuned model serving an internal HR policy
assistant. Traffic: ~2k queries/day, mostly short questions,
some long policy comparisons. Currently fp16 on one GPU.

Propose a plan to cut cost, in this order:
1. Which two techniques to try first, and why those two.
2. The exact evaluation I must run before and after, including
   what to hold out so I do not fool myself.
3. The failure signature that would tell me to revert.
4. The metric I report to finance (not GPU utilisation).
```

Then do it with a real stack: serve the same model at `Q4_K_M` and at `Q8_0` in llama.cpp or Ollama, and run the assistant's own twenty hardest questions through both. What to point at: the answers are usually identical on the easy ones and diverge on the ones containing numbers or clause references — which is precisely the risk.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — same question answered by two model sizes with a cost per thousand queries on screen.
2. **State the objective** — pick a precision level, defend it with an evaluation.
3. **Recall prior learning** — memory bandwidth from `TSC7-Advanced-K3`.
4. **Present the content** — the efficiency ladder, latency versus throughput, distillation, routing.
5. **Guide** — work the HR assistant plan together.
6. **Elicit performance** — teams run the before/after comparison on a small local model.
7. **Give feedback** — debrief where quality diverged and whether it mattered.
8. **Transfer** — each learner computes cost per acceptable answer for one workload they own.

## What the framework doesn't mention but trainers need to know

- **Cost per *acceptable* answer is the only metric finance understands.** Include the retry rate.
- **Tail degradation is invisible to benchmarks.** Build a small adversarial set of twenty cases and keep it forever.
- **Serving architecture beats model choice more often than people expect.** Caching, routing and batching usually beat swapping models.
- **Every efficiency change needs a rollback path.** Quantised models fail differently, and the failure looks like a content bug, not an ops bug.

## Watch out

- **Do not demo speed without a quality check in the same breath.** It teaches the wrong habit.
- **Do not quote bits-per-weight as a guarantee.** Kernels, hardware and sequence length all change the result.
- **Do not present distillation as compression.** It needs data, a training run and its own evaluation.
- **The stale claim to retire:** "wait for cheaper hardware." In 2026 the savings come from the stack you build, not the chip you buy.
