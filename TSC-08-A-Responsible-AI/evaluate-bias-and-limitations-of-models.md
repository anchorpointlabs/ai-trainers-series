---
id: 08.03.A.A2
tsc: 8
level: Advanced
code: A2
title: Evaluate bias and limitations of models
---

# Evaluate bias and limitations of models

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A2**

**Bullet (verbatim):** Evaluate biases, limitations and ethical implications of models, including using an evaluation dataset from various sources.

**What it means:** Evaluation for ethics means testing the model on data from many sources — not one convenient dataset — to expose bias and limitations. A model looks fine on one dataset and fails on another; the skill is testing across sources.

**The learner must be able to:**
- Build an evaluation set from multiple sources.
- Expose a bias that one dataset hides.
- Explain why source diversity matters.

**How to teach it in 20 minutes:**
1. Show a model that passes one dataset and fails another. (6 min)
2. Teach 'one dataset is a flattering mirror'. (5 min)
3. Learners design a multi-source test. (6 min)
4. Debrief. (3 min)

**Exercise (with the exact prompt):**
```text
Design a multi-source evaluation for a translation model to expose dialect bias.
```
Expected: test on standard English, Singlish, and minority languages from different sources.

**Common mistakes:**
- Evaluating on one convenient dataset.
- Assuming a good score on one source means no bias.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 8)
