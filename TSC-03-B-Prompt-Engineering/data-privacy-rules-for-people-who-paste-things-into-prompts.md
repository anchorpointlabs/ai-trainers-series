---
id: 03.01.B.K6
tsc: 3
level: Basic
code: K6
title: Data privacy rules for people who paste things into prompts
as_at: 2026-11-26
review_by: 2027-02-25
---

# Data privacy rules for people who paste things into prompts

> **TSC #3 Prompt Engineering · Basic · Knowledge K6**


> **Framework text (verbatim):** "Overview of data privacy regulations."
>
> **TSC #3** Prompt Engineering · **Basic** · Knowledge · Bullet 6 of 15

**One-line version:** A prompt is a disclosure to a third party — so the privacy question is not "is this allowed" but "what did I just send, to whom, for how long, and under which terms".

## What it is

Data privacy law governs how organisations may collect, use, disclose and retain information about identifiable people. In Singapore the baseline is the Personal Data Protection Act, with sector rules layered on top for banking, healthcare and other regulated areas. For a prompt builder the law matters at one specific moment: the instant a document containing real people's details is pasted into a tool run by somebody else.

## Deep expansion

### The concept

Most privacy training is written for people who design systems. Prompt builders need a shorter, harder version, because the decision happens in three seconds at a text box and cannot be undone.

The structure of the obligation is stable across frameworks: know why you are collecting the data, use it only for that purpose, tell people what you are doing, protect it, keep it only as long as needed, and be accountable for it. The practitioner's translation of that into a prompt workflow has four questions:

1. **What is in this document?** Names, NRIC numbers, phone numbers, addresses, salary, medical details, performance comments, customer account data. Anything that identifies a person, alone or in combination.
2. **Whose is it?** Your own organisation's data has an owner and a policy. A client's data may have contractual terms stricter than the law.
3. **Where does it go, and under which terms?** The provider is a separate organisation. The relevant documents are the data processing terms, the retention period, the training-use setting, and the region where processing happens. The free consumer tier and the enterprise tier are different products with different terms, and this is the single most common misunderstanding in the room.
4. **How long does it stay, and can you get it out?** A saved prompt, a project file, or a conversation history is a store. If a person asks what you hold about them, that store is in scope.

The practical discipline that follows is data classification before prompting: public, internal, personal, sensitive. Personal data does not go into a consumer tool. Sensitive data — health, financial, identity numbers — does not go into a prompt at all unless there is an approved path, and usually the right move is to reduce the data rather than to trust the tool.

### The sub-concepts

**Consent is not the whole law.** Consent is one basis among several, and even with consent the purpose limitation still applies: a customer who agreed to be contacted about a delivery has not agreed to have their complaint analysed by a model.

**Notification is a separate duty.** Telling people what you do with their data is an obligation in its own right, and "we use AI tools" is now the kind of thing that belongs in a privacy notice, not just in an internal wiki.

**The provider's terms are the operative document.** No amount of careful prompting fixes a tool whose terms allow the operator to use your inputs for model improvement. Read the two settings that matter — training use and retention — before the first paste, not after.

**Retention cuts both ways.** Keeping prompts "for audit" creates a record containing personal data, with the same access and protection duties as any other record. Deleting them removes your own evidence. Decide which risk you are taking.

**Cross-border transfer.** Where the provider processes the data matters. Most Singapore organisations can rely on the transfer rules if the recipient is bound by comparable protection, but the practitioner still has to know whether the setting exists, and choose it.

**Anonymisation is a technique, not a permission slip.** Covered properly at `TSC3-Basic-A7`; the short version here is that masking names while leaving a distinctive job title, department and date is not anonymisation.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-K6` (Prompt Design); see that entry for the user-level basics of the PDPA. `TSC3-Basic-A7` is the anonymisation ability that makes this bullet operational, `TSC3-Basic-K7` covers guardrails that stop data leaving in an output, and the responsible-AI entries in TSC #8 go further into the ethics that sit above the legal minimum.

### What is current as of November 2026

The terms have become the battleground. Enterprise tiers of the major assistants now typically offer no-training commitments, configurable retention, regional processing and administrative controls, while consumer tiers continue to trade those away for free access. At the same time, saved prompts and project files have turned casual use into persistent storage — a shift that quietly moved many organisations from "we don't store customer data in AI tools" to "we store it in twelve people's accounts".

Singapore's guidance has kept pace in shape rather than in detail: the expectation is a documented purpose, a lawful basis, transparency and accountability, with the organisation — not the model provider — answerable for the use.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"If I delete the chat, the data is gone."* Deletion removes it from your view. Retention, backups and provider logs follow the provider's terms, not the delete button.
- *"The free and paid versions have the same privacy terms."* They routinely do not, and the difference is usually training use and retention.
- *"It is only a summary, so it is not personal data."* A summary of personnel files is still personal data, and often harder to correct because the detail is gone.
- *"Pseudonymised means anonymous."* If a key exists somewhere, or the combination of remaining fields points at one person, it is still personal data.

## How a student should understand it

**Mental model:** handing a photocopy of your IC across a counter. You know who you gave it to; you do not know which drawer it ends up in, or who opens the drawer next year.

**Things they can do after this bullet:**
1. Classify a document into public, internal, personal or sensitive before pasting it.
2. Find the two settings that matter in any tool: training use and retention.
3. State, in one sentence, why the free tier and the enterprise tier are not interchangeable.

**Misconceptions to kill:** that deleting the chat deletes the data; that a summary is not personal data; that a careful prompt substitutes for a lawful basis.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The IC photocopy at the gym counter.** You hand it over to prove you are a resident. It goes into a tray, then a folder, then a drawer nobody audits. The document had one purpose; the drawer has none. Where it breaks: the gym is one organisation and one jurisdiction, while a model provider is a separate company, often processing in another country under terms you clicked past.

**The office noticeboard.** Anything pinned to it is effectively public to everyone who walks past, including the cleaner, the contractor and the visitor. A prompt box feels private and behaves like the noticeboard whenever the terms allow retention. Where it breaks: the noticeboard is inside the building; the prompt box is not.

### Worked example with a real tool

Task: analyse a batch of customer complaints, some of which contain names, phone numbers and order IDs. Start with the unsafe version and let the room see it before you correct it:

```text
Here are 40 customer complaints. Summarise the top five issues and quote the
angriest customer in full so I can call them.
```

Then the practitioner version, pasted with a cleaned file:

```text
Below are 40 complaints with names, phone numbers, emails and order numbers
replaced by [CUSTOMER], [PHONE], [EMAIL], [ORDER]. Dates are kept to the month.

Summarise the top five issues, each with a count and one representative
sentence. Do not attempt to identify any customer. If a complaint is
unintelligible after masking, list it under "unclear" rather than guessing.
```

What to point at afterwards: the masking is a technique, but the *decision* was made earlier — the personal data was never sent, so the provider's retention terms stopped mattering for those fields. Then ask the room the follow-up that always lands: who is allowed to unmask, and where does the key live? If the answer is "whoever has the spreadsheet", the masking was decoration.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask how many have pasted a real customer email into a free AI tool this month. Do not ask for hands; ask for honesty in private writing.
2. **State the objective** — by the end you will classify a document, find the two settings that matter, and mask a file before prompting.
3. **Recall prior learning** — connect to the PDPA briefing they have already had, and to the DPA their organisation signs with any vendor.
4. **Present the content** — teach the four questions, the four classification tiers, and the two settings.
5. **Guide** — open a real tool's settings page together and find the training-use and retention controls.
6. **Elicit performance** — each learner takes a document from their own work, classifies it, and writes the masked version plus the prompt.
7. **Give feedback** — swap documents and try to re-identify someone from the masked version. That exercise does more than any slide.
8. **Transfer** — each learner writes the one-line rule they will apply from tomorrow, and the person they will ask when unsure.

## What the framework doesn't mention but trainers need to know

- **"Which tool is approved" is an organisational answer, not a legal one.** Teach learners to ask, and teach them that the answer changes when the tier changes.
- **Contractual confidentiality can be stricter than the law.** Client data under an NDA may prohibit third-party processing regardless of PDPA compliance. The stricter rule wins.
- **The subject access problem is real.** If someone asks what you hold about them, a saved prompt is a record. Organisations that never thought about prompt storage discover this at the worst moment.
- **Do not teach the law as a permission.** The common failure is a learner who concludes "there is no explicit prohibition, so it is fine". Purpose, notification and accountability are the tests.

## Watch out

- **Do not demo with real personal data**, not even "anonymised" real data, in a live session. Use a synthetic file.
- **Do not tell the room that one vendor is safe.** Say what to check; the products move quarterly and the terms move with them.
- **Do not let the session become a law lecture.** Fifteen minutes of law plus an hour of classification and masking beats the reverse.
- **The stale claim to retire:** "enterprise AI tools don't keep your data." Some keep it, some keep it for a defined period, some do not — and only the terms for your tier tell you which.
