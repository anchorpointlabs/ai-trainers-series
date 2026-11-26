---
id: 03.03.A.K7
tsc: 3
level: Advanced
code: K7
title: Fine-tuning on a RAG knowledge base
---

# Fine-tuning on a RAG knowledge base

> **TSC #3 Prompt Engineering · Advanced · Knowledge K7**

**Bullet (verbatim):** Modification of model configurations to optimise output (e.g., use of fine tuning based on RAG knowledge base).

**What it means:** RAG injects knowledge at *answer time*; fine-tuning bakes it into the *weights* during training. Fine-tuning on a RAG-derived dataset means using retrieved question-answer pairs as training examples so the model learns the domain's style. Fine-tuning changes *how* the model writes; RAG changes *what* it knows. They are complements, not rivals.

**The learner must be able to:**
- Distinguish fine-tuning (weights) from RAG (context).
- Explain when fine-tuning is worth the cost vs. plain RAG.
- Describe what data you would need to fine-tune.

**How to teach it in 20 minutes:**
1. Use the 'bootcamp vs open-book manual' analogy (from TSC #4). (3 min)
2. Contrast the two failure modes: stale weights vs. stale context. (5 min)
3. Learners decide, for three scenarios, whether to fine-tune, use RAG, or both. (7 min)
4. Debrief the cost/benefit. (5 min)

**Exercise (with the exact prompt):**
```text
You are deciding between RAG and fine-tuning for a clinic's SOP chatbot. List one reason to use RAG alone, one reason fine-tuning alone would fail, and one case where you would use both.
```
Expected: RAG for fresh policy, fine-tuning alone fails (policy changes), both for style + facts.

**Common mistakes:**
- Assuming fine-tuning is always better than RAG (it is costlier and goes stale).
- Fine-tuning on too little or unlabelled data and expecting accuracy.
- Treating the two as the same thing.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md)
