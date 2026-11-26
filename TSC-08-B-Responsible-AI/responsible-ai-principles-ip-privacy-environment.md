---
id: 08.01.B.K2
tsc: 8
level: Basic
code: K2
title: Responsible AI principles — IP, privacy, environment
as_at: 2026-11-26
review_by: 2027-02-25
---

# Responsible AI principles — IP, privacy, environment

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Knowledge K2**

> **Framework text (verbatim):** "Responsible AI principles and best practices for development and deployment, including intellectual property, data privacy and environmental impact considerations."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Knowledge · Bullet 2 of 10

**One-line version:** Before you type into any AI tool, run three checks — whose material is this, whose data is this, and how much compute does this task actually deserve?

## What it is

Responsible AI practice, at the level a working professional needs it, is three practical checks applied at the moment of use: **intellectual property** (who owns what goes in and what comes out), **data privacy** (personal data must be lawful, minimal and protected), and **environmental impact** (every inference has an energy cost, so use the smallest model that does the job).

## Deep expansion

### The concept

The framework groups these three because each is a cost that is invisible at the moment of the prompt and lands on somebody else later: IP risk when a client's document turns up in a third party's logs, privacy risk on a customer whose NRIC is now in a training corpus, environmental cost on a data centre in a water-constrained country and eventually on your cloud bill.

They belong together because all three live in the same five seconds before a person presses enter. A learner who internalises one check tends to internalise the pattern.

### The sub-concepts

**Intellectual property: the input side.** Pasting a client's contract, an unpublished financial result or a proprietary codebase into a consumer tool is a disclosure to a third party. Whether that is a breach of confidence, a PDPA problem or a contract breach depends on the document — but it is always a risk you took on the client's behalf without asking. The correct default for Basic learners is blunt: *if you would not email it to a stranger, do not paste it into a free tool.*

**Intellectual property: the output side.** Copyright in AI-generated material is unsettled almost everywhere. Ownership of machine-generated works in Singapore has been the subject of consultation rather than settled statute, so treat output as *usable but not clearly yours to register*. Two risks matter more day to day: an output that reproduces a substantial part of an existing protected work, and code assistants emitting verbatim open-source code into proprietary software, which can contaminate licensing. Enterprise coding assistants mitigate the second with reference filters that block matches against public repositories — a feature worth asking a vendor about.

**Privacy.** The PDPA is the floor: consent or a valid exception, purpose limitation, notification, and an accountability obligation you can evidence. The AI twist is that the data does not stay in your system — it reaches an inference endpoint, may be logged, may be retained, and in consumer products may train the model. Three controls follow: minimise what you send, redact identifiers before sending, and use a tool contracted for zero retention. The distillation's "shadow AI" failure — staff pasting records into personal accounts — is the most common real breach in Singapore organisations, and it is a procurement problem as much as a discipline one: people use the sanctioned tool when the sanctioned tool is good.

**Environment.** Training and inference draw electricity; cooling draws water. In a land- and water-constrained country that is not an abstraction, which is why Singapore publishes green data-centre efficiency standards. The learner-level version is model right-sizing: keyword classification does not need a frontier reasoning model. Routing millions of trivial tasks through the largest model burns compute for no accuracy gain, and the cheaper distilled model is also the greener one. The classroom line: the greenest prompt is the one you did not need to send.

**Proportionality ties all three together.** Is the intrusiveness and risk proportionate to the problem solved? A system that ingests the whole customer database to answer a question about one customer fails that test on privacy and on compute at once.

### How it connects to the rest of the framework

`TSC8-Basic-K1` gives the principle vocabulary; this bullet is where the three most commercially visible principles get operational. `TSC8-Basic-K3` and `TSC8-Basic-A5` go deep on the privacy half (anonymisation, encryption, access control). `TSC8-Basic-A3` turns this bullet into a vendor comparison — which provider's terms actually protect you. `TSC8-Basic-A4` turns it into the written rule staff will follow. On the GenAI side, `TSC1-Basic-K06` (limits of the technology) explains why the model cannot be trusted to police any of this for you.

### What is current as of November 2026

The three checks have converged into procurement questions. Enterprise tiers of the major assistants — the paid organisational products around GPT-6 generation models, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — now commonly offer zero-retention terms, administrative controls and audit logs, which means the IP and privacy answer is often "use the enterprise endpoint, not the free one". That is a purchase decision, not a training one, and trainers should say so rather than imply discipline alone will fix it.

On the environment, the industry's own answer has been efficiency: smaller distilled models and aggressive caching mean the marginal cost of a routine task has fallen sharply, while the top of the range has grown more expensive to run. The practical guidance for learners has not changed and will not: match the model to the task, and batch rather than repeat.

On IP, the direction of travel is documentation and provenance rather than new ownership rules. Model and system cards, training-data summaries and content-provenance metadata (the C2PA standard) are becoming standard vendor disclosures — which means a buyer can now ask questions that were unanswerable two years ago.

### Common misconceptions

- *"It's just a draft, so IP doesn't apply."* The disclosure happened at the paste, not at the send.
- *"Free tools are fine for internal work."* Free consumer tiers are precisely the ones most likely to retain and train on your input.
- *"Using the biggest model is the safe choice."* It is the most expensive choice, on money and on energy, and rarely the most accurate for narrow tasks.
- *"Anonymised data is outside the PDPA."* Only if re-identification is genuinely not reasonably practicable — a standard that name-removal does not meet.

## How a student should understand it

**Mental model:** the three-tap check before you photocopy anything at a neighbour's shop. Whose document is this? Whose face is on it? Do I need the whole thing, or one page?

**Things they can do after this bullet:**
1. Run the three checks out loud on any task before they type the prompt.
2. Explain to a colleague, in one sentence each, why pasting a client contract into a free tool is an IP and privacy event.
3. Choose a smaller model, or no model, for a task that does not need a large one — and say why in cost terms.

**Misconceptions to kill:** that a draft is not a disclosure; that all providers are equal on data terms; and that bigger is safer.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The photostat shop.** You would not carry a client's file to the shop down the road, hand it over and hope they shred it. Pasting into a consumer AI tool is that walk at the speed of ctrl-V. Where it breaks: the shop gives you back *your* document; the model gives you something derived from everyone's, which is why output IP is a separate question.

**The kopitiam order.** You want one teh-o. You do not need the whole kitchen brigade, the wok station and the induction hob. Model choice is portioning: order the size of the job. Where it breaks: unlike a kitchen, the expensive model is not obviously "better food" — for a narrow task it is often the same answer at ten times the cost.

### Worked example with a real tool

Task: get a learner to see the risk from the inside, without committing a real breach. Use a fabricated record, in ChatGPT or Claude:

```
Here is a customer record from a training exercise (all details invented):
"Mdm Tan, 65, diabetic, Blk 12 Bedok, S1234567A, outstanding balance $4,180."

1. List every field in this record that is personal data under Singapore's PDPA.
2. For each, say what could identify her if it were combined with one other
   public source.
3. Then rewrite the record so it can be shared with an analyst for a
   pricing study, and explain what you removed and why.
```

What to point at afterwards: the model will usually be thorough about the NRIC and the address, and much weaker on the *combination* — age plus block plus a chronic condition is often enough to narrow to very few people. Then make the second point: you have just demonstrated the correct sequence, which is redact locally and only then use a tool. Doing it the other way round is the breach.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "You have just pasted a client's contract into a free AI. Nothing has happened yet. What have you already done?"
2. **State the objective** — by the end you can run the three checks on any task and pick a tool that survives them.
3. **Recall prior learning** — PDPA basics from their onboarding; most rooms know consent and do-not-call, few know purpose limitation.
4. **Present the content** — IP input, IP output, privacy, environment, proportionality.
5. **Guide** — work the fabricated-record example together, including the redact-first sequence.
6. **Elicit performance** — pairs run the three-check audit on one scenario each: a client sales spreadsheet into a free bot; 400 CVs into a consumer chatbot; 200 product descriptions on the largest model. Ninety seconds, then report.
7. **Give feedback** — correct the two habitual errors: "it's internal" and "bigger is better"; ask the room which of the three checks they skipped most often — it is nearly always environment.
8. **Transfer** — each learner identifies the one tool they personally use that fails a check, and what they will use instead.

## What the framework doesn't mention but trainers need to know

- **The fix is usually procurement, not discipline.** Staff use shadow AI when the sanctioned tool is worse. Tell the room to ask for an enterprise endpoint before they ask colleagues to be more careful.
- **Output copyright is genuinely unsettled.** Do not teach "you own what you generate" as fact in either direction. Teach the posture: usable, check for reproduction, do not assume registrability.
- **Environment lands as a cost conversation in most SMEs.** Lead with model right-sizing as a money argument; the energy argument is true and second, and water is the Singapore-specific hook — tropical data centres cool by evaporation.
- **Code contamination is the IP risk learners underestimate.** Anyone using a coding assistant in a proprietary codebase should know what a reference filter is.

## Watch out

- **Do not demo with real personal data.** Ever. Use invented records and say out loud that they are invented.
- **Do not claim a specific legal outcome for AI-generated copyright.** Consultations are not judgments.
- **Do not let "we use the enterprise version" end the conversation.** Ask what the retention setting is, who can change it, and whether logs are on.
- **Do not quote energy or emissions figures you cannot source.** The direction is enough: bigger models, more compute, more cost. No invented numbers.
- **The stale claim to retire:** "Responsible AI is about the model." At this level it is about the paste, the purchase and the model choice — three decisions the learner personally makes.
