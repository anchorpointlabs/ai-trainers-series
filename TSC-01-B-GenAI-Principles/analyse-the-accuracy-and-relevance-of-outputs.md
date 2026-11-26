---
id: 01.01.B.A2
tsc: 1
level: Basic
code: A2
title: Analyse the accuracy and relevance of outputs
as_at: 2026-11-26
review_by: 2027-02-25
---

# Analyse the accuracy and relevance of outputs

> **TSC #1 Generative AI Principles and Applications · Basic · Ability A2**

> **Framework text (verbatim):** "Analyse the accuracy and relevance of generative AI outputs for specific tasks."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Ability · Bullet 10 of 13

**One-line version:** Read the output like an editor with a source open, not like a reader being persuaded — accurate means it matches the facts, relevant means it answers the question you asked, and neither can be judged from how good the prose is.

## What it is

This is the ability that makes everything else safe. Given an output and a task, the learner checks three things: is it **accurate** (do the facts match the source I supplied or can find), is it **relevant** (does it answer the actual question, for the actual audience, at the right scope), and is anything **invented** (a figure, a citation, a commitment nobody authorised). Then they say what to correct and re-run. The output is a draft until this happens, and the learner decides when it stops being one.

## Deep expansion

### The concept

Checking is a different cognitive task from reading, and most people never switch modes. Reading for sense is fast, holistic and forgiving; checking is slow, granular and suspicious. A fluent paragraph disables the second mode, which is why the most dangerous output is the well-written one with a single wrong number.

The trainer's job is therefore not to teach vigilance — everyone already believes they are vigilant — but to install a **procedure** that survives a busy afternoon. Three passes, in this order:

1. **Against the source.** Every factual claim compared to the document, system or person it came from. Not skimmed — located.
2. **Against the brief.** Every requirement checked off: length, audience, tone, inclusions, exclusions.
3. **Against consequence.** Which sentences, if wrong, would matter most? Those get a second look regardless of how confident they read.

The order matters. Learners check prose quality first because it is the easiest thing to judge, and it is the only thing that carries no information about correctness.

### The sub-concepts

**Accuracy has three levels, and they fail differently.** *Factual*: a date, a figure, a name, a citation — check by locating it. *Relational*: facts right, relationship wrong; the source said software grew and hardware fell, the summary says the reverse. This is the intrinsic-hallucination failure, invisible unless you read the source sentence rather than the number. *Attributional*: right fact, wrong source, or no source at all. All three pass a fluency check.

**Relevance has four shapes.** *Scope*: asked for a decision, got a summary; asked for 200 words, got 700. *Audience*: technically correct, wrong for a regulator, a customer or a new joiner. *Question*: answers the general version of what was asked rather than the specific case. *Constraint*: ignores an instruction — no jargon, must mention the deadline, no numbers in the headline. Relevance failures are the ones learners forgive themselves for, because the output is still useful. That tolerance is exactly what the framework's word "relevant" is guarding against.

**Verification by construction, the practitioner's move.** Do not check a claim you cannot trace; arrange the task so the trace exists. Four techniques, all usable at Basic level: **supply the source and demand the quote** ("answer only from the document; for each claim quote the exact sentence and give the page"); **ask for uncertainty explicitly** ("if you cannot verify a fact without an external source, say so rather than guessing"); **ask it to audit itself against your brief** ("list every requirement in my request and whether the draft meets it"); and **keep a source of truth open** — if you cannot open a source, you cannot verify, and the honest move is to mark the claim unverified.

**Consequence × verifiability.** Two axes. High consequence, easy to verify: always check, cheaply. High consequence, hard to verify: do not use the output. Low consequence, easy: spot-check. Low consequence, hard: fine to use, and say so if asked. This replaces "be careful", which nobody can act on, with a decision.

**Re-running is part of the check.** Correcting a sentence by hand is fine for one error. If errors are structural — wrong tone throughout, wrong structure, facts wrong in three places — re-run with a better brief. Patching a bad draft produces a document with two voices.

### How it connects to the rest of the framework

`TSC1-Basic-K6` explains why every failure here exists. `TSC1-Basic-A01` produces the output this bullet examines — a good brief makes the check cheap. `TSC1-Basic-K4` decides whether the check is worth doing at all. `TSC1-Basic-A05` asks who signs off when it is done. At Intermediate this becomes an evaluation routine with samples and a scoring rubric.

### What is current as of November 2026

- **Citations are easier to produce and just as easy to fake.** Search-augmented products attach numbered footnotes, and a footnote proves only that a retrieval step found something. The click-through is still the check.
- **Closed-world grounding changed the arithmetic.** Products that answer strictly from an uploaded source set — NotebookLM is the clearest example — refuse when the answer is not in the documents, which turns a verification problem into a coverage problem. A better trade for high-stakes reading, and an option rather than a universal answer.
- **Reasoning modes make the check easier and the error more convincing.** A visible chain can be audited step by step, and a chain built on one fabricated premise still reaches a confident wrong answer.
- **Agentic outputs need a fourth check.** With tool access the output may include actions taken, not just text produced, so accuracy includes "did it do what it said it did" — checked in the system, not the reply. The agentic governance framework (January 2026) assumes this check exists.

### Common misconceptions

- *"It's well written, so it's probably right."* Prose quality and factual accuracy come from different mechanisms and correlate weakly.
- *"I checked it and it looked fine."* Looking is not locating. The check is "I found this sentence in the source".
- *"Asking the model if it is sure counts as checking."* It tests agreeableness. Use a source.
- *"Relevance is a nice-to-have."* An accurate but irrelevant answer still fails the task, and it is the failure the framework names.
- *"If I give it the source document, it cannot be wrong."* It can misread the source, blend in assumptions, or answer from the wrong section. Grounding narrows a class of error; it does not close it.

## How a student should understand it

**Mental model:** a sub-editor on a newspaper desk. Not hostile, not credulous — paid to find the one number that will get the paper sued, in four minutes.

**Things they can do after this bullet:**
1. Take an output and its source and mark every claim as verified, unverified or wrong, with the location.
2. Name the four relevance failures and spot at least two in a sample.
3. Decide whether to check by hand, re-run with a better brief, or not use the output at all.

**Misconceptions to kill:** that fluent means accurate, that "are you sure" is a check, and that relevance is optional.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The insurance assessor.** An assessor does not decide whether a claim *sounds* genuine. They compare it against the policy wording, the receipts and the incident report, line by line, and write down which document each conclusion came from. That is the posture: not suspicion, just provenance.

**The tuition worksheet with one wrong answer key.** A parent checking homework against a wrong key will "correct" the child's right answer. That is what happens when a learner checks an AI output against another AI output.

### Worked example with a real tool

Give the model the facts, then check it against them:

```text
Fact sheet:
- Meeting: 18 June, 3 pm, Blue Room (changed from Green Room).
- Attendees: finance team only; no external guests.
- Lunch: not provided; the café downstairs is open.
- Papers: circulated by 15 June.

Write a 60-word notice for the finance team.
```

Then the audit pass, which is where the learning is:

```text
Now list every factual claim in your notice, and for each one, quote the
line in the fact sheet that supports it. If a claim has no supporting line,
say so.
```

What to point at afterwards: the notice is usually close, and the audit surfaces the invented detail — "please bring your laptops", an assumed duration, a room number in the wrong format. Two lessons at once: the model can audit its own draft against a supplied source fairly well, and it invented things nobody asked for because a notice of that type usually contains them. Then have the room do the same check by hand on a different output and time it. The timing is the argument for building the check into the workflow rather than adding it at the end.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — A generated notice with one wrong date, one wrong room and one invented detail. Who caught all three? Usually nobody.
2. **State the objective** — "You will check an output against its source in five minutes and say not just what is wrong but where the right answer is."
3. **Recall prior learning** — From K6: fluent and wrong. What must a check look like to catch that?
4. **Present the content** — Three passes: source, brief, consequence. Then the four relevance failures.
5. **Guide** — Run the fact-sheet example, then the audit prompt, then verify the survivors by hand.
6. **Elicit performance** — Pairs check a generated reply against a short fact sheet, marking verified / unverified / wrong.
7. **Give feedback** — Compare marks. Disagreements are always about claims that are true but unsupported — name that category, because it is the one that gets sent.
8. **Transfer** — Pick one output type produced weekly and write the three-pass check for it.

## What the framework doesn't mention but trainers need to know

- **Verification cost decides whether the workflow survives.** If checking takes longer than writing from scratch, the tool is a hobby. Design the brief so the check is cheap.
- **"True but unsupported" is the category that ships.** It passes a casual review and fails an audit. Teach the three-way mark, not the two-way.
- **Relevance failures are invisible to the author.** The person who wrote the brief knows what they meant; a second reader catches scope and audience errors.
- **Re-running beats patching when errors are structural.** Two or more errors of the same type means the brief was wrong, not the sentence.
- **The audit prompt is a skill, not a trick.** It works because the task changes from generation to comparison. It is still not verification — the learner confirms the final claim.

## Watch out

- **Do not demo checking on an output that is obviously wrong.** The skill shows up on the output that looks right. Use a good draft with one buried error.
- **Do not let the room check against another chatbot.** Two models agreeing is two averages.
- **Do not turn this into a proofreading lesson.** Spelling and grammar are the least important layer and the easiest to fix.
- **The stale claim to retire:** "AI output cannot be trusted, so check everything." Checking everything costs more than the tool saves. The teachable position is: check what carries consequence, and design the task so the check is cheap.
