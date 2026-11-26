---
id: 02.01.B.A2
tsc: 2
level: Basic
code: A2
title: Recognise AI tool issues
---

# Recognise AI tool issues

> **TSC #2 Prompt Design · Basic · Ability A2**

> **Framework text (verbatim):** "Recognise issues encountered with AI tools."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 12 of 15

**One-line version:** Say what you can see — an unsupported claim, a wrong shape, a refusal, an error — and stop before you say why.

## What it is

Recognising an issue is observing that something is wrong and naming it precisely, without diagnosing it. The answer may contain a claim the note never supported; it may arrive in a layout you did not ask for; it may refuse the request; or the tool may show an error instead of an answer. Each is a different observation. A detail missing from the note is unsupported by that note — which is not the same as false — and a refusal is not automatically a fault.

## Deep expansion

### The concept

Learners tend to jump straight from "something is off" to "the AI is broken" or "the AI is lying". Both are diagnoses, and both are usually wrong. The skill in this bullet is the middle step: describing the mismatch in terms someone else could verify.

Four observations cover almost everything a Basic user meets:

- **An unsupported claim.** The notice says the room seats forty; the note never mentioned capacity. Unsupported means "not in the source", not "untrue" — though in a workplace document it may as well be untrue, because nobody can defend it.
- **A layout mismatch.** You asked for two labelled lines; you got a sentence, or a heading, or a line with an extra item appended. The facts may all be correct.
- **A refusal.** The tool declines. This can be a safety filter, a misunderstood instruction, or a genuine content restriction. It is not evidence of an outage.
- **A service error.** A message appears instead of an answer. The message is a clue, not a cause; the same words can mean several different things depending on where they were generated.

Recognising is deliberately unambitious. It produces a sentence like "the second line adds a chair name that is not in the note", which anyone can check, instead of "the AI hallucinated", which nobody can.

### The sub-concepts

**Unsupported is not false — but treat it as unusable.** A statement the source cannot back is a risk you cannot discharge. The right handling is the same as for a false statement: remove it, or find the fact.

**Hallucination is fluent by construction.** The model is producing the most probable continuation, and a plausible detail is often more probable than an admission of ignorance. That is why invented facts arrive in the same confident register as correct ones — tone is not evidence of anything.

**Sycophancy corrupts the check.** Ask "are you sure?" and the model may flip a correct answer to agree with your implied doubt. A learner who "verifies" by asking again is measuring agreement, not accuracy.

**Layout failures are cheap and constant.** Preludes ("Here is your notice:"), trailing offers ("Let me know if you'd like..."), extra headings, extra columns. They are the most common issue in practice and the least alarming.

**Refusal is information, not insult.** It tells you something about the boundary you crossed or the way you asked. Rewriting the request plainly often resolves it; treating it as a service fault wastes the session.

**A message is not a diagnosis.** "Service temporarily unavailable" from the product, an error page from the network, and a sentence the model invented about an outage look similar and mean different things. Only the first two are evidence.

### How it connects to the rest of the framework

`TSC2-Basic-K1` is the technique set this observation feeds; `TSC2-Basic-A4` is the procedure to run once an issue is recognised; `TSC2-Basic-K4` covers outputs that strayed because the prompt let them; `TSC2-Basic-K2` explains why invention happens at all. At Intermediate level, `TSC6-Intermediate-A1` reads the same failures from an error log.

### What is current as of November 2026

The frontier models of late 2026 — OpenAI's GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — hallucinate less on well-grounded tasks and more convincingly on ungrounded ones, because they are better at sounding certain. Two practical consequences. First, unsupported detail is now the dominant issue in workplace use; formatting failures are easy to see and easy to fix, while a confident invented figure passes a casual read. Second, refusals have become less frequent and more specific, so a refusal is now stronger evidence that you asked for something genuinely restricted rather than that the model was confused.

### Common misconceptions

- *"If it's not in the notes, it's a lie."* It is unsupported. Call it that; the correction is the same and the accusation is more accurate.
- *"A tidy, well-formatted answer has been checked."* Format is the easiest part to get right and says nothing about the facts.
- *"Asking 'are you sure?' is how you verify."* It is how you invite agreement. Verify against the source.
- *"A refusal means the service is down."* It means the request was declined. Those are different findings.

## How a student should understand it

**Mental model:** a receipt with one line you did not buy. You do not need to know how it got there to refuse to pay it; you just point at the line and say "this is not mine".

**Things they can do after this bullet:**
1. Name the mismatch in one sentence, using the source as the reference.
2. Separate a content issue, a layout issue, a refusal and an error.
3. Stop at observation, without guessing a cause.

**Misconceptions to kill:** unsupported-equals-false; format-equals-verified; "are you sure" as a check.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic queue screen.** If your number is not called, you do not conclude the doctor is on strike. You check the screen, ask the counter, and only then consider an outage. Observation, then check, then conclusion — in that order. Where it breaks: a clinic counter can tell you what is happening; an AI tool usually cannot say why it declined or invented.

### Worked example with a real tool

```text
This is a fictional classroom task. Note: "The Green Team meets on Tuesday at 10:00 in Cedar Room."

First write a notice using only the note. The notice must be exactly two lines: line 1 begins "When:" and gives the day and time; line 2 begins "Where:" and gives the place. Do not add facts or a heading above the notice.

Then copy the following four labelled practice cards exactly after the notice, preserving their wording and line breaks. They are invented examples for the same task, not reports of real incidents. Card D is a pretend message from the service. Do not analyse or name the problems.

A:
When: Tuesday at 10:00
Where: Cedar Room; chair: Mei
B:
The Green Team meets on Tuesday at 10:00 in Cedar Room.
C:
I cannot help with that request.
D:
Service temporarily unavailable.
```

What to point at afterwards: the four cards are a taxonomy, not a quiz. A adds a fact the note does not contain — unsupported. B has the right facts in the wrong shape — a layout mismatch. C declines — a refusal. D is an error message — a service observation. Then ask the class to describe each in one sentence without using the words "hallucinate", "broken" or "down". The constraint forces observation, which is the whole ability.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If an AI answer looks tidy, how would you tell whether it meets the request?" Take two suggestions.
2. **State the objective** — by the end you can name four kinds of issue and describe one without diagnosing it.
3. **Recall prior learning** — the check-against-the-notes habit from earlier bullets.
4. **Present the content** — the four observations, unsupported versus false, fluency as non-evidence.
5. **Guide** — classify the four cards together, writing the one-sentence descriptions on the board.
6. **Elicit performance** — pairs run the prompt, check the actual notice, then write their own fifth card for a new failure.
7. **Give feedback** — read the fifth cards aloud; mark any that name a cause.
8. **Transfer** — each learner names the issue they have actually seen at work and how they would now describe it.

## What the framework doesn't mention but trainers need to know

- **Naming matters more than fixing, at first.** A learner who can say "unsupported" can hand the problem to someone else; a learner who says "the AI is bad" cannot.
- **Invention clusters around specifics.** Numbers, dates, names, capacities and citations are where the plausible filler lands. Teach learners to check those first.
- **Some issues are the prompt's fault.** If three learners get a wrong layout, the instruction is probably ambiguous; ask the room before blaming the tool.
- **Record the exact wording.** "It gave a weird error" cannot be searched or reported; a copied message can.

## Watch out

- **Do not let the room diagnose.** "It's hallucinating because it's out of date" is a guess; stop it kindly and ask for the observation.
- **Do not present refusals as failures of the tool.** Some refusals are the system working correctly.
- **Do not use real incidents in the cards.** Invented cards keep the exercise safe and the taxonomy clean.
- **The stale claim to retire:** "you can tell when it's making things up because it sounds unsure." In November 2026 invented detail sounds exactly like sourced detail.
