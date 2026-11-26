---
id: 05.02.I.K8
tsc: 5
level: Intermediate
code: K8
title: "Ethics is part of the test: the frameworks that constrain evaluation"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Ethics is part of the test: the frameworks that constrain evaluation

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K8**


> **Framework text (verbatim):** "Ethical frameworks and guidelines for responsible AI evaluation."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 8 of 12

**One-line version:** The ethical frameworks do not sit after the evaluation — they decide what the evaluation must cover, what it must disclose, and what it must refuse to ship even when the score is good.

## What it is

Ethical frameworks for AI evaluation are the external standards — Singapore's IMDA and PDPC governance frameworks, the OECD principles, UNESCO's recommendation, the NIST risk management framework, ISO/IEC 42001, and the EU AI Act's risk tiers — that specify what an evaluation of a generative system must address beyond quality. In practice they convert into design requirements: what to test, how to document it, who must be able to see it, and which uses are out of bounds regardless of performance.

## Deep expansion

### The concept

A quality evaluation asks "does this work". An ethical evaluation asks "for whom, at whose expense, and who can find out". Those are different questions with different methods, and the frameworks exist because the second set is the one that gets skipped when a deadline is close.

The frameworks are also not interchangeable. Some are principles (OECD, UNESCO) that shape reasoning; some are management-system standards (ISO/IEC 42001) that shape process; some are regulatory obligations with penalties (the EU AI Act's risk-tiered duties) that shape what may be deployed where. A Singapore organisation typically works with the local governance frameworks as its operating posture, the international principles as its vocabulary, and jurisdiction-specific rules where it sells abroad. Teaching them as one undifferentiated "ethics" blob is the most common error in this area.

### The sub-concepts

**The frameworks and what each is for.** IMDA's Model AI Governance Framework (internal governance and the four pillars of explainability, fairness, robustness, accountability) and the Generative AI Governance Framework extend to the specific risks of generative systems — hallucination, copyright and provenance, and the difficulty of evaluation itself. AI Verify and its ecosystem provide a testing toolkit and a common language for reporting. The OECD principles and UNESCO's recommendation supply the ethical vocabulary. NIST's AI RMF supplies a risk-management structure. ISO/IEC 42001 supplies a certifiable management system. The EU AI Act supplies tiered obligations for the highest-risk uses.

**Proportionality.** The depth of evaluation should scale with the impact on people. A tool that drafts internal meeting notes needs less evidence than one that triages housing applications. Frameworks express this differently; the practical translation is a risk tier per use case, agreed before the build.

**Provenance, consent and disclosure.** Where did the evaluation data come from, were the people in it told, and are users told they are dealing with a model? The evaluation cannot answer these questions, but it must record that they were asked.

**Documentation as a deliverable.** A model card or system card with disaggregated results, known limitations and the conditions under which the system should not be used is an evaluation artefact in its own right. It is also the artefact a procurement team will actually read.

**Independent scrutiny.** Third-party testing, red-teaming and internal audit with a route to the people who can stop the deployment. Self-assessment alone rarely survives an incident.

**Refusal and escalation.** Some uses are excluded regardless of score: decisions with irreversible personal consequences made without human review, covert manipulation, surveillance of identifiable people. The framework does not always say so bluntly; the ethics review must.

**Who is in the room.** Affected groups, frontline staff and the people who will absorb the failures are part of the evaluation's design, not its audience. An evaluation of a service for elderly residents that never involved an elderly resident has a coverage problem the metrics cannot show.

### How it connects to the rest of the framework

`TSC5-Intermediate-K5` is the measurement half of fairness and explainability; `A4` is the mitigation half; this bullet is the authority that makes both non-optional. `K4` supplies the rubric, whose gates should be derived from these frameworks rather than invented. `TSC8-*` (Responsible AI and Generative AI Practices) is the organisational sibling, and `TSC9-*` covers security and adversarial ethics. `TSC5-Basic-K6` is the entry-level version: ethical considerations in development and deployment.

### What is current as of November 2026

Singapore's posture has settled on "test it, document it, disclose it": the Generative AI Governance Framework is used by enterprises as a practical checklist, AI Verify provides a shared testing vocabulary, and procurement increasingly asks for evidence rather than assurance. Globally the picture diverges — the EU's tiered obligations, sectoral US rules and labelling requirements in several Asian markets mean "compliant" is a jurisdiction-specific claim, not a property of a system. Within evaluation practice the visible shift is that disclosed limitations have become a trust signal: vendors who publish disaggregated failure modes are treated as more credible than those who publish only strengths.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Ethics is a policy document signed at the end."* Policy without an evaluation artefact behind it is a claim, and claims are what incidents dismantle.
- *"If it's legal, it's ethical."* Law is a floor set after the harm was understood; several well-documented failures were entirely legal.
- *"Our framework is the only one."* Frameworks overlap heavily in substance and diverge in enforcement. Know which one binds you and which one persuades.
- *"Ethics slows delivery."* Undisclosed bias, a copyright claim or a regulator's letter slows delivery far more.

## How a student should understand it

**Mental model:** the food-hygiene grade displayed at the stall, not filed in a drawer. The test is public, the standard is written down, and the grade changes what customers do — which is why the stall cares.

**Three things they can do after this bullet:**
1. Map a use case against a named framework and produce a gap list.
2. Set the risk tier and the corresponding depth of evaluation before the build starts.
3. Write the limitations section of a model card so that it would survive a hostile reader.

**Misconceptions to kill:** ethics happens at the end, compliance equals ethics, and one framework covers every market.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food-hygiene grade.** A letter on the wall, from an inspector with a published checklist, that customers act on. It works because it is standardised, visible and enforced. Now notice its limitation: it tells you the kitchen is clean, not that the food is fair to the people who cook it.

**The fire-safety certificate.** You do not self-certify a building. An independent party inspects, signs, and the certificate is a precondition for occupancy. High-risk AI use is heading the same way, and some markets have already arrived.

### Worked example with a real tool

Run the gap analysis on a real (or realistic) use case:

```
We want to deploy an AI assistant that drafts replies to housing-loan
enquiries, including rejections. It will be used by 40 staff.

Act as a governance reviewer. Using Singapore's Model AI Governance
Framework and the Generative AI Governance Framework as the reference:

1. What risk tier is this, and why?
2. What must our evaluation cover beyond reply quality?
3. What must we document before deployment, and for whom?
4. What should we refuse to automate here, regardless of the score?
5. Produce a gap list as a table: requirement | evidence we have | missing.
```

What to point at afterwards: the reply-quality section is the shortest part of the output. The gaps are almost always disclosure, disaggregated fairness evidence, a human-review route for rejections, and a named accountable owner. That list is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out a two-line incident: a model declined applications with no explanation and no appeal route. Ask which framework requirement was missed.
2. **State the objective** — you will map one use case onto a named framework and produce a gap list.
3. **Recall prior learning** — Basic K6 on ethical considerations; ask what evidence they produced then.
4. **Present the content** — the frameworks and their different jobs; proportionality; provenance and disclosure; documentation; independent scrutiny; refusal.
5. **Guide** — run the housing-loan gap analysis together and rank the gaps by consequence.
6. **Elicit performance** — each team maps their own use case and proposes the risk tier.
7. **Give feedback** — challenge tiers set too low, and documentation that lists only strengths.
8. **Transfer** — they draft the limitations section of a model card and bring it for peer review.

## What the framework doesn't mention but trainers need to know

- **Frameworks are written for organisations, not for evaluators.** Your job is translation: which clause becomes which test, owned by whom, evidenced by which artefact. Keep that mapping in a table or it stays a poster.
- **Documentation is the deliverable that outlives the project.** The people who inherit the system will have the model card and nothing else. Write for them.
- **Ethics review needs a stop authority.** An evaluation that can only recommend is decoration. Somebody must be able to say no, and that must be known in advance.
- **Local context is not a detail.** Multilingual service, an ageing population, a small market with high trust in public institutions — these change what "fair" and "harmful" mean here, and the international frameworks will not tell you.

## Watch out

- **Do not teach ethics as a list of prohibitions.** Learners leave able to recite and unable to evaluate. Anchor everything to an artefact they must produce.
- **Do not present one jurisdiction's rules as universal.** Say which framework binds the learner, which persuades, and where they diverge.
- **Do not let the room treat a signed policy as evidence.** Ask for the test, the sample, the result and the date.
- **The stale claim to retire:** "responsible AI is a communications problem." It is an evaluation and documentation problem with a communications symptom.
