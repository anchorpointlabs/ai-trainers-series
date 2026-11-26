---
id: 01.01.B.K8
tsc: 1
level: Basic
code: K8
title: Data privacy and the PDPA
---

# Data privacy and the PDPA

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K8**

> **Framework text (verbatim):** "Fundamentals of data privacy and protection (e.g., data privacy laws and regulations such as Personal Data Protection Act)."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 8 of 13

**One-line version:** Pasting a customer's details into a public AI tool is a disclosure of personal data to a third party — and "the tool answered helpfully" is not a lawful basis for it.

## What it is

Singapore's Personal Data Protection Act governs how organisations collect, use, disclose and retain personal data. The consequence for this course is narrow and important: before anything is typed into an AI tool, the learner has to know whether the content contains personal data, whether the tool's terms permit that use, and whether the person it belongs to has been told. Most of the leaks in the news were not hacks. They were a helpful employee pasting a spreadsheet.

## Deep expansion

### The concept

PDPA rests on a small number of obligations; a Basic room needs three. **Consent** — a lawful basis, usually consent given with notice of purpose. **Purpose limitation** — use it only for the purpose you told the person about, and disclose it only as that purpose requires. **Protection** — reasonable security, and no retention beyond the purpose. Add notification, access and correction, accuracy and transfer limitation for completeness; they are consequences of the same posture.

The GenAI twist is what happens when a learner opens a chat window. That act is a **disclosure** of whatever is in the prompt to a provider outside your control, possibly outside Singapore, whose staff may review samples, and whose consumer tiers may use inputs for training by default. If the input contains a name, NRIC, medical detail or salary, the learner has disclosed personal data without consent and without a purpose that covers it. That is the whole lesson and it fits on one slide.

The second twist: **"we don't train on your data" is not "your data is safe".** It is a statement about model training. The data is still transmitted, still logged for some period, still subject to the provider's access controls, and still a transfer if the servers are elsewhere. Enterprise terms, regional processing and zero-retention options reduce the exposure; none converts personal data into anonymous data.

### The sub-concepts

**What counts as personal data.** Data about an individual who can be identified from it, or from it and other information the organisation has or is likely to have. Two clarifications learners need. First, **an identifier does not have to be a name**: an email address alone, an employee number alone, a customer ID with a complaint attached — all personal data. A job title alone usually is not, but a job title plus department plus suburb often is. Second, **business contact information is treated differently** when used for business-to-business contact; that exception does not extend to NRIC, salary, health or performance records.

**Consent, and the part people skip.** Consent must come with notice of purpose, and it can be withdrawn. If the tool's use was never described in the privacy notice, the consent you hold does not cover it. This is the commonest gap in SME practice and it is invisible until an incident.

**Protection, retention and transfer.** Know where prompts are logged, for how long, and who can read them. Sending personal data outside Singapore carries comparable-protection obligations; a model hosted regionally is easier to defend than one hosted elsewhere, and one running on your own infrastructure removes the question.

**Breach notification.** If personal data is exposed there are obligations to assess and to notify. A pasted spreadsheet that ends up in a vendor's corpus is an incident even if nothing is published, and the assessment has to be documented.

**Deemed personal data.** NRIC and similar national identifiers get heightened treatment: generally not collected unless required, and not displayed in full. For AI work the rule is simple — strip them before upload.

**Do Not Call.** Separate from the main obligations and relevant whenever the AI drafts outbound marketing. A model that writes the campaign does not change whether the recipient may be contacted.

### How it connects to the rest of the framework

`TSC1-Basic-A03` is the detection skill — how to spot personal data in a dataset. `TSC1-Basic-A04` is the mitigation skill — masking, perturbation, pseudonymisation. `TSC1-Basic-K7` is the broader responsible-AI frame this sits inside, and `TSC1-Basic-A05` is the deployment check where privacy is one of five questions.

### What is current as of November 2026

- **Consumer tiers and enterprise terms are different products.** Free and low-cost consumer tiers commonly reserve the right to use inputs for improvement; business tiers and APIs commonly do not. The learner's question is "which tier am I on?", not "is this company trustworthy?".
- **Enterprise data-processing terms are now standard at the top of the market.** Regional processing, zero retention and customer-managed keys exist across the frontier vendors — OpenAI's GPT-6 generation, the Claude 5.5 line, and Gemini 3.1 Pro / Gemini 4 Argon. They change the risk; they do not change the obligation.
- **Re-identification got cheaper.** Models are very good at joining fragments — a job title, a project name, a block number — and inferring who is meant. A dataset that resisted linkage in 2020 may not resist it now.
- **Agentic tools widened the disclosure surface.** A tool that reads your mailbox and writes to a shared drive touches personal data at both ends, and the agentic governance framework (January 2026) assumes a privacy review has been done.
- **Private deployment is a real option.** Open-weight models can run on your own infrastructure, which is often the cleanest answer for data that cannot leave. It is a data-residency answer, not a quality answer.

### Common misconceptions

- *"It's just a draft, not a disclosure."* Transmission is the disclosure. The provider received the data when the prompt was sent.
- *"I removed the name."* The combination of the remaining fields often identifies the person. That is `TSC1-Basic-A04`, and it is why "anonymised" is a claim, not a step.
- *"We pay for the tool, so it's compliant."* You pay for a licence. Compliance is about consent, purpose, protection, retention and transfer.
- *"PDPA only applies to customers."* It applies to employees, applicants, contractors, next of kin, and anyone else whose data you hold.
- *"Public data is fair game."* A LinkedIn profile is public; processing it in bulk for an unrelated purpose is still a PDPA question, and copyright may apply too.

## How a student should understand it

**Mental model:** the office noticeboard. If you would not pin it where colleagues, cleaners and visitors can read it, do not paste it into a public AI tool. Crude, and it works.

**Things they can do after this bullet:**
1. Look at a block of text and say whether it contains personal data, and which kind.
2. State the three basics — consent, purpose, protection — and apply them to one tool they use.
3. Decide whether a specific piece of data may go into a specific tool, and what would have to change for the answer to be yes.

**Misconceptions to kill:** that a name is the only identifier, that deleting afterwards undoes the disclosure, and that a paid licence equals compliance.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Telling a stranger at the kopitiam.** You would not read out a customer's NRIC, medical history and salary to a stranger helping you draft a letter — even a helpful stranger who promises to forget. The AI tool is that stranger, with better manners and a log file.

**The office noticeboard test.** Would this go on the board by the lift? A department name and a project code, probably. A name with a diagnosis, no. Where it breaks: the board is seen by fifty colleagues, whereas a prompt may be read by reviewers in another country and retained for months. The test is a floor, not a ceiling.

### Worked example with a real tool

A prompt with everything wrong with it, then the same task cleaned:

```text
Draft a reply to this complaint, in a calm and apologetic tone:

"Hi, this is Mdm Tan Ah Moi, NRIC S1234567A. My son, who is in P5 at
Bedok Green Primary, has asthma and needs his inhaler during your
programme. The instructor on 12 Nov told him to wait. I am 65 and a
diabetic, my mobile is 91234567. Please reply to tan.ah.moi@example.com."
```

```text
Draft a reply to this complaint, in a calm and apologetic tone.

Context: parent of a P5 child with a medical condition; the child was
asked to wait during a programme session on 12 Nov; the parent is an
elderly caregiver. No names or contact details are needed for the draft.

"During the session on 12 Nov, my child, who has asthma, was told to wait
when he asked for his inhaler. I am his main caregiver and I am not
comfortable with how this was handled."
```

What to point at afterwards: the first prompt contains an NRIC, a minor's school, a health condition, an age, a phone number and an email — five categories of personal data, two sensitive, one belonging to a child. The second produces a **better** reply, because there is nothing irrelevant to distract the model. Privacy and quality point the same way, which is the argument that persuades an operations manager.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "What would you not want on the noticeboard by the lift?" Collect five answers, comment on none.
2. **State the objective** — "You will look at any prompt or file and say whether it can go into this tool, and what you would change first."
3. **Recall prior learning** — From K6: the model does not remember, and uploading is not learning. So why is privacy still an issue? Because the data left the building.
4. **Present the content** — Consent, purpose, protection. Then the three categories: direct identifiers, quasi-identifiers, sensitive attributes.
5. **Guide** — Run the two-prompt example, counting the identifiers together.
6. **Elicit performance** — Each table takes a realistic work document and marks every field that must come out before upload.
7. **Give feedback** — Debrief the misses: job title plus department, a child's school, a photo, a filename, a screenshot header.
8. **Transfer** — Each learner writes the one rule they will apply from tomorrow, in their own words.

## What the framework doesn't mention but trainers need to know

- **The tier question is the practical question.** Consumer subscription, business tier, API, self-hosted — four answers to "may I paste this?".
- **Prompt logs are a copy of the data.** Anonymising before pasting is the control; deleting afterwards is not.
- **Screenshots and attachments bypass every column-level control.** A PDF with a name in the header defeats a masking tool.
- **Metadata travels.** Author names, tracked changes, file properties and cell comments survive "cleaning".
- **Small datasets are the easiest to re-identify.** A forty-person department is effectively unique at row level; aggregation is often the only honest option.

## Watch out

- **Do not turn this into a law lecture.** Three obligations, three categories, one test. The rest is reference material.
- **Do not use "PDPA says you cannot" as a scare.** PDPA permits plenty, with consent, purpose and protection. Precision earns credibility.
- **Do not skip the employee case.** Most rooms hold more risk in HR documents than in customer records.
- **The stale claim to retire:** "we use the enterprise version, so it's fine." The tier changes retention and access. It does not change what you decided to paste.
