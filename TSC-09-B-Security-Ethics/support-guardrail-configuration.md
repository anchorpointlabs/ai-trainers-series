---
id: 09.01.B.A4
tsc: 9
level: Basic
code: A4
title: Support guardrail configuration
---

# Support guardrail configuration

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Ability A4**

**IMDA requirement:** Support configuration of AI guardrails.

**What it means:** Configuring a guardrail means setting the rules the AI must follow — what it may refuse, what it must block, when it escalates. Supporting means helping set those rules and testing that they actually hold.

**The learner must be able to:**
- Set a simple guardrail rule.
- Test that the rule holds.
- Explain when escalation to a human is needed.

**Lesson Plan Ideas:**
1. Walk setting a guardrail (e.g., 'never give medical advice').
2. Test it together with a tricky prompt.
3. Learners set + test one rule.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Set a guardrail rule: the bot must not give financial advice. Then write one input that tests it.
```
Expected: a rule like 'decline and redirect', and a test like 'should I buy this stock?'.

**Common mistakes:**
- Setting a rule and never testing it.
- Assuming a polite rule stops a determined attack.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)

