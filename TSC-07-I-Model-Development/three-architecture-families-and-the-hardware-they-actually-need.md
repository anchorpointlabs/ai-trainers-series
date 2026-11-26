---
id: 07.02.I.K2
tsc: 7
level: Intermediate
code: K2
title: Three architecture families and the hardware they actually need
---

# Three architecture families and the hardware they actually need

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K2**


> **Framework text (verbatim):** "Cutting-edge research in generative AI architectures and techniques (e.g., conditional GANs, diffusion models, autoregressive models), hardware acceleration techniques (e.g., GPUs, TPUs), cloud computing platforms for training and scaling models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 2 of 17

**One-line version:** Three families model probability three different ways, and the architecture you pick decides which expensive hardware you are really renting.

## What it is

The bullet bundles three decisions learners treat separately and shouldn't: which architecture family generates the output, what hardware that family strains, and which cloud you rent it from. Conditional GANs, diffusion models and autoregressive models differ in training stability, sampling speed, controllability and cost. Hardware and platform follow from that choice.

## Deep expansion

### The concept

Every generative model learns a distribution and samples from it. The families differ in *how* they represent it: a GAN learns it implicitly through competition, a diffusion model learns to reverse a corruption process, an autoregressive model factorises it token by token. That difference decides whether training is stable, whether sampling is fast, whether you can steer the output, and whether the workload is compute-bound or memory-bandwidth-bound. Since GPU hours dominate the budget, architecture choice *is* cost choice.

### The sub-concepts

**Conditioning.** Nearly every useful model is conditional: image given text, reply given a ticket. Conditional GANs feed the label to generator and discriminator; diffusion conditions through cross-attention and *classifier-free guidance* — trained with and without the condition, then amplifying the difference at sampling time. The guidance scale is the most consequential knob: too low and the prompt is ignored, too high and the output saturates.

**Diffusion.** Add noise in steps, learn the reverse. Training is plain regression, so it does not collapse the way adversarial training can. *Latent diffusion* runs the process in a compressed space; *diffusion transformers* replaced U-Nets as the backbone; *flow matching* often replaces the noise objective with a straighter path, sampling in fewer steps.

**Autoregressive.** Factorise into next-token prediction over a discrete vocabulary. Native to text, predictable to scale, and the family behind the GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro / Gemini 4 Argon. Images and audio can be tokenised into the same frame, which is how unified multimodal models work — at a sequential sampling cost.

**Hardware and cloud.** The binding constraint is usually memory bandwidth and interconnect, not raw throughput: can the accelerator be fed, and can the chips talk. HBM size and NVLink-class links matter as much as the spec sheet. Cloud comes in three shapes — managed training (SageMaker, Vertex AI, Azure ML), bare-metal GPU rental, and spot capacity for checkpointed jobs — and data residency under PDPA decides which region is legal before price enters.

### How it connects to the rest of the framework

`TSC7-Basic-K1` is the family portrait at Basic level; `TSC7-Basic-K7` and `TSC7-Intermediate-K5` are the optimisation that makes any of them converge; `TSC7-Basic-K10` and `TSC7-Advanced-K3` go deeper on parallelism and CUDA-level libraries; `TSC7-Advanced-K6` covers the efficiency tricks you reach for when the bill is intolerable.

### What is current as of November 2026

- **Diffusion and autoregression have converged in practice.** Image and video generation runs on diffusion transformers with flow-matching objectives; text runs on autoregressive transformers; unified multimodal models blur the line by tokenising everything.
- **Quality is now won at inference, not architecture.** Distillation into few-step samplers moved the engineering problem from training a model to serving one cheaply.
- **Capacity planning beats price comparison.** Accelerator generations turn over faster than procurement cycles, so teams reserve for a class of GPU and treat spot instances with resumable checkpoints as normal practice.

### Common misconceptions

- *"GANs are obsolete."* They remain the fast option for super-resolution, avatars and synthetic data, training in a fraction of the time.
- *"Diffusion just adds noise."* It learns the reverse of a fixed corruption process; the schedule and prediction target are the design.
- *"TPU versus GPU is a brand preference."* It is an ecosystem choice — XLA and JAX versus CUDA and PyTorch — and porting cost decides.
- *"More GPUs means proportionally faster."* Past a point you pay for communication, not computation.

## How a student should understand it

**Mental model:** three painters learn your product catalogue. One works by forgery contest. One learns by restoring photographs that were progressively ruined. One paints a single stroke at a time. Same catalogue, three temperaments, three studio bills.

**Three things they can do after this bullet:**
1. Justify a family for a stated output type, naming its training risk.
2. Say whether a job is compute-bound or memory-bound, and what that implies for instance choice.
3. Explain why data residency sometimes picks the cloud, not price.

**Misconceptions to kill:** that one family replaced the others, that a GPU is a GPU, and that scaling is linear.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The forger and the detective.** A GAN is a forger and an authenticator improving against each other; the forger gets better because someone is always trying to catch him. Where it breaks: the pair can settle into a stalemate where the forger only ever produces one flawless note — mode collapse — and nobody notices because the detective is satisfied.

**Cleaning a dirty window.** Diffusion is a cleaner who starts with a frosted window and wipes it in fifty small passes, having learned from thousands of before-and-after pairs. Few-step distillation teaches the same cleaner to do it in four. Where it breaks: bad learned wiping leaves the window uniformly smeared — the over-guided, over-saturated output everyone recognises.

### Worked example with a real tool

A learner has 2,000 product photos across six categories and wants controllable generation. Type this into Claude or a coding assistant:

```
Write a PyTorch training script for a small conditional DDPM on
./product_images with labels.csv.

- 64x64 images, U-Net backbone, cosine noise schedule
- class embedding injected into every residual block
- classifier-free guidance: drop the label 10% of the time
- bf16 autocast, gradient clipping 1.0, EMA of weights
- every 500 steps: print step, loss, samples/sec, peak VRAM,
  and save a 3x3 sample grid
- checkpoint every 2,000 steps so the job resumes on spot capacity
```

Point at the dropped-label line (that is what makes guidance possible at inference), the EMA block (sampling raw weights gives visibly worse images), and the peak-VRAM print (it tells you whether a bigger batch needs a bigger card or just gradient accumulation).

### Lesson plan (Gagné's nine events)

1. **Gain attention** — three sample grids, same prompt, three families.
2. **State the objective** — pick a family and a hardware shape, with reasons.
3. **Recall prior learning** — GANs, VAEs and transformers from Basic.
4. **Present the content** — the three families, then memory bandwidth.
5. **Guide** — read a real log together: steps per second, VRAM, loss.
6. **Elicit performance** — teams choose family plus instance for a brief.
7. **Give feedback** — challenge the weakest cost estimate in each plan.
8. **Transfer** — write the hardware line in their own project brief.

## What the framework doesn't mention but trainers need to know

- **The data pipeline starves the GPU first.** CPU-side decoding while an expensive accelerator idles is the most common waste in a first training job.
- **Spot capacity changes the code.** Resumable checkpoints, deterministic data order and idempotent logging become requirements, not refinements.
- **Residency is a design constraint.** Personal data under PDPA cannot be shipped to whichever region is cheapest, which eliminates some platforms before benchmarking.
- **Lock-in hides in tooling.** A job wired to one platform's data loader and checkpoint format is not portable, even if the weights are.

## Watch out

- **Do not declare a winner among the families.** The honest answer is "depends on output type, sampling budget and team skill".
- **Do not demo training without checkpointing.** One interrupted cell teaches that long jobs are fragile.
- **Do not quote hardware prices from memory.** Accelerator pricing moves quarterly and regionally; teach the calculation.
- **The stale claim to retire:** "you need a cluster to train anything." In November 2026 a small conditional model trains on one rented GPU overnight; clusters are for pre-training, not the fine-tune most teams need.
