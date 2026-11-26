---
id: 05.01.B.A1
tsc: 5
level: Basic
code: A1
title: Collect user feedback on generated content
as_at: 2026-11-26
review_by: 2027-02-25
---

# Collect user feedback on generated content

> **TSC #5 Generative AI Model Evaluation · Basic · Ability A1**


> **Framework text (verbatim):** "Collect user feedback on generated content."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Ability · Bullet 7 of 11

**One-line version:** Collecting feedback is not "ask people what they thought" — it is designing the question so the answer is specific, and capturing what people *do* with the output, not just what they say.

## What it is

This is the hands-on ability to gather usable feedback on generated content: decide what to ask, who to ask, and how to capture both the words and the behaviour. The output is not a pile of opinions — it is a set of specific, attributable findings that can be turned into improvements.

## Deep expansion

### The concept

Feedback is only useful if it can be acted on. "It was good" and "it was bad" cannot be. The ability is to design collection so that every response names *what* specifically worked or failed, *for which task*, and *for whom* — and to capture the silent behavioural signals (copy, edit, regenerate, abandon) that users would never think to report. A well-run feedback collection turns evaluation from a one-off judgement into a repeatable measurement.

### The sub-concepts

**Who to ask.** The end user, not the builder. The person who actually has to use the output — send the email, file the report — has the feedback that matters. Ask the wrong person and you collect enthusiasm or complaints, not usefulness data.

**What to ask.** Non-leading, specific questions. "What did you have to fix before you could use it?" beats "Was it helpful?" every time, because it forces a concrete answer instead of a polite one.

**How to capture behaviour.** Copy events, edit distance (how much the user changed the draft), regeneration count, time-to-abandon. These are free, continuous, and honest, and they do not depend on anyone filling in a form.

**How to record it.** Feedback with no attribution is noise. Capture *what* task, *which* output, *who* the user, *what* they changed — or the finding cannot be traced to a cause.

### How it connects to the rest of the framework

This is the ability that feeds the entire evaluation loop. `TSC5-Basic-K3` is the knowledge (qualitative methods) it rests on; `TSC5-Basic-A2` (interpret metrics) is what you do with the *numeric* half; `TSC5-Basic-A3` (propose improvements) is the next step after this one — you collect the feedback, then you act on it. The chain is collect → interpret → improve.

### What is current as of November 2026

The modern reality is that **most feedback is now captured automatically, not collected by hand.** Chat products log copy, edit, regenerate and rating events natively, so the ability has shifted from "run a survey" to "read the telemetry and design the missing questions". A Basic practitioner should be able to do both: interpret the built-in behaviour logs, and design the one or two targeted questions the logs cannot answer (why did you abandon it, what did you actually use it for).

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"More feedback is better feedback."* More *unattributed, vague* feedback is just noise at scale. One specific finding beats a hundred "good job" responses.
- *"A survey is the way to collect feedback."* A survey captures what people *say*; behaviour captures what people *do*. For most evaluation, the behaviour is the more honest half.
- *"No complaints means no problems."* Silence usually means people found a workaround or stopped using the tool, not that it worked.

## How a student should understand it

**Mental model:** a restaurant owner who wants to know if the new dish works — she watches which plates come back half-eaten and what regulars actually reorder, and only then asks one pointed question of the people who did not reorder.

**Three things they can do after this bullet:**
1. Write one non-leading feedback question that would surface a real problem, not a polite "yes".
2. Name two behavioural signals they could capture for an AI output in their own work, and how.
3. Record one feedback item with full attribution: task, output, user, and what changed.

**Misconceptions to kill:** more = better, survey = the whole job, and silence = success.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker who reads the plates.** The stall owner does not ask every customer "was your meal good?" — she watches what comes back. Half-eaten plates, untouched sides, the dish that regulars stopped ordering: that is behavioural feedback, and it is more truthful than any comment card. The comment card (the survey) is only for what the plates cannot tell her.

**The colleague's red pen.** When you ask a colleague to review a draft and they say "looks good" but return it covered in edits, the edits are the feedback and the "looks good" is noise. Good collection asks for the red pen directly.

### Worked example with a real tool

Have a learner generate an output and run a two-question collection on a partner, structured so the answer is specific:

```
Draft a short weekly status update for your team.

Give it to a partner, who answers exactly these two questions:
1. Name ONE specific thing you would change, and why.
2. Would you send this as-is to your own team? Yes or no.
```

What to point at afterwards: the "one specific thing" answer is actionable; the yes/no is a blunt behavioural proxy; and the two together are richer than any five-star scale. Then add the behavioural layer: ask the partner whether they would have *copied* it, *edited* it, or *abandoned* it — and note which is the most honest signal.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room: "who here has rated something five stars and never used it again?" The gap is the topic.
2. **State the objective** — you will collect feedback that is specific, attributable, and actable.
3. **Recall prior learning** — they know the four criteria and qualitative methods; this is the collection half.
4. **Present the content** — who to ask, what to ask, behaviour vs words, how to record.
5. **Guide** — run the two-question exercise once, together, on a shared output.
6. **Elicit performance** — each learner collects structured feedback on their own output from a partner.
7. **Give feedback** — flag the leading questions that slipped in, and the vague answers that slipped out.
8. **Transfer** — for their next real AI task, they log one behavioural signal and one targeted question.

## What the framework doesn't mention but trainers need to know

- **Behaviour beats self-report.** The framework says "collect feedback" and most people picture a form. The modern, high-leverage version is reading copy/edit/regenerate telemetry. Teach the plates before the comment card.
- **Feedback needs a schema.** Without task, output, user and change recorded together, feedback cannot be traced to a cause and is worthless. This is the single discipline that separates evaluation from anecdote.
- **Ask the person who uses it, not the person who built it.** Builders collect validation; users give you the truth. The trainer should model this by collecting feedback from the *audience* of the output, not its author.

## Watch out

- **Do not teach a survey template and stop.** The framework's phrase is the entry point; the real ability is behaviour-plus-targeted-question. A survey-only lesson produces learners who collect polite yeses and call it evaluation.
- **Do not let learners collect feedback on each other's output and call it "user" feedback.** A peer is not the end user. Model the distinction or the exercise teaches the wrong habit.
- **The stale claim to retire:** "we asked everyone and they all liked it, so it's validated." Popularity is not performance; a collection that only finds agreement was designed to find agreement.
