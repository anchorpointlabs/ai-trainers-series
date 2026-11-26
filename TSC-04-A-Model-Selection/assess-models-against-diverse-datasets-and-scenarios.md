---
id: 04.03.A.A2
tsc: 4
level: Advanced
code: A2
title: Assess models against diverse datasets and scenarios
---

# Assess models against diverse datasets and scenarios

> **TSC #4 Generative AI Model Selection · Advanced · Ability A2**

**IMDA requirement:** Assess the effectiveness of models against diverse datasets and scenarios.

**What it means:** A model that scores well on one dataset may fail on a different distribution — other languages, domains, or edge cases. Effectiveness is assessed by testing across *diverse* scenarios and watching where it breaks, not by a single benchmark.

**The learner must be able to:**
- Run a model on two different datasets and compare.
- Spot where the model's strength is dataset-specific.
- State why diverse testing matters.

**Lesson Plan Ideas:**
1. Show a model that aces English and stumbles on Singlish. 
2. Teach 'a benchmark is one dataset, not the truth'. 
3. Learners list diverse scenarios to test a model for Singapore use. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
List three diverse scenarios to test a customer-service model for Singapore (hint: language and culture).
```
Expected: Singlish, code-switching, and local policy references.

**Common mistakes:**
- Trusting one benchmark as proof a model works.
- Testing only the happy path in one language.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 8)
