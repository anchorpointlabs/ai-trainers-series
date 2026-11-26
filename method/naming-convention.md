# Naming convention

How folders and entries are named, so anyone can find a thing and cite it unambiguously.

## Folder names

```
[NN] TSC-NN-{B|I|A}-{Topic}/
```

- `NN` — the TSC number (01–09), zero-padded.
- `{B|I|A}` — proficiency: `B` = Basic, `I` = Intermediate, `A` = Advanced.
- `{Topic}` — a short kebab-case topic.

Examples:

- `[01] TSC-01-B-GenAI-Principles/`
- `[02] TSC-02-B-Prompt-Design/`

## Multi-level TSCs

When a TSC spans more than one proficiency level, group them under the TSC number:

```
[03] New GenAI TSC #3 - Prompt Engineering      (the group — not a folder)
[03.01] TSC-03-B-Crafting/                      (Basic)
[03.02] TSC-03-I-Engineering/                   (Intermediate)
[03.03] TSC-03-A-Optimising/                    (Advanced)
```

## Entry IDs

Every entry carries a stable ID in its YAML frontmatter and in the index:

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
