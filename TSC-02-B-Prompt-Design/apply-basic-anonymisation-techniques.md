---
id: 02.01.B.A3
tsc: 2
level: Basic
code: A3
title: Apply basic anonymisation techniques
---

# Apply basic anonymisation techniques

> **TSC #2 Prompt Design · Basic · Ability A3**

> **Framework text (verbatim):** "Apply basic anonymisation techniques (e.g., data masking, perturbation, pseudonymisation)."
>
> **TSC #2** Prompt Design · Basic · Ability · Bullet 14 of 15

**One-line version:** Three cheap changes make a record less identifying — hide part of a value, shift a value, swap a name for a label — and none of them makes it anonymous.

## What it is

Anonymisation is changing information about people so that they cannot reasonably be identified. Three basic techniques reduce the risk. **Data masking** hides part of a value (`ZP4829` becomes `ZP****`). **Perturbation** changes a value slightly (a 12-minute wait becomes 14). **Pseudonymisation** replaces identifying details with made-up labels, consistently — the same label every time a person recurs. Each keeps something useful for the task, and each leaves a route back to the individual if someone has the other pieces.

## Deep expansion

### The concept

The three techniques are taught together because they trade off the same two things: usefulness and identifiability. Masking keeps the format but destroys the link. Perturbation keeps the pattern but corrupts the exact figure. Pseudonymisation keeps the relationships — repeat visits, sequences, counts — while removing the name. Choosing among them is choosing which feature your task needs.

Two warnings sit on top of all three.

**Reversibility.** A fixed rule ("always mask the last four digits", "always add two minutes") is easy to apply and easy to undo if someone knows the rule. For a classroom demonstration that is an advantage, because the answer is checkable. For real data it is a weakness: the change is a transformation, not a guarantee.

**Linkage.** Anonymity is a property of a dataset in a context, not of a row in isolation. A person who has the name-to-label list can undo pseudonymisation in one step. A person who knows the workplace can recognise "the only Year 6 teacher in that block with a rare complaint". Basic learners do not need the mathematics of re-identification; they need the habit of asking "who else could join this up?"

### The sub-concepts

**Masking: keep the shape, lose the identifier.** Good for reference numbers, account codes, NRIC fragments in a demonstration. Poor for anything where the visible part is itself distinctive.

**Perturbation: keep the distribution, lose the exact value.** Useful for "roughly how long do people wait", useless for "what was this person's exact wait". Say which you need before you perturb.

**Pseudonymisation: keep the relationships, lose the name.** The most useful of the three for analysis, and the most commonly mistaken for anonymisation. It is a change of label, not a removal of risk — especially if the mapping table exists anywhere.

**Consistency is the whole point of a label.** If Brel becomes P07 on one row and P12 on the next, the dataset lies about repeat visits. The rule must be "same label, every time".

**The mapping list is the crown jewel.** If you keep one, keep it separate, keep it secure, and keep it out of the prompt. A pseudonymised dataset plus a careless mapping file is a named dataset with extra steps.

**Do not paste real data into a chatbot.** Even anonymised-in-principle data. The safest rule for Basic learners is the one the framework implies: work on invented or properly approved data, and let the organisation decide what counts as safe.

### How it connects to the rest of the framework

`TSC2-Basic-K6` is the legal baseline these techniques serve; `TSC2-Basic-A7` covers the prompt misuses — including pasting identifiable data — that make the techniques necessary; `TSC2-Basic-K4` is the output-side control. The same three techniques, at greater depth and with the reversibility argument spelled out, are `TSC1-Basic-A4`.

### What is current as of November 2026

Two shifts. First, guidance has settled on risk-based thinking: the question is not "is this anonymous?" but "how likely is identification in this context, and what else could be joined to it?" That framing is teachable at Basic level and much more useful than a binary. Second, models are better at pattern completion, which raises the stakes on weak masking: give a 2026 frontier model a masked reference plus a job title plus a postal code and it will happily propose a plausible identity. The models are not looking anything up; they are completing a pattern. That is exactly why the human has to be the one deciding whether the pattern is safe.

### Common misconceptions

- *"No names means anonymous."* Names are one identifier among many.
- *"Pseudonymised is anonymised."* Only if the mapping cannot be recovered and nothing else identifies the person.
- *"Perturbation protects the person."* It protects against exact matching, not against a distinctive combination.
- *"Masking is enough for a chatbot."* Chatbot use is an organisational decision, not a technique decision.

## How a student should understand it

**Mental model:** blurring a face in a video but leaving the uniform, the car plate and the house number. The most obvious identifier is gone; the person is still recognisable to anyone who knows them.

**Things they can do after this bullet:**
1. Explain each technique with an example, and say what it preserves.
2. Apply all three to invented records without losing the analysis.
3. Describe one route back to an individual, and name the next step before real use.

**Misconceptions to kill:** names-as-the-test; pseudonym-equals-anonymous; fixed rules as protection.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The exam script number.** During marking, scripts carry index numbers, not names, so markers judge the work. That is pseudonymisation, and it works because the number list is held by one person and never circulated. Where it breaks: exam scripts are read by people with no other data about the candidate; a support record carries a topic, a date and a location that narrow the field.

### Worked example with a real tool

Do the transformations by hand first, then paste this to compare.

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

What to point at afterwards: three techniques, three preserved features. The label keeps repeat visits visible (P07 appears twice). The mask keeps the reference format. The perturbation keeps the shape of the waits while making exact matching wrong. Then ask the class to do the attacker's job: what would you need to identify P07? The mapping list, or the topic plus the date plus a small team. That exercise does more than any definition.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If a list of support visits has no names, is it necessarily anonymous?" Invite a reason for each answer.
2. **State the objective** — by the end you can apply all three techniques and explain one re-identification route.
3. **Recall prior learning** — the identifiability definition from `TSC2-Basic-K6`.
4. **Present the content** — the three techniques, what each preserves, reversibility and linkage.
5. **Guide** — transform row 1 together on the board, arguing about what to keep.
6. **Elicit performance** — pairs complete all three rows by hand before running the prompt.
7. **Give feedback** — compare tables; mark any inconsistent label, unmasked digit or unchanged wait.
8. **Transfer** — each learner names one dataset in their work that would need this before any AI use.

## What the framework doesn't mention but trainers need to know

- **Pseudonymisation is the technique learners will over-trust.** It produces the tidiest output and the weakest guarantee.
- **Usefulness is a real constraint.** If masking destroys the analysis, the answer is "do not use this data here", not "mask harder".
- **The mapping list is the exam-script number list.** One holder, secured, never pasted.
- **Consent does not transfer with the label.** Pseudonymising data does not create permission to use it for a new purpose.

## Watch out

- **Do not describe any output as anonymous.** Say "less identifying, and still not anonymous" — because that is true, and it is the sentence they will remember.
- **Do not use real records in the demo, even anonymised ones.** Invented rows teach the technique with none of the risk.
- **Do not skip the attacker's question.** Without it, the class learns three procedures and no judgement.
- **The stale claim to retire:** "we removed the names, so it's fine to paste." In November 2026 that is the most expensive sentence in a Singapore office.

---

**Related:** [Masking, perturbation, pseudonymisation](../TSC-01-B-GenAI-Principles/masking-perturbation-pseudonymisation.md) — the same three techniques at the principles level.
