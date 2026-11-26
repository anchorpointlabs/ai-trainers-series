---
id: 04.02.I.A2
tsc: 4
level: Intermediate
code: A2
title: Implement models for specific domains or styles
---

# Implement models for specific domains or styles

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A2**

**IMDA requirement:** Implement models to create content in specific domains or styles.

**What it means:** A general model can be steered to a domain (medical, legal, marketing) or a style (formal, playful) through prompting and examples. 'Implementing' here means setting up the prompt + examples so the model produces that domain's content reliably.

**The learner must be able to:**
- Steer a model to a domain with a prompt.
- Use few-shot examples to fix a style.
- Explain why examples anchor the style.

**Lesson Plan Ideas:**
1. Show a generic output vs a domain-steered output. 
2. Teach 'few-shot anchors the style'. 
3. Learners steer a model to a style with two examples. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
Steer the model to write a formal legal tone. Provide two example sentences in that tone, then ask it to rewrite a casual note.
```
Expected: the rewrite matches the legal tone of the examples.

**Common mistakes:**
- Expecting a domain style without examples or instruction.
- Using one example and expecting a consistent style.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 3)
