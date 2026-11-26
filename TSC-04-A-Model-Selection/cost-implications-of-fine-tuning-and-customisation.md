---
id: 04.03.A.K4
tsc: 4
level: Advanced
code: K4
title: Cost implications of fine-tuning and customisation
---

# Cost implications of fine-tuning and customisation

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K4**

**IMDA requirement:** Complexities of fine-tuning and customising AI models for specific tasks or outputs (including implications of models' size and features on the cost).

**What it means:** Fine-tuning and customisation are not free: bigger models cost more to fine-tune and run, and customising introduces maintenance (the fine-tune goes stale as the domain changes). The skill is pricing the full lifecycle, not just the one-off run.

**The learner must be able to:**
- Name the cost drivers of fine-tuning.
- Explain why a custom model needs maintenance.
- Price a fine-tune over its lifetime.

**Lesson Plan Ideas:**
1. Contrast 'one fine-tune run' vs 'a custom model you must maintain'. 
2. Teach the cost drivers (size, data, retraining). 
3. Learners estimate lifetime cost for a scenario. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
A fine-tuned model must be retrained whenever the domain data changes. What does that do to its lifetime cost?
```
Expected: it turns a one-off into a recurring cost — retraining, re-evaluation, redeployment.

**Common mistakes:**
- Pricing only the initial fine-tune, not the maintenance.
- Fine-tuning a large model when a small one would do.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 3.3)
