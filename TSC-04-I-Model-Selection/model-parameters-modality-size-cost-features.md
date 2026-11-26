---
id: 04.02.I.K3
tsc: 4
level: Intermediate
code: K3
title: Model parameters — modality, size, cost, features
as_at: 2026-11-26
review_by: 2027-02-25
---

# Model parameters — modality, size, cost, features

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K3**

> **Framework text (verbatim):** "Model parameters for different use cases (e.g., modality, size, cost, features)."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Knowledge · Bullet 3 of 11

**One-line version:** Four dials decide a model's fit — what it can perceive, how much it knows, what it costs, and what it can be wired into — and the use case, not the leaderboard, sets the acceptable position on each.

## What it is

Model selection reduces to a comparison across four dimensions. **Modality** is what goes in and what comes out: text, image, audio, video, embeddings. **Size** is capability class — edge, small, mid, frontier — usually proxied by parameter count. **Cost** is the per-token price for input and output, plus the discounts for cached input and batch work. **Features** are the operational extras: context window, native tool calling, strict structured output, caching, fine-tuning support, data residency and retention terms.

## Deep expansion

### The concept

Each dial trades against the others, and the trade is not linear. Size buys breadth of knowledge and robustness on ambiguous cases; it costs money and latency. Features buy engineering simplicity; they are usually the cheapest improvement available. Modality is a hard gate — if the task is "read this scanned invoice", a text-only model is not a compromise, it is a non-starter.

The selection method that follows from this: **gate on the hard constraints first, then optimise on the soft ones.** Modality, residency and regulatory terms are gates. Size, cost and latency form a Pareto frontier — several models will be acceptable, and the right one depends on which of the three your application actually feels.

### The sub-concepts

**Modality is a gate, not a score.** Text-to-text, vision, audio, embeddings and multimodal-native are different products. Native multimodal models read the raw image and preserve layout — tables, stamps, handwriting — that an optical character recognition step destroys before the language model ever sees it. For scanned Singapore invoices and forms, this difference is the whole task.

**Size has tiers, and narrow tasks saturate early.** Edge models under a few billion parameters for on-device work; small models around seven to fourteen billion that handle classification, extraction and summarisation well; mid-size models for multi-step reasoning; frontier models for open-ended, ambiguous, high-stakes work. Most enterprise volume belongs in the small and mid bands. Using a frontier model to route support emails is a cost decision masquerading as a quality decision.

**Output tokens cost more than input tokens.** Generation is sequential and memory-bandwidth bound, which vendors price at a multiple of input — commonly several times. Long-form answers are output-priced. Cached input and batch tiers attack the input and scheduling sides respectively.

**Latency has two halves.** Time to first token reflects reading the prompt; time per output token reflects writing the answer. A voice interface needs the first under a few hundred milliseconds; a background extraction job needs neither.

**Features are where money is quietly saved.** Strict structured output removes brittle parsing code. Prompt caching discounts repeated static content. Batch endpoints discount asynchronous work. Native tool calling removes glue. None of these change model quality; all of them change project risk and cost.

**Context window: declared versus effective.** A large window means the API will not error. It does not mean the model reasons reliably across all of it — accuracy on facts buried in the middle degrades, and prefill cost and latency rise with length. Use the window for what fits naturally, not as a substitute for retrieval.

### How it connects to the rest of the framework

`TSC4-Intermediate-K1` explains the mechanics behind each dial. `TSC4-Intermediate-A1` is the practice: run one task on two models, compare quality and price. `TSC4-Advanced-K4` prices the lifecycle. `TSC4-Intermediate-A3` is the residency and retention gate in detail. `TSC4-Advanced-A2` is how you prove the smaller model actually meets the bar rather than assuming it.

### What is current as of November 2026

Current frontier models have flattened the quality dimension and steepened the others:

- **Every major family now sells tiers, not a single model.** A fast cheap tier and an expensive reasoning tier of the same generation. Choosing the tier is now a larger cost decision than choosing the vendor.
- **Modality converged into one endpoint.** Vision, audio and text arrive together on the frontier products, so "which modality" is often answered by "the same model, different input".
- **Caching and batch are standard.** Ignoring them is now a straightforward overpayment rather than a missed optimisation.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The biggest model is the safest choice."* It is the safest choice for quality and the worst for cost, latency and carbon. Most tasks do not need it.
- *"Cost is a finance problem."* Cost is a design parameter. It determines what is feasible to scale.
- *"A big context window means I do not need retrieval."* It means you can fit more; it does not mean the model will find it.
- *"Open weights are free."* Licensing may be free; the hardware, the engineer and the idle hours are not.

## How a student should understand it

**Mental model:** renting a vehicle. A lorry, a van and a motorcycle all deliver parcels; the parcel size decides which you may use, and the delivery volume decides which you should.

**Things they can do after this bullet:**
1. Name the four dials and give a work example of each constraining a choice.
2. Gate a candidate list on modality and compliance before comparing quality.
3. Justify a smaller tier with a cost-per-outcome argument.

**Misconceptions to kill:** that bigger is better, that cost is someone else's problem, and that a feature list is marketing rather than engineering.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The polyclinic and the specialist.** A general practitioner handles most cases quickly and cheaply; a senior consultant at a specialist centre is the right call for the difficult minority. Nobody proposes sending every patient to the consultant — the queue alone would kill the system.

**The delivery fleet.** Modality is vehicle type (a motorcycle cannot carry a sofa), size is load capacity, cost is per-trip charge, features are whether it has a tail-lift and can take card payment.

### Worked example with a real tool

Give the room a constraint set and make them choose:

```text
Task: draft 500 marketing emails a day. Budget ceiling: $0.01 per email.
Constraint: brand tone must be consistent. Which of the four dials
dominates your choice, and what would make you revisit the decision?
```

What to point at afterwards: cost dominates, but not alone — a small model with two tone examples in the prompt will meet the bar, and revisiting happens when quality complaints appear, not when a new model launches. Then change one dial and rerun the reasoning:

```text
Same task, but every email must also read a scanned supplier invoice
and quote the total. Which dial now dominates, and what breaks?
```

The room should notice modality has become a gate: the invoice needs a vision-capable model, which changes both the cost ceiling and the viable tier list.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a price table for three tiers and ask what the cheapest one cannot do.
2. **State the objective** — by the end you can gate a candidate list and defend the tier you chose.
3. **Recall prior learning** — tokens as the unit of billing.
4. **Present the content** — the four dials, gates versus frontier, the two latency halves.
5. **Guide** — walk the email scenario together, dial by dial.
6. **Elicit performance** — pairs run the second scenario with the invoice requirement added.
7. **Give feedback** — debrief, especially choices that ignored modality until it broke.
8. **Transfer** — each learner writes the four-dial constraint set for one real task.

## What the framework doesn't mention but trainers need to know

- **Compliance is a fifth dial that overrides the other four.** Data residency, retention and training opt-out can eliminate the cheapest and best option entirely. Check it first or waste a week.
- **Vendor lifecycle is a dial too.** Snapshots retire within roughly a year; rate limits cap throughput by spending tier. A model you cannot pin is a model you cannot rely on.
- **The cheapest change is usually a feature, not a model.** Structured output, caching and batch often beat switching tiers on both cost and reliability.
- **Benchmarks do not cover your distribution.** The four dials tell you what is plausible; only your own test set tells you what works.
- **Carbon and procurement rules are arriving.** Some Singapore public-sector buyers now ask sustainability and residency questions alongside price.

## Watch out

- **Do not present a live price list.** Prices move quarterly; teach the structure of the bill and where to look it up.
- **Do not let "we need the best model" pass unchallenged.** Ask what the task requires and what "best" would buy.
- **Do not demo only text tasks.** Modality gating is the most commonly skipped step and the most expensive to discover late.
- **The stale claim to retire:** "there is one best model." In November 2026 there is a best model per constraint set, and the constraint sets differ.
