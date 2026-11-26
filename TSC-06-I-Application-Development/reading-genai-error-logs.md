---
id: 06.02.I.A1
tsc: 6
level: Intermediate
code: A1
title: Reading a GenAI error log: the four families of failure
as_at: 2026-11-26
review_by: 2027-02-25
---

# Reading a GenAI error log: the four families of failure

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Ability A1**


> **Framework text (verbatim):** "Identify issues in generative AI models by analysing and interpreting error logs."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Ability · Bullet 8 of 12

**One-line version:** Almost every GenAI failure announces itself in one field — the status code, the `finish_reason` or the token count — and the skill is reading that field before touching anything else.

## What it is

This is the ability to take a log line or error object from a generative AI system and name the actual fault: authentication, request shape, transport, or content. It is diagnostic, not speculative — the output is a sentence like "the request exceeded the context window by 3,842 tokens, so the retrieval stage is returning too many chunks", not "the model seems flaky".

## Deep expansion

### The concept

An error log is a compressed account of what the system believed when it failed. Most people read the message field, which is written for humans and often vague, and skip the structured fields, which are precise. Read in a fixed order: the status code (which layer failed), `finish_reason` (how generation ended — `stop`, `length`, `content_filter`, `tool_calls`), the token counts, the timing, and the correlation ID.

Four families cover nearly everything:

**Authentication and authorisation.** 401, 403, an expired key, the wrong project, a key scoped to a model you are not calling, a key present locally but absent from the deployment's secret store.

**Request shape.** 400s: context length exceeded, a malformed message array, a parameter the model does not support, invalid JSON schema, an image too large.

**Transport and capacity.** Timeouts, connection resets, 429 rate limits, 500/503 from the provider, a regional outage, proxy or TLS interception on a corporate network.

**Content.** The request succeeded and the answer is wrong — empty completion, truncated at `max_tokens`, a refusal, JSON that fails to parse, a hallucinated citation.

### The sub-concepts

**`finish_reason` is the most under-read field in the stack.** A truncated answer is not a quality problem; it is a `max_tokens` setting. A filtered answer is not a refusal; it is a guardrail. Telling these apart changes the fix entirely.

**The context window is a budget, not a limit you discover.** Prompt tokens plus reserved completion tokens must fit. Applications that build prompts by concatenation fail at exactly the document that pushes it over — usually the biggest and most important one.

**Truncation is silent by default.** Many APIs return HTTP 200 with a cut-off answer. If you are not reading `finish_reason`, you will ship half-sentences.

**Reproduce with the smallest request.** Strip the conversation to the failing turn, remove the retrieval context, drop one message at a time. The moment it succeeds, you have found the contributor.

**Distinguish the three owners.** Model issue (provider), integration issue (your code), input issue (the user's document). The log tells you which, and the ticket goes to the right place — the difference between escalating usefully and escalating noisily.

**Redaction while logging.** Logs must carry enough to debug and not enough to breach PDPA. Hash identifiers, redact content, keep structure.

### How it connects to the rest of the framework

`TSC6-Basic-K5` is basic troubleshooting and `TSC6-Basic-A3` is escalation; this is the intermediate step where "it doesn't work" becomes a diagnosis. `TSC6-Intermediate-K5` determines where in the chain the log sits, and `TSC6-Intermediate-A5` is the neighbouring ability for environment-level failures. At Advanced level, `TSC6-Advanced-K4` and `A6` automate this reading with scripts.

### What is current as of November 2026

Log reading is easier and more necessary at once. Structured errors are standard — nearly every provider returns a typed error object with a machine-readable code, and OpenAI-compatible endpoints made the shapes similar enough for one handler to cover several vendors. Tracing tools now show the whole chain: each stage, its input, its tokens and its latency, so the skill has shifted from parsing text to reading a waterfall. And context windows grew, which removed some 400s and replaced them with a quality failure — attention diluted across 200,000 tokens of retrieved text — that carries no error code at all.

### Common misconceptions

- *"The error message tells you what's wrong."* It tells you the layer. The structured fields tell you the cause.
- *"A 200 response means success."* Truncation, refusal and empty completion all return 200.
- *"429 means we're being attacked."* It usually means your own retry loop, or a batch job sharing the key with production.

## How a student should understand it

**Mental model:** the mechanic with the fault-code reader. He does not listen to the engine and guess; he reads the code and knows which subsystem to open.

**Three things they can do after this bullet:**
1. Take an error object and classify it into one of four families, naming the field that decided it.
2. Read `finish_reason` and say whether the output was truncated, filtered or refused — and what to change.
3. Produce a minimal reproduction by stripping a failing request down.

**Misconceptions to kill:** the message field is the answer, HTTP 200 means success, and flakiness is an explanation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic's lab report.** You do not re-run the test to understand it; you read the flags — which value is out of range, and what that implicates. The log is the lab report, and the conclusion is in the flags, not the paragraph. Where it breaks: lab ranges are standardised across labs, while log field names still vary between providers.

**The order chit that never reached the kitchen.** When a dish does not arrive, the floor manager does not blame the chef. She checks whether the chit was written, whether it reached the pass, and whether the kitchen read it. Input, transport, processing — three places a request can die, and the log records which.

### Worked example with a real tool

Paste a real error into a model and make it read the fields, not the prose. In Claude:

```
I got this from my app. Tell me which layer failed, what specifically
caused it, and the smallest change that fixes it.

{"error": {"message": "This model's maximum context length is 128000
tokens. However, your messages resulted in 131842 tokens.",
"type": "invalid_request_error", "code": "context_length_exceeded",
"param": "messages"}}
```

Then the harder one — no error at all:

```
finish_reason: "length", completion_tokens: 512, max_tokens: 512,
output: "Based on the three quotations provided, the recommended
supplier is Sin Heng because their lead time is shortest and"
```

What to point at afterwards: the first is a request-shape failure with the exact overage (3,842 tokens) and a named parameter; the fix is the retrieval budget, not a new model. The second returned HTTP 200 and looks like a normal answer — the only evidence is `finish_reason: length` against `max_tokens: 512`. Learners who read those two in under a minute have the skill.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a support ticket saying "the AI is giving short answers", and the log that answers it in one field.
2. **State the objective** — you will classify any GenAI error into one of four families and name the fix.
3. **Recall prior learning** — they know the pipeline stages (K5) and the API contract (K1); the log is the contract failing.
4. **Present the content** — the five-field reading order and the four families.
5. **Guide** — read three real error objects together, one from each family.
6. **Elicit performance** — each learner diagnoses one error from their own logs (or the supplied set) in a single sentence.
7. **Give feedback** — the recurring error is jumping to the model; correct them back to the field.
8. **Transfer** — they add `finish_reason` and token counts to their logging config this week.

## What the framework doesn't mention but trainers need to know

- **Most "model problems" are prompt-budget problems.** In a room of twenty, expect fifteen of the failures to be context length, truncation or a malformed message array. Say so; it recalibrates expectations fast.
- **Silent truncation is a production hazard.** A summary that stops mid-sentence damages trust more than an error page would. Assert on `finish_reason` in code.
- **Rate limits are shared.** One key across dev, staging and a nightly batch is the most common cause of a 429 in production, and separate keys per environment is a five-minute fix nobody does until it bites.
- **The log is also the evaluation input.** Every real failure should become an eval case (K6).

## Watch out

- **Do not teach log reading as reading stack traces.** The GenAI-specific skill is the semantic fields; a generic traceback workshop misses it.
- **Do not accept "it's intermittent" as a diagnosis.** Intermittent usually means a retry succeeding, a quota boundary, or one specific input — all findable.
- **Do not demo with fabricated errors.** Use a real error object from a real provider; learners check.
- **The stale claim to retire:** "check the error message." In November 2026 the message is the least informative field in the object.
