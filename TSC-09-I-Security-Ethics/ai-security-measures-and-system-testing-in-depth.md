---
id: 09.02.I.K1
tsc: 9
level: Intermediate
code: K1
title: AI security measures and system testing in depth
---

# AI security measures and system testing in depth

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Knowledge K1**

**Bullet (verbatim):** In-depth understanding of AI security measures and system testing.

**What it means:** Security measures are the full set of controls — input/output filtering, least privilege, logging, rate limiting — and system testing verifies them systematically. Depth means knowing how each control fails and testing for exactly that failure.

**The learner must be able to:**
- Name the full control set.
- Explain how one control fails.
- Design a test for a specific control.

**How to teach it in 20 minutes:**
1. Map the control set (filter, privilege, log, rate-limit). (6 min)
2. Teach 'every control has a failure mode — test for it'. (5 min)
3. Learners design a test for one control. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
Design a test to check whether an output filter actually blocks credit-card numbers.
```
Expected: inputs containing card-like numbers, checking the output is redacted/blocked.

**Common mistakes:**
- Assuming a control works because it was configured.
- Testing controls in isolation, not together.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (sections 4, 5)
