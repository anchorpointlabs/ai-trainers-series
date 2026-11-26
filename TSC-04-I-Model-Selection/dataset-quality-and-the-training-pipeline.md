---
id: 04.02.I.K5
tsc: 4
level: Intermediate
code: K5
title: Dataset quality and the training pipeline
---

# Dataset quality and the training pipeline

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K5**

**IMDA requirement:** Significance of dataset quality and model training, including data management (e.g., extract, transform and load process).

**What it means:** A model is only as good as its data. The **ETL** pipeline (extract, transform, load) governs how raw data becomes training data, and bad data — duplicates, bias, mislabels — produces bad models. For selection, this matters because a model's published quality reflects its training data.

**The learner must be able to:**
- Explain why data quality drives model quality.
- Name the ETL stages.
- Spot a data-quality risk in a dataset description.

**Lesson Plan Ideas:**
1. Use 'garbage in, garbage out' as the anchor. 
2. Walk ETL with a simple example. 
3. Learners list what could go wrong in a messy customer dataset. 
4. Debrief. 

**Exercise (with the exact prompt):**
```text
A training dataset has duplicate rows and missing labels. List two ways the resulting model could misbehave.
```
Expected: the model over-fits duplicates and fails on unseen cases.

**Common mistakes:**
- Assuming a model's quality is independent of its data.
- Skipping data cleaning before training or fine-tuning.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [model-selection-and-evaluation.md](../core-knowledge/model-selection-and-evaluation.md) (section 2.4)
