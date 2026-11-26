---
id: 03.02.I.K6
tsc: 3
level: Intermediate
code: K6
title: Prompt design, model behaviour, and output diversity
---

# Prompt design, model behaviour, and output diversity

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K6**

**IMDA requirement:** Relationship between prompt design, model behaviour, and output diversity.

**What it means:** The prompt is a dial: tighten it (constraints, format) and the output gets precise; loosen it and it gets diverse. Model behaviour follows the prompt — a vague prompt produces vague behaviour. Diversity and precision trade off, and the prompt design decides where you sit on the dial.

**The learner must be able to:**
- Explain the design→behaviour→diversity link.
- Adjust a prompt to increase or decrease diversity.
- Write a precise version and a diverse version of the same task.

**Lesson Plan Ideas:**
1. Show the same task prompted tight (one exact answer) vs loose (ten varied answers). 
2. Teach the dial metaphor. 
3. Learners write both versions for one task. 
4. Compare where the dial landed. 

**Exercise (with the exact prompt):**
```text
Precise: List the 3 risks of this plan as a table. No other text.
Diverse: Give 10 very different slogans for a pickleball club.
```
Expected: the first is tight and uniform; the second varies widely.

**Common mistakes:**
- Blaming the model for behaviour the prompt's wording caused.
- Wanting both precision and diversity from one loose prompt.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 5)
