---
id: 03.02.I.K2
tsc: 3
level: Intermediate
code: K2
title: Foundation Models — definition, characteristics, limitations
---

# Foundation Models — definition, characteristics, limitations

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K2**

> **Framework text (verbatim):** "Definition and characteristics of Foundation Models and their limitations."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Knowledge · Bullet 2 of 13

**One-line version:** A foundation model is one large model trained on broad data and then adapted to many jobs by asking — which is why it is general, why it is fluent, and why it is confidently wrong about your office.

## What it is

A foundation model is a large neural network pre-trained on a broad body of text and media, then aligned to follow instructions, so that a single model can serve many unrelated tasks without retraining. You adapt it by prompting, not by rebuilding it. Its defining characteristics are generality, pattern-learning and probabilistic prediction; its defining limitations follow from the same three properties.

## Deep expansion

### The concept

The word "foundation" is architectural: it is the base layer other things are built on. Before 2018-ish, software for language tasks was purpose-built — a spam filter, a sentiment classifier, a résumé parser, each trained on its own labelled data for its own narrow label set. A foundation model inverts that. One model absorbs general patterns; the task is specified at run time, in words, by whoever is using it.

Three properties follow, and every strength and weakness in this bullet is one of them wearing a different hat:

1. **General-purpose.** It can attempt almost anything describable, which is why adoption spread through offices faster than any previous enterprise tool — and why it will attempt things it cannot do.
2. **Pattern-based.** It learns from examples, in training and in the prompt. It does not consult a rulebook; it has absorbed what usually follows what.
3. **Probabilistic.** It predicts the most plausible continuation. It does not retrieve a stored fact, check it, and then answer.

Instruction-following is a fourth, added property: after pre-training, models are fine-tuned on instruction-and-ideal-response pairs and then preference-aligned so that helpful, well-formatted, compliant answers become more probable. When a learner writes "summarise this as three bullets", they are activating patterns installed at that stage, not issuing a command to software.

### The sub-concepts

**Generalist, not specialist.** A purpose-built classifier is narrow, cheap, fast, auditable and boring: same input, same output, one label set. A foundation model is broad, expensive per call, non-deterministic and opaque. Neither is "better" — the question is whether the task boundary is known in advance. If it is, build the classifier; if the task arrives in language, you need the generalist.

**In-context learning is working memory.** Without changing a single weight, the model can pick up a new taxonomy, a house style or a rule set from material placed in the prompt. That is why prompting works at all — and why the prompt is temporary. Close the chat and the model has learned nothing.

**Knowledge has a date and a shape.** What the model "knows" is compressed from its training corpus, so it is stale by construction and lossy in detail. It is strong on widely written-about things and weak on the specific, the recent and the private.

**Limits that matter in an office.** Hallucination, fluent and confident. Sycophancy, agreeing with a wrong premise to be helpful. Unreliable arithmetic — it predicts numbers rather than calculating them, so any figure that matters goes through a calculator or code. Sensitivity to wording. Non-determinism even at temperature zero, because floating-point arithmetic across parallel hardware can flip a near-tie. A context window that is finite and unevenly attended.

**The two failure shapes learners must recognise.** Wrong and hesitant (rare, easy to catch) versus wrong and polished (common, expensive). The polished kind is dangerous precisely because the model is good at the register of expertise.

### How it connects to the rest of the framework

`TSC1-Basic-K03` is the model landscape this bullet defines; `TSC1-Intermediate-K1` and `TSC1-Intermediate-K2` explain the principles and the training pipeline underneath. `TSC3-Intermediate-K4` takes the context window as a working constraint, and `TSC3-Intermediate-A5` is the practical consequence: different models need different prompting because their post-training differs.

### What is current as of November 2026

The frontier has converged on capability and diverged on economics. The GPT-6 generation (Astra, Sol, Luna, then 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon all handle text, image, audio, files and code in one surface, all use tools, and all offer long context. Differentiation now sits in reliability on hard tasks, price per token, context size, latency and deployment posture rather than in "can it".

Three teaching-relevant shifts:

- **Reasoning tiers are a separate product decision.** A deliberating model is slower and dearer per answer; for classification and extraction the fast tier is usually the right call. Learners who always reach for the biggest model are paying for deliberation they do not need.
- **Open-weight models are close enough to matter.** For narrow, high-volume jobs, a small fine-tuned model can match a frontier model at a fraction of the cost, which makes "which model" a genuine engineering question rather than a brand question.
- **The limits have not moved.** Better models hallucinate less on well-covered topics and just as fluently on the obscure. Grounding, escape hatches and human checking remain the controls, not model choice.

### Common misconceptions

- *"Foundation model means any AI."* A rules engine, a recommender and a small classifier are AI and are not foundation models.
- *"It looks things up."* It predicts. Products that search are adding retrieval around the model; the model itself is not a database.
- *"It will get better at our work the more we use it."* Not without fine-tuning or retrieval. Each conversation starts from the same weights.
- *"Bigger is always better."* Bigger is more capable and more expensive. For a fixed extraction task, the small model with a tight schema often wins on both cost and consistency.

## How a student should understand it

**Mental model:** a first-class honours graduate on their first morning — widely read, quick, eager to please, no knowledge of your department, and no memory of yesterday. You would not let them send a client email unread, not because they are slow, but because they do not know what you know.

**Things they can do after this bullet:**
1. Define a foundation model in one sentence and name three tools built on one.
2. Point at a live output and name which characteristic produced it — generality, pattern-matching or prediction.
3. Name the limitation behind a specific failure they have seen, and the control that would have caught it.

**Misconceptions to kill:** that it is a search engine; that it learns from use; that a fluent answer is a checked answer.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The Swiss Army knife versus the can opener.** The foundation model has a blade, a corkscrew and a tiny saw; it will open a can, badly, and cut your finger. The purpose-built classifier is the can opener: one job, no drama, done in half a second. Where it breaks: a Swiss Army knife does not confidently invent a new tool, and a model will.

**The generalist clerk from HQ.** Sent to your branch for a week, well-read, no local knowledge. Ask for "the usual monthly report" and you get a beautifully formatted report about the wrong things — because "the usual" was never in the briefing. Where it breaks: the clerk would ask; the model, trained to be helpful, guesses.

### Worked example with a real tool

Give the room one task with three observable properties:

```text
Our department spent $48,300 on travel across 37 trips last quarter.
What was the average cost per trip, and what are three ways to cut it by 15%?
```

Run it in ChatGPT, Claude or Gemini. Then check the arithmetic yourself, or ask the same model in a fresh chat. Point at three things in order: the fluency (characteristic: prediction), the arithmetic (limitation: it predicts numbers — the fix is a calculator or code tool), and the generic suggestions (limitation: no knowledge of your department — the fix is context, not a better model). One prompt, three properties of foundation models, visible on screen.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room to name the AI in their phone keyboard's next-word suggestion. Same mechanism, smaller.
2. **State the objective** — by the end you can define a foundation model and name the limitation behind any failure we see today.
3. **Recall prior learning** — what did they learn about generative versus discriminative models, or about training data?
4. **Present the content** — the definition, the four properties (including instruction-following), then limits with a live failure.
5. **Guide** — run the travel-spend prompt together and label what they see.
6. **Elicit performance** — pairs take a tool they use daily and write one characteristic and one limitation visible in it.
7. **Give feedback** — collect three answers, correct the ones that describe a product feature rather than a model property.
8. **Transfer** — each learner writes the one control (grounding, escape hatch, calculator, human check) they will add to their next prompt.

## What the framework doesn't mention but trainers need to know

- **The limits are not bugs awaiting a patch.** They are consequences of the design. Teaching them as temporary invites learners to wait instead of to control.
- **"Foundation" implies dependency.** Choosing a model is choosing a supplier: price changes, deprecations and drift arrive on someone else's schedule. Intermediate learners should hear about model pinning now, not in an engineering course.
- **Reasoning models change the failure profile.** They are better at multi-step logic and worse at being cheap or fast, and their visible explanations are not guaranteed to be the actual cause of their answer.
- **Non-determinism is a feature of the hardware, not a setting.** Temperature zero reduces variation; it does not guarantee identical output, which matters for anyone planning to certify a process.
- **Model choice is a risk decision, not only a quality one.** Where the data goes, who can see it, and what the provider retains are questions the prompt cannot answer.

## Watch out

- **Do not say "it understands".** Say it predicts, and show the failure that proves the difference. "Understands" gets repeated to a regulator.
- **Do not teach a leaderboard.** Rankings move monthly and mostly measure benchmarks, not your task.
- **Do not demo a hallucination as a joke.** Demo it as a control problem, with the fix in the next slide, or you teach cynicism instead of practice.
- **The stale claim to retire:** "the model has read the whole internet, so it knows everything." It has absorbed a compressed, dated, partial sample of what was written — and it has no idea what it does not know.
