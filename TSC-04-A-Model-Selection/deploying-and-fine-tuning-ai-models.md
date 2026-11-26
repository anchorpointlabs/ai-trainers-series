---
id: 04.03.A.K3
tsc: 4
level: Advanced
code: K3
title: Deploying and fine-tuning AI models
---

# Deploying and fine-tuning AI models

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K3**

**IMDA requirement:** Workflow of deploying and fine-tuning AI models.

**What it means:** Deployment and fine-tuning follow a workflow: prepare data, choose a base model, fine-tune, evaluate against a test set, then deploy behind a gateway with pinned versions and monitoring. It is an engineering lifecycle, not a one-off action.

**The learner must be able to:**
- Describe the fine-tune-then-deploy workflow.
- Explain version pinning and monitoring.
- Name the evaluation step's role.

**Lesson Plan Ideas:**
1. Walk the lifecycle end-to-end on the board.
2. Teach version pinning with a 'don't move the goalposts' example.
3. Learners order the workflow steps.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Put these in order and explain: deploy, prepare data, pin version, evaluate, fine-tune, monitor.
```
Expected: prepare → fine-tune → evaluate → deploy (pin version) → monitor.

**Common mistakes:**
- Deploying without pinning versions, so behaviour silently changes.
- Skipping evaluation after fine-tuning.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 10)

