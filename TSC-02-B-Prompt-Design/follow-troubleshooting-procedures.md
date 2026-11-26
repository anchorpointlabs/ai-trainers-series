---
id: 02.01.B.A4
tsc: 2
level: Basic
code: A4
title: Follow troubleshooting procedures
as_at: 2026-11-26
review_by: 2027-02-25
---

# Follow troubleshooting procedures

> **TSC #2 Prompt Design · Basic · Ability A4**

> **Framework text (verbatim):** "Follow standard troubleshooting procedures."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 13 of 15

**One-line version:** Record it, check the outside world, retry once in a clean chat, then escalate with facts — in that order.

## What it is

Following a standard procedure means doing the same five things in the same order when an AI tool fails, instead of improvising: note what happened and when, check the service status and the connection, retry the same harmless request once in a new chat, check the result, and pass the facts to support if it is still broken. The point is not the sequence itself. It is that the sequence produces evidence a stranger can act on.

## Deep expansion

### The concept

The habit this ability installs is *order*. Most learners, faced with an error, do the most expensive thing first: reinstall, switch browsers, rewrite the request, ask a colleague. A standard procedure is cheaper and it leaves a trail.

Five steps, and each has a reason:

1. **Record the error and the time.** Without a timestamp and the exact wording, the report is an opinion. One line in a notebook or a note app is enough: what you saw, when, what you were doing.
2. **Check the service status page, then check whether an approved public website loads.** Status tells you whether the provider knows about an incident. A working website tells you your connection is broadly fine. Neither proves anything on its own; both narrow the field.
3. **Retry once, in a new chat, with the same harmless request.** Same tool, same settings, one deliberate variable: a clean session.
4. **Check the result and record it unchanged.** If it now works, note "retry succeeded" and carry on. If the same error appears, you have a reproducible failure rather than a one-off.
5. **Escalate with the evidence.** Error, time, status findings, connection finding, retry result, and what you have already ruled out. No passwords, no private conversation content.

The discipline is that steps three and four are one retry, not a loop. Repetition adds no information and can trip rate limits.

### The sub-concepts

**Evidence over narrative.** "It's not working" cannot be actioned. "10:15 on 15 November, error generating a response, status page clear, other sites load, same error after one retry in a new chat" can.

**One retry is a test.** It answers exactly one question: is this transient? It does not answer why, and it should not be repeated to look thorough.

**Leave security settings alone.** Disabling protections to "see if that fixes it" is the standard way a small problem becomes a large one. If workplace guidance forbids it, that is the answer; for real problems, follow the organisation's procedure.

**The status page is aggregated.** Your region, your account or your tier can be affected while the page is green. Record what the page said; do not treat it as a verdict.

**Escalation is completion, not failure.** A well-formed support message is the successful end of the procedure when the fault is not yours.

**Not every problem is a service problem.** If the answer arrives and is wrong, this is the wrong procedure — go to `TSC2-Basic-K1`'s classification step and check the prompt instead.

### How it connects to the rest of the framework

`TSC2-Basic-K1` is the reasoning behind the steps; `TSC2-Basic-A2` is recognising which kind of issue you have; `TSC2-Basic-K4` covers the case where the tool works but the output strayed. The same procedure appears at application level, with logs, in `TSC6-Basic-A3`.

### What is current as of November 2026

Two practical changes. First, most 2026 products surface failures in more places — browser, desktop app, mobile app, API — and the error text differs in each, so "which surface" is now part of the record. Second, current frontier assistants are generally more reliable moment-to-moment than their predecessors, which means a persistent failure is more likely to be account-level, regional, or a permission problem than a transient blip. That makes step five — a specific, evidenced report — more often the productive one.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"If it fails, try five times."* One retry answers the transient question; the rest is noise.
- *"A clear status page means the problem is mine."* It means the provider has not published an incident.
- *"Support needs the whole conversation."* Support needs the error, the time, the checks and the retry. Private content is a liability, not evidence.
- *"Turning off the security warning will show me the cause."* It shows you a second problem.

## How a student should understand it

**Mental model:** a fire drill. Nobody improvises the route during a fire; the route was decided calmly in advance, and the value is that everyone does the same thing without thinking.

**Things they can do after this bullet:**
1. Write a five-line record of a failure, in order, with no personal data.
2. Perform exactly one controlled retry and describe the result.
3. Draft a support message with the evidence and nothing else.

**Misconceptions to kill:** retry-as-ritual; status-page-as-verdict; detail-as-helpfulness.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The GP clinic triage.** Fever, cough, and a form at the counter: symptoms, duration, what you have already taken. The form is not bureaucracy; it is what lets the doctor help in four minutes instead of fifteen. A support ticket is the same form. Where it breaks: a clinic can examine you; support can only reproduce what you describe, so the description has to be complete on its own.

### Worked example with a real tool

Everything in this prompt is simulated — read it, then write your own record before generating the model answer.

```text
This is a simulation. Do not access websites, send messages or claim to have checked a real service.

Invented case: At 10:15 on 15 November 2026, Singapore time, a user asked a web-based AI chat: "List two ways to save water." The screen showed "There was an error generating a response." The provider's fictional status page reports no known incident, and an approved public website loads. When the user starts a new chat and retries exactly the same request once, the same error appears. No other changes were made.

Produce a model action record for a learner to compare with their own. Use five numbered steps in order: record the error and time without sensitive information; check the fictional service status and connection evidence; isolate the chat session by using a new chat and retrying the same request once; check the retry result without guessing its cause; escalate the unresolved issue to IT support. End with a short support message containing the error, time, status and connection checks, the retry and its result. Treat all checks and actions as simulated. Do not suggest disabling security controls or include names, passwords or private conversation content.
```

What to point at afterwards: the model answer is not the point — the comparison is. Read a learner's five steps beside the model's and mark each against the procedure. Then read the support message aloud and ask what is missing. The most common omission is the time; the second is that the retry used the *same* request. Both are cheap to fix and both decide whether the report is actionable.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "A chat gives an error instead of an answer. What should you do before changing settings or trying repeatedly?" Take two suggestions and hold them for comparison.
2. **State the objective** — by the end you can run the five steps and write the escalation message.
3. **Recall prior learning** — the three fault areas from `TSC2-Basic-K1`; the observation-versus-diagnosis habit from `TSC2-Basic-A2`.
4. **Present the content** — the five steps, one retry, the status-page caveat, what never goes in a ticket.
5. **Guide** — role-play the simulated case together and fill in the record on the board.
6. **Elicit performance** — pairs write their own record and support message before running the prompt.
7. **Give feedback** — compare against the model answer; mark missing time, changed variables, missing retry result.
8. **Transfer** — each learner saves the five-line template somewhere they will actually find it.

## What the framework doesn't mention but trainers need to know

- **The single-retry rule is a classroom convention.** Providers may suggest more; the classroom needs a rule that produces evidence rather than hope. Say which is which.
- **Record-keeping is the transferable skill.** Most learners will never diagnose a service fault; all of them will need to report one.
- **Permission problems masquerade as errors.** In workplace deployments, "it works for my colleague" is often an access issue, not a service one.
- **The evidence template should fit on a card.** Error, time, surface, status, connection, retry, result — seven fields, one line each.

## Watch out

- **Do not perform real checks in a simulation.** Notice that the worked prompt says so explicitly; learners copy that caution.
- **Do not let anyone paste a private conversation into a ticket.** Model the redacted version every time.
- **Do not treat the status page as proof.** Say what it reported; do not say what it means.
- **The stale claim to retire:** "restart everything and try again." In November 2026 a recorded single retry produces more useful information than a reboot ritual, and it can be handed to someone else.
