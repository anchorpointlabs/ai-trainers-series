---
id: 09.02.I.A6
tsc: 9
level: Intermediate
code: A6
title: Monitor AI systems through the lifecycle
---

# Monitor AI systems through the lifecycle

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A6**

**Bullet (verbatim):** Monitor AI systems for trust and safety throughout project life cycle.

**What it means:** Monitoring is continuous: watch outputs for drift and abuse, watch logs for attacks, and act on what you see. It runs from launch to retirement, not just the first week.

**The learner must be able to:**
- Name what to monitor.
- Spot a drift or abuse signal in a log.
- Describe the monitor-and-act loop.

**How to teach it in 20 minutes:**
1. Teach 'monitoring is continuous, not a launch task'. (4 min)
2. Show a log with a drift signal and an attack signal. (6 min)
3. Learners mark what they would act on. (6 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
Your bot's refusal rate jumps 3x in a week. What would you check?
```
Expected: a new attack pattern, a prompt/guardrail change, or a data shift.

**Common mistakes:**
- Monitoring only at launch.
- Ignoring drift because 'it worked before'.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 5)
