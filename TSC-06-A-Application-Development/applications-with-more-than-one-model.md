---
id: 06.03.A.A1
tsc: 6
level: Advanced
code: A1
title: "Building an application that uses more than one model, and knows why"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Building an application that uses more than one model, and knows why

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A1**


> **Framework text (verbatim):** "Create applications that integrate multiple generative AI models and use context augmentation techniques."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 6 of 12

**One-line version:** A multi-model application is not impressive because it has three models — it is good because each model was chosen for a job the others would do worse or dearer.

## What it is

This is the ability to compose an application from several models and retrieve the right context for each: a small model that answers routine questions from a handbook, a frontier model that handles exceptions, an embedding model that indexes, a reranker that orders evidence, a vision model that reads a photographed receipt, a classifier that routes between them. The Advanced part is holding the whole composition together — a shared data contract, a reason for every hop, and an evaluation that can tell you which hop failed.

## Deep expansion

### The concept

Single-model applications fail in one way: the model is wrong. Multi-model applications fail in six: the router misroutes, the retrieval returns nothing, the small model is confidently wrong, the hand-off loses context, the fallback returns a different answer, or the cost triples and nobody notices until the invoice.

So composition is a discipline of *justification and contract*. Justification: every model earns its place by being cheaper, faster, more specialised, more reliable or more independent than the alternative. Contract: every hop passes a defined structure — not a paragraph of prose — so the next hop can check it.

Three composition patterns cover most real systems:

- **Route.** A classifier sends each request to the appropriate model. Cheapest at scale, and the router is the single point of failure.
- **Cascade.** The small model answers; if confidence is low, escalate to the frontier model. Most traffic stays cheap, hard cases get quality, and the confidence threshold is the tuning dial.
- **Verify.** One model produces, another checks against the source or a rubric. Costs two passes and catches the failure that matters most: fluent invention.

Beyond these, planner-executor and specialist delegation patterns exist, and they are harder than they look. Each extra hop multiplies the failure surface, and the first question in any design review should be "what breaks if we delete this model?".

### The sub-concepts

**The shared envelope.** A single structure carried through every hop: user request, resolved intent, retrieved evidence with source IDs, model outputs with confidence, guardrail decisions, trace ID. Without it, the verifier cannot check the producer and the logs cannot reconstruct the run.

**Routing on observable features.** Route on intent classification, input length, presence of an image, tenant, or explicit user choice — not on vibes. Every routing rule needs a test case and a fallback when the classifier is unsure.

**Confidence that means something.** Model self-reported confidence is weakly calibrated. Better: retrieval score, agreement between two samples, schema validity, or a small classifier trained on your own labelled outcomes.

**Context per hop, not context everywhere.** The verifier needs the source; the router does not. Sending the full context to every model is the most common cost mistake in multi-model design.

**Degradation, not failure.** When the frontier model is unavailable or rate-limited, the application should serve the small model's answer with a visible caveat, not an error page. Fallback is a design decision with a quality statement attached.

**Evaluation per hop.** A router accuracy set, a retrieval recall set, a generation quality set. End-to-end scores hide which component regressed.

### How it connects to the rest of the framework

`TSC6-Advanced-K3` supplies the augmentation techniques this ability composes; `TSC6-Advanced-K1` explains why the small-first cascade is usually the cheapest correct design. `TSC6-Advanced-A2` is the serving layer underneath, and `TSC6-Advanced-K2` covers the guardrails that sit between hops. `TSC6-Intermediate-A2` is the workflow-design predecessor; this bullet assumes those integration patterns and adds a second and third model to them.

### What is current as of November 2026

- **The cascade is the dominant cost pattern.** Small model first, frontier model on low confidence. Most production teams describe their architecture this way now, and it is why routing quality matters more than raw model choice.
- **Model gateways are standard infrastructure.** One internal endpoint that fronts several providers gives you key management, fallback, cost attribution and per-tenant limits — and it makes multi-model design practical instead of bespoke.
- **Orchestration frameworks matured and multiplied.** They reduce boilerplate and add hidden control flow; teams that debug them well often end up with explicit code instead.
- **Multi-agent designs are used more cautiously.** The enthusiasm of 2024–25 has given way to "one agent, several tools" for most tasks, with multi-agent reserved for genuinely separable work.
- **The frontier models are close enough on ordinary tasks** that routing decisions increasingly turn on price, latency and context size rather than capability.

### Common misconceptions

- *"More models means better quality."* More models means more failure points. Quality comes from each hop doing a job the others cannot.
- *"The router is trivial."* The router is a classifier with its own accuracy problem, and it sits on the critical path of every request.
- *"Confidence scores are reliable."* Self-reported confidence is weakly calibrated; design a measurable proxy instead.
- *"End-to-end evaluation is enough."* It tells you the system regressed; it does not tell you which of five models did it.

## How a student should understand it

**Mental model:** the polyclinic referral system. The GP handles most cases well and cheaply, refers the difficult ones to a specialist, and both write in the same patient record. The record is the envelope; the referral threshold is the router.

**Three things they can do after this bullet:**
1. Draw a multi-model application with a named job for each model and a stated reason it is not a single-model design.
2. Define the shared envelope and the per-hop contract.
3. Set a confidence threshold with a test set, and describe the fallback behaviour.

**Misconceptions to kill:** more models equals better, the router is free, and fallback is an error page.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**GP and specialist.** The polyclinic doctor sees forty patients a day and refers two. The system works because the referral criteria are written down and both parties share the record — not because the specialist is smarter. Where it breaks: a patient can choose to walk into A&E, so your router needs a "user insists" path that bypasses the threshold.

**The zi char kitchen brigade.** One wok is not a kitchen. The order goes to the right station, the expediter checks the plate, and the same order ticket follows the dish. Remove the ticket and the kitchen collapses — that ticket is the shared envelope.

### Worked example with a real tool

Give an assistant the design brief and make it justify each hop:

```
Design a support application for a tuition centre with three models:

- Model A (small, cheap): answers FAQ from a 40-page parent handbook.
- Model B (frontier): handles complaints, refunds and fee disputes.
- Model C (vision): reads a photographed receipt or invoice.

Define: the routing rules including a low-confidence path; what context
each model receives and what it must not receive; the JSON structure
passed between hops; the fallback when B is unavailable; and how I would
test the router separately from the answer quality.
```

What to point at afterwards: the answer will name the models and the rules, and it will usually forget to say what A must *not* receive — parent contact details it has no use for. It will also hand-wave the router test. Those two omissions are the exam: context minimisation per hop, and a labelled routing set of fifty real requests with expected destinations.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a single-model application giving a refund answer it had no authority to give. Ask what would have caught it.
2. **State the objective** — you will design a justified multi-model application with a contract per hop.
3. **Recall prior learning** — they built one model plus retrieval; now they add a router and a verifier.
4. **Present the content** — route, cascade, verify; the envelope; per-hop context.
5. **Guide** — design the tuition-centre example together, arguing each model in or out.
6. **Elicit performance** — teams draw their own composition and delete one model to test the justification.
7. **Give feedback** — challenge designs where two models do the same job, and routers with no test set.
8. **Transfer** — they write an architecture note with a per-hop evaluation plan before building.

## What the framework doesn't mention but trainers need to know

- **Cost attribution per hop is a design requirement.** Without per-hop token accounting you cannot tell which model is eating the budget.
- **Latency adds up silently.** Three sequential model calls at one second each is a three-second experience; parallelise what is independent.
- **Model versions drift independently.** Pin each hop, and re-run the per-hop evaluation when any one of them changes.
- **Vendor independence is a real reason to compose.** A verifier on a different provider catches failures a same-provider verifier shares.
- **The simplest composition that passes the evaluation wins.** Every hop you can delete is maintenance you do not own.

## Watch out

- **Do not demo a five-model architecture as a beginner pattern.** It teaches complexity as sophistication, and the room will copy the diagram without the evaluation.
- **Do not let the router be invisible.** If a request silently goes to the cheap model, a user who needed the frontier model experiences it as the system being bad.
- **Do not skip the "delete a model" question** in design review; it is the fastest way to find architecture for its own sake.
- **The stale claim to retire:** "multi-agent is the future of applications." In November 2026 most reliable production systems are one model, several tools, and a verifier.
