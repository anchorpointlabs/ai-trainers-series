---
id: 08.03.A.A4
tsc: 8
level: Advanced
code: A4
title: Develop privacy-preserving algorithms
---

# Develop privacy-preserving algorithms

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A4**

**Bullet (verbatim):** Develop new privacy-preserving algorithms.

**What it means:** Privacy-preserving techniques — differential privacy, federated learning, secure computation — let you use data without exposing individuals. Developing them is specialist work, but the skill includes knowing which technique fits which problem.

**The learner must be able to:**
- Name the main techniques.
- Match a technique to a problem.
- Explain what differential privacy does in one line.

**How to teach it in 20 minutes:**
1. Map the techniques to the problems they solve. (6 min)
2. Teach differential privacy with the 'add a little noise' picture. (5 min)
3. Learners match techniques to scenarios. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
Match: (a) train on data without collecting it centrally, (b) release statistics without identifying anyone. Which technique for each?
```
Expected: (a) federated learning, (b) differential privacy.

**Common mistakes:**
- Reaching for a heavy technique when simple anonymisation would do.
- Confusing the techniques with each other.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 2)
