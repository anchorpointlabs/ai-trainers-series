---
id: 09.02.I.K4
tsc: 9
level: Intermediate
code: K4
title: Risk management frameworks and trust-and-safety best practice
---

# Risk management frameworks and trust-and-safety best practice

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Knowledge K4**

**Bullet (verbatim):** Best practices for maintaining AI trust and safety, including risk management frameworks (e.g., risk assessment matrix, bowtie analysis, agile risk).

**What it means:** Frameworks make trust-and-safety a process, not a scramble: a risk matrix ranks, a bowtie maps causes to consequences, and agile risk embeds the checks into ongoing work. The skill is picking and running a framework so nothing is left to memory.

**The learner must be able to:**
- Name the frameworks and what each is for.
- Apply a bowtie to an AI failure.
- Explain 'agile risk' in one line.

**How to teach it in 20 minutes:**
1. Contrast the three frameworks with one example each. (6 min)
2. Walk a bowtie for a chatbot leak. (7 min)
3. Learners map a second failure with a bowtie. (5 min)
4. Debrief. (2 min)

**Exercise (with the exact prompt):**
```text
Draw a bowtie (causes — event — consequences) for: a support bot accidentally emails a customer's data to the wrong person.
```
Expected: causes (bad routing, no check), event (data sent), consequences (PDPA breach, reputational).

**Common mistakes:**
- Running no framework and relying on memory.
- Using a framework once and never again.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [ai-security.md](../core-knowledge/ai-security.md) (section 5)
