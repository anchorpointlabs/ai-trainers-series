---
id: 02.01.B.K3
tsc: 2
level: Basic
code: K3
title: Different output modes
as_at: 2026-11-26
review_by: 2027-02-25
---

# Different output modes

> **TSC #2 Prompt Design · Basic · Knowledge K3**

> **Framework text (verbatim):** "Impact of prompts on different modes of AI output."
>
> **TSC #2** Prompt Design · **Basic** · Knowledge · Bullet 4 of 15

**One-line version:** The same facts asked for as prose and as code need two different prompts — and only one of the two answers can be trusted without running it.

## What it is

A prompt can ask for different forms of result: a written update, a program, a table, an image, a short script. Each mode needs its own details in the prompt, because each has its own idea of what "correct" means. A notice is checked by reading it against the facts and the requested length. Code is checked by running it, and by reading it first to see what it is going to do.

## Deep expansion

### The concept

Text and code arrive in the same chat window, in the same typeface, with the same confident tone. That similarity is the trap. They are judged by completely different standards.

A written update is correct when its claims match the source and its shape matches the request. You can verify that by reading, in seconds, with no tools. A program is correct when it produces the right output for the inputs you care about — and that cannot be established by reading alone, because execution is where the logic either holds or does not. A persuasive, tidy, well-commented program that prints the wrong number is a normal failure, and it looks exactly like a correct one.

So the design difference is not stylistic. It is about what the prompt must specify, and what the check must be afterwards.

### The sub-concepts

**Prose wants a reader; code wants a contract.** For an update, the prompt names the audience, the tone, the length and the facts. For a program, the prompt names the language, the inputs and their names, the calculation, and the exact output lines. "Make it work" is as useless to a model as it is to a junior developer.

**Code prompts must forbid side effects.** A program you asked for should store values, calculate and print. If the reply also writes files, opens a connection, or asks for input, you cannot safely run it. Read first; run second. This is a design instruction ("use no input, files or external libraries") and it is also a classroom safety rule.

**Exact output lines are a gift.** "Print exactly these two lines: `Cedar: 2 booked, 1 available`" turns an ambiguous task into a testable one. When the model's program prints something slightly different, you have a crisp failure rather than a debate about style.

**Images and audio are not extensions of text skill.** A prompt for a poster or a voice-over has its own vocabulary (composition, framing, tone of voice) and its own failure modes. Being good at text prompts does not transfer automatically, and a trainer who implies it does sets learners up for quiet embarrassment.

**Fluency transfers; correctness does not.** The model writes code with the same confidence it writes prose. What changes is that code can be executed — which means code is the one mode where the model's output can be checked mechanically, if you bother to run it.

### How it connects to the rest of the framework

`TSC2-Basic-K2` is the mechanism (why any prompt shapes output); this bullet is what changes when the *target* changes. `TSC2-Basic-K5` supplies the construction techniques; `TSC2-Basic-A5` names the elements that shift most between modes (format, constraints); `TSC2-Basic-K4` covers what to do when the output arrives in the wrong shape entirely.

### What is current as of November 2026

The modes have merged in the interface and stayed separate underneath. A single chat with current frontier models will happily produce prose, runnable code, a table, an image brief and a voice script in one conversation — which makes the merge look total. It is not. Structured output is now usually enforced at the platform level (a schema the model must conform to) rather than pleaded for in prose, which is a real improvement for anything feeding a spreadsheet or a system. Code generation has improved most in the middle of the difficulty range: short scripts that do arithmetic, parse a file or reshape a table are now reliable enough to run after a quick read, while anything touching an unfamiliar library or a large codebase still needs a developer.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It came back as a neat code block, so it's a working program."* Neatness is formatting. Working is execution.
- *"If the notice is right, the program based on the same figures will be right."* They share facts, not logic. Only the program can be run.
- *"Asking for code and asking for an explanation are the same request."* Explanation is a different mode with a different check.
- *"The table is basically text."* If it is going into a system, its delimiters and its absence of commentary are the whole point.

## How a student should understand it

**Mental model:** asking a colleague for a written summary and asking the same colleague for a calculator. You read the summary; you test the calculator.

**Things they can do after this bullet:**
1. Write two prompts for the same facts — one for prose, one for code — and say what differs.
2. Read a short program before running it, and refuse to run one that does more than asked.
3. Change one input value, rerun, and predict what should change.

**Misconceptions to kill:** that presentation implies correctness; that a text answer vouches for a program; that mode is only a matter of layout.

## How a trainer explains it

### Analogies that work in a Singapore classroom

### Worked example with a real tool

Run these in two separate chats, with a Python runner open beside you.

```text
Use these invented figures: Cedar has 3 seats, of which 2 are booked; Ash has 5 seats, of which 1 is booked. Available seats are total seats minus booked seats.
Write a short update for a colleague in exactly two sentences, one per room. Each sentence must state the room name, how many seats are booked and how many are available. Use British English. Return only the update.
```

```text
Use these invented figures: Cedar has 3 seats, of which 2 are booked; Ash has 5 seats, of which 1 is booked. Available seats are total seats minus booked seats.
Write a complete Python 3 program that stores the four given numbers in variables named cedar_seats, cedar_booked, ash_seats and ash_booked. Calculate each room's available seats by subtraction. Print the room names, booked values and calculated available values as exactly these two lines:
Cedar: 2 booked, 1 available
Ash: 1 booked, 4 available
Use no input, files or external libraries. Return only the code, without an explanation or Markdown fences.
```

What to point at afterwards: the facts block is identical; everything after it changes. The text prompt names a reader and a sentence count. The code prompt names a language, four variable names, a method (subtraction), two exact output lines and a ban on side effects. Then inspect the code and run it. Finally change `cedar_booked` from 2 to 1 and run again — Cedar should read `1 booked, 2 available` while Ash is untouched. That ten-second experiment is the whole reason code is a different mode: you can test it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If I need a room update for a colleague and a program to calculate the same figures, should I ask for exactly the same thing?" Collect two views.
2. **State the objective** — by the end you can write both prompts and state the different check each needs.
3. **Recall prior learning** — the notice-writing prompts from earlier bullets; same facts, new target.
4. **Present the content** — prose wants a reader, code wants a contract; structure has its own failure pattern; fluency is not correctness.
5. **Guide** — write both prompts together, then inspect and run the code on screen.
6. **Elicit performance** — pairs run both, then modify one value and rerun.
7. **Give feedback** — debrief any mismatch: was it the prompt, the reading, or the run?
8. **Transfer** — each learner names one task in their job better suited to code, and one better suited to prose.

## What the framework doesn't mention but trainers need to know

- **The code mode is a safety topic, not just a productivity one.** "Read before you run" and "run it where it cannot reach real data" belong in the same sentence as the demo.
- **Most learners will never run code.** For an admin audience, the transferable lesson is not Python; it is that a confident artefact still needs the check its mode allows.
- **Mode confusion is expensive in offices.** A table pasted into an email, a JSON blob wrapped in an apology, a program nobody executed — the cost lands on whoever uses it next.
- **Ask what happens after the output exists.** A perfect table that the receiving system rejects for its delimiters has failed the task.

## Watch out

- **Do not run unreviewed code in front of a class.** Read it aloud first; say what each line does; only then execute.
- **Do not demo only the pretty mode.** If you show prose and skip code, the room learns the wrong hierarchy of difficulty.
- **Do not let a working program end the discussion.** Ask what would happen if the input had a blank cell — that is where the real question lives.
- **The stale claim to retire:** "it writes code, so it can do your spreadsheet." It writes plausible code; whether the logic fits your spreadsheet is a separate, human judgement.
