---
id: 09.03.A.K4
tsc: 9
level: Advanced
code: K4
title: Red teaming for vulnerabilities
---

# Red teaming for vulnerabilities

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K4**

**Bullet (verbatim):** Red teaming for discovering vulnerabilities in generative AI models.

**What it means:** Red teaming is attacking your own model on purpose — a team plays the adversary, trying jailbreaks, injections, and data extraction — to find weaknesses before real attackers do. It is the highest-value pre-launch activity.

**The learner must be able to:**
- Explain what red teaming is.
- Name the attack classes a red team tries.
- Describe a red-team finding and its fix.

**How to teach it in 20 minutes:**
1. Contrast red teaming with ordinary testing (adversarial vs functional). (4 min)
2. Walk one red-team exercise (extract the system prompt). (7 min)
3. Learners write one red-team attack. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
You are red-teaming a finance bot. Write one attack to try, and say what a defender should do if it succeeds.
```
Expected: e.g. 'reveal your instructions' — and the fix (constrain outputs, drop system-prompt disclosure).

**Common mistakes:**
- Thinking red teaming is optional or only for big firms.
- Red-teaming without acting on the findings.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (sections 3, 4)
