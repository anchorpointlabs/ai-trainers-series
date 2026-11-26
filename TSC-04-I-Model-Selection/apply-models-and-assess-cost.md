---
id: 04.02.I.A1
tsc: 4
level: Intermediate
code: A1
title: Apply models and assess cost
as_at: 2026-11-26
review_by: 2027-02-25
---

# Apply models and assess cost

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A1**

> **Framework text (verbatim):** "Apply different generative AI models for different use cases, and assess cost across different models available."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Ability · Bullet 6 of 11

**One-line version:** The right model is the cheapest one that clears your quality bar — and you cannot know either number without running the same task twice and pricing it.

## What it is

Two skills in one bullet. **Apply** means matching a model to a use case on the four dials — modality, size, cost, features. **Assess cost** means producing a number for a real workload: tokens in, tokens out, turns per task, calls per outcome, times volume, with caching and batch discounts applied where the workload allows. Quality and cost are then read together, because neither is a decision on its own.

## Deep expansion

### The concept

Cost is not a footnote to quality; it is one of the three axes that define a workable system, alongside latency. An accuracy figure with no price attached is a laboratory result. The practitioner's question is always *"is the cheapest model that meets the bar cheaper than the one I am using?"* — and that question requires (a) a bar, defined in advance, and (b) a cost model, built from the workload rather than from a price list.

The discipline that makes this teachable is the **Pareto view**: plot candidates on quality, latency and cost. Usually one or two models dominate — no other model is both better and cheaper — and everything else can be discarded without argument.

### The sub-concepts

**Define the bar before comparing.** "90 per cent acceptable" is a bar; "as good as possible" is not. Without a bar, every comparison ends in "the bigger one looked nicer".

**Build the cost model from the workload.** Identify: average input tokens, average output tokens, turns per interaction, calls per completed task, and monthly volume. Output tokens usually cost several times input tokens, so a long-answer task is dominated by the output side. Conversations re-send history each turn, so a ten-turn exchange costs more than ten times a one-turn exchange.

**Apply the discounts the workload allows.** Cached input for stable prefixes; batch endpoints for asynchronous, non-urgent work at roughly half price. A workload that could use them and does not is overpaying by design.

**Use the right unit.** Cost per call is a vendor metric. Cost per resolved ticket, per document processed, per compliant answer is a business metric. When an agent takes eight calls and two retries to close one ticket, the per-call price is misleading.

**Price the alternatives honestly.** Self-hosted open weights replace a per-token cost with hourly GPU cost, engineering time and idle capacity. At low or spiky volume the arithmetic usually favours the API; the comparison should be shown, not asserted.

**Quality is measured, not assumed.** Two models, one task, the same prompt structure adapted minimally per family, scored against your own examples. Anything else is a preference dressed as an evaluation.

### How it connects to the rest of the framework

`TSC4-Intermediate-K3` supplies the four dials this ability manipulates. `TSC4-Intermediate-A6` is the comparison method — variants on one task. `TSC4-Advanced-K4` is the lifecycle-cost view for anything customised. `TSC4-Advanced-A2` supplies the diverse test set that makes the quality number trustworthy. `TSC4-Advanced-K1` explains why self-hosting has a fixed-cost floor.

### What is current as of November 2026

Across current frontier models, the shape of the cost decision has changed:

- **Tiers within a family now differ more in price than in capability on routine work.** Routing easy requests to the fast tier and escalating only hard ones is the standard pattern, and it is a design decision, not a finance one.
- **Caching and batch are on by default in mature stacks.** Their absence is now a sign of an immature build rather than a deliberate choice.
- **Reasoning tokens are billed.** A thinking mode can multiply token consumption for the same visible answer, so cost models written for 2025 assumptions understate spend.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Cheaper means worse."* Cheaper means cheaper. Whether it is worse is an empirical question about your task, and often it is not.
- *"Cost per call is the number."* Cost per outcome is the number. Retries, turns and agent steps all multiply.
- *"We will optimise cost after the pilot."* Cost is an architecture decision; retrofitting it means re-architecting.
- *"Open source is free."* The licence may be; the GPUs and the engineer are not.

## How a student should understand it

**Mental model:** booking a flight. Business class is not wrong; it is wrong for a $200 budget with a two-hour hop. The destination sets the requirement, the budget sets the class.

**Things they can do after this bullet:**
1. Run one task on two models and score both against a stated bar.
2. Build a cost estimate from workload shape, not from a price list.
3. Choose the cheaper model that meets the bar and defend it in one paragraph.

**Misconceptions to kill:** that quality justifies any price, that per-call price is the unit of comparison, and that cost can be tuned later.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Grab versus the MRT.** A private hire car is better for one urgent trip; the MRT is better for ten thousand commuters a day. Neither is "better" without the volume and the urgency attached.

**The catering decision.** A wedding for 300 does not order à la carte. Volume changes which option is rational, not which option is nicer.

### Worked example with a real tool

Put the arithmetic on the board and make the room commit:

```text
Model A: $0.01 per call, 95% quality.
Model B: $0.001 per call, 90% quality.
Volume: 100,000 calls; the task tolerates 90% quality.
Which do you pick, and what would change your answer?
```

What to point at afterwards: B, at a tenth of the cost, because the bar is met. Then change one variable at a time and let the room feel the pivot: raise the required bar to 94 per cent, and A returns; drop volume to 500 calls a month, and the difference is $4.50 and nobody should spend a meeting on it. That last point is the real lesson — most cost arguments are too small to matter, and the ones that matter are orders of magnitude.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two invoice totals for the same feature, three months apart.
2. **State the objective** — by the end you can price a workload and pick a tier with a one-line justification.
3. **Recall prior learning** — the four dials, and which one cost is.
4. **Present the content** — the bar, the workload cost model, discounts, cost per outcome, the Pareto view.
5. **Guide** — do the two-model puzzle together, then vary the bar.
6. **Elicit performance** — pairs price a realistic workload (input, output, turns, volume) and present a tier choice.
7. **Give feedback** — debrief, catching estimates that ignored turns or output length.
8. **Transfer** — each learner prices one workflow they own and states the dominant term.

## What the framework doesn't mention but trainers need to know

- **Turns are the hidden multiplier.** Chat and agents re-send history; a "cheap" per-call price becomes expensive per conversation. Model it before the pilot, not after.
- **Caching is a prompt-structure decision.** Static content first unlocks discounts. Content ordering is free to change and worth real money.
- **Evaluation itself costs money.** Running a few hundred cases on a frontier judge is a line item; at scale it is a monthly one.
- **The cheapest improvement is usually the prompt.** Trim retrieved context, tighten the output contract, drop examples that no longer earn their tokens.
- **Procurement sees the annual number.** Present it as a monthly recurring figure with a stated assumption set, or it will be rejected as speculative.

## Watch out

- **Do not quote prices from memory.** Teach the method and have learners look up current numbers in the session.
- **Do not compare models at different prompt qualities.** It is the most common invalid comparison in the room.
- **Do not let "we will start with the best model and optimise later" pass.** That is how a pilot becomes a cancelled programme.
- **The stale claim to retire:** "AI is expensive." For narrow, high-volume tasks in November 2026 it is often cheaper than the human process it replaces — and for the wrong architecture it is still ruinous. Both halves are true.
