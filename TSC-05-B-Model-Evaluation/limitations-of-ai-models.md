---
id: 05.01.B.K4
tsc: 5
level: Basic
code: K4
title: Limitations of AI models in generating relevant outputs
as_at: 2026-11-26
review_by: 2027-02-25
---

# Limitations of AI models in generating relevant outputs

> **TSC #5 Generative AI Model Evaluation · Basic · Knowledge K4**


> **Framework text (verbatim):** "Limitations of AI models in generating relevant outputs."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Knowledge · Bullet 4 of 11

**One-line version:** A model does not know what is relevant to your situation — it only knows what is statistically likely, and the gap between "likely" and "relevant to you" is where almost every real-world failure lives.

## What it is

AI models have hard limits on producing output that is *relevant* — correct for this person, this company, this moment. The limits come from what the model actually is: a pattern predictor trained on general data, with no access to your context unless you give it, and no built-in awareness that it is wrong. This bullet is about naming those limits precisely so they can be evaluated against.

## Deep expansion

### The concept

The core limit is a mismatch of definitions. The model optimises for *plausible continuation*; the user needs *relevant* — factually right, situationally appropriate, and complete against the actual task. Those two things overlap often but not always, and when they diverge the model produces fluent, confident, irrelevant output. Evaluation of a model is therefore partly evaluation of *this gap*: given a real task, how often does "likely" land on "relevant"?

### The sub-concepts

**Hallucination.** The model invents facts — a citation that does not exist, a policy that was never written. It is the flagship failure of relevance because the output is confident and wrong, which is worse than silent.

**No memory of you.** A model does not know your customer, your SOPs, your constraints — unless you put them in the prompt or connect a retrieval system. Its "relevance" is to the average, not to you.

**The context-window limit.** There is a hard cap on how much it can hold in one exchange, and relevance degrades toward the middle and edges of a very long input. You cannot dump an entire file room in and expect it all to matter.

**Staleness.** A model's training has a cutoff. Anything after it — today's price, last week's policy — it does not know, and it will not reliably tell you it does not know.

### How it connects to the rest of the framework

This bullet is the *why* behind the whole evaluation discipline. `TSC5-Basic-K2` (the criteria) is how you catch relevance failure; `TSC1-Basic-K6` (limitations of AI models, the principles-level version) is the same idea one level up; `TSC5-Basic-A4` (identify limitations and biases) is the ability to spot it in a live output. And `TSC4-Intermediate-K1` (how models work inside) explains *mechanically* why the limits exist.

### What is current as of November 2026

The limits have narrowed but not vanished. Late-2026 models hallucinate less than their 2024 ancestors and cite sources more often — but the *relevance* limit is unchanged: a frontier model with no access to your data is still guessing about your business. The frontier has also introduced a new wrinkle: **reasoning models are slower to produce an answer**, which is a relevance limit of a different kind — an answer that arrives after the meeting is over is not relevant, however correct. And "long context" marketing still misleads: a 1-million-token window does not mean the model *uses* the middle of it reliably.

### Common misconceptions

- *"If it sounds confident, it's relevant."* Confidence is the model's default register, not a signal of correctness.
- *"It searched the web, so it's current and relevant."* Some products search; generation and retrieval are different mechanisms, and a cited answer still needs checking.
- *"Bigger model = always more relevant."* A bigger model is more fluent and more knowledgeable in general, but relevance to *your* task is driven by the context you give it, not by parameter count.

## How a student should understand it

**Mental model:** a brilliant consultant who has read everything ever published, has never set foot in your company, and will not admit when they are guessing. Everything they say is plausible. Whether it is *relevant* is your job to check.

**Three things they can do after this bullet:**
1. Name the three most likely relevance failures (hallucination, no context, staleness) and give an example of each from their own work.
2. State what a model *cannot* know about their job, in one sentence, before generating anything.
3. Check any output for "is this right *for us*, not just plausible *in general*?"

**Misconceptions to kill:** confidence = correctness, "it searched so it's current", and bigger = more relevant.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tour guide who never visited.** You hire a guide in a foreign city who has memorised every guidebook ever written but has never been there this week. She speaks beautifully about the famous hawker centre — and confidently sends you to one that closed two years ago. Her knowledge is real; her relevance is broken. The model is that guide.

**The polyclinic triage.** The framework-adjacent analogy: a general practitioner is excellent and fast, but she does not know your full history unless you tell her. Give her the wrong history and her advice is confidently irrelevant. The model's relevance is only as good as the context you supply.

### Worked example with a real tool

Ask a model for an answer that *requires* information it does not have, then watch it invent it:

```
What is the name of my company's primary bank, and what is our current
account balance?
```

What to point at afterwards: if you gave the model no such information, a strong model may still produce a plausible bank name and a plausible number rather than saying "I don't know". That is hallucination in one line — and the demonstration of why relevance must be checked against ground truth you actually hold. (For the careful version, feed it a real fact first, then ask it to *use only* that fact, and show it straying anyway.)

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show one confident, specific, completely invented answer and ask the room how many would have believed it.
2. **State the objective** — you will name the limits on relevance and check any output against them.
3. **Recall prior learning** — they just learned the four criteria; relevance failure is accuracy plus context failure.
4. **Present the content** — hallucination, no-memory, staleness, context limits.
5. **Guide** — run the bank-balance exercise live and let them catch the invention.
6. **Elicit performance** — each learner writes one thing the model cannot know about their job, then asks it anyway and checks.
7. **Give feedback** — separate "wrong" from "not given the context to be right" — a key distinction learners blur.
8. **Transfer** — tomorrow, before trusting an output, ask: "does the model have the information to make this relevant?"

## What the framework doesn't mention but trainers need to know

- **Relevance failure is usually a context failure, not a model failure.** When a learner says "the model was wrong", the trainer's first question should be "what did you give it to work with?" Half the time the model never had the information.
- **The "I don't know" absence.** Models rarely volunteer that they lack information; they answer anyway. Teaching learners to *expect* an answer and *demand* the basis is the single most transferable habit.
- **Relevance is time-sensitive.** A correct answer that arrives late, or a general answer to a specific question, is a relevance failure even with zero hallucination. Fold this into the definition or learners will miss it.

## Watch out

- **Do not demo only hallucination.** The relevance limit is broader: staleness, missing context, and slow reasoning models are all relevance failures with no hallucination at all. Teach all of them or the learner walks away thinking "just check for made-up facts."
- **Do not overclaim the fix.** Retrieval and fine-tuning reduce some limits and introduce others (a retriever that pulls the wrong document produces confidently relevant *wrong* answers). Do not promise a model that is always relevant.
- **The stale claim to retire:** "just give it more context and it will be relevant." More context can *reduce* relevance — the model loses the thread in the middle of a huge prompt, and cost and latency rise. Relevance is an engineering problem, not a volume problem.
