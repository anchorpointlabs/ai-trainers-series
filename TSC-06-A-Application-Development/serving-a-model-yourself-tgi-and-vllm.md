---
id: 06.03.A.A2
tsc: 6
level: Advanced
code: A2
title: "Serving a model yourself: what TGI and vLLM actually buy you"
---

# Serving a model yourself: what TGI and vLLM actually buy you

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A2**


> **Framework text (verbatim):** "Deploy generative AI models for inference using serving infrastructure (e.g., Text Generation Inference (TGI)/ Virtual Large Language Model (VLLM))."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 7 of 12

**One-line version:** A serving stack turns a set of weights into a dependable endpoint — batching, cache management, sharding and metrics — and your job is the capacity plan and the operations around it.

## What it is

This is the ability to take an open-weight model and put it behind an inference server: TGI, vLLM or a peer, running on your own GPU or a rented one, exposing an API your application can call. It covers the launch configuration, the capacity arithmetic, the health and scaling behaviour, and the version discipline that makes an endpoint something you can promise a service level for.

## Deep expansion

### The concept

Loading weights and calling `generate()` works for one user. A serving stack exists because of what happens at the hundredth concurrent user: the device idles while requests wait, memory fragments as conversations grow, and one long prompt starves everyone behind it.

The stack solves four problems. It **batches** work continuously so the GPU is never waiting for a single sequence. It **manages the key-value cache** in pages rather than contiguous blocks, so memory can be reused as requests finish. It **shards** a model too large for one device across several. And it **exposes** the operational surface — metrics, health, streaming — that an application needs to be run rather than demonstrated.

The Advanced judgement is deciding whether to self-host at all. Self-hosting is justified by data residency, by a fine-tuned model nobody else hosts, by a steady load where the arithmetic beats per-token pricing, or by latency requirements a public endpoint cannot meet. It is not justified by "cheaper" in the abstract, because the fixed cost — GPU hours, idle capacity, upgrades, someone on call — is paid whether or not traffic arrives.

### The sub-concepts

**Continuous batching.** Requests join and leave the running batch as they arrive and finish, instead of waiting for a fixed group. This is the single largest throughput gain over naive serving, and it is on by default in every serious stack.

**Paged cache management.** The key-value cache is allocated in fixed-size blocks, so a long conversation does not need one contiguous reservation. It is also what makes prefix sharing practical: a common system prompt can be cached once and reused across requests.

**Sharding.** Tensor parallelism splits each layer across devices; pipeline parallelism splits layers into stages. Both need fast interconnect to be worth it. The first question is always "does it fit on one device at 4-bit", because one device is simpler to operate than two.

**The memory flags.** Maximum sequence length, fraction of device memory the server may claim, and maximum concurrent sequences are the real levers. They are not tuning details: setting the sequence length to the model's maximum on a device that cannot hold the resulting cache is the most common self-inflicted outage.

**An OpenAI-compatible surface.** Most stacks expose the same request shape as the major vendors. Keep it, and your application can switch between self-hosted and managed backends with a base URL — which is also how you migrate off in a hurry.

**Streaming and time to first token.** Users judge speed by the first word, not the last. Server-sent token streaming and a warm model matter more to perceived latency than raw tokens per second.

**The operational surface.** Health endpoint, warm-up on start, metrics (queue depth, cache utilisation, tokens per second, time to first token, time per output token), graceful drain, autoscaling on queue depth rather than CPU, and a pinned model version in the response headers.

### How it connects to the rest of the framework

`TSC6-Advanced-K1` explains every technique the server implements — quantisation, batching, caching — so this ability is that knowledge made operational. `TSC6-Advanced-A1` consumes this endpoint as one hop in a multi-model design. `TSC6-Advanced-K4` is how you notice it degrading: queue depth and time to first token are the signals. `TSC4` supplies the model-selection judgement that precedes the deployment decision.

### What is current as of November 2026

- **The stacks converged on the same feature set.** Continuous batching, paged cache, prefix caching and OpenAI-compatible APIs are table stakes in vLLM, TGI and their peers; the differences now are quantisation support, multi-GPU ergonomics and stability under odd workloads. Check the current release notes rather than trusting a course slide.
- **Self-hosting is usually a data or customisation decision**, not a cost decision. Managed endpoints for open-weight models are widely available and often cheaper at low and bursty volume.
- **Open-weight models are good enough for narrow production tasks**, which is what made self-hosting common outside research labs.
- **GPU capacity is rented by the hour and priced by the generation**, so capacity planning is now a monthly financial exercise, not a one-off procurement.
- **Fine-tuned weights force self-hosting or a managed fine-tune service**, and that is the most common reason teams end up operating a server.

### Common misconceptions

- *"Self-hosting is cheaper."* Only at sustained utilisation. Idle GPU hours are the most expensive form of caution.
- *"vLLM and TGI are interchangeable."* They are close, but features, quantisation support and defaults differ, and those differences decide incidents.
- *"Deployment is launching a container."* Deployment is warm-up, health checks, limits, versioning, rollback and monitoring. The container is the easy part.
- *"Set max length to the model maximum."* That reserves cache you cannot afford and turns a documentation example into an outage.

## How a student should understand it

**Mental model:** the hawker centre's central kitchen. One kitchen cooks for twenty stalls on a schedule, with portion control and a dispatch board. The stalls do not each need a wok — but the kitchen must be sized for lunch, not for a quiet Tuesday.

**Three things they can do after this bullet:**
1. Write a launch configuration for a stated model and device, and justify each memory flag.
2. State the three metrics that tell you the endpoint is saturated.
3. Decide, with reasons, between self-hosting and a managed endpoint for a given case.

**Misconceptions to kill:** self-hosting is cheaper, the stacks are interchangeable, and deployment ends at container start.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The central kitchen.** Twenty stalls, one kitchen, one dispatch board. Batching is cooking four orders of the same dish together; the dispatch board is the queue; the portion scale is the memory flag. Where it breaks: a central kitchen can hold stock, while a GPU cannot — unused capacity is lost every second.

**The MRT depot.** Trains are serviced, staged and dispatched from a depot with a timetable. Nobody measures the depot by how many trains it owns, but by how many it can put on the line at 7am. Throughput at peak, not fleet size, is the number.

### Worked example with a real tool

Ask for the command, then for the method:

```
I have 2 × L4 24 GB GPUs and an open-weight 8B instruct model that fits
on one card at 4-bit. I want OpenAI-compatible serving.

1. Give me the vLLM launch command with tensor parallelism, maximum
   sequence length and memory utilisation set, and explain each flag.
2. Roughly how many concurrent 2k-context requests will it hold before
   p95 time-to-first-token passes 3 seconds?
3. What do I measure to find out for real, and what do I change first
   if it does not hold?
```

What to point at afterwards: the flags are plausible and the concurrency estimate is a guess dressed as arithmetic. The honest answer to question two is "measure it" — and question three is the actual ability. Point at `--tensor-parallel-size` with two cards for a model that fits on one: that halves capacity for nothing, and it is exactly the mistake the exercise is designed to surface.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a demo that is instant for one user and eight seconds for the tenth. Ask what changed.
2. **State the objective** — you will configure, size and monitor an inference endpoint.
3. **Recall prior learning** — they know batching and cache costs from K1; now those become flags.
4. **Present the content** — the four problems a server solves, and the operational surface.
5. **Guide** — set the flags for the 8B model together, computing the cache first.
6. **Elicit performance** — pairs produce a launch command and a three-metric dashboard.
7. **Give feedback** — correct the pair who set maximum length, and the pair who used two GPUs unnecessarily.
8. **Transfer** — they write a one-page runbook: start, warm, check, roll back.

## What the framework doesn't mention but trainers need to know

- **Warm-up is mandatory.** The first requests after start are slow; send synthetic ones before the load balancer admits traffic.
- **Autoscale on queue depth, not utilisation.** GPU utilisation looks healthy while requests queue.
- **Drain gracefully.** Killing a server mid-generation fails requests that were almost finished; stop accepting, finish the batch, then exit.
- **Pin and canary model versions.** A silent upgrade changes answers; serve the new version to 5% and compare.
- **Cost per thousand tokens is the number to report**, not GPU hours. It is the only figure a business sponsor can compare against an API bill.

## Watch out

- **Do not demo production serving on a laptop.** It creates a false sense of what the operational surface costs.
- **Do not quote throughput numbers from a blog post.** Model, quantisation, context length and hardware all change the answer.
- **Do not present self-hosting as the advanced choice by default.** The advanced choice is the one whose total cost and risk you can state.
- **The stale claim to retire:** "you need a dedicated MLOps team to serve a model." In November 2026 one engineer with a runbook serves a narrow workload; the discipline is in the runbook, not the headcount.
