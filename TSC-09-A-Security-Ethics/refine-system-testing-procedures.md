---
id: 09.03.A.A1
tsc: 9
level: Advanced
code: A1
title: Refine system testing procedures
---

# Refine system testing procedures

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A1**

**Bullet (verbatim):** Refine comprehensive system testing procedures.

**What it means:** Refining testing means improving the procedure itself — from the failures you find, you add new cases, close gaps, and raise the bar. A test procedure that never changes is a procedure that stops catching new attacks.

**The learner must be able to:**
- Update a test procedure from a finding.
- Explain why procedures must evolve.
- Add a new test case class.

**How to teach it in 20 minutes:**
1. Show a procedure that missed an attack, and how to amend it. (5 min)
2. Teach 'every missed attack becomes a new test case'. (5 min)
3. Learners amend a procedure from a finding. (7 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
Your tests missed a jailbreak that used a long story. Amend the test procedure.
```
Expected: add 'long-context narrative jailbreaks' as a new case class.

**Common mistakes:**
- Running the same test set forever.
- Not converting incidents into test cases.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)
