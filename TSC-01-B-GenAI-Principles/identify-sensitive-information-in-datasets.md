---
id: 01.01.B.A3
tsc: 1
level: Basic
code: A3
title: Identify sensitive information in datasets
---

# Identify sensitive information in datasets

> **TSC #1 Generative AI Principles and Applications · Basic · Ability A3**

**Bullet (verbatim):** Identify sensitive information in datasets.

**What it means:** Sensitive data is **personal data** (names, NRIC, contact, health) plus **confidential data** (trade secrets, client lists). Before any dataset is used — for training, analysis, or pasting into a tool — scan it for these. The noticeboard test: if you would not pin it publicly, treat it as sensitive.

**The learner must be able to:**
- Spot personal and confidential data in a sample.
- Flag indirect identifiers (an email alone is personal data).
- Decide whether a dataset can be used or must be cleaned.

**How to teach it in 20 minutes:**
1. Give the noticeboard test as the one-line rule. (3 min)
2. Walk a sample row and circle the sensitive fields. (5 min)
3. Learners scan a short customer list and flag every sensitive item. (7 min)
4. Debrief the indirect identifiers they missed. (5 min)

**Exercise (with the exact prompt):**
```text
Flag every sensitive item:
"Customer 412 — Mdm Tan, NRIC S1234567A, 65-year-old diabetic, lives at Blk 12 Bedok."
```
Expected: name, NRIC, age + health condition, and address are all flagged as personal data.

**Common mistakes:**
- Missing indirect identifiers (email, phone, address are personal data).
- Assuming a small dataset is safe.
- Confusing 'anonymised' with 'safe to share' without checking.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 1)
