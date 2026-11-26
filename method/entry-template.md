# Library Entry Template

Every TSC entry is one file, one knowledge/ability item. Filename is a descriptive kebab-case slug of the title (e.g. `conditional-prompts-context-manipulation-refining.md`), never a code like `k2.md`.

## YAML frontmatter (required)

```yaml
---
id: 02.01.B.K7
tsc: 2
level: Basic
code: K7
title: Concept of prompt design
---
```

- `id` — stable ID `NN.MM.L.code` (see `naming-convention.md`).
- `level` — `Basic` / `Intermediate` / `Advanced`.
- `code` — the IMDA K/A code.

## Body (fixed order)

```markdown
# <Title>

> **TSC #<n> <Topic> · <Level> · <Knowledge|Ability> <code>**

**IMDA requirement:** <the framework item, quoted word-for-word>

**What it means:** <plain language — explain it to a colleague, no jargon. 2-4 sentences.>

**The learner must be able to:**
- <observable ability>
- <observable ability>

**Lesson Plan Ideas:**
1. <gain attention — open with a hook>
2. <state the objective>
3. <recall prior learning>
4. <present the content>
5. <guide — work one example together>
6. <practise — learners do it>
7. <feedback — debrief>
8. <transfer — apply to their own work>

**Exercise (with the exact prompt):**
```text
<exact prompt the learner types>
```
Expected: <what a correct run looks like>

**Common mistakes:**
- <mistake as a learner would state it, then the correction>

**Sources:**
- <IMDA framework PDF URL>
- [<file>](../core-knowledge/<file>.md) (section <n>)
```

## Writing rules

1. **IMDA requirement is quoted word-for-word** — never paraphrase the anchor (WSQ/SSG accreditation depends on exact wording).
2. **Lesson Plan Ideas follow Gagné's nine events of instruction** — gain attention, state the objective, recall prior learning, present, guide, elicit performance, give feedback, transfer. No fixed timings; the trainer decides.
3. **One analogy per entry** — concrete, Singapore footing (hawker, PSLE, CPF, HDB, polyclinic). It must survive a sceptic.
4. **The exercise uses a real prompt** the learner types and a stated expected result.
5. **Common mistakes are stated the way a learner says them**, then corrected.
6. **No invented statistics, studies or dates.**
7. **Link the core-knowledge source** — `[file](../core-knowledge/file.md) (section n)`.
8. **~450-600 words.** One page, teachable in a class.
