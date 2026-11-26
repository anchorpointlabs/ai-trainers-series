---
id: 09.03.A.K5
tsc: 9
level: Advanced
code: K5
title: Enterprise risk management frameworks
as_at: 2026-11-26
review_by: 2027-02-25
---

# Enterprise risk management frameworks

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K5**

> **Framework text (verbatim):** "Enterprise risk management frameworks."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Knowledge · Bullet 5 of 12

**One-line version:** Enterprise risk management is the organisation's existing habit of naming risk, pricing it and reporting it upward — and AI risk only becomes managed on the day it gets a row in that same register.

## What it is

Enterprise risk management (ERM) is the system by which an organisation identifies risk across all its activities, decides how much of each it will carry, assigns an owner, sets controls, and reports the residual to the board. An AI risk framework is the same discipline applied to models: a register, a tiering rule, an appetite statement, named owners, and a reporting rhythm.

## Deep expansion

### The concept

The mistake almost every organisation makes first is treating AI risk as a technology problem owned by the engineering team. It is not, for one structural reason: the decisions that must be made about AI risk are business decisions. How much reputational damage will we accept from a chatbot that insults a customer? Will we accept a small probability of a wrong credit decision in exchange for speed? Those are appetite questions, and appetite lives with the board, not with the person who deployed the endpoint.

ERM supplies the machinery that makes those questions answerable rather than rhetorical:

- **A register** — one row per system, so nobody has to remember what exists.
- **A tiering rule** — how much scrutiny a system gets, decided by impact and autonomy rather than by enthusiasm.
- **An appetite statement** — what loss is tolerable, in words a board will sign.
- **An owner** — a named human, not a committee, accountable for the residual.
- **A reporting rhythm** — what reaches the risk committee, how often, and what triggers escalation.

What changes for the learner is the unit of analysis. They stop asking "is this model safe?" and start asking "what does this system expose us to, who owns that exposure, and does it fit inside what we said we would carry?"

### The sub-concepts

**Tiering before controls.** Prohibited (not built at all), high (consequential decisions about people — credit, employment, medical triage, essential services), limited (customer-facing generation and recommendation), minimal (internal productivity with human review). Controls are then proportionate: a meeting-summariser must not face the same gate as a credit model.

**Appetite expressed as a number or a threshold.** "Zero tolerance for unconsented personal data in training" and "no automated credit rejection without an explainable model" are appetite statements. "We take AI risk seriously" is not.

**Three lines of defence.** The build team owns the risk; an independent function — model risk management, or a governance lead reporting to the risk officer rather than the product chief — challenges it and can veto; internal audit checks that both lines actually work. Without the second line, teams grade their own homework.

**Frameworks worth naming.** NIST's AI Risk Management Framework organises the work into govern, map, measure and manage, and its generative-AI profile adds the GenAI-specific failure modes. ISO/IEC 42001 is the certifiable management-system standard, the AI equivalent of an information-security management system. Both are structures for the register and the controls, not substitutes for judgement.

**Residual risk, not absolute risk.** After controls, something remains. The register records that remainder with an owner, a review date, and a decision: accept, reduce further, transfer (insurance or contract), or avoid.

**Reporting that means something.** A quarterly view of tier, incidents, control failures, overdue actions and accepted risks — short enough that the committee reads it.

### How it connects to the rest of the framework

K1 supplies the security methodology whose results feed the register. K6 makes the residual quantitative. A5 writes the policies that the register enforces. A6 designs the gates where the register is consulted. A3 owns the trust-and-safety metrics that are, in ERM terms, control effectiveness measures. At Intermediate level `09.02.I.K3` and `09.02.I.K4` cover risk assessment methods and frameworks in practice.

### What is current as of November 2026

- **The management-system standard is real.** ISO/IEC 42001 certification is now something enterprises ask vendors for, which turns "we have a framework" into an auditable claim.
- **Regulation has teeth somewhere.** The EU AI Act's high-risk obligations and its general-purpose model rules reach any provider whose output is used in the EU, and Singapore's PDPA carries statutory penalties — including a share of annual turnover — for personal-data failures, so the voluntary Model AI Governance Framework sits on top of enforceable law rather than replacing it.
- **Sector rules lead.** Financial institutions work to MAS's fairness, ethics, accountability and transparency expectations; clinical AI falls under device regulation. Sector supervisors move faster than horizontal regulators.
- **Agents changed the risk shape.** A system that can act has an availability and authorisation risk profile that a content-only register misses, so entries now need a tool inventory and a spend cap.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"AI risk is a technical problem."* The technical controls are one input; the decisions are business decisions with a named human owner.
- *"ERM is paperwork."* A register nobody updates is paperwork. A register that blocks a launch or prices an insurance policy is management.
- *"The vendor owns the risk."* The vendor owns its model. You own what your deployment does to your customers, and regulators treat it that way.
- *"Voluntary framework, so no consequences."* The framework is voluntary; the data-protection, consumer-protection and sector laws underneath it are not.

## How a student should understand it

**Mental model:** the same filing cabinet the finance director uses for currency and counterparty risk, with an AI drawer in it — same owner, same appetite, same quarterly review.

**Things they can do after this bullet:**
1. Write one register row for a system they know: tier, owner, data, controls, residual, review date.
2. Draft an appetite sentence a board could actually sign.
3. Say which line of defence they sit in, and what that line may veto.

**Misconceptions to kill:** that AI risk belongs to IT, that a framework is a document rather than a set of decisions, and that using a vendor transfers accountability.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**COE, VICOM and the demerit system.** Ethics is the belief that people should not die on the road. Safety engineering is the airbag. Governance is the whole apparatus — COE quotas, roadworthiness inspection, ERP pricing, demerit points, licensing. You can drive at 90 km/h on the expressway *because* that apparatus exists, not despite it. Where it breaks: traffic rules are enforced by the state, while AI governance is largely self-imposed until something goes wrong.

**The office fire-insurance renewal.** Someone walks the building, notes the risks, sets a deductible, and signs. Nobody calls that bureaucracy until the fire happens.

### Worked example with a real tool

Turn a vague risk into a register row:

```
You are the risk partner for a retail bank.

Proposal: a customer-facing assistant that answers questions about the customer's own
transactions, can email a summary, and can raise a dispute ticket.

Produce one enterprise risk register row with these fields: system purpose, risk tier
and why, data sensitivity, agency level, named owner (role, not person), top three
failure modes, preventive controls, detective controls, residual risk statement,
appetite decision (accept / reduce / transfer / avoid), review date, and the one
metric that would tell us the controls stopped working.
```

What to point at afterwards: the model will fill the row plausibly, and learners will notice how many fields require a human decision — tier, appetite, owner. That is the lesson: ERM is a decision structure, and the model can only draft it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a board paper that says "AI risk: medium" with no owner and no number.
2. **State the objective** — produce one complete register row and one appetite sentence.
3. **Recall prior learning** — how their organisation already records operational or vendor risk.
4. **Present the content** — register, tiering, appetite, three lines, residual risk, reporting.
5. **Guide** — tier the retail assistant together and argue the boundary case.
6. **Elicit performance** — pairs complete the row for a system they know.
7. **Give feedback** — hunt for rows with no owner, no metric, or an appetite with no threshold.
8. **Transfer** — each learner proposes where the register should live and who reviews it.

## What the framework doesn't mention but trainers need to know

- **The register is a political artefact.** Whoever controls the tiering rule controls how much friction a project meets; write the rule down before the first disputed case.
- **Aggregation hides concentration.** Twenty low-risk assistants on one vendor's API is one high-risk dependency.
- **Appetite without a metric is a slogan.** Every appetite statement needs the measure that would show it has been breached.
- **Incidents belong in the same register as projects.** Otherwise lessons are learned in one process and applied in none.
- **Decommissioning is a risk event.** Retired models leave orphaned integrations and retained data; the framework should say who signs that off.

## Watch out

- **Do not let the framework become the deliverable.** A certified management system with no veto power is decoration.
- **Do not score risk in averages.** A single severe outcome is not offset by many harmless ones.
- **Do not present frameworks as interchangeable.** NIST organises the work, ISO certifies the system, and sector rules bind; a trainer who says "just use NIST" will confuse a bank's risk officer.
- **The stale claim to retire:** "AI governance is a compliance exercise." As of November 2026 it is risk management with a budget line, an owner and, increasingly, an audit opinion.
