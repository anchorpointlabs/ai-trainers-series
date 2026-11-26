---
id: 03.03.A.K3
tsc: 3
level: Advanced
code: K3
title: Prompt optimisation and sequencing of instructions
---

# Prompt optimisation and sequencing of instructions

> **TSC #3 Prompt Engineering · Advanced · Knowledge K3**

**IMDA requirement:** Nuances of prompt optimisation and its role in generating tailored outputs (e.g., sequencing of instructions in prompts).

**What it means:** The *order* of instructions changes the result, because the model reads the prompt like a brief and weights later text against what came before. Optimisation is the deliberate loop: try, score against a fixed check, change one thing, try again — never change everything at once.

**The learner must be able to:**
- Explain why instruction order matters and give an example.
- Run a two-version comparison changing only the order of constraints.
- Describe a one-variable-at-a-time optimisation loop.

**Lesson Plan Ideas:**
1. Show the same three constraints in two orders producing different outputs.
2. Introduce 'change one thing at a time' as the optimisation rule.
3. Pairs take a weak prompt, change one variable, and log the difference.
4. Debrief which single change helped most.

**Exercise (with the exact prompt):**
```text
Version A: Summarise this report in 3 bullets, keep it under 50 words, write for a busy director.
Version B: Write for a busy director. Summarise this report in 3 bullets, keep it under 50 words.

<report>
```
Expected: the two outputs differ in emphasis, showing order matters.

**Common mistakes:**
- Optimising by rewriting the whole prompt each time, so you cannot tell what helped.
- Believing the model 'learns' from your corrections inside one chat — each turn is a fresh read.
- Ignoring the check: optimising with no fixed success criterion is just fiddling.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (sections 5, 9)

