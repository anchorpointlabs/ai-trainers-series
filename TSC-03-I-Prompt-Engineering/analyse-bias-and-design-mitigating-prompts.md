---
id: 03.02.I.A7
tsc: 3
level: Intermediate
code: A7
title: Analyse bias and design mitigating prompts
---

# Analyse bias and design mitigating prompts

> **TSC #3 Prompt Engineering · Intermediate · Ability A7**

**IMDA requirement:** Analyse potential bias in foundation model responses and design prompts that mitigate the bias.

**What it means:** Models echo the bias in their training data — gender, race, language, profession. The skill is catching a biased output and re-prompting to mitigate it (e.g. 'use gender-neutral language', 'show a balanced set of examples').

**The learner must be able to:**
- Spot bias in a model's output.
- Write a re-prompt that mitigates it.
- Explain why the bias appears.

**Lesson Plan Ideas:**
1. Show a biased output (a model assuming a nurse is 'she').
2. Teach 'the model echoes its training data — check, then re-prompt'.
3. Learners re-prompt a biased output to fix it.
4. Debrief what the re-prompt changed.

**Exercise (with the exact prompt):**
```text
Output to fix: "The nurse told the patient she would check on him." Re-prompt so the nurse is not assumed female.
```
Expected: a re-prompt like 'rewrite using gender-neutral terms for the nurse'.

**Common mistakes:**
- Ignoring bias because 'it's just the model'.
- Assuming a single re-prompt cannot help.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 2.3)

