---
id: 09.02.I.K4
tsc: 9
level: Intermediate
code: K4
title: Risk management frameworks and trust-and-safety best practice
as_at: 2026-11-26
review_by: 2027-02-25
---

# Risk management frameworks and trust-and-safety best practice

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Knowledge K4**

> **Framework text (verbatim):** "Best practices for maintaining AI trust and safety, including risk management frameworks (e.g., risk assessment matrix, bowtie analysis, agile risk)."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Knowledge · Bullet 4 of 10

**One-line version:** A framework is the difference between handling risk and remembering risk — it says who scores, who approves, what evidence is kept, and when it happens again.

## What it is

A risk management framework is the standing arrangement around risk assessment: the methods used (matrix, bowtie, agile risk), the tiers that decide how much control a system needs, the checkpoints in the project lifecycle where a decision is taken, the artefacts kept, and the cadence at which everything is reviewed. Trust-and-safety best practice is the operating layer on top: monitoring, incident response, moderation decisions and the review rhythm.

## Deep expansion

### The concept

Frameworks exist because good intentions do not scale past one team. The value is in three properties. **Repeatability**: two assessors reach roughly the same answer, so the outcome does not depend on who was in the room. **Traceability**: for any live system you can say what was assessed, when, by whom, what was decided, and on what evidence. **Proportionality**: the framework spends control effort where the risk is, instead of applying the same heavyweight process to a brochure bot and a payment agent.

That last property is the one learners most often miss. A framework that demands human approval for every message is not more secure; it is a framework that will be abandoned. Good frameworks define tiers with minimum controls, so the conversation moves from "should we do security" to "which tier is this, and have we met it".

For Singapore organisations the reference points are the PDPA obligations on protecting personal data, and the Model AI Governance Framework, whose logic — internal governance, human involvement in decisions, testing and monitoring, and communication with users — maps closely onto the bullets in this TSC. Trainers should name them without turning the class into a compliance lecture.

### The sub-concepts

**The three methods and when each fits.** The matrix ranks a portfolio of risks quickly. The bowtie analyses one well-defined event in depth, separating prevention from containment. Agile risk keeps assessment inside the delivery loop with short notes per increment. Most organisations need all three at different moments.

**Tiering.** Three tiers are enough: low (public content, no tools, human reads every output), medium (authenticated users, scoped read or low-impact writes, identity bound in code), high (untrusted inputs plus private data plus action-taking tools). Each tier carries a minimum control set; the assessment's job is to place the system honestly.

**Lifecycle checkpoints.** At least three: intake (is this use allowed, and at what tier?), pre-deployment (has the tier's control set been met and tested?), and periodic review (has anything changed?). The pre-deployment checkpoint is where the test evidence is actually read.

**Artefacts.** A register, a policy, a test plan with results, an incident log, and a change log for prompts and rules. Five artefacts; if any is missing, the framework is a rumour.

**Trust-and-safety operations.** A named queue for flagged content, an escalation route to a human decision-maker, a published standard for what is refused, and a public-facing response when the system gets it wrong.

**The cadence.** Weekly triage of flags, monthly review of block rates and refusals, quarterly review of the register and the policy, and event-driven review on any model, prompt or corpus change.

### How it connects to the rest of the framework

`TSC9-Intermediate-K3` supplies the scoring methods this framework schedules. `TSC9-Intermediate-A4` performs the comprehensive assessment the framework requires, and `TSC9-Intermediate-A6` runs the monitoring that keeps it honest. At Basic, `TSC9-Basic-K4` is the post-launch loop in miniature, and `TSC9-Basic-A2` is the single risk note the register is built from. At Advanced, `TSC9-Advanced-A6` embeds all of this into organisational AI strategy.

### What is current as of November 2026

Two forces have pushed frameworks from optional to expected. Procurement now asks suppliers for AI risk documentation, and regulators increasingly expect demonstrable governance rather than stated intent. Meanwhile the technical object being governed keeps moving: current frontier models ship as a continuously updated service, so "the system changed" is routine rather than exceptional.

- **Frameworks now need a version-change clause.** A quarterly review is too slow if the model moves monthly.
- **Agentic systems have made tiering the central skill.** The same model can sit in tier one or tier three depending on what it is wired to.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The framework is the documentation."* Documentation is the residue; the framework is the decisions and their cadence.
- *"More process means more safety."* Process beyond what the tier needs gets bypassed, and then nothing is followed.
- *"Compliance with PDPA is the whole obligation."* PDPA covers personal data. Security, fairness and content harm sit outside it.
- *"Trust and safety is a moderation filter."* Moderation is one control inside a system that also needs monitoring, escalation and review.

## How a student should understand it

**Mental model:** the building's fire-safety regime — alarms, drills, extinguishers, an appointed warden, and a log — not a single extinguisher by the door.

**Things they can do after this bullet:**
1. Place a system in a risk tier and name the minimum controls for that tier.
2. Name the three lifecycle checkpoints and what is decided at each.
3. Describe the operating cadence and who owns each review.

**Misconceptions to kill:** that a framework is paperwork; that heavier process is safer; that compliance with one law covers the whole obligation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The fire-safety regime.** Singapore buildings do not rely on one extinguisher. There is an alarm system, a warden, a drill schedule, a log book and an annual inspection. Each element is cheap; the regime is what saves lives. Where it breaks: fire risk is well understood and stable; AI risk changes with every release.

**The hawker centre grading.** An A, B or C grade tells you what standard was met and when it was checked. Tiering an AI system should feel like that: a published standard, an assessment, a visible outcome.

### Worked example with a real tool

Use the model to draft the regime, then prune it with the room:

```
We run three AI systems: a public FAQ bot with no tools, an internal
HR assistant that reads resumes, and a finance agent that can raise
purchase orders up to $5,000.

For each: assign a risk tier, list the minimum controls, name the
lifecycle checkpoints, and say what evidence we should keep.
Then tell me which of your own recommendations is over-engineered
for the tier and should be dropped.
```

What to point at afterwards: the model will happily propose human approval on every message for the FAQ bot. Pruning that is the exercise — proportionality is the skill, and learners should be able to defend what they dropped.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask who can name the person accountable for the last AI system their organisation deployed. Let the pause do the work.
2. **State the objective** — by the end, they can tier a system, name its checkpoints and describe the review cadence.
3. **Recall prior learning** — any ISO-style or safety regime they have worked under.
4. **Present the content** — repeatability, traceability, proportionality; tiers; checkpoints; artefacts; cadence; PDPA and Model AI Governance Framework as reference points.
5. **Guide** — tier the three systems together and prune the over-engineering.
6. **Elicit performance** — groups write a one-page regime for one system.
7. **Give feedback** — check for an owner, a cadence and evidence, in that order.
8. **Transfer** — each learner maps their organisation's current practice against the five artefacts.

## What the framework doesn't mention but trainers need to know

- **Accountability needs a name, not a department.** "IT is responsible" means nobody is.
- **Frameworks fail at version change.** Write the change-trigger into the framework or the review will lag the deployment.
- **Small organisations can run a light regime.** A register, a tier per system, a pre-launch test and a quarterly look will pass most scrutiny and cost a few hours a month.
- **The board question is different from the engineer's.** Have an answer ready in one slide: what can go wrong, what we did, what we watch.

## Watch out

- **Do not teach frameworks as certificates.** The certificate is not the control.
- **Do not let tiering become flattery.** Teams will place systems lower to avoid controls; the four axes are there to make that hard.
- **Do not ignore the public-facing obligation.** A trust-and-safety regime that never talks to users about a failure is not trusted.
- **Retire the stale claim:** "we review AI risk annually." In November 2026 the model underneath you may change before the next review.
