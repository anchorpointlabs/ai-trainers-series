---
id: 04.02.I.A3
tsc: 4
level: Intermediate
code: A3
title: Compare data compliance on content storage
---

# Compare data compliance on content storage

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A3**

> **Framework text (verbatim):** "Compare data compliances on where the generated content is stored upon creation."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Ability · Bullet 8 of 11

**One-line version:** The moment a prompt leaves your network, someone else's retention policy governs it — and "the cloud is compliant" is not a clause anyone signed.

## What it is

Comparing providers on data handling means reading four things in their terms: **where** inference runs and data rests, **how long** prompts and outputs are retained, **whether** they are used for training, and **who else** touches them — sub-processors, support staff, abuse-monitoring reviewers. Then matching those answers against obligations that bind you: the Personal Data Protection Act, sector rules, and whatever your client contract says.

## Deep expansion

### The concept

Storage location is a selection criterion on the same footing as price. For a consumer chatbot, residency is an abstraction. For a bank, a hospital or any organisation handling NRIC numbers, it is the constraint that eliminates most of the market.

The comparison is not "which vendor is compliant" — no vendor is compliant in the abstract. The question is: *does this configuration of this vendor satisfy this obligation for this dataset?* The same provider can be acceptable for public marketing copy and unacceptable for claims records. Compliance attaches to the data flow, not the logo.

### The sub-concepts

**Residency: where does compute and storage sit?** Regional endpoints matter — a Singapore region endpoint keeps processing in-country. A non-regional endpoint may route anywhere. Check the specific endpoint, not the brand.

**Retention: how long is it kept, and who can see it?** Consumer tiers commonly retain conversations for a period and allow human review of flagged content. Enterprise terms can offer zero data retention, where prompts and completions are not stored beyond the request. That clause is the one to find in the contract.

**Training use: is my content feeding the model?** Many consumer products reserve the right to use interactions to improve services; enterprise agreements usually opt out by default. This is a separate clause from retention and is often missed.

**Sub-processors and onward transfer.** A provider that hosts in Singapore may still use a support team or a moderation vendor elsewhere. Cross-border transfer obligations under the PDPA attach to the onward flow, not only to the first hop.

**Sector overlays in Singapore.** Financial institutions work under MAS technology risk expectations; healthcare under MOH guidance; public sector under Government Commercial Cloud arrangements. Each adds requirements that a generic vendor page will not answer.

**Governance framework alignment.** IMDA's Model AI Governance Framework for Generative AI is the reference map for what a responsible deployment covers. Citing it in a procurement paper is normal and expected.

**Deletion and the data subject.** If someone requests deletion, retention in a vendor's logs is still retention. Know the deletion path before promising it.

### How it connects to the rest of the framework

`TSC4-Intermediate-K3` lists compliance as a gate among the selection dials; this bullet is that gate in detail. `TSC4-Advanced-K1` explains the hosting patterns that determine residency. `TSC4-Advanced-A4` places retention and audit in the operations pipeline. `TSC4-Intermediate-K5` covers the same obligation for training data, where a deletion request is even harder to honour.

### What is current as of November 2026

For the 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — the practical landscape:

- **Regional endpoints are now standard for enterprise tiers, not premium add-ons.** Singapore-region processing is available across the major vendors; the consumer tiers remain less predictable.
- **Zero-retention and no-training terms are negotiated, not assumed.** They exist at enterprise tier under a data processing agreement, and the default consumer behaviour is different.
- **Agentic features widened the data flow.** Tool calls, browsing and file analysis send content further than a chat completion did, so the scope of a residency review now includes every tool a model can reach.

### Common misconceptions

- *"It is a US company, so it is non-compliant."* The question is where the endpoint processes and stores data, under which contract terms. Many US-headquartered providers offer in-region processing and zero retention.
- *"We signed a DPA, so we are covered."* A DPA without checking sub-processors, retention and training clauses is a signature, not a control.
- *"We only send anonymised data."* Names removed is not anonymised; free text is full of re-identifying detail.
- *"Deleting the chat deletes the data."* It deletes your view of it. Ask about logs, backups and review queues.

## How a student should understand it

**Mental model:** sending a document to a contractor. The question is not whether the contractor is trustworthy; it is whether the document leaves the country, sits in their inbox for thirty days, and gets read by their intern.

**Things they can do after this bullet:**
1. Read a provider's terms and locate the retention, training and residency clauses.
2. Compare two providers on those four questions for a stated dataset.
3. Escalate a specific risk with the clause that creates it, rather than a general worry.

**Misconceptions to kill:** that cloud means compliant, that a DPA covers everything, and that removing names makes data safe.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The office shredder.** A policy of "we shred everything after use" is only meaningful if you know which bins the cleaner empties and where the bags go. Retention clauses are the shredder; sub-processors are the cleaner.

**The overseas tailor.** Fine work, good price — but your measurements now live in another country, and you cannot get them deleted when you change your mind.

### Worked example with a real tool

Ask for the questions, not the answer:

```text
A client requires their data to stay in Singapore with no retention.
What three questions do you ask a model provider, and what would a
bad answer look like for each?
```

What to point at afterwards: residency, retention, and sub-processor sharing. Good answers add the training-use clause and the deletion path. Then make it concrete with a second prompt, which is the real teaching moment:

```text
Here is a provider summary. Find the two clauses that would block us
for a dataset containing NRIC numbers, and quote them.
[Paste: a short, plainly-written summary with a 30-day retention clause
and a "may use inputs to improve services" clause.]
```

The room should locate both clauses by name. That is the skill — locating a clause in a document, not remembering a regulation.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "where does your prompt go when you press enter?" Let the room guess, then correct.
2. **State the objective** — by the end you can find and compare the four clauses and escalate a specific risk.
3. **Recall prior learning** — hosting patterns from the earlier bullets.
4. **Present the content** — residency, retention, training use, sub-processors, sector overlays, deletion.
5. **Guide** — read one provider's summary together and mark the clauses.
6. **Elicit performance** — pairs compare two summaries against a client requirement.
7. **Give feedback** — debrief, insisting on quoted clauses rather than impressions.
8. **Transfer** — each learner lists the obligations their own organisation's data carries.

## What the framework doesn't mention but trainers need to know

- **The consumer and enterprise products of the same vendor behave differently.** A team can pilot on the free tier and then discover the production terms are the ones that matter. Start the compliance review in the right tier.
- **Agentic tool use widens the scope.** Every connected system is a new data flow to review. A residency assessment that covers the chat endpoint but not the browsing tool is incomplete.
- **Abuse monitoring can involve human review.** Flagged content may be read by a person, which is a disclosure event under some contracts.
- **Deletion promises need a technical path.** If the vendor retains logs for a period, your deletion promise to a customer is not keepable within that window.
- **Put the clauses in the procurement paper.** "Vendor states 30-day retention, which conflicts with clause 7 of our client agreement" wins the argument; "we are worried about privacy" does not.

## Watch out

- **Do not give legal advice.** Teach how to read the clauses and who to escalate to. The trainer is not the data protection officer.
- **Do not name a provider as compliant or non-compliant.** Terms change and configurations differ; teach the questions.
- **Do not demo with real personal data.** Ever, in any tier, for any reason.
- **The stale claim to retire:** "we will sort out compliance before go-live." Compliance is a design input; discover it late and you rebuild.
