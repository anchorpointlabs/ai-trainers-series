---
id: 07.02.I.A5
tsc: 7
level: Intermediate
code: A5
title: Fine-tuning a pre-trained model without breaking what it knows
---

# Fine-tuning a pre-trained model without breaking what it knows

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A5**


> **Framework text (verbatim):** "Fine-tune pre-trained models for optimal performance."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 15 of 17

**One-line version:** Every fine-tune buys specialisation with general ability — "optimal" means the best trade you can defend, not the lowest training loss.

## What it is

The practical craft of adapting a pre-trained model to your task: deciding whether fine-tuning is the right move at all, shaping the dataset, choosing between adapters and full tuning, setting hyperparameters that suit the method, and gating the result so it ships only if it improved without collateral damage.

## Deep expansion

### The concept

A fine-tune shifts the model's output distribution toward your examples. Do that well and you get consistency, format compliance and cost reduction. Do it carelessly and you get a model that is excellent on your training distribution, brittle one step outside it, and quietly worse at everything else. Optimal performance is therefore a constrained optimisation: maximise task quality subject to no meaningful regression on general capability, format validity and safety behaviour.

### The sub-concepts

**Decide before you tune.** Prompt engineering with a few examples, plus retrieval if facts are involved, often reaches most of the way. Fine-tune when you need *consistency* (the same structure every time), *compression* (a small model replacing an expensive call), *latency*, or a behaviour the base model will not adopt from instructions alone.

**Data shape.** A few hundred to a few thousand well-formed pairs is often enough for style and format; new domain competence needs substantially more and is better served by continued pre-training. Diversity beats volume: vary length, phrasing, difficulty and edge cases, and include the awkward examples your reviewers complain about. One consistent template, applied at training and at inference, is worth more than another thousand rows.

**Method.** Parameter-efficient tuning — LoRA, QLoRA, DoRA — trains small adapters against a frozen base, tolerates learning rates roughly an order of magnitude higher than full fine-tuning, and lets several tasks share one base model. Full fine-tuning is for large domain gaps, unusual output formats or small base models. Rank is a capacity knob, not a quality dial: higher rank fits more, and more easily overfits a small set.

**Gates.** Four checks before shipping: the task metric on a held-out set, a general-capability regression test, format validity on a large sample, and a safety spot-check. Then fifty human readings, then a canary deployment with a rollback path.

### How it connects to the rest of the framework

`TSC7-Intermediate-K10` separates this from continued pre-training; `TSC7-Intermediate-K8` builds the dataset; `TSC7-Intermediate-K5` covers the optimiser settings; `TSC7-Intermediate-A1` is the broader custom-build ability; `TSC7-Intermediate-A3` provides the comparison that justifies the switch; `TSC6` is where the tuned model gets deployed and monitored.

### What is current as of November 2026

- **Adapters are the default.** QLoRA-class setups run on a single workstation GPU, and managing a library of adapters over one base model has become normal engineering.
- **Managed fine-tuning is available from the major providers.** Building on the GPT-6 generation, Claude 5.5 or Gemini 3.1 Pro no longer requires hosting weights, which shifts the question from "can we" to "is our data good enough".
- **A preference step usually follows SFT.** The DPO family and verifiable-reward RL are the expected second stage when tone and refusal behaviour matter.

### Common misconceptions

- *"Fine-tune to add facts."* It adds behaviour; facts belong in retrieval. A fine-tune on facts produces confident invention off-distribution.
- *"More epochs, better fit."* More epochs memorise phrasing and degrade general ability — the regression shows up on the general test, not the training loss.
- *"Higher rank is better."* Rank buys capacity to overfit as well as capacity to learn.
- *"Validation loss improved, so ship it."* Validation loss on your own distribution says nothing about the general regression you just caused.

## How a student should understand it

**Mental model:** sending an experienced employee on a specialist course. Three days and they handle your niche process well; send them for three months on nothing but that process and they forget how to run a meeting.

**Three things they can do after this bullet:**
1. Justify fine-tuning over prompting or retrieval, or the reverse.
2. Configure a LoRA run and explain each setting's effect.
3. Gate a release on task gain plus regression evidence.

**Misconceptions to kill:** that fine-tuning injects knowledge, that more training is better, and that a single metric clears a release.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The specialist course.** A good employee sent for a three-day course on your niche process comes back useful. Sent for three months on only that process, they return unable to handle anything else — that is catastrophic forgetting, and it is measurable. Where it breaks: the employee still has weekends and old habits; the model keeps only what the examples reinforced, and nothing brings back what the gradient overwrote.

**Seasoning a new wok.** A new carbon-steel wok needs oil and heat in layers. Season it once, properly, and it lasts; dump a bottle of oil in and you get a gummy pan that ruins everything you cook. Fine-tuning is layers, not volume. Where it breaks: a badly seasoned wok can be stripped and redone; an over-trained checkpoint often cannot be recovered by re-tuning, and you start again from the base.

### Worked example with a real tool

A learner wants their support replies to follow a fixed structure. Type this into a coding assistant:

```
Fine-tune with LoRA on ./pairs.jsonl (3,000 instruction/response pairs).

1. Config: r=16, alpha=32, dropout 0.05, target the attention and MLP
   projections, lr 1e-4 with 3% warmup and cosine decay, 2 epochs,
   bf16, effective batch 16 via accumulation, eval every 100 steps.
2. Use the model's chat template and mask loss on the prompt tokens.
3. After training, run three gates and print a table:
   (a) 200-case held-out task eval, (b) a 100-item general capability
   test scored before and after, (c) JSON-validity rate on 200 samples.
4. Save the adapter with its config, dataset hash and git sha.
```

Point at the general capability test in gate (b) — it is the one teams skip and the one that catches forgetting — and at the saved config with the dataset hash, without which a good adapter becomes unreproducible within a month.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a fine-tune that aced the task and lost its manners.
2. **State the objective** — run a gated fine-tune and defend the trade-off.
3. **Recall prior learning** — SFT versus CPT from K10, data prep from K8.
4. **Present the content** — decide, shape data, choose method, gate release.
5. **Guide** — set the LoRA config together and predict each effect.
6. **Elicit performance** — teams fine-tune on their own small set.
7. **Give feedback** — debrief the gate tables; find the regression.
8. **Transfer** — each learner writes the release checklist for their team.

## What the framework doesn't mention but trainers need to know

- **Iteration cost is dominated by labelling.** The regression set takes longer to build than the first fine-tune takes to run.
- **Adapters need versioning and an owner.** Two adapters with the same name and different data is a production incident waiting for a release.
- **Base-model upgrades invalidate adapters.** A new base version means retraining every adapter; plan for it in the roadmap.
- **Licence terms differ for tuning and redistribution.** A model you may fine-tune is not automatically a model you may ship as your own.

## Watch out

- **Do not teach learning rates as universal constants.** Give the reasoning — adapters tolerate higher rates because they update far fewer parameters — and let learners sweep.
- **Do not skip the regression gate.** It is the single practice that separates a professional fine-tune from a notebook experiment.
- **Do not fine-tune on everything you have.** A curated thousand beats a scraped hundred thousand, and the difference shows in the tails.
- **The stale claim to retire:** "fine-tune it and it will know our business." In November 2026 it will *sound* like your business and still invent your prices.
