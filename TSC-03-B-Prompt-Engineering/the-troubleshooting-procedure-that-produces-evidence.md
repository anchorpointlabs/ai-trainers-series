---
id: 03.01.B.A6
tsc: 3
level: Basic
code: A6
title: The troubleshooting procedure that produces evidence, not guesses
---

# The troubleshooting procedure that produces evidence, not guesses

> **TSC #3 Prompt Engineering · Basic · Ability A6**


> **Framework text (verbatim):** "Follow standard troubleshooting procedures."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 13 of 15

**One-line version:** A procedure is what you follow when you are not the expert in the room — so it has to be written down, ordered, and end with a decision rather than an opinion.

## What it is

A standard troubleshooting procedure is an ordered sequence anyone can follow when an AI tool misbehaves: capture, classify, run the cheap checks, isolate, decide, record. The word doing the work is *standard* — followed by one person privately, it is a habit; written down with an escalation threshold, it is a procedure the team can rely on when the person who wrote it is on leave.

## Deep expansion

### The concept

The reason a procedure exists is that under pressure people skip to the interesting step. The interesting step is always "try a different prompt", and it produces a new output with no explanation and no record, which is how the same failure recurs every fortnight with nobody able to say why.

A workable procedure has six steps and one rule.

1. **Capture.** Screenshot or copy the prompt, the input, the output, the timestamp, and the model or product name. Before anything else.
2. **Classify.** Name the symptom and the domain: prompt, input, model, account, interface, environment. `TSC3-Basic-A5` is the symptom vocabulary; `TSC3-Basic-K5` is the domain tests.
3. **Run the cheap checks.** Retry once in a fresh session; check the provider status page; check file size and format; check the account's limits. Four checks, two minutes.
4. **Isolate.** Change one variable. Bisect the prompt if it reproduces. Confirm the failure is repeatable before explaining it.
5. **Decide.** Three outcomes, and only three: use a workaround and continue; escalate with evidence; report a defect in the prompt design and fix it. Say which one, out loud, in the log.
6. **Record and share.** Prompt version, model, symptom, steps taken, decision, owner.

The rule: **never change two things between runs.** Two changes and you have learned nothing, even when it starts working — especially then.

### The sub-concepts

**The escalation threshold is the part that gets omitted.** "Escalate when it is serious" is not a threshold. A usable one: escalate when the failure repeats after two isolation attempts, blocks a deadline today, or involves personal data appearing where it should not. Data exposure escalates immediately and is never retried for convenience.

**Some things must not be retried at all.** If the output contained another customer's data, or a credential, retrying spreads it further and destroys the record. Freeze, capture, escalate.

**The workaround is a decision, not a fix.** "Use the shorter input for now" is legitimate and must be written as temporary, with an owner and a review date, or it becomes the system.

**Escalation has a package.** Prompt, input, output, timestamp, model, steps taken, what you expected. Six items turn "it doesn't work" into a defect report that a support engineer can act on in one pass.

**The procedure is short on purpose.** A twelve-step procedure is followed in the first week only. Six steps fit on a card taped next to the monitor.

**Follow it even when you already know the answer.** The value of a procedure is that the tenth person — who does not know — can still reach the same conclusion.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A4` (Prompt Design); see that entry for the user-level sequence of recording what you see, checking the service, changing one thing and escalating. `TSC3-Basic-K5` is the technique inside step 3 and 4, `TSC3-Basic-A5` is the classification in step 2, `TSC3-Basic-K7` is what changes so the failure cannot recur, and `TSC3-Basic-A4` is the practice list the fix should satisfy.

### What is current as of November 2026

Procedures have had to absorb two things that did not exist in earlier versions of this course. First, version churn: with model versions retired behind unchanged product names, "it worked yesterday" now has a default hypothesis, and the procedure should record the model version at the time of the last good run, not just at the time of failure.

Second, agentic actions. When a tool can send, book, pay or delete, a failure is not only a wrong answer — it is a wrong effect. The procedure needs one extra question before any retry: *did anything already happen as a result of that output?* Retrying a draft costs nothing; retrying a completed action can double it.

### Common misconceptions

- *"Troubleshooting means fixing it."* It means reaching a defensible decision — workaround, escalate, or fix the design. Most failures end in a workaround or a report, not a repair.
- *"If I can fix it, I do not need to log it."* Then the next person pays for the same lesson.
- *"Escalating makes me look incompetent."* Escalating without evidence looks incompetent. Escalating with six items looks like engineering.
- *"The procedure slows me down."* It slows down the first ten minutes and saves the third hour.

## How a student should understand it

**Mental model:** the lift breakdown notice pasted inside the lift — which lift, is anyone trapped, call this number, do not force the door. Written for a stranger under stress.

**Things they can do after this bullet:**
1. Run the six steps on a real failure and produce a log entry.
2. Apply an escalation threshold without asking anyone whether it counts.
3. Write the six-item escalation package.

**Misconceptions to kill:** that the goal is a fix; that logging is optional once resolved; that a workaround is a solution.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The lift breakdown procedure.** Pasted inside the lift, addressed to whoever is standing there: identify the lift, check whether anyone is trapped, call the number on the sticker, do not force the door. Four instructions, no diagnosis, and it works for a resident who has never seen the machinery. Where it breaks: a lift either moves or it does not, while an AI failure can be partial — a usable answer with one wrong figure — so step 2 has to include "is this actually broken, or just imperfect".

**The air-con servicing contract.** Scheduled checks, a fault line to call, and a defined response time. The contract exists because the person who owns the unit does not want to diagnose a compressor at 2pm in April. Where it breaks: the contract has a vendor on the other end; your escalation may go to a colleague who is also guessing.

### Worked example with a real tool

The runbook card, written for a team:

```text
WHEN THE OUTPUT IS TRUNCATED OR CUT OFF

1. CAPTURE  Copy prompt + output + timestamp + model name into the incident note.
2. CLASSIFY Symptom: truncation. Domain: input volume / output limit / thinking budget.
3. CHECK    (a) rerun unchanged in a new chat  (b) check status page
            (c) check file size and row count  (d) check plan limits
4. ISOLATE  Rerun with the first 20 rows only. If complete, it is volume-related.
            If still cut, bisect the instruction, not the data.
5. DECIDE   Workaround: split the batch / raise the output limit if available.
            Escalate: if it recurs on small inputs, or blocks today's deadline.
6. RECORD   Log the decision and owner. Set a review date for the workaround.

DO NOT   Do not retry with real personal data after a suspected data leak.
         Do not change prompt and input in the same run.
```

Then walk one real incident through it with timestamps — 09:12 captured, 09:15 classified, 09:18 checks cleared the account and status page, 09:24 isolated to input volume, 09:31 workaround of batching 400 rows into 100, 09:34 logged with a review date. What to point at afterwards: no step involved guessing, the whole thing took 22 minutes, and the log means the next occurrence takes four.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read the lift notice aloud. Ask why it does not explain how lifts work.
2. **State the objective** — by the end you will run six steps on a live failure and produce a log a stranger can follow.
3. **Recall prior learning** — ask for the last time they escalated something to IT and what they sent. Nearly everyone sends a screenshot and a sentence.
4. **Present the content** — teach the six steps, the one rule, and the escalation threshold.
5. **Guide** — run the truncation case together, with the trainer deliberately trying to skip to a prompt rewrite.
6. **Elicit performance** — pairs take a failure they have actually had and produce the log plus the six-item package.
7. **Give feedback** — another pair follows the log without asking questions. Every question is a missing step.
8. **Transfer** — the team adopts the card, names an owner, and sets a review date.

## What the framework doesn't mention but trainers need to know

- **The procedure is a governance artefact, not a personal habit.** In an audit or an incident review, the log is the evidence that the organisation had a method.
- **Data incidents are not troubleshooting cases.** They are reportable events with their own path. Teach the difference explicitly; learners conflate them under pressure.
- **Workarounds become the system.** Every workaround needs an expiry date, or the temporary batching of 400 rows becomes next year's architecture.
- **Written procedures expose design debt.** If the card grows to twelve steps with three branches, the prompt design is the problem, not the procedure.

## Watch out

- **Do not teach the procedure by describing it.** Run it, in front of the room, on a failure you did not stage.
- **Do not let the room skip step 1.** Capture is the step everyone drops and the one that makes everything else possible.
- **Do not present escalation as failure.** Present it as the expected outcome of a threshold, reached on purpose.
- **The stale claim to retire:** "keep trying until it works." Retrying without recording is how a team learns nothing from its own incidents.
