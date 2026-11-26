---
id: 09.02.I.A5
tsc: 9
level: Intermediate
code: A5
title: Conduct pre-deployment system testing
---

# Conduct pre-deployment system testing

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A5**

**Bullet (verbatim):** Conduct comprehensive pre-deployment system testing.

**What it means:** Comprehensive testing is a plan: normal cases, edge cases, adversarial cases, and integration checks — run systematically and documented. It is how you find the failure before the attacker does.

**The learner must be able to:**
- Build a test plan across case types.
- Run and document a test.
- Explain what 'comprehensive' includes.

**How to teach it in 20 minutes:**
1. Teach the four case types (normal, edge, adversarial, integration). (5 min)
2. Show a test plan. (5 min)
3. Learners write one case per type for a scenario. (7 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
Write one test case for each type (normal, edge, adversarial, integration) for an AI that reads invoices.
```
Expected: a clean invoice, a malformed one, a hidden-instruction one, and a wrong-format one.

**Common mistakes:**
- Testing only normal cases.
- Skipping documentation so tests are not repeatable.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)
