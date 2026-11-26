---
id: 08.03.A.K1
tsc: 8
level: Advanced
code: K1
title: Ethical frameworks and global standards
as_at: 2026-11-26
review_by: 2027-02-25
---

# Ethical frameworks and global standards

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Knowledge K1**

> **Framework text (verbatim):** "Ethical frameworks and guidelines relevant to AI development (including global standards or frameworks for data privacy)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Knowledge · Bullet 1 of 14

**One-line version:** A framework is a promise you can audit; a standard is the version of that promise your market holds you to.

## What it is

An ethical framework states the values an AI system should serve — fairness, accountability, transparency, human oversight — and the practices that turn those values into decisions. A standard is the same content written so a third party can check it. Global standards matter because models cross borders while organisations stay put: one product may have to satisfy Singapore's PDPA, the EU AI Act and a customer's ISO certification at once.

## Deep expansion

### The concept

Frameworks arrive in three layers, and learners blur them constantly. The **principle layer** is prose: the OECD AI Principles, the UNESCO Recommendation, the ASEAN Guide, Singapore's IMDA Model AI Governance Framework. It supplies vocabulary and is not enforceable by itself. The **management-system layer** is process: ISO/IEC 42001 (impact assessment, risk treatment plan, 38 controls across nine domains), ISO/IEC 23894, and the NIST AI RMF with its four functions — GOVERN, MAP, MEASURE, MANAGE. This is what an auditor walks through. The **statutory layer** is law: the EU AI Act's risk pyramid, the PDPA's consent, notification and accountability obligations, MAS's FEAT principles, HSA's medical-device rules. Only this layer fines you.

Serious programmes use all three in that order — principles to decide, management system to operate, law as the floor — and can show the mapping. That mapping, the crosswalk, is the most valuable artefact a governance team owns: one piece of evidence can satisfy several regimes.

### The sub-concepts

**Principles are not requirements.** "Human-centric" cannot be tested; "a named human owner signs the pre-deployment report" can. When a learner quotes a principle, ask what they would file as evidence.

**Certification is not safety.** ISO/IEC 42001 certifies a working management system, not an unbiased model. AI Verify and Project Moonshot reports document what was tested; a clean result on the wrong test set proves little.

**Privacy regimes differ in shape.** The PDPA runs on consent, notification and accountability. The GDPR adds lawful-basis categories, data-subject rights and heavier penalties. Both now expect you to say plainly, before collection, that personal data feeds a decision — and data scraped in disregard of either carries the objection into every deployment.

**The local stack is the operative one.** MAS FEAT and Veritas for financial institutions; the IMDA Model AI Governance Framework and its generative-AI companion with nine dimensions (accountability, data, trusted development, incident reporting, testing and assurance, security, content provenance, safety R&D, AI for public good); AI Verify for predictive models, Project Moonshot for LLMs. A Singapore class taught only the EU AI Act learns a rulebook they will never be audited against.

**Responsibility is split; liability is not.** The GenAI framework divides responsibility between model developer, application deployer and cloud host — and the deployer carries the customer-facing liability. Buying an API does not buy immunity.

### How it connects to the rest of the framework

This bullet is the map. `TSC8-Advanced-K3` is where standards collide across borders; `TSC8-Advanced-A6` is how to critique one; `TSC8-Advanced-A1` is how to apply one; `TSC8-Advanced-A5` is the dilemmas no standard resolves; `TSC8-Advanced-A9` is where you must write a new one. `TSC8-Advanced-K4` supplies the four lenses every framework is trying to reconcile.

### What is current as of November 2026

The EU AI Act has moved from text to enforcement: prohibited practices from February 2025, high-risk and general-purpose obligations phasing in, penalties up to EUR 35 million or 7% of global turnover for prohibited uses and 3% for the transparency tier. ISO/IEC 42001 has become the certificate procurement asks for, with the NIST framework as the shared vocabulary in US-facing contracts. And the generative frameworks were rewritten for agents — the IMDA 2024 framework and the 2025 ASEAN expansion now cover tool-using systems, provenance and incident reporting — because the systems shipping in late 2026, OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon, act rather than merely answer. Their model and system cards are the practical starting point for a deployer's documentation.

### Common misconceptions

- *"Singapore's framework is voluntary, so nothing happens."* The framework is voluntary; the PDPA is not, and regulators read adherence as evidence of reasonableness. MAS, HSA, POFMA and OCHA add hard enforcement.
- *"GDPR is the global privacy standard."* It is the strictest large-market standard, not a global one; PDPA notification duties and China's PIPL filing rules fail differently.
- *"One framework covers everything."* Principles do not certify, certificates do not legislate, and legislation does not tell you what customers will accept.
- *"We are too small to need one."* The deployer is liable regardless of size.

## How a student should understand it

**Mental model:** a building code, a fire certificate and a QA stamp — the code defines safety, the certificate proves this building was inspected, the stamp says the builder's process was audited. You need all three, and none guarantees no leaks.

**Things they can do after this bullet:**
1. Place any named framework into the correct layer.
2. Given a product and its markets, list which regimes bite and what evidence each asks for.
3. Explain why "we follow the IMDA framework" is not, alone, a compliance answer.

**Misconceptions to kill:** voluntary means optional, certification equals safety, one jurisdiction's rules travel with the model.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**BCA code, SCDF certificate, ISO stamp.** A building meets the BCA code (principles), needs a fire safety certificate from SCDF before occupancy (the statutory gate), and the contractor may hold ISO 9001 for its process. Nobody confuses the three or thinks the ISO stamp makes the building fireproof. Where it breaks: building codes are inspected on every project; AI frameworks are enforced unevenly, often only after an incident.

**The travel adaptor.** Same appliance, different socket. A model is the appliance, the jurisdiction the socket — except a model usually cannot be rewired per market, which is why the strictest market sets the design.

### Worked example with a real tool

```
We deploy a CV-screening assistant built on a third-party foundation model.
Customers are employers in Singapore and the EU.
Give me a table: (1) frameworks and standards that plausibly apply to us as
deployer, (2) the obligation we would have to evidence for each, (3) whether
each is law or voluntary. Then flag the three obligations most often missed.
```

What to point at: the list will be plausible and partly wrong, and that is the lesson. The class sorts each row into a layer, then asks who would inspect it. The pattern: employment screening is named in the EU AI Act's high-risk annex, so the EU obligation is the binding design constraint even for a Singapore-only vendor.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two products: one with a "Responsible AI" web page, one with an ISO/IEC 42001 certificate. Which does an enterprise buyer trust? Neither answer is complete.
2. **State the objective** — place any framework into the three layers and name the evidence it demands.
3. **Recall prior learning** — bias and privacy harms are what these frameworks exist to prevent.
4. **Present the content** — the three layers, one named example each, then the Singapore stack.
5. **Guide** — walk the CV-screening table together on the whiteboard.
6. **Elicit performance** — pairs take a product from their own organisation through the same table.
7. **Give feedback** — debrief the misplacements: principles filed as law, voluntary frameworks dismissed as irrelevant.
8. **Transfer** — each learner brings one page of their product documentation and marks what an auditor would find missing.

## What the framework doesn't mention but trainers need to know

- **Frameworks lag by design.** Each was written for the previous generation; agents that execute actions, synthetic media and embodied AI are under-specified — the gap `TSC8-Advanced-A9` fills.
- **Procurement is where standards bite.** Most Singapore organisations buy models rather than train them. The vendor questionnaire, the zero-retention clause and the model-card request are the real instruments.
- **Nobody is audited against a principle.** Learners who recite values but cannot produce evidence have learned decoration.

## Watch out

- **Do not teach framework names as trivia.** Knowing ISO/IEC 42001 exists is worthless; knowing it certifies a management system and not a model is the whole bullet.
- **Do not present the EU AI Act as a foreign problem.** Its scope follows the output into the EU market.
- **Do not call a voluntary framework "compliance".** Say it is what a regulator reads as evidence of reasonableness.
- **The stale claim to retire:** "AI ethics is about principles." In November 2026 the argument has moved to management systems, audit evidence and incident reporting.
