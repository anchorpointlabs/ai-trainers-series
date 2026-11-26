---
id: 08.02.I.A2
tsc: 8
level: Intermediate
code: A2
title: Assess environmental impact
---

# Assess environmental impact

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A2**

> **Framework text (verbatim):** "Assess environmental impact (e.g., estimate energy footprint)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 7 of 14

**One-line version:** You cannot manage a footprint you never put on a dashboard — estimate it, state the assumption, and let the number change one decision.

## What it is

Assessing environmental impact means estimating the energy, water and carbon consequence of a model choice, alongside cost and quality, and using that estimate in a real decision. It is an estimate with declared assumptions, not a measurement programme: three numbers multiplied together, compared to the alternative, and recorded.

## Deep expansion

### The concept

The instinct when this topic comes up is to say it cannot be measured precisely, and therefore to defer. That instinct is how a real cost disappears from a decision. Assessment is not metrology; it is arithmetic at the resolution the decision needs. If you are choosing between a small and a frontier model for the same task, you do not need a carbon audit — you need to know that one is dramatically more expensive per call and that the difference multiplies by your monthly volume.

The arithmetic is short. Take call volume, tokens per call, and energy per unit from the provider or a published estimate. Multiply. Multiply again by the number of months the system will run. Then do the same for the smaller alternative and compare. The uncertainty is large, and it almost never changes the direction of the answer, which is the point: this is a decision tool, not a compliance number.

The second idea is that assessment has a boundary. Training is paid once and mostly by the provider; inference is paid continuously and mostly by you. Water is consumed at the data centre, usually far from the user. Chips carry an embodied footprint that no meter records. State which boundary you are assessing, because two teams comparing "the footprint" while measuring different boundaries will always disagree.

### The sub-concepts

**Scope and boundary.** Training versus inference; your emissions versus the provider's (which land in your Scope 3); operational versus embodied. A number without a boundary is not a number.

**A per-unit metric.** Energy per 1,000 requests, carbon per ticket resolved, kilowatt-hours per active user. Per-unit metrics survive growth and make alternatives comparable; totals do not.

**The right-sizing test.** Take the hardest 100 cases in your workload, run the small model, and count how many it gets wrong that the frontier model gets right. If the answer is a handful, the frontier model is not buying you quality — it is buying you insurance you have not priced.

**Cascade economics.** Route the easy majority to a small model and escalate on low confidence or explicit failure. Cascades usually capture most of the quality at a fraction of the cost, and the escalation rule is the whole design.

**Water and location.** Cooling dominates a tropical data centre's water use, which makes siting and cooling design a local issue rather than a global average. Singapore's land, power and water constraints make this the most concrete version of the lesson for a local class.

**Honest uncertainty.** Report a range and the assumption behind it. A precise number from a bad assumption is worse than a range from a good one, because it invites false confidence.

### How it connects to the rest of the framework

`TSC8-Intermediate-K2` is the knowledge behind this ability. `TSC8-Intermediate-A1` lists sustainability among the checks to run at each stage, and this is how that check is actually performed. `TSC8-Intermediate-K1` connects through proportionality: a system whose footprint exceeds the value of the problem fails on more than one axis. `TSC8-Intermediate-A7` matters when you ask whether a framework's sustainability dimension gives you anything measurable — usually it does not, so you build the metric yourself.

### What is current as of November 2026

Tiering has become the practical lever. The GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon are each offered at several capability and price points, and price per token remains the most reliable public proxy for relative compute. Publishing a sustainability summary is now normal for providers; publishing it in a comparable unit is not, so cross-vendor comparison is still a judgement call.

Two shifts matter. Agentic workflows have multiplied inference volume — a task that was one call is now a loop with retries — so volume estimates written last year are usually too low. And small models have improved sharply on narrow tasks, which means the cheap option is now a defensible engineering choice rather than a compromise.

### Common misconceptions

- *"We do not train models, so we have no footprint."* Inference is the recurring cost, and it is yours.
- *"Renewable certificates cancel it."* They address a specific boundary under a specific accounting method. They do not reduce the water or the chips.
- *"It cannot be measured, so it cannot be managed."* It can be estimated well enough to change a decision, which is all the decision requires.
- *"The biggest model gives the best answer."* It gives the best answer on hard tasks and an expensive answer on easy ones.

## How a student should understand it

**Mental model:** the utility bill versus the receipt. The receipt tells you what one call cost; the bill tells you what the building did last month, and the bill is the number that gets noticed.

**Things they can do after this bullet:**
1. Estimate the relative footprint of two model choices for one workload, with the assumption stated.
2. Choose a tier and defend it on quality, cost and footprint together.
3. Name the three numbers they would need to collect to replace the estimate with a measurement.

**Misconceptions to kill:** that no training means no footprint, that certificates erase it, and that imprecision justifies ignoring it.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Taking a taxi to buy one packet of tissue.** The trip works. It is also absurd for the errand, and everybody recognises the absurdity instantly once it is named. A frontier model tagging an email category is the same trip. Where it breaks: the taxi fare is visible, whereas an oversized model call is buried in a monthly bill nobody reads.

**The office air-con left on overnight.** Everyone has seen the bill, nobody has seen the compressor. The consumption happens somewhere else, at a scale you do not witness, and it is real anyway.

### Worked example with a real tool

```text
Workload: 250,000 short customer messages a month, each needing one of eight categories.

Estimate the relative energy of doing this with a small model versus a frontier model.
Show the arithmetic symbolically: energy = calls x tokens per call x energy per token.
Do not invent figures — leave each term as a named variable with the unit I need to find.

Then: what is the escalation rule that would let me use the small model for most traffic
without losing quality, and what would I measure to know the rule is working?
```

What to point at afterwards: the formula, not the answer. Learners copy a number from a chatbot and defend it in a meeting; the formula is what survives the meeting. Point at the escalation rule too — without one, volume quietly migrates to the expensive tier and the savings never appear.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask how many model calls the last "quick" AI task made. Most rooms guess one.
2. **State the objective** — by the end you can estimate relative footprint and defend a tier choice.
3. **Recall prior learning** — connect to price per million tokens, which they already use.
4. **Present the content** — boundary, per-unit metrics, right-sizing test, cascade.
5. **Guide** — build the estimation formula on the board with the class.
6. **Elicit performance** — pairs estimate their own workload and propose a tier.
7. **Give feedback** — challenge any estimate with no stated assumption.
8. **Transfer** — each learner adds one footprint metric to a dashboard they own.

## What the framework doesn't mention but trainers need to know

- **Most of the footprint is Scope 3**, which means procurement holds a lever that engineering does not.
- **The rebound effect is real.** Cheaper inference increases usage; efficiency gains get spent rather than banked.
- **Reported figures use different boundaries.** Teach the boundary question before the number, or learners will compare incomparable claims.
- **The strongest lever is demand.** First ask whether the feature should exist, then which tier serves it, then how to make the call cheaper.

## Watch out

- **Do not quote an energy-per-prompt figure you cannot source.** It is the fastest way to lose an engineer's respect in this lesson.
- **Do not call a model "green".** Versions change quarterly; the claim does not survive.
- **Do not let the lesson become an argument for under-serving users.** Fitness for purpose is the standard, not the smallest possible model.
- **The stale claim to retire:** "AI is free to run once it is built." Inference is metered, and agents meter it faster.
