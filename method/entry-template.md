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

**Bullet (verbatim):** <the IMDA bullet, word for word>

**What it means:** <plain language — explain it to a colleague, no jargon. 2-4 sentences.>

**The learner must be able to:**
- <observable ability>
- <observable ability>

**How to teach it in 20 minutes:**
1. <step with minutes> (x min)
2. ...

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

1. **Verbatim bullet** — quote IMDA exactly; never paraphrase the anchor.
2. **One analogy per entry** — concrete, Singapore footing (hawker, PSLE, CPF, HDB, polyclinic). It must survive a sceptic.
3. **The exercise uses a real prompt** the learner types and a stated expected result.
4. **Common mistakes are stated the way a learner says them**, then corrected.
5. **No invented statistics, studies or dates.** If a number is not certain, describe the direction.
6. **Link the core-knowledge source** — `[file](../core-knowledge/file.md) (section n)`.
7. **~450-600 words.** One page, teachable in a class.
