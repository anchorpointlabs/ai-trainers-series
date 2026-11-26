---
id: 08.02.I.A3
tsc: 8
level: Intermediate
code: A3
title: Mitigate bias and ethical risks
---

# Mitigate bias and ethical risks

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A3**

**IMDA requirement:** Implement strategies to mitigate bias and ethical risks in AI systems.

**What it means:** Mitigation is concrete: fix the training data, add fairness checks, constrain the output, or add a human gate. The skill is picking the mitigation that actually addresses the risk, not a symbolic gesture.

**The learner must be able to:**
- Pick a mitigation for a named bias.
- Explain why the mitigation addresses the cause.
- Add a fairness check to a pipeline.

**Lesson Plan Ideas:**
1. Show a biased output and trace it to a cause, then fix it.
2. Teach the mitigation menu (data, checks, constraints, human gate).
3. Learners pick a mitigation for a risk.
4. Debrief.

**Exercise (with the exact prompt):**
```text
A model gives shorter, colder replies to certain names. Name the cause and one mitigation.
```
Expected: cause = biased training data; mitigation = rebalance data + a fairness test.

**Common mistakes:**
- Adding a mitigation that does not touch the cause.
- Treating 'we added a check' as proof the bias is gone.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 2)

