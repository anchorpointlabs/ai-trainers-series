# Library Entry Template

Every TSC entry is one file, one knowledge/ability item. Filename is a descriptive kebab-case slug of the title. This is the **rich format** — model it on `TSC-01-B-GenAI-Principles/purpose-of-generative-ai.md`, the reference entry.

## YAML frontmatter (required)

```yaml
---
id: 01.01.B.K1
tsc: 1
level: Basic
code: K1
title: The purpose of generative AI: five things it is actually for
as_at: 2026-11-26
review_by: 2027-02-25
---
```

- `id` — stable ID `NN.MM.L.code` (see `naming-convention.md`).
- `level` — `Basic` / `Intermediate` / `Advanced`.
- `code` — the IMDA K/A code.
- `as_at` / `review_by` — set by `python scripts/living.py stamp YYYY-MM-DD`; review_by = as_at + 91 days.

## Body (fixed order)

```markdown
# <Title>

> **TSC #<n> <Topic> · <Level> · <Knowledge|Ability> <code>**

> **IMDA requirement:** "<the framework item, quoted word-for-word>"
> **TSC #<n>** <Topic> · <Level> · <Knowledge|Ability> · Bullet <X> of <Y>

**One-line version:** <one memorable line that captures the idea>

## What it is
<2–3 sentences — the plain definition.>

## Deep expansion

### The concept
<the key idea, why it matters, what changes for the learner.>

### The sub-concepts
<each with a **bold lead**, e.g. **Mode.**, **Generation versus retrieval.**>

### How it connects to the rest of the framework
<name the related bullets by code, e.g. "TSC1-Basic-K03 is the what…".>

### What is current as of <month year>
<what changed for THIS topic, in one to three sentences. Models, versions and prices live in the Living Register.>

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions
<stated the way learners say them, each with the correction.>

## How a student should understand it

**Mental model:** <one image or sentence — a fast junior colleague, a magic wok, a goldfish with a PhD.>

**Things they can do after this bullet:**
1. <observable outcome>
2. <observable outcome>

**Misconceptions to kill:** <the 2–3 to target first.>

## How a trainer explains it

### Analogies that work in a Singapore classroom
<one or two concrete analogies — hawker, PSLE, CPF, HDB, polyclinic. State where each breaks.>

### Worked example with a real tool
<the exact prompt to type, and what to point at afterwards.>

### Lesson plan (Gagné's nine events)
1. **Gain attention** — <hook>
2. **State the objective** — <what they will be able to do>
3. **Recall prior learning** — <connect to what they know>
4. **Present the content** — <teach it>
5. **Guide** — <work one example together>
6. **Elicit performance** — <learners do it>
7. **Give feedback** — <debrief / correct>
8. **Transfer** — <apply to their own work>

## What the framework doesn't mention but trainers need to know
<extra insights the framework misses but the classroom needs.>

## Watch out
<pitfalls for the trainer — what not to demo, what not to overclaim, the stale claim to retire.>
```

## Writing rules

1. **IMDA requirement is quoted word-for-word** — never paraphrase the anchor (WSQ/SSG accreditation depends on exact wording).
2. **Lesson plan follows Gagné's nine events** — no fixed timings; the trainer decides.
3. **One or two strong analogies, Singapore footing** — they must survive a sceptic.
4. **The worked example uses a real prompt** the learner types, with what to point at afterwards.
5. **Common misconceptions stated the way learners say them**, then corrected.
6. **No invented statistics, studies or dates.**
7. **"What is current as of…" carries only this topic's change** and ends with the Living Register pointer. Products, versions and prices go in the register. Re-date it with `scripts/living.py stamp` when reviewed.
8. **~800–1,200 words.** One page in the browser, teachable in a class.
