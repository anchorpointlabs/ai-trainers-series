---
id: 09.02.I.K2
tsc: 9
level: Intermediate
code: K2
title: Configuring guardrails for content generation
---

# Configuring guardrails for content generation

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Knowledge K2**

**IMDA requirement:** Configuration and implementation of AI guardrails for content generation.

**What it means:** Content-generation guardrails bound what the model produces — blocking harmful, off-topic, or out-of-policy output. Configuring them means defining the policy, encoding it as rules, and testing against realistic and adversarial generation attempts.

**The learner must be able to:**
- Define a content policy.
- Encode it as guardrail rules.
- Test the guardrail against attempts to slip through.

**Lesson Plan Ideas:**
1. Write a content policy together (what the bot must never produce).
2. Encode it as rules.
3. Learners try to make the model violate the policy.
4. Debrief which attempts slipped through.

**Exercise (with the exact prompt):**
```text
Policy: the bot never gives medical advice. Write three attempts to get it to break the policy.
```
Expected: e.g. roleplay as a doctor, ask 'hypothetically', or hide the ask in a story.

**Common mistakes:**
- Writing a vague policy that cannot be encoded.
- Testing only polite requests, not adversarial ones.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)

