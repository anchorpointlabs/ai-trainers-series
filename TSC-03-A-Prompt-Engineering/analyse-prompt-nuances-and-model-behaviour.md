---
id: 03.03.A.A2
tsc: 3
level: Advanced
code: A2
title: Analyse prompt nuances and model behaviour
---

# Analyse prompt nuances and model behaviour

> **TSC #3 Prompt Engineering · Advanced · Ability A2**

**IMDA requirement:** Analyse the nuances of prompts and their influence on AI model behaviour.

**What it means:** Small wording changes shift output more than people expect: 'summarise' vs 'critique', 'list' vs 'explain', the placement of a constraint. The skill is reading an output and tracing *which part of the prompt* produced it, so you can predict and correct behaviour instead of guessing.

**The learner must be able to:**
- Take an output and point to the prompt wording that caused it.
- Change one word and predict the resulting shift.
- Describe how role, tone, and format words steer behaviour.

**Lesson Plan Ideas:**
1. Show two prompts differing by one word, with visibly different outputs.
2. Teach the trace: output feature → prompt cause.
3. Pairs get a prompt/output pair and highlight the causal wording.
4. Debrief the traces.

**Exercise (with the exact prompt):**
```text
Prompt: 'Explain the new leave policy.'
Output: a 400-word explanation.
Now: 'Summarise the new leave policy in 2 bullets.'
```
Expected: learners identify that 'explain' triggered length and 'summarise' + '2 bullets' triggered brevity.

**Common mistakes:**
- Blaming 'the model' for behaviour that the prompt wording caused.
- Assuming wording is neutral — every verb is an instruction.
- Not reading the output against the prompt before re-prompting.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (sections 4, 5)

