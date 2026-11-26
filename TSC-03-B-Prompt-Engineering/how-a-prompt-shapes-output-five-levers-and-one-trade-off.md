---
id: 03.01.B.K2
tsc: 3
level: Basic
code: K2
title: How a prompt shapes output: five levers and one trade-off
as_at: 2026-11-26
review_by: 2027-02-25
---

# How a prompt shapes output: five levers and one trade-off

> **TSC #3 Prompt Engineering · Basic · Knowledge K2**


> **Framework text (verbatim):** "Principles of how prompts shape AI-generated content."
>
> **TSC #3** Prompt Engineering · **Basic** · Knowledge · Bullet 2 of 15

**One-line version:** A prompt does not command the model — it narrows the set of answers the model finds plausible, and every constraint you add buys predictability with robustness.

## What it is

A prompt shapes output because the model's only job is to continue what it has been given, in the most probable way. The prompt is the first part of that continuation, so it decides which of the model's many stored patterns gets used. Understanding the principles means knowing which parts of a prompt move which part of the answer, and where the moving stops being free.

## Deep expansion

### The concept

The mental error to remove first is the order-giving one. Learners write as though a prompt were a memo to a subordinate who will do what it says or come back with questions. The model does neither: it produces the answer that best fits the whole situation you have described, including the parts you described by accident.

So a prompt works by conditioning. Five levers do almost all of it:

- **The operation** — the verb. "Summarise", "rewrite", "critique", "classify", "draft" select different behaviour from the same material, and choosing the wrong verb is the most common reason a good prompt disappoints.
- **The material** — the facts, rows, or document supplied. A prompt cannot make the model use knowledge it was not given about your case; it can only make it use that knowledge well or badly.
- **The reader** — who receives the output. This sets register, level of explanation, and what counts as obvious.
- **The container** — length, structure, format. This is the lever learners reach for first because it is the easiest to check.
- **The boundary** — what must not appear: no invented figures, no names, no promises about timing, no speculation about a colleague's motives.

Each lever narrows. That is the whole mechanism, and it is also where the trade-off lives.

### The sub-concepts

**Specificity is a curve, not a dial.** Too little constraint and you get the average of everything the model has seen — fluent, generic, and usually wrong for your reader. Too much constraint and you get exactly the shape you asked for with content squeezed to fit it: the eight required bullet points become eight thin ones, the mandated table invents cells to fill. The right amount is the least constraint that makes your check passable.

**Position carries weight.** The opening line sets the frame; the last line sets the immediate task. An instruction buried in the middle of two thousand words of pasted policy is the instruction most likely to be dropped. Practitioners put the task at the end when the material is long, and the rules immediately after it.

**Facts in, not facts implied.** The model will not tell you it lacked the number you forgot to attach. It will produce a plausible number, in the right format, with the same confident tone as the correct ones. This is the single most expensive principle in the list.

**Register has a price.** Asking for "warm and professional" often produces a warm professional nothing. Tone instructions pull prose toward the middle of the genre. If the content matters, specify the content and edit the tone by hand.

**Constraints conflict silently.** "Be concise" and "explain the reasoning" cannot both fully hold. The model picks one and drops the other without telling you, so the prompt that contains both is not stricter — it is ambiguous.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-K2` (Prompt Design); see that entry for the user-level basics. `TSC3-Basic-K1` is the design posture, `TSC3-Basic-K3` turns these levers into named techniques, `TSC3-Basic-K4` shows how each lever behaves in a different output mode, and `TSC3-Basic-A3` is how you test whether a change to a lever actually helped.

### What is current as of November 2026

Two changes matter. First, current frontier models follow long, conflicting constraint lists noticeably better than their predecessors did, which shifts the practitioner's problem from "will it obey" to "did I ask for the right thing". Second, the folklore tricks have aged badly: capital letters, repetition, flattery and threats were crude ways of adding weight to an instruction, and on current models they are unreliable at best and noise at worst. Structure — headings, numbered rules, a labelled input block — now does the work that shouting used to be asked to do.

A third, quieter change: longer context windows encouraged people to paste everything. Attention is still not uniform across a very long input, so more material has not made position irrelevant.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"More words means more control."* More words means more competition for attention. Control comes from the checkable parts.
- *"If I say it twice it is twice as likely."* Repetition mostly signals that the prompt has no structure. Fix the structure.
- *"Tone instructions are free."* They cost content, because the model will trade specificity for the adjective it was told to hit.
- *"A prompt can fix a knowledge gap."* It can stop the model guessing, which is different and usually more useful.

## How a student should understand it

**Mental model:** you are not giving orders to a junior; you are briefing a very widely read freelancer who will guess what you meant from the brief alone, and who has never met your customer.

**Things they can do after this bullet:**
1. Point at a prompt and say which lever each sentence is pulling, or that it is pulling none.
2. Diagnose a generic answer as under-constraint and a hollow answer as over-constraint.
3. Rewrite a prompt so the task sits where attention is strongest.

**Misconceptions to kill:** that prompts are commands; that specificity is always an improvement; that the model will flag missing information.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The zi char order.** "Cook me something nice" gets you the average of the menu. "Fish head curry, less oil, no okra, for four, takeaway" gets you dinner. Where it breaks: the stall has fixed recipes and a fixed repertoire; the model has read everything, including dishes nobody in your family would order — so an under-specified prompt ranges wider than any stall would.

**The tailor.** More measurements give a better fit. A hundred measurements on one posture give a shirt that fits nobody else and exposes every measurement you took wrong. Where it breaks: a tailor will ask you to stand still and re-measure; the model takes your numbers on faith.

### Worked example with a real tool

One task, three levels. Ask ChatGPT or Claude to reply to a customer complaint, changing only the amount of constraint:

```text
Level 1: Write a reply to this customer complaint.
Level 2: Write a 120-word reply to this complaint for a customer who has
been waiting six days for a refund. Acknowledge the delay, state what
happens next and by when, no apology for "any inconvenience".
Level 3: Write a 120-word reply. Use exactly 3 short paragraphs. Paragraph 1
must begin with the words "Thank you for writing in". Do not use the words
"unfortunately", "valued" or "feedback". Include the case number
SG-2026-4471 twice, once in the first sentence and once in the last.
```

Run all three on the same complaint. Level 1 gives a competent letter addressed to nobody. Level 2 gives something a manager would actually sign. Level 3 gives a letter that satisfies every instruction and reads like a form — the case number is there, the warmth is not. What to point at: the difference between Level 2 and Level 3 is not effort, it is that the constraints stopped serving the reader and started serving the checklist.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read the Level 1 output aloud. Ask who would send it. Nobody.
2. **State the objective** — by the end you will name which lever a sentence pulls and add or remove constraint deliberately.
3. **Recall prior learning** — compare to briefing a contractor: scope, materials, deadline, exclusions. Same five levers.
4. **Present the content** — teach the five levers, then the specificity curve, then position.
5. **Guide** — annotate the three-level example together, marking each sentence with its lever.
6. **Elicit performance** — pairs take a prompt from their own work and mark every sentence "lever or noise", then delete the noise.
7. **Give feedback** — run the trimmed prompts, compare before and after, and name which removal changed the output.
8. **Transfer** — each learner commits to one lever they will always specify, and one they will stop over-specifying.

## What the framework doesn't mention but trainers need to know

- **The verb is the cheapest improvement available.** Swapping "improve this" for "cut this to 100 words without losing any figure" changes more than any amount of added context. Trainers should drill verbs.
- **Constraint conflicts are the quiet killer.** Two rules that cannot both hold produce a confidently compromised answer. Teach learners to read their own prompt looking for fights.
- **Under-constraint looks like success.** A generic answer is pleasant, fast and useless, and learners accept it because nothing about it looks broken.
- **Position advice inverts in the API.** With a long system prompt, the durable rules belong in the system message, not repeated in the user turn. Chat-only learners never see this layer, and it is where team prompts actually live.

## Watch out

- **Do not sell "the model ignores you unless you shout".** That advice circulates widely and it teaches a habit that will not survive the next model.
- **Do not demo only the failing case.** Show a well-constrained prompt too, or the lesson becomes "AI is unreliable" rather than "constraint is a design choice".
- **Do not confuse a specificity exercise with a quality exercise.** Level 3 in the worked example is more constrained and worse — say so out loud, or the room learns the wrong lesson.
- **The stale claim to retire:** "temperature and creativity are the same dial." Temperature changes variance; it does not add judgement.
