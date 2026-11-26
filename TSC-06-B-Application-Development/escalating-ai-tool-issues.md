---
id: 06.01.B.A3
tsc: 6
level: Basic
code: A3
title: "Escalating an AI problem so that someone can actually fix it"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Escalating an AI problem so that someone can actually fix it

> **TSC #6 Generative AI Application Development and Deployment · Basic · Ability A3**


> **Framework text (verbatim):** "Describe and appropriately escalate issues encountered with AI tools."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Ability · Bullet 9 of 11

**One-line version:** An escalation is a request for a decision, not a forwarded screenshot.

## What it is

Escalating well means writing down what you did, what you expected, what actually happened, the exact error and its timestamp, what you already ruled out, and what you are asking for — then sending it to the right tier with personal data removed. The description is the deliverable; the diagnosis belongs to the recipient, or at least should be offered as a hypothesis rather than a verdict.

## Deep expansion

### The concept

Every support system is a queue with tiers, and each tier costs more than the one before. What moves a case efficiently is not urgency of tone but completeness of information. A report missing the error text, the time or the environment comes straight back with a question, and a day is gone.

There is a second reason to write it properly: **the act of writing it usually solves it.** The five-line format often surfaces the cause at line three. That is not a reason to withhold an escalation — it is a reason to write it before deciding whether to send.

And a third: the report is an audit trail. When a data incident is reviewed later, the difference between "we reported it immediately with evidence" and "someone mentioned it in a group chat" is substantial.

### The sub-concepts

**The five-line report.** What I did. What I expected. What happened, with the exact message. When and where — timestamp with timezone, tool, model, plan, browser or OS. What I already tried. Then: who is affected, what it costs them, and what you are asking for.

**Symptom before diagnosis.** "The bot gives wrong answers about leave" can be investigated. "The retrieval layer is broken" is a diagnosis and, if wrong, sends everyone down your path for a day. Offer hypotheses separately, labelled as such.

**Tiering.** Self-help and documentation → your team's technical contact → IT or the platform administrator → vendor support → and, separately, the data protection officer if personal data was exposed. Some issues skip tiers: a suspected leak does not wait behind a password reset.

**Severity versus urgency.** Severity is impact — how many people, how blocked, is there a workaround. Urgency is your need. A single user with a workaround is low severity even when it is urgent to them, and saying so makes the report credible.

**Confidentiality and the ask.** Strip names, NRIC numbers, account numbers and customer records before the report leaves the organisation. End with the decision you need: a fix, a workaround, a permission change, an explanation, an owner. "Please advise" is not an ask.

### How it connects to the rest of the framework

`TSC6-Basic-K3` supplies the error vocabulary this report uses; `TSC6-Basic-K5` is the procedure you complete before escalating; `TSC6-Basic-A4` is the specialised version for performance. `TSC8` covers the responsible-AI and incident-reporting obligations around a data exposure, and `TSC6-Intermediate-A1` is what the receiving engineer does with your report.

### What is current as of November 2026

- **The admin console is the first stop.** Enterprise deployments expose usage, error rates, audit logs and quota in one place; a good report quotes the console, not just the user's experience.
- **Vendors ship support assistants that are confidently wrong.** They resolve many tier-one questions and invent features that do not exist. Verify before quoting one into a ticket.
- **Deprecation notices arrive by email and need an owner.** A very common escalation in 2026 is an app that broke because a pinned model snapshot was retired on a schedule nobody read.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Escalating means forwarding the screenshot."* A screenshot has no timestamp, environment or reproduction steps. It is evidence, not a report.
- *"The louder the better."* Volume gets attention once and credibility never. Impact gets attention every time.
- *"I should wait until I understand the problem."* Waiting is right for diagnosis and wrong for exposure.

## How a student should understand it

**Mental model:** the polyclinic referral letter. The GP writes what was tried, what was found and what is suspected. A referral that says only "patient unwell" sends the specialist back to the beginning, and the patient waits.

**Three things they can do after this bullet:**
1. Write a five-line report from a messy description, with personal data removed.
2. Choose the right tier and severity, and defend both in one sentence.
3. State the ask explicitly, so the recipient knows what "resolved" looks like.

**Misconceptions to kill:** that escalation is forwarding, that urgency substitutes for impact, and that a diagnosis is more useful than a symptom.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The insurance claim form.** Every field exists because someone once left it out and the claim bounced. Learners find the form annoying, then watch a claim rejected for a missing date. Escalation templates are the same artefact for the same reason.

**The three-minute voice note.** A rambling audio message with no timestamps, no error text and no ask. The recipient listens twice and still has to call back. A five-line report is the same content, written to be acted on without a phone call.

### Worked example with a real tool

Give the room a realistic mess and ask an assistant to restructure it:

```
Rewrite the message below as a five-line issue report for our IT service desk.
Include: what I did, what I expected, what happened, the exact error and the
time, and what I already tried. Add one line stating what I am asking for.
Remove all personal data — replace names with [NAME] and reference numbers
with [REF]. Do not add facts that are not in the message; list anything
missing under "Missing information" instead of guessing.

Message: "hi the ai thing not working again since this morning, i ask it about
the invoice for tan enterprises and it anyhow say one thing then later say
another thing, i tried logout login already, my colleague also same problem,
please help urgent!!"
```

What to point at afterwards: the rewrite is clean, and it has invented an error message and a timestamp. Those two insertions are exactly what to watch for — a report with fabricated evidence is worse than a messy one. The learner fills those lines from reality (screenshot, console log, clock) and lets the model do only the restructuring. Then pairs swap and must act on each other's report without asking a question.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read the voice-note message aloud, then ask who could act on it. Ask what they would need.
2. **State the objective** — by the end you can write a five-line report, pick a tier and severity, and state the ask.
3. **Recall prior learning** — the error catalogue from K3 and the procedure from K5.
4. **Present the content** — the five lines, symptom versus diagnosis, tiers, severity versus urgency, confidentiality.
5. **Guide** — write one report together from a real incident, arguing about which line is missing.
6. **Elicit performance** — pairs write a report for a fault they have personally seen and swap with another pair.
7. **Give feedback** — the receiving pair reports what they could not determine. Every gap is a teaching point.
8. **Transfer** — each learner saves the template into their team's notes with the escalation path and data-protection contact.

## What the framework doesn't mention but trainers need to know

- **Most escalations are documentation failures.** The answer existed and could not be found. Fixing the doc prevents the next five tickets.
- **The tier you escalate to should be written down before the incident.** Under pressure, people email whoever replied last.
- **Never paste production data into a vendor's public form.** If you cannot describe the problem without it, use the approved secure channel.

## Watch out

- **Do not teach the template as bureaucracy.** Show the same problem escalated badly and well, and let the room feel the response-time difference.
- **Do not let learners write "it doesn't work".** Ban it in the exercise; the ban is the lesson.
- **The stale claim to retire:** "email the vendor's support address and wait." The path is now the admin console, the status page, then the support channel.
