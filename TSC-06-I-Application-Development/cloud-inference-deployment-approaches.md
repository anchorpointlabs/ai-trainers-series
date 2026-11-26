---
id: 06.02.I.K3
tsc: 6
level: Intermediate
code: K3
title: Five ways to serve a model from the cloud, and how to choose
as_at: 2026-11-26
review_by: 2027-02-25
---

# Five ways to serve a model from the cloud, and how to choose

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Knowledge K3**


> **Framework text (verbatim):** "Approaches to deploy models for inference using cloud platforms."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Knowledge · Bullet 3 of 12

**One-line version:** Nobody "deploys a model" in the abstract — you rent it per token, per hour or per machine, and the rent decides what you can promise your users.

## What it is

Deploying for inference means making a model answer requests from your application, over a network, at a reliability and cost you can defend. "Cloud platforms" covers everything from a vendor's managed endpoint to your own container on rented GPUs. The knowledge here is the menu, and the properties each item buys and costs.

## Deep expansion

### The concept

The framework says "approaches", plural, because the choice trades four variables that cannot all be maximised: **control**, **cost**, **latency** and **compliance**. The five a trainer should name:

1. **Vendor API endpoint.** You call the provider's hosted model. No infrastructure, per-token billing, the provider's upgrade schedule.
2. **Managed hosting on your cloud.** The model served inside your cloud account (Bedrock, Vertex AI, Azure AI Foundry style services), inheriting your identity, logging and network controls.
3. **Serverless function in front of a model.** A function holds the key, applies guardrails, returns a response. Never put a model key in a browser.
4. **Self-hosted on GPUs.** The model in a container on rented GPUs behind your own serving stack. Maximum control, real capacity planning.
5. **Batch inference.** A large job submitted to a discounted asynchronous endpoint, or run overnight on your own machines.

Each answers a different question. A prototype wants (1) or (2); a regulated product wants (2) or (4); a nightly corpus job wants (5); a fine-tuned model with no vendor offering wants (4).

### The sub-concepts

**Endpoint.** A URL and a contract. Region, authentication, rate limit and model version all hang off it.

**Region and residency.** Where the request is processed, physically. Singapore organisations frequently require customer data processed in-country, and some sectors impose it. Region choice is a compliance decision disguised as a dropdown.

**Secrets.** Keys in the platform's secret store, injected at runtime, scoped to one service, rotated. A key in a front-end bundle is a public key.

**Autoscaling and cold start.** How many requests are in flight, and what happens at the ceiling. Scaling that reacts in four minutes is not scaling for a chat interface; a large model on a fresh node takes seconds to minutes to wake.

**Quota.** Enforced per key and per model, raised by a support ticket rather than a config change. Quota is the ceiling on your product's traffic.

**Observability and versioning.** Request logs, token counts, latency, error rates, plus the ability to pin a model version and roll back.

### How it connects to the rest of the framework

`TSC6-Intermediate-K1` supplies the contract discipline; this is where that contract physically lives. `TSC6-Intermediate-A2` is the workflow that calls it, `TSC6-Intermediate-K5` the pipeline above it. At Advanced level, `TSC6-Advanced-A2` covers serving infrastructure — Text Generation Inference and vLLM — which is approach 4 in detail.

### What is current as of November 2026

The menu has not changed shape, but the pricing logic has inverted. Self-hosting was often cheaper at scale two years ago; provider prices have fallen faster than GPU rental, so self-hosting is now usually justified by *control* — residency, fine-tuned weights, guaranteed latency — rather than cost. Managed hosting inside the big clouds has become the default enterprise answer because it inherits identity and private networking, and batch endpoints are now materially cheaper than synchronous calls, which has moved much back-office work off the synchronous path.

### Common misconceptions

- *"Cloud means someone else runs it, so capacity is their problem."* You still own the quota, the concurrency and the cost ceiling. You have outsourced the machine, not the responsibility.
- *"Self-hosting is cheaper."* Only above a utilisation threshold, and only if you count the engineer who maintains it.
- *"Latency is a model property."* It is a path property: network hop, queue, prompt length, tokens generated.

## How a student should understand it

**Mental model:** the central kitchen versus your own wok. A central kitchen sells consistent, inspected portions and you cannot change the recipe. Your own wok gives you any dish and dies with the gas supply.

**Three things they can do after this bullet:**
1. Match a workload to one of the five approaches and defend it on cost, latency and compliance.
2. Say where the API key lives, and why it is not in the browser.
3. Name what to instrument before going live: latency, tokens, errors, cost.

**Misconceptions to kill:** cloud removes responsibility, self-hosting is cheaper, and latency is a model spec.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Central kitchen versus own wok.** Portions, consistency, inspection, no recipe control. Own wok means full control, own gas supply, own cook. Where it breaks: a central kitchen has one menu, while an endpoint is configured per request.

**Season parking versus the meter.** Reserved capacity is season parking: you pay whether or not the lot is used, and the lot is always there. Per-token billing is the meter: cheap when idle, painful on a full day. Most organisations discover which they are after the first invoice.

### Worked example with a real tool

Ask a model to write the client, then audit it for the deployment properties. In Claude:

```
Write a minimal Python function that calls a hosted LLM endpoint.
It must read the API key and base URL from environment variables,
set a 30 second timeout, retry twice on 429 and 5xx with backoff,
and return (text, usage_tokens) or raise a clear error.
```

What to point at afterwards: `os.environ` is secrets management; `base_url` is what makes the same code work against four providers and your own vLLM server; the timeout is the latency contract; the 429 retry is quota handling; `usage_tokens` is cost instrumentation. Four lines contain the whole deployment decision, and a learner who can point at them can hold a conversation with a platform engineer.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — one invoice line from a month-long pilot, and the question of which of the five approaches produced it.
2. **State the objective** — you will choose an approach for a workload and state its cost, latency and compliance consequences.
3. **Recall prior learning** — they know what an API call is (K1); now they decide where it lands.
4. **Present the content** — the five approaches and the four trade-off variables.
5. **Guide** — choose together for three scenarios: an internal prototype, a customer chatbot with PDPA obligations, a 50,000-document overnight job.
6. **Elicit performance** — each learner maps their own use case and writes one sentence per variable.
7. **Give feedback** — the recurring miss is ignoring region and residency until procurement asks.
8. **Transfer** — they add a deployment-choice section to their design template.

## What the framework doesn't mention but trainers need to know

- **Residency kills projects late.** Ask in week one. Moving a live system in-region after a compliance review is expensive and embarrassing.
- **Quota is a product decision.** If the provider allows 200 requests per minute and launch expects 2,000, the product is not ready regardless of code quality.
- **Cost per request is a design input.** Long system prompts and retrieval context are billed on every call, so a verbosity habit becomes a line item.

## Watch out

- **Do not turn this into a vendor comparison.** The five approaches are the lesson; the logo is a purchasing decision that changes quarterly.
- **Do not demo a local model as a deployment.** A model on a laptop proves nothing about concurrency, cold start or region.
- **Do not let "it's on the cloud, so it's secure" pass.** That sentence loses the audit.
- **The stale claim to retire:** "you need GPUs to build with generative AI." In November 2026 most teams never touch a GPU, and the ones that do want control, not capability.
