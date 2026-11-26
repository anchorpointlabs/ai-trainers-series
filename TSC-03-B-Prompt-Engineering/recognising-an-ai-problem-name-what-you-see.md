---
id: 03.01.B.A5
tsc: 3
level: Basic
code: A5
title: Recognising an AI problem: name what you see, not what you think
---

# Recognising an AI problem: name what you see, not what you think

> **TSC #3 Prompt Engineering · Basic · Ability A5**


> **Framework text (verbatim):** "Recognise issues encountered with AI tools."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 12 of 15

**One-line version:** The dangerous AI failure is not the one that stops you — it is the one that looks finished, and recognising that difference is the whole skill.

## What it is

Recognising an issue means being able to say precisely what went wrong, in terms someone else can act on, without jumping to a cause. It covers a small vocabulary of symptoms — unsupported claims, format drift, truncation, refusals, empty responses, run-to-run variation, sudden regressions — and a severity judgement about whether the output can still be used.

## Deep expansion

### The concept

Learners describe failures in two unhelpful ways. Either they name a cause ("it hallucinated") which stops the investigation, or they name a feeling ("it gave a weird answer") which cannot be investigated at all. The practitioner's habit is narrower: describe the observation, the artefact, and the consequence.

"There is no refund amount in the case note, and the draft says $72" is an observation. It can be checked in ten seconds. "It hallucinated" is a theory that invites agreement rather than verification, and it hides the more useful question — was the amount invented, inferred from a similar case, or carried over from the previous row?

The second half of the skill is severity. Three grades:

- **Blocking** — no usable output. Error, empty reply, refusal, total truncation. Visible, reported, fixed.
- **Corrupting** — usable output that is wrong in a way the reader will not notice. A plausible figure, an invented policy, a summary that drops the one exception, a table whose counts do not add up. This is the expensive one, and it is systematically under-reported because nothing about it looks broken.
- **Cosmetic** — visible and harmless. Wrong heading level, an extra bullet, inconsistent capitalisation. Worth noting, not worth escalating.

Most training spends its time on blocking failures because they demo well. Most workplace damage comes from corrupting ones.

### The sub-concepts

**Eight symptoms, eight different next steps.** Fluently wrong content; format drift; truncation; refusal; empty or error; variation between identical runs; regression ("it worked yesterday"); wrong scope (it answered a different question). Recognising which one you have is the skill; treating them all as "bad output" wastes the diagnosis.

**Observation before diagnosis.** Write the sentence with no causal verb in it: what the input was, what the output said, where they disagree. Causal language is for step two, after evidence.

**Capture before retry.** Screenshot or copy the prompt, the output, the timestamp and the model version before you change anything. The instinct to retry immediately destroys the only evidence you had.

**Some issues are prompt issues, and that is fine.** "The tool did exactly what the prompt said, and the prompt was ambiguous" is a legitimate recognition. Naming it is routing, not blame.

**Refusal is not always a fault.** Content policy, a contradictory instruction and a genuinely unsupported request all produce a refusal-shaped output, and only one of them is a problem with the tool.

**Severity is a judgement about the reader, not the text.** The same error is cosmetic in a brainstorm and corrupting in a customer letter. Recognising severity means asking who acts on this and what they would do.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A2` (Prompt Design); see that entry for the user-level basics of spotting an unsupported claim or a refused request. `TSC3-Basic-K5` is the diagnostic technique this feeds, `TSC3-Basic-A6` is the procedure it triggers, `TSC3-Basic-K7` is what to change so the symptom cannot recur, and `TSC3-Basic-A8` explains which misuses produce which symptoms.

### What is current as of November 2026

Two symptoms have changed shape. Truncation is now more often a thinking-budget or output-limit setting than a length instruction problem, so "make it shorter" is frequently the wrong first move. And regressions have become the most common corrupting failure: model versions are retired and rerouted behind unchanged product names, so a prompt that produced acceptable output last quarter can produce different output today with no change on your side.

The other shift is that corrupting failures are easier to catch than they used to be, because structured outputs and citations give you something mechanical to check — a schema, a quote, a source link. A team that specifies an output shape has, in effect, built its own detection.

### Common misconceptions

- *"If the answer looks right, there is no issue."* That is the definition of a corrupting failure.
- *"Retry until it works, then move on."* You have fixed the symptom and destroyed the evidence.
- *"A refusal means the tool is broken."* It may be the tool working as configured, against a request that was never going to pass.
- *"Reporting is complaining."* A report with input, output, timestamp and expected result is a defect report. Without those it is a complaint.

## How a student should understand it

**Mental model:** the triage nurse at the polyclinic. The nurse does not diagnose; the nurse classifies urgency and routes — and a patient who says "I feel weird" gets asked four questions before anything happens.

**Things they can do after this bullet:**
1. Name the symptom in one sentence containing no causal verb.
2. Grade it blocking, corrupting or cosmetic and say who it affects.
3. Capture the artefact before touching the prompt.

**Misconceptions to kill:** that a good-looking answer is a good answer; that naming a cause is recognising a problem; that refusals are always faults.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Triage at the polyclinic.** The nurse sorts by urgency, not by diagnosis, and the sorting determines what happens next. Get the sorting wrong and the heart attack waits behind the sprained ankle. Where it breaks: a patient can describe their own symptoms, while an AI output has no complaint of its own — someone has to read it against the source, and that person is you.

**Dashboard warning lights.** A red light means stop now; an amber light means check soon; a service light means it can wait until Saturday. Where it breaks: a car has a fixed, documented set of lights, while AI symptoms are open-ended — which is why the vocabulary has to be taught rather than looked up.

### Worked example with a real tool

One prompt, five outputs, all generated from a real case file:

```text
Summarise this case note in 60 words for the duty manager, and state the
next action and who owns it.
```

Then classify what came back:

| What you see | Symptom | Severity |
|---|---|---|
| The reply stops mid-sentence at "the customer has" | Truncation | Blocking |
| A tidy 60-word summary naming an action nobody in the case note owns | Invented owner (fluently wrong) | Corrupting |
| A correct summary, but formatted as a paragraph and 140 words | Format drift + length | Cosmetic-to-blocking, depending on the downstream template |
| "I'm sorry, I can't help with that request." | Refusal | Blocking, and possibly correct |
| The same input, run twice, gives different next actions | Variation between runs | Corrupting if either is acted on |

What to point at afterwards: the second row is the one that costs money, and nothing about it looks wrong. Then ask the room which of the five they would have reported, and let the silence do the teaching. The follow-up question is the practical one: what would have caught it? A named-owner field checked against the case note — which is a design change, not a recognition skill, and that is the correct conclusion.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show the invented-owner summary and ask for a show of hands: would you have sent this? Most hands go up.
2. **State the objective** — by the end you will name a symptom without a cause, grade its severity, and capture the evidence.
3. **Recall prior learning** — ask how they report a fault to facilities: what they say, what they photograph, what they avoid claiming.
4. **Present the content** — teach the eight symptoms, the three severities, and the observation sentence.
5. **Guide** — write observation sentences for two of the five outputs together, refusing every causal verb offered.
6. **Elicit performance** — pairs generate outputs from their own prompt and grade five of them.
7. **Give feedback** — the room votes on severity. Disagreements are the lesson: severity depends on the reader, and the reader must be named.
8. **Transfer** — each learner adds "capture before retry" to their working habits and reports one corrupting failure they have seen.

## What the framework doesn't mention but trainers need to know

- **Corrupting failures are under-reported by design.** Nobody reports an output they did not notice was wrong. Ask the room for the one they *did* notice late, and the room will go quiet in a useful way.
- **Severity needs a named reader.** "Is this serious" is unanswerable; "would the duty manager act on it differently" is answerable.
- **Variation is a symptom in its own right.** A task that works three times in four cannot be automated without a check, and that is a fact worth writing down rather than a mood.
- **Recognition is a cultural skill.** In teams where reporting a bad output is treated as incompetence, only blocking failures get reported, and the corrupting ones reach the customer.

## Watch out

- **Do not accept "hallucination" as a description.** Ask for the sentence that was wrong and the line in the source that contradicts it.
- **Do not demo only blocking failures.** They are dramatic and they teach the wrong risk profile.
- **Do not blame the learner for a prompt issue, and do not let them blame the model for one either.** The point is routing, not fault.
- **The stale claim to retire:** "you can tell when AI is wrong because it sounds confident." Confidence and correctness are unrelated; the source is the test.
