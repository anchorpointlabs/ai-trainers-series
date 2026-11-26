---
id: 07.03.A.K2
tsc: 7
level: Advanced
code: K2
title: Generative AI as the connective tissue of emerging technology
as_at: 2026-11-26
review_by: 2027-02-25
---

# Generative AI as the connective tissue of emerging technology

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K2**


> **Framework text (verbatim):** "Concepts on integrating generative AI models with emerging technologies."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 2 of 20

**One-line version:** Generative models rarely ship alone any more — the design question is which other technology supplies the senses, the hands or the guarantee, and what that partnership costs in latency and trust.

## What it is

Integrating generative AI with emerging technologies means designing systems where a generative model is one component among several: a robot's planner, a headset's scene understanding, a digital twin's scenario generator, a lab rig's experiment proposer. The model contributes language, priors or generative capacity; the surrounding technology contributes grounding, actuation, real-time constraints or verification. The discipline is deciding where the boundary sits.

## Deep expansion

### The concept

A standalone chatbot can afford two seconds of latency and no physical consequence. Wire a generative model into a robot, a headset, a factory line or a clinical workflow and three constraints appear that it was never designed for.

**Grounding.** The surrounding system tells the model what is actually there — sensor readings, database state, device telemetry. A grounded model stops inventing and starts referencing.

**Latency budget.** Physical and interactive systems have deadlines in milliseconds. A model streaming tokens for four seconds cannot close a control loop; it can only advise one.

**Consequence.** If the output moves an arm or writes to a medical record, you need a verifier, an interlock or a human gate, and no amount of prompt engineering substitutes for them.

The pattern that has settled out is not "put a model in the product" but "put a model behind a contract": it sees structured state, returns structured actions, and the surrounding system validates before acting. Everything else — which technology, which protocol — is detail.

### The sub-concepts

**Embodied AI and vision-language-action models.** A policy takes an image plus an instruction and emits motor commands. The model supplies generalisation across objects and tasks; the controller supplies safety and repeatability. Measured by task success in a physical environment, not by text quality.

**Spatial and wearable computing.** Headsets and glasses need on-device or low-latency inference, aggressive compression, and awareness of what the user is looking at. Privacy moves left: the camera feed should not leave the device.

**Digital twins and simulation.** A generative model proposes scenarios; a physics simulator tests them. The cheapest place to put a generative component, because failure is free.

**Agentic tool use as the integration fabric.** Function calling, structured outputs and open tool protocols are now the standard way to attach a model to a database, a payment API, a CAD package, a CRM. Most integration work in practice is tool-call design, and edge deployment — small quantised models beside the sensor — is the same contract under a tighter budget.

### How it connects to the rest of the framework

This is the systems view of `TSC6-Advanced-K5`, which covers the same ground from the application side. `TSC7-Advanced-K3` (hardware libraries) explains why on-device work is hard; `TSC7-Advanced-A5` (agentic systems) is the software pattern that usually carries the integration; `TSC7-Advanced-K6` (compute efficiency) is what makes the edge case viable.

### What is current as of November 2026

The integration story of 2025–26 was the normalisation of tool calling and the arrival of agent protocols that let one model call another system's tools without bespoke glue. Robotics moved from demos to supervised pilots in warehouses and labs. On the consumer side, assistant features moved into headsets, phones and cars, pushing inference to the device or a nearby edge node. Current frontier models differ less in raw capability than in how well they hold a structured contract over many turns, which is exactly the property an integration depends on.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Integration means calling the API from my app."* That is the easy half. The hard half is defining what the model may do and bounding the damage when it is wrong.
- *"A bigger model removes the need for grounding."* It lowers the rate of unsupported claims; it never removes the need.
- *"Integration is a research problem."* Mostly it is interface design and failure handling. Very little of it is novel modelling.

## How a student should understand it

**Mental model:** the model is a brilliant consultant on the phone. Everything else is the person holding the phone who can see the machine, press the button and stop the line.

**Three things they can do after this bullet:**
1. Draw the boundary: what the model decides, what the system decides, where the interlock sits.
2. Write a tool contract — inputs, outputs, failure behaviour — for one integration at work.
3. State the latency budget and say whether a model fits inside it.

**Misconceptions to kill:** that integration equals API calls, that scale substitutes for grounding, and that simulation and production carry the same risk.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The order-taker versus the cook.** The order-taker handles any customer, a changed order, a suggestion. The cook has a wok at 200°C and cannot un-burn a dish. You do not let the order-taker reach into the wok. Where it breaks: in a real stall the two talk constantly; in software the interface must be written down, because nothing is inferred from eye contact.

**The polyclinic triage nurse.** Screens, suggests, routes — but a doctor signs off anything with consequence. Good triage makes the doctor faster; it does not replace the signature.

### Worked example with a real tool

A facilities team wants an assistant that reads sensor alerts and proposes maintenance actions. Get the contract written before any code:

```
We run 12 buildings. Sensors emit alerts like "AHU-3 supply air
temp 4C above setpoint for 40 min". We want an LLM to propose a
maintenance action.

Write the integration contract:
1. The JSON schema the model receives (only fields it needs).
2. The JSON schema it must return, including a confidence field
   and a "needs_human" flag.
3. Three rules the surrounding system must enforce regardless of
   what the model returns.
4. What happens when the model returns invalid JSON.
```

What to point at afterwards: learners write rule 3 as "check the model's answer", which is not a rule. Push until they produce checkable ones — the action must reference an asset ID that exists, the work order must fit the maintenance window, low confidence routes to a human. That is the difference between a demo and an integration.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a short clip of a robot arm halting on a human gate; why does the gate exist?
2. **State the objective** — produce a written integration contract with a real interlock.
3. **Recall prior learning** — tool calling from `TSC6-Basic-K1`; what does an API already guarantee?
4. **Present the content** — grounding, latency, consequence; then the contract pattern.
5. **Guide** — fill in the building-alert contract on the whiteboard.
6. **Elicit performance** — groups draft a contract for their own system.
7. **Give feedback** — swap; the receiving group tries to break the interlock.
8. **Transfer** — each learner names the integration worth piloting and its interlock.

## What the framework doesn't mention but trainers need to know

- **Integration cost sits in the boring parts:** schema versioning, retries, timeouts, logging, slow-model handling.
- **The verifier is the product.** Anything that matters needs something able to say "no" without a model's opinion.
- **Data rights travel with the sensor.** A camera on a headset in a Singapore office collects personal data; PDPA obligations do not pause because inference is on-device.

## Watch out

- **Do not demo a robot you do not control.** A stage failure teaches the room this is theatre.
- **Do not let "emerging technology" become a buzzword list.** Anchor every example in a constraint.
- **Do not overclaim autonomy.** If a human supervises, say so.
- **The stale claim to retire:** "the model is the system." In 2026 the model is a component with a contract, and the contract is what you are paid to design.
