---
id: 03.02.I.K1
tsc: 3
level: Intermediate
code: K1
title: Theoretical frameworks of prompt engineering
---

# Theoretical frameworks of prompt engineering

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K1**

**IMDA requirement:** Theoretical frameworks of prompt engineering techniques.

**What it means:** A "framework" here is a reusable structure for a good prompt — role-context-task-format, few-shot examples, chain-of-thought, system-vs-user messages. They are lenses for organising a brief, not fixed recipes, and the craft is choosing the right frame for the task.

**The learner must be able to:**
- Name three prompt frameworks and what each is for.
- Explain that a framework is a reusable structure, not a magic formula.
- Decompose a real prompt into its framework parts.

**Lesson Plan Ideas:**
1. Show one strong prompt and label its parts (role, context, task, format). 
2. Introduce two more frames (few-shot, chain-of-thought) with one line each. 
3. Learners re-write a weak prompt using one framework. 
4. Debrief which frame fitted which task. 

**Exercise (with the exact prompt):**
```text
Label each part of this prompt as role / context / task / format:
"You are a safety inspector. Here are three incident reports. List the root cause of each as a table with columns Report, Cause, Evidence. If the cause is unclear, say so."
```
Expected: learners correctly label role, context (reports), task (list root cause), format (table).

**Common mistakes:**
- Thinking 'framework' means a fixed magic formula.
- Mixing several frameworks incoherently in one prompt.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (sections 3, 4)
