---
id: 07.01.B.A2
tsc: 7
level: Basic
code: A2
title: "Implementing a model from an existing architecture, without inventing anything"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Implementing a model from an existing architecture, without inventing anything

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Ability A2**


> **Framework text (verbatim):** "Implement generative models based on existing architectures."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Ability · Bullet 12 of 15

**One-line version:** The job is to stand up a known architecture correctly — config, weights, tokeniser, forward pass — and to know which of those four you are allowed to change.

## What it is

This is the ability to take a published architecture — a transformer block, a VAE, a small GAN, a diffusion UNet — and get it running as working code, either by loading published weights or by instantiating the architecture from its configuration. "Existing" is the operative word: at Basic level you are not designing a novel network. You are reproducing a known one faithfully and understanding each part well enough to adapt it.

## Deep expansion

### The concept

An architecture is a *shape*: how many layers, how wide, how attention is arranged, what the output head looks like. A model is that shape plus a set of trained weights. Most of the time you want both, already paired, from a model hub. Sometimes you want the shape with fresh weights — to train from scratch on a small domain, to study the parts, or to attach a different head.

The four things that must agree:

1. **The configuration** — layer count, hidden size, vocabulary size, attention heads. Change the vocabulary size and the embedding table no longer matches the tokeniser.
2. **The tokeniser** — must be the one the weights were trained with. A different tokeniser produces token IDs the model has never seen.
3. **The weights** — the checkpoint, in the format the library expects.
4. **The head** — causal language modelling, sequence classification, conditional generation. Swapping the head is legitimate and common; swapping the others usually is not.

### The sub-concepts

**Loading versus instantiating.** `from_pretrained` gives you shape plus weights. `from_config` gives you the shape with random weights. Knowing which you called is the first competency.

**Parameter count.** Roughly, parameters scale with layers × width². Counting them is how you sanity-check that you loaded what you think you loaded.

**The forward pass.** Input IDs in, logits out. At Basic level you should be able to say what shape the output tensor has and what the numbers mean.

**Head swapping.** A causal model can be turned into a classifier by replacing the language-modelling head and training the new one. This is a legitimate, common adaptation — and it is still "based on an existing architecture".

**Initialisation.** Random weights need a sensible initialisation scheme. Wrong initialisation produces a model that never trains, and the symptom looks like a learning-rate problem.

**Licence and provenance.** An architecture may be free to use while the weights are not, or vice versa. The model card states it; read it before you build a product on it.

### How it connects to the rest of the framework

`TSC7-Basic-K1` is the theory of the architecture you are implementing; `TSC7-Basic-K2` is the library you implement it in; `TSC7-Basic-K5` is the tokeniser that must match. `TSC7-Basic-K8` is the fine-tuning that usually follows. `TSC7-Basic-A1` decided that this architecture is the right choice. `TSC7-Intermediate-A1` (constructing custom models for specific tasks) is where you start changing the shape rather than reproducing it.

### What is current as of November 2026

The hub has become the work surface. Hugging Face's `transformers`, `diffusers` and `timm` libraries now cover the overwhelming majority of published architectures, and loading a model is two lines with a documented config behind them. Two shifts matter for a Basic class: **safetensors has displaced pickle-based checkpoints** as the default weight format, largely for security reasons, and **architecture families are increasingly standardised across vendors**, so the same loading code works for a Llama-derived, Qwen-derived or Mistral-derived checkpoint.

The honest consequence: writing an architecture from scratch is now a research skill, not a practitioner skill. Reading one, adapting its head, and loading it correctly is the practitioner skill this bullet tests.

### Common misconceptions

- *"Implementing a model means writing the layers myself."* It means standing one up correctly. Writing the layers is a different, more advanced job.
- *"Any tokeniser works if the vocabulary size matches."* Matching size is necessary and nowhere near sufficient; the token-to-ID mapping must be identical.
- *"Random weights are a blank slate with no consequences."* Initialisation scale affects whether training converges at all.
- *"If it loads, it is correct."* It loads, but it may be in the wrong precision, on the wrong device, or in training mode when you wanted evaluation mode.
- *"The architecture licence covers the weights."* They are separate grants and often differ.

## How a student should understand it

**Mental model:** flat-pack furniture. The design is done; your job is to assemble it exactly, with the right screws, and to notice when a part is missing rather than forcing it.

**Three things they can do after this bullet:**
1. Load a published model and report its parameter count, precision and device.
2. Instantiate the same architecture from its config and explain the difference in the two code paths.
3. Swap the output head for a classification task and describe what must now be trained.

**Misconceptions to kill:** that implementation means invention, that tokenisers are interchangeable, and that a successful load means a correct setup.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Flat-pack furniture.** The instructions exist, the holes are pre-drilled, and the failure mode is not "I could not design a better shelf" — it is "I used the wrong screw and it wobbles". Most model bugs are wrong screws.

**The recipe versus the kitchen.** The architecture is the recipe; the weights are a batch someone already cooked. Loading `from_pretrained` is reheating their batch. `from_config` is starting from the recipe with an empty pot. Both are cooking; only one is likely to be edible today.

### Worked example with a real tool

Two cells, deliberately adjacent, so the difference is visible:

```python
from transformers import AutoConfig, AutoModelForCausalLM

cfg = AutoConfig.from_pretrained("gpt2")
print(cfg.n_layer, cfg.n_embd, cfg.vocab_size)

fresh = AutoModelForCausalLM.from_config(cfg)          # random weights
trained = AutoModelForCausalLM.from_pretrained("gpt2") # real weights

print(sum(p.numel() for p in fresh.parameters()))
print(sum(p.numel() for p in trained.parameters()))
```

Then generate from both:

```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("gpt2")
print(tok.decode(fresh.generate(tok("The stall", return_tensors="pt").input_ids,
      max_new_tokens=20)[0]))
```

What to point at afterwards: identical parameter counts, completely different output. The architecture determines the shape; the weights determine whether it can speak. That one comparison prevents a great deal of confusion about what "training a model" is for.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two outputs, one fluent and one gibberish, and reveal that both come from the same architecture.
2. **State the objective** — by the end you can load a model, count its parameters, and explain the difference from instantiating one.
3. **Recall prior learning** — from K2 they know the libraries; now they use them.
4. **Present the content** — the four things that must agree, plus head swapping and licensing.
5. **Guide** — run both cells and read the outputs aloud together.
6. **Elicit performance** — pairs load a different small model, report parameter count, precision and licence.
7. **Give feedback** — catch anyone who loaded a tokeniser from a different family; show the ID mismatch explicitly.
8. **Transfer** — each learner identifies one model they could legitimately adapt with a new head for their own work.

## What the framework doesn't mention but trainers need to know

- **Precision and device are part of "implemented".** A model loaded in fp32 on CPU will work and be unusable. Teach `torch_dtype` and `.to("cuda")` as part of the same step.
- **Evaluation mode matters.** Dropout left on during inference produces inconsistent, slightly wrong output that looks like a model problem.
- **The model card is the specification.** Context length, licence, training data, known limitations. Learners who read it avoid most surprises.
- **Small models are the right teaching tool.** A 124-million-parameter model demonstrates every concept and runs in seconds. Do not start with a 70-billion-parameter download.

## Watch out

- **Do not let the demo become a download race.** A large model download will eat the session; pin a small one.
- **Do not skip the licensing line.** Learners ship things; a licence read at build time is worth more than a lecture on ethics later.
- **Do not imply that loading a model is the same as building a system.** The system is data, evaluation, serving and monitoring — this is one component.
- **The stale claim to retire:** "you need to implement the transformer yourself to understand it." In November 2026, `from_config` plus a parameter count teaches the shape faster and leaves more time for data and evaluation, which is where the actual difficulty lives.
