---
id: 07.01.B.K7
tsc: 7
level: Basic
code: K7
title: "Optimisation: the learning rate, the batch and the knobs that decide a run"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Optimisation: the learning rate, the batch and the knobs that decide a run

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K7**


> **Framework text (verbatim):** "Optimisation techniques for training neural networks."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 7 of 15

**One-line version:** Optimisation is how the model walks downhill on the loss, and the learning rate is the size of each step — almost every failed training run is a walk problem, not a model problem.

## What it is

Optimisation is the procedure that adjusts the model's weights to reduce the loss. The core is gradient descent: compute which direction increases the error, then move the opposite way. Everything else — momentum, Adam, weight decay, warm-up, schedules, gradient clipping, mixed precision — exists to make that walk faster, steadier or cheaper. At Basic level the goal is to recognise the handful of settings that decide whether a run converges, and to know what each failure looks like.

## Deep expansion

### The concept

Picture a landscape where height is the loss and position is the set of weights. The gradient tells you which way is uphill at the point you are standing. You step downhill. Repeat a few hundred thousand times.

Two things make this harder than it sounds. First, the landscape is not a bowl — it has ravines, plateaus and saddle points, and a naive step can bounce from wall to wall. Second, each step is expensive: you must run the whole model forward and backward over a batch of data before you can take it. So every optimisation technique is really an answer to one of two questions: *which direction, and how big a step?*

**SGD with momentum** averages recent gradients so the walk keeps moving through small bumps and does not stall in a shallow dip. **Adam** (and its corrected cousin **AdamW**) additionally scales each weight's step by how noisy its gradient has been, which is why it is the default for transformers — it works without much tuning. **AdamW** decouples weight decay from the update, which is a subtlety that matters more than it sounds.

### The sub-concepts

**Learning rate.** The single most consequential setting. Too high and the loss spikes or diverges; too low and the run crawls or parks in a bad region. Typical fine-tuning values are far smaller than pre-training values.

**Warm-up and schedules.** Start with a small learning rate, rise over a few hundred steps, then decay — often following a cosine curve. Warm-up exists because early gradients are wild and a full-size step at step one can wreck the weights.

**Batch size.** How many examples contribute to one step. Larger batches give smoother gradients and better hardware utilisation; smaller batches give noisier steps but more updates per epoch. Global batch size is the total across all devices, not the per-device number.

**Weight decay.** A small pull toward zero on every weight, which discourages the model from relying on any single extreme value. Regularisation, not optimisation, but it is set alongside the learning rate.

**Gradient clipping.** Cap the gradient's magnitude so one freak batch cannot blow up the run. Standard in fine-tuning, invisible when it works.

**Mixed precision.** Run most arithmetic in a lower-precision format to halve memory and speed up training. Nearly free accuracy-wise for most work, and the reason a fine-tune fits on one consumer GPU.

**Early stopping.** Stop when validation loss stops improving. The cheapest regulariser available.

### How it connects to the rest of the framework

`TSC7-Basic-K6` is the number being minimised; this bullet is how. `TSC7-Basic-K1`'s three families need different optimisers and different stability tricks. `TSC7-Basic-K10` (parallel training) multiplies the effective batch, which changes the learning rate you need. `TSC7-Basic-A4` (training on a benchmark) is where these settings first bite. `TSC7-Intermediate-K5` (optimisation for output quality) is the next level, where schedule shape and data mixture start to matter.

### What is current as of November 2026

The defaults have hardened. For supervised fine-tuning of open-weight models, the standard recipe is AdamW, a small learning rate, a short warm-up, cosine decay, gradient clipping at 1.0, and bf16 mixed precision. Tooling — TRL, Axolotl, Unsloth — ships sensible defaults, which is a mixed blessing: learners get working runs without understanding them, then cannot diagnose the run that fails.

Two genuine shifts. First, **bf16 has largely displaced fp16** on modern accelerators because it does not need loss scaling, removing a whole class of beginner bug. Second, **the interesting optimisation problem moved to post-training**: preference-based methods that align a model to human judgements have their own optimisation behaviour, and the frontier labs' advantage increasingly sits there rather than in the pre-training loop.

### Common misconceptions

- *"Adam is better than SGD."* Adam is more forgiving by default. Well-tuned SGD with momentum still matches or beats it on many vision tasks.
- *"A lower learning rate is always safer."* Too low and the model barely moves; you get a run that looks stable and learns nothing.
- *"Bigger batch is always better."* It changes the optimisation dynamics and often needs a higher learning rate to compensate.
- *"If the loss spikes, the data is bad."* Usually the learning rate is too high or warm-up is too short.
- *"Training loss not moving means a broken model."* Often it means a frozen backbone, a zero learning rate, or labels misaligned.

## How a student should understand it

**Mental model:** walking downhill in thick fog. You can feel the slope under your feet but cannot see the valley. The learning rate is your stride. Too long and you overshoot into the next ravine; too short and you are still on the ridge at nightfall.

**Three things they can do after this bullet:**
1. Read a loss curve and name the likely cause: spike, plateau, slow crawl or overfit.
2. Set a defensible starting configuration for a fine-tune: optimiser, learning rate, warm-up, batch, clipping, precision.
3. Explain why the learning rate for fine-tuning is much smaller than for pre-training.

**Misconceptions to kill:** that the optimiser is a detail, that lower learning rate is safer, and that a spike means bad data.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The gas pedal on a manual car.** Learning rate is how hard you press. Too hard at the start and you stall or lurch; too gentle and you never leave the car park. Warm-up is releasing the clutch gradually rather than dumping it.

**Tuning an old radio.** You turn the dial in steps. Big steps find the station fast and miss it entirely; small steps find it eventually. A schedule is starting with big steps and finishing with small ones, which is exactly what "cosine decay" does.

### Worked example with a real tool

In Colab, run the same tiny fine-tune twice with two learning rates and plot both losses. The code is the standard `Trainer` path:

```python
from transformers import (AutoModelForCausalLM, AutoTokenizer,
                          TrainingArguments, Trainer)
from datasets import load_dataset

tok = AutoTokenizer.from_pretrained("gpt2"); tok.pad_token = tok.eos_token
model = AutoModelForCausalLM.from_pretrained("gpt2")
ds = load_dataset("yelp_review_full", split="train[:200]")
ds = ds.map(lambda b: tok(b["text"], truncation=True, max_length=128,
                          padding="max_length"), batched=True)

args = TrainingArguments(
    output_dir="out", per_device_train_batch_size=4, max_steps=60,
    learning_rate=5e-4, lr_scheduler_type="cosine", warmup_steps=10,
    max_grad_norm=1.0, bf16=True, logging_steps=5, report_to="none")
Trainer(model=model, args=args, train_dataset=ds).train()
```

What to point at afterwards: the logged loss at steps 5, 10 and 60. Rerun with `learning_rate=5e-2` and watch it jump or go to `nan`. That contrast — one number, two completely different runs — is the whole bullet.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two loss curves, one smooth and one spiking, and ask which model is better. Nobody can tell, which is the point.
2. **State the objective** — by the end you can set a sane optimiser configuration and diagnose a bad curve.
3. **Recall prior learning** — from K6 they know the loss; now they move it.
4. **Present the content** — gradient descent, momentum, AdamW, learning rate, warm-up, batch, clipping.
5. **Guide** — run the snippet, then change one setting and predict the effect before rerunning.
6. **Elicit performance** — pairs diagnose three printed loss curves and write the first fix for each.
7. **Give feedback** — correct "spike = bad data" and "plateau = broken model" using the pairs' own evidence.
8. **Transfer** — each learner writes the training configuration they would try first on their own data, with one sentence of justification.

## What the framework doesn't mention but trainers need to know

- **One variable at a time.** Learners change five settings, the run improves, and they learn nothing. Insist on single-variable experiments even when they are slow.
- **Defaults are opinions.** A tool's default learning rate was chosen for someone else's dataset. It is a starting point, not a recommendation for your data.
- **Reproducibility is a settings problem.** Seed, precision, batch order and library version all affect results. Log them or you cannot defend a claim.
- **Cost per experiment is real.** A failed run still bills. Teach learners to smoke-test on a few hundred steps before committing to a full run.

## Watch out

- **Do not teach the Adam update equation at Basic level.** Boxes and arrows; the formula is Advanced.
- **Do not demo a spike without explaining it.** A learner who sees a `nan` loss and no explanation concludes the tool is broken.
- **Do not present "learning rate 3e-4" as the answer.** It is a starting point that depends on model size, batch and data.
- **The stale claim to retire:** "you need fp16 with loss scaling to fine-tune on one GPU." In November 2026, bf16 on a modern accelerator removes that complexity, and most tooling defaults to it.
