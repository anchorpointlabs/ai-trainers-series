---
id: 04.02.I.K1
tsc: 4
level: Intermediate
code: K1
title: How models work — transformers, attention, encoders and decoders
as_at: 2026-11-26
review_by: 2027-02-25
---

# How models work — transformers, attention, encoders and decoders

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K1**

> **Framework text (verbatim):** "Principles behind generative AI model operation and output generation (e.g., how model is trained, transformers and attention mechanisms, encoders and decoders in large language models, modality gap)."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Knowledge · Bullet 1 of 11

**One-line version:** A transformer reads the whole sequence at once, weighs which words matter for each word, and then predicts the next token — one token at a time, for as long as you keep reading.

## What it is

Modern generative models are **transformers**. Their defining trick is **attention**: for every position in the text, the model computes how much each other position matters, so a word's meaning is built from its context rather than from position alone. **Encoders** turn input into a representation; **decoders** generate output from one. The gap between what a model was trained to perceive and what you are asking it to perceive — text versus an image, English versus Tamil — is the **modality gap**, and it decides which model you may choose.

## Deep expansion

### The concept

Text arrives as **tokens** — sub-word chunks mapped to integers. A common English word is roughly one token; rare words, code and non-Latin scripts split into several. Everything downstream is arithmetic on those integers.

The transformer's engine is self-attention. For each token, the model asks "which other tokens should influence me, and by how much?" and blends their representations accordingly. That is how a model resolves ambiguity: the word "bank" is a river or a financial institution depending on words hundreds of positions away. There is no left-to-right reading in the attention step; the reading order comes later, from the causal mask that stops a decoder looking at tokens it has not yet produced.

Generation is autoregressive: predict a probability distribution over the next token, sample one, append it, repeat. The model has no plan and no draft buffer — the thousandth token is produced after the nine hundred and ninety-ninth, which is why long answers take linearly longer.

### The sub-concepts

**Attention costs grow with length.** Standard self-attention compares every token with every other, so doubling the input length roughly quadruples the work of reading it. This is why very long prompts get slow and expensive before they get inaccurate — and then they get inaccurate too.

**The KV cache is why chat feels fast.** Generating a token normally requires attention over everything already seen. To avoid recomputing that every step, the model stores the attention keys and values for past tokens in GPU memory. That store grows with context length and with the number of concurrent users, and it is the usual reason a server runs out of memory.

**Three architecture families, three jobs.** Encoder-only models read bidirectionally and produce dense representations — classification, extraction, reranking, embeddings for search. They cannot write fluent prose. Decoder-only models generate token by token and do all the chat, coding and reasoning work. Encoder-decoder models map one sequence onto another, which is why speech-to-text and translation still use them. A fourth variant, mixture-of-experts, is a decoder that routes each token through only a few of its sub-networks, giving big-model capability at small-model compute per token.

**Training happens in stages, and each stage leaves a fingerprint.** Pre-training on trillions of raw tokens gives knowledge and grammar. Instruction tuning on curated question–answer pairs gives assistant behaviour. Preference alignment gives tone and refusals — and an over-aligned model refuses benign requests and flatters wrong users. Reasoning training gives step-by-step problem solving at the cost of hidden tokens and latency. When you pick a model, you are picking a point in that pipeline.

**The modality gap is a design constraint, not a bug.** A text-only model trained on text has no representation for pixels or waveforms. Multimodal models are trained jointly on several modalities, which is why they preserve layout, handwriting and tone, while a stitched pipeline of separate optical character recognition plus a text model loses exactly that.

### How it connects to the rest of the framework

`TSC4-Intermediate-K3` turns these mechanics into selection knobs: modality, size, cost, features. `TSC4-Advanced-K2` goes deeper into the training stages and optimisation. `TSC4-Intermediate-K2` is where prompting meets these mechanics — you are steering a next-token predictor. `TSC4-Intermediate-A5` is the applied version: sampling settings change behaviour because of how the final distribution is sampled.

### What is current as of November 2026

Current frontier models are decoder-only at the top of every product line, with mixture-of-experts routing as the standard way to get scale affordably. Three points for this bullet:

- **Everything converged on one interface.** Text, image, audio and code now arrive at the same endpoint, and the modality gap has narrowed for the frontier products — though not closed, and not evenly.
- **Reasoning became a visible mode.** The same model can answer immediately or think first for thousands of tokens. The architecture did not change; the training and the serving policy did.
- **Context windows grew faster than effective use of them.** Longer windows are real, but attention over a huge context is expensive and unreliable in the middle. Bigger is not automatically better.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Attention means the model reads left to right, like me."* Attention is a weighting over the whole sequence; the left-to-right order comes from a mask applied during generation.
- *"The model looks up facts in a database."* It predicts tokens from learned statistical structure. There is no lookup table of truths.
- *"It counts letters, so it can spell."* Text is tokenised into chunks, so a model may never see individual letters. Ask it to spell and you are asking it to reason about something it cannot perceive.
- *"A multimodal model is just a text model with an image plug-in."* Native multimodal models share one representation space; stitched pipelines bolt on an extractor and lose what the extractor throws away.

## How a student should understand it

**Mental model:** a very well-read colleague reading your entire email at once, weighing every sentence against every other, then writing the reply one word at a time without ever going back.

**Things they can do after this bullet:**
1. Explain attention in one sentence, without jargon.
2. Say which architecture family fits a task: classify, generate, or map one sequence to another.
3. Explain why a text-only model is the wrong instrument for an image task.

**Misconceptions to kill:** that attention is sequential reading, that the model retrieves rather than predicts, and that modality is a bolt-on.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The meeting-room whiteboard.** Everyone in the room can see the whole whiteboard at once and each person decides which parts matter to them. That is attention: simultaneous, weighted, no queue. Where it breaks: attention has a fixed budget, so a very crowded whiteboard makes everyone slightly worse at reading any single line.

**The courtroom stenographer versus the juror.** The encoder is the juror who read all the evidence and formed a view (a representation). The decoder is the stenographer writing the verdict word by word (generation). Useful for explaining why a classification model is not a chatbot.

### Worked example with a real tool

Demonstrate attention cheaply, with no maths:

```text
"The bank was steep and muddy, so we climbed it slowly."
"The bank rejected the loan, so we appealed."

For each sentence, say what "bank" means and which words told you.
```

Then ask the model to do it with a longer distractor inserted between the cue and the word. What to point at afterwards: the disambiguating word can be far from the target and still work — that is attention spanning distance. Then try the spelling test — "how many r's in strawberry?" — and let the room watch a confident wrong answer. That is tokenisation, and it is a better lesson than any diagram.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "how many r's in strawberry?" Live. Let it fail.
2. **State the objective** — by the end you can explain attention, name the three architecture families, and use the modality gap to justify a model choice.
3. **Recall prior learning** — what a token is, from the foundations course.
4. **Present the content** — tokens, attention, the KV cache, encoder versus decoder, the training stages, the modality gap.
5. **Guide** — annotate one sentence together: which words influence "bank".
6. **Elicit performance** — pairs assign four tasks to architecture families and justify each.
7. **Give feedback** — debrief, focusing on the classification tasks people instinctively send to a chatbot.
8. **Transfer** — each learner identifies one task in their work where an encoder would beat a generative model.

## What the framework doesn't mention but trainers need to know

- **Tokenisation is the hidden cost driver.** The same sentence in Tamil or Chinese can cost several times the tokens of English, which multiplies price and shrinks effective context. This is invisible in a demo and obvious on an invoice.
- **The "lost in the middle" effect is real.** Facts buried in the middle of a very long context are retrieved less reliably than facts at the start or end. Put critical instructions where the model looks hardest.
- **Small models are not failed large models.** A 300-million-parameter encoder beats a large generative model at sorting a million tickets, on every axis including accuracy.
- **The training-stage vocabulary is a selection tool.** If a model is described as base, instruct or reasoning, that tells you what it will and will not do without further prompting.

## Watch out

- **Do not teach the maths.** The room needs the shape of the mechanism, not the softmax formula. One diagram, one sentence, move on.
- **Do not claim the model "understands".** It weights and predicts. Saying otherwise sets up a trust problem you will spend the rest of the course undoing.
- **Do not use the strawberry question as a joke without the explanation.** Otherwise the room concludes the model is stupid rather than differently built.
- **The stale claim to retire:** "transformers read text in order." They attend in parallel; order is imposed by masking.
