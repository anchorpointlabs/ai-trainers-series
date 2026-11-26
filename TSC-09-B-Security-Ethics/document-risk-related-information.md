---
id: 09.01.B.A2
tsc: 9
level: Basic
code: A2
title: Document risk-related information
---

# Document risk-related information

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Ability A2**

**Bullet (verbatim):** Document risk-related information.

**What it means:** A risk is only manageable if it is written down: what the risk is, how likely, what it could do, and what the mitigation is. Documentation is the difference between 'we discussed it' and 'we can prove we handled it'.

**The learner must be able to:**
- Write a one-line risk note.
- Name the four parts (risk, likelihood, impact, mitigation).
- Explain why documenting matters.

**How to teach it in 20 minutes:**
1. Teach the four-part risk note with one example. (5 min)
2. Contrast 'we talked about it' with a written risk log. (5 min)
3. Learners write a risk note for a hallucinating chatbot. (6 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
Write a four-part risk note for a support bot that sometimes invents refund promises.
```
Expected: risk (hallucinated promises), likelihood, impact (financial/reputational), mitigation (guardrail + human approval).

**Common mistakes:**
- Keeping risks in your head.
- Writing risks without a mitigation.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 5)
