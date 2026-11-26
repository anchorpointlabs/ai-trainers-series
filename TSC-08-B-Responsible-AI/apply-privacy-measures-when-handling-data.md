---
id: 08.01.B.A5
tsc: 8
level: Basic
code: A5
title: Apply privacy measures when handling data
as_at: 2026-11-26
review_by: 2027-02-25
---

# Apply privacy measures when handling data

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Ability A5**

> **Framework text (verbatim):** "Apply privacy measures when handling data for AI applications (e.g., implement simple data anonymisation and de-identification techniques, secure data storage using basic encryption)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Ability · Bullet 9 of 10

**One-line version:** Privacy is a routine, not a project — minimise what you hold, reduce what you send, lock what you store, and know who can open it.

## What it is

This ability is the practical enforcement of privacy at the desk: anonymise or de-identify before sharing, restrict access to people who need it, encrypt data at rest and in transit, keep it only as long as needed, and use tools whose contracts match those commitments. The measure is whether these happen every time, not whether they happen once under supervision.

## Deep expansion

### The concept

Privacy failures are rarely dramatic. They look like an analyst emailing a full customer export because it was easier than a filtered view, a shared drive with open permissions left from a project that ended, a spreadsheet of NRICs sitting unencrypted on a laptop that goes to a coffee shop.

The unifying idea is **least exposure at every step**: the least data collected, the least copied, the least shared, the least retained, the fewest people able to open it. Each "least" is a decision someone makes, and in most organisations that someone is the person doing the task, not the DPO.

The generative AI twist is that a new exposure point appeared in the middle of the workflow. Data now leaves your perimeter into an inference endpoint on its way to doing the work. That means privacy measures have to be applied *before* the prompt, not only at storage.

### The sub-concepts

**Minimisation before collection.** Ask what the task actually needs. A pricing study does not need names; a service recovery call does not need an NRIC. The strongest privacy measure is not collecting the field, because data you never held cannot leak.

**De-identification before sharing.** Apply `TSC8-Basic-K3` here as a step in the workflow: remove direct identifiers, generalise quasi-identifiers, pseudonymise where re-linkage is needed, and aggregate when only counts are required. For internal analysis, the practical default is pseudonymise plus generalise, and record what was done.

**Redaction before the prompt.** Regex and named-entity recognition filters catch NRIC numbers, phone numbers, card numbers and names before text goes to an external model. This is a control you configure, not a habit you trust. Test it with your own formats — a filter tuned for American phone numbers will miss a local mobile number.

**Access control.** Role-based permissions, and for retrieval systems, permissions enforced at the document level so a query cannot surface a file the user could not open directly. The test: ask a junior staff member to search the internal assistant for "salary" and see what returns.

**Encryption and secure storage.** Encryption at rest protects a stolen disk; encryption in transit protects the wire. Neither protects against a person with legitimate access copying data out, which is why encryption is one layer and not the answer. Basic learners need the one-line version and the reason, not the key management.

**Retention and deletion.** Data kept "just in case" is liability with no upside. Set a retention period per dataset, actually delete at the end, and include the mapping key for pseudonymised data — an orphan key table is a common, quiet failure.

**Vendor terms as a privacy measure.** Zero-retention, no-training-on-your-data and a data-processing agreement are technical controls expressed as contract. Choosing a tool without them is choosing to skip the measure.

**Detection and response.** Data-loss prevention and cloud-access-security monitoring catch the paste into a personal account and the bulk upload to an unsanctioned service. And if a breach occurs, Singapore requires notification to the PDPC within three calendar days of assessing a notifiable breach — which means someone must be able to tell, quickly, what data was involved. Learners should know that a breach they cannot scope is a breach they cannot report correctly.

### How it connects to the rest of the framework

`TSC8-Basic-K2` explains why the three checks exist; `TSC8-Basic-K3` gives the techniques this bullet applies as steps. `TSC8-Basic-A4` writes the requirement into the team's guideline, and `TSC8-Basic-A3` selects tools whose terms make the measures possible. `TSC8-Basic-A6` closes the loop on output: privacy applied on the way in does not verify what comes back out.

### What is current as of November 2026

Enterprise tiers of the major assistants — the organisational products around OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — now typically ship retention controls, admin audit logs and in-product PII detection, which moves several of these measures from "user discipline" to "configuration". Trainers should show the settings, not just describe them.

The other shift is enforcement posture: PDPC guidance on AI recommendation and decision systems expects documented data lineage and a lawful basis, so the practical artefact is a record of what was used, why, and what protections applied. Organisations that can produce that record fare very differently from those that cannot.

### Common misconceptions

- *"It's internal, so privacy doesn't apply."* Most incidents are internal circulation, and the PDPA does not stop at the firewall.
- *"Encryption solves it."* Encryption protects against theft of storage, not against authorised misuse.
- *"The DPO handles privacy."* The DPO sets the standard; the person handling the data applies it.
- *"If we delete the file, it's deleted."* Backups, sync folders, email attachments and model logs all keep copies.
- *"Anonymised data is out of scope."* Only where re-identification is not reasonably practicable — see `TSC8-Basic-K3`.

## How a student should understand it

**Mental model:** the polyclinic counter. Patient files are not left on the front desk; they are behind the counter, accessed by staff who need them, logged, and returned. Nobody thinks this is bureaucracy — it is how the clinic works. Privacy measures are the same posture applied to data.

**Things they can do after this bullet:**
1. Apply a four-step pre-send routine — minimise, de-identify, check the tool, restrict the recipients — to any dataset.
2. Explain in one sentence why encryption does not prevent an insider copying data.
3. Name the retention period and deletion owner for a dataset they handle.

**Misconceptions to kill:** that internal means safe; that encryption is sufficient; that deleting the file deletes the data.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic counter.** As above. Where it breaks: clinic access is physical and visible; digital access leaves no trace unless logging is switched on.

**The office key cabinet.** Only the facilities lead holds the master key, the register records every issue, and keys come back at the end of the shift. Access control is a register, not a promise. Where it breaks: digital permissions are copied, inherited and forgotten far more easily than physical keys.

### Worked example with a real tool

Build the checklist before the handoff:

```
I need to hand a customer dataset to an external analyst for a pricing
study. Data currently includes: name, NRIC, mobile, email, address,
date of birth, plan type, monthly spend, complaint notes.

Act as our data protection officer and produce:
1. A field-by-field table: keep / generalise / remove, with the reason.
2. The minimum dataset that still supports a pricing study, and what
   precision we lose.
3. A five-line pre-send checklist covering access, encryption, retention
   and the recipient's obligations.
4. Two questions I must answer before sending, that no checklist can.
```

What to point at afterwards: the model is good at the field table and bad at question 4 — it will not know your contractual obligation to the customer or whether the analyst is a sub-processor. Those two questions are the ones a person must answer, and they are usually the ones that stop the transfer.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "A laptop with a customer spreadsheet was left in a Grab. What is the first question your DPO asks?" Answer: what was on it, and was it encrypted.
2. **State the objective** — apply a four-step routine to a real dataset and produce a pre-send checklist.
3. **Recall prior learning** — `TSC8-Basic-K3`'s techniques; today they become steps in a workflow.
4. **Present the content** — minimise, de-identify, redact, access control, encryption, retention, vendor terms, detection, notification.
5. **Guide** — build the field table and checklist together for the analyst handoff.
6. **Elicit performance** — each pair applies the routine to a dataset from their own work (invented details) and presents one surprise.
7. **Give feedback** — catch the three recurring errors: retaining NRIC "for matching", leaving the mapping key with the data, and no stated deletion date.
8. **Transfer** — each learner names one dataset they will minimise this month and who must approve it.

## What the framework doesn't mention but trainers need to know

- **The mapping key is the weak point.** Pseudonymisation with the key in the same folder is decoration. Ask who holds it and whether access is logged.
- **Backups and sync folders defeat deletion.** Teach the full set: primary store, backups, email attachments, shared drives, tool logs.
- **Breach response is a time problem.** Three calendar days to notify the PDPC after assessing a notifiable breach means you must be able to scope the data in hours. That capability is built before the incident.
- **Configuration beats training for PII redaction.** If the tool can redact automatically, switch it on; do not rely on people remembering.
- **Small teams still need a named owner.** "Everyone is responsible" means nobody checks the permissions quarterly.

## Watch out

- **Do not demo with real records.** Invented data, stated as invented, every time.
- **Do not teach encryption as a silver bullet.** Say what it protects against and what it does not.
- **Do not overclaim anonymisation.** "De-identified using these techniques" is defensible; "anonymous" usually is not.
- **The stale claim to retire:** "privacy is a compliance team task." The exposures happen at the desk, in the paste and the forward.
