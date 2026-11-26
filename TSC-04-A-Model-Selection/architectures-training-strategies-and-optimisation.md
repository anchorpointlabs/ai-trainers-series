---
id: 04.03.A.K2
tsc: 4
level: Advanced
code: K2
title: Architectures, training strategies, and optimisation
---

# Architectures, training strategies, and optimisation

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K2**

**Bullet (verbatim):** Concepts in generative AI, including model architectures, training strategies, and optimisation techniques (including pre-training vs fine-tuning for specialised tasks or domains).

**What it means:** Pre-training builds the base model from broad data; fine-tuning adapts it to a specialised domain. The choice between them is a selection decision: pre-training is vast and expensive; fine-tuning is cheap and targeted but inherits the base model's limits.

**The learner must be able to:**
- Contrast pre-training and fine-tuning.
- Explain when fine-tuning is the right choice.
- Name an optimisation technique (quantisation, distillation).

**How to teach it in 20 minutes:**
1. Reuse the 'general schooling vs bootcamp' analogy. (4 min)
2. Teach the cost/benefit of fine-tuning. (5 min)
3. Learners decide pre-train vs fine-tune for a scenario. (7 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
You need a model for Singapore legal contracts. Pre-train from scratch, or fine-tune an existing model? Justify.
```
Expected: fine-tune — pre-training is prohibitive, and the base model already knows language.

**Common mistakes:**
- Assuming pre-training from scratch is ever the cheap option.
- Fine-tuning when prompting or RAG would do.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 2.4)
