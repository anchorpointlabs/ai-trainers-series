---
id: 03.02.I.A5
tsc: 3
level: Intermediate
code: A5
title: Match prompt techniques to foundation models
---

# Match prompt techniques to foundation models

> **TSC #3 Prompt Engineering · Intermediate · Ability A5**

**Bullet (verbatim):** Identify which prompt techniques are best-suited for specific foundation models.

**What it means:** Different models need different handling: some reason well without being asked, others need an explicit 'think step by step'; some follow format rules strictly, others drift. The skill is testing a technique against *your* model and adapting, not assuming one prompt works everywhere.

**The learner must be able to:**
- Note how two models respond differently to the same prompt.
- Adapt a prompt to a model's behaviour.
- Explain why you test rather than assume.

**How to teach it in 20 minutes:**
1. Run one prompt on two models (if available) and show the difference. (6 min)
2. Teach 'different models, different needs — test'. (3 min)
3. Learners write one prompt with a note on how they would adapt it. (7 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
Write a chain-of-thought prompt. Then note: for a model that already reasons well, what would you drop?
```
Expected: learners note they would drop the explicit 'step by step' for a strong reasoning model.

**Common mistakes:**
- Assuming one prompt transfers unchanged across models.
- Not testing before scaling a prompt.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [popular-llms-and-notebooklm.md](../core-knowledge/popular-llms-and-notebooklm.md) (section 4)
