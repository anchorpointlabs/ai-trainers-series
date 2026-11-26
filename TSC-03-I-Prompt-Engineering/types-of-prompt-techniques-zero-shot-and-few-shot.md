---
id: 03.02.I.A3
tsc: 3
level: Intermediate
code: A3
title: Types of prompt techniques — zero-shot and few-shot
---

# Types of prompt techniques — zero-shot and few-shot

> **TSC #3 Prompt Engineering · Intermediate · Ability A3**

**IMDA requirement:** Identify the types of prompt engineering techniques (e.g., zero-shot and few-shot learning applied to foundation models).

**What it means:** **Zero-shot** is asking with no example — just the instruction. **Few-shot** is showing one or more examples in the prompt so the model copies the pattern. The skill is knowing when examples are worth the extra tokens: add them when the format or style matters and is hard to describe.

**The learner must be able to:**
- Distinguish zero-shot from few-shot.
- Convert a zero-shot prompt into few-shot.
- Decide when examples are worth it.

**Lesson Plan Ideas:**
1. Show the same task zero-shot (messy) vs few-shot (clean).
2. Teach 'zero-shot is asking, few-shot is showing'.
3. Learners add examples to a prompt that needs a format.
4. Debrief the token trade-off.

**Exercise (with the exact prompt):**
```text
Zero-shot: "Write a product update in the style of our release notes."
Few-shot: add two example release notes first, then the request.
```
Expected: the few-shot version matches the house style more closely.

**Common mistakes:**
- Always adding examples even when the instruction is enough.
- Never adding them when the format is hard to describe.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 3)

