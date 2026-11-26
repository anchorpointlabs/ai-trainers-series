---
id: 09.01.B.K1
tsc: 9
level: Basic
code: K1
title: Fundamentals of AI model security
---

# Fundamentals of AI model security

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Knowledge K1**

**IMDA requirement:** Fundamental concepts of AI model security, including importance of monitoring and reporting risks.

**What it means:** AI models are attacked through their inputs, not just their code. A prompt is a new door into the system — the model reads text and may act on it. Security means treating the model as a gullible but powerful worker: monitor what it does, and report anything odd.

**The learner must be able to:**
- Explain why a prompt is a security surface.
- State why monitoring and reporting matter.
- Name one sign that a model has been tricked.

**Lesson Plan Ideas:**
1. Use the gullible-intern analogy as the frame.
2. Teach 'the prompt is a door, not just a question'.
3. Learners list what could go wrong if nobody monitors an AI that reads emails.
4. Debrief.

**Exercise (with the exact prompt):**
```text
An AI assistant auto-replies to customer emails. List two things that should be monitored to catch abuse.
```
Expected: unusual instructions in emails, and any action the AI takes (sending, transferring).

**Common mistakes:**
- Thinking security is only about the model's code.
- Treating the AI's actions as always safe because it is 'just text'.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 1)

