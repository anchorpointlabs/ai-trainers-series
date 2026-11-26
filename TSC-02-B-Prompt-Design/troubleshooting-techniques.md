---
id: 02.01.B.K1
tsc: 2
level: Basic
code: K1
title: Troubleshooting techniques
as_at: 2026-11-26
review_by: 2027-02-25
---

# Troubleshooting techniques

> **TSC #2 Prompt Design · Basic · Knowledge K1**

> **Framework text (verbatim):** "Techniques in troubleshooting AI tools."
>
> **TSC #2** Prompt Design · **Basic** · Knowledge · Bullet 5 of 15

**One-line version:** Separate the fault into a bad answer, a bad connection or a bad service — then change one thing, retry once, and write down what you saw.

## What it is

Troubleshooting is the discipline of working out why a tool is not doing what you expect, without guessing. The first move is not to fix anything; it is to classify. Did an answer arrive and disappoint you, or did no answer arrive at all? Those are different problems with different checks, and mixing them is why people restart laptops over a badly worded prompt.

## Deep expansion

### The concept

Every AI problem a Basic learner meets falls into one of three areas, and the areas are tested in a fixed order because the cheap checks come first.

**The prompt.** An answer arrived, but it was the wrong shape, the wrong length, or contained something you did not supply. This is the most common cause and the easiest to test: compare the reply with your instruction, then change one wording.

**The connection.** No usable answer appeared, and the evidence points at the path between you and the service. The cheap test is to load another website you are permitted to use. If that also fails, the problem is likely yours or the network's, not the model's.

**The service.** No usable answer appeared, the network is fine elsewhere, and the provider's status page shows an incident. That is a clue pointing at the provider, not proof — a status page can be clear while your region is degraded, and a page can be stale.

The technique underneath all three is the same: hold everything still, change one thing, observe, record. A single test is a clue. Only a controlled comparison distinguishes "the prompt was wrong" from "the service was having a bad afternoon".

### The sub-concepts

**Classify before you fix.** Content problem, layout problem, refusal, or service error — four different observations, four different first moves. A refusal is not a fault and an error message is not a diagnosis.

**One variable at a time.** Change the prompt and the network together and you learn nothing, even if the problem disappears. This is the single most transferable habit from this bullet, and it is why the classroom version changes exactly one number.

**A retry is a test, not a ritual.** Retrying the identical request tells you whether the failure was transient. Retrying ten times tells you nothing new and may look like abuse to a provider's rate limits.

**Record what you saw, not what you think.** Time, the exact error text, what you changed, what happened. "It was broken" is not evidence; "10:15, error generating a response, same request in a new chat, same error" is.

**Escalation is a technique.** Knowing when to stop diagnosing is part of troubleshooting. If a clear instruction, a working connection and a clear status page still produce nothing, the next productive step is a support ticket with the evidence attached — and never with your password.

### How it connects to the rest of the framework

`TSC2-Basic-A2` is recognising an issue (naming what you see); this bullet is the technique set behind it; `TSC2-Basic-A4` is the standard procedure someone else may have written down. `TSC2-Basic-K4` covers the case where the issue is an output that strayed, not a tool that failed. Troubleshooting also pays off in `TSC2-Basic-K5`: the fastest fix for a bad answer is usually better construction.

### What is current as of November 2026

Two things have changed. First, error surfaces have multiplied: the same product can fail differently in a browser tab, a desktop app, a mobile app and an API, and the error text is rarely the same in each. Second, agents and connected tools make "no answer" rarer and "wrong action" more common — a tool-enabled assistant may not error at all, it may simply do the wrong thing with the right permissions. That is not a troubleshooting case; it is a guardrail case (`TSC2-Basic-K4`). With current frontier models, most failures a Basic user sees are still the two old ones: an unclear prompt, and a transient service blip.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The answer was bad, so the internet must be down."* A bad answer is a prompt problem until proven otherwise. Nothing about a poor notice suggests a network fault.
- *"I'll change the prompt, the model and the browser and see if it helps."* Then you will never know which one mattered.
- *"The status page says all systems operational, so the fault is mine."* Status is aggregated; individual availability can differ.
- *"The AI told me there was an outage."* Models invent plausible error text. Use the provider's page or an actual error message, not a sentence in the reply.

## How a student should understand it

**Mental model:** a triage nurse. You do not treat the patient at the door; you sort them into the right queue using a few cheap checks, and you write down what you saw.

**Things they can do after this bullet:**
1. Classify a failure as prompt, connection or service, and name the check for each.
2. Change one factor, retry once, compare, record.
3. Decide when to stop and escalate, and what evidence to attach.

**Misconceptions to kill:** that a bad answer means a broken tool; that multiple simultaneous changes are efficient; that a reply's own explanation of the error is evidence.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT delay notice.** When a train stalls, you do not conclude the whole network is down. You check the platform screen, then the app, then whether another line is moving. Three cheap checks, in order, each narrowing the fault. Where it breaks: a train delay has an official cause published within minutes; an AI service often has no explanation at all, so you must be comfortable ending with "unresolved".

### Worked example with a real tool

Run both prompts in fresh chats, same tool, same settings:

```text
Using only these fictional facts, write a queue summary in 1 sentence.
Open tickets: 3
Closed today: 5
```

```text
Using only these fictional facts, write a queue summary in 2 sentences.
Open tickets: 3
Closed today: 5
```

What to point at afterwards: one character changed. Prompt 1 conflicts with the requirement (two sentences), which is why it belongs first — it teaches learners to check the instruction before blaming the tool. Count sentences in both replies, confirm both mention 3 open and 5 closed, then ask: "if the second reply had also come back in one sentence, what would you do?" The answer is retry once, unchanged, and record the result — not rewrite the prompt five times.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "What would you check first if a reply had the wrong format? What if no reply appeared at all?" Collect one suggestion for each.
2. **State the objective** — by the end you can name the fault area, run one controlled test, and write an evidence note.
3. **Recall prior learning** — the "change one word" comparison from earlier bullets; same control, new purpose.
4. **Present the content** — three areas, four observations, one-variable testing, evidence, escalation.
5. **Guide** — work the two queue prompts together and fill in a three-line evidence note on the board.
6. **Elicit performance** — pairs run both prompts, record results, then classify two invented failure descriptions.
7. **Give feedback** — compare classifications; challenge any that name a cause rather than an observation.
8. **Transfer** — each learner writes the evidence note they would actually send to their IT contact.

## What the framework doesn't mention but trainers need to know

- **Most "AI problems" are prompt problems.** If your course spends an hour on outages and five minutes on unclear instructions, the proportions are inverted.
- **The classroom cannot reproduce a real outage.** Say so, and use simulations with invented error text rather than pretending.
- **Rate limits feel like errors.** A learner hammering retry can hit a limit and read it as a service failure; one retry is both good method and good manners.
- **Evidence notes are a workplace artefact.** Teaching the five-line note is often more valuable than teaching the diagnosis, because the note is what gets the problem fixed.

## Watch out

- **Do not let anyone diagnose a cause from one observation.** "It's the server" after a single bad reply is the habit you are trying to break.
- **Do not demo on your own account under pressure.** Have a second tool ready in case the live service genuinely fails mid-session — and use the failure as the lesson if it does.
- **Do not ask for passwords or paste real conversations into a support message.** Model the safe version every time.
- **The stale claim to retire:** "clear your cache and it will work." In November 2026 the useful checks are the instruction, the connection and the provider's status — in that order.
