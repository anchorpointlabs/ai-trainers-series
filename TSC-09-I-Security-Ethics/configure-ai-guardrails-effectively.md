---
id: 09.02.I.A3
tsc: 9
level: Intermediate
code: A3
title: Configure AI guardrails effectively
---

# Configure AI guardrails effectively

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A3**

**Bullet (verbatim):** Configure AI guardrails effectively.

**What it means:** Configuring effectively means the guardrail actually changes behaviour — the model refuses the harmful ask, blocks the bad output, or escalates. It is tested, tuned, and re-tested, not just switched on.

**The learner must be able to:**
- Configure a guardrail and verify it holds.
- Tune a guardrail that is too strict or too loose.
- Explain the trade-off between safety and usefulness.

**How to teach it in 20 minutes:**
1. Show a guardrail too loose (lets harm through) and too strict (refuses everything). (5 min)
2. Teach the tuning loop. (5 min)
3. Learners tune a guardrail on sample inputs. (6 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
A guardrail blocks all requests containing 'password'. It now blocks 'how do I reset my password?'. Tune it.
```
Expected: refine the rule to block only suspicious uses, not legitimate support questions.

**Common mistakes:**
- Over-blocking and frustrating users.
- Under-blocking and letting harm through.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)
