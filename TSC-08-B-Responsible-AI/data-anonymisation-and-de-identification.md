---
id: 08.01.B.K3
tsc: 8
level: Basic
code: K3
title: Data anonymisation and de-identification
---

# Data anonymisation and de-identification

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Knowledge K3**

**IMDA requirement:** Data anonymisation and de-identification techniques.

**What it means:** Anonymisation removes identifying details so a person cannot be traced: masking (hide part), perturbation (change values slightly), and pseudonymisation (replace names with codes). De-identification is the goal — the techniques are the way there.

**The learner must be able to:**
- Distinguish anonymisation from pseudonymisation.
- Name the three techniques.
- Explain why 'removing the name' is not enough.

**Lesson Plan Ideas:**
1. Teach the three techniques with a customer record.
2. Show why name-only removal fails (other fields still identify).
3. Learners anonymise a sample record.
4. Debrief.

**Exercise (with the exact prompt):**
```text
Anonymise: "Mdm Tan, 65, diabetic, Blk 12 Bedok, S1234567A." Which fields must change, not just the name?
```
Expected: NRIC, address, age + condition — not just the name.

**Common mistakes:**
- Removing only the name and calling it anonymous.
- Confusing pseudonymisation (reversible) with anonymisation (not).

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [governance-and-ethics.md](../core-knowledge/governance-and-ethics.md) (section 1)

