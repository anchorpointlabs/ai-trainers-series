---
id: 04.02.I.K1
tsc: 4
level: Intermediate
code: K1
title: How models work — transformers, attention, encoders and decoders
---

# How models work — transformers, attention, encoders and decoders

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K1**

**Bullet (verbatim):** Principles behind generative AI model operation and output generation (e.g., how model is trained, transformers and attention mechanisms, encoders and decoders in large language models, modality gap).

**What it means:** Under the hood, a modern model is a **transformer** that uses **attention** to weigh which words matter when predicting the next one. **Encoders** read input into a representation; **decoders** generate output from it. The **modality gap** is why a text model is clumsy at images. You need the picture, not the maths, to choose a model sensibly.

**The learner must be able to:**
- Explain attention in one line (which words matter).
- Contrast encoder vs decoder.
- Explain why the modality gap matters for model choice.

**How to teach it in 20 minutes:**
1. Draw the transformer as 'reads the whole sentence, weighs each word, predicts the next'. (6 min)
2. Contrast encoder/decoder with an example. (5 min)
3. Learners explain the modality gap's effect on choosing an image vs text model. (5 min)
4. Debrief. (4 min)

**Exercise (with the exact prompt):**
```text
Explain, in plain words, why a text model is the wrong tool for generating an image, using 'modality gap'.
```
Expected: the learner connects the modality gap to why image and text models are separate.

**Common mistakes:**
- Thinking attention is 'the model reads left to right'.
- Ignoring the modality gap when picking a model for a task.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 2)
