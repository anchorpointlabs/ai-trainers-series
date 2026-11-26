---
id: 01.01.B.A4
tsc: 1
level: Basic
code: A4
title: Masking, perturbation, pseudonymisation: three tools, three limits
as_at: 2026-11-26
review_by: 2027-02-25
---

# Masking, perturbation, pseudonymisation: three tools, three limits

> **TSC #1 Generative AI Principles and Applications · Basic · Ability A4**


> **Framework text (verbatim):** "Apply basic anonymisation techniques (e.g., data masking, perturbation, pseudonymisation)."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Ability · Bullet 12 of 13

**One-line version:** Anonymisation is not deleting the name column; it is breaking the link between a record and a person, and the link can survive in the combination of everything else you left behind.

**Note on duplication:** `TSC2-Basic-A07` carries almost exactly the same sentence. This entry covers the data-handling scale — a dataset being prepared for analysis or for a tool. That entry covers the prompting scale.

## What it is

Anonymisation is a set of techniques that reduce or remove the ability to attach a record to a specific person, while keeping the data useful. The framework names three: masking, perturbation and pseudonymisation. They sit at different points on a spectrum of identifiability, and none of them is absolute.

## Deep expansion

### The concept

Identifiability is a spectrum, not a switch. At one end sits a named individual with an NRIC number. At the other sits a statistic that describes nobody in particular. Every technique moves a record along that spectrum, and the question is never "is it anonymous?" but "how much effort would it take, with the data I have released, to point at a person?"

Three kinds of attribute matter:

- **Direct identifiers** — name, NRIC/FIN, passport number, phone, email, home address, employee number, account number.
- **Quasi-identifiers** — age, sex, postal code, occupation, department, salary band, date of visit. Harmless alone; dangerous in combination.
- **Sensitive attributes** — health, religion, union membership, financial position, disciplinary records, sexual orientation, and anything about a minor.

Anonymisation works by removing the first, generalising or perturbing the second, and being careful about what the third is attached to.

### The sub-concepts

**Data masking.** Replacing a value with a placeholder of the same shape: `S**** 1234` for a name, `XXXX123A` for an NRIC, `***@***.com` for an email. Fast, readable, and adequate when the field itself is what you must not see. It fails in two ways. First, a masked field that stays *consistent* still functions as a pseudonym — if every row for the same customer shows the same masked string, the pattern is preserved even though the identity is not. Second, masking one column while leaving eight others intact often changes nothing about identifiability.

**Pseudonymisation.** Replacing identifiers with artificial but consistent keys: `CUST-00041`, `EMP-118`. The mapping table is kept separately, under access control, so that analysis can proceed and re-identification remains possible for a legitimate purpose. This is the workhorse technique for training and analytics, and the one most often mislabelled as anonymisation. Under PDPA, pseudonymised data that can be re-linked is still personal data — the mapping table is the reason.

**Perturbation.** Changing the data slightly so that exact values no longer hold, while the aggregate pattern survives: adding noise to a salary, generalising age 34 to "30–39", reporting by band instead of by value, aggregating to counts, or the classical k-anonymity idea — ensure each record is indistinguishable from at least k−1 others on the quasi-identifiers. Perturbation buys usefulness at the cost of precision, and it is the only one of the three that addresses the combination problem directly.

Adjacent techniques worth naming in class, without teaching them in depth: tokenisation and format-preserving encryption, synthetic data generation, and differential privacy.

### How it connects to the rest of the framework

`TSC1-Basic-A03` is the identification step that must come first — you cannot protect what you have not spotted. `TSC1-Basic-K08` supplies the legal frame (PDPA obligations). `TSC2-Basic-A07` applies the same three techniques inside a prompt. `TSC1-Basic-A05` asks the governance question that follows: was anonymising enough, given who is affected?

### What is current as of November 2026

- **Re-identification got cheaper.** Large language models are extremely good at joining fragments — a job title here, a project name there, a suburb — and inferring who is meant. A dataset that resisted linkage in 2020 may not resist it now, because the linking tool is free and fluent.
- **"We don't train on your data" is not anonymisation.** It is a retention and training statement. The data is still transmitted, still logged for some period, and still subject to the provider's access controls.
- **Enterprise tiers change the risk, not the obligation.** Data-processing terms, regional processing and zero-retention options reduce exposure; they do not convert personal data into anonymous data.
- **Free text is the leak.** Comments fields, case notes, email bodies and chat transcripts contain identifiers that no column-level masking touches. In practice this is where anonymisation fails, not in the NRIC column.

### Common misconceptions

- *"I removed the name, so it's anonymous."* The classic failure. Postcode plus age plus sex re-identifies a large share of a small population.
- *"Masked means safe."* A consistent mask is a pseudonym. A mask that leaves the last four digits plus a date of birth is close to an identifier.
- *"Synthetic data is always safe."* Generated data can reproduce rare combinations from the original, especially in small datasets.
- *"Our dataset is too small to matter."* Small datasets are the easiest to re-identify, not the hardest.
- *"The vendor says it's compliant."* Compliance is about the contract and the processing; it says nothing about whether your specific release of data is safe.

## How a student should understand it

**Mental model:** a record points at a person through the *combination* of what it contains, not through any single field. Anonymising means breaking enough of the combination that the pointing stops.

**Three things they can do:**
1. Sort a column list into direct identifiers, quasi-identifiers and sensitive attributes.
2. Pick a technique by purpose — masking to display, pseudonymising to analyse, perturbing or aggregating to publish.
3. Run the combination test: "with this table plus Google, could I name row 7?"

**Misconceptions to kill:** that removing names is enough, that masking equals anonymising, and that small samples are inherently safe.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic queue.** The board shows "Queue 07 — Dr Tan — 2:15pm". No name anywhere, and yet everyone in the waiting room knows exactly who that is, because the combination is unique in a room of twelve people. That is a quasi-identifier attack, and it is why "we removed the name" is not an answer.

**The blurred photo with the lanyard.** You blur every face in the office photo and post it. The lanyard, the desk nameplate and the window view still say who sits where. Masking one feature and calling the picture anonymous is the same mistake.

### Worked example with a real tool

A 60-row customer file going into a chatbot for a service-quality analysis. Three passes:

```
Pass 1 - direct identifiers
  Name              -> delete the column entirely (not mask: nothing needs it)
  NRIC              -> delete
  Email / phone     -> delete
  Customer ID       -> pseudonymise to CUST-001 ... CUST-060, mapping kept in a
                       separate file on a shared drive with access control

Pass 2 - quasi-identifiers
  Date of birth     -> generalise to age band (20s, 30s, ...)
  Postal code       -> generalise to region (West, North-East, ...)
  Exact spend       -> band ($0-50, $51-200, ...)

Pass 3 - free text (the one everybody forgets)
  Complaint text    -> read it. "My son's school bus from Bukit Panjang was late
                       again and the driver Mr Lim shouted at him" is a full
                       identification in one sentence. Either rewrite the text,
                       or keep it out of the tool.
```

What to point at: pass 3 is where most real leaks live, and it is the only pass that requires a human to read.

### Live demo or exercise

**"Name row 7."** Hand out a 12-row table with names removed but department, age band, job title, suburb and one distinctive note left in. Give the room three minutes and public search. They will identify at least one row. Then run the same table after generalisation and ask them to try again. The difference in effort is the lesson — and the fact that it took three minutes rather than zero is the honest limit of the technique.

## What the framework doesn't mention but trainers need to know

- **PDPA has no clean "anonymous data" exemption** in the way GDPR's recital language is often summarised. If re-identification is reasonably possible, treat it as personal data and let the obligations follow.
- **The mapping file is the crown jewel.** Pseudonymisation without access control on the key is decoration. Ask where the key lives.
- **Prompt logs are a copy of the data.** Whatever you paste is retained for some period under some policy. Anonymising before pasting is the control; deleting afterwards is not.
- **Screenshots and attachments bypass every column-level control.** A pasted PDF with a name in the header is a leak that no masking tool sees.
- **Metadata travels.** Author names, tracked changes, file properties and cell comments routinely survive "cleaning".
- **Small-n reality in Singapore.** A 40-person SME department is effectively unique at the row level. Aggregation is often the only honest option.

## Watch out

- **Do not teach masking as anonymisation.** They are different operations with different failure modes; conflating them is the single most common error in this bullet.
- **Do not skip the combination test.** Every class has someone who removed the NRIC column and believes the job is done.
- **Do not overstate perturbation.** Adding noise to one field while leaving eight quasi-identifiers intact protects nothing.
- **Do not imply a tool does this for you.** Data-loss tools pattern-match; they do not read a complaint paragraph and notice that "Mr Lim" plus a school plus a suburb is a person.
- **The stale claim to retire:** "we use the enterprise version, so it's fine." The tier changes retention and access. It does not change what you decided to paste.

**Related:** [Apply basic anonymisation techniques](../TSC-02-B-Prompt-Design/apply-basic-anonymisation-techniques.md) — the same skill at a different level.
