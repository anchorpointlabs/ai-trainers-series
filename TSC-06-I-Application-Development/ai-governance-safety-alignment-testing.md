---
id: 06.02.I.K6
tsc: 6
level: Intermediate
code: K6
title: AI governance you can run: testing applications for safety and alignment
---

# AI governance you can run: testing applications for safety and alignment

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Knowledge K6**


> **Framework text (verbatim):** "Concepts behind AI governance and how to test and evaluate applications for safety and alignment."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Knowledge · Bullet 6 of 12

**One-line version:** Governance is not a policy document — it is the register, the gate and the evidence, and testing is how the evidence gets made.

## What it is

AI governance is the set of decisions, roles and records that make an organisation's use of AI accountable: what is deployed, who approved it, what it may touch, how it is watched, and what happens when it goes wrong. Testing for safety and alignment is the operational half — the checks that produce evidence a governance process can point at. This bullet connects the two, because a governance framework with no test evidence is a filing cabinet.

## Deep expansion

### The concept

Learners meet "governance" as a document and "testing" as a technical task, and never connect them. The connection is this: **every governance control is either a record or a test.** "Human oversight" is a test that a human actually reviews a sample. "Data minimisation" is a test that no unnecessary personal data reaches the prompt. "No harmful output" is a suite of adversarial inputs with a pass rate.

The governance objects a learner should be able to name:

- **Register.** Every AI system in use, with owner, purpose, model, data touched and risk tier. You cannot govern what you have not inventoried, and shadow AI is the normal starting condition.
- **Risk classification.** An internal summariser and a system that decides credit eligibility are different risk classes and should face different gates.
- **Approval gate and change control.** A named human accepts the risk before go-live with evidence attached; a model upgrade, prompt change or new data source is a change that can invalidate that evidence.
- **Incident path and audit trail.** Who is told, how fast, what gets shut down, what gets written down — and logs that let someone reconstruct what the system said to whom, months later.

### The sub-concepts

**Safety versus alignment.** *Safety* asks whether the system can cause harm. *Alignment* asks whether it does what the operator intends and refuses what it should. A bot can be safe and misaligned (refuses everything useful) or aligned and unsafe (efficiently does something harmful because it was asked).

**Evaluation sets.** A fixed, versioned collection of inputs with expected behaviour, including the adversarial ones. Twenty to fifty curated cases is enough to catch regressions; it does not need to be a research programme.

**Red-teaming.** Deliberate attempts to make the system misbehave: jailbreaks, prompt injection through uploaded documents, out-of-scope requests, system-prompt extraction, attempts to reach another customer's data.

**Groundedness testing.** For retrieval systems, whether the answer is supported by the retrieved context. This is where most real-world harm lives — a confident, wrong, uncited claim.

**Refusal testing.** Whether the system refuses the right things, and refuses them gracefully. Over-refusal is a governance failure too: it drives users to bypass the system.

**Sampling and monitoring.** Post-launch, a fixed sample of real interactions reviewed by a human, plus automated flags on refusal rate, block rate and escalation rate.

### How it connects to the rest of the framework

`TSC6-Intermediate-K7` is the runtime enforcement of what this bullet tests; `TSC6-Intermediate-A4` is deploying it. `TSC6-Intermediate-K5` is where the pipeline puts the checkpoints. `TSC8` is the full discipline this introduces, `TSC5` supplies the metrics, and `TSC6-Basic-A3` is the human end of the incident path.

### What is current as of November 2026

Governance has become concrete and testable. Assurance frameworks moved from principles to evidence — Singapore's AI Verify testing framework and its generative AI evaluation work normalised the idea that a vendor hands over test results, and buyers now ask for them. Providers publish system cards and refusal behaviour, so a team can test against a documented baseline. And regulation is horizontal and sector-specific at once: PDPA applies everywhere, while finance, healthcare and education add their own layer.

### Common misconceptions

- *"Governance slows us down."* A register and a twenty-case eval set take an afternoon. Rebuilding trust after an incident takes quarters.
- *"Testing is a one-off before launch."* Models change, prompts change, data changes. A model upgrade is a new system in all the ways that matter.
- *"Safety is the model provider's job."* The provider tests the base model. Nobody tests your prompt, your retrieval, or your users.
- *"If the model refuses, we're safe."* Over-refusal pushes users to a shadow tool with no controls at all.

## How a student should understand it

**Mental model:** the food-hygiene grade on the wall. The letter is not the achievement — the achievement is the unannounced inspection, the temperature logbook and the power to close the stall.

**Three things they can do after this bullet:**
1. Add one AI system to a register with owner, risk tier and data touched.
2. Build a twenty-case evaluation set including five adversarial inputs, and run it.
3. Name who is told, and within what time, when the system produces something harmful.

**Misconceptions to kill:** governance is bureaucracy, testing is one-off, and refusal equals safety.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hygiene grade.** An "A" tells you the stall was inspected and passed; it tells you nothing about tomorrow, which is why the logbook and the re-inspection exist. A model's safety claim is the certificate; your eval set and monitoring are the logbook. Where it breaks: hygiene failures are visible to a customer, while a model failure is fluent and invisible — which is why sampling matters more here than in a kitchen.

**CPF statements.** You trust CPF not because it says it is trustworthy, but because every contribution is recorded, reconcilable and auditable years later. That is the audit trail: not a promise, a record. Break: CPF records money, which is countable; AI records conversations.

### Worked example with a real tool

Have the model red-team your own application — the fastest way to a first eval set. In Claude:

```
You are a red-team tester. My application is a customer service
chatbot for a tuition centre. It answers questions about courses,
fees and schedules only.

Write 12 test inputs: 4 normal, 4 out-of-scope, 4 adversarial
(prompt injection, system prompt extraction, requests for other
students' data, and a policy-bending request). For each, state what
a safe response must do.
```

What to point at afterwards: the twelve lines become version one of the evaluation set, and the "what a safe response must do" column is the pass criterion. Run them against the live bot, count failures, and record the result with a date and a model version. That single artefact — a dated table of pass and fail — is what a governance process actually consumes, and it took twenty minutes.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask who could list every AI tool their team used last month. Usually nobody, which is the register problem.
2. **State the objective** — you will register a system, classify its risk, and produce a dated test result.
3. **Recall prior learning** — they know evaluation metrics from TSC5 and pipeline checkpoints from K5.
4. **Present the content** — the four governance objects, safety versus alignment, then the test types.
5. **Guide** — build the twelve-case eval set together and run three cases live.
6. **Elicit performance** — each team writes three adversarial cases for their own application and one incident-path sentence.
7. **Give feedback** — the common gap is no pass criterion: learners write inputs but not what "correct" means.
8. **Transfer** — they take the register template and eval-set format back to their team.

## What the framework doesn't mention but trainers need to know

- **Shadow AI is the biggest actual risk, and no test catches it.** The register matters more than the eval set, because unregistered use has no owner, no evidence and no incident path.
- **Small eval sets beat none.** The temptation is to wait for a proper evaluation programme. Twenty curated cases run monthly will find more real problems than a plan.
- **Model upgrades invalidate evidence silently.** A deprecation notice is a governance event. Put the re-test in the change process, or the certificate describes a model you no longer use.

## Watch out

- **Do not present governance as a document review.** If the session ends with a policy and no test, the room has learned the wrong thing.
- **Do not demo only successful tests.** Show a jailbreak that gets through — it makes the case for the register better than any slide.
- **Do not imply compliance once and done.** A dated test result has a shelf life; say so plainly.
- **The stale claim to retire:** "we'll do governance once the regulation is clear." In November 2026 the buyer's question is already "show me your tests", and PDPA already applies.
