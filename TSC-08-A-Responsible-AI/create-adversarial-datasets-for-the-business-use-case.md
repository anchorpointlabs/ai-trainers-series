---
id: 08.03.A.A3
tsc: 8
level: Advanced
code: A3
title: Create adversarial datasets for the business use case
---

# Create adversarial datasets for the business use case

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A3**

**IMDA requirement:** Create adversarial datasets for the business use case.

**What it means:** An adversarial dataset is built to break the model — inputs designed to trigger bias, failure, or unsafe output, specific to *your* use case. Building one means thinking like an attacker and like the worst-case user.

**The learner must be able to:**
- Build an adversarial example for a use case.
- Explain why adversarial testing beats ordinary testing.
- Turn a failure into a new test case.

**Lesson Plan Ideas:**
1. Contrast ordinary test data with adversarial data. 
2. Build adversarial examples together for a use case. 
3. Learners add an adversarial case. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
For a customer-service bot, write two adversarial inputs that would expose bias or unsafe output.
```
Expected: e.g. a dialect-heavy insult, and a request that tests for gender/race bias.

**Common mistakes:**
- Testing only with polite, normal inputs.
- Not turning a discovered failure into a permanent test case.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 8)
