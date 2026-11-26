---
id: 06.01.B.K3
tsc: 6
level: Basic
code: K3
title: "How an AI application fails: the error messages and what sits behind them"
as_at: 2026-11-26
review_by: 2027-02-25
---

# How an AI application fails: the error messages and what sits behind them

> **TSC #6 Generative AI Application Development and Deployment · Basic · Knowledge K3**


> **Framework text (verbatim):** "Limitations of model capabilities and performance, including common error messages and issues in AI applications."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Knowledge · Bullet 3 of 11

**One-line version:** A model fails quietly and an application fails loudly — the job is to know which of the two just happened.

## What it is

Models have limits no prompting removes: a knowledge cutoff, a finite context window, non-deterministic output, latency and cost that grow with length. Applications built on them add mechanical failures — authentication, quotas, malformed requests, provider outages, guardrail refusals. This bullet is the catalogue, and the skill is telling the two apart.

## Deep expansion

### The concept

There are two failure surfaces and learners consistently conflate them. The **model** fails on quality: fluent, plausible, wrong. The **application** fails on mechanics: it does not answer at all, or the request never reached the model intact.

"The AI is broken" usually means a 429 because the key's quota ran out. "The AI is stupid" usually means retrieval returned nothing and the model filled the gap. Triage comes before fixing, because fixing a quota problem with prompt rewrites wastes an afternoon and teaches the wrong lesson.

### The sub-concepts

**The model's built-in limits.** Knowledge cutoff; context window (exceed it and the request is rejected or the oldest turns silently vanish); non-determinism (same prompt, different output); hallucination, worst where the model is least certain; latency and cost, which grow with tokens the user never sees; refusal and over-refusal, especially around medical, legal or security wording; prompt injection, where text inside a retrieved document hijacks your instruction.

**The status codes are a routing table.** `401` / `invalid_api_key` — key missing, wrong or revoked: yours. `403` — no permission for this model or region: yours, then the plan's. `404` / `model_not_found` — misspelled or retired model. `400` / `context_length_exceeded` — prompt too long or body malformed. `429` — rate limit or quota: pace yourself, or ask for a limit increase. `500` / `503` / `overloaded` — provider-side: wait and retry. Timeout — network, proxy or slow generation: measure first.

**Faults that are not model errors at all.** A missing environment variable, a package that will not import, a browser blocking a cross-origin request, a file the parser cannot read. These look like AI failures to a business user and are ordinary bugs to anyone who has built before.

**Silent failures.** Context overflow in a chat interface drops older turns without announcing it; guardrails refuse without explaining; retrieval returns a wrong passage and the answer is still fluent. The loud errors are easy. The quiet ones cost trust.

### How it connects to the rest of the framework

`TSC6-Basic-K5` is the procedure for working through these; `TSC6-Basic-A3` is how you hand one to someone else; `TSC6-Basic-A4` covers the subset about speed and cost. `TSC6-Basic-K1` explains the most common quality failure — no context supplied — and `TSC9` treats prompt injection and security as a discipline of its own.

### What is current as of November 2026

- **Reasoning modes changed the cost profile.** The current flagships — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — spend hidden tokens thinking before answering. Apps that were affordable on a chat model became slower and dearer after a switch, and the visible symptom is a timeout, not a bill.
- **Deprecation is now a routine failure.** Pinned model snapshots retire on a published schedule; an app that worked for a year returns `model_not_found` on a Tuesday with no code change. This is the most under-taught production failure at Basic level.
- **Guardrails fail in both directions, and region matters.** Content filters refuse benign inputs and miss hostile ones; model availability, latency and data-residency commitments differ by region, so a tutorial written for a US tenant may not reproduce in Singapore.

### Common misconceptions

- *"An error means the AI is broken."* Most errors are configuration, quota or request shape. The model never saw the request.
- *"It worked yesterday, so the model changed."* Check key, quota, pinned version, then prompt length — in that order.
- *"429 means I'm banned."* It means slow down or top up. It is the most recoverable error in the list.

## How a student should understand it

**Mental model:** the polyclinic triage counter. Before anyone sees a doctor, a nurse sorts the case: life-threatening, needs a doctor, or self-care. You cannot skip triage, and you cannot fix the wrong queue.

**Three things they can do after this bullet:**
1. Read an error and say whether it is a model limit, a configuration fault or a provider incident.
2. Name the four model limits most likely to affect a workplace app, with an example of each.
3. Predict the failure that appears when a document exceeds the context window, before it happens in front of a client.

**Misconceptions to kill:** that errors equal model failure, that a refusal equals danger, and that the same prompt gives the same answer twice.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food hygiene grade.** A stall with a B grade is not closed and not unsafe — it lost points on specific, listed items. An error message names the failed check; your job is to read the grade card, not to panic about the stall. Where it breaks: some errors genuinely are a closed stall, which is why triage precedes diagnosis.

**The MRT disruption announcement.** "Delay on the East–West line, westbound, track fault at Clementi." Someone who hears only "delay" cannot reroute. Someone who hears the station can. Read the whole message, including the part after the colon.

### Worked example with a real tool

Hand the room three real error strings, then type this into any assistant:

```
For each error: (a) is the cause my configuration, my request, or the provider?
(b) what do I check first? (c) give the exact phrase to search in the docs.
Do not suggest a fix before telling me the category.

1. openai.AuthenticationError: Error code: 401 - {'error': {'message':
   'Incorrect API key provided: sk-proj-...'}}
2. Error code: 429 - {'error': {'message': 'Rate limit reached on requests per min'}}
3. Error code: 400 - {'error': {'message': "maximum context length is 128000
   tokens. However, your messages resulted in 154210 tokens."}}
```

What to point at afterwards: the classifications are right, the fixes are plausible, and one of the three "exact search phrases" is invented. That is the lesson — the tool is excellent at triage and unreliable at detail. Verify the phrase in the documentation before it goes into a ticket.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — project a red stack trace and ask who would know what to do. Nobody does. Good.
2. **State the objective** — by the end you can triage an AI failure into model, configuration or provider, and name the next check.
3. **Recall prior learning** — knowledge cutoff and hallucination from TSC #1; the context window from the RAG bullet.
4. **Present the content** — two failure surfaces, the model limits that matter at work, the status-code routing table.
5. **Guide** — take one error, talk through the triage aloud, wrong turns included.
6. **Elicit performance** — pairs sort six error strings into three columns and write the first check for each.
7. **Give feedback** — compare columns. Most disagreement lands on 400 versus 429, which is the useful argument.
8. **Transfer** — each learner writes the three errors they have personally seen and what they now believe caused them.

## What the framework doesn't mention but trainers need to know

- **Context overflow is silent in many interfaces.** The model "getting dumber" after twenty messages is usually the instruction having scrolled out of the window.
- **Prompt injection deserves ten minutes even at Basic.** Uploaded documents can carry instructions. If the app has tools, injected text can trigger them. "Treat retrieved text as data, never as instructions" belongs on a slide.
- **Retry logic turns a small problem into a big one.** Aggressive retries on 429 deepen the rate limit and inflate the bill. Backoff, not persistence.

## Watch out

- **Do not teach the status codes as trivia.** They are a routing table; memorising 401 without learning "check the key file first" is useless.
- **Do not claim these errors are rare.** They are routine, and pretending otherwise makes the trainer look sheltered.
- **The stale claim to retire:** "AI errors are unpredictable." In production they are boringly predictable, and that predictability is what makes them teachable.
