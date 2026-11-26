---
id: 07.01.B.K3
tsc: 7
level: Basic
code: K3
title: "Probability and statistics: why a generative model is a sampling machine"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Probability and statistics: why a generative model is a sampling machine

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K3**


> **Framework text (verbatim):** "Probability theory and statistics (e.g., latent variables, probabilistic modelling)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 3 of 15

**One-line version:** A generative model does not store answers — it stores a probability distribution over answers, and every output you see is one draw from it.

## What it is

Probability theory and statistics are how a model represents uncertainty. In a generative system you are not predicting a single label; you are modelling the distribution of possible outputs, then sampling from it. Latent variables are the hidden factors the model invents to explain the data it was shown, and probabilistic modelling is the discipline of writing those assumptions down precisely. At Basic level you need three ideas — distributions, sampling and latent structure — and no proofs.

## Deep expansion

### The concept

Ask a classifier "is this a cat?" and it answers yes or no. Ask a generative model "what comes after this sentence?" and the honest answer is not a word — it is a list of words with weights. Every generative system works this way internally: it produces numbers that behave like probabilities over the next token, pixel or frame, and something then picks one.

That pick is the part learners miss. **Sampling** means the model can give a different answer to the same input, and that is not a bug. It is the mechanism. A temperature setting, a top-p cutoff, a random seed — these are all controls on how the draw is made, not on what the model knows.

Latent variables are the second idea. The model cannot observe everything that explains the data — the lighting, the writer's intent, the reason this review is negative — so it invents a small set of hidden numbers that, in combination, would generate what it sees. In a VAE those numbers are the compressed code. In a diffusion model they start as noise. In an agent they are the "state of the world" the model is implicitly tracking.

### The sub-concepts

**Distribution.** A description of which outcomes are likely, not which outcome will occur. A model is trained to match the data's distribution, not to memorise its rows.

**Sampling and temperature.** Low temperature concentrates the draw on likely tokens (safe, repetitive). High temperature spreads it (varied, incoherent). "top-p" is a different rule with a similar effect.

**Latent variables.** Hidden factors that explain visible data. The single most useful abstraction in this bullet, because it recurs in VAEs, diffusion and embeddings.

**The likelihood idea.** Training maximises the probability the model assigns to the real data. Loss functions in `TSC7-Basic-K6` are, almost always, a re-arrangement of that same idea.

**Expected value versus one draw.** A model with good average quality can still produce a terrible specific output. Evaluation has to look at both.

### How it connects to the rest of the framework

This bullet is the mathematical floor under `TSC7-Basic-K1`: GANs, VAEs and transformers are three different ways to learn and use a distribution. `TSC7-Basic-K6` (loss functions) is the likelihood idea made concrete. `TSC7-Basic-K5` (embeddings) is the geometric view of the same object. `TSC7-Intermediate-K9` (synthetic data) is sampling at industrial scale. And `TSC5-Basic-K3` (evaluating outputs) exists precisely because one draw is not the distribution.

### What is current as of November 2026

The sampling controls are now user-facing product features. "Temperature", "top-p" and "seed" appear in developer consoles for current frontier models; diffusion tools expose "steps" and "guidance" instead, which are the same idea wearing different clothes. Reasoning-tuned models have complicated the picture: they spend extra compute on a *search* over possible continuations before answering, which is a form of sampling multiple candidates and selecting among them.

The practical consequence for a Basic class: output variance is now expected, and "it gave me a different answer yesterday" is a statement about sampling, not about the model being broken. Teams that need repeatability set temperature low, fix the seed where the API allows it, and log the settings alongside the output.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The model has a right answer and sometimes gets it wrong."* For open-ended generation there is no single right answer; there is a distribution, and the model samples from it.
- *"Temperature makes the model smarter."* It changes the draw. Higher is not smarter; it is more willing to pick unlikely tokens.
- *"Latent variables are a deep-learning invention."* Factor analysis and principal components are the same idea, decades older.
- *"Statistics is only for evaluation."* It is inside the training objective. You cannot read a loss curve without it.

## How a student should understand it

**Mental model:** a chicken-rice stall whose cook never gives you exactly the same plate twice. The recipe is the distribution; the plate in front of you is one draw. Judging the stall from one plate is a sampling error.

**Three things they can do after this bullet:**
1. Explain why the same prompt produces different outputs, and name the two or three controls that change the spread.
2. Point at a model's latent space in a diagram and say what "hidden factor" means there.
3. Say why evaluating a generative model needs many outputs, not one.

**Misconceptions to kill:** that variation means malfunction, that temperature is a quality dial, and that the model stores answers rather than distributions.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The weather forecast.** "70% chance of rain" is not a wrong forecast when it stays dry. It was a probability; the day was one draw. A generative model is a forecast over words, and a single bad output no more refutes it than one dry day refutes the meteorological service. The analogy breaks when the model is confidently wrong about a fact — that is a knowledge error, not a sampling error, and learners must separate the two.

**The four-digit lottery, but honest.** The model is not picking numbers it likes. It is drawing from a weighted pool. Turn the temperature up and you are flattening the weights, which is why high-temperature output reads like a stranger's dream.

### Worked example with a real tool

In Colab, show the draw explicitly. Same prompt, three settings, one run:

```python
from transformers import pipeline
gen = pipeline("text-generation", model="gpt2")

for t in [0.2, 0.8, 1.4]:
    out = gen("At the polyclinic, the queue", max_new_tokens=15,
              temperature=t, do_sample=True, num_return_sequences=1)
    print(t, "→", out[0]["generated_text"])
```

Run it twice and the outputs change. What to point at afterwards: at 0.2 the model repeats safe, common phrasing; at 1.4 it wanders. Nothing about the model changed between the three lines — only the width of the draw. That is the entire concept, demonstrated in ten seconds.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room to predict the next word in a sentence you read aloud, then show the model's top five candidates.
2. **State the objective** — by the end you can explain output variation using three words: distribution, sample, temperature.
3. **Recall prior learning** — from TSC #1 they know the model predicts; now they see *what* it predicts.
4. **Present the content** — distribution, latent variables, sampling controls, with one diagram.
5. **Guide** — run the three-temperature cell together and narrate what you expect before pressing play.
6. **Elicit performance** — pairs pick a temperature for a stated job (patient instructions vs brainstorm) and justify it.
7. **Give feedback** — challenge any pair that says low temperature is "more accurate"; it is more predictable.
8. **Transfer** — each learner names one workflow where variation is unacceptable and one where it is valuable.

## What the framework doesn't mention but trainers need to know

- **Determinism is a product decision, not a default.** Many APIs no longer guarantee identical output even at temperature zero, because batching and hardware differ. Teach logging, not hoping.
- **Latent variables are the bridge to every modern architecture.** If learners leave with only this idea, the bullet has paid for itself.
- **Statistical literacy is uneven in the room.** Some learners will have done A-level maths; others will flinch at the word "distribution". Use the stall analogy first and the term second.
- **Sampling costs money.** Generating five candidates to pick one multiplies inference spend. Basic learners should know the economics exist.

## Watch out

- **Do not teach Bayes' theorem here.** It is the wrong level and it eats the session.
- **Do not say "random" without qualification.** The draw is weighted; "random" makes learners think the model is guessing blindly.
- **Do not confuse variance with hallucination.** One is sampling; the other is a model asserting something false. Different fixes.
- **The stale claim to retire:** "set temperature to zero for facts." In November 2026, zero temperature reduces variation but does not guarantee truth, and several providers no longer promise bit-identical output.
