---
id: 06.03.A.K4
tsc: 6
level: Advanced
code: K4
title: "Scripting and automation: making the machine do the first hour of debugging"
---

# Scripting and automation: making the machine do the first hour of debugging

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Knowledge K4**


> **Framework text (verbatim):** "Scripting and automation for troubleshooting."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Knowledge · Bullet 4 of 12

**One-line version:** Generative systems fail non-deterministically, so the only debugging that scales is the debugging you wrote down as code — capture, probe, reproduce, alert.

## What it is

Scripting and automation for troubleshooting means turning diagnosis into something a machine runs: structured logging, scheduled probes, reproduction harnesses, regression checks and alerts that fire before a user complains. The Advanced content is knowing which parts of debugging can be automated and which cannot — and building the boundary deliberately, with scripts that are safe to run unattended.

## Deep expansion

### The concept

Debugging a conventional application has a reliable starting point: the same input produces the same failure. Generative systems break that. The same prompt gives a different answer at temperature 0.7; a model update changes behaviour overnight with no code change; a retrieval index drifts as documents are edited. Hand-debugging therefore fails not because engineers are careless but because the evidence has already evaporated by the time someone looks.

Automation restores the evidence. Three loops need it:

- **Detect** — something is wrong, ideally before a user reports it.
- **Isolate** — which hop failed: input handling, retrieval, model, guardrail, post-processing?
- **Reproduce** — turn the failure into a fixed case that can be re-run on demand.

Each loop has a different tool. Detection needs probes and thresholds. Isolation needs per-hop traces. Reproduction needs pinned versions and captured inputs. The professional habit is that every incident ends with a new automated check, so the same failure cannot recur silently.

### The sub-concepts

**Capture before analysing.** Structured logs with a request ID, the rendered prompt, retrieved document IDs, model name and version, token counts, latency per hop, guardrail decisions and the final output. Without these, debugging is anecdote. With them, most incidents are answered in a query.

**Synthetic probes.** A handful of canary questions with known correct answers, run every few minutes against production. This is the only reliable way to catch silent degradation — a model provider changing behaviour, an index losing documents, a reranker timing out and being skipped.

**Reproduction.** Pin temperature, seed where supported, prompt version, model version and retrieval snapshot. A failing case becomes a fixture: a folder with input, expected behaviour and a note on why it matters.

**Regression gating.** A small evaluation suite in the deployment pipeline — twenty to fifty cases, cheap, run on every prompt or model change. It will not prove quality; it will catch the change that broke the thing you fixed last month.

**Thresholds that mean something.** Error rate, ninety-fifth-percentile latency, cost per conversation, refusal rate, empty-retrieval rate, guardrail block rate. Alert on the second derivative as well as the absolute: a refusal rate that doubled is a signal even at 4%.

**Runbooks as code.** The third time you perform a manual sequence, script it: idempotent, read-only by default, logged, safe to re-run. Then the runbook and the tool are one artefact, and it cannot go stale in someone's memory.

### How it connects to the rest of the framework

`TSC6-Advanced-A6` is the ability this knowledge serves — automating troubleshooting by building custom scripts and tools. `TSC6-Advanced-A2` supplies the metrics that serving infrastructure exposes; those numbers are the raw material for every alert. `TSC6-Advanced-K1` explains why cost per conversation is a first-class symptom, not an accounting detail. `TSC6-Basic-K5` and `TSC6-Basic-A4` are the manual versions: read the docs, follow the standard procedure. This bullet is what happens when the manual procedure is run ten thousand times.

### What is current as of November 2026

- **LLM tracing is now a product category.** Managed observability tools record prompts, retrievals, tool calls and token costs per span, which means building your own tracer is rarely justified — building your own *thresholds* still is.
- **Agent runs need span-level traces.** A single conversation may contain twelve model calls and four tool calls; a flat log is unreadable and useless for isolation.
- **Evaluation in CI has become normal practice** for teams shipping AI features weekly, typically a small suite rather than a large benchmark.
- **Cost anomaly alerts are as common as latency alerts**, because token spend is now a variable cost that can multiply within an hour.
- **Prompt and model versioning are prerequisites**, not nice-to-haves: without a version identifier in the log, no trace can be reproduced.

### Common misconceptions

- *"If it works in the playground, it works in production."* Playground traffic is one user, one phrasing, no concurrency. Production is a distribution.
- *"I can debug by reading the prompt."* You can form a hypothesis; only the trace can confirm it.
- *"More logging is always better."* Logging prompts means logging personal data. Retention, redaction and access control are part of the design.
- *"Automation replaces judgement."* It replaces the gathering. The interpretation — is this a real regression or a bad canary — remains human.

## How a student should understand it

**Mental model:** the polyclinic triage nurse. She does not diagnose; she takes temperature, blood pressure and history in a fixed order, so the doctor starts with evidence instead of a queue.

**Three things they can do after this bullet:**
1. Name the six fields every LLM request log must carry to be debuggable.
2. Write a canary probe and set a threshold that would have caught a stated past failure.
3. Decide which parts of a manual troubleshooting runbook should become a script, and which must stay human.

**Misconceptions to kill:** that playground success predicts production, that prompt-reading is debugging, and that logging more is free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT fault crew.** They do not fix a train by staring at it. There is a diagnostic panel, a fault code, a checklist and a depot. The panel does not understand the train; it narrows the search. Scripts are the panel, and the engineer still decides.

**The insurance claims file.** A claim with photographs, receipts and a timeline is settled; a claim with a story takes weeks. Structured capture is what makes the difference, and it is written before the incident, not after. Where it breaks: claims are rare and high-value, while LLM requests are numerous and cheap — so the capture must be automatic and sampled, not hand-assembled.

### Worked example with a real tool

Ask an assistant to write the diagnostic script, then audit it:

```
Write a Python script that reads my app's logs, one JSON object per line,
with these fields: timestamp, request_id, latency_ms, status,
prompt_tokens, completion_tokens, error, model_version.

It should print:
1. p50 and p95 latency,
2. error rate by status code,
3. the ten slowest requests with their token counts,
4. the same three numbers for the previous day, so I can see the delta.

Use only the Python standard library. No pandas.
```

What to point at afterwards: the script will usually run, and the percentile code is often subtly wrong — check the index arithmetic by hand with a list of ten numbers. Then point at the bigger lesson: the script is the artefact, but the *reading* is the skill. A p95 that moved from 2.1 s to 2.4 s while p50 stayed flat means queueing, not a slower model, and no script says that for you.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — replay a support call: "it gave a wrong answer yesterday, can you check?" Show that nothing was recorded.
2. **State the objective** — you will specify the capture, probe and regression check for your own application.
3. **Recall prior learning** — they know the standard troubleshooting steps; now they automate the repeatable ones.
4. **Present the content** — the three loops and the tool for each.
5. **Guide** — write one canary question and its pass condition together.
6. **Elicit performance** — pairs build a three-line probe plan and one log-schema change.
7. **Give feedback** — correct any plan that logs full prompts without redaction, and any alert with no threshold.
8. **Transfer** — they add one automated check to their next release and one new case after each incident.

## What the framework doesn't mention but trainers need to know

- **Non-determinism has to be bounded, not eliminated.** Pin what you can (version, temperature, seed), record what you cannot, and compare distributions rather than single runs.
- **Sampling is a design choice.** Log every failure and 5% of successes; full capture is often unaffordable and a privacy liability.
- **Canaries rot.** A canary whose expected answer is no longer correct produces false alarms and then gets muted — the worst outcome. Review them quarterly.
- **Alert fatigue is the real failure mode.** Three alerts nobody acts on train the team to ignore the fourth.
- **The incident review is the product.** If a postmortem does not produce a new automated check, it produced a document.

## Watch out

- **Do not let anyone script against production with write credentials.** Read-only by default, and say so before the exercise, not after.
- **Do not log raw prompts containing personal data** in a demo — the class will copy the pattern into a real system.
- **Do not trust auto-generated statistics code.** Percentiles, medians and timezone handling are where assistants are confidently wrong.
- **The stale claim to retire:** "AI applications cannot really be monitored." In November 2026 the tracing is standard; what is missing is usually the team's thresholds and ownership.
