---
id: 07.02.I.K5
tsc: 7
level: Intermediate
code: K5
title: Optimisation strategies: the knobs between a model that runs and one worth using
---

# Optimisation strategies: the knobs between a model that runs and one worth using

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K5**


> **Framework text (verbatim):** "Optimisation strategies for achieving higher-quality outputs."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 5 of 17

**One-line version:** Anyone can make loss go down; the craft is knowing which knobs buy quality and which only buy a nicer curve.

## What it is

"Optimisation" covers two different jobs that learners merge. One is numerical: the optimiser, learning-rate schedule, batch size, precision and clipping that decide whether training converges at all. The other is about output quality: data curation, guidance, sampling settings, rejection sampling and the post-training step. The first is compulsory. The second is where the difference between a usable model and a technically finished one lives.

## Deep expansion

### The concept

Gradient descent only promises to reduce the loss you gave it. Whether that loss corresponds to good output is a separate question answered by data and evaluation. So optimisation strategy splits cleanly: *get the run to converge stably*, then *spend the remaining effort on quality*. Teams that skip the first waste GPU hours; teams that skip the second ship a model whose validation loss is excellent and whose samples are dull.

### The sub-concepts

**The optimiser and its schedule.** AdamW with decoupled weight decay is the default; the schedule — linear warmup, then cosine decay or a warmup-stable-decay shape — matters more than the optimiser choice. Gradient clipping at a modest norm prevents the single bad batch that destroys a run. Gradient accumulation buys effective batch size when memory does not. bf16 autocast is standard; it has enough exponent range that loss scaling is rarely needed.

**Batch size and stability.** Larger batches give lower-variance gradients, which permits a higher learning rate and better hardware utilisation — but past a point the extra compute buys fewer updates per epoch and convergence per token drops. Batch size, learning rate and warmup are one decision, not three.

**Sampling-time quality.** The cheapest quality available: temperature and top-p for language, classifier-free guidance scale and step count for diffusion, and *best-of-n* — generate several candidates, score them with a verifier or judge, keep the best. Rejection sampling costs inference money instead of training money and often beats a week of tuning.

**Post-training quality.** Supervised fine-tuning on a small, clean, deduplicated set; then a preference step to shape behaviour (tone, refusal, verbosity). Both are sensitive to data quality far more than to hyperparameters, and the preference step has a characteristic failure: push the margin hard enough and the model becomes flattering and long-winded.

### How it connects to the rest of the framework

`TSC7-Basic-K7` is the entry-level version of the numerical half; `TSC7-Intermediate-K8` is the data work that dominates the quality half; `TSC7-Intermediate-K4` supplies the metrics that tell you whether a knob helped; `TSC7-Intermediate-K10` is the fine-tuning sequence these strategies apply to; `TSC5` is the evaluation discipline that keeps you honest.

### What is current as of November 2026

- **Quality now comes from data and post-training, not architecture.** The frontier model families — GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — differentiate on curation, post-training recipe and inference-time budget rather than on novel optimisers.
- **Test-time compute became a first-class knob.** Best-of-n with a verifier, and longer reasoning before answering, are now routine ways to buy quality at inference, which changes the usual "tune the training job" instinct.
- **Few-step sampling matured.** Distilled samplers mean the step count for image generation is a cost decision you can now make aggressively.

### Common misconceptions

- *"Higher learning rate converges faster."* It converges faster until it diverges, and the run that diverged looked fine for the first thousand steps.
- *"Bigger batch is always better."* It is better for throughput, not automatically for sample efficiency, and it demands a matching learning rate.
- *"Higher temperature means more creative."* It means more random. Creativity that survives evaluation usually comes from better data and better instructions.
- *"More denoising steps, better images."* Past a threshold you pay more for less, and over-guidance can make extra steps actively worse.

## How a student should understand it

**Mental model:** the wok. Same ingredients, same recipe — the difference between good char kway teow and a soggy plate is heat control and timing, not a secret ingredient. Optimisation is heat control; the ingredients are data.

**Three things they can do after this bullet:**
1. Set up a stable training run — warmup, schedule, clipping, precision — and explain each choice.
2. Run a small sweep and interpret variance instead of chasing the best single run.
3. Buy quality at sampling time when it is cheaper than retraining.

**Misconceptions to kill:** that faster convergence is better, that batch size is free, and that hyperparameters substitute for clean data.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Manual driving in city traffic.** Gear, RPM and clutch are interdependent: change one and the others must follow. Learning rate, batch size and warmup behave the same way — a learner who tunes one in isolation stalls the car. Where it breaks: a car stalls visibly; a training run with a bad learning rate can look healthy for hours.

**Wok hei.** The smoky flavour comes from heat applied at the right moment, not from cooking longer. Extra epochs are longer cooking: they dry the dish out. Where it breaks: a cook tastes and stops; a training run gives no taste until you evaluate, so "a bit longer" continues by default.

### Worked example with a real tool

A learner's fine-tune is unstable — loss spikes every few hundred steps. Type this into a coding assistant:

```
My LoRA fine-tune spikes around step 600 (log attached, lr 3e-4,
batch 4, no warmup, no clipping). Write a sweep script that:

1. Runs four configurations: lr {1e-4, 3e-4} x warmup {0, 100 steps},
   everything else identical, fixed seeds, 1,500 steps each.
2. Applies gradient clipping at norm 1.0 in all four.
3. Logs train loss, validation loss, gradient norm and tokens/sec
   to W&B with the config as tags.
4. Prints a table of best validation loss and the step it occurred,
   plus the spread across seeds.
```

Point at the gradient-norm curve (spikes precede loss spikes — that is your early warning), the fixed seeds (a single run is an anecdote), and the spread column — if the differences are inside seed variance, the sweep proved nothing and the answer is data, not knobs.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two runs, same data, one converged and one wrecked by learning rate.
2. **State the objective** — configure a stable run and justify each setting.
3. **Recall prior learning** — gradients, epochs and loss from the Basic level.
4. **Present the content** — optimiser, schedule, batch, sampling, post-training.
5. **Guide** — diagnose a spike together from the gradient-norm plot.
6. **Elicit performance** — teams run two configurations and compare honestly.
7. **Give feedback** — debrief; insist on the seed-variance caveat.
8. **Transfer** — each learner writes the stability checklist into their project.

## What the framework doesn't mention but trainers need to know

- **Sweeps are expensive and mostly low-yield.** For fine-tuning, a small honest sweep over learning rate and warmup beats a large grid; the rest is data work.
- **The last few points of quality come from curation.** Deduplicating and filtering the training set outperforms another hundred steps almost every time.
- **Evaluation during training prevents wasted runs.** A validation metric every few hundred steps catches divergence, overfitting and formatting collapse before you spend the night on it.
- **Determinism is fragile.** cuDNN kernels, data-loader workers and distributed reductions all introduce variance; report ranges, not best runs.

## Watch out

- **Do not teach "tune until the metric improves".** Without a held-out set that never enters the loop, tuning is memorisation with extra steps.
- **Do not present a single best run as a result.** It is a lucky draw; the class will copy the number.
- **Do not confuse bigger models with better outputs.** In November 2026 a well-tuned small model with clean data routinely beats a badly tuned large one.
- **The stale claim to retire:** "more epochs, better model." Beyond the point where validation loss turns, more epochs is a longer lesson in the training set's quirks.
