---
id: 09.03.A.A4
tsc: 9
level: Advanced
code: A4
title: Apply red teaming to mitigate risk
---

# Apply red teaming to mitigate risk

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A4**

**IMDA requirement:** Apply red teaming to identify and mitigate security risks in AI systems.

**What it means:** Red teaming is not just finding flaws — it is turning findings into mitigations: reproduce, fix, retest, and add the case to the permanent test set. The loop closes only when the weakness is closed.

**The learner must be able to:**
- Run a red-team attack and produce a fix.
- Close the loop: fix, retest, add to test set.
- Explain why findings must become mitigations.

**Lesson Plan Ideas:**
1. Walk the red-team loop (attack → fix → retest → add to tests).
2. Run one attack together and fix it.
3. Learners write the fix for a finding.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Red team found the model reveals its system prompt when asked in Malay. Write the fix and the new test case.
```
Expected: a guardrail/filter for multilingual prompt extraction, plus a regression test.

**Common mistakes:**
- Finding flaws and stopping there.
- Not adding the finding to the permanent test set.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)

