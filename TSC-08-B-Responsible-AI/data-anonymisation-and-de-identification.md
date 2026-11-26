---
id: 08.01.B.K3
tsc: 8
level: Basic
code: K3
title: Data anonymisation and de-identification
as_at: 2026-11-26
review_by: 2027-02-25
---

# Data anonymisation and de-identification

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Knowledge K3**

> **Framework text (verbatim):** "Data anonymisation and de-identification techniques."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Knowledge · Bullet 3 of 10

**One-line version:** Removing the name is not anonymising — it is tidying. A record is only de-identified when the *combination* of what remains cannot point at one person.

## What it is

Anonymisation and de-identification are the techniques that reduce a dataset so that the people inside it can no longer be picked out. The common methods are masking (hide part of a field), perturbation (alter values slightly or generalise them), and pseudonymisation (replace identifiers with codes held separately). De-identification is the goal; the techniques are the route.

## Deep expansion

### The concept

Personal data has two lives: the one where it is useful and the one where it is dangerous. De-identification tries to keep the first and remove the second. It is not a deletion exercise — you keep the record, you keep its analytic value, and you remove the thread that leads back to a person.

The reason this is hard, and the reason it belongs in a Responsible AI course rather than an IT course, is that identification is *relational*, not field-by-field. A name identifies you on its own. A postcode does not. But a postcode, an age, a job title and a chronic condition, together, often narrow to a handful of people — and in a small organisation, to one. Every learner has had the experience of reading an "anonymous" survey response and knowing exactly who wrote it. That instinct is the whole lesson, formalised.

### The sub-concepts

**Masking.** Replace or suppress part of a value: `S1234567A` becomes `S****567A`, a phone number keeps its last four digits, a name becomes `CUSTOMER_014`. Fast, reversible only with the mapping, and good for display and testing. What it does not do is stop correlation — a masked NRIC still sits next to a birth date and a block number.

**Perturbation and generalisation.** Change values slightly, or coarsen them, so the exact figure no longer belongs to anyone in particular: age 65 becomes an age band of 60–69, `Blk 12 Bedok` becomes `Bedok`, a salary of $4,180 becomes `$4,000–4,999`. Generalisation is usually the more defensible move in a governance argument, because it is easy to explain: you are not distorting the truth, you are lowering the resolution.

**Pseudonymisation.** Replace direct identifiers with a key or code — `Mdm Tan` becomes `subject_0421` — and hold the key separately under access control. This is the workhorse for AI training and for analyst handoffs, and it is the technique most often confused with anonymisation. It is **reversible** by design; that is its point. Under the PDPA, pseudonymised data is still personal data, because someone in your organisation can re-link it.

**Anonymisation proper.** Irreversible in practice: re-identification is not reasonably practicable by anyone, including you, given the data and the means available. This is a high bar and it is why regulators speak of "anonymised" cautiously. The honest classroom position: most internal datasets are pseudonymised, not anonymised, and the paperwork should say so.

**Aggregation and differential privacy.** At one end, publish only counts and averages, never rows. At the other, inject calibrated statistical noise so that no individual's presence in the dataset can be inferred from any output — the technique behind differential privacy. The trade-off is always the same: more privacy protection, less precision in the answer. The distillation's principle here is data minimisation — collect and send the least that does the job, because data you never held cannot leak.

**Redaction before the prompt.** For GenAI work the practical technique is a pre-inference scrub: regex and named-entity recognition models that catch NRIC numbers, phone numbers, card numbers and names, and mask them before anything leaves your machine. This is a control, not a policy, and it fails in the same way spell-check fails — silently on the unusual case.

### How it connects to the rest of the framework

`TSC8-Basic-K1` supplies the privacy principle this bullet operationalises; `TSC8-Basic-K2` frames why the data leaves your perimeter at all; `TSC8-Basic-A5` is the ability version — applying anonymisation, encryption and access control as a routine. `TSC8-Basic-A3` uses de-identification as a vendor comparison criterion, since a provider's retention and training terms change how much anonymisation you need. On the model side, `TSC1-Basic-K06` explains the failure mode this defends against: a model can memorise and later reproduce verbatim sequences it was trained on.

### What is current as of November 2026

Two shifts matter.

First, the tools moved from add-ons to defaults. Enterprise tiers of the major assistants — the paid organisational products around GPT-6 generation models, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — increasingly offer automatic PII detection and redaction in the upload path, along with retention controls. That is good and it is not sufficient: a redactor that catches NRICs still misses the combination problem, and it does nothing about data you paste into a personal account.

Second, the regulatory conversation has shifted from "is it anonymous" to "can you show your work". PDPC guidance expects organisations to document how personal data is used in AI decision systems, which means the practical deliverable is no longer a claim but a record: what was removed, what was generalised, what key exists, who holds it, and when it was destroyed. Model and system cards are the vendor-side version of the same discipline.

### Common misconceptions

- *"We removed the names, so it's anonymous."* Postcode, age, block and condition usually re-identify. In a small dataset, two fields are often enough.
- *"Pseudonymisation is anonymisation."* Pseudonymised data can be re-linked and remains personal data in law.
- *"Anonymising once is enough forever."* Re-identification gets easier as other datasets appear. A 2019 "anonymous" file can become identifiable against a 2026 one.
- *"We only share it internally, so the standard is lower."* Internal circulation is where most leaks happen, and PDPA obligations do not stop at the firewall.
- *"The AI tool does the anonymising for me."* Only if you configured it to, and only for the patterns it knows.

## How a student should understand it

**Mental model:** the school photo with the faces blurred. You have not anonymised the class if the caption still says "Pri 6A, 2019, Bedok", the class has 32 pupils, and one of them was the only girl with crutches. Blurring helps; context identifies.

**Things they can do after this bullet:**
1. Take a customer record and say which fields must change, not just the name.
2. Tell a colleague, correctly, why pseudonymised data still counts as personal data.
3. Choose between masking, generalising and aggregating for a stated purpose — and say what precision they gave up.

**Misconceptions to kill:** that name removal is anonymisation; that pseudonymisation is irreversible; that the technique matters more than the combination of fields left standing.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The void deck poster.** A notice that says "Resident of Block 12, 3-room flat, recently discharged from hospital, please collect parcel" identifies one household without naming anyone. Where it breaks: a void deck audience is small and local, so the analogy *understates* the risk online, where the audience is everyone and the linking data is free.

**The primary school class photo.** As above. Where it breaks: photo blurring is visually obvious, so people trust it; field-level de-identification is invisible, so people over-trust it.

### Worked example with a real tool

The exercise teaches the right sequence — redact locally, then use the tool, never the other way round.

```
Here is an invented customer record used for training:
"Mdm Tan, 65, diabetic, Blk 12 Bedok, S1234567A, outstanding $4,180."

1. Which fields are direct identifiers, which are quasi-identifiers,
   and which is sensitive health data?
2. Rewrite it three ways: (a) masked, (b) generalised, (c) pseudonymised.
   State what each version would still let someone infer.
3. For a pricing study by an external analyst, which version would you
   send, and what would you write in the data-sharing note?
```

What to point at afterwards: the model will do (a) and (c) well and often under-do (b) — it generalises the age but leaves the block. Then ask the room the harder question: even fully generalised, does "Bedok, 60s, diabetic" identify anyone in a dataset of 40 people? That is the moment the combination idea lands.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out an "anonymous" survey comment from a real-sounding workplace and ask who wrote it. The room usually knows.
2. **State the objective** — by the end you can take a record, de-identify it three ways, and justify which version leaves the building.
3. **Recall prior learning** — PDPA consent and purpose limitation from `TSC8-Basic-K2`.
4. **Present the content** — masking, perturbation/generalisation, pseudonymisation, anonymisation, aggregation, pre-prompt redaction.
5. **Guide** — work the Mdm Tan record together, including the "what could still be inferred" column.
6. **Elicit performance** — pairs de-identify a record from their own workplace (invented details) and write the one-line data-sharing note.
7. **Give feedback** — the two errors to catch: leaving quasi-identifiers intact, and calling pseudonymised data anonymous.
8. **Transfer** — each learner names one dataset they currently share and the change they will make.

## What the framework doesn't mention but trainers need to know

- **The bar is "reasonably practicable", not "impossible".** Teach the standard as a judgement about effort and available data, not a technical guarantee. No honest trainer promises irreversibility.
- **Utility is the negotiation.** Every generalisation costs an analysis. Ask what decision the data supports, then remove precision the decision does not need — that argument wins rooms where "privacy" alone does not.
- **Small datasets cannot be anonymised, only aggregated or not shared.** A 30-row customer list with a handful of attributes is effectively a list of people.
- **The mapping table is the crown jewel.** Pseudonymisation is only as strong as the access control on the key. Ask who holds it and whether access is logged.

## Watch out

- **Do not claim a dataset is anonymous.** Say "de-identified" and specify the technique; overclaiming is how organisations end up defending a statement they cannot support.
- **Do not demo with real records, even "just to show the tool".** Use invented data and say so out loud.
- **Do not teach anonymisation as a one-time step.** It is a property of a dataset against a threat model that keeps changing.
- **The stale claim to retire:** "delete the name column and it's safe." That belief is the single most common cause of avoidable PDPA exposure in Singapore organisations.
