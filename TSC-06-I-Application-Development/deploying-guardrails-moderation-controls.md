---
id: 06.02.I.A4
tsc: 6
level: Intermediate
code: A4
title: Deploying guardrails and moderation on the way in and the way out
as_at: 2026-11-26
review_by: 2027-02-25
---

# Deploying guardrails and moderation on the way in and the way out

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Ability A4**


> **Framework text (verbatim):** "Deploy existing guardrails and moderation controls to control inputs and outputs to prevent undesirable model behaviours."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Ability · Bullet 11 of 12

**One-line version:** You are not inventing the control — you are installing one that already exists, at the right point in the request path, with a threshold you can defend and a log you can read.

## What it is

This is the applied ability to take an off-the-shelf moderation control — a provider's moderation endpoint, a cloud content-safety service, a guardrail framework, a PII redactor, a schema validator — and put it in front of or behind a model so undesirable inputs and outputs are stopped, logged and handled. The deliverable is a request path with visible checkpoints, and measured evidence of what they catch and what they cost.

## Deep expansion

### The concept

The word "existing" is doing the work in this bullet. The frameworks, classifiers and moderation services already exist and are cheap; what is hard, and what learners get wrong, is **placement and posture**.

**Placement** — before the model, after the model, or both. Input checks stop the request reaching the model at all (cheaper, and it keeps bad content out of your logs and context). Output checks catch what the model produced anyway. Both is the default for anything customer-facing.

**Posture** — block, redact, rewrite, or flag-and-allow. Not every finding should stop the interaction. A phone number in a prompt should be redacted and passed; a request for another student's records should be blocked; a mildly rude sentence might be flagged and logged.

A guardrail that only blocks will over-block, and an over-blocking guardrail gets switched off by the business within a quarter. The posture decision is what keeps it alive.

### The sub-concepts

**Threshold tuning.** Every classifier returns a score. The threshold decides the trade between false positives (annoying, drives users away) and false negatives (harmful content passes). Tune against a fixed test set, not intuition, and revisit when the vendor updates.

**Deterministic pre-checks first.** Size limits, file-type allowlists, schema validation, blocked-string lists for account numbers and NRICs. Free, instant, explainable and exact — run them before the expensive classifiers.

**PII detection and redaction.** Detect before the prompt leaves your boundary, and again on the way out, because models reproduce and invent identifiers. Redaction (replacing with a token) is usually better than rejection, since the task often does not need the real value.

**Schema-constrained output.** The most reliable output guardrail is a validator: if the response must match a schema, malformed output fails loudly instead of leaking into the next stage.

**Groundedness check.** For retrieval answers, verify claims against the retrieved context, or require citations and validate that the cited passage exists and supports the sentence.

**Block-and-continue UX.** The user sees a reason, an alternative, and a route to a human. "Request rejected" is a bug report in waiting.

**Audit logging with reason codes.** Every trigger records which control fired, what score, which policy version. Without reason codes you cannot tune, and you cannot answer "how many legitimate customers did we block last week".

### How it connects to the rest of the framework

`TSC6-Intermediate-K7` is the conceptual layer model; this ability installs it. `TSC6-Intermediate-K6` is the governance and testing that produces the evidence, and `TSC6-Intermediate-K2` and `K5` determine where the checkpoints sit. At Advanced level, `TSC6-Advanced-K2` and `A3` cover effectiveness measurement and building new controls. `TSC3-Basic-K7` is prompt-level guarding, which this supersedes.

### What is current as of November 2026

Deploying a guardrail is now an integration task rather than a research task. Moderation is a service call: provider endpoints and cloud content-safety APIs cover hate, harassment, self-harm, sexual content and violence out of the box, with per-category scores, cheap enough to run on every request. Guardrail frameworks are standard middleware — declarative policy in front of the model call, handling input rails, output rails and tool-call rails. And prompt-injection detection is treated as necessary and insufficient: classifiers catch the crude attempts, while least privilege and human confirmation catch the rest.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"One moderation endpoint covers everything."* Generic categories miss domain rules: your refund policy, your competitors, your unreleased product names, your PDPA obligations.
- *"Blocking is the safe default."* Over-blocking is a measurable business cost, and the users you block are usually the ones with legitimate edge cases.
- *"If it's on, it's working."* Without a bypass test you do not know the rate.

## How a student should understand it

**Mental model:** the overload sensor in an HDB lift. A fixed rule, cheap and deterministic, that does not care why you are over the limit — it simply refuses to close.

**Three things they can do after this bullet:**
1. Place an input and an output check in an existing request path, with a stated posture for each.
2. Write the user-facing message and the reason code for each control.
3. Run five known attacks against the deployed path and report the block rate.

**Misconceptions to kill:** one endpoint covers everything, blocking is the safe default, and "it's on" means "it works".

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The lift overload sensor.** Deterministic, cheap, unarguable. It does not judge intent, and that is its strength — it never gets tired and never negotiates. Where it breaks: overload is a measurable physical fact, while "is this prompt harmful" is a judgement with a grey zone two-thirds of the way across.

**Raw and cooked chopping boards.** Two boards, two colours, never crossed. Cheap, dumb, effective, and it prevents a category of contamination that careful cooking cannot fix. Where it breaks: contamination shows on a swab, whereas a prompt injection looks like ordinary text until you read the meaning.

### Worked example with a real tool

Deploy a moderation wrapper and test it at the boundary. In Claude:

```
Write a Python wrapper around an OpenAI-compatible chat call with two
guardrails:

1. INPUT: call the moderation endpoint on the user message first.
   If flagged above threshold, return a polite refusal naming the
   category and offer a human handoff. Otherwise redact anything that
   looks like an NRIC or phone number before sending.
2. OUTPUT: run the same moderation check on the reply, plus a check
   that it contains no more than 3 URLs. If either fails, return a
   fixed safe fallback message.

Log every trigger as JSON: timestamp, stage, control, score, reason.
Use thresholds from config, not hard-coded.
```

What to point at afterwards: the two stages, the thresholds in config so tuning is not a deploy, and the JSON log with reason codes so blocks can be counted by cause. Then run a borderline input through — something rude but not abusive — and watch the room argue about the threshold. That argument is the lesson: the threshold is a policy decision, and it belongs in a config file with a named owner.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a support transcript where a guardrail blocked a legitimate question about a refund policy, and the customer left.
2. **State the objective** — you will deploy an input and an output control with a stated posture, a threshold and a log.
3. **Recall prior learning** — they know the three layers (K7) and the governance tests (K6); now they install it.
4. **Present the content** — placement, posture, thresholds, deterministic-first, UX, logging.
5. **Guide** — write the wrapper together and wire it into the FAQ app from A3.
6. **Elicit performance** — teams add two controls to their own application and pick a threshold with a justification.
7. **Give feedback** — the recurring miss is no user-facing message and no reason code, so the control is unmeasurable.
8. **Transfer** — they run five attacks and record the block rate with a date.

## What the framework doesn't mention but trainers need to know

- **"Deploy existing" is a real constraint, not a shortcut.** Building a classifier is a research project; installing three existing controls this week is the job. Say that to learners who want to train their own.
- **The blocked path is the product.** A refusal that explains, offers an alternative and hands off preserves trust. A bare block creates a support ticket and a shadow-tool user.
- **Measure the false-positive rate, not just the catch rate.** Of the requests we blocked last week, how many were legitimate? Nobody asks, and it is the number that decides whether the guardrail survives.
- **Guardrails do not stop a determined attacker.** Prompt injection through uploaded documents defeats most filters; architecture is the mitigation.

## Watch out

- **Do not demo a guardrail by blocking something obviously awful.** Every control looks good against an easy case. Demo the borderline case and the false positive.
- **Do not tune thresholds by vibes in the room.** Pick a number, test against a fixed set, move it once with a reason.
- **Do not imply compliance.** A deployed guardrail is evidence of care, not a certificate.
- **The stale claim to retire:** "the model's own safety training is our moderation." In November 2026 that is one layer of three, and the weakest for domain-specific rules.
