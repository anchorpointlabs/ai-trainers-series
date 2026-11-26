---
id: 03.03.A.A1
tsc: 3
level: Advanced
code: A1
title: Create prompts for precise and diverse responses
---

# Create prompts for precise and diverse responses

> **TSC #3 Prompt Engineering · Advanced · Ability A1**

**IMDA requirement:** Create prompts to elicit precise and diverse responses from AI models.

**What it means:** Precise = the output matches the exact shape you asked for. Diverse = the model explores genuinely different options instead of minor variations of one idea. You control each with different levers: precision comes from constraints and format; diversity comes from asking for distinct angles and a higher temperature.

**The learner must be able to:**
- Write one prompt optimised for precision and one for diversity.
- Explain which levers (format, constraints, temperature) serve which goal.

**Lesson Plan Ideas:**
1. Show a precise output (a fixed-format table) vs a diverse one (ten different slogans).
2. Name the levers.
3. Learners write both prompts for one task.
4. Compare and tune.

**Exercise (with the exact prompt):**
```text
Precision: List the 5 risks of this plan as a table with columns Risk, Likelihood (High/Med/Low), Owner. No other text.
Diversity: Give 10 taglines for a pickleball club, each in a different emotional register.
```
Expected: the first is a clean table, the second ten clearly different tones.

**Common mistakes:**
- Using the same prompt style for both goals and being disappointed with one of them.
- Thinking 'be creative' produces diversity without direction.
- Adding constraints that fight each other (precise AND free-form).

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (sections 4, 9)

