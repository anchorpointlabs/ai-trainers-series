---
id: 03.03.A.K2
tsc: 3
level: Advanced
code: K2
title: Conditional prompts, context manipulation, refining
---

# Conditional prompts, context manipulation, refining

> **TSC #3 Prompt Engineering · Advanced · Knowledge K2**

**IMDA requirement:** Concepts in prompt engineering (e.g., conditional prompts, context manipulation, refining for specific outputs).

**What it means:** Three levers, one idea: you steer what the model attends to. **Conditional prompts** are 'if-then' instructions (if the input is X, do Y). **Context manipulation** is choosing *which* background to put in the window and in what order. **Refining** is iterating — take the first output, tighten the instruction, run again. Together they are how you convert a one-shot guess into a controlled result.

**The learner must be able to:**
- Write an if-then prompt for a real task.
- Reorder the context in a prompt and describe how it changes the output.
- Refine a prompt across three passes and say what each pass changed.

**Lesson Plan Ideas:**
1. Define the three levers with one example each. 
2. Show one prompt rewritten three ways (conditional, reordered context, refined). 
3. Learners take a pasted email and write a conditional prompt to categorise it. 
4. Share and compare outputs; note how reordering changed the answer. 

**Exercise (with the exact prompt):**
```text
Read the email below. If it is a customer complaint, reply with a 3-bullet apology and a next step. If it is a refund request, list the two pieces of evidence the customer must attach. If it is neither, reply 'not a service request'.

<email>
```
Expected: the reply follows the matching branch only.

**Common mistakes:**
- Using 'please' and politeness as if they were the lever — the lever is the conditional structure.
- Putting the most important context last, where the model weighs it less.
- Accepting the first output instead of refining it.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 4)
