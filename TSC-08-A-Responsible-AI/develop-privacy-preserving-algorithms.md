---
id: 08.03.A.A4
tsc: 8
level: Advanced
code: A4
title: Develop privacy-preserving algorithms
---

# Develop privacy-preserving algorithms

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A4**

> **Framework text (verbatim):** "Develop new privacy-preserving algorithms."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 8 of 14

**One-line version:** Privacy engineering is the art of learning from data you are not allowed to see.

## What it is

Privacy-preserving techniques let an organisation extract a pattern — a model, a statistic, a risk score — without exposing the individuals whose records produced it. Four families do most of the work: data minimisation and redaction, which removes the obvious identifiers; differential privacy, which adds calibrated noise so no single record can be inferred; federated learning, which trains across institutions by exchanging model updates rather than records; and secure computation, which lets parties compute on encrypted or isolated data. Developing new algorithms is specialist research; the skill at this level is knowing which family fits which problem, and what each one actually promises.

## Deep expansion

### The concept

The naive answer, "remove the names", fails for a reason worth teaching first: anonymisation is a property of a dataset, and inference is a property of everything else you know. Two released tables can be joined on a quasi-identifier — postal code, birth year, gender — and re-identify people. A model itself learns distributions: a membership inference attack asks "was this person's record in the training set?" and often gets a confident answer. So the modern framing is not "is it anonymous" but "what can an adversary learn, with what confidence, and at what cost".

Each technique answers a different question, and trainers should keep them separate:

**Differential privacy** answers "how much does one person's record change the output?" Noise is added so that the answer with and without that record is nearly identical. The guarantee is mathematical and it degrades predictably as you answer more queries — the privacy budget, epsilon. Small epsilon means more noise and stronger protection; the trade-off is explicit, which is its virtue.

**Federated learning** answers "can we train without centralising the data?" Hospitals, banks or agencies each train locally and share only model updates. The data never moves; the statistics do.

**Secure computation** — secure multiparty computation, homomorphic encryption, trusted execution environments — answers "can parties compute together without seeing each other's inputs?" It is the most expensive option and the right one when the data cannot legally or commercially move at all.

**Redaction and minimisation** answer "do we need this field?" Presidio-style scanners catch NRIC numbers, phone numbers and card numbers before a prompt leaves the building; minimisation asks why the field was collected at all.

### The sub-concepts

**Epsilon must be stated.** A differential-privacy claim without a budget is marketing. Ask what epsilon, how many queries, and over what period.

**Federated learning is not a privacy guarantee.** Gradients leak; a curious server or a poisoned participant can reconstruct information. It needs secure aggregation and clipping to mean anything.

**Synthetic data inherits its source.** A generator trained on real records can memorise them; evaluate it with the same membership tests as a model.

**Redaction fails on context.** A name removed but a rare job title, a project code and a date left in place may still identify one person.

**Purpose limitation is a design constraint.** The PDPA's business-improvement exception lets an organisation use existing data for internal improvement without fresh consent, under conditions — not as a general licence.

### How it connects to the rest of the framework

`TSC8-Advanced-K1` supplies the privacy frameworks this technique satisfies; `TSC8-Advanced-A2` supplies the evaluation method for testing whether the protection holds (canary insertion, membership inference); `TSC8-Advanced-A3` supplies the attacker's view; `TSC8-Advanced-A10` is the advocacy case for funding it; `TSC8-Advanced-K4` is the socio-political question of who bears the risk when it is skipped.

### What is current as of November 2026

Privacy engineering has become a procurement line item rather than a research topic. Enterprise agreements with the major providers — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and 4 Argon — now turn on zero data retention, regional processing and whether prompts train anything. Confidential computing is available on mainstream cloud, which makes "compute on encrypted data" a configuration rather than a research project. The live pressure is agentic: an assistant with tool access can move data to places the privacy review never saw, which is why input redaction and permission scoping matter more than the model's own memory settings.

### Common misconceptions

- *"We anonymised it, so it is safe."* Anonymisation fails under linkage and under model inference. Differential privacy is the guarantee you can state.
- *"Federated learning means the data never leaves."* The data stays; the leakage moves into the updates.
- *"Privacy costs accuracy, so we accept the loss."* The trade-off is tunable: quantify utility at several privacy levels and choose.
- *"We do not collect personal data, so PDPA does not apply."* Inferred data about an identifiable person is personal data.

## How a student should understand it

**Mental model:** the ballot box. Each person's vote is secret; the count is public and exact enough to decide an election. Federated learning is counting per polling station and reporting only totals; differential privacy is publishing the count with enough rounding that no single ballot can be deduced.

**Things they can do after this bullet:**
1. Match a technique to a problem, and say what it does not protect.
2. Read a differential-privacy claim and ask for epsilon, query count and period.
3. Place redaction at the boundary where data leaves the organisation.

**Misconceptions to kill:** anonymisation is safety, federated means private, and privacy always costs more accuracy than it is worth.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The ballot box and the counting room.** Votes are secret, totals are published, and the system works precisely because the two are separated. Where it breaks: a small precinct's total can reveal how one household voted, which is exactly the small-group problem in privacy.

**Static on a phone line.** Differential privacy is deliberate static: you can follow the conversation, but not every word, and the amount of static is the promise you are making. Where it breaks: static is audible; a privacy budget is invisible to the listener.

### Worked example with a real tool

```
Match each requirement to a privacy technique and state what it does NOT protect:
(a) train a shared model across three hospitals without pooling patient records
(b) publish average waiting times without identifying any patient
(c) let two agencies compute a combined eligibility score without sharing lists
(d) stop NRIC numbers reaching an external LLM API
```

What to point at: the mapping is easy (federated, differential privacy, secure computation, redaction); the second column is where the learning is. Almost nobody volunteers that federated learning leaks through updates or that averages over small cells identify people. That column is what separates a technique name from an engineering judgement.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two "anonymised" tables joined live to reveal one person. No maths, just a join.
2. **State the objective** — choose a technique per problem and state its limit.
3. **Recall prior learning** — PDPA consent and notification from `TSC8-Advanced-K1`.
4. **Present the content** — four families, one guarantee each, one failure each.
5. **Guide** — work the matching exercise together.
6. **Elicit performance** — groups write a one-paragraph design for a real data-sharing proposal.
7. **Give feedback** — challenge any claim without a stated epsilon or retention rule.
8. **Transfer** — each learner audits one live data flow for an unnecessary field.

## What the framework doesn't mention but trainers need to know

- **Most breaches are convenience, not attack.** A copied spreadsheet, a pasted prompt, a personal account — the technical controls are the last line, not the first.
- **The privacy budget is a governance object.** Someone must own how many queries are allowed, or the guarantee erodes one analyst at a time.
- **Vendors differ on retention.** Ask what happens to prompts, outputs and uploaded files, and get it in the contract.
- **Small populations break every aggregate.** In Singapore, a "district-level average" over a few hundred households is closer to a list than a statistic.

## Watch out

- **Do not teach differential privacy as "add noise".** Teach it as a bound on what one record can change.
- **Do not imply re-identification is exotic.** It is a join and a guess, done by a curious colleague.
- **Do not let "privacy-preserving" pass without a threat model.** Preserving against whom?
- **The stale claim to retire:** "We removed the NRIC column." Identifiers are plural; inference does not need the column.
