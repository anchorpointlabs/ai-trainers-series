---
id: 08.02.I.A2
tsc: 8
level: Intermediate
code: A2
title: Assess environmental impact
---

# Assess environmental impact

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A2**

**IMDA requirement:** Assess environmental impact (e.g., estimate energy footprint).

**What it means:** Assessing impact means estimating the energy cost of a model choice — roughly, bigger model = more compute = more energy — and factoring it into the decision alongside cost and quality.

**The learner must be able to:**
- Estimate relative energy cost of two models.
- Factor footprint into a model choice.
- Name a lower-footprint alternative.

**Lesson Plan Ideas:**
1. Show a rough energy comparison of model sizes. 
2. Teach 'estimate, then right-size'. 
3. Learners compare two options on footprint. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
Estimate: a frontier model vs a small model for 1M simple classifications. Which has the lighter footprint and by roughly how much?
```
Expected: the small model — often orders of magnitude cheaper in energy.

**Common mistakes:**
- Ignoring footprint because it is hard to measure exactly.
- Choosing the biggest model when the task is trivial.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 2)
