---
id: 09.03.A.K3
tsc: 9
level: Advanced
code: K3
title: Strategic refinement of AI guardrails
---

# Strategic refinement of AI guardrails

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K3**

**IMDA requirement:** Strategic development and refinement of AI guardrails.

**What it means:** Refining guardrails strategically means measuring where they fail (false positives vs false negatives), and tuning them toward the organisation's actual risk appetite — not just patching one case at a time. It is guardrail management as a discipline.

**The learner must be able to:**
- Measure a guardrail's false positives and negatives.
- Explain risk appetite.
- Propose a refinement from failure data.

**Lesson Plan Ideas:**
1. Teach false positive vs false negative with examples.
2. Explain tuning to risk appetite.
3. Learners propose a refinement from failure data.
4. Debrief.

**Exercise (with the exact prompt):**
```text
A guardrail misses 2% of harmful output (false negative) but blocks 15% of good output (false positive). Which way would you tune it, and why?
```
Expected: depends on risk appetite — tighten for safety-critical, loosen for creative.

**Common mistakes:**
- Patching one case without measuring the pattern.
- Tuning with no stated risk appetite.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)

