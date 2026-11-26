---
id: 09.03.A.A2
tsc: 9
level: Advanced
code: A2
title: Refine and enhance AI guardrails
---

# Refine and enhance AI guardrails

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A2**

**Bullet (verbatim):** Propose refinements and enhancements to AI guardrails.

**What it means:** Refining guardrails is improving them from measured failure — tightening where harm slips through, loosening where good use is blocked, and adding new rules for new attack patterns. It is continuous tuning, not a finished product.

**The learner must be able to:**
- Propose a refinement from failure data.
- Balance false positives against false negatives.
- Add a rule for a new attack.

**How to teach it in 20 minutes:**
1. Show a guardrail's failure data and propose a tune. (6 min)
2. Teach the safety-usefulness balance. (5 min)
3. Learners propose a refinement. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
A new attack convinces the model to reveal hidden data via a 'roleplay'. Propose a guardrail enhancement.
```
Expected: add a rule or filter that detects roleplay-style instruction subversion.

**Common mistakes:**
- Treating guardrails as finished.
- Refining with no data on where they fail.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)
