---
id: 03.03.A.A4
tsc: 3
level: Advanced
code: A4
title: Evaluate effectiveness across scenarios
---

# Evaluate effectiveness across scenarios

> **TSC #3 Prompt Engineering · Advanced · Ability A4**

**Bullet (verbatim):** Evaluate the effectiveness and adaptability of prompt engineering methods across diverse scenarios.

**What it means:** A technique that works for one task may fail on another domain, language, or format. Adaptability is tested by deliberately varying the scenario — switch the audience, switch to Singlish, switch the output format — and watching where the method holds and where it cracks.

**The learner must be able to:**
- Run one method across two different scenarios and compare.
- Identify the variable that broke the method.
- Adjust the method to the new scenario and retest.

**How to teach it in 20 minutes:**
1. Take a method that works in English and run it in Singlish or a different format; show the crack. (5 min)
2. Teach 'vary one variable to test adaptability'. (3 min)
3. Learners stress-test a prompt across two scenarios. (7 min)
4. Debrief what they had to change. (5 min)

**Exercise (with the exact prompt):**
```text
Prompt: 'Summarise this meeting in 3 bullets for a formal report.'
Now run the same instruction, but the summary is for a WhatsApp message to a colleague in Singlish.
```
Expected: the formal version fails for WhatsApp; learners adjust register and length.

**Common mistakes:**
- Assuming one good prompt transfers unchanged to every scenario.
- Blaming the model for a domain gap that is really a prompt gap.
- Not retesting after adapting.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 5)
