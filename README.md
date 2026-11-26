# APL: AI Trainer's Series

A reference library for AI trainers — one entry per skill from the IMDA / SkillsFuture
*Skills Framework for ICT: Skills in Generative AI* (the nine GenAI TSCs), plus living
product deep-dives.

Written for trainers, not for learners and not for assessment. Each entry gives the
framework bullet in plain words, a way to teach it in a class, a tested exercise with the
exact prompt, common mistakes, and dated sources — so a trainer can walk in and teach the
thing, not just read the slide.

## What's inside

| Folder | What it holds |
|---|---|
| [TSC #1 · GenAI Principles](TSC-01-B-GenAI-Principles/) | B (13) · I (10) — complete |
| [TSC #2 · Prompt Design](TSC-02-B-Prompt-Design/) | B (15) — complete |
| [TSC #3 · Prompt Engineering](TSC-03-B-Prompt-Engineering/README.md) | B (15) · I (13) · A (13) — complete |
| [TSC #4 · Model Selection](TSC-04-I-Model-Selection/README.md) | I (11) · A (8) — complete |
| [TSC #5 · Model Evaluation](TSC-05-B-Model-Evaluation/README.md) | B (11) · I (12) · A (13) — complete |
| [TSC #6 · Application Development](TSC-06-B-Application-Development/README.md) | B (11) · I (12) · A (12) — complete |
| [TSC #7 · Model Development](TSC-07-B-Model-Development/README.md) | B (15) · I (17) · A (20) — complete |
| [TSC #8 · Responsible AI](TSC-08-B-Responsible-AI/README.md) | B (10) · I (14) · A (14) — complete |
| [TSC #9 · Security & Ethics](TSC-09-B-Security-Ethics/README.md) | B (8) · I (10) · A (12) — complete |
| [Tools](Tools/) | [ChatGPT](Tools/OpenAI/ChatGPT.md) · [Claude](Tools/Anthropic/Claude.md) · [Gemini](Tools/Google/Gemini.md) · [Copilot](Tools/Microsoft/Copilot.md) · [Grok](Tools/xAI/Grok.md) · [more…](Tools/) — 11 living deep-dives |
| [concepts](concepts/) | Cross-cutting mechanisms, by decay tier |
| [Living Register](concepts/living/register.csv) | Current models, versions, prices — checked monthly, every row sourced to the vendor |
| [method](method/) | Decay model · entry template · naming convention |

## Naming convention

- **TSC folder:** `TSC-NN-{B|I|A}-{Topic}/` — `NN` = TSC number; `B` / `I` / `A` = Basic / Intermediate / Advanced. The TSC number and level also live in each entry's YAML.
- **Multi-level TSC:** one folder per level — `TSC-03-B-Prompt-Engineering/`, `TSC-03-I-Prompt-Engineering/`, `TSC-03-A-Prompt-Engineering/`.
- **Tool (living):** `Tools/<Company>/<Tool>.md` — e.g. `Tools/OpenAI/ChatGPT.md`, `Tools/Anthropic/Claude.md`.
- **Entry ID (YAML + index):** `NN.MM.L.code` — e.g. `02.01.B.K7` = TSC 2, Basic, knowledge item K7. Cite it to flag stale content. Full rules in [`method/naming-convention.md`](method/naming-convention.md).

## How to read an entry

Every entry maps to one Knowledge/Ability item from the IMDA Skills Framework, quoted word-for-word — so the library stays mappable for WSQ/SSG accreditation and assessment.

**Lesson Plan Ideas** follow Gagné's nine events of instruction: gain attention, state the objective, recall prior learning, present the content, guide, elicit performance, give feedback, and transfer. Timings are the trainer's call.

## The decay model

Every entry declares how fast it rots, and the format changes with it:

- **Durable** (`concepts/durable/`) — the mechanism. Years to decades. No product names.
- **Technique** (`concepts/technique/`) — a craft with knobs. Method durable, fields living.
- **Living** (`concepts/living/`, `Tools/`) — models, prices, deprecations. Weeks to a quarter.
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

- **All nine TSCs complete** — 289 entries across 23 level-folders (Basic / Intermediate / Advanced). No level is still "planned."
- **Tools (living)** — 11 product deep-dives under `Tools/` (versions, features, pricing; refreshed per quarter).
- **Concepts** — 13 cross-cutting mechanisms (10 durable, 1 technique, 1 living, 1 event).

## Contact

Anchor Point Labs — [anchorpointlabs.github.io](https://anchorpointlabs.github.io)
