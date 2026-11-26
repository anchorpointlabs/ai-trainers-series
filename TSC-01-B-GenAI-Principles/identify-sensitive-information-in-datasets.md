---
id: 01.01.B.A3
tsc: 1
level: Basic
code: A3
title: Identify sensitive information in datasets
---

# Identify sensitive information in datasets

> **TSC #1 Generative AI Principles and Applications · Basic · Ability A3**

> **Framework text (verbatim):** "Identify sensitive information in datasets."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Ability · Bullet 11 of 13

**One-line version:** A dataset rarely has one sensitive column — it has six innocuous columns that, together, name a person, so the scan is a combination test, not a search for "NRIC".

## What it is

This is the ability that must happen before any other data skill: given a file, a folder or an export, find everything that identifies, exposes or embarrasses a person or an organisation. Sensitive information means **personal data** (identifiers, contact, health, financial, employment, anything about a minor) plus **confidential data** (trade secrets, pricing, client lists, unpublished plans). You cannot protect what you have not spotted, and this bullet is the spotting.

## Deep expansion

### The concept

Trainers teach this as "find the NRIC column", and learners pass the exercise and then fail in the office, because the NRIC column is the only easy part of the problem. The real work is a two-part scan: first **what is in the file**, then **what the file points at**.

Three categories of field, because they need different treatment:

- **Direct identifiers.** Name, NRIC/FIN, passport, phone, email, home address, employee number, account number, date of birth, photograph, voice recording.
- **Quasi-identifiers.** Age, sex, postal code, block number, occupation, department, salary band, date of visit, school. Harmless alone, identifying in combination — and this is where almost all real re-identification happens.
- **Sensitive attributes.** Health, disability, religion, financial position, union membership, disciplinary records, immigration status, anything about a person under 18.

Anonymisation, in `TSC1-Basic-A04`, works by removing the first, generalising the second, and being careful what the third is attached to. This bullet is the step before: knowing which is which in *this* file.

Then the part that separates competence from compliance: **the dataset is not the spreadsheet**. Sensitive information lives in free-text fields, attachment filenames, image content, headers and footers, comments, tracked changes and file metadata. A file with every column masked and one complaint paragraph — "the driver Mr Lim on the Bukit Panjang school bus shouted at my son" — is fully identifiable. That paragraph is the real risk, and no column scan will find it.

### The sub-concepts

**The noticeboard test.** If you would not pin it by the lift, treat it as sensitive. Crude, memorable, and it correctly flags things that feel harmless: a staff photo, a list of who attended a wellness screening, a salary band next to a job title. It is a floor, not a ceiling — an AI tool sees more people, from further away, for longer.

**Combination, not individual fields.** Pick a row and ask: with this row plus Google, could I name the person? A 45-year-old female finance manager at a 30-person firm in a specific block is one of one. Age band plus department plus suburb is usually enough in small populations — which is why Singapore's SME-heavy economy makes this worse than learners expect.

**Personal versus confidential.** Personal data is about an individual, protected by PDPA (`TSC1-Basic-K8`). Confidential data is about the organisation: cost sheets, unpublished pricing, client lists, tender responses, litigation material. The tests differ — PDPA does not apply to a margin sheet — but the handling rule in an AI tool is the same: it does not go in unless the terms and the purpose allow it.

**Where it hides, in the order people miss it.** Free-text fields; filenames ("TanAhMoi_MedicalReport.pdf"); screenshots and scanned PDFs pasted into a chat; headers and footers on an exported template; spreadsheet comments and hidden columns; tracked changes and document properties; images of faces, lanyards, name plates and whiteboards; and the combination of six fields that each pass on their own.

**Small-n is the amplifier.** A forty-person department is effectively unique at row level. The smaller the dataset, the more each remaining field identifies — the opposite of the intuition learners bring. Where the population is tiny, aggregation is often the only honest answer.

**The decision, which is the output of the scan.** Four options the learner should be able to defend: **use as is** (no personal data, or the terms cover it); **clean then use** (strip direct identifiers, generalise quasi-identifiers, rewrite free text); **aggregate** (counts and bands, no rows); **do not use** (the purpose does not justify the exposure).

**Consistency is not safety.** A masked field that stays the same across rows is a pseudonym. If every record for a customer shows the same masked string, the pattern survives even though the name does not. This is the commonest technical error in the area and it belongs here as a spotting skill.

### How it connects to the rest of the framework

`TSC1-Basic-K8` is the legal frame — consent, purpose, protection. `TSC1-Basic-A04` is the mitigation toolkit this scan feeds. `TSC1-Basic-A05` asks the governance question afterwards: was cleaning enough, given who is affected? At Intermediate the same scan becomes a data-handling procedure with an owner and a record.

### What is current as of November 2026

- **Models made re-identification cheap.** An LLM will join a job title, a project name and a block number and suggest who is meant, quickly and fluently. A dataset that resisted linkage in 2020 may not resist it now, because the linking tool is free.
- **The leak moved to free text and attachments.** As column-level tooling matured, most real incidents moved to the parts no tool reads: a pasted PDF, a screenshot, a complaint paragraph, a filename.
- **Enterprise terms change the risk, not the obligation.** Regional processing and zero-retention options reduce exposure and do not convert personal data into anonymous data. The scan still has to happen.
- **Agentic tools widened the surface.** A system that reads a shared drive and writes to a chat now scans, copies and transmits on its own. The scan must cover what the agent can reach, not only what the user attached.

### Common misconceptions

- *"I removed the name, so it's anonymous."* Name removal addresses one direct identifier and leaves every quasi-identifier in place.
- *"Only NRIC and phone numbers count."* An email address alone is personal data. So is a photo, a voice note, and a block number with a job title.
- *"Our dataset is too small to matter."* Small datasets are the easiest to re-identify.
- *"It's internal, so it isn't sensitive."* Internal HR and disciplinary files are the highest-risk data most organisations hold.
- *"The tool masks it automatically."* Pattern-matching finds formats. It does not read a paragraph and notice that a person is being described.

## How a student should understand it

**Mental model:** a record points at a person through the *combination* of what it contains. Your job is to find the combination, not the name.

**Things they can do after this bullet:**
1. Sort a column list into direct identifiers, quasi-identifiers and sensitive attributes without help.
2. Run the combination test on one row of a real file and say whether it points at a person.
3. Pick one of the four decisions and give a reason that survives a challenge.

**Misconceptions to kill:** that removing names is enough, that small datasets are safe, and that masking one column is anonymisation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic queue screen.** "Queue 07 — Dr Tan — 2:15pm." No name anywhere, and everyone in a twelve-person waiting room knows exactly who that is. That is a quasi-identifier attack in one sentence, and it is why "we removed the name" is not an answer.

**The blurred office photo with the lanyard.** You blur every face and post the photo. The lanyard, the desk nameplate and the window view still say who sits where. Masking one feature and calling the picture anonymous is the same mistake, at the level of the whole file.

### Worked example with a real tool

Project one row and run the scan as a class:

```text
Customer 412 — Mdm Tan, NRIC S1234567A, 65-year-old diabetic, lives at
Blk 12 Bedok, tel 91234567, email tan.ml@example.com, visited 3 Nov,
complained that "the driver Mr Lim on the Bedok Green school bus
shouted at my grandson".
```

Then the prompt, to make the categories explicit:

```text
For the record below, list every item of sensitive information and classify
each as: direct identifier, quasi-identifier, or sensitive attribute. Then
tell me which items in combination could identify this person, and what you
would remove, generalise or rewrite before this record could be analysed by
an AI tool.

<record pasted here>
```

What to point at afterwards: the model finds the name, NRIC, condition and address, and usually misses or under-ranks the **free-text driver reference** — the most identifying item in the record, because it names a third party, a school and a route. Second lesson: it will call a masked NRIC "anonymised" unless pushed, which is the misconception to correct in real time. Close by asking which of the four decisions they would take for a 60-row file like this: the honest answer is usually *clean, then aggregate*.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — Show the clinic queue screen. Ask who is in room 3. Let them answer, then explain why they could.
2. **State the objective** — "You will scan a real file and produce a list of what has to come out, what can be generalised, and what stops you using it."
3. **Recall prior learning** — From K8: consent, purpose, protection. Now: what exactly are we protecting?
4. **Present the content** — Three categories, then the four decisions. One slide each, no more.
5. **Guide** — Run the record scan, then the prompt, then correct the "anonymised" claim.
6. **Elicit performance** — Teams get a 12-row file (names removed, everything else intact) and must produce the clean / aggregate / do-not-use verdict with reasons.
7. **Give feedback** — Debrief the free-text field and the small-n problem. Those are the two that split rooms.
8. **Transfer** — Each learner names one dataset they handle monthly and which decision it should get.

## What the framework doesn't mention but trainers need to know

- **The free-text field is the whole job.** Comments, case notes, email bodies and chat transcripts carry identifiers no column tool sees. Budget classroom time accordingly.
- **Filenames and headers leak.** `TanAhMoi_Medical_Oct.pdf` inside a "cleaned" folder is a disclosure waiting for a forward.
- **Images are data.** A photo of a whiteboard, a lanyard or a screen carries names and figures. Trainers who scan only text miss half the files in a real office.
- **Confidential data has no regulator and more consequence.** A leaked client list ends a relationship; a leaked cost sheet ends a tender.
- **The scan needs a record.** "We checked" is not an audit trail. One line per dataset — what was found, what was done, who decided — is enough.

## Watch out

- **Do not teach this as a search for NRIC.** The exercise passes and the skill fails. Use a file with no NRIC in it and watch the room struggle — that is the lesson.
- **Do not let "anonymised" pass unchallenged.** Ask whether the same value repeats across rows. If it does, it is a pseudonym.
- **Do not skip the confidential half.** Personal data gets the attention; commercial data is what most SMEs actually lose.
- **The stale claim to retire:** "small samples are safe because there are fewer people to identify." Fewer people means each row is more unique. Say it twice.
