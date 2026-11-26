---
id: 01.02.I.K2
tsc: 1
level: Intermediate
code: K2
title: "Training data, algorithm, output: the three that shape every answer"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Training data, algorithm, output: the three that shape every answer

> **TSC #1 Generative AI Principles and Applications · Intermediate · Knowledge K2**


> **Framework text (verbatim):** "Generative AI model workings, including training data, algorithms, and outputs."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Knowledge · Bullet 2 of 10

**One-line version:** Every answer is the product of three separable things — the data the model was built from, the training that shaped it, and the moment of generation — and knowing which one produced a defect is the difference between fixing it and blaming the vendor.

## What it is

A generative model is built in stages: pre-training on an enormous corpus, post-training on curated examples and preference signals, then inference at the keyboard. Each stage leaves a different fingerprint on the output, and a practitioner who can read the fingerprint knows whether the fix is a better brief, better retrieval, a different model, or a conversation with whoever owns the data.

## Deep expansion

### The concept

**Pre-training** exposes the model to text, code, images and audio at a scale no team could curate, with next-token prediction as the objective. What survives is a general statistical picture of language and of the world as described in language; what does not survive is freshness, your private knowledge, and anything the corpus covered thinly.

**Post-training** sets behaviour. Supervised fine-tuning on demonstrations teaches format and register — how to answer, how to refuse, how to structure a list. Preference optimisation teaches which of two answers people prefer, which reliably produces helpfulness and, less reliably, agreement. This is what learners mistake for "the model being smart".

**Inference** decides the remainder: prompt, attached documents, tools, memory and decoding. Most of what a learner can control lives here, and most of what they blame on the model was decided here too.

### The sub-concepts

**Corpus composition sets the centre of gravity.** English web text, code, licensed books and, increasingly, synthetic data dominate. Singapore-specific detail is thin, so the default voice drifts international unless you correct it.

**Knowledge cutoff is a data fact.** Training stops; the world does not. Anything that changed after the cutoff is answered confidently from the old distribution. A learner who cannot tell whether search ran cannot judge the answer.

**Post-training teaches the persona, including its evasions.** Hedging, apology, refusal phrasing and confident assertion are learned habits. "I don't have enough information" is an installed behaviour, not a measurement of uncertainty.

**Distillation.** A smaller student model trained on a large teacher's outputs inherits the shape of its reasoning and loses part of the long tail — which is why "small model, same family" is a reasonable first cost experiment.

**One sample is not a measurement.** The same prompt is a draw; judging a model on one output is like judging a stall on one plate from the relief cook.

### How it connects to the rest of the framework

`TSC1-Intermediate-K01` supplies the principles these stages implement. `TSC1-Intermediate-K05` goes deep on the data half; `TSC1-Intermediate-K03` covers the inference half, where prompts act. `TSC1-Basic-K03` is the product-level view of which model is which, and `TSC4` (Model Selection) is the decision this entry feeds.

### What is current as of November 2026

Three shifts. **Synthetic data** is now ordinary in post-training and increasingly used in pre-training, which raises a live question about training on model output and its long-term effect on quality — an open debate, not a settled finding, so quote no figure. **Preference optimisation has partly moved** from human raters to AI feedback and verifiable rewards on tasks with checkable answers, which makes reasoning modes stronger at maths and code than at your policy document.

And **the visible pipeline changed shape**: reasoning models insert a deliberation stage between prompt and answer, search is attached by default in consumer products, and structured outputs let a schema enforce format. A learner who assumes one undifferentiated "AI brain" misreads all three.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It was trained on everything, including our systems."* Nothing private is in the weights unless you put it there through fine-tuning or retrieval.
- *"When I correct it, it learns."* A memory feature stores text; the weights are frozen at deployment.
- *"Fine-tuning is how you teach it facts."* It reliably teaches format, tone and task shape; facts belong in retrieval, where they can be updated and cited.

## How a student should understand it

**Mental model:** a kitchen with three shifts — the supplier, the chef who sets the recipes, and the cook plating tonight's order. A bad dish can come from any of the three, and the complaint has to go to the right one.

**Things they can do after this bullet:**
1. Diagnose a defect as data, training or inference, and name the evidence.
2. Explain why the same prompt behaves differently in two products without calling either broken.
3. Choose between "add the document", "change the model" and "rewrite the prompt", with a reason.

**Misconceptions to kill:** that the model learns from the conversation, that fine-tuning installs facts, and that one output is a measurement.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT line built in stages.** Track laying is pre-training — slow, expensive, and it fixes where you can possibly go. Signalling and station fit-out is post-training — it decides how the service behaves. Tonight's journey is inference. Where it breaks: track cannot be retrofitted cheaply, whereas a model can be fine-tuned on a few thousand examples.

**The hawker supply chain.** The supplier decides what is fresh, the stall owner sets the recipe, the cook plates the order. "Less oil" is a question for the cook; "why is the fish not fresh" is a question for the supplier.

### Worked example with a real tool

Run this in ChatGPT or Claude with search off, then on:

```
Summarise what changed in Singapore's CPF Ordinary Account interest rates
over the last three years. If you are not certain about a specific year,
say so instead of guessing, and tell me which parts you could verify.
```

What to point at: without search the answer is structurally perfect and temporally unreliable — the dates carry the same confidence as the parts that are right. With search on, it carries links the learner can check. The difference is one stage of the pipeline, not intelligence. Then ask it to name its knowledge cutoff: a self-description, not a guarantee.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two answers from two products to the same prompt; ask what differs.
2. **State the objective** — by the end you can place a defect in the pipeline and pick the fix.
3. **Recall prior learning** — prediction, average-case fit, scale.
4. **Present the content** — pre-training, post-training, inference, and what each decides.
5. **Guide** — walk the CPF example with search off and on.
6. **Elicit performance** — three-stage triage: pairs assign three deliberate defects to a stage.
7. **Give feedback** — debrief, correcting every fix that is "prompt harder".
8. **Transfer** — each learner writes one line for their team: "if you see X, it is stage Y, do Z".

## What the framework doesn't mention but trainers need to know

- **System prompts and safety layers are invisible variables.** The same prompt in a consumer app, an enterprise tenant and an API behaves three ways. When a learner says "it worked at home", this is why.
- **Memory is text, not learning.** Stored notes are re-injected, and they can be stale or contradictory — a governance issue, not a convenience.
- **The corpus is a legal artefact.** Licensing and residency differ by vendor; never assert what a hosted model trained on without reading the terms.

## Watch out

- **Do not demo with search on and let the room believe it is memory.** Half of all impressive demos are retrieval wearing a costume.
- **Do not assert what is in a training set.** Nobody outside the vendor knows, and confident claims about corpus contents lose technical audiences.
- **Do not present fine-tuning as fact injection.** It is the most common expensive mistake in enterprise AI.
- **The stale claim to retire:** "the model's knowledge stops in 2023." Cutoffs have moved and are stated per model; teach learners to ask and then verify against a dated source.
