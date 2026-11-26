---
id: 04.03.A.A1
tsc: 4
level: Advanced
code: A1
title: Deploy models for specialised tasks
---

# Deploy models for specialised tasks

> **TSC #4 Generative AI Model Selection · Advanced · Ability A1**

**IMDA requirement:** Deploy existing models for a variety of specialised tasks or creative applications (including using techniques such as pre-training or fine-tuning).

**What it means:** Deploying for a specialised task means taking an existing model and adapting it — via prompting, RAG, or fine-tuning — then putting it behind a stable, monitored endpoint. The skill is the whole path from 'generic model' to 'running in production'.

**The learner must be able to:**
- Choose an adaptation route (prompt vs RAG vs fine-tune).
- Describe a deployment with version pinning and monitoring.

**Lesson Plan Ideas:**
1. Show one specialised task solved three ways (prompt, RAG, fine-tune).
2. Teach 'pick the lightest route that meets the bar'.
3. Learners choose a route for a task and justify it.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Task: answer questions from a company handbook. Prompt, RAG, or fine-tune? Justify.
```
Expected: RAG — the handbook changes, and RAG injects fresh content without retraining.

**Common mistakes:**
- Reaching for fine-tuning before trying prompting or RAG.
- Deploying without monitoring or version pinning.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [rag-and-retrieval.md](../core-knowledge/rag-and-retrieval.md) (section 1)

