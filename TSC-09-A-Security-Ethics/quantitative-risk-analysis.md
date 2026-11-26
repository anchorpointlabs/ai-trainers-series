---
id: 09.03.A.K6
tsc: 9
level: Advanced
code: K6
title: Quantitative risk analysis
---

# Quantitative risk analysis

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K6**

**IMDA requirement:** Quantitative risk analysis techniques (e.g., Monte Carlo simulation, decision tree analysis).

**What it means:** Quantitative analysis puts numbers on risk instead of 'low/medium/high'. A **Monte Carlo** simulation runs many scenarios to estimate a range of outcomes; a **decision tree** maps choices and their probabilities. Both make risk decisions defensible and comparable.

**The learner must be able to:**
- Explain Monte Carlo in one line.
- Draw a simple decision tree.
- Say when numbers beat a risk matrix.

**Lesson Plan Ideas:**
1. Contrast 'low/medium/high' with a number and a range. 
2. Walk a decision tree for 'launch with guardrails vs delay'. 
3. Learners sketch a tree for a scenario. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
Draw a decision tree: launch the AI now (60% chance of a breach costing $50k) vs delay two weeks to test (costs $5k, cuts breach chance to 20%).
```
Expected: learners compare expected costs and pick the cheaper path.

**Common mistakes:**
- Using 'low/medium/high' when a number is available.
- Ignoring probability entirely in a decision.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 5)
