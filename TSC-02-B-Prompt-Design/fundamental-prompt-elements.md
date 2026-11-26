---
id: 02.01.B.A5
tsc: 2
level: Basic
code: A5
title: Fundamental prompt elements
---

# Fundamental prompt elements

> **TSC #2 Prompt Design · Basic · Ability A5**

> **Framework text (verbatim):** "Define the fundamental elements ofs a prompt."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 8 of 15

**One-line version:** Five parts do the work — task, context, audience, constraints, format — and a good prompt uses the three or four that this job actually needs.

## What it is

A prompt is a request or instruction given to an AI tool. Its parts can be named: the **task** says what to do, the **context** supplies the facts and background it depends on, the **audience** is who will read the result, **constraints** are the limits (a word count, a ban on invention), and **format** is the shape of the answer (a list, a table, two labelled lines). These are useful elements to consider, not a compulsory formula.

## Deep expansion

### The concept

The five elements are a checklist for diagnosis, not a template to fill. Learners who treat them as a form write bloated prompts with an "audience:" line for a task that has no reader, and then wonder why the output is worse. The real skill is knowing which elements a given job cannot do without.

A workable rule: **task and context are almost always required; audience, constraints and format are the ones you add when their absence caused a failure last time.** A summary for yourself needs task and context. A notice for members needs audience and length. A table going into a spreadsheet needs format, stated exactly.

There is a deeper version of the same list that trainers should know even if they do not teach it at Basic level. Production prompts often carry seven parts: role or system identity, task, context, constraints and guardrails, output format, worked examples, and an evaluation criterion the model checks itself against before answering. The last one — "before you answer, verify that every figure appears in the source" — is the one Basic prompts almost never include and almost always benefit from.

### The sub-concepts

**Task is a verb, not a topic.** "Library closure" is a topic. "Write a two-sentence notice about the closure" is a task. Learners routinely name the subject and assume the action is implied; then they get an essay when they wanted a notice.

**Context is what the task runs on.** Facts, notes, source text, rules. Keep it visually separate from the instruction — a blank line, a delimiter, a heading — so neither the model nor a colleague reading it has to guess where the facts end.

**Audience is a separate element from context.** "New volunteers" is not background information about the garden; it is a specification of who the words are for, and it changes vocabulary, tone and how much can be assumed.

**Constraints are limits; format is shape.** "No more than 12 words" is a constraint. "Exactly two bullet points" is a format. Learners merge the two, which makes their feedback vague: the output was too long *and* had three points, and they cannot say which instruction failed.

**Ordering is an element too.** Instructions at the start and the end of a long prompt carry more weight than instructions buried in the middle. If a prompt contains a long pasted document, repeat the key constraint after it.

**Elements can be left out on purpose.** Knowing which to drop is design. "Write three subject lines for an internal newsletter" needs neither audience nor context — adding them would be padding.

### How it connects to the rest of the framework

`TSC2-Basic-K7` is the concept these elements serve; `TSC2-Basic-K2` explains why each element changes the output; `TSC2-Basic-A1` covers techniques (examples) that sit alongside them; `TSC2-Basic-A6` turns the element list into a set of habits. In production terms, the seven-part version is the same anatomy at `TSC3-Basic-A1`.

### What is current as of November 2026

Interfaces now supply some elements for you. Saved instructions and project memory act as standing context; structured-output settings act as enforced format; role settings act as system identity. That means fewer elements need to be typed, and more need to be *checked* — a learner who does not know what is in their saved instructions cannot tell whether the prompt or the standing brief produced a particular answer. The late-2026 frontier models — OpenAI's GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — are also more tolerant of an element being implied rather than stated, which is a gift to experienced writers and a trap for beginners who never learn to state it.

### Common misconceptions

- *"Every prompt should have all five elements."* That produces padding, not precision. Use what the job needs.
- *"The topic is the task."* A subject is not an action.
- *"Audience and context are the same thing."* One is who reads it; the other is what it is built from.
- *"A word limit is a format."* Limit and shape are two different instructions, and they fail separately.

## How a student should understand it

**Mental model:** a job card at a workshop. Who asked, what to make, out of what material, to what size, in what shape. Any card missing a line produces a part that gets returned.

**Things they can do after this bullet:**
1. Label the five elements in any prompt, including a colleague's.
2. Say which element is missing when an output disappoints.
3. Write a prompt using only the elements the task requires — and defend the omissions.

**Misconceptions to kill:** the topic-as-task error; audience confused with context; limit confused with format.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tailor's order slip.** Measurement, fabric, cut, delivery date, name on the ticket. Miss the delivery date and you get a beautiful shirt next month. Miss the fabric and you get the shirt in the shop's default cloth. Where it breaks: a tailor will phone you about a missing measurement; the model will choose one.

### Worked example with a real tool

```text
Write a notice for new volunteers at a fictional community garden.
The tool shed will be closed on Tuesday for repairs. Volunteers should collect tools from the main desk instead.
Use only those facts. Write exactly two bullet points, each no more than 12 words: one about the closure and one about collecting tools.
```

What to point at afterwards: four of the five elements are visible — task ("write a notice"), context (the closure and the collection point), audience ("new volunteers"), constraints ("use only those facts", "no more than 12 words") and format ("exactly two bullet points"). Then ask which element would change if this notice were going on a public noticeboard instead of to volunteers, and let the room find that audience is the only difference. Finally, delete the word limit and rerun: the bullets grow, which shows a constraint doing its job in a way nobody can argue with.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If you asked someone to write a notice, what would they need to know?" Collect answers and sort them into the five elements on the board.
2. **State the objective** — by the end you can define the five elements and label them in a real prompt.
3. **Recall prior learning** — the task/background split from `TSC2-Basic-K7`, now with audience and limits added.
4. **Present the content** — the five elements, the limit-versus-shape distinction, and permission to omit.
5. **Guide** — label the garden prompt together, arguing about the borderline cases.
6. **Elicit performance** — pairs label a prompt from their own workplace and mark any element they would add.
7. **Give feedback** — compare labels; use disagreements to sharpen definitions rather than to declare a winner.
8. **Transfer** — each learner rewrites one recurring request using only the elements it needs.

## What the framework doesn't mention but trainers need to know

- **The elements are diagnostic, not generative.** Their best use is after a bad output: which element was missing?
- **Order matters as much as presence.** The same five elements in a different sequence can perform differently, especially with a long context block.
- **Self-check criteria are the missing sixth element.** A line like "before replying, confirm each figure appears in the notes" catches a class of errors nothing else does.
- **Learners will ask for a template.** Give them the elements and the rule for choosing, not a fill-in-the-blanks form; forms produce compliance, not judgement.

## Watch out

- **Do not present the five as a formula.** The moment it becomes a form, the room stops thinking about the task.
- **Do not skip the omission case.** Show a good prompt that uses only two elements, or the lesson teaches padding.
- **Do not confuse limit and shape in your own feedback.** If you blur them, the class will too, and their revisions will be guesswork.
- **The stale claim to retire:** "a good prompt has a role, a task, context, examples and a format." In November 2026 that stack is one option among several, and for a short internal task it is three elements too many.
