---
id: 05.03.A.K5
tsc: 5
level: Advanced
code: K5
title: "The rulebook an evaluation must survive: ethical frameworks and data privacy"
as_at: 2026-11-26
review_by: 2027-02-25
---

# The rulebook an evaluation must survive: ethical frameworks and data privacy

> **TSC #5 Generative AI Model Evaluation · Advanced · Knowledge K5**


> **Framework text (verbatim):** "Ethical frameworks and guidelines relevant to AI development (including global standards or frameworks for data privacy)."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Knowledge · Bullet 5 of 13

**One-line version:** Every evaluation is a data-processing activity, and the rules were written for a world where test data was a spreadsheet, not a transcript of someone's worst week.

## What it is

This bullet covers the external rulebook that constrains how a generative system may be built, tested and evidenced: international principles (the OECD AI Principles, the UNESCO Recommendation on the Ethics of AI), management-system standards (NIST's AI Risk Management Framework, ISO/IEC 42001), Singapore's Model AI Governance Framework with the AI Verify testing toolkit, and the data-protection law governing what may be put into a test set — principally the PDPA here, and the GDPR where European data is involved.

## Deep expansion

### The concept

Learners expect a list to memorise. It is better taught as **obligations attached to artefacts**, because that is how it behaves in a project. An evaluation has four artefacts that carry obligations: the **test data**, the **prompts**, the **outputs** and the **report**. Test data is usually the most sensitive asset in the building, because a good evaluation set is made of real cases, and real cases contain names, account numbers, health details and complaints. Prompts and outputs travel — into vendor APIs, into logs, into slides. The report is read by someone outside the team and may end up in a dispute.

The privacy questions that matter in practice are narrow and more useful than a summary of the legislation. **What is the lawful basis for using this text?** "It was in our systems" is not one. **What is the minimum needed?** Most items can be reduced to the shape of the case with identifiers removed — which also stops the model scoring the name instead of the argument. **Where does it go?** Sending a test set to an API is a transfer to a processor; retention defaults, training-on-data defaults and regional processing all have to be checked, not assumed. **How long is it kept?** Eval sets age, and retention limits are also a defence against contamination.

### The sub-concepts

**Principles versus standards versus law.** OECD and UNESCO are normative; ISO/IEC 42001 and NIST are management systems you can audit against; the PDPA and GDPR are enforceable, with penalties. Blurring the three produces learners who cannot tell a recommendation from a requirement.

**Assurance toolkits.** AI Verify and its generative AI evaluation work (Project Moonshot) give a practical route from principle to test — adversarial prompt sets, harnesses, a reporting structure. Useful because it makes "responsible" operational.

**Anonymisation versus pseudonymisation.** Removing names is not anonymisation if the remaining combination re-identifies. In small populations — one branch, one rare condition — re-identification is easy and the set must be handled as personal data.

**Purpose limitation.** Data collected to serve a customer may not automatically be used to evaluate a model. The second use needs its own justification.

**Transparency.** If outputs reach customers they may need to know; if the model contributed to a decision about them, the explanation obligation in `05.03.A.K2` becomes legal rather than a design nicety.

### How it connects to the rest of the framework

`05.02.I.K8` is the same material at Intermediate level; this bullet is about interpreting it for a programme you are accountable for. `05.03.A.K6` takes the interdisciplinary view where this one takes the formal instruments, and `05.03.A.A7` is the advocacy obligation that follows. `TSC8` and `TSC9` carry the operational responsible-AI and security controls an evaluation must itself comply with.

### What is current as of November 2026

Two shifts. Assurance has become a procurement requirement: buyers ask vendors for evaluation evidence, and a vendor that cannot produce its judge, rubric and slice table loses the deal — pushing frameworks out of the policy team and into the sales cycle. And the practical centre of gravity has moved from principles to **records**: model cards, evaluation reports, provenance logs, audit trails. The frameworks themselves have not changed much; the expectation that you can show your working has.

### Common misconceptions

- *"If the data is anonymised, PDPA does not apply."* Anonymisation is a high bar. Pseudonymised records with distinctive details are still personal data.
- *"Public data is free to use."* Publicly visible is not licensed for training or evaluation, and it is not consented.
- *"Ethics is the compliance team's job."* They own the policy; the evaluation team owns the test set, prompts and report, which is where the exposure sits.

## How a student should understand it

**Mental model:** the food-hygiene inspection, not the recipe. Nobody inspects whether your laksa is delicious; they inspect surfaces, temperatures and records — and the grade is withdrawn if you cannot show them.

**Three things they can do after this bullet:**
1. Map each artefact of an evaluation to the obligation it carries and the control that satisfies it.
2. Decide whether a proposed test set is personal data, and defend the answer.
3. Tell a principle from a standard from a law, and say which one binds them here.

**Misconceptions to kill:** that anonymisation is a checkbox, that public means free, and that frameworks are law.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic queue.** A polyclinic can use your records to treat you. Using the same records to test a triage model is a different purpose needing a different justification — even though the file is already in the building. It breaks because clinical data has its own stricter regime; the general rule is looser, not tighter.

**The food-hygiene grade.** The stall is judged on process and records, not taste, and the grade is displayed for customers who cannot inspect the kitchen. AI assurance is heading the same way: a rating you publish, backed by an inspection you can produce on request.

### Worked example with a real tool

A team wants to build an evaluation set from 50 real complaints. Draft the data plan, then attack it. Paste this into Claude:

```
We want a 50-item eval set from real CRM complaints, to test a reply-drafting
assistant. Singapore company, PDPA applies. The model is called through a vendor API
whose retention setting we have not checked.

Draft a one-page data handling plan covering: (1) lawful basis for this secondary
use and what to confirm with our DPO; (2) what to remove or generalise from each
complaint, and re-identification risks in a company with ~2,000 customers; (3) what
must be true of the vendor contract before text leaves our network; (4) retention for
the eval set and the prompt/output logs, and who approves it; (5) what may appear in
the final report without further approval.

Then list the three weakest assumptions in your own plan.
```

What to point at afterwards: the last instruction. Learners accept the first draft as authoritative; making the model critique its own plan is the habit that matters. Then point at item 2 — in a 2,000-customer base, removing the name is nowhere near enough.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out a plausible eval item built from a real complaint, then ask who has just seen personal data.
2. **State the objective** — learners can map an evaluation's four artefacts to obligations and name the control for each.
3. **Recall prior learning** — the Intermediate fairness and explainability material; where does the duty to explain come from?
4. **Present the content** — principle versus standard versus law; the four artefacts; minimisation, retention, transfer, notice.
5. **Guide** — build the data plan together, leaving the DPO question visibly unanswered.
6. **Elicit performance** — pairs apply it to one of their own datasets and list what they must stop doing today.
7. **Give feedback** — debrief the gaps: no retention period, no vendor check, no rule for the report.
8. **Transfer** — each learner names one control they will put in place before the next run, and who signs it off.

## What the framework doesn't mention but trainers need to know

- **The DPO is a stakeholder, not a gatekeeper.** Bring the plan before the data moves; a late review is a rewrite.
- **Vendor retention defaults are the commonest leak.** Most APIs have a training-on-data default that has to be switched off contractually, not in a settings page.
- **Small populations break anonymisation.** An eval set drawn from a few thousand customers, one branch or one rare condition should be treated as identifiable.
- **Reports leak.** A quoted failure example with a name or a distinctive circumstance is a disclosure even when the aggregate is fine.

## Watch out

- **Do not teach the frameworks as a memorisation list.** Nobody has been saved by reciting the OECD principles; they are saved by knowing which artefact is exposed.
- **Do not say "compliant" on the basis of a framework.** That word belongs to legal and audit, and loose use gets quoted back in a dispute.
- **Do not demo with real customer data in a public model.** Use a synthesised or heavily altered case, and say out loud that you have.
- **Do not skip retention.** It is the cheapest control and the one most often missing.
- **The stale claim to retire:** "we will handle privacy at deployment." The test set is the exposure, and it exists months before deployment.
