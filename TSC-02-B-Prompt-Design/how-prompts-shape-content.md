---
id: 02.01.B.K2
tsc: 2
level: Basic
code: K2
title: How prompts shape content
---

# How prompts shape content

> **TSC #2 Prompt Design · Basic · Knowledge K2**

> **Framework text (verbatim):** "Principles of how prompts shape AI-generated content."
>
> **TSC #2** Prompt Design · **Basic** · Knowledge · Bullet 2 of 15

**One-line version:** A prompt does not place an order; it tilts a set of odds, and every word you add tilts them somewhere.

## What it is

The words in a prompt change what the model produces next. Two things do the shaping: the instruction, which tells the tool what kind of answer to aim for, and the context — the facts, notes or source text you supply — which gives it something to answer *with*. Neither guarantees the result. The same prompt run twice can give two different replies, so the output still has to be checked against what you asked and what you supplied.

## Deep expansion

### The concept

The teaching point that unlocks this bullet is mechanical, and it takes one sentence: the model is predicting the next piece of text, then the next, each one conditioned on everything above it. Your prompt is that conditioning. So a prompt is less like a form submitted to a clerk and more like the opening bars of a song — the model plays the continuation it has heard most often after those bars.

Three practical consequences follow, and every other principle in this bullet is one of them.

**Specificity narrows the odds.** "Write an update" opens onto thousands of plausible continuations. "Write a two-sentence update for visitors, mentioning only these two facts" collapses that space to a handful. The mechanism is probability, not obedience; but the observable effect is the same and it is what learners need.

**Order changes weight, not just content.** Material at the start and at the very end of a long prompt gets attended to more strongly than material buried in the middle. A limit stated once at the top of a two-page paste is a limit the model may be effectively ignoring by the time it reaches the end. Practical rule: put the big source text in the middle, and repeat the crucial instruction after it.

**The output is a sample, not a calculation.** Nothing in the process guarantees that identical input gives identical output. Two runs can differ in wording, in sentence count, occasionally in which detail they lead with. This is not a fault to be fixed; it is a property to be designed around — which is why "check it" is a competency in the framework, not a courtesy.

### The sub-concepts

**Instruction versus context.** The instruction shapes *form* — length, tone, structure, what to include. The context shapes *substance* — the facts the answer is built from. Weak prompts usually fail on one of the two, and it is worth teaching learners to diagnose which: a beautifully formatted answer with the wrong date is a context failure; a factually complete answer in five paragraphs when you asked for one is an instruction failure.

**In-context learning.** Inside one conversation the model picks up a pattern from what you have shown it — a house style, a labelled example, a rule you invented for this task. Nothing is being learned permanently; the pattern lives only in that window. This is why a chat can be "taught" your format in three lines, and why a new chat forgets it entirely.

**Words carry neighbourhoods.** "Act as a compliance officer" pulls in the vocabulary of compliance writing; "give me some advice" pulls in the vocabulary of a forum post. The difference is not intelligence, it is which region of the training data you pointed at.

**Small changes compound.** Because each generated word becomes part of the input for the next, a one-word difference can change the first sentence, which changes the second, until by the end of a paragraph the two replies are unrelated in tone. Learners read this as randomness. It is drift, and it is why single-word comparisons in class are so convincing.

### How it connects to the rest of the framework

`TSC2-Basic-K7` is the concept this mechanism serves; `TSC2-Basic-K5` supplies techniques that exploit it (examples, instructions, sampling settings); `TSC2-Basic-K3` shows the mechanism operating differently across output modes; `TSC2-Basic-K4` is what to do when the shaping fails; `TSC2-Basic-A8` turns the one-word comparison into a method.

### What is current as of November 2026

Two changes matter here. First, the strongest 2026 models — OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon — hold far more context than their predecessors, which makes the ordering effect more visible, not less: the longer the window, the more a mid-document instruction gets diluted. Second, the newest reasoning-tuned models often do substantial internal work before emitting anything, so prompts that once needed "explain your steps" now often produce tighter answers without it.

### Common misconceptions

- *"The prompt is an instruction the model chooses to follow."* It is a continuation cue. Compliance is a trained habit, not a decision.
- *"Context is optional if the instruction is clear."* Clear form with no substance gives you a well-shaped answer about nothing in particular.
- *"Same prompt, same answer."* Not with chat tools. Expect variation and check accordingly.
- *"If the notes are in the prompt, the reply will use them."* Notes can be dropped, half-used, or supplemented with plausible invention. Reading the reply against the notes is the only way to know.

## How a student should understand it

**Mental model:** phone predictive text, taken seriously. You type three words; the keyboard offers what usually comes next. Now imagine the keyboard has read most of the internet and remembers a hundred thousand words of context instead of two — same mechanism, vastly better guesses.

**Things they can do after this bullet:**
1. Point to the instruction and the context in any prompt, including their own.
2. Predict what will change in an output when one instruction changes.
3. Explain, in one sentence, why two runs can differ.

**Misconceptions to kill:** that the model obeys rather than continues; that context is optional; that a repeat run should be identical.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The kopitiam order.** "Kopi, less sugar, iced, takeaway" gets you a specific drink. "Something cold and not too sweet, I'm quite sleepy today" gets you whatever the uncle thinks you mean, and he will not ask twice at 12.30pm. Where it breaks: the uncle has professional judgement and 20 years of experience; the model has statistics and no memory of you.

### Worked example with a real tool

Run A and B in two separate fresh chats with the same tool:

```text
Write a one-sentence update for visitors using only these invented notes. Mention both details.

Notes: The Oak Room opens on Tuesday at 10:00. Entry is free.
```

```text
Write a two-sentence update for visitors using only these invented notes. Mention both details.

Notes: The Oak Room opens on Tuesday at 10:00. Entry is free.
```

What to point at afterwards: one word differs — "one" to "two" — and the notes are identical. Count the sentences in each reply and check the room, day, time and price against the notes. Then ask the room to predict what would happen if you changed "visitors" to "staff", and run it. The prediction being roughly right is the lesson: prompts shape content in ways you can reason about, not in ways you have to memorise.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If you need a notice about a room opening, what details would the writer need?" Take two answers, then ask how a limit on length would change the notice.
2. **State the objective** — by the end you can identify the instruction and the context in a prompt, and explain why a clear request still needs checking.
3. **Recall prior learning** — what happened in the last exercise when the brief was thin; connect to the same mechanism.
4. **Present the content** — the model continues your text; instruction shapes form, context shapes substance; order matters; output varies.
5. **Guide** — run A and B together on screen, count sentences, compare facts with the notes.
6. **Elicit performance** — pairs run A and B, then design a third variant changing one further element and record the result.
7. **Give feedback** — debrief the mismatches: which were instruction failures, which were context failures, which were just variation.
8. **Transfer** — each learner names one instruction they will start adding to their own requests (a length, a reader, a ban on invention).

## What the framework doesn't mention but trainers need to know

## Watch out

- **Do not change several things at once.** One word, one run, one observation — otherwise the room learns nothing and the demo teaches confusion.
- **Do not let "use only these notes" stand unverified.** Show a reply that added a detail anyway, if one appears; if not, say plainly that the sentence reduces but does not remove the risk.
- **Do not demo on a live customer document.** Invented notes are enough for the mechanism and keep the privacy lesson clean.
- **The stale claim to retire:** "it understands what you mean." In November 2026 it continues what you wrote, extremely well; the gap between those two descriptions is where most workplace errors live.
