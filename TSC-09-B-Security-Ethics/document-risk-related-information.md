---
id: 09.01.B.A2
tsc: 9
level: Basic
code: A2
title: Document risk-related information
as_at: 2026-11-26
review_by: 2027-02-25
---

# Document risk-related information

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Ability A2**

> **Framework text (verbatim):** "Document risk-related information."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Basic** · Ability · Bullet 6 of 8

**One-line version:** A risk you cannot point to on paper is a risk you cannot manage, fund, or defend — so write it in four parts and give it a name.

## What it is

Documenting risk means recording each identified risk in a form someone else can act on: what could happen, how likely it is, what the impact would be, and what is being done about it. It converts a conversation into a record. For an AI system the record is what a manager approves, what an auditor samples, and what the next engineer reads before changing a prompt.

## Deep expansion

### The concept

There are three reasons documentation is an ability and not paperwork. First, **memory fails**: the team that discussed the hallucination risk in March will not remember the mitigation in September, and the person who joins in October will not know it was discussed at all. Second, **risk needs a decision**: writing "likelihood: medium, impact: high, mitigation: human approval on refunds" forces someone to accept or reject that trade-off, and it names who accepted it. Third, **evidence**: under Singapore's PDPA, an organisation must be able to show it took reasonable steps to protect personal data. A risk log is part of that showing.

The Basic-level skill is not the framework. It is the habit: a short, specific, four-part note, written at the moment the risk is found, with an owner.

### The sub-concepts

**The four parts.** Risk (one sentence, specific), likelihood (how often it would bite), impact (what it would cost — money, data, customer, reputation, regulatory), mitigation (the control that reduces it). Anything less is a worry, not a record.

**Specificity.** "The AI might give wrong answers" is not a risk statement; it is a category. "The assistant may confirm a refund the customer was not offered, and the customer may hold us to it" is a risk statement — it says who does what and what follows.

**The mitigation column is the point.** A note with no mitigation is a complaint. The mitigation should name a control (guardrail, human gate, data restriction, monitoring) and, ideally, who owns it.

**Owner and review date.** Every entry has a person and a date. Without an owner, nothing happens; without a review date, the entry quietly becomes false.

**Residual risk.** After the mitigation, some risk remains. Naming it — "after human approval, residual risk is low but not zero for high-value refunds" — is what lets a manager make a real decision rather than a hopeful one.

**The register.** Individual notes accumulate into a register: a table of id, risk, likelihood, impact, mitigation, owner, status, review date. The register is the artefact that survives staff turnover.

### How it connects to the rest of the framework

`TSC9-Basic-A1` is finding the risk; this bullet is recording it. `TSC9-Basic-K4` is the ongoing review that keeps entries current. At Intermediate, `TSC9-Intermediate-K3` supplies the scoring methods (risk matrix, bowtie) that make likelihood and impact comparable, `TSC9-Intermediate-A4` runs a full assessment, and `TSC9-Intermediate-A1` pairs each risk with a mitigation worth its cost.

### What is current as of November 2026

Two pressures have made this bullet more visible. Regulators expect documented risk management for AI, and enterprise procurement now asks for it — a supplier without a risk register struggles to pass a security review. At the same time the systems being documented have become agentic: current frontier models are routinely connected to tools, so the impact column now frequently involves an action rather than an answer.

- **Risk language has been standardised by procurement.** Buyers ask for a register; a scruffy one costs deals.
- **Agentic risks need an action column.** "What can it do" belongs in the same note as "what could go wrong".

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"We discussed it in the meeting, so it is covered."* A discussion has no owner, no date and no evidence.
- *"The register is for the auditor."* It is for the next engineer, who will otherwise remove a guardrail without knowing why it exists.
- *"Writing it down makes us liable."* Not documenting a known risk is worse: it removes any argument that you acted reasonably.
- *"One risk, one line is enough."* Only if the line is specific about what happens and who does what next.

## How a student should understand it

**Mental model:** the incident book at a workshop — short entries, written when it happens, read by whoever is on shift next.

**Things they can do after this bullet:**
1. Write a four-part risk note for a concrete AI failure.
2. Turn a vague worry into a specific risk statement.
3. Add owner, residual risk and review date to an entry.

**Misconceptions to kill:** that discussion counts as documentation; that a risk without a mitigation is finished; that the register exists for auditors rather than for colleagues.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic's patient file.** A doctor's verbal handover is useful at 5pm and useless at 9am the next day. The file is what makes care continuous. A risk note is a handover to someone who was not in the room.

**The kitchen's temperature log.** Nobody reads it during service. It exists so that when something goes wrong, the owner can show what was checked and when. Where the analogy breaks: a temperature log records a number, whereas a risk note records a judgement.

### Worked example with a real tool

A support bot sometimes invents refund promises. Draft the note with the model, then have the room attack the draft for vagueness:

```
Write a risk register entry for this: our support chatbot sometimes
tells customers a refund has been approved when no refund exists.
Use these columns: risk statement, likelihood, impact, existing
control, residual risk, owner, review date.
Keep the risk statement to one sentence naming who does what and
what follows.
```

What to point at afterwards: the first draft's risk statement is usually a category ("hallucination risk"). Rewrite it on the board until it names the customer action and the business consequence. Then look at the mitigation: "improve the prompt" is not a control, and the room should say so.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask who in the room could prove, today, what risks their AI system carries. Let the silence sit.
2. **State the objective** — by the end, they can write a four-part note with an owner and a review date.
3. **Recall prior learning** — any incident report or near-miss form they have filled in.
4. **Present the content** — the four parts; specificity; residual risk; the register.
5. **Guide** — draft the refund-promise entry together.
6. **Elicit performance** — pairs write one entry from their own workplace, then swap.
7. **Give feedback** — mark three things: is the risk specific, is the mitigation a control, is there an owner.
8. **Transfer** — each learner adds one entry to their team's real register this week.

## What the framework doesn't mention but trainers need to know

- **Write for the person who inherits it.** The test of a good note is whether a new colleague could act on it without asking questions.
- **Keep the register short.** A fifty-row register nobody reads is worse than a twelve-row register reviewed monthly.
- **Link to evidence.** A transcript, a screenshot, a test case id. Claims without artefacts get argued about.
- **Personal data in the note is still personal data.** Describe the incident, not the customer; do not paste NRIC numbers into a risk log.

## Watch out

- **Do not model risk notes as long documents.** Learners stop writing them.
- **Do not accept "monitor it" as a mitigation** unless someone is named, with a threshold and a frequency.
- **Do not let severity language inflate.** If everything is critical, nothing is.
- **Retire the stale claim:** "we will document it at the end of the project". Risks found and not recorded are risks that reappear as incidents.
