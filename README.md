# APL: AI Trainer's Series

**[Browse the full index →](INDEX.md)**

A reference library for AI trainers — one entry per skill from the IMDA / SkillsFuture
*Skills Framework for ICT: Skills in Generative AI* (the nine GenAI TSCs).

Written for trainers, not for learners and not for assessment. Each entry gives the
framework bullet in plain words, a way to teach it in a class, a tested exercise with the
exact prompt, common mistakes, and dated sources — so a trainer can walk in and teach the
thing, not just read the slide.

## What's inside

| Folder | What it holds |
|---|---|
| `[01] TSC-01-B-GenAI-Principles/` | Generative AI Principles and Applications (Basic) — partial |
| `[02] TSC-02-B-Prompt-Design/` | Prompt Design (Basic) — the complete K1–K7 / A1–A8 set |
| `concepts/` | Cross-cutting mechanisms, organised by **decay tier** |
| `method/` | The methodology: the decay model, the entry template, the naming convention |

## Naming convention

- **Folder:** `[NN] TSC-NN-{B|I|A}-{Topic}/` — `NN` = TSC number; `B` / `I` / `A` = Basic / Intermediate / Advanced.
- **Multi-level TSC:** a `[NN]` group with `[NN.01]` (Basic), `[NN.02]` (Intermediate), `[NN.03]` (Advanced) sub-folders.
- **Entry ID (YAML frontmatter + index):** `NN.MM.L.code` — e.g. `02.01.B.K7` = TSC 2, level 01 (Basic), knowledge item K7. Cite the ID when you flag something stale. Full rules in [`method/naming-convention.md`](method/naming-convention.md).

## The decay model

Every entry declares how fast it rots, and the format changes with it:

- **Durable** (`concepts/durable/`) — the mechanism. Years to decades. No product names.
- **Technique** (`concepts/technique/`) — a craft with knobs. Method durable, fields living.
- **Living** (`concepts/living/`) — models, prices, deprecations. Weeks to a quarter.
- **Event** (`concepts/event/`) — a dated incident, written once, taught as a case study.

The test for which tier you're writing: **what would make it wrong?** A new model release →
Living. Nothing → Durable. It happened on a date → Event. A vendor renaming a field →
Technique.

The rule behind it: *a library of 40 entries refreshed monthly beats 200 entries refreshed
never.* Read the full model in [`method/decay-model.md`](method/decay-model.md).

## Who this is for

Singapore's AI courses are built on a national framework of nine GenAI skills. Adult
educators are being asked to teach against it — often without having read the framework
themselves. This library is the reference for them.

## Source framework

IMDA / SkillsFuture — *Skills Framework for Infocomm Technology (ICT): Skills in Generative
Artificial Intelligence (AI)* (March 2025, nine GenAI TSCs).

Individual bullets are quoted verbatim with attribution, under non-commercial, informational
use. The full bullet list is not reproduced here — link to the source document instead.

## Status

- **TSC #2 Prompt Design (Basic)** — complete: 15 entries (K1–K7, A1–A8).
- **TSC #1 Generative AI Principles and Applications (Basic)** — 4 entries so far.
- **Concepts** — 13 cross-cutting mechanisms (10 durable, 1 technique, 1 living, 1 event).

Prompt Engineering (TSC #3), the AI Practitioners TSCs (#4–#7) and Ethics & Governance
(#8–#9) are in progress.

## Contact

Anchor Point Labs — [anchorpointlabs.github.io](https://anchorpointlabs.github.io)
