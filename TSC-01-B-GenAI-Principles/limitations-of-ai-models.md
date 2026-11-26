---
id: 01.01.B.K6
tsc: 1
level: Basic
code: K6
title: Limitations of AI models
as_at: 2026-11-26
review_by: 2027-02-25
---

# Limitations of AI models

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K6**

> **Framework text (verbatim):** "Limitations of AI models in generating relevant outputs."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 6 of 13

**One-line version:** The failure that matters is not "wrong" — it is *fluently* wrong: an answer that reads as relevant, matches the brief in tone, and contains a fact, a figure or a citation that does not exist.

## What it is

Generative models fail in a small number of predictable ways, and each one follows from the mechanism in `TSC1-Basic-K2`: they predict probable text rather than retrieving verified facts. The framework's key word is **relevant** — output can be grammatical, on-topic-looking and well-formatted while failing to answer the actual question or match the actual facts. Learners need the list, the mechanism behind each item, and a detection habit.

## Deep expansion

### The concept

Learners arrive with two opposite errors. Some think the model is a search engine with a voice, so a confident answer must be sourced. Others think it is a toy, so nothing it says needs checking. One observation refutes both: **the model has no separate confidence signal**. It produces a true statement and a fabricated one in the same register, the same punctuation, the same paragraph.

So the limitations are not bugs awaiting a patch. They are the shape of the instrument. A ruler is not "limited" because it cannot measure weight; it is the wrong tool, and knowing that is competence. The complication here is that the model *looks* like a general tool, which is exactly why the specific limits have to be taught.

### The sub-concepts

**Hallucination, of two kinds.** *Extrinsic* invents something that exists nowhere: a citation, a statute section, a statistic, a URL. *Intrinsic* misreads a document you supplied: the source says revenue grew 12% in software while hardware fell 4%, and the summary says hardware grew 12%. The second is more dangerous in an office because it looks grounded — the user supplied the source and assumes the answer is inside it. The mechanism is the same: the model produces what a correct answer would *sound like*.

**Stale knowledge.** Training stops at a cutoff, and a search layer does not fully repair it: the model's patterns pull toward the past, and a three-year-old article gets summarised in the present tense. Anything with a date attached — rates, thresholds, grant rules, leadership, software versions, prices — is checked at source.

**No understanding.** The model represents statistical relationships at a fidelity that often looks like comprehension. It has no model of your business, your intent or the consequence of being wrong. That is why it will produce a flawless plan for a business that cannot exist, and why it never says "this premise is wrong" unless asked.

**Weakness at exact operations.** Counting, arithmetic in prose, character-level tasks and exact length constraints fail because the model works in tokens, not characters or numbers. It gets them right only when it delegates to a tool — a code interpreter, a spreadsheet, a calculator — and the learner should look for the evidence that it did.

**Context degradation.** Long threads and large uploads degrade. Attention is strongest at the start and end of the input, so early instructions get forgotten and middle facts get missed; in consumer interfaces, exceeding the window can silently drop the earliest turns. The failure looks like carelessness; it is arithmetic.

**Sycophancy.** The model is trained, in part, on human approval. Push back and it often agrees — including when it was right. "Are you sure?" therefore tests agreeableness, not accuracy, and a learner who uses it as verification has built a ritual.

**Uncalibrated confidence.** No hedging unless prompted. The prose does not report uncertainty because fluency is what was optimised, which is what makes the other failures expensive: a hesitant wrong answer gets checked, a confident one gets forwarded.

**Prompt injection.** Text inside a document, email or web page can carry instructions the model treats as its own. To the model, system instructions, your message and pasted content are one stream of tokens. This becomes a live risk the moment it has tools and can act.

**Relevance failure.** The framework's specific concern, in four shapes: answering the general question instead of the specific one; answering for the wrong audience; answering at the wrong scope (a summary when a decision was needed); omitting the constraint that mattered ("under 100 words", "no jargon"). All four pass a spell-check and fail the brief.

### How it connects to the rest of the framework

`TSC1-Basic-K2` is the cause. `TSC1-Basic-K4` turns these failures into a fit decision. `TSC1-Basic-A02` is the response — the accuracy and relevance check, which is the practical half of this bullet. `TSC1-Basic-A05` asks who is accountable when the check fails. At Intermediate the same list reappears as guardrail design.

### What is current as of November 2026

- **Hallucinated citations remain the most common serious failure in professional use.** Better models made them more convincing, not rarer. A bibliography, a case citation or a regulation section number is never evidence until it is opened.
- **Closed-world grounding reduced the problem where it is used.** Products that answer strictly from a supplied document set — Google's NotebookLM is the clearest example — refuse when the answer is not in the sources. That trades coverage for verifiability, and it is worth teaching as a design choice.
- **Agents added a failure class that did not exist before.** A wrong sentence is embarrassing; a wrong write action — a sent email, an updated record, a merged pull request — is a state change. That is why the agentic governance framework exists.
- **Reasoning modes improved multi-step logic, not freshness or truth.** A model that shows its working is easier to audit and still capable of building a flawless argument on a fabricated premise.

### Common misconceptions

- *"It reads confidently, so it is probably right."* Confidence is a style, not a signal; it is identical across true and invented claims.
- *"Asking 'are you sure?' checks it."* It tests sycophancy. Use a source.
- *"I uploaded the document, so the answer is grounded."* Uploading places the document in the window; it does not stop the model misreading it or blending in its own assumptions.
- *"The errors are random, so retrying will converge on truth."* Errors are systematic — the same invented pattern recurs. Retrying gets you a different confident answer, not a verified one.

## How a student should understand it

**Mental model:** a witness who has read everything and seen nothing. Fluent, cooperative, and with no way to distinguish a memory from a plausible reconstruction — and no tell in their voice when they do it.

**Things they can do after this bullet:**
1. Name the four failures they are most likely to meet and give a work example of each.
2. Read a generated paragraph and mark every sentence that requires verification before use.
3. Explain why "check against the source" is not optional, in terms of the mechanism rather than trust.

**Misconceptions to kill:** that fluent means true, that "are you sure?" is a check, and that uploading the document settles the grounding question.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The witness who has read every newspaper.** This witness can describe any incident in perfect detail — the date, the weather, the exact quote from the minister. But they were never there, and they have no memory of not being there. When they are right, the pattern held. When they are wrong, they are just as calm. You would not put them on the stand without corroboration, however compelling they sound.

**The GPS with no signal that never says "I am guessing".** It keeps giving directions, the arrow moves, and you only discover the problem when you arrive somewhere that is not your destination. That is uncalibrated confidence, and it is why the check happens before the output is used, not after.

### Worked example with a real tool

Type this exactly, then verify at the source:

```text
How many public libraries are there in Singapore, and which one is the
largest by floor area? Give the exact figures, and cite the source and
the date of the source for each figure.
```

What happens: the model gives specific numbers and often names a source. Now open the National Library Board website and check. In most runs at least one figure is wrong, a source is invented or misattributed, or a true figure is attached to the wrong library. Point at three things — the confidence of the phrasing, the presence of a citation that looks real, and the distance between "cited" and "verified". That last distinction is what changes behaviour.

A second, cheaper demonstration of "no understanding": ask it to summarise your own document, then ask why it chose a particular structure. It will produce a fluent, plausible account of its own process that has no relationship to what happened. Thirty seconds, and the room remembers it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — Read a fluent paragraph containing one fabricated statistic and one invented citation. Ask for hands when they spot it. Almost nobody will.
2. **State the objective** — "You will name the four failures you will actually meet, and show me what you would check before using the output."
3. **Recall prior learning** — From K2: it predicts, it does not retrieve. What follows for facts?
4. **Present the content** — The list, grouped: invented, stale, uncomprehending, misaligned. One clause of mechanism each.
5. **Guide** — Run the library prompt, then verify live. Let the room watch you find the error.
6. **Elicit performance** — Pairs take a generated paragraph from their own domain and underline everything that must be checked.
7. **Give feedback** — Compare underlinings. The gap is always the number of things people assume are safe.
8. **Transfer** — Each learner writes the one check they will always perform, and for what kind of output.

## What the framework doesn't mention but trainers need to know

- **Intrinsic hallucination is the sleeper risk.** Everyone teaches invented citations; the failure that damages real work is a plausible misreading of a document the learner supplied and trusts.
- **"Grounded" is a spectrum, not a switch.** Closed-world products refuse, search-augmented products cite, and neither is verification.
- **Sycophancy is invisible in a demo.** Set it up deliberately: argue against a correct answer and let the model fold.
- **Long threads are the most common self-inflicted failure.** Teach thread hygiene as limitation management, not housekeeping.
- **The limitation list is the sales list.** Every honest vendor roadmap item is on this slide, which makes it a good client conversation rather than an embarrassment.

## Watch out

- **Do not teach limitations as a list to memorise.** Teach the mechanism once; the list follows. A learner who understands prediction can derive the failures nobody told them about.
- **Do not use "it hallucinates" as a blanket dismissal.** It also drafts, summarises and structures well. The point is which output needs which check.
- **Do not demo a failure without a fix.** A demo that ends in "so be careful" teaches fear. End in a check the learner can run.
- **The stale claim to retire:** "AI makes things up because it is still learning." It makes things up because it predicts. That will not be trained out, and the check is permanent infrastructure.
