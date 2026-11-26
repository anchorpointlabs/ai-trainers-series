---
id: 03.02.I.A4
tsc: 3
level: Intermediate
code: A4
title: Apply prompt techniques for use cases
---

# Apply prompt techniques for use cases

> **TSC #3 Prompt Engineering · Intermediate · Ability A4**

**Bullet (verbatim):** Apply prompt techniques as necessary for use cases.

**What it means:** Pick the technique that fits the task: few-shot for format and style, chain-of-thought for multi-step reasoning, role for tone, extraction for fields. The skill is matching, not collecting techniques.

**The learner must be able to:**
- Match a technique to a use case.
- Apply the matched technique to a task.
- Explain why that technique fit.

**How to teach it in 20 minutes:**
1. Show a task solved with the wrong technique, then the right one. (5 min)
2. Teach the matching table (format→few-shot, reasoning→CoT, tone→role). (5 min)
3. Learners choose + apply a technique for a task. (6 min)
4. Debrief the choices. (4 min)

**Exercise (with the exact prompt):**
```text
Task: work out how many staff are needed for a shift. Which technique fits, and write the prompt.
```
Expected: chain-of-thought, with 'work step by step'.

**Common mistakes:**
- Using a technique without matching it to the task.
- Collecting techniques instead of applying them.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 3)
