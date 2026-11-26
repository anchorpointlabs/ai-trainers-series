---
id: 07.02.I.K4
tsc: 7
level: Intermediate
code: K4
title: Loss functions and metrics: what you optimise is not what you care about
---

# Loss functions and metrics: what you optimise is not what you care about

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K4**


> **Framework text (verbatim):** "Advanced loss functions and metrics for evaluating generative performance."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 4 of 17

**One-line version:** The loss is the only thing the model can hear; the metric is the only thing you can defend — and the two are never the same number.

## What it is

A loss function is the differentiable signal training follows, computed per batch and averaged. A metric is the number a human uses to decide whether the model is good. Advanced generative work needs both: losses that survive adversarial, likelihood and preference training, and metrics that hold up when the output is an image, a paragraph or a waveform rather than a label.

## Deep expansion

### The concept

You cannot train on "is this good". You can only train on a smooth proxy: how surprised the model was by the right token, how far the predicted noise was from the real noise, how much the discriminator disliked the sample. Every proxy is a simplification, and every simplification can be optimised past the point where it corresponds to quality. GANs reach low adversarial loss while covering three of the twelve product categories. Language models reach low validation loss while producing bland, hedged prose. The skill at this level is reading a loss curve and a metric panel together and knowing which one is lying.

### The sub-concepts

**Likelihood losses.** Cross-entropy, equivalently negative log-likelihood, reported as perplexity. Cheap, stable, and per-token — which means a long, easy document can dominate a short, hard one. Teacher forcing during training versus free-running at inference creates *exposure bias*: the model never practises recovering from its own mistakes unless you train it to.

**Distribution-matching losses.** The VAE's ELBO balances reconstruction against a KL term that keeps the latent space orderly — turn the KL weight down and reconstructions sharpen while the space stops being samplable. Adversarial losses replace a fixed objective with a learned critic, adding feature-matching terms to stop training from thrashing. Diffusion uses plain MSE on the predicted noise (or velocity, or flow); its stability comes precisely from not being adversarial.

**Preference losses.** Instead of "match this target", the signal is "prefer A to B". A pairwise ranking loss over human or model-judged comparisons yields DPO and its relatives, which raise the probability of preferred completions without training a separate reward model. The characteristic failure is over-optimisation: push the margin too far and the model becomes verbose, sycophantic or degenerate.

**Metrics that are not losses.** FID compares feature statistics of generated and real images; CLIPScore measures text-image alignment; BLEU, ROUGE, chrF and WER score text against references; perplexity scores language models; win rate scores preference. None is differentiable, none is comparable across papers with different preprocessing, and all of them can be gamed by a model that has seen the test set.

### How it connects to the rest of the framework

`TSC7-Basic-K6` introduces the basic loss-and-metric pairs; `TSC7-Intermediate-K5` is the optimisation that makes them converge; `TSC7-Intermediate-K7` shows why a single aggregate metric hides subgroup failure; `TSC5` is the full evaluation discipline; `TSC7-Advanced-K9` supplies the statistical inference needed before you claim a difference is real.

### What is current as of November 2026

- **Preference optimisation is standard after supervised tuning.** The DPO family displaced most reward-model pipelines for general alignment, while reinforcement learning against verifiable rewards became the norm for reasoning-heavy models.
- **FID is still reported and still distrusted.** Practitioners increasingly pair it with human or model-judged pairwise comparisons, because FID moves with sample count and preprocessing as much as with quality.
- **Judge-based metrics arrived with their own bias.** Using a frontier model — GPT-6 generation, Claude 5.5, Gemini 4 Argon — as the scorer is now common, and so is the discovery that it favours long, confident, well-formatted answers.

### Common misconceptions

- *"Lower loss means a better model."* Lower *training* loss means a better fit to the training set. Validation loss and human preference are the numbers that matter.
- *"FID of 12 beats FID of 15."* Only if the sample size, resize filter and feature extractor match. Across papers, they usually don't.
- *"Low perplexity means it knows the subject."* It means the text was unsurprising to the model, which is also true of repetitive boilerplate.
- *"BLEU measures translation quality."* It measures n-gram overlap with one reference, and it rewards bland phrasing.

## How a student should understand it

**Mental model:** a marking scheme. The rubric can only count what it can count — spelling, structure, number of points — so a well-spelled wrong answer scores higher than a correct one written badly. The rubric is the loss; the examiners' real judgement is the metric.

**Three things they can do after this bullet:**
1. Pick a loss appropriate to the model family, and state what it cannot see.
2. Choose metrics that match the deployment claim, including a human or judge check.
3. Explain why a leaderboard win and a good product are different events.

**Misconceptions to kill:** that loss equals quality, that metrics are comparable across papers, and that one aggregate number is enough.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food hygiene grade.** A stall with an A grade is not necessarily delicious; the grade measures handling practice, not taste. Chasing the grade — clean, refrigerated, tasteless — is exactly what over-optimising a proxy looks like. Where it breaks: unlike FID, the hygiene grade is at least audited by a human.

**PSLE tuition and the answer key.** A student trained only on one publisher's answer key learns the key's quirks. Feed the same paper back and the score is perfect; change the publisher and the score collapses. That is test-set contamination with a familiar face. Where it breaks: a student can be handed an unseen paper by a different setter; a benchmark that leaked has no second setter unless you wrote a private one.

### Worked example with a real tool

A learner has a fine-tuned image model and a folder of 500 real product shots. Type this into a coding assistant:

```
Write an evaluation script:

1. Generate 500 images with the same class prompts and seed range
   as the reference set.
2. Compute FID with pytorch-fid, fixing the resize filter and
   image size, and print the exact preprocessing used.
3. Compute mean CLIPScore between each image and its prompt.
4. Bootstrap both metrics over 1,000 resamples and print the 95%
   confidence interval.
5. Save a contact sheet of the 10 lowest-scoring images.
```

Point at step 2 (fixed preprocessing is what makes the number defensible), step 4 (two FID runs that differ by less than the interval are the same run), and step 5 — the low-scoring images tell you *what kind* of failure you have, which no scalar ever will.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a model with excellent loss and visibly worse samples.
2. **State the objective** — choose and defend a loss plus a metric panel.
3. **Recall prior learning** — basic loss and metric pairs from the Basic level.
4. **Present the content** — likelihood, distribution-matching, preference, metrics.
5. **Guide** — read one FID report and one win-rate table together.
6. **Elicit performance** — teams write a one-page metric panel for their own model.
7. **Give feedback** — mark the panels: is every claim measurable by the metric chosen?
8. **Transfer** — each learner replaces one vanity metric in their current project.

## What the framework doesn't mention but trainers need to know

- **Aggregate metrics hide subgroup failure.** A model can improve FID overall while degrading badly on one category; slice before you ship.
- **Human evaluation is the expensive part.** A credible win-rate study needs blinded raters, a rubric and agreement checking — budget for it or the claim is decorative.
- **Judge models have positional and length bias.** Swap the order of A and B and a meaningful share of verdicts flip; run both orders.
- **Every metric you optimise becomes a target.** If the team sees only FID, someone will tune preprocessing until FID improves and the images do not.

## Watch out

- **Do not compare metrics from different sources.** Most "our model beats theirs" claims collapse on inspection of preprocessing and sample count.
- **Do not quote a benchmark number without its interval.** Small-sample generative metrics are noisy, and the difference is often inside the noise.
- **Do not let a judge model be the only judge.** It is a screening tool, not a measurement of user preference.
- **The stale claim to retire:** "the loss went down, so the model improved." In November 2026 the honest version is "validation loss fell and the blinded win rate moved in the same direction".
