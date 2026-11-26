---
id: 08.03.A.A1
tsc: 8
level: Advanced
code: A1
title: Apply comprehensive ethical frameworks
as_at: 2026-11-26
review_by: 2027-02-25
---

# Apply comprehensive ethical frameworks

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A1**

> **Framework text (verbatim):** "Apply comprehensive ethical frameworks to AI projects."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 5 of 14

**One-line version:** A framework is applied when a named person signs a dated decision backed by evidence — everything else is a citation.

## What it is

"Comprehensive" has three parts, and a framework missing any one of them is a poster. It covers the whole lifecycle, from the proposal to the retirement of the system. It covers all the lenses — legal, cultural, socio-political, environmental — not just the one the organisation finds easy. And it names stakeholders, including the people who never appear in the meeting. "Applying" it means using it to make and record decisions at each stage, with an owner and an artefact, rather than quoting it in a slide.

## Deep expansion

### The concept

The lifecycle is the spine. A governance framework that only appears at launch is a gate, not a system: the decisions that determine harm are taken earlier, when the use case is scoped, the data is chosen and the success metric is defined. The practical instrument is a sequence of gates, each with a question, a required artefact and an approver.

Gate 0, intake: who is building or buying this, what does it decide, does it touch personal data, is it on the prohibited list. Gate 1, design and data: lawful basis, impact assessment, data lineage and representation, the fairness metric chosen in advance, the human-oversight model chosen in advance. Gate 2, pre-deployment: model card, evaluation report, red-team results, guardrails verified, kill-switch tested. Gate 3, canary: live but limited, checking the human interface and the disclosure to customers. Gate 4, production: monitoring, drift, periodic re-validation, and automatic re-entry to Gate 2 on any model or prompt change. Gate 5, retirement: archived logs, weights, prompts, and a clean-data wipe.

Three properties make it comprehensive rather than theatrical. **Tiering** matches friction to risk, so a meeting summariser does not wait six weeks and a credit model does not slip through in a day. **Independence** keeps the builder from grading their own homework — the second line holds veto power over high-risk deployments. **Evidence** replaces assertion: a checklist item without an attached artefact is an opinion.

### The sub-concepts

**Owner.** One named human, not a committee. Committees diffuse accountability until nobody can be asked what happened.

**Decision rights.** Who may approve which tier, and who may stop a deployment. A framework with no veto is advisory.

**Proportionality.** The intensity of review scales with impact severity, autonomy and scale. Over-governing low-risk work teaches the organisation to route around governance.

**Traceability.** Every gate produces a dated artefact — impact assessment, evaluation report, sign-off — so an incident six months later can be reconstructed rather than remembered.

**Re-entry.** The most-missed control: swapping the underlying model, changing the system prompt or updating the retrieval corpus invalidates the previous approval.

### How it connects to the rest of the framework

`TSC8-Advanced-K1` supplies the frameworks being applied; this bullet is the application discipline. `TSC8-Advanced-A2` and `TSC8-Advanced-A3` produce the evidence Gate 2 requires. `TSC8-Advanced-A5` is what to do when two gates demand incompatible things. `TSC8-Advanced-A6` is how to critique the framework if it is unworkable. `TSC8-Advanced-K4` supplies the lenses the framework must cover.

### What is current as of November 2026

The application standard has hardened. ISO/IEC 42001 asks for a documented management system with an impact assessment and a risk treatment plan, and procurement in Singapore and Europe now asks for the certificate. The EU AI Act requires high-risk deployers to run a fundamental-rights impact assessment and to keep logs, which turns "we considered ethics" into a filing obligation. Agentic systems add a gate nobody had in 2023: review of what the system may do with tools, not only what it may say. Whether the underlying model is OpenAI's GPT-6 generation, Anthropic's Claude 5.5 or Google's Gemini 3.1 Pro, a version change forces re-entry — the vendors ship updates on their own schedule, not yours.

### Common misconceptions

- *"We cited the framework in the design document."* Citation is not application. Application produces a decision, an owner and a date.
- *"Comprehensive means a longer document."* It means wider coverage of stages and lenses, and sharper decisions.
- *"The framework makes the decision."* It structures the trade-off; a person still chooses and still answers for it.
- *"One approval covers the project."* It covers a version. Models, prompts and data change weekly.

## How a student should understand it

**Mental model:** an aviation pre-flight checklist. Same list every flight, signed by a named pilot, and no item is skipped because the last flight was fine.

**Things they can do after this bullet:**
1. Map a project onto six gates and name the artefact each demands.
2. Assign an owner and an approver for one gate.
3. Explain why a model swap re-opens approval.

**Misconceptions to kill:** citation equals application, comprehensive equals long, and approval is permanent.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The renovation permit.** You cannot start hacking walls without the HDB permit, cannot occupy without the inspection, and cannot close the case without the contractor's sign-off and the debris cleared. Each stage has an owner and a piece of paper. Where it breaks: renovation has one regulator; AI has several, and they do not share a file.

**The pre-flight checklist.** Two pilots, one list, read aloud, every flight — including the flight after a thousand safe ones. Where it breaks: a plane's failure is immediate and visible; a biased model fails quietly for months.

### Worked example with a real tool

```
We are applying a fairness framework to a SME loan-scoring model at the
evaluation stage. Produce: (1) the fairness checks to run and the metric
chosen in advance, (2) the artefact each check produces, (3) the named role
who signs off, (4) what would force this evaluation to be re-run.
Then state the one check most often skipped and why.
```

What to point at: the answer usually gets the metrics right and the ownership wrong — "the data science team" is not a name. Push until a role with veto power appears. Then point at the last line: re-run triggers are almost always omitted, which is why a model that passed in March is ungoverned by June.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — an incident report where every gate was "completed" and none had an artefact.
2. **State the objective** — map a project to six gates with owners and evidence.
3. **Recall prior learning** — the standards from `TSC8-Advanced-K1`; the harms from the K-block.
4. **Present the content** — the gates, the three properties, the re-entry rule.
5. **Guide** — fill a gate table for the loan model together.
6. **Elicit performance** — groups map their own project across the gates.
7. **Give feedback** — strike out any gate whose evidence is "discussed" rather than filed.
8. **Transfer** — each learner converts one gate into a real calendar commitment.

## What the framework doesn't mention but trainers need to know

- **Governance that costs six weeks gets bypassed.** Fast-track the low-risk 80% or the organisation will invent shadow processes.
- **The approver needs technical literacy.** A committee that cannot read an evaluation report approves the cover page.
- **Tiering is the political act.** Whoever writes the tiering rubric decides which projects get scrutiny.
- **Retirement is the forgotten gate.** Orphaned endpoints keep answering long after the owner has left.

## Watch out

- **Do not let the framework become the deliverable.** The decision is the deliverable.
- **Do not accept "the vendor is compliant".** Deployer obligations attach to your use.
- **Do not skip the proportionality argument.** It is what stops governance from being abolished after one slow quarter.
- **The stale claim to retire:** "We have an ethics framework." Everyone has one; almost nobody has gates with owners.
