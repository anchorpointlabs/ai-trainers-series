---
id: 08.02.I.A4
tsc: 8
level: Intermediate
code: A4
title: Evaluate privacy vs performance trade-offs
---

# Evaluate privacy vs performance trade-offs

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A4**

**IMDA requirement:** Evaluate the trade-offs between privacy and model performance.

**What it means:** Privacy and performance often pull against each other: anonymising or federating data can cost accuracy. The skill is measuring both and making a deliberate choice, not defaulting to one side.

**The learner must be able to:**
- Name a privacy measure that costs performance.
- Weigh the two on a decision.
- Justify a trade-off choice.

**Lesson Plan Ideas:**
1. Show anonymisation slightly reducing accuracy.
2. Teach 'name the trade-off, then choose'.
3. Learners weigh a trade-off for a scenario.
4. Debrief.

**Exercise (with the exact prompt):**
```text
You can train on full data (high accuracy, privacy risk) or anonymised data (slightly lower accuracy, safer). For a health model, which do you pick?
```
Expected: anonymised — the small accuracy loss is worth the privacy gain in a health context.

**Common mistakes:**
- Always choosing performance over privacy.
- Always choosing privacy without measuring the cost.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 2)

