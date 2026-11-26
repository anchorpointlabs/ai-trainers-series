---
id: 03.03.A.K6
tsc: 3
level: Advanced
code: K6
title: Prompt engineering tools and frameworks
---

# Prompt engineering tools and frameworks

> **TSC #3 Prompt Engineering · Advanced · Knowledge K6**

**IMDA requirement:** Use of prompt engineering tools and frameworks to streamline implementation of prompt engineering methods.

**What it means:** Tools and frameworks turn prompt techniques from ad-hoc typing into reusable, testable assets: versioning, templating, evaluation harnesses, and batch runs against a test set. The skill is not the tool; it is knowing that a prompt is a component to be managed like code, not a chat message to retype.

**The learner must be able to:**
- Name what a prompt tool buys you (versioning, testing, reuse).
- Explain why you would template a prompt rather than retype it.
- Choose a tool for a given team need.

**Lesson Plan Ideas:**
1. Contrast 'prompt in a chat window' with 'prompt as a managed asset'. 
2. Walk one templated prompt with placeholders. 
3. Learners template a real prompt, replacing names/dates with placeholders. 
4. Debrief what would break if the template changed. 

**Exercise (with the exact prompt):**
```text
Turn this into a reusable template with placeholders in {braces}:

'Dear Ms Tan, thank you for your enquiry about the Python course. The next intake is 12 May and it costs $480.'
```
Expected: placeholders for name, course, date, price — reusable across customers.

**Common mistakes:**
- Treating the chat window as the permanent home of a prompt (no versioning).
- Over-tooling a one-off question that needs no reuse.
- Confusing the framework with the method — the prompt design is what matters.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 9)
