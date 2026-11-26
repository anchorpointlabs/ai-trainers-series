---
id: 08.02.I.K2
tsc: 8
level: Intermediate
code: K2
title: Environmental impact of generative AI
as_at: 2026-11-26
review_by: 2027-02-25
---

# Environmental impact of generative AI

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Knowledge K2**

> **Framework text (verbatim):** "Environmental impact of generative AI use (e.g., energy consumption)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Knowledge · Bullet 2 of 14

**One-line version:** Every token is electricity and water somewhere — which makes the cheapest ethical decision in generative AI the same as the cheapest financial one: use the smallest model that clears the bar.

## What it is

Training and running generative models consumes electricity for compute, water for cooling, and hardware that is mined, shipped and discarded on a short refresh cycle. For a working developer the consequence is narrow and practical: model choice is an environmental decision, and at production volume the recurring cost of *inference* usually dwarfs the one-off cost of training.

## Deep expansion

### The concept

The environmental impact of generative AI has two phases and one bill. **Training** is a large, one-time expenditure of compute: a frontier model is trained once, at enormous cost, and then served to millions. **Inference** is small per call and repeated forever. An organisation that never trains a model still pays the inference bill, and an organisation that runs an agent pays it many times per task, because a single user request can become a dozen or a hundred model calls as the agent plans, searches, reads and retries.

That asymmetry is what makes this a developer's bullet rather than a policy bullet. You cannot influence how a frontier lab trains its model. You can decide, every time you write a line of code, which tier answers the question — and that decision is the largest lever most teams actually hold.

The second thing to teach is that the footprint is not one number. It is energy (kilowatt-hours), water (evaporative cooling, which matters more in a tropical data centre than in a temperate one), and embodied carbon (the chips themselves, replaced on a cycle far shorter than a building's). A provider that reports one of the three is not reporting the footprint.

### The sub-concepts

**Two phases, two different problems.** Training is a capex event with a carbon debt paid up front; inference is an opex stream that grows with adoption. Efficiency work that reduces training cost does nothing for a product whose users triple.

**Right-sizing.** The single most useful habit: match model capability to task difficulty. Classification, extraction, tagging, routing and short summarisation are usually well served by a small model. Multi-step reasoning, ambiguous instructions and long-context synthesis are where the frontier tier earns its cost. A cascade — small model first, escalate only on low confidence or explicit failure — gets most of the quality at a fraction of the spend.

**Water and land.** Data centres in Singapore compete for land, power and water like any other large industrial user. Cooling design therefore has a local regulatory dimension as well as a global one; the industry has standards for tropical data centres precisely because the default assumptions were written for colder places.

**Embodied carbon and e-waste.** Accelerators are replaced every few years, and the manufacturing footprint is a real share of the lifetime total. This is the part learners never think about, and the part that makes "we bought renewable certificates" an incomplete answer.

**Measurement units.** Energy per 1,000 inferences, tokens per joule, carbon per request. Providers report inconsistently and rarely in comparable units, so the practical skill is estimating from what you can observe — call volume, token counts, price per million tokens — and stating the assumption.

**The rebound effect.** When a model gets cheaper and faster, usage goes up. Efficiency gains are frequently spent on new use cases rather than banked. This is why "the model is more efficient now" is not an environmental argument on its own.

### How it connects to the rest of the framework

`TSC8-Intermediate-A2` is the ability version of this bullet: the estimating method and the decision it feeds. Sustainability is listed alongside fairness, accountability and transparency in `TSC8-Intermediate-A1`, so it belongs in the same checkpoint rhythm as the other three. It also connects back to `TSC1-Basic-K1`: the fifth purpose of generative AI — *act* — is the most energy-intensive, because an agent multiplies calls. And it connects to `TSC8-Intermediate-K1` through proportionality: a system whose cost exceeds the value of the problem it solves fails on more than one axis.

### What is current as of November 2026

Model tiers are now explicitly priced and positioned for this decision. The GPT-6 generation spans small, mid and frontier variants (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber); Anthropic's Claude 5.5 line ships a fast tier alongside the flagship; Google's Gemini 3.1 Pro and Gemini 4 Argon sit at the top of its range. Choosing a tier is now simultaneously a quality, cost and energy decision, and the pricing page is the most reliable public proxy for relative compute per token.

Two shifts matter. First, agentic workflows have made inference volume the dominant term for many teams — a "single task" that used to be one call is now a loop, and loops do not stop when the answer is good enough unless you tell them to. Second, providers now publish sustainability summaries and, in some cases, per-request carbon estimates; they are not yet comparable across vendors, so treat them as directional rather than auditable.

### Common misconceptions

- *"Training is the whole footprint."* For a model you train once and serve a million times, inference dominates. For a model you fine-tune weekly and serve rarely, the reverse is true. Do the arithmetic for your own case.
- *"It runs in the cloud, so it is not our problem."* It is your Scope 3, and increasingly your customer's procurement question. "Not on my site" is not the same as "not in my inventory".
- *"One prompt is negligible."* True. A hundred thousand a day is not, and neither is an agent that makes forty calls per ticket.
- *"The biggest model is the safe choice."* It is the safe choice for quality on hard tasks and the wrong choice for everything else — including cost, latency and energy.
- *"Green claims from a provider are audited."* Some are, under specific reporting regimes; most marketing claims are not. Ask for the methodology before you quote the number.

## How a student should understand it

**Mental model:** the electricity meter on the wall, not the receipt in your hand. The receipt shows the price of one call; the meter shows what the building did all month.

**Things they can do after this bullet:**
1. Estimate the relative energy of two model choices for the same task and say what assumption the estimate rests on.
2. Choose a model tier for a workload and defend it on quality, cost and footprint together.
3. Name one metric they would add to a dashboard to make consumption visible to the team.

**Misconceptions to kill:** that energy is the vendor's problem, that bigger is automatically better, and that a single call does not matter.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The bus and the letter.** Sending one letter by hiring a 40-seat bus is not wrong in principle — it will definitely arrive — but it is absurd for the job. Running a frontier model to tag an email as "billing" or "technical" is the same decision. Where it breaks: a bus is visible and embarrassing, whereas an oversized model call is invisible and shows up as a line item nobody reads.

**Air-con in a shophouse versus a mall.** Everyone in Singapore understands that cooling is most of the bill and that the water goes somewhere you cannot see. A data centre is a mall-sized air-con load, and in the tropics the cooling design is not an afterthought. Where it breaks: you can switch off your air-con; you cannot switch off a shared inference endpoint.

### Worked example with a real tool

```text
I process 100,000 support emails a month. Roughly 70% are simple category tags,
20% need a short reply drafted, and 10% are complaints needing careful handling.

Design a routing plan across a small model, a mid model and a frontier model.
For each tier tell me: what share of traffic it takes, the escalation rule that moves
work upward, and how I would measure the energy I avoided.

Do not invent energy figures. Show the arithmetic symbolically, and list the three
numbers I would need to collect to fill it in.
```

What to point at afterwards: the model will produce a sensible cascade and then, if allowed, invent plausible-looking kilowatt figures. That invention is the teaching moment — the formula is the deliverable, the numbers are yours to collect. Point at the escalation rule: without one, everything drifts to the frontier tier and the plan collapses.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room how many model calls their last "quick" AI task actually made. Most will guess one; agents make dozens.
2. **State the objective** — by the end you can estimate relative footprint and defend a model-tier choice.
3. **Recall prior learning** — connect to cost per token, which they already know from pricing pages.
4. **Present the content** — two phases, three footprint components, right-sizing, the cascade.
5. **Guide** — build the routing table together for the email workload.
6. **Elicit performance** — each pair right-sizes one workload from their own organisation.
7. **Give feedback** — challenge every "we'd just use the best model" with a cost and volume question.
8. **Transfer** — each learner writes the one sentence they will add to their team's model-selection checklist.

## What the framework doesn't mention but trainers need to know

- **Your footprint is mostly Scope 3.** The emissions happen at the provider's site; they land in your inventory. That is why procurement, not just engineering, owns part of this.
- **The strongest lever is demand, not efficiency.** The first question is whether the feature should exist, the second is which tier serves it, and only the third is how to make the call cheaper.
- **Reported numbers are not comparable yet.** Different vendors measure different boundaries (training only, training plus inference, market-based versus location-based electricity). Teach the boundary question, not the number.
- **Small models are now genuinely good at narrow tasks.** The gap that justified "always use the frontier model" in 2023 has narrowed sharply for classification and extraction work.

## Watch out

- **Do not quote an energy-per-prompt figure you cannot source.** The most common error in this lesson is a confident number that a sceptical engineer will dismantle.
- **Do not call any specific model "green".** Model versions change every quarter; the claim does not survive the change.
- **Do not let sustainability become an argument for under-serving users.** The point is fitness for purpose, not the smallest possible model.
- **The stale claim to retire:** "AI is free to run once it is built." Inference is a metered utility, and agents meter it faster.
