---
id: 09.02.I.A4
tsc: 9
level: Intermediate
code: A4
title: Conduct comprehensive risk assessments
---

# Conduct comprehensive risk assessments

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A4**

**Bullet (verbatim):** Conduct comprehensive risk assessments.

**What it means:** A comprehensive assessment covers the whole system — the model, its data, its tools, its users — and produces a ranked risk register with owners. It is comprehensive because it leaves no surface unexamined.

**The learner must be able to:**
- Enumerate the system's surfaces.
- Produce a ranked risk register.
- Assign an owner to each risk.

**How to teach it in 20 minutes:**
1. Map the surfaces of a sample AI system. (6 min)
2. Teach the risk register format. (5 min)
3. Learners produce a short register. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
List the surfaces of a booking bot (model, data, tools, users), and name one risk per surface.
```
Expected: model (hallucination), data (PII leak), tools (bad API call), users (abuse).

**Common mistakes:**
- Assessing only the model and ignoring data and tools.
- Producing risks with no owner.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 5)
