---
id: 07.01.B.K1
tsc: 7
level: Basic
code: K1
title: "Deep learning theory: GANs, VAEs and transformers in plain terms"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Deep learning theory: GANs, VAEs and transformers in plain terms

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K1**


> **Framework text (verbatim):** "Deep learning theory and algorithms (e.g., GANs, VAEs, Transformers)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 1 of 15

**One-line version:** Three families of network, three different bets about what "generate" means — and one of them, the transformer, is the bet your job currently rests on.

## What it is

Deep learning theory is the set of ideas that explain how a network with many layers can learn to *produce* content rather than just label it. The framework names three algorithm families — GANs, VAEs and Transformers — because each answers the generation question in a different way and fails in a different way. At Basic level you are not deriving the maths. You are learning which family does what, what its output looks like, and why the choice still matters when you are only fine-tuning.

## Deep expansion

### The concept

A generative network is shown many examples and then asked to make more of the same kind. All three families do that, but they disagree about the *training signal* — the thing that tells the network whether it did well.

A **GAN** trains two networks against each other. The generator makes a fake; the discriminator tries to tell fake from real. The generator's only reward is fooling the discriminator, so it improves by being pushed, not by being corrected. That is why GAN output is sharp and why GAN training is famously unstable.

A **VAE** trains one network to squeeze an input into a small cloud of numbers — a *distribution* over latent variables — and a second network to reconstruct the input from a point sampled out of that cloud. The loss has two parts: reconstruct faithfully, but keep the cloud close to a simple bell curve so you can sample from it later. That second term is what makes the latent space smooth and the output slightly soft.

A **transformer** reads a whole sequence at once through *attention*, weighing every token against every other token, and is trained to predict the next token. Nothing in the architecture is specific to language. The same block, given images cut into patches or audio cut into frames, works. That generality is why one architecture now covers text, image, audio and code.

### The sub-concepts

**The training signal.** Adversarial (a judge), reconstruction (a copy), or prediction (the next item). Everything else follows from this.

**Latent space.** A compressed map where similar things sit near each other. The VAE's contribution, and the reason "interpolate between two faces" works.

**Attention.** Each token looks at all the others and decides what to carry forward. It is a weighting scheme, not cognition.

**Token-by-token generation.** A transformer writes one token, appends it, and runs again. Every long answer is many short predictions.

**Where diffusion sits.** Not named in this bullet, but since 2022 the dominant image and video method has been diffusion: start from noise, denoise step by step. It borrows the VAE's latent space and the transformer's attention, which is why the three names still explain the field.

### How it connects to the rest of the framework

`TSC7-Basic-K3` is the probability under all three — sampling is what they have in common. `TSC7-Basic-K5` (embeddings and tokenisation) is what goes in the front door. `TSC7-Basic-K6` (loss functions) is how each family is judged during training. `TSC7-Intermediate-K2` is where diffusion, conditional GANs and hardware acceleration get proper treatment. If you only remember one thing from this bullet, remember that architecture is a *choice*, not a given.

### What is current as of November 2026

The transformer won. Every frontier system named in this library — the GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — is transformer-family, and so are the open-weight models most teams fine-tune. GANs have retreated into components and niches: super-resolution, real-time avatars, some synthetic-data pipelines. VAEs survive mainly as the compressor inside latent diffusion models. Diffusion is the default for images and video, and increasingly for audio.

The practical shift for a Basic class: you are far more likely to *adapt* a transformer than to train any of these from scratch. Learn the families as vocabulary and as diagnosis — "this output is blurry" points at a VAE-lineage component; "this output repeats itself" points at decoding and training data.

### Common misconceptions

- *"Transformer is a model."* It is an architecture. GPT-6 Terra and Claude 5.5 are models built on it, the way two different cars can share a chassis.
- *"GANs are dead."* They are components now, and still the fastest route to sharp, small, real-time output.
- *"Attention means it focuses like a person."* Attention is a weighted average. It has no goal.
- *"You need the maths to work in this field."* You need the vocabulary to read a model card and the judgement to pick one. The derivations are for the Advanced level.

## How a student should understand it

**Mental model:** three ways to learn a dish you have only eaten. One cooks for a harsh friend who marks every attempt (GAN). One learns the *range* the recipe allows and re-rolls within it (VAE). One reads every recipe ever written and predicts the next step (transformer).

**Three things they can do after this bullet:**
1. Look at a model card or a paper title and name the family: adversarial, reconstruction or prediction.
2. Explain in one sentence why an image model and a text model can share an architecture.
3. Predict the characteristic failure: blur (VAE lineage), repetition and collapse (GAN), confident nonsense (transformer).

**Misconceptions to kill:** that the architecture *is* the product, that GANs are obsolete, and that generative models "understand" what they produce.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The forger and the ICA officer.** A forger makes ICs; an officer checks them. Each improves because the other does. Stop challenging the forger and the skill decays — that is mode collapse. The analogy breaks at the endpoint: a real forger eventually stops needing the officer, while a GAN generator is only ever as good as its discriminator.

**The MRT map versus one station at a time.** An older sequence model read the line station by station, remembering only what it carried. A transformer looks at the whole map and asks, for each station, which other stations matter. That is why it handles long context and why it costs more as the map grows.

**The recipe that says "salt to taste".** A VAE does not memorise one laksa; it learns the *distribution* of laksa and samples a plausible bowl. Sometimes that means a bowl nobody would order — which is exactly the trade you are making.

### Worked example with a real tool

Open Google Colab and run one cell. This is a real, working demonstration of sampling:

```python
!pip install -q transformers
from transformers import pipeline

gen = pipeline("text-generation", model="gpt2")
print(gen("The stall closes at", max_new_tokens=20, num_return_sequences=3))
```

What to point at afterwards: three different completions from one prompt. Nothing changed in the input — the model produced a *distribution* and sampled from it three times. That single observation separates generative models from classifiers, and it is the bridge to `TSC7-Basic-K3`.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show three images of a person who does not exist and ask who they are. Let the room argue before you answer.
2. **State the objective** — by the end you can name the three families and predict what each one gets wrong.
3. **Recall prior learning** — they already know what a model is from TSC #1; ask what "training" meant there.
4. **Present the content** — the three training signals, one slide each, plus the note that diffusion is the current image default.
5. **Guide** — walk through the Colab cell together and ask the room to explain the three outputs before you do.
6. **Elicit performance** — in pairs, match six model cards to a family and write the failure they expect.
7. **Give feedback** — correct the pair that called a diffusion model a GAN; praise anyone who spotted the VAE inside it.
8. **Transfer** — each learner names one model they use at work and the family it belongs to.

## What the framework doesn't mention but trainers need to know

- **Almost nobody trains these from scratch.** The realistic Basic task is fine-tuning a transformer or calling an API. Teach the families as diagnosis, not as a build order.
- **Data beats architecture at this level.** A modest transformer on clean data outperforms a large one on scraped rubbish. The framework lists architectures before it lists data, which inverts the actual priority.
- **The vocabulary is the deliverable.** Learners will sit in meetings where someone says "we're using a diffusion backbone with a LoRA". Being able to nod correctly is a real outcome.
- **Cost is architectural.** Attention grows with context length; that is why long documents cost more per token. One sentence here prevents a lot of confusion later.

## Watch out

- **Do not teach backpropagation to a Basic class.** Draw the three training signals as arrows and stop.
- **Do not present GANs as the future.** A 2019 slide deck is the most common source of this error.
- **Do not say "the model learns like a brain".** It optimises a number. The brain comparison causes more harm than it saves.
- **The stale claim to retire:** "generative AI means GANs." In November 2026 it means transformers and diffusion, with GANs as a component supplier.
