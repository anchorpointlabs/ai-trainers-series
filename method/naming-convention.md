# Naming convention

How folders and entries are named, so anyone can find a thing and cite it unambiguously.

## TSC folders

```
TSC-NN-{B|I|A}-{Topic}/
```

- `NN` — the TSC number (01–09), zero-padded.
- `{B|I|A}` — proficiency: `B` = Basic, `I` = Intermediate, `A` = Advanced.
- `{Topic}` — a short kebab-case topic.

The TSC number and level are also in each entry's YAML — the folder name never carries a
`[NN]` prefix.

Examples:

- `TSC-01-B-GenAI-Principles/`
- `TSC-02-B-Prompt-Design/`
- `TSC-03-I-Prompt-Engineering/`

## The nine TSCs and their levels (authoritative)

Source: *Skills Framework for ICT — Skills in Generative AI* (IMDA, March 2025).

| TSC | Topic | Levels |
|---|---|---|
| #1 | Generative AI Principles and Applications | B · I |
| #2 | Prompt Design | B |
| #3 | Prompt Engineering | B · I · A |
| #4 | Generative AI Model Selection | I · A |
| #5 | Generative AI Model Evaluation | B · I · A |
| #6 | Generative AI Application Development and Deployment | B · I · A |
| #7 | Generative AI Model Development and Fine Tuning | B · I · A |
| #8 | Responsible AI and Generative AI Practices | B · I · A |
| #9 | Generative AI Models — Technical Aspects of Security and Ethics | B · I · A |

One folder per level. A TSC that spans all three gets three folders, all sharing the same
topic slug:

```
TSC-03-B-Prompt-Engineering/
TSC-03-I-Prompt-Engineering/
TSC-03-A-Prompt-Engineering/
```

## Tools (living)

Product deep-dives live under `Tools/`, organised by company then tool:

```
Tools/<Company>/<Tool>.md
```

Examples:

- `Tools/OpenAI/ChatGPT.md`
- `Tools/OpenAI/Codex.md`
- `Tools/Anthropic/Claude.md`
- `Tools/Microsoft/Copilot.md`

These are **living** docs — versions, features and pricing rot within weeks to a quarter,
so each file is refreshed, never treated as durable knowledge.

## Entry IDs

Every TSC entry carries a stable ID in its YAML frontmatter and in the index:

```
NN.MM.L.code
```

- `NN` — TSC number (01–09).
- `MM` — proficiency ordinal: `01` Basic, `02` Intermediate, `03` Advanced.
- `L` — proficiency letter: `B` / `I` / `A`.
- `code` — the IMDA knowledge/ability code (`K1`…`Kn`, `A1`…`Am`).

Examples:

- `02.01.B.K7` — TSC 2, Basic, knowledge item K7.
- `01.01.B.A4` — TSC 1, Basic, ability item A4.

**Why:** a contributor can point at one exact skill and say "`06.01.B.01` looks stale"
without naming a file or re-reading the framework.

## YAML frontmatter

Every entry starts with:

```yaml
---
id: 02.01.B.K7
tsc: 2
level: Basic
code: K7
title: Concept of prompt design
---
```

- `id` — the stable ID (above).
- `tsc` — TSC number.
- `level` — `Basic` / `Intermediate` / `Advanced` (the word, not just the letter).
- `code` — the IMDA K/A code.
- `title` — the entry title (matches the H1).
