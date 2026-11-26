---
id: 09.01.B.A3
tsc: 9
level: Basic
code: A3
title: Assist in pre-deployment testing
---

# Assist in pre-deployment testing

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Ability A3**

**Bullet (verbatim):** Assist in pre-deployment system testing.

**What it means:** Pre-deployment testing is a team effort, and assisting means contributing test cases — adversarial inputs, edge cases, and realistic data — and recording results. It is not passive watching.

**The learner must be able to:**
- Contribute a test case.
- Record a test result.
- Explain what an adversarial input is.

**How to teach it in 20 minutes:**
1. Define adversarial input (an input designed to break it). (4 min)
2. Show a test log and its fields. (5 min)
3. Learners write three test cases for a booking bot. (7 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
Write three test cases for a hotel-booking bot: one normal, one edge case, one adversarial.
```
Expected: a normal booking, a weird date/name, and a jailbreak attempt.

**Common mistakes:**
- Only testing normal inputs.
- Not recording results, so nothing is repeatable.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)
