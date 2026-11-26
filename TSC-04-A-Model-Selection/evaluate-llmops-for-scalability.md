---
id: 04.03.A.A4
tsc: 4
level: Advanced
code: A4
title: Evaluate LLMOps for scalability
as_at: 2026-11-26
review_by: 2027-02-25
---

# Evaluate LLMOps for scalability

> **TSC #4 Generative AI Model Selection · Advanced · Ability A4**

> **Framework text (verbatim):** "Evaluate the use of LLMOps on the scalability of advanced generative models for real-world applications."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Ability · Bullet 8 of 8

**One-line version:** LLMOps is what turns one working chatbot into twenty working services — registries, gates, gateways and telemetry instead of memory and courage.

## What it is

LLMOps is the operations discipline for generative systems: versioned artefacts, evaluation gates in the delivery pipeline, a gateway that routes and limits traffic, telemetry on cost and quality, and a rollback path. Assessing it for scalability means asking a blunt question — if the number of models, prompts, users and weekly changes all multiplied by ten, would this setup survive, and what would fail first?

## Deep expansion

### The concept

Traditional MLOps assumed numeric inputs, stable schemas and labels arriving later. LLMOps inherits worse conditions: models are enormous, inputs and outputs are unstructured, ground truth rarely exists in real time, and a third party can change your system's behaviour without telling you. Four properties follow, and each has an operational answer:

- Nothing is reproducible unless **six artefacts** are versioned together: model snapshot, prompt template, sampling settings, tool schemas, retrieval configuration, guardrail thresholds. Version the model and nothing else and you cannot explain last month's output.
- Behaviour is only knowable through **evaluation gates** — a run on every prompt or model change, sized so it completes in minutes.
- Cost and latency are **runtime properties**, controlled at a gateway: routing, caching, token caps and quotas.
- Failure is **invisible without telemetry**: latency percentiles, token spend by feature, guardrail trips, and quality sampled asynchronously.

Scalability is then not "more servers". It is whether those four controls exist before the tenth model arrives.

### The sub-concepts

**Registry before deployment.** Prompts belong in a versioned registry, decoupled from application code, so a wording change is a reviewable artefact with an author and a diff. Teams that edit prompts inside the codebase cannot answer "what changed on Tuesday".

**Evaluation in the pipeline.** A small, fast suite (tens of cases, under a minute) on every change; a larger stratified suite (hundreds) as the release gate. Without this, every prompt edit is a coin flip performed on customers.

**The gateway as the control point.** One service in front of all model calls gives you: cascade routing (cheap model first, escalate on difficulty), exact and semantic caching, per-tenant token budgets, loop breakers for agents, and provider failover. Centralising this is the difference between twenty teams negotiating with vendors and one policy.

**Telemetry in four columns.** Infrastructure (latency percentiles, error codes, queue depth), cost (tokens in, out and reasoning, tagged by feature and tenant), safety (injection attempts, redactions, schema failures), and quality (drift in inputs, retrieval similarity, retry and abandonment rates).

**Progressive delivery.** Shadow traffic to score a candidate offline on live inputs, then canary at a small percentage with automatic rollback on latency, failure rate or retry spikes. Big-bang prompt rollouts are how an ordinary Tuesday becomes an incident.

**The data flywheel.** Sampled production traces plus every thumbs-down go to review, become corrected examples, and join the regression set. This is what makes the tenth iteration better than the first.

### How it connects to the rest of the framework

`TSC4-Advanced-K3` is the single-model version of this; A4 is the portfolio version. `TSC4-Advanced-A3` defines what monitoring must detect. `TSC4-Advanced-A2` supplies the evaluation sets that the gates run. `TSC4-Advanced-K4` explains the cost telemetry that the gateway produces. `TSC4-Advanced-K1` is the serving layer underneath.

### What is current as of November 2026

For the 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — the operations burden grew in three specific ways:

- **Reasoning modes multiplied the variables.** Each request may now run in a fast mode or a thinking mode, with very different latency and cost. Routing policy is an ops decision with a quality consequence.
- **Prompt caching is now a scheduling decision.** Placing static content first in the payload unlocks large input discounts; placing it badly wastes them. This is configuration, not code, and it belongs in the gateway.
- **Multi-provider portfolios are normal.** Organisations routinely run two vendors for resilience and price leverage, which makes per-family prompt templates a registry requirement rather than a nicety.

### Common misconceptions

- *"We will add operations when we scale."* Operations is what makes scaling possible; retrofitting it means freezing the roadmap for a quarter.
- *"LLMOps is MLOps with a new name."* The artefacts, the failure modes and the third-party dependency are all different. Reusing an MLOps playbook unchanged misses all three.
- *"Monitoring means uptime."* Uptime is the least interesting metric. Quality drift, cost per outcome and refusal rate are the ones that matter.
- *"One prompt, one model, one team — we do not need a registry."* You need it the first time someone asks what changed.

## How a student should understand it

**Mental model:** a hawker centre rather than a single stall. One stall can run on the owner's memory; a centre needs licences, a cleaning roster, a supplier contract and a notice board, because thirty stalls cannot coordinate by memory.

**Things they can do after this bullet:**
1. Define LLMOps in one sentence and name its five components.
2. Predict what breaks first when models, prompts and users multiply by ten.
3. Specify the gate, the pin and the rollback for a given deployment.

**Misconceptions to kill:** that operations is a later phase, that uptime equals quality, and that a working prototype is production-ready.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The stall and the hawker centre.** Above. It also carries the cost point: a centre has overheads a stall does not, and those overheads are what let it serve a lunchtime crowd without collapsing.

**The MRT signalling system.** Trains are the models; signalling is LLMOps. Adding trains without signalling does not increase throughput, it increases the chance of a collision. Nobody proposes "we will add signalling once ridership grows".

### Worked example with a real tool

Give the room an uncomfortable but realistic picture and ask what breaks:

```text
Your team runs 20 models and ships 5 prompt updates a week, all deployed
by hand from one engineer's laptop. List two things that will break,
and say which one breaks first.
```

What to point at afterwards: the answers usually name version drift and missing regression testing; the sharper observation is that nobody can reproduce last week's output, so every complaint becomes unfalsifiable. Then ask for the smallest fix that buys the most safety — the answer is almost always "pin the model snapshot and put the prompt in a registry with a diff", which costs a day and prevents the class of incident they just described.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out the twenty-models-five-updates scenario and ask for a show of hands: "who has seen this?"
2. **State the objective** — by the end you can assess an ops setup against scale and name the first failure point.
3. **Recall prior learning** — version pinning and evaluation gates from the deployment workflow bullet.
4. **Present the content** — the six artefacts, the two-speed gate, the gateway functions, the four telemetry columns, progressive delivery.
5. **Guide** — map one real (or realistic) system onto the five components and mark the gaps.
6. **Elicit performance** — teams produce a one-page ops gap list for their scenario.
7. **Give feedback** — debrief, prioritising by blast radius rather than by elegance.
8. **Transfer** — each learner names the single gap they would close first in their own organisation.

## What the framework doesn't mention but trainers need to know

- **The first thing to build is the registry, not the dashboard.** A dashboard tells you something is wrong; the registry tells you what changed.
- **Evaluation gates need a latency budget.** A gate that takes forty minutes will be bypassed within a month. Keep the fast suite under a minute.
- **Semantic caching is dangerous on personalised queries.** Two questions with near-identical embeddings can have different correct answers ("my balance" versus "his balance"). Cache exact matches freely; cache semantic matches carefully.
- **Cost per outcome beats cost per call.** If resolution takes eight calls and two retries, the unit of measurement is the ticket.
- **Governance is part of ops in Singapore.** PDPA obligations, retention rules and audit expectations belong in the same pipeline, not in a separate policy document.

## Watch out

- **Do not sell LLMOps as tooling.** It is a set of controls; the tools are interchangeable and the controls are not.
- **Do not demo a dashboard as if it were the answer.** Pretty telemetry with no gate and no pin is decoration.
- **Do not overclaim scale readiness from a pilot.** The pilot had twenty users and one model; the question is what happens at five thousand and ten models.
- **The stale claim to retire:** "we will harden it after launch." Launch is when hardening stops being possible cheaply.
