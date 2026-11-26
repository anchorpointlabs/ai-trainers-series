---
id: 03.01.B.A1
tsc: 3
level: Basic
code: A1
title: The seven parts of a prompt, and which ones you can drop
as_at: 2026-11-26
review_by: 2027-02-25
---

# The seven parts of a prompt, and which ones you can drop

> **TSC #3 Prompt Engineering · Basic · Ability A1**


> **Framework text (verbatim):** "Define the fundamental elements of a prompt."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 8 of 15

**One-line version:** The elements of a prompt are a diagnostic checklist, not a form to fill in — their value is in naming which one is missing when the output disappoints.

## What it is

The fundamental elements are the pieces a prompt is assembled from: the task, the context or facts, the reader, the constraints, and the output format. Two more belong in any prompt that will be run more than once — the definition of done, and the instruction for what to do when the input is unfit. Naming all seven is the easy part; knowing which to drop is the ability.

## Deep expansion

### The concept

Taught badly, this bullet produces a template with seven headings that learners fill in obediently, producing long prompts that are no more reliable than short ones. Taught well, it produces a review habit: when an answer disappoints, run down the list and find the element that was absent.

The seven, in the order they should be decided:

1. **Task** — the operation, in a verb. Summarise, classify, rewrite, draft, extract, compare. If two verbs are present ("analyse and improve"), you have two tasks and one output, which is where mush starts.
2. **Context** — the facts the model may use. Supplied, not implied. The single biggest cause of confidently wrong output is a fact the writer knew and did not type.
3. **Reader** — who receives it. This sets register, assumed knowledge and length far more reliably than adjectives like "professional".
4. **Constraints** — what must and must not appear: word limits, banned claims, mandatory inclusions, tone limits.
5. **Format** — the shape: table with named columns, numbered list, JSON with these keys, three paragraphs.
6. **Definition of done** — how you will know it worked. This is the element the user-level list usually omits, and it is the one that turns a prompt into a specification.
7. **Failure instruction** — what to do when the input does not support the task: say so, stop, ask, or return a fixed string.

Elements 6 and 7 cost one line each and prevent the two most expensive failures: an answer that looks finished and is not, and an answer that invents what it lacks.

### The sub-concepts

**Order matters, not just presence.** Context, then task, then rules, then input, then format reminder. A task stated before the material is a task the model holds while reading; a task stated after 2,000 words of material is the one it is most likely to act on — which is why long prompts often repeat the task at the end, deliberately.

**Every element costs attention.** A seven-element prompt for a two-sentence request is bloat. Short-lived prompts need task, context and format. Prompts that others will run need all seven.

**The reader element is the most under-used.** Rooms full of people write "professional tone" and skip "this goes to a customer who has already complained twice". The second is usable; the first is wallpaper.

**Format is a check, not a decoration.** If you cannot specify the shape, you cannot check the answer cheaply, and an unchecked answer becomes someone's problem later.

**The failure instruction is the element learners resist.** It feels like planning for failure. It is actually the difference between a prompt that reports a gap and one that fills it.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A5` (Prompt Design); see that entry for the user-level basics of task, context, audience, constraints and format. `TSC3-Basic-K2` explains why each element moves the output, `TSC3-Basic-A4` turns the list into review practice, `TSC3-Basic-K7` is built almost entirely from elements 4, 6 and 7, and `TSC3-Basic-A3` is how you compare two assemblies of the same elements.

### What is current as of November 2026

Current models need less ceremonial framing than their predecessors did. Role statements ("you are a world-class analyst") have become largely decorative; explicit rules, an output schema and a supplied source do the work. Structured output modes have also absorbed element 5 — where the platform supports a schema, format is enforced rather than described, and the prompt only needs to say which schema.

What has grown instead is the input element. With long context, the material supplied is often the largest part of the prompt, and the practitioner's skill has moved from writing instructions to labelling inputs: this block is the source, that block is the example, this block is the question.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A good prompt has all the elements."* A good prompt has the elements the task needs. Filling the form is how prompts become unmaintainable.
- *"Longer context always helps."* Unlabelled context competes with the instruction. Label it or leave it out.
- *"Format is cosmetic."* Format is how the answer becomes checkable.
- *"If I explain the background well, it will know what I want."* Background explains the world; the task states the operation. Both are needed and they are not substitutes.

## How a student should understand it

**Mental model:** a renovation quotation. Scope, materials, timeline, exclusions, payment terms. A quote with no exclusions is where the argument starts — and the exclusions are the failure instruction.

**Things they can do after this bullet:**
1. Label the seven elements in any prompt, including their own.
2. Diagnose a disappointing answer by naming the missing element rather than rewriting everything.
3. Decide, for a short task, which elements to drop and say why.

**Misconceptions to kill:** that the list is a template; that format is decoration; that context can substitute for a task statement.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The renovation quote.** A contractor who quotes a price but no scope, no materials and no exclusions is not cheaper — he is just holding the argument for later. Where it breaks: a quotation is negotiated and signed, while a prompt is executed immediately and without discussion, so a missing exclusion becomes a silent assumption rather than a phone call.

**The zi char order slip.** The kitchen writes: table, dish, portion, "no chilli", "less oil", time. Six fields, and the one that is missing is the one the customer complains about. Where it breaks: a stall's slip is standardised across every table, while a prompt's elements change with the task — copying the slip is not the skill.

### Worked example with a real tool

Take a prompt a learner might actually type, and annotate it:

```text
[TASK] Draft a reply to this customer complaint.
[READER] The customer has already written in twice and has been waiting a week.
[CONTEXT] Use only the case notes below.
[CONSTRAINTS] 120 words maximum. No compensation offers. No promises of dates.
[FORMAT] Three short paragraphs; last line is "Ref: <order number>".
[DONE] A colleague reading it can say what happens next and by when.
[FAILURE] If the case notes contain no action taken, write
"NOT IN SOURCE" instead of describing one.
```

What to point at afterwards: delete the READER line and run it again — the answer becomes a generic apology. Delete the FAILURE line and run it on an incomplete case — an action appears from nowhere. Restore both and the prompt is longer by two lines and dramatically more predictable. That is the whole lesson, demonstrated in two runs rather than asserted.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out a prompt with an obvious missing element and ask what the output will get wrong before generating it.
2. **State the objective** — by the end you will label the seven elements in a prompt and diagnose a failure by the missing one.
3. **Recall prior learning** — ask what goes into a good email to a contractor: what, for whom, by when, and what to do if something is unavailable.
4. **Present the content** — teach the seven elements in decision order, then the drop rule for short tasks.
5. **Guide** — annotate the complaint prompt together, then delete elements one at a time and predict the failure before running.
6. **Elicit performance** — each learner annotates two prompts from their own work and finds one missing element in each.
7. **Give feedback** — run the predictions. Where the room predicted wrong, the element was doing less work than assumed — a useful correction.
8. **Transfer** — each learner adds a done-check and a failure line to one prompt they will use this week.

## What the framework doesn't mention but trainers need to know

- **Two verbs is a design smell.** "Analyse and rewrite" produces a rewrite with no analysis, or an analysis with a token rewrite. Split it into two prompts or sequence them.
- **The done-check is the element that survives staff turnover.** Formats and constraints can be read off the prompt; "what good looks like" usually lives in someone's head until it is written down.
- **Elements interact.** A tight word limit plus a long list of mandatory inclusions produces compression, and compression drops the least-repeated item. That is a predictable failure, not a mystery.
- **Learners will ask for the template.** Give them the checklist, not a form. The form teaches compliance; the checklist teaches diagnosis.

## Watch out

- **Do not hand out a fill-in-the-blanks template as the deliverable.** It produces uniform prompts and no judgement.
- **Do not teach format as "make it look nice".** Teach format as the cheapest possible check.
- **Do not skip the failure instruction because it is depressing.** It is the single most useful line in the list.
- **The stale claim to retire:** "start every prompt with 'act as'." Personas are decoration on current models; rules and supplied sources are not.
