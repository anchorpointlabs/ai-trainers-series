---
id: 01.02.I.K1
tsc: 1
level: Intermediate
code: K1
title: "The principles underneath the output: prediction, representation, objective, scale"
as_at: 2026-11-26
review_by: 2027-02-25
---

# The principles underneath the output: prediction, representation, objective, scale

> **TSC #1 Generative AI Principles and Applications · Intermediate · Knowledge K1**


> **Framework text (verbatim):** "Underlying principles, core concepts and theories governing generative AI."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Knowledge · Bullet 1 of 10

**One-line version:** Four principles explain almost everything a learner sees at the keyboard — the model predicts, it predicts in a space of meaning, it was trained to be average-case good, and its competence came from scale.

## What it is

The principles governing generative AI are not facts to memorise; they are a few mechanisms that let you explain behaviour you did not expect. Prediction, representation, the training objective and scale each account for a different class of failure.

## Deep expansion

### The concept

At Basic level the requirement is knowing the model predicts rather than looks up. At Intermediate level it is tracing an observation — "it keeps giving me the same three phrasings", "it forgot my instruction halfway", "it is confident and wrong on Malay names" — back to a mechanism, so you can predict the failure before you run the prompt.

Four principles carry most of the weight. **Prediction:** the model estimates a distribution over the next token given everything so far, and every output is a sample from it; nothing is retrieved unless a tool is attached. **Representation:** text and media become vectors, so meaning becomes distance — which is why an unfamiliar phrasing still works. **The objective:** training minimises average loss across an enormous corpus, optimising the typical case and sacrificing the unusual one by design. **Scale:** capability appeared as parameters, data and compute grew, buying general competence, not per-task reliability.

### The sub-concepts

**Conditioning.** Everything you type is context the distribution is conditioned on. There is no separate command channel, which is why framing and examples move output further than emphasis does.

**Average-case fit.** The model is best at what it has seen most. Dialects, small languages, house formats and one-off exceptions revert to the mean.

**Distribution, not belief.** The model has no representation of true and false, only of what usually follows what. Fluency is therefore uniform across correct and incorrect spans — the single most important fact for anyone checking output.

**Decoding.** Temperature and top-p choose how the distribution is sampled. They change variety and consistency; they add no knowledge.

### How it connects to the rest of the framework

`TSC1-Basic-K02` is the same territory at user level. `TSC1-Intermediate-K02` shows the principles inside the training pipeline; `TSC1-Intermediate-K03` shows them operating at the keyboard; `TSC1-Intermediate-K04` formalises the prediction-versus-decision split; `TSC1-Intermediate-A04` is how you test whether a change actually moved anything.

### What is current as of November 2026

Reasoning has been industrialised. The current frontier families now spend additional compute on internal deliberation before the visible answer. "It predicts the next token" remains true, but the tokens now include thinking, so behaviour looks less like autocomplete and more like a fast draft with working shown.

Representation is also multimodal at the input layer, and decoding has become a product surface: effort settings and thinking budgets are how a buyer now chooses between speed and deliberation.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It has a database and searches it."* Nothing is searched unless a retrieval tool is attached, and the apparent recall fails exactly where the pattern is thin.
- *"Higher temperature means more creative, therefore better."* It means more variance; for extraction and compliance work it is a defect.
- *"It learns from my corrections in the chat."* Nothing is written back into the weights. Memory features store notes; they do not train.

## How a student should understand it

**Mental model:** a widely read colleague answering from the average of everything they have read — including the average's blind spots — who never signals the difference between remembering and guessing.

**Things they can do after this bullet:**
1. Trace any output defect to one of the four principles.
2. Predict which parts of an answer will be reliable before running the prompt.
3. Explain to a manager why a confident answer still needs a source.

**Misconceptions to kill:** that it looks things up, that scale solves reliability, and that fluency is evidence.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Ten thousand plates of char kway teow.** A cook who has tasted ten thousand plates can reproduce the perfect average plate: right amount of sweet sauce, right wok hei, right ratio of cockles. Ask for a version nobody sells — no dark sauce, with laksa leaf — and the cook improvises something plausible and slightly wrong. Where it breaks: a real cook can taste the result. The model cannot.

**The PSLE student who only did past-year papers.** Fluent on anything shaped like a past question, shaky on the one with a twist, and unable to say "this is outside the syllabus".

### Worked example with a real tool

In a new chat, in ChatGPT or Claude:

```
Complete this sentence five different ways, each under 15 words:
"The lift upgrading at Block 123 will begin on..."
```

What to point at: the five completions share grammar and register and differ only in small details — samples from one distribution, not five ideas. Then ask the same model for a specific start date, and show the same confidence attached to a date nobody supplied.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run the five completions; ask why they all sound plausible.
2. **State the objective** — by the end you can trace an output problem to a mechanism.
3. **Recall prior learning** — the Basic idea that it predicts the next token; ask what follows.
4. **Present the content** — the four principles, one failure example each.
5. **Guide** — diagnose one real output from the room, out loud.
6. **Elicit performance** — pairs diagnose three outputs from a supplied pack.
7. **Give feedback** — debrief the hardest two, naming the principle each time.
8. **Transfer** — each learner writes the principle most likely to bite in their own work, and the check they will use.

## What the framework doesn't mention but trainers need to know

- **Tokenisation explains a cluster of odd failures.** Counting letters, reversing words, long-digit arithmetic and unfamiliar names degrade because the model sees chunks, not characters.
- **The context window is a working-memory limit.** Long inputs are attended unevenly, so an instruction at the top of a 200-page document carries less weight than the same instruction repeated at the end.
- **Sycophancy is an objective artefact.** "Are you sure?" produces agreement. Teach a re-derivation request instead.

## Watch out

- **Do not teach the maths unless asked.** Cross-entropy and logistic functions lose the room; the failing behaviour does not.
- **Do not say "it is just autocomplete" and stop there.** True, and heard as "worthless". Say what follows: fluent, fast and unverifiable without a source.
- **Do not demo temperature as a creativity dial.** Half the room will go back and set it to maximum for a compliance report.
- **The stale claim to retire:** "it was trained on the whole internet, so it knows everything." Coverage is uneven, cutoffs are real, and the thin parts are where your learners work.
