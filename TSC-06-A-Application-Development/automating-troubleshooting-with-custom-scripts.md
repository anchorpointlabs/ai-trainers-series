---
id: 06.03.A.A6
tsc: 6
level: Advanced
code: A6
title: "Automating troubleshooting with your own scripts and tools"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Automating troubleshooting with your own scripts and tools

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A6**


> **Framework text (verbatim):** "Automate troubleshooting tasks by creating custom scripts or tools."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 11 of 12

**One-line version:** Build the tool that answers "is it broken, where, and since when" in one command — and make it safe enough to run unattended at 3am.

## What it is

This is the ability to build a small, durable piece of tooling that does the diagnosis for you: a health-check CLI, a canary runner, a log aggregator that summarises the last hour, a cost-anomaly detector, an incident-timeline generator. It goes beyond writing an ad-hoc script — the tool has an interface, a failure mode, an owner and a place in the on-call routine.

## Deep expansion

### The concept

Every team has a set of diagnostic moves performed by hand: check the endpoint, run three sample questions, look at the error rate, compare with yesterday, check whether the index was rebuilt, ask whether the model version changed. Done by hand, these take twenty minutes and depend on who is on call. Built as a tool, they take twenty seconds and produce the same evidence regardless of experience.

The design principle is that **automation should own detection and evidence, and humans should own judgement.** A tool that says "retrieval returned zero documents for 14% of requests in the last hour, starting 09:40" has done its job. A tool that decides to roll back the model on its own has taken a judgement it is not equipped to make.

That gives a three-part shape to any troubleshooting tool:

- **Probe** — synthetic requests with known correct answers, run on a schedule.
- **Collect** — pull the metrics and logs that would be needed if this were an incident, so they exist before anyone asks.
- **Summarise** — one line a tired person can read at 3am, and a detailed view for the morning.

### The sub-concepts

**Canaries with known answers.** Not "does the API return 200" but "does the answer to this question contain the correct clause ID". Liveness checks pass while the product is broken; canaries catch semantic failure.

**Hop-level timing.** Measure transcription, retrieval, generation, guardrails and post-processing separately. End-to-end latency tells you it is slow; hop timing tells you where.

**Exit codes and machine-readable output.** A tool that prints prose is for humans only. A tool that exits non-zero and emits JSON can gate a deployment, page an on-call engineer, or feed a dashboard.

**Bounded self-healing.** Restart a wedged process, fail over to a secondary model, open a circuit breaker. Each action needs a limit (once per ten minutes), a log, and a human notification. Unbounded self-healing produces outages that look like stability.

**Monitoring the monitor.** A canary that silently stops running is worse than no canary, because it manufactures confidence. Heartbeat the checker; alert on absence of data, not just on bad data.

**Rate limits and safety rails.** Read-only credentials by default, request caps, a dry-run mode, and no destructive action without an explicit flag. The tool will eventually be run by someone in a hurry.

**An owner and a review date.** Tools rot: endpoints move, expected answers go stale, thresholds drift. A tool with no owner becomes a false-alarm generator, then gets muted, then gets deleted.

### How it connects to the rest of the framework

`TSC6-Advanced-K4` is the scripting knowledge this ability turns into a product — K4 teaches what to automate, A6 teaches how to build it durably. `TSC6-Advanced-A2` is the serving layer whose metrics the tool reads. `TSC6-Advanced-A3` produces the guardrail decisions the tool should be watching. `TSC6-Intermediate-A1` is reading error logs by hand; this bullet is the same skill compiled. `TSC6-Advanced-A7` is where the tool's behaviour gets written down.

### What is current as of November 2026

- **Tracing SDKs made the collection layer cheap.** Prompt-level traces with per-span timing are widely available, so custom tooling now concentrates on *checks and summaries* rather than plumbing.
- **Synthetic monitoring is a commodity service**, which means the differentiator is the design of the canary questions, not the scheduler.
- **Agentic on-call assistants exist and are used with supervision.** They read dashboards, summarise an incident and propose a runbook step; they do not hold the pager alone.
- **Cost anomaly detection became standard**, because a looping agent can multiply spend within an hour.
- **Self-healing is bounded by policy**, typically restart, fail over and shed load — actions with reversible effects.

### Common misconceptions

- *"A dashboard is automation."* A dashboard requires someone to look at it at the right moment. Automation decides when to look.
- *"Self-healing means no on-call."* It means fewer trivial pages, and more subtle ones.
- *"Write it once and forget it."* Tools decay with every endpoint, model and schema change; ownership is part of the build.
- *"If the check passes, the system is healthy."* The check passes for the questions you thought of; that is why canary design is the hard part.

## How a student should understand it

**Mental model:** the HDB lift that phones the contractor before a resident complains. Sensors, a threshold, a call, a log. Nobody expects the lift to repair itself — they expect it to notice, report and stop safely.

**Three things they can do after this bullet:**
1. Write a canary with a semantic pass condition, not an HTTP 200.
2. Build a one-command diagnostic that exits non-zero and prints a one-line cause.
3. List the three false alarms their tool will produce and how to damp them.

**Misconceptions to kill:** that monitoring equals a dashboard, that self-healing removes the human, and that a tool needs no owner.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Lift condition monitoring.** The lift reports a door-cycle anomaly, the contractor is dispatched, and the resident never knows. The value is the early, boring report — not a dramatic rescue.

**The MRT depot's diagnostic panel.** The technician does not guess; the panel names the subsystem. But the panel is not the engineer: it narrows the search to the door controller, and the decision to take the train out of service is made by a person with a rulebook. Tools narrow; people decide. Where it breaks: train faults have known signatures after decades, while generative failures are new — so your panel needs to be extensible, and its summaries must admit uncertainty.

### Worked example with a real tool

Build a "doctor" for a RAG application:

```
Write a Python "doctor" script for my RAG app. It should:

1. Send five canary questions whose correct answers I know, each with an
   expected clause ID, and check the answer contains it.
2. Time each hop: retrieval, generation, post-processing.
3. Exit non-zero and print ONE line naming the failed hop if any check fails.
4. Emit JSON to a file for the dashboard.
5. Be safe to run every five minutes from cron: read-only, no retries that
   could amplify load, hard timeout of 30 seconds.

Then list the three false alarms it will produce in the first month and how
to damp each one.
```

What to point at afterwards: the script is straightforward; the last instruction is the ability. Typical false alarms — a canary whose expected answer is now outdated, a cold-start timeout after a redeploy, and a legitimate model rephrasing that omits the clause ID while remaining correct. Each has a different fix: review the expected answer quarterly, add a warm-up grace period, and check for the clause *reference* rather than the exact string.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — an outage discovered by a customer email, two hours after a canary would have caught it.
2. **State the objective** — you will ship one diagnostic tool with a pass condition and an owner.
3. **Recall prior learning** — they have written ad-hoc log scripts; now the script becomes a tool.
4. **Present the content** — probe, collect, summarise; bounded healing; monitor the monitor.
5. **Guide** — design one canary together and argue about what "correct" means.
6. **Elicit performance** — teams build the doctor for their own application, with three false alarms named.
7. **Give feedback** — reject any tool that prints prose only, and any self-heal without a rate limit.
8. **Transfer** — the tool goes into the deployment pipeline and the on-call runbook that week.

## What the framework doesn't mention but trainers need to know

- **The tool must survive the person who wrote it leaving.** README, owner, review date, and a test that proves it still works.
- **Run it against staging before production**, and make the production mode read-only by default.
- **Absence of data is a signal.** Alert on "no canary results in 15 minutes", or a broken scheduler looks like calm.
- **Keep a human-readable incident timeline.** It is the artefact postmortems are written from, and it is cheap to generate.
- **Measure the tool's own cost.** A canary every five minutes against five questions is trivial; a hundred questions every minute is a line item.

## Watch out

- **Do not demo unbounded self-healing.** It looks impressive and it produces flapping systems; show the limit and the notification instead.
- **Do not let learners point tools at production with write credentials.** Say it before the exercise, not after.
- **Do not let a tool's summary become the truth.** State confidence, show the underlying numbers, and keep the detail view one flag away.
- **The stale claim to retire:** "AI applications are too non-deterministic to monitor." In November 2026 semantic canaries are ordinary practice; what is missing is usually ownership.
