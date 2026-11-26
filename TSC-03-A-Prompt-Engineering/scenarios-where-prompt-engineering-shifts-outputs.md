---
id: 03.03.A.K1
tsc: 3
level: Advanced
code: K1
title: Scenarios where prompt engineering shifts outputs
---

# Scenarios where prompt engineering shifts outputs

> **TSC #3 Prompt Engineering · Advanced · Knowledge K1**

**IMDA requirement:** Scenarios where prompt engineering significantly influences outputs.

**What it means:** Prompt engineering matters most when the task is ambiguous, high-stakes, or needs a specific shape — not when the answer is a lookup. The payoff comes from *structure* (role, steps, format, constraints), not from finding a magic phrase. A model left unguided will answer the *average* question; a well-engineered prompt makes it answer *your* question.

**The learner must be able to:**
- Name three scenarios where careful prompting changes the result vs. where it does not.
- Explain why the same question, prompted differently, produces a different-shaped answer.

**Lesson Plan Ideas:**
1. Ask: when would a vague one-line prompt be fine, and when would it fail? Collect two answers. 
2. Show a weak prompt vs a structured prompt on the same task; point out the difference is structure, not vocabulary. 
3. Pairs pick one workplace task and write both a weak and a structured version. 
4. Debrief: which differences came from structure? 

**Exercise (with the exact prompt):**
```text
Weak: Help me with the staff roster.
Strong: You are the admin for a 12-person clinic. Build next week's roster. Each staff works 5 days, max 2 weekends a month, and Nurse A cannot work Friday. Output a table with day, shift, and staff name. If any constraint is impossible, say which one and why.
```
Expected: the weak prompt returns generic advice; the strong one returns a usable table or a named conflict.

**Common mistakes:**
- Assuming a longer prompt is automatically better — it is structure, not length, that helps.
- Chasing 'magic phrases' instead of specifying the task and constraints.
- Using prompt engineering when a direct lookup or a spreadsheet would be faster.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (sections 1, 5)
