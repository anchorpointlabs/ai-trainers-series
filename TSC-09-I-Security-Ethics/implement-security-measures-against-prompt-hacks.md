---
id: 09.02.I.A2
tsc: 9
level: Intermediate
code: A2
title: Implement security measures against prompt hacks
---

# Implement security measures against prompt hacks

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A2**

**IMDA requirement:** Implement security measures to protect AI models (e.g., from large language model prompt hacks).

**What it means:** Prompt hacks — injection, jailbreaks — are countered with layered measures: input filtering, constrained outputs, least privilege, and human gates. The skill is implementing the measures that actually stop the attack, not just warning the model.

**The learner must be able to:**
- Choose layered measures for a threat.
- Explain why warnings alone do not stop attacks.
- Implement constrained outputs and least privilege.

**Lesson Plan Ideas:**
1. Use the kopitiam-runner analogy (quarantined reader, constrained tokens).
2. Teach the layered measures.
3. Learners pick measures for a scenario.
4. Debrief.

**Exercise (with the exact prompt):**
```text
A bot reads customer emails and can refund orders. Which two measures best stop a prompt-injection refund attack?
```
Expected: constrained output (it can only return pre-set actions) + human approval for refunds.

**Common mistakes:**
- Relying on a system prompt saying 'ignore bad instructions'.
- Giving the model more power (refunds) than it needs.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)

