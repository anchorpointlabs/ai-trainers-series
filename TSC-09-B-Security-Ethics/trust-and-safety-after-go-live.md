---
id: 09.01.B.K4
tsc: 9
level: Basic
code: K4
title: Trust and safety after go-live
as_at: 2026-11-26
review_by: 2027-02-25
---

# Trust and safety after go-live

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Knowledge K4**

> **Framework text (verbatim):** "General trust and safety practices post go-live."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Basic** · Knowledge · Bullet 4 of 8

**One-line version:** Launch is the day the testing stops being hypothetical — so trust and safety after go-live is a standing loop of watching, triaging, patching and re-testing, not a sign-off.

## What it is

Post-go-live trust and safety is the ongoing practice of keeping an AI system acceptable once real users, real data and real attackers are on the other side of it. It covers monitoring what the system does, catching new abuse and new failure, responding to incidents, and feeding what you learn back into the guardrails and the test set. The framework calls it "general practice"; in operation it is a weekly rhythm with named owners.

## Deep expansion

### The concept

A launched AI system drifts. Not because anything broke, but because the world around it moves: users discover new ways to ask, attackers publish new prompts, the model vendor ships a new version, the document corpus is updated by someone who has never heard of the policy, and the business changes a rule that the prompt still states the old way. None of these is a defect at the moment it happens. Together they mean that the system you tested in October is not exactly the system running in January.

So the loop is: **observe** what the system is doing, **triage** what looks wrong, **fix** the control or the data, **re-test** to prove the fix, and **record** so the next person inherits knowledge instead of folklore. The output of the loop is not just fewer incidents; it is an evidence trail that the organisation exercised reasonable care.

For a Basic audience, the crucial correction is about the shape of the work. It is not a project with an end date. It is closer to how a shop handles cleanliness: a daily wipe-down, a weekly deep clean, and a response when something spills.

### The sub-concepts

**What to watch.** Four signals, in plain language: what people are asking (new topics, sudden spikes, repeated attempts at the same thing); what the system is refusing (a jump in refusals usually means either a new attack pattern or a guardrail that is too tight); what the system is doing with tools (unusual actions, unusual volumes, actions at odd hours); and what it costs (a spend spike is a signal of automated abuse as much as of popularity).

**New abuse.** Jailbreaks and injection prompts circulate publicly within days of a model or product release. A prompt that worked on someone else's bot will be tried on yours. The post-launch practice is to keep a source for these — a watch list, a vendor advisory, a community — and to replay new ones against your system.

**Drift.** The system's behaviour changes when the model version changes, when the retrieval corpus changes, or when the prompt is edited by someone who did not know why a line was there. Drift is not always a regression in quality; it can be a regression in safety, with quality unchanged.

**Incident response.** When something goes wrong: contain it (switch the tool or the endpoint off), assess what was exposed and to whom, fix the cause, and communicate to whoever needs to know — including, where personal data is involved, whoever owns the PDPA obligation. Containing first and diagnosing second is the discipline that separates an incident from a disaster.

**The kill switch.** A pre-agreed way to disable a specific capability — external sending, code execution, a particular tool — without taking the whole product down. Deciding this during an incident is too late.

**The review rhythm.** A weekly look at refusals, flagged conversations and tool actions; a monthly or quarterly review of the guardrail rules against what users actually ask; a test-set replay whenever the model, prompt or corpus changes.

### How it connects to the rest of the framework

`TSC9-Basic-K3` is the control layer that this loop maintains. `TSC9-Basic-K2` produced the test set that the loop replays. `TSC9-Basic-A2` is where the findings get written down. At Intermediate, `TSC9-Intermediate-A6` makes monitoring a lifecycle discipline, and `TSC9-Intermediate-A1` turns findings into mitigations rather than apologies.

### What is current as of November 2026

Two things have changed the post-launch picture. First, model updates arrive continuously rather than as annual releases — current frontier models are delivered as a moving service, so "the model changed" is a routine event, not an incident. Second, agents with tools are now ordinary, which means post-launch monitoring has to cover *actions*, not just answers.

- **Version changes are the most common cause of sudden behaviour change.** Pin versions where the vendor allows it, and replay the test set when you move.
- **Attack traffic is now automated.** Expect probing within hours of any public launch; rate limits and spend caps are part of trust and safety, not just cost control.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"We launched, so the project is done."* Launch is when the evidence starts arriving. The work changes shape; it does not end.
- *"No complaints means no problems."* Users do not report a bot that quietly gives a plausible wrong answer. They stop using it, or they act on it.
- *"Monitoring means reading the logs when something happens."* That is forensics. Monitoring means someone looks on a schedule, with a threshold that triggers action.
- *"If it worked in testing, it still works."* The corpus, the model and the users have all moved since testing.

## How a student should understand it

**Mental model:** a swimming pool with a lifeguard — the pool does not become safe because it was built to code; it stays safe because someone is watching, and there is a whistle and a pole.

**Things they can do after this bullet:**
1. Describe the observe–triage–fix–retest–record loop in their own words.
2. Name four things to watch after launch and who should look at them.
3. Say what they would switch off first if a data-leak path were found.

**Misconceptions to kill:** that go-live ends the work; that silence means safety; that logs are only for after-the-fact blame.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker stall's daily routine.** The stall opens at six; by six-fifteen the owner has wiped the counter, checked the chiller temperature, and thrown out yesterday's garnish. Nobody audits this daily. It is what keeps the stall's licence, its customers and its reputation. Post-launch trust and safety is that routine, with a weekly review instead of a daily wipe.

**The lift maintenance contract.** The lift passed inspection before the building opened, and it still has a monthly service and an emergency phone. Nobody argues that the inspection made the contract unnecessary. Where the analogy breaks: lift failures are mechanical and repeatable; AI failures arrive as novel sentences.

### Worked example with a real tool

Set up the triage conversation with a real model, using a realistic week of signals:

```
Our support bot went live three weeks ago. This week:
- refusal rate up 3x
- average conversation length up sharply
- API spend doubled
- three customers say the bot "promised" a refund
Give me a triage plan: what to check first, what each signal could
mean, and which checks are one-hour jobs versus one-week jobs.
```

What to point at afterwards: the model will usually reach "someone is attacking you" and "your guardrail is too tight" as competing explanations for the refusal spike. Both are plausible, and only the logs distinguish them. That is the lesson: the signal is not the diagnosis.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read a short news-style item about a jailbreak circulating for a popular assistant, and ask what the team would do on a Monday morning.
2. **State the objective** — by the end, they can describe the loop and name the four signals to watch.
3. **Recall prior learning** — any operations routine they know: stock check, safety walk, shift handover.
4. **Present the content** — drift, new abuse, incident response, kill switch, review rhythm.
5. **Guide** — run the triage prompt together and argue both explanations.
6. **Elicit performance** — groups write a one-page weekly review for a system they know.
7. **Give feedback** — compare reviews: who named an owner, a threshold and an action?
8. **Transfer** — each learner adds one monitoring line to their team's existing checklist.

## What the framework doesn't mention but trainers need to know

- **Someone must own the queue.** Monitoring without a named owner produces dashboards nobody opens.
- **Set thresholds in advance.** "Refusals up 3x" is only actionable if someone agreed, before the incident, that 3x triggers a look.
- **Keep the transcript, not just the score.** A classifier that says "blocked" is useless in a review; the conversation is the evidence.
- **Plan for the quiet failure.** The most expensive post-launch problem is usually not an attack but a plausible wrong answer that spread through a workflow for six weeks.

## Watch out

- **Do not present monitoring as surveillance of staff.** Be explicit that the object is the system's behaviour and the data it touches.
- **Do not promise a permanent fix.** The honest phrasing is "contained, tested, and watched".
- **Do not skip the boring part.** The weekly review is the control; the tooling only feeds it.
- **Retire the stale claim:** "we will monitor it after launch" as a substitute for pre-launch testing. Monitoring catches what testing missed; it does not replace it.
