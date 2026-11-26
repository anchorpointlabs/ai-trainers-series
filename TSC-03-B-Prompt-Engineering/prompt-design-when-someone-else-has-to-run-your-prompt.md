---
id: 03.01.B.K1
tsc: 3
level: Basic
code: K1
title: Prompt design when someone else has to run your prompt
as_at: 2026-11-26
review_by: 2027-02-25
---

# Prompt design when someone else has to run your prompt

> **TSC #3 Prompt Engineering · Basic · Knowledge K1**


> **Framework text (verbatim):** "Concept of prompt design."
>
> **TSC #3** Prompt Engineering · **Basic** · Knowledge · Bullet 1 of 15

**One-line version:** Prompt design is deciding what the answer must be before deciding how to ask — and doing it well enough that a colleague can run the prompt without you standing behind them.

## What it is

Prompt design is the work of specifying a task for a generative model: what to produce, from which facts, for which reader, within which limits, and then the wording that carries all four. At this level the framework asks only for the concept. The workplace adds a constraint the framework leaves implicit — the prompt will be run by people who were not in the room when you wrote it.

## Deep expansion

### The concept

Everyone in the room has already typed a prompt. The shift this bullet asks for is small in wording and large in posture: you stop writing messages and start writing a specification that happens to be phrased as a message. A message is judged by whether it got the job done this time. A specification is judged by whether six people can run it next month, on inputs you have never seen, and get answers that pass the same check.

That change pulls four things into the work that a one-off message never needs.

**An output spec.** Not "summarise this" but "eight rows, one per complaint, each ending with the action taken, no adjectives". If you cannot write the acceptance check, you have not designed the prompt — you have described a hope.

**Input variability.** A practitioner prompt runs on this week's spreadsheet, not last week's clean sample. Design for the untidy case: the missing column, the complaint written in Chinese, the row where the customer's name appears in the remarks field. The prompt should say what to do when the input is unfit, and the safest default is to stop and report rather than improvise.

**Acceptance inputs.** Two or three inputs whose correct answer you already know. Without them, every change to the prompt is judged by impression, and an improvement and a regression look identical.

**A home.** Where the prompt lives, who owns it, what version it is, and what changed. A prompt that exists only in someone's chat scrollback is not an asset; it is a habit.

### The sub-concepts

**Design order.** Task and acceptance check first, facts second, reader third, wording last. Learners invert this: they hunt for persuasive phrasing and leave the check until afterwards, which is why their prompts get longer without getting more reliable.

**The runner's floor.** Write for the colleague who pastes the input untrimmed and skips the paragraph of explanation. A prompt that needs a briefing is not finished. The test is whether it works read cold.

**Deliberate under-specification.** Some parts should be left to the model — the exact phrasing of a polite sentence, the choice of illustration. Knowing what to leave open is design, not laziness. What must never be left open is anything the reader will be held to: figures, names, dates, commitments.

**Prompt debt.** Every hard-coded exception ("unless it is a CPF case, then...") is a maintenance obligation. Teams accumulate these silently until the prompt is unreadable and the next person rewrites it from scratch without knowing why the clauses existed.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-K7` (Prompt Design); see that entry for the user-level basics. `TSC3-Basic-K2` explains the mechanism — why wording changes output at all; `TSC3-Basic-A1` gives the parts a prompt is built from; `TSC3-Basic-A3` is how two designs are compared; `TSC3-Basic-A4` is the practice list; `TSC3-Basic-A8` catalogues the ways designs fail. If a learner remembers one thing from this level, it should be that design ends when someone else can run it.

### What is current as of November 2026

The main shift is that prompts now have somewhere to live. The major assistants let you save standing instructions, keep a project's files attached, and share a setup with a team, so the artefact framing above is no longer a metaphor — there is a storage location, an owner and usually a version history. Two consequences: a prompt library is a document that needs a librarian, and a saved prompt containing real customer examples is a data store with the same obligations as any other.

The second shift is that some of what prompts used to plead for is now enforced by the platform. Structured outputs, tool schemas and system-level instructions move format control out of prose and into configuration. That is good for reliability and dangerous for the learner who believes a well-worded sentence is a guarantee.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Designing a prompt just means writing it more carefully."* Careful wording with no output spec produces a nicer version of the same variability.
- *"The longer the prompt, the more control I have."* Past a point, each added line competes for attention with the instruction that matters. Length is a cost, not a virtue.
- *"It worked, so it is designed."* One clean run on a clean input is an anecdote. The design question is the input you did not test.
- *"If it breaks, the model got worse."* Usually the input changed, or someone edited the prompt without knowing why a clause was there.

## How a student should understand it

**Mental model:** writing the recipe card for a hawker stall you will not be working in — the dish has to come out the same when the part-timer cooks it on a busy Saturday.

**Things they can do after this bullet:**
1. Write an output spec and two acceptance inputs before touching the wording.
2. Name the prompt's owner, version and storage location.
3. Run their own prompt on a deliberately messy input and report what happened.

**Misconceptions to kill:** that a prompt is a message rather than a specification; that length equals control; that one good output is evidence of design.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The SOP card above the wok.** A hawker who cooks from memory makes a great plate and can never take a day off. The stall that taped a card above the wok — two ladles of gravy, ninety seconds, garnish on the left — can be run by the part-timer on Saturday. Where it breaks: a card cannot capture "until the oil shimmers", so the trainer's real job is converting judgement into something checkable, which is precisely the skill being taught.

**The PSLE marking scheme.** A question paper without a marking scheme starts arguments between markers; a prompt without an output spec starts rewrites between colleagues. Where it breaks: markers discuss and converge, while the model will comply with a bad spec without complaint — so the spec has to be right the first time.

### Worked example with a real tool

Task: a five-person admin team compiles a weekly complaint summary for a retail manager. The version everyone writes first:

```text
Summarise these customer complaints for my boss.
```

Then the practitioner version, pasted with the week's rows underneath:

```text
You are summarising this week's customer complaints for a retail manager who
has four minutes and will forward the table to the store supervisor.

Produce a markdown table with exactly these columns:
Complaint type | Count | Example (one line) | Action taken

Rules:
- Use only the rows I paste below. Do not add complaint types that are not in the data.
- If a row has no action recorded, write "not recorded". Do not guess one.
- Sort by Count, highest first. Cap at 8 rows; if there are more, add a final
  row "Other" with the combined count.
- If the pasted data contains no complaint rows, reply with the single line
  "NO COMPLAINT ROWS FOUND" and nothing else.

Data:
<the week's rows>
```

What to point at afterwards: four choices are doing the work — the reader and time budget, the fixed columns, the "do not guess" rule, and the empty-input escape. Then run it twice, once on a clean week and once on a week where the action column is missing, and show that the second run behaves predictably instead of inventing actions. That predictable second run is the deliverable, not the pretty first one.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a prompt that produced a beautiful summary with two invented action items, and ask who in the room would have caught them.
2. **State the objective** — by the end you will write one prompt a colleague can run cold, with an output spec and two acceptance inputs.
3. **Recall prior learning** — ask what they already say when briefing a new colleague on a recurring task; it is the same three questions of what, for whom, and what must not happen.
4. **Present the content** — teach design order: check, facts, reader, wording; then the four artefacts — spec, variability, tests, home.
5. **Guide** — build the complaint-summary prompt together on screen, taking suggestions for the columns and the empty-input rule.
6. **Elicit performance** — pairs write a prompt for a recurring task from their own job, plus two acceptance inputs.
7. **Give feedback** — swap prompts between pairs and run them cold; the writer may not explain anything.
8. **Transfer** — each learner names where their prompt will live and who else will run it.

## What the framework doesn't mention but trainers need to know

- **Prompts carry policy.** "If the customer is a CPF case, escalate" is a business rule, and the person who wrote the prompt may have no authority to decide it. Ask who approves. If nobody does, the prompt is where policy is being made by accident.
- **A prompt that "works" often hides its cost.** If the output is plausible but never checked, the design has transferred risk rather than removed work.
- **Storage is part of design.** A saved prompt holding three real customer emails is a small database. Where it lives decides who can read it, how long it stays, and whether it survives the author leaving.
- **The best prompt in the room is often the shortest.** Practitioners over-fit. Half the value of a review is deleting clauses nobody can justify.

## Watch out

- **Do not demo a prompt cold.** Rehearse the worked example on the day's model. A live failure teaches only if it is the failure you planned.
- **Do not let one good output close the exercise.** Ask for the messy input before anyone relaxes.
- **Do not teach this as a bag of magic phrases.** Learners who collect tricks cannot diagnose a failure.
- **The stale claim to retire:** "just tell it what you want and it will figure out the rest." In November 2026 it will produce something; whether that something is repeatable is the actual subject of this TSC.
