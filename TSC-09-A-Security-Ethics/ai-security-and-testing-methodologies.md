---
id: 09.03.A.K1
tsc: 9
level: Advanced
code: K1
title: AI security and testing methodologies
---

# AI security and testing methodologies

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K1**

**Bullet (verbatim):** Methodologies of AI model security and testing.

**What it means:** A methodology is a repeatable, defensible way to secure and test models — not ad-hoc poking. It defines the threat model, the test catalogue, and the acceptance bar, so security is consistent across models and teams.

**The learner must be able to:**
- Define a threat model in one line.
- Explain what a test catalogue is.
- State an acceptance bar for a model.

**How to teach it in 20 minutes:**
1. Contrast ad-hoc poking with a methodology. (4 min)
2. Walk a threat model for a sample system. (7 min)
3. Learners sketch a threat model. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
Sketch a threat model for a chatbot with access to a customer database: who might attack, via what, to get what?
```
Expected: attacker (user/insider), via prompt injection or the DB tool, to get PII.

**Common mistakes:**
- Securing without a threat model.
- Testing with no defined pass bar.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (sections 2, 4)
