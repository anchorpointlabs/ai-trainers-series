---
id: 09.03.A.A6
tsc: 9
level: Advanced
code: A6
title: Design and govern ethical AI systems
as_at: 2026-11-26
review_by: 2027-02-25
---

# Design and govern ethical AI systems

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A6**

> **Framework text (verbatim):** "Implement strategies for designing and governing ethical AI systems (e.g., integrate risk management into AI strategy)."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Ability · Bullet 12 of 12

**One-line version:** Governance is a set of gates with names on them — a decision, an artefact, an approver — repeated across the life of every AI system, not a slide at the end of a deck.

## What it is

Designing and governing ethical AI means building risk management into how AI work is chosen, built, tested and run. In practice that means defined checkpoints with required evidence and a named approver at each; an accountable owner per system; a chosen fairness measure rather than a vague commitment to fairness; oversight that a human can actually exercise; and a loop that continues after launch.

## Deep expansion

### The concept

Ethics becomes governance at the moment someone has to decide. "We value fairness" decides nothing. "For this credit model we optimise equal opportunity, we accept a disparate-impact ratio no lower than our stated floor, and the credit risk owner signs the trade-off" is a decision with a name attached, and it can be audited.

The enabling structure is a **gate lifecycle**: points at which work cannot proceed without a defined artefact. Five gates cover most organisations:

1. **Ideation** — is this use permitted at all? A short questionnaire against a prohibited list, plus a provisional risk tier.
2. **Design and data** — what data, on what lawful basis, for which population; which fairness metric; which oversight model.
3. **Pre-deployment** — model or system card, evaluation results, red-team findings, a verified kill switch.
4. **Limited deployment** — shadow or small-slice traffic, checking that the oversight interface works in practice and that disclosure and appeals exist.
5. **Production and retirement** — monitoring, scheduled re-validation, change triggers, and a defined decommissioning path with log retention.

Each gate needs three things or it is theatre: a required artefact, an approver with authority to say no, and a consequence for proceeding without it.

### The sub-concepts

**A named accountable owner.** Not a committee. One executive whose name is on the system, with the authority and the budget to fix it. Diffuse accountability is how organisations end up in tribunal arguing that the chatbot was a separate legal entity — an argument that has already failed in court, on the principle that a bot wearing your logo speaks with your voice.

**Fairness is a choice, not a measurement.** Several fairness definitions are mathematically incompatible: you can equalise approval rates across groups, or equalise the chance that a genuinely qualified person is approved, but not reliably both. Choosing which one a product optimises is an executive decision with distributional consequences, and it belongs in the design gate, written down.

**Oversight that is not rubber-stamping.** A human clicking approve four hundred times an hour is not oversight. Real oversight requires time per case, uncertainty information, the underlying evidence, authority to overrule without career penalty, and periodic checks that the human is still reading — including deliberately seeded errors.

**Tiering that is honest about asymmetry.** A meeting summariser and a credit decision should not pass through the same gate with the same effort. Tier by impact on people, autonomy of action, and scale.

**Contestability and redress.** Someone affected by an automated decision needs a route to a human with authority to change it, and a plain explanation of what drove the outcome. This is the part most programmes build last and regulators ask for first.

**Continuous governance.** A model certified in March is not certified in November: data drifts, providers change versions, adversaries adapt. Re-validation rhythm and change triggers are part of the design, not an operational afterthought.

### How it connects to the rest of the framework

K5 supplies the appetite and register the gates enforce. A5 writes the policies the gates apply. A3 owns the trust-and-safety metrics that show whether controls work in production. K1 and K4 supply the security evidence the pre-deployment gate demands. K3 defines the guardrail configuration the deployment gate checks. In the responsible-AI family, `08.03.A.K1` and `08.03.A.K3` cover ethical frameworks and the policy debates behind them.

### What is current as of November 2026

- **The management-system standard is certifiable.** ISO/IEC 42001 gives auditors something to certify, and procurement teams now ask for it, which turns governance from a claim into a document set.
- **Regulation differentiates by risk.** High-risk obligations, transparency duties for chatbots and synthetic media, and general-purpose model rules now sit alongside sector supervision in finance and healthcare; Singapore's voluntary Model AI Governance Framework sits on top of statutory data-protection enforcement.
- **Testable artefacts exist.** AI Verify and Project Moonshot give teams something to run at the pre-deployment gate rather than something to assert.
- **Frontier capability moves the gate.** Current frontier models make agentic action routine, so the oversight question shifts from "is the output good" to "was the action authorised".

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Ethics is the last slide."* If it is, it is a press release. It is a gate, an artefact and a signature.
- *"Human-in-the-loop makes it safe."* Only if the human has time, evidence, authority and attention — otherwise it is a signature machine.
- *"The framework is voluntary, so nothing applies."* The framework is voluntary; the data-protection, consumer-protection, sector and safety laws underneath it are not.
- *"Certification means done."* Certification describes a management system on a date. The system still drifts.

## How a student should understand it

**Mental model:** the building approval process — plan submitted, inspections at defined stages, occupancy permit, periodic fire certification. Nobody thinks the inspections are opposed to construction; they are what makes the building lettable.

**Things they can do after this bullet:**
1. Place the five gates on their own project and name the artefact each one requires.
2. Write the accountability sentence: system, owner, authority, review date.
3. Name the fairness metric a decision system will optimise, and who signs that choice.

**Misconceptions to kill:** that ethics is a final review, that a human in the loop is automatically an oversight, and that a certificate is a permanent state.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**COE, inspection and demerit points.** Ethics is the conviction that people should not be harmed on the road. Safety engineering is the airbag and the brake. Governance is the whole apparatus that lets a vehicle be driven fast without constant disaster: quotas, roadworthiness checks, pricing, licensing, penalties. Where it breaks: the state enforces traffic rules, while most AI governance is self-imposed until an incident makes it compulsory.

**Hospital triage at the A&E door.** A sprained ankle and a heart attack do not get the same team. Governance fails in two directions: treating every AI tool like a heart attack, which paralyses the business, or treating every tool like a grazed knee, which produces breaches. Tiering is the triage nurse.

### Worked example with a real tool

```
You are the AI governance lead for an insurer piloting a claims-triage assistant that
ranks incoming motor claims by suspected fraud and emails a recommendation to the
claims officer.

1. Assign a risk tier and justify it in two sentences.
2. For each gate — ideation, design and data, pre-deployment, limited deployment,
   production — name the one artefact that must exist to pass, and the role that
   signs it.
3. State the fairness metric this system optimises, and the concrete harm the
   alternative definition would create.
4. Describe the oversight in a way that would survive an auditor asking "how do you
   know the officer is reading?"
5. Name the change that forces re-entry to the pre-deployment gate.
```

What to point at afterwards: step three and step four. Learners want to say "we treat all claimants fairly"; push for the metric and the trade-off. And on oversight, the answer that satisfies an auditor is not "the officer reviews each case" but "we sample overrides, we seed known errors, and we measure whether they are caught".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a tribunal ruling holding a company liable for its chatbot's invented policy.
2. **State the objective** — design a five-gate governance path for one real system.
3. **Recall prior learning** — an approval process they already navigate (procurement, change advisory, safety).
4. **Present the content** — the gates, the artefacts, accountability, fairness choice, oversight design.
5. **Guide** — place the design and data gate for the claims assistant together.
6. **Elicit performance** — pairs write the pre-deployment gate and its signer.
7. **Give feedback** — challenge any artefact that cannot be checked and any signer without veto.
8. **Transfer** — each learner maps the gates onto their organisation's existing lifecycle.

## What the framework doesn't mention but trainers need to know

- **Gates fail when they are slow for low-risk work.** Fast-track the small cases in hours, or teams route around the process and governance loses legitimacy.
- **Shadow deployments are the real risk.** The system nobody registered is the one that reaches customers unreviewed; the register is the control.
- **Ethics committees without veto are advisory decoration.** Authority is the difference between governance and commentary.
- **Proportionality is a principle, not an excuse.** The justification for a low-friction path must be written down for each tier.
- **Decommissioning is a governance event.** Orphaned integrations and retained data outlive the model that created them.

## Watch out

- **Do not let the framework become a checklist of principles.** Principles without gates, artefacts and signatures change nothing.
- **Do not accept "the vendor handles ethics".** The vendor supplies a model; the deployment, the population and the consequences are yours.
- **Do not confuse transparency with explainability.** Telling users AI is involved is not the same as explaining why their claim was ranked high.
- **The stale claim to retire:** "governance slows delivery." As of November 2026 the organisations shipping fastest are the ones whose gates are automated, tiered and fast for low-risk work — the friction is concentrated where the harm is.
