---
id: 07.02.I.A2
tsc: 7
level: Intermediate
code: A2
title: Watching a model learn: stability, convergence and the loss curve
---

# Watching a model learn: stability, convergence and the loss curve

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A2**


> **Framework text (verbatim):** "Monitor generative training processes for stability and convergence."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 12 of 17

**One-line version:** A training run tells you it is failing long before it fails — in the gradient norm, the tokens per second and the shape of the curve.

## What it is

Monitoring is the practice of watching a training run while it happens: loss against steps, gradient norms, throughput, memory, and periodic evaluation and samples. Its purpose is to distinguish three situations that look similar from the outside — the run is learning, the run is learning the wrong thing, and the run is about to collapse — and to intervene while the intervention is still cheap.

## Deep expansion

### The concept

You have one curve and several hypotheses. A spike can be a bad batch, a learning rate that is too high, a numerical overflow, or a dataloader returning garbage. Diagnosis means looking at the *other* signals before touching the configuration: if the gradient norm spiked first, it is numerical or batch-related; if tokens per second dropped, something upstream is starving the GPU; if validation loss diverged while training loss fell, you are overfitting. The discipline is to instrument before you train, so the diagnosis has evidence.

### The sub-concepts

**Reading the curve.** A healthy run dips sharply during warmup, settles into a noisy downward trend, and shows step-wise improvement when the learning rate decays. Warning shapes: repeated sawtooth (learning rate too high), a step change that never recovers (bad data shard), a slow upward drift in training loss (diverging), validation loss turning up while training loss falls (overfitting), and a dead-flat line from step zero (learning rate too low, or gradients not flowing).

**Healthy signals by family.** Autoregressive losses fall predictably and should be inspected per token position and per language. Diffusion losses fall fast, then plateau — a plateau there is normal, and per-noise-level loss tells you whether the model is ignoring high-noise steps. GAN losses are not interpretable on their own; judge those with fixed-seed sample grids and a quantitative metric. A VAE's ELBO should be logged split into reconstruction and KL, or you cannot tell which term is misbehaving.

**Instrumentation.** Log gradient norm and clipping fraction, learning rate, tokens or samples per second, memory use, and a NaN counter. Keep an EMA of weights for sampling. Write checkpoints on a schedule that matches the cost of losing the run, and verify that a checkpoint actually resumes before step one — not after hour nine.

**The intervention ladder.** Re-check the data first, because most instability is a data bug wearing a numerical costume. Then lower the learning rate, lengthen warmup, tighten clipping, adjust batch and learning rate together, resume from the last good checkpoint, and only then restart clean.

### How it connects to the rest of the framework

`TSC7-Intermediate-K5` is the configuration being monitored; `TSC7-Intermediate-K4` defines what the periodic evaluation measures; `TSC7-Intermediate-K2` explains the hardware signals; `TSC7-Advanced-A3` is the deeper performance optimisation this diagnosis feeds; `TSC7-Advanced-A6` covers automating the response.

### What is current as of November 2026

- **Observability is a first-class part of training.** Runs against the GPT-6 generation class of models are tracked with per-step metrics, and the teams that ship reliably are the ones with alerting on gradient norm rather than on loss alone.
- **Loss spikes are understood as state events.** The research conversation has shifted toward optimiser-state resets and checkpoint rollback rather than only lowering the learning rate.
- **Cost telemetry sits beside the loss curve.** Tracking dollars per step, not just seconds per step, has become normal as accelerator rental dominates budgets.

### Common misconceptions

- *"Loss must always go down."* Diffusion plateaus by design; a flat stretch is often the model learning high-noise structure.
- *"A NaN means the model is broken."* It usually means one batch contains something pathological — check the data loader first.
- *"Low discriminator loss means the GAN is winning."* GAN losses are relative, not absolute; only sample-based metrics tell you about quality.
- *"If loss looks fine, the run is fine."* Throughput collapse and silent data duplication both leave the loss curve looking acceptable.

## How a student should understand it

**Mental model:** the dashboard, not the windscreen. You drive by the temperature gauge and the tachometer; the scenery tells you nothing about whether the engine is about to seize.

**Three things they can do after this bullet:**
1. Instrument a run so that a failure is diagnosable from the logs alone.
2. Recognise four curve shapes and name the likely cause of each.
3. Follow the intervention ladder instead of randomly changing hyperparameters.

**Misconceptions to kill:** that loss must always fall, that NaN means a broken model, and that a flat curve means success.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Simmering laksa.** You do not judge a pot by the bubbles alone; you watch the heat, the reduction and the colour, and you taste at intervals. Training is the same pot: loss is the bubbles, gradient norm is the heat, periodic samples are the tasting. Where it breaks: a pot gives you smell warnings; a training run gives you only the logs you thought to record.

**Driving to KL.** You do not check fuel only when the tank is empty — you watch the gauge, the odometer and the time, and you decide early whether to stop. A run that dies at hour nine without a checkpoint is a car that ran out on the highway. Where it breaks: a car shows one gauge per system; a training run throws hundreds of metrics at you, and most of them are noise.

### Worked example with a real tool

A learner's run keeps dying overnight. Type this into a coding assistant:

```
I exported a failed run from W&B (run.csv: step, train_loss,
val_loss, grad_norm, clip_frac, lr, tokens_per_sec, gpu_mem_gb).

1. Plot train/val loss, grad norm (log scale) and tokens/sec on
   shared x-axis, marking where val loss stopped improving.
2. Find the first step where grad_norm > 3x its rolling median and
   list the 10 steps before it.
3. Cross-check tokens/sec for dips in the same window.
4. Print a one-paragraph diagnosis with the evidence for each
   hypothesis you can support, and what data to inspect next.
```

Point at step 2 — the gradient spike almost always precedes the loss spike, which is what makes early alerting possible — and step 3: a throughput dip alongside a spike usually means one worker returned malformed samples rather than the model misbehaving.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two runs, one healthy and one about to die; ask which and why.
2. **State the objective** — instrument a run and diagnose four classic failures.
3. **Recall prior learning** — optimiser settings from K5, metrics from K4.
4. **Present the content** — curve shapes, per-family signals, the ladder.
5. **Guide** — read one real log together and name the failure.
6. **Elicit performance** — teams diagnose three anonymised log excerpts.
7. **Give feedback** — debrief: which evidence supported which hypothesis.
8. **Transfer** — each learner adds gradient-norm alerting to their next run.

## What the framework doesn't mention but trainers need to know

- **Alerting beats watching.** Nobody stares at a curve for nine hours; a threshold on gradient norm and a monitor on tokens per second save more runs than any dashboard.
- **Checkpoint resume must be tested.** A resume path exercised only in theory is a resume path that fails at 3 a.m.
- **Evaluation noise gets mistaken for progress.** With a small validation set, a few tenths of a point is noise; log the interval, not just the mean.
- **Data can change mid-run.** If the corpus is still being appended to while training reads it, your curve is measuring two distributions.

## Watch out

- **Do not declare a run dead after one spike.** Look for the recovery; a single spike with a clean gradient norm is usually harmless.
- **Do not interpret GAN losses as quality.** Show a fixed-seed sample grid instead.
- **Do not change three things at once.** You will learn nothing and the next run will be uninterpretable.
- **The stale claim to retire:** "the loss went down, so it's better." In November 2026 the diagnosis is gradient norm, throughput, validation and samples, read together.
