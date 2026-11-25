# Data privacy regulations

> **TSC #2 Prompt Design · Basic · Knowledge K6**

**Bullet (verbatim):** Overview of data privacy regulations.

**What it means:** Singapore’s Personal Data Protection Act (PDPA) is a baseline law for how organisations handle personal data: information about someone who can be identified from it, alone or with other information the organisation has or is likely to have. Organisations generally need to tell people why their data is collected, used or shared, obtain their consent (permission) unless an exception applies, and take reasonable steps to protect it. A prompt is an instruction to an AI tool; before using real personal data, check the intended use, the relevant permissions and your organisation’s rules, because removing names alone does not guarantee anonymity, meaning that a person cannot be identified from the data. This overview is general information, not a legal determination; for a real case, consult your organisation’s data protection officer, the person responsible for data protection, or a legal adviser.

**The learner must be able to:**
- Explain what personal data means under the PDPA, including identification using other available information.
- Describe the general duties to give notice of purposes, obtain consent where required and protect personal data.
- Distinguish a person’s consent or an applicable legal exception from an organisation’s own approval rules.
- Identify why deleting names may not make a record anonymous and choose a next step before using real data in a prompt.

**How to teach it in 20 minutes:**
1. Ask: “If a customer record has no name, why might it still need care before you put it into a chat AI?” Collect suggestions without asking for real customer details. (3 min)
2. Explain the PDPA baseline using an imagined appointment list: the intended use must be appropriate, people generally need to be told the purpose, consent may be needed, and personal data needs reasonable protection. Exceptions can apply. Explain that an organisation’s own rules and approval for an external (outside the organisation) chat AI are separate checks, and safeguards are ways of protecting data. (7 min)
3. In pairs, learners run the exercise below. They compare the checklist with the stated checks, mark any missing point and explain one correction to each other. (8 min)
4. Debrief: ask why B and C are paused, why an appointment-reminder agreement is not automatically permission for AI use, and why the fictional approval rule is not a universal PDPA requirement. (2 min)

**Exercise (with the exact prompt):**
*Setup: pairs need access to a chat AI; no files or real customer information are needed.*

```text
You are helping a Singapore workplace prepare a privacy checklist. All people, workplaces and situations below are fictional; no real customer details are supplied.

Use these teaching points:
- Singapore's Personal Data Protection Act (PDPA) gives a baseline standard for organisations' handling of personal data: information about a person identifiable from the data alone or with other information the organisation has or is likely to have access to.
- Organisations generally must notify individuals of purposes and obtain consent for collection, use or disclosure, unless an exception applies; purposes must be reasonable. They must use reasonable security arrangements.
- Removing a name alone does not ensure anonymity; remaining details combined with other information may identify someone.

Fictional workplace policy: A worker may use the external chat AI for generic text without customer data. For actual customer data, the worker must first obtain approval from the data protection officer (DPO), the person responsible for data protection, and check the relevant permissions and safeguards. This is a made-up workplace rule, not a claim that the PDPA always requires this approval.

Consider these hypothetical requests:
A. Draft a generic appointment reminder, with no customer data.
B. Paste customer names and phone numbers from an appointment list into the chat AI. Customers agreed to receive appointment reminders, but there is no approval for this AI use.
C. Paste customer records without names, but with exact job titles and postal codes. Other information available to the organisation could identify those customers. There is no approval for this AI use.

Create a three-row checklist, one row per case, with a decision to proceed or pause, a short reason, and a next step. Distinguish consent or an applicable exception under the law from the fictional workplace approval. End with one sentence saying this is general information, not a legal determination. Do not invent or ask for any customer records.
```

*Expected result: a three-row checklist with a decision, reason and next step for each case, followed by the general-information statement.*  
*What to check: A proceeds with generic text; B and C pause. B’s reminder agreement does not by itself settle permission for AI use; C may still identify customers. The checklist separates the fictional approval rule from checks on notice, consent or an applicable exception, and safeguards.*

**Common mistakes:**
- Treating agreement to receive reminders as automatic permission for any AI use — check the proposed purpose, notice and consent or an applicable exception, as well as safeguards and the organisation’s approval rules.
- Assuming that deleting a name makes a record anonymous — other available details can still identify someone; pause and seek a proper assessment before using the record.
- Treating the AI’s checklist as a legal ruling — check current PDPC guidance and consult the data protection officer or a legal adviser about the actual facts.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf — accessed 2026-11-15; page 5 establishes the TSC, level and verbatim bullet.
- https://www.pdpc.gov.sg/about/the-legislation/pdpa-overview — accessed 2026-11-15; defines personal data and describes the PDPA’s baseline and scope.
- https://www.pdpc.gov.sg/data-protection-obligations — accessed 2026-11-15; describes notification, consent, purpose limitation, protection and accountability obligations, and notes that exceptions may apply.
- https://www.pdpc.gov.sg/assets/143cb9d4-532e-4cca-9a77-bcc0415ca294 — accessed 2026-11-15; PDPC’s 2026 generative AI advisory discusses consent and exceptions, organisations’ responsibilities, safeguards and written policies; it states that the guidance is not legal advice.
- https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/advisory-guidelines/guide-to-basic-anonymisation-%28updated-24-july-2024%29.pdf — accessed 2026-11-15; explains that removing direct identifiers is not necessarily anonymisation because other information can enable identification.
- https://developers.openai.com/api/docs/guides/evaluation-best-practices — accessed 2026-11-15; explains that outputs can vary for the same input and should be checked against specific criteria.
