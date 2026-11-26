---
id: 03.03.A.A5
tsc: 3
level: Advanced
code: A5
title: Refine outputs and extend capabilities
---

# Refine outputs and extend capabilities

> **TSC #3 Prompt Engineering · Advanced · Ability A5**

**Bullet (verbatim):** Apply prompt engineering strategies to refine model outputs and extend capabilities of models.

**What it means:** Refining is a loop: generate, read against the goal, change one thing, regenerate. Extending is adding capability the base model lacks — retrieval, a tool call, a structured chain — through the prompt's orchestration rather than retraining. Both are iterative and testable.

**The learner must be able to:**
- Run a three-pass refinement on one prompt.
- Add a retrieval or tool step to a prompt to extend it.
- Explain what each pass changed and why.

**How to teach it in 20 minutes:**
1. Show a first-draft output, then two refinements, and name what changed each time. (5 min)
2. Demonstrate extending a prompt with a retrieval step. (5 min)
3. Learners refine a weak prompt across three passes. (6 min)
4. Share the before/after. (4 min)

**Exercise (with the exact prompt):**
```text
Pass 1: 'Write a complaint reply.'
Pass 2: add audience and tone. 'Reply to a customer complaint, apologetic but firm, 3 sentences.'
Pass 3: add a constraint. '...and do not promise a refund.'
```
Expected: each pass narrows the output toward the goal.

**Common mistakes:**
- Rewriting from scratch instead of changing one thing.
- Skipping the read-back step and refining blindly.
- Confusing refinement (same task, better output) with extension (new capability).

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 9)
