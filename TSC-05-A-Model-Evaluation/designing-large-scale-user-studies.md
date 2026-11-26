---
id: 05.03.A.A1
tsc: 5
level: Advanced
code: A1
title: "Running it at scale: studies that survive a review board"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Running it at scale: studies that survive a review board

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A1**


> **Framework text (verbatim):** "Design and conduct large-scale user studies and A/B tests."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 7 of 13

**One-line version:** At scale a study is infrastructure: if assignment, logging and the stopping rule are not built before launch, the result is a story rather than a measurement.

## What it is

This is the execution half of `05.03.A.K1`. Designing and conducting at scale means writing a protocol a reviewer can approve, instrumenting the system so every outcome is attributable to a variant, recruiting sufficient participants or traffic, analysing to a pre-declared plan, and reporting the result with its uncertainty and its limitations. It is project work as much as statistics.

## Deep expansion

### The concept

At small scale you hold the study in your head. At large scale three things break. **Assignment** breaks first: users share devices, teams share accounts, and an agent acting on a shared case cannot be randomised per request. **Instrumentation** breaks second: the outcome you care about — did the customer's problem get resolved — lives in a different system from the one serving the model, and the join key often does not exist until someone builds it. **Attention** breaks third: a six-week study gets checked twice, and if the dashboard does not answer the decision question in one screen, it will be replaced by opinion.

The discipline holding all three together is the **protocol** — a short document written before launch naming the decision, variants, unit, primary metric, guardrails, sample size, stopping rule and analysis. Its purpose is to make the result falsifiable by the team that wants a particular answer.

### The sub-concepts

**The decision the study serves.** Write it as a sentence with a verb: "if variant B raises resolution-without-escalation by five points without raising handle time, we migrate in Q1". A study with no decision attached gets reinterpreted afterwards.

**Sampling frame and exclusions.** Who is eligible, who is excluded and why. Excluding the hardest cases improves the numbers and ruins the finding — but excluding users whose data may not be processed is a legal requirement the report must state.

**Power before, not after.** Fix the minimum detectable effect, baseline rate, allocation and expected attrition. If the required sample exceeds the traffic, say so and change the design rather than run an underpowered test and call the null a finding.

**Stratification.** Randomise within branch, tenure band or case type so imbalance cannot masquerade as an effect. Cheapest robustness win available.

**Guardrails with an automatic stop.** Cost per interaction, escalation rate, complaints, latency, refusal rate — with a written stop rule owned by a named person, or it will not be pulled.

**A blinded human sample.** Even in a live test, a stratified sample scored blind is what lets you say the automated metric meant something.

**Analysis plan.** Primary metric, pre-declared segments, correction for multiple comparisons, missing-data handling, and what would count as null.

### How it connects to the rest of the framework

`05.03.A.K1` is the design rationale; this is the delivery. `05.03.A.K4` supplies the automated scoring used to triage and monitor during the run, and `05.02.I.K6` the statistics. `05.03.A.A3` is the leadership that keeps the study resourced and on schedule, `05.03.A.K5` governs data handling, and `TSC6-I` supplies the deployment and feature-flag machinery the test depends on.

### What is current as of November 2026

Live testing of generative features is routine enough that tooling assumes it: feature flags routing by model version, prompt registries, evaluation hooks in the serving layer. The awkward cases are agentic and long-context systems, where a session is the real experimental unit and the outcome may take days to resolve. Teams increasingly run two tracks — a fast judged evaluation on logged traffic weekly, and a slower randomised test quarterly — because the weekly loop answers questions the quarterly test is too slow to serve.

### Common misconceptions

- *"Scale means more traffic."* Scale means enough traffic **and** an assignment scheme that does not mix the variants.
- *"We can pick the metric after we see what moved."* That is a search, not a test, and it will always find something.
- *"The engineer can add logging later."* By later, the interesting traffic has gone through.

## How a student should understand it

**Mental model:** a proper trial at a polyclinic — the protocol is approved before the first patient, the randomisation is done by the pharmacy, and the stopping rule is written on the wall.

**Three things they can do after this bullet:**
1. Write a one-page protocol a reviewer can approve or reject without a follow-up question.
2. Name the identifier that joins outcome to variant, and get it built.
3. Run the pre-launch checklist: power, guardrails, stop rule, analysis plan, approvals.

**Misconceptions to kill:** that analysis is the hard part, that logging is an engineering detail, and that a null result is a failed study.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT platform trial.** You would not paint half a platform and count one morning. You would pick two comparable stations, run a fortnight, count boardings and complaints, and stop early if the crowd-safety margin is breached. That is a protocol with a guardrail. It breaks because commuters cannot opt out.

**The tray-return trial.** Two blocks, same town council, new signage in one. The measure is trays returned per hundred, not whether people say they like it. The confound is the cleaner reassigned mid-trial — exactly the thing that goes unlogged and ruins the result.

### Worked example with a real tool

A team is about to test a new prompt across 1,200 seats. Before launch, have a model review the protocol adversarially. Paste this into Claude:

```
You are a methods reviewer on an internal research review board. Be unkind.

Protocol: 1,200 agents, randomised 50/50 at agent level by seat ID. Variant A is the
current prompt; B adds a mandatory escalation check. Primary metric: resolution
without escalation, from the ticketing system. Guardrails: handle time, CSAT,
complaints. Duration 3 weeks. Baseline 62%, target lift 4 points. Outcome joined on
ticket ID; some tickets have no agent ID (web form).

Give me: (1) five ways this could produce a confidently wrong answer, with severity
and the cheapest fix for each; (2) whether 1,200 agents over 3 weeks is plausibly
enough for a 4-point lift on a 62% baseline with agent-level clustering, and what
you would need to know to answer properly; (3) the one number to look at on day 3 to
decide whether to stop.

Bullet points. No praise.
```

What to point at afterwards: point 2. Learners want a yes or no; the correct answer is "here are the assumptions, and clustering eats your effective sample". Point 3 is the practicality check — a study with no early signal gets abandoned rather than read.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — present a study that "proved" a 3-point lift, then reveal the variants were assigned per request.
2. **State the objective** — each learner has a one-page protocol a peer has tried and failed to break.
3. **Recall prior learning** — the counterfactual and unit-of-randomisation discussion from K1.
4. **Present the content** — the protocol's parts, clustering and power, guardrails and stop rules, analysis plans.
5. **Guide** — draft the 1,200-seat protocol on the projector, arguing about the unit.
6. **Elicit performance** — teams write a protocol for their own system and hand it to another team.
7. **Give feedback** — the reviewer must find one fatal flaw; if they cannot, the protocol is under-specified, not perfect.
8. **Transfer** — each learner runs the pre-launch checklist against a real upcoming change.

## What the framework doesn't mention but trainers need to know

- **Clustering is the number that embarrasses people.** Cases within an agent or a branch are correlated; ignoring it can inflate significance substantially.
- **The join key is the project.** Budget a week of data engineering before any statistics. Most failed studies are failed joins.
- **Write the stop rule with a name attached.** "The team will monitor" means nobody will.
- **Get the approval chain early.** Changes to what customers are told touch legal, compliance and often staff representation.

## Watch out

- **Do not run an underpowered test and read the null as equivalence.** With 40 users, "no significant difference" means you learned nothing.
- **Do not make the primary metric a composite you cannot explain.** Weighted indices produce arguments about weights instead of the system.
- **Do not skip the human-rated sample.** Automated metrics drift, and the drift is invisible without a fixed reference.
- **Do not test on a population that excludes the people the system is for.** Internal staff answer a different question.
- **The stale claim to retire:** "we will run the A/B test and see what the data says." Data says nothing until a decision rule tells it what to answer.
