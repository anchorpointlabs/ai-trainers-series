---
id: 04.03.A.K4
tsc: 4
level: Advanced
code: K4
title: Cost implications of fine-tuning and customisation
as_at: 2026-11-26
review_by: 2027-02-25
---

# Cost implications of fine-tuning and customisation

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K4**

> **Framework text (verbatim):** "Complexities of fine-tuning and customising AI models for specific tasks or outputs (including implications of models' size and features on the cost)."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Knowledge · Bullet 4 of 8

**One-line version:** A fine-tune is a subscription, not a purchase — you pay once to build it and then keep paying to keep it true.

## What it is

Customising a model carries four kinds of cost: the one-off build (data curation, training, evaluation), the standing inference cost (a custom model still charges per token, and a bigger model charges more of it), the maintenance cost (retraining when the domain moves or the base model is retired), and the hidden operational cost (the human who owns the pipeline forever). Pricing only the first is the standard enterprise mistake.

## Deep expansion

### The concept

Every cost question here decomposes into "per build" and "per month". The build is visible, quotable and easy to get approved. The per-month line is invisible until year two, when the domain has changed, the base model has been deprecated, and the person who wrote the training script has left.

Customisation also changes the *shape* of inference cost. A fine-tuned small model can replace a five-thousand-token prompt on a frontier model with a fifty-token prompt, which is a real and large saving — this is the distillation pattern, and it is the single most reliable cost lever in the discipline. A fine-tuned *large* model does the opposite: it adds a customisation premium on top of an already expensive per-token price.

### The sub-concepts

**Size is the first cost driver.** Per-token price rises steeply with capability tier. So does the cost of the training run, and so does the GPU memory needed to serve it. Choosing a mid-size model for a narrow task is not a compromise; it is usually the correct engineering decision.

**Data is the second, and it is mostly labour.** Curating a few thousand clean pairs, with human verification, is weeks of skilled work. Synthetic data lowers the cost and raises the risk: unverified synthetic examples teach the model the teacher's mistakes.

**Output tokens cost more than input tokens — often several times more.** Generation is sequential and memory-bandwidth bound, so vendors price output higher, commonly around three to five times input. A task that produces long answers is dominated by output price, not input price. Cached input and batch tiers (roughly half price for asynchronous work) attack the input side and the scheduling side respectively.

**Conversation history is re-sent every turn.** In multi-turn chat and agent loops, token consumption grows faster than the number of turns suggests, because each turn re-pays for the history. Long agent runs are where budgets die quietly.

**Self-hosting swaps a variable cost for a fixed one.** Rented GPUs bill hourly, idle or not, plus engineering time and egress. At low or spiky volume, per-token pricing almost always wins; at steady high volume with a small model, self-hosting can win. The crossover is a calculation, not an opinion.

**Maintenance is the cost nobody quotes.** Domain data changes, so the fine-tune goes stale. The base model is retired, so the adapter must be rebuilt. Each retrain implies a re-evaluation, a redeployment and a rollback plan. That is a recurring line item with a named owner.

### How it connects to the rest of the framework

`TSC4-Advanced-K2` explains which optimisation techniques reduce which cost — distillation cuts inference, quantisation cuts memory, adapters cut training. `TSC4-Advanced-K3` is the workflow that generates most of the recurring cost. `TSC4-Intermediate-A1` is the applied version: run one task on two models and price it. `TSC4-Advanced-K1` supplies the hardware economics behind the self-host decision.

### What is current as of November 2026

Across current frontier models, three pricing patterns now hold:

- **Tiering within a family is the norm.** Each vendor sells a fast cheap tier and an expensive reasoning tier of nominally the same generation. Most enterprise volume belongs on the cheap tier, with escalation only for hard cases.
- **Caching and batch tiers are standard, not premium.** Input caching at a large discount and asynchronous batch at roughly half price are available on every major platform. Teams that ignore them pay double for no benefit.
- **Reasoning tokens are billed.** A "thinking" mode can multiply the token count for a request while the visible answer stays the same length. Cost models written before reasoning tiers existed understate spend badly.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Fine-tuning is a one-off cost."* It is a recurring cost with a one-off entry fee. The domain drifts and the base model gets retired.
- *"Customising a big model makes it cheaper because the prompt gets shorter."* Only if you move to a *smaller* model. A fine-tune on a frontier model adds cost.
- *"Open weights mean free."* The licence may be free; the GPUs, the engineer and the idle hours are not.
- *"Cost per call is the metric."* Cost per *successful business outcome* is. An agent that takes eight calls and two retries to resolve one ticket is priced per ticket, not per call.

## How a student should understand it

**Mental model:** a company car versus a taxi. A fine-tuned model is a company car — a capital outlay, then road tax, servicing, insurance and a driver, every month, whether you drive it or not. A pay-per-token API is a taxi: expensive per trip, zero cost when you stay home. Which is cheaper depends entirely on how many trips you actually make.

**Things they can do after this bullet:**
1. Break a customisation into build cost, running cost and maintenance cost.
2. Explain why output length and conversation turns dominate the bill.
3. Argue for a smaller model with evidence rather than taste.

**Misconceptions to kill:** that fine-tuning ends when the model is trained, that a custom model is cheaper by definition, and that per-call price is the unit of comparison.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The company car and the taxi.** Above, and it holds up well because every learner has done this calculation for real. Where it breaks: a car depreciates predictably; a fine-tune can become worthless overnight when the vendor retires the base model.

**The renovation with a maintenance contract.** The quote is for the build; the contract is for the next five years. Any contractor who quotes only the build is quoting the easy half.

### Worked example with a real tool

Make the room do the arithmetic, then the judgement:

```text
A fine-tuned model must be retrained whenever the domain data changes.
What does that do to its lifetime cost? Answer in three bullets, then
name the one number a finance director will ask for.
```

What to point at afterwards: good answers convert a one-off into a recurring cycle — retrain, re-evaluate, redeploy — and the number finance asks for is cost per month at expected volume, not cost per training run. Then run the second half, which is the actual skill:

```text
Task: draft 500 marketing emails a day. Budget ceiling $0.01 per email.
Which model tier do you choose, and what would make you revisit it?
```

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two invoices: a $50 pilot month and a $150,000 rollout month, same system.
2. **State the objective** — by the end you can price a custom model across its lifetime and name the dominant driver.
3. **Recall prior learning** — the pre-train versus fine-tune distinction from two bullets back.
4. **Present the content** — the four cost buckets, token economics, the self-host crossover.
5. **Guide** — work the company-car calculation on the board with round numbers.
6. **Elicit performance** — teams price a scenario and defend the tier they chose.
7. **Give feedback** — debrief, especially the teams that priced only the build.
8. **Transfer** — each learner writes the monthly cost line for one system in their own organisation.

## What the framework doesn't mention but trainers need to know

- **Cost is multiplicative, not additive.** Users × prompt size × turns. A pilot with twenty users hides the multiplication entirely, which is why pilots are so often followed by shocks.
- **The cheapest lever is usually retrieval hygiene.** Stuffing forty thousand tokens of context into every call is a design choice with a price tag. Retrieve less, better.
- **Evaluation has a cost too, and it is not optional.** The evaluation set, the judge model and the human review hours are part of the programme budget.
- **"Cost reduction" projects usually mean distillation.** Framing it that way makes the conversation honest: you are trading a maintenance burden for a training burden.
- **Retirement is a cost event.** When a vendor retires a snapshot, the migration is engineering time you did not plan for. Charge it to the model, not to the team.

## Watch out

- **Do not quote current prices.** They change quarterly and a stale figure in a slide becomes an argument you lose. Teach the structure of the bill.
- **Do not let "cheaper" mean "worse".** The correct claim is "meets the bar at lower cost", and the bar must be defined first.
- **Do not skip the maintenance line to make a business case look good.** It returns as an overrun.
- **The stale claim to retire:** "we will optimise cost after launch." Cost is an architecture decision; retrofitting it means re-architecting.
