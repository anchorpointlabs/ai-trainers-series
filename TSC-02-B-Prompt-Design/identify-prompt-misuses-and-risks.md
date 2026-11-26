---
id: 02.01.B.A7
tsc: 2
level: Basic
code: A7
title: Identify prompt misuses and risks
---

# Identify prompt misuses and risks

> **TSC #2 Prompt Design · Basic · Ability A7**

> **Framework text (verbatim):** "Identify common prompt misuses (e.g., lack of context, vague instructions) and risks."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 15 of 15

**One-line version:** Two misuses cause most of the damage — no context, and no clear instruction — and neither is fixed by trusting the answer more carefully.

## What it is

A prompt misuse is a way of asking that reliably produces a bad or unusable answer. Leave out the situation and the facts, and the tool guesses; leave the instruction vague, and it chooses a shape you did not want. Each misuse has a realistic consequence: a wrong time in a notice, a crucial detail omitted, a family arriving at a closed library. Fixing the prompt reduces the risk. It does not remove the need to check the answer against a reliable source.

## Deep expansion

### The concept

This is the last bullet in the topic, and it is the one that gathers the earlier ones into a risk register. Learners should leave able to look at any prompt — theirs or a colleague's — and name what is missing and what could go wrong because of it.

The two the framework names are the two that matter most.

**Lack of context.** The prompt does not say what the situation is or supply the facts. The model has no option but to fill the gap with the most ordinary plausible material, and ordinary material is wrong for a specific workplace. Risk: an invented time, an invented venue, an invented policy — delivered fluently.

**Vague instructions.** "Write something good about the library" is not a task. It does not name the form (notice, email, post), the content required, or the length. Risk: a piece that is pleasant and useless, missing the one thing the reader needed, such as the cancellation.

Beyond those two, five more misuses appear often enough to name in a Basic class.

**Contradiction.** The instruction says two sentences; the example shows four. The model obeys whichever has more weight on the day, and behaviour becomes erratic.

**No instruction for missing information.** Nothing says what to do when a detail is absent, so the model invents one. Risk is highest exactly where the stakes are highest: figures, dates, names.

**Over-specification.** Twenty micro-rules produce an output that satisfies most of them and drops the rest, or reads stiffly because the constraints fight each other.

**One prompt, many jobs.** Extract, translate, judge, draft and format in a single request. Accuracy plateaus, and when it fails you cannot tell which job failed.

**Untrusted text treated as instruction.** Pasting an email or a web page that contains commands, without marking it as data. At Basic level this is a habit, not a security specialism.

### The sub-concepts

**Risk is specific, not general.** "The AI might be wrong" is not a risk statement. "Families could arrive during the closure because the model guessed a time" is. Teach the specific form; it makes the mitigation obvious.

**Fixing the prompt is half the job.** The other half is checking the output against the source facts, independently of how good the prompt now is. A learner who believes a clear prompt guarantees a correct answer has swapped one risk for another.

**Some misuses are inherited.** A template copied from the internet carries its author's assumptions — a different country, a different register, a different purpose. Ask where the prompt came from.

**Prompts are policy.** If a prompt contains a business rule ("if the amount is over $500, escalate"), someone is making policy in a text box. That is a misuse of the prompt and a governance problem at once.

**The risk register is short and portable.** Two misuses, two risks, two fixes — that fits on a card and survives a busy week. Depth can come later.

### How it connects to the rest of the framework

`TSC2-Basic-K7` is the concept these misuses violate; `TSC2-Basic-K2` explains why missing context gets invented; `TSC2-Basic-A6` is the positive practice list; `TSC2-Basic-K4` supplies the guardrails that mitigate them; `TSC2-Basic-K6` and `TSC2-Basic-A3` cover the privacy misuse of pasting real data. At Intermediate level, `TSC3-Intermediate-A6` builds a fuller misuse catalogue.

### What is current as of November 2026

The failure has become quieter. The late-2026 frontier models — OpenAI's GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — fill a gap so smoothly that a vague prompt now produces something that reads finished. Two years ago the seams showed; now they do not. That makes the check more important, not less, and it makes the "vague instruction" misuse the one most likely to pass unnoticed in a workplace. The second 2026 development is tool access: a prompt misuse that once produced a wrong document can now produce a wrong action, which moves some of these risks into `TSC2-Basic-K4` territory.

### Common misconceptions

- *"If the answer is wrong, the model is bad."* Usually the prompt left a decision open. Ask which one.
- *"A clearer prompt removes the need to check."* It narrows the risk; it does not verify anything.
- *"More instructions means more control."* Past a point, more instructions means more contradictions and less compliance.
- *"Misuse means deliberate abuse."* Most misuse is careless, not malicious. The word covers both.

## How a student should understand it

**Mental model:** sending a new staff member to represent you at a meeting with no brief. Whatever they say will be plausible, confident, and not quite your position.

**Things they can do after this bullet:**
1. Name a missing context and a vague instruction in a weak prompt.
2. State a specific risk for each, in terms of who is affected.
3. Rewrite the prompt and then check the answer independently.

**Misconceptions to kill:** model-blaming; clarity-as-verification; length-as-control.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The relief-bus announcement.** "Bus service affected" tells nobody anything. "Service 92 skips stops 5–8 from 9am to 2pm; use Service 93" is a brief. The first causes a crowd at a closed stop; the second causes a detour. Where it breaks: a bus announcement is checked before it is broadcast, and the check is someone else's job; here it is yours.

### Worked example with a real tool

```text
Write a notice to parents who booked the children's reading session at a fictional library. Use only the facts below and include every fact. Write two sentences in plain British English. Do not invent a new session date or time.

Facts:
- On Tuesday, the library will be closed from 1 pm to 3 pm because of a water leak.
- The children's reading session planned for Tuesday at 1.30 pm is cancelled and will not be held online.
- Parents should check the library noticeboard on Wednesday for rescheduling information; no new session date or time has been set.
```

What to point at afterwards: first show the weak version — "Write something good about the library" — and have the class name both misuses and both risks before you paste the good prompt. Then run the good prompt and check each of the three facts against the notice, sentence by sentence. The most instructive moment is when a fluent notice invents a rescheduling date; if it does not, point out that the ban on inventing dates is why, and that the ban was a decision someone had to make.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If I ask for 'something good about the library', what might a parent expecting an important notice miss?" Take a consequence, not a prediction of failure.
2. **State the objective** — by the end you can name two misuses, state a specific risk, and rewrite the prompt.
3. **Recall prior learning** — the element list and the guardrail list; this bullet is what happens when both are ignored.
4. **Present the content** — the two named misuses, five more, and the rule that clarity is not verification.
5. **Guide** — mark the weak prompt together, then write the replacement on the board.
6. **Elicit performance** — pairs rewrite a weak prompt from their own workplace and state one risk each.
7. **Give feedback** — run the prepared prompt and check the output against the facts independently.
8. **Transfer** — each learner adds one line to their personal prompt card: the misuse they are most likely to commit.

## What the framework doesn't mention but trainers need to know

- **Misuse is usually inherited, not invented.** Templates travel; ask where a prompt came from before critiquing it, or you critique the learner's predecessor.
- **The risk register should name a person harmed.** "Parents could arrive at a closed library" lands harder than "output may be inaccurate", and it is more useful.
- **Learners fix the prompt and stop.** Insist on the independent check as a separate step with its own evidence.
- **Some prompts should not exist.** If a task needs six jobs done at once or a policy decision made in a text box, the answer is a workflow change, not better wording.

## Watch out

- **Do not let "misuse" sound like misconduct.** Most of it is haste. Keep the tone diagnostic.
- **Do not demo the weak prompt and leave it there.** The rewrite is the lesson; the failure is only the hook.
- **Do not overstate what a good prompt buys.** It buys a narrower risk and a checkable output — nothing more.
- **The stale claim to retire:** "a good prompt can't go wrong." In November 2026 a good prompt goes wrong less often and less visibly, which is exactly why the check stays in the procedure.
