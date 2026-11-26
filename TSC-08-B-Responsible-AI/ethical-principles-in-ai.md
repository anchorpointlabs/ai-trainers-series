---
id: 08.01.B.K1
tsc: 8
level: Basic
code: K1
title: Ethical principles in AI
as_at: 2026-11-26
review_by: 2027-02-25
---

# Ethical principles in AI

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Knowledge K1**

> **Framework text (verbatim):** "Ethical principles in AI."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Knowledge · Bullet 1 of 10

**One-line version:** Ethics is not a poster on the wall — it is a short list of principles, each of which changes a specific decision you were about to make.

## What it is

AI ethics is the study of what an AI system *ought* and *ought not* to do: which values it serves, who it may harm, what a fair outcome looks like. For a Basic learner it collapses into a short list — fairness, transparency, accountability, safety, privacy — each of which maps onto a concrete choice about how a tool is built, bought or used.

## Deep expansion

### The concept

The framework's bullet is four words long, which is why trainers get it wrong. "Ethical principles in AI" sounds like a philosophy seminar. It is a decision aid.

Three words are used interchangeably in most rooms and must be separated:

- **Ethics** asks *should we build this, and who does it serve or harm?* Moral question, no single statutory answer.
- **Governance** asks *who has the authority to approve it, what thresholds must it pass, who answers if it fails?* Roles, gates, sign-offs, audit rhythm.
- **Safety engineering** asks *how do we technically constrain the model so it cannot output the harmful thing?* Classifiers, guardrails, evaluation harnesses.

A learner who can separate those three can talk to a risk officer, an engineer and a customer without confusing them. A learner who cannot keeps saying "isn't that the same thing?" and loses the room.

The second shift: principles are only real when they bind a decision. "We value fairness" is decoration. "We will not deploy the screening model until the disparate impact ratio across applicant groups clears our threshold, and a named person signs that off" is a principle at work. Insist on the second form every time a learner offers the first.

### The sub-concepts

**The core five.** Fairness (no unjustified differential treatment or outcome), transparency (people know AI is involved and what data it used), accountability (a named human owns the outcome), safety (no physical, psychological or financial harm), privacy (personal data is lawful, minimal, protected). The distillation lists twelve in total; for Basic, these five are the working set and the rest are refinements.

**Accountability is the load-bearing principle.** Every other principle can be delegated to a process; accountability cannot. It must land on a named human with the authority to say no. It is also the principle that survives a tribunal: when a company argued its website chatbot was a separate legal entity and therefore its own statements were not the company's, the argument failed. A chatbot on your site wears your uniform.

**Fairness is not blindness.** The instinct is to delete race, gender and age columns and declare the model neutral. High-dimensional models rebuild those attributes from proxies almost immediately — postal code, school name, mother-tongue subject, NS vocation, employment gaps. Worse, deleting the columns blinds the auditor, who can no longer measure whether outcomes differ by group. Exclude the attributes from the predictive features; retain them in a controlled audit table.

**Principles conflict, and someone must choose.** Mathematical fairness definitions are provably incompatible: you can equalise approval rates across groups, or equalise the chance that a genuinely qualified person is approved, generally not both. Ethics names the trade-off; governance picks which one this product optimises for and records why.

**Transparency is not explainability.** Transparency is the sign at the stall: *cooked by a robot, contains peanuts*. Explainability is being able to ask why your bowl was saltier than your friend's and get a real answer. Everyone deserves the first; a loan refusal or a flagged scan needs the second.

### How it connects to the rest of the framework

This bullet is the vocabulary. `TSC8-Basic-K2` extends it to the three practical checks (IP, privacy, environment); `TSC8-Basic-K3` handles the data end of privacy; `TSC8-Basic-K4` is what happens when these principles are ignored in a live GenAI interaction. `TSC8-Basic-A1` is this bullet applied at the moment of decision, `TSC8-Basic-A2` is how much scrutiny a use deserves, and `TSC8-Basic-A4` turns principles into a written guideline a team can follow.

### What is current as of November 2026

The principles now have statutory teeth even though the flagship framework is voluntary. IMDA's Model AI Governance Framework for Generative AI (May 2024) set nine dimensions — accountability, data, trusted development and deployment, incident reporting, testing and assurance, security, content provenance, safety and alignment R&D, AI for public good. The PDPA carries enforcement: penalties up to 10% of annual turnover in Singapore or SGD 1 million, whichever is higher, with PDPC advisory guidelines defining what "reasonable" looks like. Voluntary guidance plus hard statute is the operating model; calling Singapore "self-regulation" misleads the room.

The frontier models of late 2026 — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — are close enough on capability that the question is rarely "can it". It is "may it, on whose authority, with what record". That is why this bullet sits at the front of the TSC.

### Common misconceptions

- *"Ethics is a compliance function that slows engineering down."* Legal compliance is a fraction of it. The rest is quality assurance and operational risk management, and automated evaluation pipelines are what let a prototype leave the sandbox.
- *"Remove the demographic columns and the model cannot discriminate."* It can, through proxies — and you can no longer prove otherwise.
- *"We have a human in the loop, so we are compliant."* A human clicking approve 400 times an hour is theatre.
- *"The vendor's model made the decision, so the vendor is liable."* The deploying organisation owns how the system treats its customers and staff.

## How a student should understand it

**Mental model:** the LTA, not the airbag. Ethics is the shared belief that nobody should die on the road; safety engineering is the crumple zone and ABS; governance is the COE system, the VICOM inspection, the ERP gantry and the demerit points. You do not drive fast *because* you have brakes — you can only drive fast *because* brakes, rules and inspections exist.

**Things they can do after this bullet:**
1. Name the five principles and give a workplace decision each would change.
2. Separate an ethics question from a governance question from a safety-engineering question when a colleague blurs them.
3. Say, for any AI use in their own work, who the accountable named human is — and notice when the answer is "nobody".

**Misconceptions to kill:** that ethics is philosophy rather than decisions; that "the AI decided" transfers responsibility; that fairness comes from hiding the demographic columns.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The LTA and the expressway.** As above. Where it breaks: road rules come from one authority with statutory power, while AI principles are contested and often voluntary — so it explains *why* governance exists, not how it is enforced.

**The uniform.** A chatbot wearing your logo is a staff member at your check-in counter; if it speaks for you, its words are yours. Where it breaks: a staff member can be asked to explain on the spot, a model cannot — which is why explainability is a separate principle.

### Worked example with a real tool

Turn four principles into four decisions for one real use case. In ChatGPT, Claude or Gemini:

```
Our HR team wants an AI tool to shortlist 300 applicants for a customer
service role. A human recruiter stays in the loop.

For each principle, give ONE decision this project must make, stated as a
testable rule, and name who should own it:
1. Fairness  2. Transparency  3. Accountability  4. Safety (candidates + data)

Then say which of the four a regulator would care about most, and why.
```

What to point at afterwards: the model assigns ownership to job titles rather than names, and usually misses that candidates must be told AI is involved. Both gaps are the lesson — a principle without a named owner and a disclosure step is still a poster.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "An AI told a customer something wrong and the company had to pay. Whose fault?" Collect answers, resolve nothing yet.
2. **State the objective** — name the five principles, attach each to a decision in your own work, say who is accountable.
3. **Recall prior learning** — ask what "professional" means in their job; ethics is that standard written down.
4. **Present the content** — the three-way distinction, then the five principles with one decision each.
5. **Guide** — work the HR shortlisting example together, filling in owner and test per principle.
6. **Elicit performance** — pairs complete a four-scenario match: (a) AI ranks applicants, nobody checks; (b) staff use AI without telling customers; (c) a model gives medical advice; (d) a customer list is pasted into a free tool. The mapping to accountability, transparency, safety and privacy is the answer key.
7. **Give feedback** — which rules were unmeasurable, which had no named owner, which forgot disclosure.
8. **Transfer** — each learner names one decision they will change this week and who they must tell. Return to the opening "whose fault?" question and re-answer it.

## What the framework doesn't mention but trainers need to know

- **Principles are cheap; owners are expensive.** The usual failure is not disagreement about fairness — it is that nobody's job description includes it. Push for names, not departments.
- **Twelve principles in ninety minutes produces nodding and no retention.** Teach five, name the rest, promise them at Intermediate.
- **Local proxies make fairness land.** Postal code, school name, mother tongue, NS vocation — every learner recognises them instantly. Better than any imported example.
- **Small firms carry the liability too.** A ten-person agency using an AI writing tool is a deploying organisation under the PDPA. Scale changes the paperwork, not the obligation.

## Watch out

- **Do not teach ethics as a list to memorise.** If the room can recite five words and cannot change one decision, the bullet failed.
- **Do not let "human in the loop" pass unchallenged.** Ask how many cases per hour that human clears; the answer usually ends the discussion.
- **Do not overclaim the law.** The IMDA frameworks are voluntary; the PDPA, MAS rules, HSA device rules and the Online Criminal Harms Act are not. A sceptical compliance officer will check.
- **The stale claim to retire:** "AI ethics is about stopping AI." It is about deciding in advance, in writing, what the system may do, who signs for it, and how a person appeals.
