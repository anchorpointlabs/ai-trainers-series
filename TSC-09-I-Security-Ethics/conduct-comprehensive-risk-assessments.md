---
id: 09.02.I.A4
tsc: 9
level: Intermediate
code: A4
title: Conduct comprehensive risk assessments
---

# Conduct comprehensive risk assessments

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A4**

> **Framework text (verbatim):** "Conduct comprehensive risk assessments."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Ability · Bullet 8 of 10

**One-line version:** Comprehensive means every surface is named and every entry has an owner — model, data, retrieval, tools, users, integrations and supply chain, not just the chatbot's answers.

## What it is

A comprehensive risk assessment examines a deployed or proposed AI system across all its surfaces, produces a ranked register with owners, and records the evidence behind each judgement. It is comprehensive in coverage and specific in content: each entry names a failure, a mechanism, a likelihood, an impact, a mitigation, an owner and a review date.

## Deep expansion

### The concept

Most assessments fail by scope, not by method. The team assesses the model's answers and stops, while the incidents that actually happen come from the retrieval layer returning another department's document, a tool call with an unvalidated argument, a rendered link, a downloaded model file, or a support agent pasting customer data into a consumer tool.

So the first move is enumeration. Seven surfaces, each with its own characteristic failure:

1. **Model and prompt** — invention, policy breach, prompt leakage.
2. **Data and corpus** — personal data in the index, poisoned or outdated documents, missing access control at retrieval.
3. **Retrieval and memory** — cross-tenant leakage, stale chunks, similarity hijacking.
4. **Tools and actions** — unauthorised action, argument injection, excessive reach.
5. **Interfaces** — rendered markup, external images and links, file uploads and parsing.
6. **People and process** — staff pasting data into consumer tools, over-trusting outputs, approval fatigue.
7. **Supply chain** — model artefacts, plugins, third-party APIs, hallucinated package names.

Then apply the two AI-specific lenses. The **lethal trifecta** check: does this system hold private data, read untrusted input, and reach an external sink? If yes, it is critical regardless of how each individual answer scores. And the **identity question**: for every action the model can take, where does the identity come from — the session, or the model's argument?

Finally, ranking. Comprehensiveness is not a longer list; it is a list short enough to act on, ordered well enough that the top three get fixed.

### The sub-concepts

**Enumeration by data flow.** Walk a real request through the system: which components see it, what each adds, where it is stored. Risks attach to components and to the gaps between them.

**The register.** Id, surface, risk statement, likelihood, impact, existing controls, residual risk, owner, review date, status. One row, one judgement, one accountable person.

**Evidence.** Each likelihood and impact should cite something: a test result, a log count, a policy, a vendor document. An assessment full of unsupported adjectives is a mood board.

**Prioritisation with a cut line.** Force a ranking and declare a line: everything above it is fixed before launch, everything below is accepted with a date. Comprehensiveness without a cut line produces paralysis.

**Assumption testing.** Write down what the assessment assumes — "the retrieval layer filters by account", "the tool cannot be called without a session". Then verify each assumption. This is where most assessments quietly fail.

**Re-assessment triggers.** Model version change, prompt change, new tool, new corpus, new user population, an incident. Calendar review alone is too slow.

**Reporting to two audiences.** The engineering view (surfaces, controls, tests) and the accountable executive's view (top three risks, decision needed, residual after mitigation). Same assessment, different length.

### How it connects to the rest of the framework

`TSC9-Intermediate-K3` supplies the scoring methods; `TSC9-Intermediate-K4` sets the tiers and cadence. This bullet is the execution. `TSC9-Basic-A2` is the single-entry version of the same artefact. Downstream, `TSC9-Intermediate-A1` turns the ranked register into mitigations, `TSC9-Intermediate-A5` tests whether the controls hold, and `TSC9-Intermediate-A6` monitors whether the assessment is still true.

### What is current as of November 2026

Assessments now have to cover action, not just speech. The late-2026 frontier — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — is commonly wired to tools, so the tool surface is where most of the register's top rows now sit. Procurement and regulators also expect the artefact: a register that can be shown, not a workshop that can be remembered.

- **Tool surface first.** Enumerate tools and their reach before writing the first model-related risk.
- **Third-party components are in scope.** Plugins and connectors inherit your trust and bring their own.

### Common misconceptions

- *"We assessed the model, so we assessed the system."* The model is one component of seven surfaces.
- *"Comprehensive means exhaustive."* It means covered and ranked, with a cut line.
- *"The vendor's model card is our assessment."* It is an input, not an assessment of your system.
- *"If no incident has occurred, risk is low."* Absence of evidence is not evidence of safety, especially for adversarial risk.

## How a student should understand it

**Mental model:** the pre-purchase inspection of a used car — engine, brakes, tyres, chassis, electrics — not a look at the paint.

**Things they can do after this bullet:**
1. Enumerate the seven surfaces for a named system.
2. Run a lethal-trifecta check and an identity check on every tool.
3. Produce a ranked register with owners, evidence and a cut line.

**Misconceptions to kill:** that the model is the system; that a long list is comprehensive; that an assessment is complete when the workshop ends.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The condo inspection handover.** The buyer checks every room, every tap, every socket, and writes a defect list with photos. A "looks fine" handover is how people discover the leak after they move in.

**The kitchen's seven stations.** A hygiene inspection covers cold storage, cooking, plating, waste, water, pest control and staff practice. Missing one is how an outbreak starts. Where it breaks: a kitchen's stations are physical; an AI system's surfaces overlap.

### Worked example with a real tool

Give the room one system and run the enumeration fast, with the model as a checklist challenger:

```
System: an HR assistant that reads uploaded resumes, searches an
internal policy folder, and emails shortlists to hiring managers.

List every component that sees a request. For each, name the failure
that would matter most and who would notice. Then tell me which
component a team would most likely leave out of an assessment, and
why that omission is dangerous.
```

What to point at afterwards: the model will list the model, the data and the tools, and usually misses the email interface (where a rendered link or an outside recipient is the exfiltration path) and the person (who pastes a candidate's resume into a consumer tool). Both omissions are typical of real assessments.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read a short incident: correct answers, but the retrieval layer served another department's documents. Ask which surface was assessed.
2. **State the objective** — by the end, they can enumerate seven surfaces and produce a ranked register with a cut line.
3. **Recall prior learning** — any audit or inspection they have conducted.
4. **Present the content** — enumeration, the trifecta and identity lenses, register fields, evidence, cut line, triggers.
5. **Guide** — enumerate the HR assistant together.
6. **Elicit performance** — groups produce a six-row register with owners.
7. **Give feedback** — mark for specificity, evidence and ownership; call out missing surfaces.
8. **Transfer** — each learner runs the enumeration on their own system and reports the missing surface.

## What the framework doesn't mention but trainers need to know

- **The assessment is only as good as its assumptions.** Write them and test them; that step finds the real gaps.
- **Include the human workaround.** Shadow AI use — staff pasting data into consumer tools — is frequently the largest uncontrolled exposure.
- **Keep the register alive.** An assessment with no review dates is a historical document within a quarter.
- **Two pages beat twenty.** The version a decision-maker reads determines whether anything is funded.

## Watch out

- **Do not run the assessment as a survey.** It is a set of judgements with evidence, not a poll.
- **Do not let the loudest risk set the order.** Rank with the method, then discuss.
- **Do not skip the interface surface.** Rendered output is where leaks leave without a tool.
- **Retire the stale claim:** "we assessed it before launch, so it is assessed." In November 2026 the model may have changed twice since.
