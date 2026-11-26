---
id: 03.03.A.A6
tsc: 3
level: Advanced
code: A6
title: Devise innovative prompt strategies
---

# Devise innovative prompt strategies

> **TSC #3 Prompt Engineering · Advanced · Ability A6**

**IMDA requirement:** Devise innovative prompt strategies that enhance generative AI capabilities.

**What it means:** Innovation here means *composing* known techniques into a new pipeline for a specific problem — not inventing new magic. Take a hard task, break it into stages, and assign the right technique to each stage (retrieve, then reason, then verify, then format). The creativity is in the decomposition and the verification step.

**The learner must be able to:**
- Decompose a hard task into stages.
- Assign a technique to each stage.
- Build in a verification step and explain why it matters.

**Lesson Plan Ideas:**
1. Present a task that defeats a single prompt; show it solved as a staged pipeline.
2. Teach 'decompose, assign, verify'.
3. Groups design a staged prompt for a real task and pitch it.
4. Vote on the strongest design.

**Exercise (with the exact prompt):**
```text
Task: check whether a supplier contract complies with 5 clauses. Design a 3-stage prompt: (1) extract the clauses, (2) check each against the contract, (3) output a compliance table with a 'verify me' column.
```
Expected: a staged pipeline with an explicit verification step.

**Common mistakes:**
- Assuming a single clever prompt beats a staged pipeline.
- Reinventing instead of composing the techniques you already know.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 3)

