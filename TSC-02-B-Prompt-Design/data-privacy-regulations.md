---
id: 02.01.B.K6
tsc: 2
level: Basic
code: K6
title: Data privacy regulations
as_at: 2026-11-26
review_by: 2027-02-25
---

# Data privacy regulations

> **TSC #2 Prompt Design · Basic · Knowledge K6**

> **Framework text (verbatim):** "Overview of data privacy regulations."
>
> **TSC #2** Prompt Design · **Basic** · Knowledge · Bullet 6 of 15

**One-line version:** Before you paste, ask three questions — whose data is it, does the person know why, and does my organisation allow this tool to see it?

## What it is

Singapore's Personal Data Protection Act (PDPA) sets a baseline for how organisations handle personal data: information about a person who can be identified from it, alone or together with other information the organisation has or is likely to have. In outline, organisations must tell people why their data is collected, used or shared, obtain consent unless an exception applies, use it only for reasonable purposes, and protect it. A prompt is an instruction to an AI tool; using real personal data in one is a decision with legal and organisational consequences, not a technical convenience.

## Deep expansion

### The concept

The framework asks for an overview, not a legal opinion. The trainer's job is to install two habits and one boundary.

The first habit is **reading a record for identifiability rather than for names**. A row with no name can still point at one person: the exact job title, the postal code, the unusual combination of a rare complaint and a date. The PDPA's definition turns on identification from the data plus other information the organisation has or is likely to have — which is why "I removed the names" is the beginning of the question, not the end of it.

The second habit is **separating three different permissions** that learners collapse into one:

- **Notice and consent** under the law — was the person told the purpose, and did they agree to it, or does an exception apply?
- **Purpose** — is using an external AI service for this data a reasonable use of what was collected? Data given for appointment reminders is not automatically data given for drafting practice.
- **Organisation approval** — does your workplace allow this tool, for this data, with these safeguards? This is a policy question that exists on top of the law, and it is frequently stricter.

The boundary is **scope**: a trainer can explain the baseline and the questions to ask; only the organisation's data protection officer (DPO) or a legal adviser can decide a real case. Say that out loud, early. It protects the learner from acting on a classroom summary and it protects the course from overclaiming.

### The sub-concepts

**Personal data is broader than it looks.** Names and phone numbers are obvious. Job titles, postal codes, plate numbers, voice recordings and free-text case notes can all be personal data when they can be linked to a person.

**Anonymisation is a standard, not an action.** Removing direct identifiers is a step. Whether the result is genuinely anonymous depends on what else is available — which is why `TSC2-Basic-A3` treats masking, perturbation and pseudonymisation as risk reduction, not as a guarantee.

**Deleting a name is the classic half-measure.** Records without names but with exact roles and locations are routinely re-identifiable by someone who knows the workplace.

**The tool is a third party.** Pasting into a chat product moves data outside your organisation's systems. Whether that is allowed, and under what safeguards, is a decision someone above the learner's pay grade has usually already made — or should have.

### How it connects to the rest of the framework

`TSC2-Basic-A3` is the practical anonymisation skill this bullet motivates; `TSC2-Basic-K4` is the output-side counterpart (guardrails on what comes back); `TSC2-Basic-A7` covers prompt misuses, including the privacy ones. The same ground appears at `TSC1-Basic-K8` (PDPA fundamentals) and at Intermediate level in `TSC8-Intermediate-K5`.

### What is current as of November 2026

The PDPC's guidance on generative AI has settled the shape of the conversation: organisations are expected to have written policies on AI use, to assess purpose and consent, and to apply safeguards proportional to the risk — rather than to treat "it's a chatbot" as either automatically permitted or automatically forbidden. The practical effect for trainers is that most Singapore workplaces now have *some* rule, even if it is only an email from IT. Two things to check before each course run: whether the organisation permits any external AI tool at all, and whether the permitted tool has a setting that stops conversations being used for training. The frontier models of late 2026 — GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — differ in their enterprise data-handling terms, so "which tool" is a privacy question as well as a capability one.

### Common misconceptions

- *"If there's no name, it's not personal data."* Identification can come from combination. That is exactly what the definition covers.
- *"Customers agreed to reminders, so we can use their data for anything."* Purpose limitation says otherwise.
- *"The AI said the checklist complies."* The model produced a plausible document. Compliance is a human and organisational determination.
- *"Our DPO approved ChatGPT, so all data is fine."* Approval usually has conditions — which data, which tool, which settings.

## How a student should understand it

**Mental model:** handing a file to a contractor. You would ask who they are, whether they are allowed in the building, what they will do with it, and whether anyone signed off. Pasting into a chatbot is the same transaction with less ceremony — which is precisely the danger.

**Things they can do after this bullet:**
1. Explain personal data as identifiable-in-context, not name-based.
2. Separate legal consent, purpose, and workplace approval in a real request.
3. Name the next step before pasting: check policy, ask the DPO, or strip the data.

**Misconceptions to kill:** that names are the test; that one consent covers all uses; that the model's answer is a legal determination.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The polyclinic queue card.** A queue number with no name feels anonymous — until the card also shows "follow-up for the rare allergy" and the clinic is in a small estate. Where it breaks: a clinic has formal controls over who sees the card; a chat window has whatever controls the provider's terms give you, which the learner usually has not read.

### Worked example with a real tool

Paste this into a chat, with every detail invented:

```text
You are helping a Singapore workplace prepare a privacy checklist. All people, workplaces and situations below are fictional; no real customer details are supplied.

Use these teaching points:
- Singapore's Personal Data Protection Act (PDPA) gives a baseline standard for organisations' handling of personal data: information about a person identifiable from the data alone or with other information the organisation has or is likely to have access to.
- Organisations generally must notify individuals of purposes and obtain consent for collection, use or disclosure, unless an exception applies; purposes must be reasonable. They must use reasonable security arrangements.
- Removing a name alone does not ensure anonymity; remaining details combined with other information may identify someone.

Fictional workplace policy: A worker may use the external chat AI for generic text without customer data. For actual customer data, the worker must first obtain approval from the data protection officer (DPO) and check the relevant permissions and safeguards. This is a made-up workplace rule, not a claim that the PDPA always requires this approval.

Consider these hypothetical requests:
A. Draft a generic appointment reminder, with no customer data.
B. Paste customer names and phone numbers from an appointment list into the chat AI. Customers agreed to receive appointment reminders, but there is no approval for this AI use.
C. Paste customer records without names, but with exact job titles and postal codes. Other information available to the organisation could identify those customers. There is no approval for this AI use.

Create a three-row checklist, one row per case, with a decision to proceed or pause, a short reason, and a next step. Distinguish consent or an applicable exception under the law from the fictional workplace approval. End with one sentence saying this is general information, not a legal determination. Do not invent or ask for any customer records.
```

What to point at afterwards: A proceeds; B and C pause, for different reasons — B because the reminder consent does not settle the purpose or the approval, C because removing names did not remove identifiability. Then read the model's final sentence aloud. It is the sentence that keeps the exercise honest, and it is the one learners skip.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If a customer record has no name, why might it still need care before it goes into a chat AI?" Take suggestions; do not ask for real examples.
2. **State the objective** — by the end you can name the three permissions and the next step for each case.
3. **Recall prior learning** — the identifiability idea from `TSC2-Basic-A3`, if already taught, or the general notion of personal data.
4. **Present the content** — the PDPA baseline in five sentences, then notice, consent, purpose, safeguards, approval.
5. **Guide** — work case A together, then B as a class, then let pairs reason C.
6. **Elicit performance** — pairs run the checklist prompt and compare it with their own three decisions.
7. **Give feedback** — debrief why B and C pause, and correct any answer that treats approval as a legal requirement.
8. **Transfer** — each learner names the person or policy they would consult in their own workplace.

## What the framework doesn't mention but trainers need to know

- **Most learners have never seen their organisation's AI policy.** Ask them to find it after the course; that single task does more than any slide.
- **The DPO is often one busy person.** Teach the learner to arrive with a specific question — which data, which tool, which purpose — not "is AI allowed".
- **Training-data settings change.** A tool permitted last quarter may have changed its defaults; the trainer should not state a provider's current terms from memory.
- **Privacy and usefulness pull in opposite directions.** Over-masking produces data too vague to be useful; the skill is keeping the analytical value while removing identity, and saying honestly what was lost.

## Watch out

- **Do not give legal advice.** "This is general information, check with your DPO" is not a disclaimer to mumble; it is part of the lesson.
- **Do not demo with real customer data, ever.** Not "anonymised" exports, not a screenshot with names blurred imperfectly.
- **Do not imply a tool is safe because it is popular.** Popularity is not a data-processing agreement.
- **The stale claim to retire:** "just remove the names and it's anonymous." In November 2026 that claim is the most common privacy error in Singapore classrooms, and it is wrong for a reason learners can understand.
