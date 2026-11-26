---
id: 06.03.A.K5
tsc: 6
level: Advanced
code: K5
title: "Generative AI meets emerging technology: four integration patterns"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Generative AI meets emerging technology: four integration patterns

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Knowledge K5**


> **Framework text (verbatim):** "Concepts on integrating generative AI models with emerging technologies."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Knowledge · Bullet 5 of 12

**One-line version:** Every integration is one of four shapes — a component behind an API, an orchestrator over tools, a model on the device, or a model inside a control loop — and each shape has its own contract.

## What it is

This is the knowledge of how generative models attach to technologies that are new or newly practical: agent tool protocols, on-device inference, real-time voice, wearables and ambient devices, robotics and building systems, and content provenance for generated media. The value is not a catalogue of gadgets. It is recognising which integration *shape* you are building, because the shape determines the interface contract, the latency budget, the failure mode and the safety argument.

## Deep expansion

### The concept

A model is not a system. It is a component that consumes text, images or audio and produces tokens, with a distribution of latency and a non-trivial error rate. Integration means wrapping that component so the surrounding technology can rely on it: a defined input, a defined output, a stated latency, a defined behaviour when it fails.

Four shapes cover almost everything:

1. **Component behind an API.** The model sits inside an existing application or ERP, called like any other service. Contract: schema, timeout, fallback. Risk: low; the surrounding system still owns the logic.
2. **Orchestrator over tools.** The model chooses and sequences calls to other systems through a tool protocol. Contract: which tools, what permissions, what it may do without approval. Risk: high, because output becomes action.
3. **Model on the device.** A quantised model runs on a phone, laptop, camera or kiosk. Contract: memory ceiling, update path, offline behaviour. Risk: capability drift between devices and silence about what the model saw.
4. **Model inside a control loop.** Robotics, lifts, HVAC, traffic systems. Contract: a hard latency bound and a deterministic safety interlock. Risk: highest, because a wrong token can move a physical object.

The Advanced judgement is refusing to force a use case into the wrong shape. A voice kiosk is shape three plus shape one; a warehouse robot is shape four with a language interface attached, and the language model must never be in the loop that stops the arm.

### The sub-concepts

**The interface contract.** Input schema, output schema, latency budget, retry policy, failure mode and observability. Written before the integration, not discovered during the incident. A model that returns prose where a validator expects a slot is not integrated.

**Tool and agent protocols.** Standard connectors — the MCP family being the widely adopted example — collapse many bespoke integrations into one protocol. The engineering win is real; the security question changes shape, from "can it call this API" to "which of forty tools may it call, with whose credentials, and what is logged".

**Edge and on-device.** Privacy and offline capability are the real reasons, not cost. The ceiling is capability: a small quantised model does narrow tasks, and the update path for a fleet of devices is a logistics problem that server deployments do not have.

**Real-time modalities.** Voice and video impose turn-taking deadlines. Streaming architectures change from "wait for the answer" to "partial results, barge-in, interruption, re-plan". Design for the interruption, not just the answer.

**Embodied and industrial systems.** Here the model proposes and a deterministic controller disposes. Safety interlocks, rate limits and a physical stop sit outside the model, always.

**Provenance.** Once generated media leaves your boundary, attestation matters: content credentials, watermarking, signed metadata. Integration with publishing and records systems is now part of the architecture, not a communications afterthought.

### How it connects to the rest of the framework

`TSC6-Advanced-A1` is the application-building ability that uses these patterns; `TSC6-Advanced-K1` explains why shape three is possible at all — quantisation is what put a usable model on a device. `TSC6-Advanced-K2` and `A3` supply the guardrail thinking that shape two demands, and `TSC6-Advanced-A2` is the serving layer for shapes one and two. `TSC4` covers the selection judgement that decides which model each shape can carry.

### What is current as of November 2026

- **Tool protocols consolidated.** A standard connector layer is now assumed in agent products, which means integration work has shifted from writing glue to governing permissions.
- **Voice agents are in production**, not pilots — call handling, kiosks, appointment booking — and the quality bar users apply is human turn-taking, not transcription accuracy.
- **On-device models ship in ordinary consumer devices** for summarisation, dictation and photo features, which quietly moved a large volume of inference off the server.
- **Embodied pilots concentrate in logistics, inspection and facilities**, where the task is bounded and the safety case can be written.
- **Provenance metadata is appearing in publishing and camera workflows**, unevenly, and regulators are watching rather than mandating.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It will just plug into our ERP."* Only if someone writes and maintains the contract, including the failure path.
- *"The model can run the robot."* The model can propose a plan. The controller runs the robot, and the safety interlock is not negotiable.
- *"On-device means no privacy issue."* It reduces data transmission; it does not remove the need to say what is recorded, stored and shared.
- *"Integration is an API call."* An API call is the easy hour. Permissions, retries, versioning and observability are the rest of the week.

## How a student should understand it

**Mental model:** adding a new payment method to an MRT gate. It must work at gate speed, with the same reliability as the old one, and it must fail safely — a gate that opens on error is worse than a gate that closes.

**Three things they can do after this bullet:**
1. Classify an integration into one of the four shapes and name its contract.
2. State the latency budget for a real-time use case and show the arithmetic across components.
3. Identify which component must remain deterministic in a control-loop design, and why.

**Misconceptions to kill:** that integration is a plug, that the model can be trusted with actuation, and that on-device removes privacy obligations.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The SimplyGo gate.** A new fare system is judged at the gate, not at the bank: 300 milliseconds or the queue backs up. Every emerging-technology integration has a gate-speed number, and the model's share of it is usually the largest and least predictable part.

**The HDB lift.** The lift phones the contractor before a resident complains, and it will not close its doors on a child no matter what the schedule says. Sensors and rules handle safety; the clever layer handles convenience. Put the model in the clever layer.

### Worked example with a real tool

Ask an assistant to design the integration, then attack the numbers:

```
We want a voice kiosk at a community club. A resident speaks in English,
Mandarin or Malay. We answer from a 60-page facilities FAQ. The answer
must start within 1.5 seconds of the resident finishing, and it must never
invent an available booking slot.

Draft the architecture: components, the interface contract between each
pair, and the three most likely failure modes with a fallback for each.
```

What to point at afterwards: the components will be sensible — speech to text, retrieval, model, text to speech — and the latency arithmetic will not add up. Add the parts yourself on the board: transcription, retrieval, generation, synthesis, network. That is the lesson: the integration is a budget, and the model is one line item. Then press on "never invent a slot": the fix is not a better prompt but a booking API that returns real slots, which is shape two wearing shape one's clothes.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — play a 1.5-second deadline: a voice assistant that pauses three seconds and loses the user.
2. **State the objective** — you will classify your integration, write its contract, and defend its latency budget.
3. **Recall prior learning** — they have deployed a chat application; now the model is one component among several.
4. **Present the content** — the four shapes, their contracts and their risks.
5. **Guide** — classify four real products into shapes together.
6. **Elicit performance** — teams sketch their own integration with a latency sum and a failure fallback.
7. **Give feedback** — challenge any sketch without a deterministic boundary.
8. **Transfer** — they write the interface contract before the next prototype.

## What the framework doesn't mention but trainers need to know

- **Version pinning gets harder at the edge.** A fleet of devices running three model versions needs a capability contract, not just an app version number.
- **Consent and notice differ by modality.** A camera that describes a room and a chat box that answers a question are not the same privacy event, even with the same model.
- **Tool proliferation is the new integration debt.** Forty tools with unclear ownership is worse than five well-governed ones.
- **Procurement cycles outlast model cycles.** A device bought in 2026 will run models from 2028; design for replaceability.
- **The demo is not the contract.** Integrations fail on permission expiry, token refresh and partial network, none of which appear in a demo.

## Watch out

- **Do not present emerging technology as a roadmap.** Teach the shapes and the contracts; the product names will change before the next cohort.
- **Do not demo autonomy in a safety-relevant setting**, even playfully. The framing learners take away is "the model decides".
- **Do not overclaim standards adoption.** Provenance and agent protocols are spreading unevenly; say "widely adopted in some markets" rather than "the standard".
- **The stale claim to retire:** "generative AI is something you chat with." By November 2026 it is a component inside kiosks, phones, cameras and control systems, and most of the work is the wiring.
