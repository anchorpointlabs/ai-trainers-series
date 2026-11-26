---
id: 02.01.B.A3
tsc: 2
level: Basic
code: A3
title: Apply basic anonymisation techniques
---

# Apply basic anonymisation techniques

> **TSC #2 Prompt Design · Basic · Ability A3**

**Bullet (verbatim):** Apply basic anonymisation techniques (e.g., data masking, perturbation, pseudonymisation).

**What it means:** Anonymisation means changing information about people so they cannot reasonably be identified. Data masking hides parts of a value; perturbation makes changes to values; pseudonymisation replaces identifying details with made-up labels. [2] These changes can keep useful context, but re-identification—working out who a record belongs to, including by combining it with other information—may still be possible. Pseudonymisation is not necessarily anonymisation, especially if a separate list links labels to people. [2] [3]

**The learner must be able to:**
- Explain masking, perturbation and pseudonymisation using an example of each.
- Apply all three techniques to fictional records while keeping useful information for the task.
- Check the changed records against the stated rules and identify what they can still be used for.
- Explain how someone might re-identify a person and why pseudonymisation alone does not necessarily make data anonymous.

**How to teach it in 20 minutes:**
1. Ask: “If a list of support visits has no names, is it necessarily anonymous?” Invite a reason for each answer. (3 min)
2. Use invented records to demonstrate each change: mask `ZX1234` as `ZX****`, perturb a wait of 12 minutes to 14, and replace a customer's name with a made-up label, using the same label for repeat visits. Explain that topics and approximate waits remain useful for discussing service waits, but the changed times are not exact. A separate name-to-label list or an unusual combination of details could link a record to a person. For real work, keep any name-to-label list separate and secure, assess identification risk in the intended sharing context, and do not put real personal data into a chatbot (a computer service that responds to typed messages). [2] [3] (7 min)
3. In pairs, learners apply all three rules by hand to every fictional row in the exercise, before running the prompt. They then compare their own table with the AI answer and the check below. (8 min)
4. Debrief one discrepancy and why it occurred. Explain that a named public post about an unusual topic and approximate wait might be matched to a row; a leaked name-to-label list could also reveal the person. The fixed adjustments here make marking easy but can be reversed if known; they do not guarantee privacy. [2] [3] (2 min)

**Exercise (with the exact prompt):**
*Setup: pairs need paper and access to a chat AI; first make all three changes by hand to the invented rows in the prompt, then paste it for a comparison.*

```text
These records are entirely invented for a classroom activity. Use only the data and rules below. Produce a worked answer for the learner to check, not a claim that the result is anonymous.

Fictional visit records:
Customer | Reference | Topic | Wait (minutes)
Brel | ZP4829 | delivery | 12
Nivo | QM7361 | returns | 7
Brel | ZP4829 | returns | 20

For each row:
- Pseudonymise the customer: replace Brel with P07 and Nivo with P23. Use the same replacement every time a customer recurs.
- Mask the reference: retain the first two letters and replace all four digits with ****.
- Perturb the wait: add 2 minutes in row 1, subtract 1 minute in row 2, and add 1 minute in row 3. These fixed adjustments are only for a checkable demonstration.
- Keep the topic unchanged.

Return only a table with columns Pseudonym | Masked reference | Topic | Adjusted wait (minutes), followed by one sentence explaining why the result would not necessarily be anonymous if these were real people's records.
```

Expected result: in order, the rows are `P07 | ZP**** | delivery | 14`, `P23 | QM**** | returns | 6`, and `P07 | ZP**** | returns | 21`.
What to check: compare both tables with those rows; confirm the repeated label, masked digits, changed waits and retained topics, and explain a possible link back to a person.

**Common mistakes:**
- Masking the reference but leaving the customer's name — replace the name with the agreed made-up label too.
- Treating the changed waits as exact — keep them for approximate discussion, not for a task requiring exact waits.
- Calling the result anonymous because names were replaced — check whether a separate list or other available details could identify someone; never paste real personal data into a chatbot.

**Sources:**
- [1] https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf — accessed 2026-11-15; page 5 confirms the TSC, level and verbatim bullet.
- [2] https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/guide-to-basic-anonymisation-%28updated-24-july-2024%29.pdf — accessed 2026-11-15; defines character masking, perturbation and pseudonymisation, explains the usefulness trade-off, reversible changes and keeping the identity list secure.
- [3] https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-sharing/anonymisation/introduction-to-anonymisation/ — accessed 2026-11-15; explains identification using other information and why pseudonymisation is not the same as anonymisation.
- [4] https://developers.openai.com/api/docs/guides/advanced-usage — accessed 2026-11-15; explains that Chat Completions outputs can differ between requests.

**Related:** [Masking, perturbation, pseudonymisation](../TSC-01-B-GenAI-Principles/masking-perturbation-pseudonymisation.md) — the same skill at a different level.
