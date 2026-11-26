---
id: 03.01.B.A7
tsc: 3
level: Basic
code: A7
title: Anonymising before you paste: masking that survives a second look
as_at: 2026-11-26
review_by: 2027-02-25
---

# Anonymising before you paste: masking that survives a second look

> **TSC #3 Prompt Engineering · Basic · Ability A7**


> **Framework text (verbatim):** "Apply basic anonymisation techniques (e.g., data masking, perturbation, pseudonymisation)."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 14 of 15

**One-line version:** Masking succeeds when the masked file still answers the question and nobody can work out who is in it — and the only way to know the second part is to try.

## What it is

Anonymisation techniques change data so that the people in it cannot reasonably be identified, while keeping enough structure for the work to be done. The three a Basic practitioner uses are masking (replacing part of a value), perturbation (altering values slightly) and pseudonymisation (replacing identifiers with consistent labels). Applying them means turning that into a repeatable step before any prompt, with a key, a test and a home.

## Deep expansion

### The concept

The technique is easy; the discipline is not. Most leaks in prompt work come from three mundane places, none of which is exotic: the remarks column, the filename, and the attachment.

A workable routine has five moves.

**1. Classify the fields before touching them.** Direct identifiers (name, NRIC, phone, email, address, account number), quasi-identifiers (postal code, birth month, job title, department, date of incident) and free text. The first group is mechanical. The second group is where re-identification lives. The third group is where masking usually fails.

**2. Mask by field type, not by search-and-replace.** Structured identifiers have patterns and can be handled mechanically — NRIC numbers, phone numbers, emails, account numbers. Names cannot: a find-and-replace on a name list misses the variant spelling, the nickname, the "Mdm Tan" in the remarks field, and the name inside the attached PDF.

**3. Pseudonymise consistently.** Replace each person with a stable label — CUST-001, or better, a keyed hash of the identifier — so the same person is the same label across every row. Consistency is what preserves joins and counts, and it is what most casual masking destroys.

**4. Test for reversal.** Before pasting, read the masked file as an outsider: can you name anyone? The three usual giveaways are a rare combination (department + role + month + an unusual event), a free-text field that describes a situation only one person could be in, and a numeric field left exact where the value is itself identifying.

**5. Keep the key, and decide who can open it.** A mapping file that lives next to the masked file is not a control. If the work needs re-identification later (it often does — you have to send the right reply to the right person), the key needs an owner, a location and a retention rule.

### The sub-concepts

**Masking is partial replacement.** Keep enough shape for the analysis: last three digits plus checksum letter for an NRIC, first two and last two digits for a phone number, the domain but not the local part of an email. Mask more than that and the data stops being useful for verification.

**Perturbation trades accuracy for distance.** Small jitter in amounts, dates and quantities preserves the distribution while breaking exact matching. It also breaks sums and totals, so perturbation is for exploratory work — never for a file that will be reconciled against a ledger.

**Pseudonymisation is not anonymisation.** If a key exists, the data is pseudonymised at best. That is a legitimate and often sufficient control, but calling it anonymous is how a control gets treated as a permission.

**Relative dates beat deleted dates.** Masking every date destroys trend analysis, which is usually the point of the exercise. Convert to relative ("day 12 of the case") and keep the analysis.

**Free text is the frontier.** Resumes, complaint narratives, chat transcripts, meeting notes. The identifier is rarely the name; it is the specific story. Either summarise the free text before pasting, or accept that the file cannot be treated as anonymous.

**The masked file is still a file.** It lives somewhere, is shared somehow, and outlives the task. Name it, store it, delete it on a schedule.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A3` (Prompt Design); see that entry for the user-level basics of masking, perturbation and pseudonymisation. `TSC3-Basic-K6` is the legal frame that decides when this matters at all, `TSC3-Basic-K7` is the output-side guardrail that stops identifiers reappearing in the reply, and `TSC3-Basic-A8` lists the misuse — pasting real data — that this ability exists to prevent.

### What is current as of November 2026

Two things have sharpened. Tooling has improved: several mainstream productivity tools now offer redaction before sending, and enterprise AI tiers increasingly offer data-loss-prevention controls that flag identifiers on the way in. That reduces the mechanical part of the work, not the judgement — a redaction feature will not tell you that "the only Grade 6 teacher in that department who filed a grievance in March" is one person.

The second shift is contractual. More client and vendor agreements now name AI processing explicitly, so the question is no longer only "is this personal data" but "does this agreement permit a third-party model provider at all". The stricter rule wins, and it is usually the contract, not the statute.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"I removed the name, so it is anonymous."* Names are one field. Combination and free text are the rest of the problem.
- *"Masking the NRIC is enough."* A masked NRIC plus a date of birth plus a postal code is often enough to resolve a person.
- *"Pseudonymised data is out of scope."* Not while a key exists, and not when the label is trivially linkable to a record.
- *"The tool has a redaction button, so the file is safe."* The button handles patterns. It does not handle stories.

## How a student should understand it

**Mental model:** the PSLE script with an index number instead of a name — markers can mark it, nobody can favour it, and the register that maps index numbers to candidates sits with the examinations board, not on the marker's desk.

**Things they can do after this bullet:**
1. Mask a real spreadsheet by field type and keep a consistent pseudonym key.
2. Read the masked file as an outsider and find one person from what remains.
3. Decide when to perturb, when to relativise dates, and when to summarise instead.

**Misconceptions to kill:** that names are the problem; that a key does not count; that redaction tools remove the need for a reversal test.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The exam index number.** Scripts are marked by number, the key is held centrally, and the marker cannot see a name even if they want to. The system works because the key has an owner and a register. Where it breaks: the examinations board is a single authority with a documented process, while a practitioner masking a spreadsheet is their own authority — and unless they write down where the key is, there is no register at all.

**The clinic queue ticket.** The board shows 042, not "Mr Lim, diabetes review". Everyone in the waiting room can see the number and nobody learns anything. Where it breaks: a queue number is meaningless by design and thrown away in twenty minutes, while your masked file may be kept for a year and joined to other files.

### Worked example with a real tool

Starting data, one row:

```text
Name: Tan Wei Ming   NRIC: S8XXXX67D   Phone: 9123 4567
Email: weiming.tan@example.com   Unit: Yishun 3-room   Case opened: 2026-03-04
Remarks: "Only caregiver for elderly mother, works night shift at the airport,
cannot attend weekday appointments."
```

Masked version, ready to paste:

```text
Customer: CUST-0142   NRIC: *****67D   Phone: 9XXX XX67
Email: ***@example.com   Unit: [TOWN]-[FLAT TYPE]
Case day: 12   Remarks: "Sole caregiver for an elderly dependant; works
night shift; cannot attend weekday appointments."
```

The prompt:

```text
Using only the rows below, propose three appointment slots that fit the
constraints stated in each row's remarks. Do not attempt to identify anyone.
If a row's constraints are contradictory, list it under "needs follow-up"
instead of proposing a slot.
```

What to point at afterwards: the masking kept the useful facts (caregiver, night shift) and dropped the identifying ones (name, exact unit, exact date). Then run the reversal test in front of the room: is the third row identifiable? If the estate has one three-room unit with a sole caregiver who works at the airport, it is — and that is the finding, not a failure of the exercise. The correct response is to generalise the remark ("works shifts") rather than to add more asterisks.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a masked file and ask the room to guess the person's estate and job from what is left. They usually can.
2. **State the objective** — by the end you will mask a file by field type, keep a consistent key, and run a reversal test.
3. **Recall prior learning** — ask how their organisation handles NRIC copies at a counter, and where those copies go.
4. **Present the content** — teach the five moves, then the three techniques with their limits.
5. **Guide** — mask the sample row together, arguing about the remarks field.
6. **Elicit performance** — each learner masks one page of a real document (or a supplied synthetic one) and keeps a key.
7. **Give feedback** — swap masked files and attempt re-identification. Every successful attempt produces one change to the masking rule.
8. **Transfer** — each learner writes the three-line rule they will apply before pasting, and where the key will live.

## What the framework doesn't mention but trainers need to know

- **The key is the whole control.** Masking without key custody is theatre. Ask, in every session: who can open the key, and where is it?
- **Consistency is what makes the data still useful.** Random per-row labels destroy counts and joins, and the analyst then goes back to the unmasked file — which is how the control fails.
- **Files carry metadata.** Author names, tracked changes, spreadsheet properties and file names leak identifiers that no cell masking touches.
- **Over-masking is a real failure mode.** A file masked until it says nothing gets replaced by the original "just this once". Design the masking to keep the analysis alive.

## Watch out

- **Do not demo on real personal data**, even real data you believe is harmless. Use synthetic rows that look real.
- **Do not teach anonymisation as a permission.** It is a risk reduction. If the data should not be processed at all, masking does not make it allowed.
- **Do not let the room believe asterisks are a technique.** The technique is deciding which fields carry identity, and testing.
- **The stale claim to retire:** "just delete the name column." That has never been anonymisation, and combination attacks have only got easier.
