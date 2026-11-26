---
id: 07.02.I.K1
tsc: 7
level: Intermediate
code: K1
title: Four generative concepts that decide how you build a model
---

# Four generative concepts that decide how you build a model

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K1**


> **Framework text (verbatim):** "Generative concepts (e.g., transfer learning, distillation, explainability, self-supervised learning)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 1 of 17

**One-line version:** Nobody at this level trains from zero — you borrow a model that already learned something, you shrink it, you explain it, and you know the trick that let it learn without labels.

## What it is

Four ideas explain why a two-person team can ship a generative model in 2026. Transfer learning lets you start from someone else's expensive training run. Distillation shrinks the result to something you can afford to serve. Self-supervised learning is how the base model absorbed knowledge with no one labelling it. Explainability is what you get asked for the moment the model nears a customer.

## Deep expansion

### The concept

Pre-training a frontier model costs more than most companies spend on software; one fine-tune costs a few hundred dollars of GPU time. Every practical build sits on a borrowed foundation, so these four words are the vocabulary for *what you borrowed, how you shrank it, how it learned, and how you defend it*. A learner who cannot use them precisely can follow a tutorial but cannot tell a demo from a deployed system.

### The sub-concepts

**Transfer learning.** Reusing representations learned on a broad corpus for a narrow task. Three modes by cost: *feature extraction* (freeze the backbone, train a head), *full fine-tuning*, *parameter-efficient tuning* (LoRA and relatives). Structure transfers — grammar, image statistics — not your SOPs.

**Distillation.** A large *teacher* produces outputs; a small *student* matches them, ideally the full softened distribution rather than the chosen token, because the distribution carries more signal per example. The 2025–26 variant trains the student on the teacher's reasoning trace. Failure mode: inherited confidence — the student copies the teacher's mistakes *and* certainty.

**Self-supervised learning.** The pretext task that made pre-training possible without labels: predict the next token, fill a masked span, match an image to its caption. The label is part of the input, so the corpus is the training set. Data quality becomes the only lever, and "unsupervised" never means "unevaluated".

**Explainability.** *Post-hoc* methods explain a finished output (attribution, counterfactuals, probes); *by-design* methods make behaviour auditable (constrained formats, citations, logged reasoning). Attention maps are in the first camp and weaker evidence than learners assume.

### How it connects to the rest of the framework

`TSC7-Basic-K1` supplies the architectures these concepts act on; `TSC7-Basic-K8` is the fine-tuning mechanics; `TSC7-Intermediate-K10` extends it to continuous pre-training; `TSC7-Intermediate-K6` is the full method list; `TSC5` proves any of it worked.

### What is current as of November 2026

- **Distillation is product strategy, not just compression.** The tiers inside one family — GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), the Claude 5.5 line, Gemini 3.1 Pro and Gemini 4 Argon — behave like models trained to hit different cost points. Teams now distil a small student from a strong API model rather than fine-tune a mid-size open one.
- **Self-supervision has not changed; the data mix has.** Curation and filtering are now the stated differentiator, exactly what this bullet implies downstream.
- **Explainability moved from pictures to features and evals.** Sparse-autoencoder work and systematic red-teaming displaced attention heatmaps as the credible audit; AI Verify-style governance wants documented evaluation, not saliency.

### Common misconceptions

- *"Transfer learning means the model knows my business."* It knows how language behaves. Product codes and approval flows are not in the weights.
- *"Distillation is just copying outputs."* It copies behaviour on the sampled distribution. Off it, the student drifts — confidently.
- *"The attention map shows what the model was thinking."* It is a correlation you can draw, not a causal account.

## How a student should understand it

**Mental model:** you inherit a trained chef, send him on a one-week course on your menu (transfer), have him train a junior who cooks the same dishes cheaper (distillation) from recipes he taught himself reading cookbooks (self-supervision), then write down why his laksa works (explainability).

**Three things they can do after this bullet:**
1. Choose between prompting, PEFT, full fine-tuning and distillation, and say why.
2. Explain what the base model did *not* learn from your data.
3. Say what they would accept as an explanation, and what they would reject.

**Misconceptions to kill:** that transfer means domain knowledge, that distillation is lossless, and that a heatmap is an explanation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tuition chain.** A star student who has sat the PSLE tutors a younger sibling on the same syllabus — transfer. The sibling then coaches a neighbour's child from condensed notes — distillation: cheaper, faster, and the notes carry only what the star thought mattered, misconceptions included. Where it breaks: a student asks something outside the notes and gets a confident wrong answer, as the distilled model does.

**The assessment book with answers at the back.** Thousands of questions, nobody marking each one — self-supervised learning, with the usual risk: practise from one publisher and you learn its quirks, not the subject. Where it breaks: a student can switch publishers and notice the difference; a model never sees the second publisher unless you put it in the evaluation.

### Worked example with a real tool

A learner wants replies in their company's tone. Type this into Claude, ChatGPT with code interpreter, or a coding assistant:

```
I have 800 past support replies in support_pairs.csv
(columns: customer_message, our_reply).

1. Write a Python script using transformers + peft that loads an
   open-weight instruct model, applies LoRA (r=16) to attention
   projections, and trains on these pairs formatted with the model's
   own chat template, masking loss on the prompt tokens.
2. Print the trainable-parameter percentage before training.
3. Add an eval loop that scores held-out replies by embedding
   similarity and saves the worst 20 to review.
```

Point at three things: the trainable-parameter percentage (well under one percent — transfer learning being cheap), the chat-template call (training on text the model never sees at inference is the classic silent bug), and the "worst 20" file — explainability as a workflow, not a diagram.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a working fine-tune beside its GPU bill and the cost of pre-training.
2. **State the objective** — pick and justify a build strategy in these four words.
3. **Recall prior learning** — pre-training, parameters, training data from Basic.
4. **Present the content** — each concept: what it buys, how it fails.
5. **Guide** — one learner's use case through borrow / shrink / explain.
6. **Elicit performance** — pairs sort five scenarios into prompt, PEFT, full fine-tune or distil.
7. **Give feedback** — debrief; the contested scenarios hold the learning.
8. **Transfer** — each learner writes their own strategy sentence.

## What the framework doesn't mention but trainers need to know

- **Distillation has a contract attached.** Distilling from a vendor API may breach its terms, and your data may be retained. That question lands in week one of real projects.
- **Explainability is usually documentation.** Teams satisfy audit with data lineage, eval results and known failure modes; saliency-only teaching misses the ask.
- **Transfer fails silently on domain distance.** A model pre-trained on English web text fine-tunes well on English tickets and badly on Singlish ones, and the loss curve cannot tell you which.

## Watch out

- **Do not present an attention heatmap as proof of reasoning.** An engineer in the room will dismantle it.
- **Do not teach distillation as free compression.** Without a held-out evaluation the student looks fine and fails where the teacher was uncertain.
- **Do not skip licences.** Open weights, open data and API terms are three different permissions.
- **The stale claim to retire:** "you need a research team to build a generative model." In November 2026 you need a base model, clean data, an evaluation, and someone who knows these four words.
