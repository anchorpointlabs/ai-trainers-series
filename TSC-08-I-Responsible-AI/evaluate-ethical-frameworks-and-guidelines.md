---
id: 08.02.I.A7
tsc: 8
level: Intermediate
code: A7
title: Evaluate ethical frameworks and guidelines
---

# Evaluate ethical frameworks and guidelines

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A7**

> **Framework text (verbatim):** "Evaluate ethical frameworks and guidelines in AI development."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 12 of 14

**One-line version:** A framework earns its place only if it changes a decision someone was about to make — everything else is a wall poster with a diagram.

## What it is

Evaluating a framework means judging whether it will actually govern work in your context: does it name specific checks, owners and thresholds; does it cover the risks that matter for this system; can it be enforced; and can a team use it on a Tuesday afternoon. The output is a recommendation, not a critique.

## Deep expansion

### The concept

There are three species of document, and learners routinely confuse them. A **value statement** says what the organisation believes ("we are committed to fairness"). A **framework** provides structure: principles, operational areas, controls and suggested evidence. A **standard** specifies auditable requirements an independent body can inspect (ISO/IEC 42001).

Only one of the three can fail a build. Evaluating means asking which species you are holding, and whether it is the one your situation needs.

The evaluation criteria are stable, which is what makes this teachable. **Specificity**: does it name checks, roles, thresholds, artefacts? **Coverage**: does it address your actual risks — bias, privacy, transparency, agents, supply chain, sustainability? **Enforceability**: what happens if a team ignores it — nothing, a contractual term, or a regulator? **Operability**: can a squad apply it in a sprint, or does it require a governance function? **Evidence**: what artefact proves compliance, and can you produce it? **Fit**: jurisdiction, sector, size, maturity.

The honest answer for most organisations is a combination: a voluntary framework for structure, a standard for auditability, and the law for the floor. "Which one is best" is the wrong question; "which combination covers my risk at a cost I can carry" is the right one.

### The sub-concepts

**Specificity is the test that catches most bad frameworks.** "Be fair" cannot be failed. "Disparate impact ratio must be at least 0.80 across protected groups, reviewed quarterly, signed by the model owner" can.

**Coverage must be checked against your system, not in the abstract.** A framework with excellent fairness guidance and nothing on tool-using agents is incomplete for the thing you are building this quarter. Map the framework's dimensions against your risk register and look at the gaps.

**Enforceability is a spectrum**, and being honest about where you sit is the professional move. Guidance + procurement clause + audit + regulator are four different strengths of enforcement, and most organisations rely on the middle two.

**Operability decides whether it is used.** A 60-page framework with no templates will be summarised into a slide, and the slide is what people follow. Ask what the framework gives a team that has to ship on Friday.

**Evidence requirements reveal intent.** Frameworks written to be enforced specify artefacts. Frameworks written to be published specify aspirations.

**Fit is not a weakness.** A framework designed for a large bank may be unusable for a 40-person SME, and the sector overlay (financial, health) usually matters more than the general guidance.

### How it connects to the rest of the framework

`TSC8-Intermediate-K5` supplies the frameworks themselves, including Singapore's model frameworks and the legal floor. `TSC8-Intermediate-A1` and `TSC8-Intermediate-A8` are the application and integration steps that depend on this evaluation. `TSC8-Intermediate-K4` connects through evidence: a framework that requires model cards is only useful if your organisation can produce them.

### What is current as of November 2026

Three developments have changed how frameworks are evaluated in practice. ISO/IEC 42001 has become the reference point procurement teams compare against, because it can be certified by an independent auditor. The EU AI Act has made parts of the landscape binding for high-risk systems and for general-purpose models, with phased application, which means framework evaluation now includes a jurisdiction question even for Singapore firms selling into Europe. And agentic capability has outrun most guidance: the current generation — GPT-6 (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — all support tool use, while most frameworks still describe a model that answers questions.

Singapore's own instruments remain the cheapest credible starting point: the IMDA frameworks are readable, sector-aligned, and paired with AI Verify and Project Moonshot tooling that turns their testing dimension into evidence.

### Common misconceptions

- *"The most well-known framework is the best one."* Familiarity is a proxy for legitimacy, not for fit.
- *"More principles means stronger governance."* Twelve unenforceable principles govern less than three enforceable controls.
- *"A framework is a policy document."* A policy states intent; a framework should specify controls.
- *"We adopted a framework, so we are covered."* Adoption is a decision. Operation is evidence.

## How a student should understand it

**Mental model:** a map with roads marked versus a poster of a map. Both show the shape of the territory; only one gets you to the address.

**Things they can do after this bullet:**
1. Classify a document as a value statement, a framework or a standard.
2. Score a framework against the six criteria for a specific system.
3. Recommend a combination — guidance, standard, law — with the gaps named.

**Misconceptions to kill:** that popularity equals quality, that principles equal controls, and that adoption equals compliance.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The recipe with no quantities.** "Add flour, sugar and butter, bake until done." It reads like a recipe and cannot be followed. A framework that says "ensure fairness" is the same document. Where it breaks: a bad recipe wastes an afternoon; a bad framework wastes a compliance budget and gives false assurance.

**The condo brochure versus the floor plan.** "Resort lifestyle living" is a value statement. The floor plan tells you whether the bed fits. Ask which document you would use to decide whether to buy. Where it breaks: buyers of frameworks can be sold on the brochure, because the failure shows up years later.

### Worked example with a real tool

```text
A bank is choosing a framework for a loan-scoring model that must also satisfy
MAS expectations and PDPA obligations.

Here is the candidate's entire text: "The organisation shall ensure its AI systems are
fair and transparent, and shall act ethically at all times."

Evaluate it against specificity, coverage, enforceability, operability, evidence and fit.
Score each 1-5 with a reason. Then tell me what a usable version of this framework
would have to contain for this model, and name the instruments I should combine instead.
```

What to point at afterwards: the model scores specificity and evidence near the bottom and then writes a competent replacement — which is the teaching moment, because a chatbot can draft a better framework than the one the organisation adopted. Point at the combination recommendation: MAS FEAT plus PDPA plus a recognised management standard is the realistic answer.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read two framework extracts aloud; ask which one could fail a review.
2. **State the objective** — by the end you can evaluate a framework and recommend a combination.
3. **Recall prior learning** — revisit the legal floor versus ethical ceiling idea.
4. **Present the content** — three species, six criteria, enforcement spectrum, combination logic.
5. **Guide** — score the one-line framework together.
6. **Elicit performance** — groups evaluate the framework their own organisation claims to use.
7. **Give feedback** — challenge any score with no evidence attached.
8. **Transfer** — each learner writes a one-paragraph recommendation for their unit.

## What the framework doesn't mention but trainers need to know

- **Frameworks are political documents.** They are negotiated between regulators, industry and civil society, and the omissions are usually deliberate. Teach the omission, not just the text.
- **The missing dimension is usually incentives.** Almost no framework tells you to stop measuring a team on shipping speed, which is the cause of most bypass.
- **Certification is a snapshot.** An ISO certificate says the management system existed at audit time, not that the model is safe today.
- **Choose the smallest set that covers your risk.** Adding frameworks adds cost and rarely adds control.

## Watch out

- **Do not teach framework-shopping** as if the goal were to find the easiest one to satisfy.
- **Do not equate certification with safety.** Say both halves of the sentence.
- **Do not let the room conclude all frameworks are useless.** The conclusion is: demand specificity, or write it yourself.
- **The stale claim to retire:** "there is no regulation, so we self-regulate." In November 2026 the binding layer exists, and the voluntary layer is how you demonstrate reasonableness under it.
