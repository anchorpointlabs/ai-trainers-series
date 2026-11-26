---
id: 09.02.I.A6
tsc: 9
level: Intermediate
code: A6
title: Monitor AI systems through the lifecycle
---

# Monitor AI systems through the lifecycle

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A6**

> **Framework text (verbatim):** "Monitor AI systems for trust and safety throughout project life cycle."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Ability · Bullet 10 of 10

**One-line version:** Monitoring is a standing capability with thresholds, owners and a kill switch — otherwise it is a dashboard nobody opens until the incident review.

## What it is

Lifecycle monitoring means watching a live AI system for the signals that something has changed — new abuse, degraded accuracy, unexpected actions, cost spikes, policy drift — and having a pre-agreed response for each. It runs from launch to retirement, covers every version change, and produces records that let an organisation answer questions months later.

## Deep expansion

### The concept

An AI system does not fail like a server. It keeps returning 200 OK while giving worse answers, following instructions it should ignore, or acting on data it should not have seen. Availability monitoring will never see this. What catches it is watching three things the traditional stack ignores: **the context** (what the model was given), **the decision** (what it proposed), and **the effect** (what the tool did).

That gives the minimum telemetry set:

1. **Context assembly** — system prompt version, user input, which chunks were retrieved (ids and hashes), and any tool outputs fed back in.
2. **Tool audit** — every proposed call, its arguments, whether it was blocked, by which rule, and under whose session.
3. **Guardrail telemetry** — classifier scores, refusals, redactions, escalations, and block rates per rule.
4. **Cost and volume** — tokens and spend per user and per hour, request volume, agent loop counts.
5. **Outcomes** — complaints, corrections, thumbs-down, abandoned conversations, and any human override of an approval.

With those, most questions become answerable: was it abused, did the guardrail over-block, did the model version change behaviour, is someone probing.

### The sub-concepts

**Thresholds decided in advance.** "Refusal rate up threefold" only triggers action if someone agreed it would. Write the threshold, the owner and the first check into an on-call note.

**Drift with three causes.** Model version change, corpus change, prompt change. Each has its own detection: version pins and replay, index diffs and answer sampling, and a change log with a regression run.

**New abuse.** Public jailbreaks and injection prompts follow every release. Keep a watch source and replay new attacks against the system; a working attack on someone else's bot is a test case for yours.

**The abuse signal is behavioural.** Repeated rephrasings of the same request, sudden language switches, long conversations with no task, attempts to extract a prompt, spikes from one account. Rate limits and iteration caps are monitoring instruments, not just cost controls.

**Incident response with a kill switch.** Contain first: disable the specific tool or endpoint, not the whole product. Then assess exposure, fix, and communicate. Decide the switch exists before you need it, and test that it works.

**Retention and privacy in the logs.** Logs contain personal data. Set retention, restrict access, and treat the log store as in scope for PDPA obligations.

**Lifecycle, not launch.** Include the change events: new model version, new tool, new corpus, new market, new user population. Each is a reason to replay the test set and re-read the register.

**Retirement.** When the system is switched off: revoke credentials, delete corpora, retain the records you must keep, and archive the test set and register for the successor.

### How it connects to the rest of the framework

`TSC9-Basic-K4` is the post-launch loop at Basic level. `TSC9-Intermediate-A5` produces the test set that monitoring replays; `TSC9-Intermediate-K1` names the controls whose health is being watched; `TSC9-Intermediate-A3` supplies the block-rate numbers; `TSC9-Intermediate-A4` supplies the surfaces and the register. `TSC9-Intermediate-K4` sets the cadence. At Advanced, `TSC9-Advanced-A6` embeds this into organisational governance.

### What is current as of November 2026

Continuous model updates have made monitoring a version-management problem as much as a security one. The late-2026 frontier — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — is delivered as a service that changes under you, and agentic deployments mean the audit trail has to cover actions.

- **Pin and replay.** Where the vendor allows a pinned version, pin it, and replay the test set before moving.
- **Watch actions, not just answers.** The costliest post-launch failure in an agent is an authorisation, not a paragraph.

### Common misconceptions

- *"Uptime monitoring is monitoring."* A system can be 100% available and 100% wrong.
- *"No complaints means no problems."* Users abandon quietly; the failure shows in outcomes, not in tickets.
- *"We will read the logs if something happens."* That is forensics. Monitoring means someone looks on a schedule, against a threshold.
- *"Model updates are the vendor's responsibility."* The vendor ships a version; you ship the behaviour change to your customers.

## How a student should understand it

**Mental model:** a building's fire panel — sensors, a named responder, a drill, and a switch that shuts the plant room down.

**Things they can do after this bullet:**
1. List the five telemetry categories and what each detects.
2. Set a threshold with an owner and a first response.
3. Describe the kill switch and what it disables.

**Misconceptions to kill:** that uptime is health; that silence is safety; that logs are for blame rather than for decisions.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic's waiting-room triage.** Patients are not monitored by a camera; they are monitored by a nurse who looks, measures and escalates. The measurement is scheduled; the escalation is scripted.

**The factory's quality sampling.** A production line can run at full speed and produce defects. Sampling catches the drift before the shipment does.

### Worked example with a real tool

Set up the review with a realistic week of signals and force a decision:

```
Our finance agent went live a month ago. This week: tool calls up 4x,
150 of them blocked by policy, API spend tripled, and two users asked
why an order was raised twice.

Give me: the three most likely explanations, the three log queries
that would distinguish them, the threshold that should have paged
someone, and what to switch off while we investigate.
```

What to point at afterwards: the model will offer "attack" and "bug" as explanations. The distinguishing evidence is the audit trail — same account or many, same arguments or varied, blocked by which rule. And the answer to "what to switch off" should be the purchase-order tool, not the whole system.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a healthy uptime graph next to a complaint log; ask which one the customer experienced.
2. **State the objective** — by the end, they can name the five telemetry categories and set a threshold with an owner.
3. **Recall prior learning** — any on-call or operations duty they have held.
4. **Present the content** — context/decision/effect; thresholds; drift; abuse signals; incident response; retention; retirement.
5. **Guide** — work the finance-agent signals together.
6. **Elicit performance** — pairs define the alert set for one system.
7. **Give feedback** — debrief: which alerts had no owner and no action.
8. **Transfer** — each learner writes one alert and one kill-switch decision for their own system.

## What the framework doesn't mention but trainers need to know

- **Alert fatigue kills monitoring.** Three or four alerts that page a person beat thirty that appear on a dashboard.
- **Log the prompt version, always.** Otherwise a behaviour change is unattributable.
- **Audit the approvals.** The most dangerous signal is a person approving actions without reading them; measure approval latency.
- **Retirement is a security event.** Credentials and corpora left behind are the next breach.

## Watch out

- **Do not present monitoring as surveillance of staff.** Scope it to system behaviour and data handling.
- **Do not collect everything.** Logs with full prompts and personal data are a liability unless retention and access are set.
- **Do not rely on one signal.** Refusal rate alone cannot distinguish an attack from an over-tight rule.
- **Retire the stale claim:** "monitoring is a launch-week task." In November 2026 the model, the corpus and the attackers all move during the year.
