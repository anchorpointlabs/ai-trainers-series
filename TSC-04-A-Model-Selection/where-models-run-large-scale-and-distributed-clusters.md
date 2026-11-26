---
id: 04.03.A.K1
tsc: 4
level: Advanced
code: K1
title: Where models run — large-scale and distributed clusters
---

# Where models run — large-scale and distributed clusters

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K1**

**IMDA requirement:** Applications and domains where generative AI models are used (e.g., large-scale and distributed computing clusters).

**What it means:** At production scale, models run on distributed clusters — many machines splitting the work. This matters for selection because scale changes the constraints: latency, throughput, and cost behave differently than on a single demo call.

**The learner must be able to:**
- Explain what a distributed cluster is for.
- Name how scale changes model constraints.
- Relate scale to a selection decision.

**Lesson Plan Ideas:**
1. Draw 'one machine' vs 'many machines' and why scale matters. 
2. Teach throughput vs latency at scale. 
3. Learners name which model trait matters more at scale. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
You need 10,000 generations a minute. Which matters more — raw model quality or throughput? Why?
```
Expected: throughput, because latency and capacity dominate at scale.

**Common mistakes:**
- Choosing a model on quality alone, ignoring scale constraints.
- Assuming demo performance equals production performance.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 3.4)
