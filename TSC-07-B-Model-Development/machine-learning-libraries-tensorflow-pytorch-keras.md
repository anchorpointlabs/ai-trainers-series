---
id: 07.01.B.K2
tsc: 7
level: Basic
code: K2
title: "The library layer: what TensorFlow, PyTorch and Keras actually do"
as_at: 2026-11-26
review_by: 2027-02-25
---

# The library layer: what TensorFlow, PyTorch and Keras actually do

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K2**


> **Framework text (verbatim):** "Machine learning libraries (e.g., TensorFlow, PyTorch, Keras)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 2 of 15

**One-line version:** A library is not a model and not a language — it is the workshop where the model gets built, and three names cover almost every job you will be handed.

## What it is

Machine learning libraries are collections of pre-written code for building, training and running neural networks. TensorFlow, PyTorch and Keras are the three the framework names, and between them they cover the overwhelming majority of published work. For a model developer, this bullet is not background reading — it is the actual equipment. The skill being tested is knowing which one you are in and why, because a model released in one does not load in another without conversion.

## Deep expansion

### The concept

Every neural network is, underneath, a very large pile of matrix multiplications plus the bookkeeping to differentiate them. Nobody writes that by hand. A library gives you three things: the **tensor** (a multi-dimensional array that can live on a GPU), **automatic differentiation** (it computes the gradients for you), and **layers and optimisers** (pre-built components you assemble). That is the whole offer. The difference between libraries is how much of the assembly they hide from you and how they behave when you deploy.

The framework lists this bullet second, right after the architectures, because you cannot express an architecture without one. A learner who says "I want to build a transformer" has really said "I want to build a transformer in something".

### The sub-concepts

**PyTorch.** The research default. Code reads like ordinary Python — you write the forward pass as a function, and it records what happened so gradients can be computed. Nearly every open-weight model on Hugging Face loads in PyTorch first, and most papers ship PyTorch code. If you are fine-tuning an existing model in 2026, this is the path of least resistance.

**TensorFlow.** Google's library, built for production pipelines from the start. Its strength is serving: taking a trained model and running it efficiently inside an application, often via TensorFlow Serving or TensorFlow Lite on a phone. Large enterprise systems and older tutorials are full of it.

**Keras.** A high-level layer — now bundled with TensorFlow, with a multi-backend version that can also run on PyTorch. You describe a model as a stack of layers in a few readable lines. It is the gentlest on-ramp and the worst place to debug something subtle, because it hides the machinery that the debugging needs.

**The three things a library gives you.** Tensors, gradients, layers. If a learner can name those three, they understand what a library *is* rather than memorising brand names.

**Ecosystem lock-in.** Weights, tokenisers and training scripts are packaged per library. Moving a model between them is possible but is real work, which is why teams pick one and stay.

### How it connects to the rest of the framework

`TSC7-Basic-K1` gives you the architecture you are about to implement. `TSC7-Basic-K7` (optimisation) is really the optimiser object inside this library. `TSC7-Basic-K10` (parallel training) is configured through this library's distributed module. `TSC5-Basic-K1` covers the same three names from the evaluator's side; here you actually run them. And `TSC7-Basic-A2`, implementing a model from an existing architecture, is unthinkable without one of these.

### What is current as of November 2026

Two shifts matter. First, **PyTorch is the de facto standard for anything you download and adapt**. Open-weight families — Llama, Qwen, Mistral, SEA-LION — publish PyTorch checkpoints and a `transformers`-compatible config, and the fine-tuning ecosystem (PEFT, TRL, Unsloth, Axolotl) is built around it. Second, **Keras has become a genuine multi-backend layer**, so "Keras" no longer implies TensorFlow underneath. TensorFlow remains strong where models are served at scale inside a product, especially on mobile and edge hardware.

For a Basic class the honest framing is: learn PyTorch enough to read a training script, learn the *idea* of TensorFlow serving, and treat Keras as the quick way to sketch an idea. You will not write a library. You will spend your life reading other people's.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"TensorFlow and PyTorch are different AI models."* They are workshops. The same architecture can be built in either.
- *"Keras is a separate library from TensorFlow."* Historically it was a wrapper on top; now it can sit on several backends. Either way it is a layer, not a competitor to the model.
- *"Learning the library is the hard part."* The library is a weekend. The hard parts are data, evaluation and knowing what "good" looks like.
- *"If it runs in Colab, it will run in production."* Colab hides version conflicts that appear the moment you install on a real server.

## How a student should understand it

**Mental model:** three brands of power tool in a renovation workshop. All three drill a hole. One is what every contractor on site uses (PyTorch), one is built for fitting the cabinet permanently into the flat (TensorFlow), and one is the cordless driver you reach for when the job is small (Keras).

**Three things they can do after this bullet:**
1. Open a Hugging Face model card and say which library the weights need.
2. Name the three things every library provides — tensors, gradients, layers — without notes.
3. Choose a library for a stated job: fine-tune an open model, serve a model on a phone, sketch an architecture quickly.

**Misconceptions to kill:** that libraries are models, that you must learn all three, and that the choice is permanent.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Three brands of power drill.** A contractor does not own three brands out of loyalty; they own the one the site uses. The bits mostly fit, the batteries do not. Swapping libraries mid-project costs you the batteries — the trained weights and the scripts.

**The kitchen and the recipe card.** PyTorch is a professional kitchen where you plate every component yourself. Keras is a recipe card that says "add the sauce" and assumes you have the sauce. When the dish tastes wrong, the professional kitchen lets you taste each component; the recipe card does not. That is the debugging trade, and it breaks only for people who never need to debug.

### Worked example with a real tool

In Colab, run this and read the output together. It is three lines and it answers "which library am I in?":

```python
import torch, tensorflow as tf
print("torch", torch.__version__, "cuda:", torch.cuda.is_available())
print("tf", tf.__version__, "gpus:", len(tf.config.list_physical_devices("GPU")))
```

Then load the same model both ways: `transformers` gives you a PyTorch model by default, and `tf.keras` can import a converted version. Point at the version numbers and the `cuda: True` line, and say: this is why the tutorial you followed last year no longer works.

What to point at afterwards: the library name in the first column of a Hugging Face model card, and the `library_name` field in its metadata. Two lines, and the learner can now classify any model they meet.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — paste a broken install error on screen and ask the room what they would do. Let the panic settle, then name it.
2. **State the objective** — by the end you can say which library a model needs and why the choice is not arbitrary.
3. **Recall prior learning** — they met these three names in TSC #5 as evaluation vocabulary. Now they are the tools.
4. **Present the content** — tensors, gradients, layers; then one word per library: research, production, approachable.
5. **Guide** — run the version-check cell together and interpret each line.
6. **Elicit performance** — pairs open two model cards and report the library, the model type and the weight format.
7. **Give feedback** — correct anyone who reads "safetensors" as a library; it is a file format.
8. **Transfer** — each learner writes the one library their organisation already standardised on, or notes that nobody has decided.

## What the framework doesn't mention but trainers need to know

- **Hugging Face is the actual hub, not a library.** Most learners will meet `transformers`, `datasets`, `peft` and `accelerate` before they meet raw PyTorch. Name the platform early or the ecosystem feels arbitrary.
- **Version mismatch is the number one beginner failure.** `pip install` today produces a different stack from the tutorial's. Teach learners to pin versions, and to read the top of any requirements file.
- **GPU access is the gatekeeper.** Colab's free tier is enough for a small fine-tune and not enough for a serious one. Say so before someone books a week of work on a free tier.
- **Nobody is loyal.** Library choice is a function of what the weights are published in. Do not teach brand preference.

## Watch out

- **Do not turn this into an install tutorial.** Ten minutes of pip errors will consume the session and teach nothing durable.
- **Do not claim one library is "better".** Say what each is better *at*, or you will be quoted as a partisan.
- **Do not skip the "library is not a model" correction.** It is the single most common confusion at this level and it survives into job interviews.
- **The stale claim to retire:** "Keras is just a wrapper on TensorFlow." In November 2026 it is a multi-backend layer, and the sentence now marks you as out of date.
