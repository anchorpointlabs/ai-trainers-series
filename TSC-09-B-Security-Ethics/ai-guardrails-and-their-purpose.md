---
id: 09.01.B.K3
tsc: 9
level: Basic
code: K3
title: AI guardrails and their purpose
---

# AI guardrails and their purpose

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Knowledge K3**

**IMDA requirement:** Introduction to AI guardrails and their purpose.

**What it means:** A guardrail is a control that keeps the AI inside safe behaviour — refusing harmful requests, blocking certain output, or escalating to a human. Its purpose is to bound the model's power so a mistake or an attack cannot cause damage.

**The learner must be able to:**
- Define a guardrail in one line.
- Name two types (input filter, output filter, human gate).
- Explain what a guardrail is protecting against.

**Lesson Plan Ideas:**
1. Compare a model with no guardrails to one with them (same input).
2. Teach the three types (input, output, human gate).
3. Learners match a guardrail to a risk.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Match each guardrail to its risk: input filter, output filter, human approval — for (a) harmful requests, (b) leaked data in replies, (c) large money transfers.
```
Expected: input→(a), output→(b), human→(c).

**Common mistakes:**
- Thinking guardrails are optional.
- Believing a guardrail is 'set and forget'.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 4)

