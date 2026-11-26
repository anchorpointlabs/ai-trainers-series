---
id: 01.01.B.K2
tsc: 1
level: Basic
code: K2
title: Fundamental concepts and theories of generative AI
---

# Fundamental concepts and theories of generative AI

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K2**

> **Framework text (verbatim):** "Fundamental concepts of and theories governing generative AI."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 2 of 13

**One-line version:** A generative model is not programmed with rules and does not look anything up — it has absorbed statistical patterns from an enormous body of text and media, and it produces the most probable continuation of whatever you give it.

## What it is

Generative AI rests on three ideas a non-specialist can hold at once: learning from examples rather than instructions, probability rather than retrieval, and neural networks as the machinery that stores the patterns. Nothing here needs calculus. What the learner must be able to do is explain why a model that has never seen their company can write about it fluently — and why the same model will state a false fact with total confidence.

## Deep expansion

### The concept

Traditional software is instructions: if this, then that, written by someone who knew the rule. A generative model is a set of **weights** — numbers adjusted during training — encoding how words, pixels and concepts tend to co-occur. Nobody wrote the rule for "a job posting sounds warm but professional"; the model saw thousands of examples and the pattern settled into the numbers.

Hence the property to teach first: the model **predicts**, it does not **retrieve**. It computes a probability distribution over what should come next and samples from it. When the sample is right, the pattern held. When it is wrong, the wrongness is grammatical and confident, because fluency and truth are produced by different things.

Two phases, which learners routinely collapse. **Training** happens once, offline: the model reads a frozen snapshot of text and media up to a cutoff and adjusts its weights. **Inference** happens every time someone presses send: those weights, unchanged, predict. In between sits **post-training**, where human raters reward helpful, well-formatted answers — which is why a raw text predictor behaves like an assistant.

### The sub-concepts

**Tokens, not words.** The model reads chunks of roughly three-quarters of a word. That one fact explains a family of failures that otherwise look like stupidity: it cannot count letters reliably, cannot hit an exact word count, and both its memory limit and its price are counted in tokens.

**Probability and sampling.** Output is a distribution. A hidden setting — temperature — controls how adventurous the sampling is; consumer products hide the dial, but the behaviour shows: ask the same question twice and the answers drift. That drift is the mechanism, not a bug.

**Attention, and what it costs.** The modern model weighs every token against every other token in its window, which is why context matters enormously and why a very long conversation degrades rather than improves.

**Context is working memory, not learning.** Everything typed sits in the **context window**, re-read every turn and discarded when the session ends. Uploading a document does not teach the model anything; it places the document in front of it. This is the antidote to the commonest fear in a Singapore classroom — that a colleague's uploaded file has entered the model.

**Emergence is uneven.** Scale produced capabilities nobody trained: translation, summarisation, code, step-by-step arithmetic when asked to show working. But it improved plausible text faster than it improved correctness, and that asymmetry is the whole argument for the checking step in `TSC1-Basic-A02`.

### How it connects to the rest of the framework

This bullet is the mechanism. `TSC1-Basic-K03` names the models that implement it. `TSC1-Basic-K05` separates it from the predictive systems most organisations already run. `TSC1-Basic-K06` is the consequence — the failure list that follows from "it predicts". `TSC1-Basic-A02` is the human response. If a learner understands this bullet, the rest of TSC #1 reads as elaboration.

### What is current as of November 2026

- **The frontier is three families at very different prices** — OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon. Same idea, different temperament, context size and bill.
- **Post-training does much of the visible work.** The difference a learner feels between two assistants is often how eagerly it refuses, how much it flatters, whether it shows its working — trained behaviour, not architecture.
- **Reasoning traces went mainstream.** Several models expose a thinking pass before answering. Useful in class, but the trace is generated text, not a readout of the model's internals. Do not present it as the model's true reasoning.

### Common misconceptions

- *"It looks things up in a database."* There is no database of facts inside the model, only weights. That is why it can be right about a niche topic and wrong about a famous one in the same paragraph.
- *"Engineers programmed it with if-then rules."* No rule for "sound apologetic but not grovelling" was ever written. It emerged from examples and feedback.
- *"It learns from our conversation."* Within the thread, earlier text stays in the window. Across sessions the weights do not change — only an explicit memory feature or a vendor's training pipeline does anything durable, and both are policy decisions.
- *"It understands the way a person does."* It represents statistical relationships at a fidelity that can look like understanding. The distinction matters the moment a learner treats fluent tone as evidence of correctness.

## How a student should understand it

**Mental model:** a very well-read colleague who has never been to your office, has no memory of yesterday, and will never say "I don't know" unless you build the sentence for them.

**Things they can do after this bullet:**
1. Explain in one sentence why the same prompt gives two different answers.
2. Point at a sentence in an output and say whether it came from the prompt, from a pattern, or from nowhere.
3. Name the three ideas — examples, probability, networks — without jargon.

**Misconceptions to kill:** that it retrieves, that it was programmed with rules, and that fluency implies comprehension.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The student who read the whole library.** A student who has read every book in the National Library, remembers the shape of every argument, and has never met a human being. Ask for a letter to your landlord and you get something that reads exactly like one, because they have read ten thousand of them. Ask whether the landlord agreed to fix the air-con and they will guess, confidently. Where it breaks: this student never tires, never asks a question first, and is available at 2am.

**The weather forecast.** A 70% chance of rain is not a claim about the world; it is a distribution, and when it rains the forecast was not "right". Generative output works the same way — sampled once. Where it breaks: the forecast publishes its uncertainty, and a chat model states everything at the same confidence.

### Worked example with a real tool

Three steps, in any current chat product:

```text
1. In a new chat, type once:
   "Write the first sentence of a Singapore ghost story set in an HDB lift."

2. Start a brand-new chat. Type exactly the same sentence again.

3. In that second chat, add one line:
   "Now rewrite it so the lift stops at the 13th floor."
```

What to point at afterwards: the two first runs differ, in wording and often in setting — proof of sampling, not retrieval. Then the third output: the model obeyed instantly, not because it knows the building, but because "the lift stops at the thirteenth floor" is an extremely probable continuation in that genre. Probability explains both the variation and the compliance, and one demonstration covers both.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "Does ChatGPT know things the way a dictionary does?" Collect four answers, correct none yet.
2. **State the objective** — "You will explain why the same question gives two answers, and why that matters for your work."
3. **Recall prior learning** — Search: you type words, you get documents. Hold that next to what they are about to see.
4. **Present the content** — Three ideas on one slide; then training once, inference every time, post-training in between.
5. **Guide** — Run the three-step demo, narrating what you expect before each run.
6. **Elicit performance** — Pairs build their own two-run test on a task from their job.
7. **Give feedback** — Two pairs explain the difference using "predict" and "sample". Correct any answer containing "searched".
8. **Transfer** — Each learner names one task where variation is fine (brainstorming) and one where it is not (a figure for a report).

## What the framework doesn't mention but trainers need to know

- **Tokenisation explains half the "dumb" failures.** One slide on tokens buys credibility for the whole course.
- **Post-training explains the personality.** Tone is trained, not evidence about the model's mind.
- **The context window is where "it forgot" lives.** Long threads degrade; the fix is a new thread, not a better prompt.
- **Cost varies by roughly two orders of magnitude** across tiers of one vendor. For Basic learners: the biggest model is not automatically the right one.

## Watch out

- **Do not teach the maths.** No gradients, no loss functions. Every concept here survives in plain language.
- **Do not demo "it learns from you".** A learner who believes the conversation trains the model will reason wrongly about privacy for the rest of the day.
- **Do not say "it thinks".** "It predicts" is accurate and does not sound dismissive; "it's just autocomplete" is dismissive and now inaccurate.
- **The stale claim to retire:** "generative AI is a parlour trick that cannot do real work." In November 2026 it drafts, summarises, codes and acts. The honest caveat is verification, not capability.
