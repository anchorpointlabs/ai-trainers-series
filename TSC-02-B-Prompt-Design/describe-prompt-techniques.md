---
id: 02.01.B.A1
tsc: 2
level: Basic
code: A1
title: Describe prompt techniques
as_at: 2026-11-26
review_by: 2027-02-25
---

# Describe prompt techniques

> **TSC #2 Prompt Design · Basic · Ability A1**

> **Framework text (verbatim):** "Describe fundamental prompt design techniques."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 9 of 15

**One-line version:** Zero-shot and one-shot are one question and one demonstration — and describing them well means a colleague could pick the right one without you in the room.

## What it is

Describing a technique means saying what it is, when to reach for it, and what it looks like in practice, in language a colleague can act on. Zero-shot: give the task and the needed information, no worked example. One-shot: the same, plus exactly one completed example — an input and its finished output — before the real input. A second attempt at the same prompt is not an example.

## Deep expansion

### The concept

The framework asks for description, not demonstration. That is deliberate. A learner who can run a one-shot prompt has a trick; a learner who can explain *why* the example helped, and what it cost, can brief a colleague, review someone else's prompt, and decide when to drop the example. That is the competency.

A usable description has four parts, and trainers should insist on all four:

1. **What it is** — one worked example of the task, done correctly, placed before the input you want done.
2. **What it is for** — showing a format or a boundary that is hard to describe in words.
3. **What it costs** — a longer prompt, and the risk that the model copies details from the example.
4. **When not to use it** — when the instruction is already unambiguous, or when a single example would bias a judgement that needs balance.

The fourth part is what classroom descriptions usually omit, and it is what stops a team from turning one-shot into a religion.

### The sub-concepts

**Counting examples, not attempts.** The count is of worked examples inside the prompt. Running a zero-shot prompt twice is still zero-shot. The confusion arises because both actions feel like "giving it another go".

**A worked example has both halves.** An input alone is a task; a finished output alone is a template. Only the pair demonstrates the transformation — which is why a "sample" pasted without its result teaches nothing reliable.

**The new input is not the example.** In the prompt below, the Cedar note is the thing to be processed. Birch plus its finished notice is the example. Learners label both as examples and then cannot count.

**Examples lock pattern, not truth.** One example is excellent at showing label order and brevity, and poor at teaching judgement: a single positive case biases toward positive. Two or three contrasting cases start to teach a boundary.

**Choosing is a judgement with a reason.** Start zero-shot when the instruction is clear and the task common. Go one-shot when the output has a shape words cannot convey, or when a team has an agreed house style to copy exactly. Say the reason aloud; that is what makes it a technique rather than a preference.

### How it connects to the rest of the framework

`TSC2-Basic-K5` is the knowledge behind this ability; `TSC2-Basic-K2` explains why an example shifts the output; `TSC2-Basic-A5` names the elements an example sits among; `TSC2-Basic-A8` is how you would compare a zero-shot and a one-shot design properly. Both techniques reappear at Intermediate level (`TSC3-Intermediate-A3`) with few-shot and contrastive variants.

### What is current as of November 2026

Zero-shot has got much better. Current frontier models follow a precise written instruction far more reliably than their predecessors, so the old advice "always include an example" is now often wasted effort. What stays genuinely hard to describe is house style: the exact label order your team uses, how your organisation writes a date, the brevity of a particular notice. That is where one-shot still earns its place — as a targeted fix for style that resists description, not as a general upgrade.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"One-shot means one attempt."* It means one worked example.
- *"Asking twice with a different tone is one-shot."* That is two zero-shot prompts.
- *"An example guarantees the format."* It improves the odds and adds copy risk.
- *"Zero-shot is the beginner version."* It is the right choice for most clear, common tasks, including for experts.

## How a student should understand it

**Mental model:** giving directions by landmark versus by marked map. "Turn left after the market" is an instruction; the map is an example. Both work; the map costs more to draw and gets copied exactly, wrong turns included.

**Things they can do after this bullet:**
1. Describe each technique in four sentences, including when not to use it.
2. Count worked examples in a prompt, and explain why a rerun does not count.
3. Choose a technique for a stated task and give a reason.

**Misconceptions to kill:** attempt-as-example; input-as-example; example-as-guarantee.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The wedding invitation.** You can describe the wording you want — formal, both families' names, date, venue, RSVP by the 30th. That is zero-shot. Or you can hand over last year's invitation and say "like this, with our names". That is one-shot: faster, closer in style, and it carries over last year's font and the cousin's name if you are careless. Where it breaks: an invitation is a fixed genre with few variations; most workplace writing drifts more.

### Worked example with a real tool

Run the zero-shot prompt twice, each in a fresh chat, then the one-shot once.

```text
Turn the following fictional facilities note into exactly two lines for a staff notice. The first line must begin 'Affected:' and include the room, closure day and reason. The second line must begin 'Reopens:' and give the reopening day and time. Do not add anything else.

Now write the notice for this note:
Note: The Cedar meeting room will be closed for floor cleaning on Tuesday and will reopen on Wednesday at 9 am.
```

```text
Turn the following fictional facilities note into exactly two lines for a staff notice. The first line must begin 'Affected:' and include the room, closure day and reason. The second line must begin 'Reopens:' and give the reopening day and time. Do not add anything else.

Example:
Note: The Birch meeting room will be closed for lighting repairs on Monday and will reopen on Tuesday at 10 am.
Affected: Birch meeting room closed on Monday for lighting repairs.
Reopens: Tuesday at 10 am.

Now write the notice for this note:
Note: The Cedar meeting room will be closed for floor cleaning on Tuesday and will reopen on Wednesday at 9 am.
```

What to point at afterwards: the two zero-shot runs are identical — same instruction, same note, no example. The one-shot prompt adds one pair: Birch. Then ask the room to count: zero, zero, one. And ask the harder question — given the instruction already fixes the label order and the two-line shape, did the example buy anything? Often the honest answer is "barely", which is the most useful finding of the exercise.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "We need a two-line closure notice. How could we show the tool the layout? Does sending it twice count as showing it?" Take two or three guesses.
2. **State the objective** — by the end you can describe both techniques, count examples, and justify a choice.
3. **Recall prior learning** — the one-word comparison from `TSC2-Basic-K2`; the elements list from `TSC2-Basic-A5`.
4. **Present the content** — the four-part description, then the attempt/example distinction.
5. **Guide** — run the zero-shot prompt twice on screen and let the room count.
6. **Elicit performance** — pairs run the one-shot prompt, then write a two-sentence description of one-shot for a colleague.
7. **Give feedback** — read descriptions aloud; check all four parts are present, especially the cost.
8. **Transfer** — each learner names a task where a house-style example would save time, and one where it would not.

## What the framework doesn't mention but trainers need to know

- **Description is testable.** Ask for it in writing; a description missing the "when not to use" part is not finished.
- **Naming conventions differ across vendors.** Some say "few-shot" for anything with examples. Teach the counting rule, not the vocabulary.
- **One-shot is a maintenance cost.** A prompt carrying an example must be updated when house style changes, and nobody remembers.
- **Learners who have mastered zero-shot often need nothing more.** Resist escalating to few-shot for its own sake.

## Watch out

- **Do not let "zero-shot" sound inferior.** It is the default for clear tasks and the cheaper option at scale.
- **Do not demo the example before the instruction.** Order matters in the prompt; it matters in the lesson too.
- **Do not forget the copy risk.** Watch for "Birch" appearing in a Cedar notice — the best teaching moment in the exercise.
- **The stale claim to retire:** "always give the model an example." In November 2026 a precise instruction often beats a single example, and one lopsided example can bias the answer.
