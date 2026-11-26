---
id: 09.02.I.A1
tsc: 9
level: Intermediate
code: A1
title: Develop mitigation strategies
---

# Develop mitigation strategies

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A1**

**IMDA requirement:** Develop mitigation strategies for identified risks.

**What it means:** A mitigation is a concrete action that reduces a risk — a guardrail, a human gate, a data change. The skill is pairing each identified risk with a specific mitigation, not a vague 'we'll be careful'.

**The learner must be able to:**
- Pair a risk with a concrete mitigation.
- Explain why 'be careful' is not a mitigation.
- Rank mitigations by cost vs effect.

**Lesson Plan Ideas:**
1. Contrast 'we'll be careful' with a real mitigation. 
2. Teach the mitigation menu (prevent, detect, respond). 
3. Learners write a mitigation for a named risk. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
Risk: the bot leaks customer names. Write two concrete mitigations.
```
Expected: e.g. output filter for names + never sending customer data to the model.

**Common mistakes:**
- Writing 'be careful' instead of a concrete control.
- Picking a mitigation that does not actually reduce the risk.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)
