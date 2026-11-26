---
id: 04.03.A.K1
tsc: 4
level: Advanced
code: K1
title: Where models run — large-scale and distributed clusters
as_at: 2026-11-26
review_by: 2027-02-25
---

# Where models run — large-scale and distributed clusters

> **TSC #4 Generative AI Model Selection · Advanced · Knowledge K1**

> **Framework text (verbatim):** "Applications and domains where generative AI models are used (e.g., large-scale and distributed computing clusters)."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Knowledge · Bullet 1 of 8

**One-line version:** The model you type into is running somewhere on a rack of GPUs, and the shape of that rack — not the benchmark table — sets the latency, throughput and price you can actually buy.

## What it is

Every generative model is served from graphical processing units (GPUs) sitting in a data centre. When a model is bigger than one GPU's memory, it is split across many machines and coordinated as a single service — that is a distributed cluster. Model selection is therefore never only a quality question: the hosting pattern you choose (a vendor's API, your own reserved GPUs, or an on-premise rack) fixes a floor on cost, a ceiling on latency, and a hard limit on how many requests per minute you can serve.

## Deep expansion

### The concept

A single modern accelerator holds tens of gigabytes of memory. A frontier model at sixteen-bit precision needs roughly two bytes per parameter just for its weights, before any working memory — which is why large models cannot live on one card. Serving them means splitting the work. There are three standard ways to split it:

- **Tensor parallelism** — cut each layer's weight matrices into slices, one per GPU, and exchange partial results every layer. Needs very fast interconnect, because the GPUs talk constantly.
- **Pipeline parallelism** — put different blocks of layers on different machines and pass activations down the line. Cheaper to wire, but the pipeline has bubbles unless it is kept full.
- **Data parallelism** — run whole copies of the model and give each copy different requests. This is the easy one, and it is what "scaling out" usually means.

A production cluster combines all three. The selection consequence is blunt: a model that needs four GPUs to fit has a four-GPU cost floor even when nobody is using it, and that floor is what makes self-hosting expensive at low volume.

### The sub-concepts

**Prefill versus decode.** Serving has two phases with opposite bottlenecks. Prefill processes the whole input in parallel and is compute-bound; decode emits output one token at a time and is memory-bandwidth-bound. Almost every latency number you care about traces back to which phase dominates.

**TTFT and TPOT.** Time to first token measures prefill plus network — the "did it hear me" delay. Time per output token measures decode speed. End-to-end latency is roughly TTFT plus TPOT multiplied by the number of output tokens, which is why long answers feel slow even on fast models.

**Throughput is not latency.** Batching more requests through the same GPUs raises tokens per second and can raise per-request wait. A batch job at 3 a.m. wants throughput; a voice agent at 2 p.m. wants latency. They are different products built on the same hardware.

**The KV cache is the memory hog.** Autoregressive generation stores attention keys and values for every token already seen, per concurrent request. That cache grows with context length and with concurrency, and in practice it exhausts GPU memory long before raw compute does. Techniques such as grouped-query attention and paged memory management exist mainly to shrink it.

**The utilisation trap.** Rented GPUs bill by the hour whether or not a request arrives. A cluster sized for the Monday morning peak sits idle the rest of the week. This single fact explains why per-token pricing so often beats self-hosting for spiky office workloads.

### How it connects to the rest of the framework

`TSC4-Advanced-K2` explains why some architectures (mixture-of-experts) need the memory of a giant model but the compute of a small one — that is a serving fact before it is an architecture fact. `TSC4-Advanced-K4` prices the lifecycle. `TSC4-Advanced-A4` is the operations question: can this setup survive twenty models and five updates a week. `TSC4-Advanced-A3` supplies the reliability lens, because a cluster that fails over badly is not reliable no matter how good the weights are.

### What is current as of November 2026

Current frontier models are all served from vendor clusters that you rent by the token, and none of them is something a mid-sized Singapore firm would host itself. Two serving-side shifts matter for this bullet:

- **Reasoning models changed the cost profile.** A model that emits thousands of hidden reasoning tokens before answering is decode-bound for far longer than a standard instruct model. Same question, same visible answer length, several times the GPU seconds. Latency budgets written for 2025 assumptions now fail.
- **Batch and cached tiers became normal.** Asynchronous batch endpoints at roughly half price, and prompt caching that discounts repeated input, moved the economics of high-volume document work. Selection now includes "which tier" as well as "which model".

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The model is one big computer."* It is a service spread across many accelerators, with a scheduler in front of it. That scheduler is why your request sometimes queues.
- *"Twice the GPUs means twice the speed."* Splitting work adds coordination cost. Past a point, more machines make a single request slower, not faster.
- *"Self-hosting is cheaper because there is no per-token fee."* There is a per-hour fee instead, and it runs all night.
- *"Throughput and latency are the same thing."* They trade against each other. Confusing them is how teams buy the wrong instance type.

## How a student should understand it

**Mental model:** an MRT system. Latency is how long you wait for the next train; throughput is how many passengers clear the platform per hour. Adding carriages helps throughput and does nothing for the person who just missed one.

**Things they can do after this bullet:**
1. Explain, without jargon, why a large model cannot run on a laptop and what a cluster does instead.
2. Name the three ways work is split across GPUs and what each one costs.
3. State which of latency, throughput or unit cost dominates for a given application, and why.

**Misconceptions to kill:** that scale is free and linear, that self-hosting removes cost rather than converting it, and that a fast demo predicts a fast production system.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker stall versus the central kitchen.** One stall (one GPU) cooks what fits on one wok. A central kitchen (a cluster) has many cooks who each do one step of the same dish and pass it along. It can feed a thousand people, but the coordination between stations is real overhead, and the kitchen's rent is paid whether or not anyone orders. Where it breaks: kitchens scale nearly linearly with cooks; attention does not, because every added GPU must exchange data with the others.

**The expressway with an ERP gantry.** Throughput is vehicles per hour past the gantry; latency is your own journey time. Widening the road raises throughput and can still leave you stuck.

### Worked example with a real tool

Ask the same model for a short and a long version of the same task, and time both:

```
Summarise this customer complaint in one sentence:
"I ordered on the 3rd, the parcel came on the 12th, the box was crushed,
and nobody answered my email. I want a refund and an apology."
```

Then, in a fresh message with the same text:

```
Now rewrite that summary as a 400-word explanation of what went wrong,
written for my operations manager.
```

What to point at afterwards: the input is identical, so the "reading" cost is identical — yet the long answer takes visibly longer to finish and streams in a steady trickle. That trickle is decode, one token at a time, and it is the single most useful intuition a non-engineer can carry into a latency budget.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — play a video of a data-centre hall, then ask: "where is ChatGPT when you close the lid?"
2. **State the objective** — by the end you can say which hosting pattern fits a given application and why.
3. **Recall prior learning** — revisit what a token is and that models predict one token at a time.
4. **Present the content** — the three splitting strategies, prefill versus decode, TTFT versus throughput, the utilisation trap.
5. **Guide** — work the MRT analogy through one real application the room recognises (a chatbot on a public website).
6. **Elicit performance** — pairs classify four scenarios (overnight invoice extraction, live voice bot, internal policy search, batch translation) as latency-bound or throughput-bound.
7. **Give feedback** — debrief, correcting the common error of treating all four as latency-bound.
8. **Transfer** — each learner names one system in their own organisation and states its binding constraint.

## What the framework doesn't mention but trainers need to know

- **Training clusters and inference clusters are different purchases.** Pre-training needs huge interconnected clusters for weeks; inference needs memory and concurrency. Learners who conflate them conclude that only the largest labs can run a model, which is false for inference.
- **Rate limits are a scale constraint you cannot buy your way out of instantly.** Requests per minute and tokens per minute ceilings sit on top of every commercial API, tiered by spend. A pilot that works at ten users can hit a wall at two hundred.
- **Residency decides which cluster you may use.** A Singapore-only data requirement can rule out a cheaper region entirely. That is a hosting question before it is a model question.
- **The cheapest architecture is usually the boring one.** A small model on a vendor API, with caching, normally beats a clever self-hosted cluster for office workloads under a few million calls a month.

## Watch out

- **Do not quote GPU prices or tokens-per-second figures from memory.** They move quarterly and a wrong number discredits the whole session. Teach the shape of the trade-off, not the current price list.
- **Do not let the room believe self-hosting is the "serious" option.** For most Singapore SMEs it is the expensive option, and saying so plainly saves a bad procurement decision.
- **Do not demo cluster dashboards.** They are unreadable at projector scale and teach nothing.
- **The stale claim to retire:** "the cloud scales infinitely." It does not; it scales to your quota, your budget and your region's capacity, in that order.
