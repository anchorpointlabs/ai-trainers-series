---
id: 04.02.I.K3
tsc: 4
level: Intermediate
code: K3
title: Model parameters — modality, size, cost, features
---

# Model parameters — modality, size, cost, features

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K3**

**IMDA requirement:** Model parameters for different use cases (e.g., modality, size, cost, features).

**What it means:** Choosing a model means weighing four knobs: **modality** (text/image/video/audio), **size** (parameter count — bigger is smarter but costlier and slower), **cost** (per-token pricing), and **features** (context length, tool use, fine-tuning support). The use case decides the acceptable point on each knob.

**The learner must be able to:**
- Name the four knobs.
- Explain the size/cost/latency trade-off.
- Pick a sensible model for a budgeted task.

**Lesson Plan Ideas:**
1. Present the four knobs with one example each.
2. Teach the trade-off: bigger is smarter but costlier.
3. Learners choose a model for a task with a cost cap.
4. Debrief the choices.

**Exercise (with the exact prompt):**
```text
Task: draft 500 marketing emails a day, $0.01 per email budget. Which knob dominates, and why?
```
Expected: cost dominates — a small, cheap model beats a frontier model on unit economics.

**Common mistakes:**
- Choosing the biggest model for everything.
- Ignoring cost until the invoice arrives.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 3)

