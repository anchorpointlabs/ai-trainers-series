---
id: 03.02.I.K4
tsc: 3
level: Intermediate
code: K4
title: Context window limits and how to work within them
---

# Context window limits and how to work within them

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K4**

**Bullet (verbatim):** Context window limitations, long context implications and strategies to work within them.

**What it means:** The model has a fixed working memory — the context window. Beyond it, the beginning is forgotten. Long inputs degrade quality (the model loses the thread and weighs the middle poorly). Strategies: keep it short, put the important context first, summarise long inputs, and start a fresh chat when the thread gets messy.

**The learner must be able to:**
- Explain the context window in plain words.
- Apply the strategies: summarise, prioritise, start fresh.
- Decide what to cut from an over-long prompt.

**How to teach it in 20 minutes:**
1. Use the 'goldfish with a PhD' picture (brilliant for 30 seconds, then forgets). (4 min)
2. Teach the three strategies. (5 min)
3. Learners trim an over-long prompt, choosing what to keep. (7 min)
4. Debrief what mattered most. (4 min)

**Exercise (with the exact prompt):**
```text
You pasted a 10-page report and the model's answer ignored your first instruction. Which three strategies would fix it?
```
Expected: summarise the report, put the instruction first, or split into a fresh chat.

**Common mistakes:**
- Pasting a huge document and expecting perfect recall of every part.
- Continuing a messy 50-message chat instead of starting fresh.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [prompting.md](../core-knowledge/prompting.md) (section 5)
