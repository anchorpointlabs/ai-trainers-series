---
id: 04.02.I.K4
tsc: 4
level: Intermediate
code: K4
title: Handling and interacting with generative AI tools
---

# Handling and interacting with generative AI tools

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K4**

**IMDA requirement:** Steps in handling and interacting with generative AI tools.

**What it means:** Using a GenAI tool well is a repeatable sequence: state the task, supply context, set the format, run, check against the goal, and iterate. The 'handling' part is the discipline around the tool — versions, settings, and reading errors — not the tool's brand.

**The learner must be able to:**
- Describe the interact-and-check loop.
- Adjust a tool setting (temperature, length) for a task.
- Read an error and state the likely cause.

**Lesson Plan Ideas:**
1. Walk the loop on a live example.
2. Teach two settings (temperature, max length) and their effect.
3. Learners run a task and log their settings.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Run: "Summarise this in 3 bullets" with temperature 0.3, then again at 0.9. Compare the variation.
```
Expected: low temperature is steadier; high temperature varies more.

**Common mistakes:**
- Ignoring settings and wondering why output varies.
- Treating an error as the model 'breaking' instead of reading it.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 2.5)

