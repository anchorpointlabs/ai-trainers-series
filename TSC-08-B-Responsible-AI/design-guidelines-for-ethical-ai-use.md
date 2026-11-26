---
id: 08.01.B.A4
tsc: 8
level: Basic
code: A4
title: Design guidelines for ethical AI use
---

# Design guidelines for ethical AI use

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Ability A4**

> **Framework text (verbatim):** "Design guidelines or strategies for ethical AI use, including use of sensitive data in generative AI tools."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Ability · Bullet 8 of 10

**One-line version:** A good guideline is one a new hire can follow at 5pm on a Friday without asking anyone — if it needs a meeting to interpret, it is not a guideline, it is a mood.

## What it is

Designing a guideline means writing the rule in plain language, making it concrete enough to check, and covering sensitive data explicitly — what may go into a generative AI tool, what may not, which tool is approved, who checks the output, and what to do when someone is unsure. The deliverable is a short document plus a set of worked examples that resolve the edge cases.

## Deep expansion

### The concept

Most organisations have a guideline. It says "employees must use AI responsibly and in compliance with all applicable laws". It changes no behaviour, because it answers no question anyone actually has.

The test of a guideline is behavioural: read it to someone who has never used the tool, give them a real scenario, and see whether they do the right thing without asking. If they ask, the guideline failed — and the questions they ask are free consulting on what to fix. Trainers should run that test in the room, with the learners' own drafts.

The second design principle is that good guidelines *name the approved path*. "Do not paste client data into AI tools" is half a rule; the other half is "use the enterprise assistant at this link, which does not retain your input, or the redaction steps in Appendix A". A prohibition without an alternative produces shadow AI, which is the exact outcome the guideline exists to prevent.

### The sub-concepts

**Anatomy of a workable guideline.** Six parts, each short: (1) **scope** — who and which tools; (2) **permitted use** — the approved tool and the tasks it is approved for; (3) **prohibited data** — named categories, not "sensitive information"; (4) **required verification** — what must be checked before output leaves the team; (5) **disclosure** — when a client or colleague must be told AI was used; (6) **escalation** — who to ask when unsure, and what to do in the meantime.

**Name the data, not the adjective.** "Sensitive data" is interpreted down to whatever the reader is already comfortable with. "NRIC numbers, full names with contact details, bank and card numbers, salary figures, medical information, unpublished financial results, client contracts and anything marked confidential" is interpreted correctly. The distillation's rule is a useful test: if you would not email it to a stranger, it does not go into a free tool.

**Make every rule checkable.** "Use AI appropriately" cannot be audited. "Every AI-drafted customer email is read in full by the sender before it is sent" can be — you can ask staff, sample outboxes, and see whether edits happen. Checkability is what separates a guideline from a wish.

**Cover the generative-specific cases.** Text in a tool is the obvious one. The ones learners miss: images of real people, voice recordings, meeting transcripts, screenshots of dashboards, and code from proprietary repositories. Each of those is now trivially pasteable, and each carries a different obligation.

**Disclosure to the client.** Where the work is delivered to an external party, say whether AI was used and for what. Learners resist this because it feels like admitting something; in practice it protects them, because an undisclosed AI-assisted error is a trust failure and a disclosed one is a process issue.

**Guideline versus policy.** A policy says what the organisation permits and carries consequences; a guideline explains how to comply day to day. Basic learners usually write the second, and should know which one they are writing so they do not over-promise enforcement they cannot deliver.

**Keep it alive.** Every guideline has a review date and a named owner. Model capability moves faster than document review cycles; a guideline that is two years old is describing tools that no longer exist.

### How it connects to the rest of the framework

`TSC8-Basic-K2` and `TSC8-Basic-A5` supply the content — the three checks and the privacy measures. `TSC8-Basic-A1` is the decision habit the guideline institutionalises; `TSC8-Basic-A3` is where the approved-tool list comes from, since the guideline can only name tools that survived a comparison. `TSC8-Basic-A6` is the verification duty the guideline encodes. In many organisations this document is the "acceptable use of AI" policy the distillation describes.

### What is current as of November 2026

Two changes. First, the approved-tool clause has become the hard part: assistants built on OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon are all competent, so organisations increasingly approve one vendor-standard tier and forbid consumer accounts, rather than banning AI. Guidelines that still say "do not use AI" are being ignored in practice and should be rewritten.

Second, agentic features mean a guideline now has to address *actions*, not just text: which tools may send email, book, pay or modify records without confirmation. A one-page guideline that covers pasting but not tool use is already out of date.

### Common misconceptions

- *"A guideline should be short and high-level."* Short, yes; high-level, no. Brevity comes from naming specific data and specific tools, not from vagueness.
- *"Staff should know better."* They know what they were told, which is usually nothing, and what their manager tolerates.
- *"If we write it down, we own the liability."* You already own it; the document is how you show reasonable steps were taken.
- *"One guideline covers all uses."* Customer-facing disclosure and internal drafting need different rules.
- *"The IT department should write it."* IT can list approved tools; only the business knows which data is genuinely sensitive.

## How a student should understand it

**Mental model:** the rules board at a public swimming complex. "No running on the deck. Children under 12 must be accompanied. No diving in the shallow end." Each rule names an action, a condition and a consequence, and a lifeguard can enforce it from the chair. A sign saying "please swim safely" would be ignored within a week.

**Things they can do after this bullet:**
1. Write a two-line rule for AI use that a new hire can apply without asking.
2. Turn "sensitive data" into a named list specific to their team.
3. State the verification duty and the escalation contact in the same page.

**Misconceptions to kill:** that vague is safer; that a prohibition is enough without an approved alternative; that the guideline is a legal document rather than a work instruction.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The swimming complex rules board.** As above. Where it breaks: a lifeguard enforces pool rules in real time; nobody watches AI use, so the guideline has to be designed for self-application.

**The hawker hygiene grade.** An A/B/C letter on the stall is a public, checkable claim about a process, displayed where the customer can see it. A visible AI-use statement on your own service works the same way. Where it breaks: hygiene grading inspects a physical premises against a published checklist; there is no equivalent inspection regime for most AI workflows yet.

### Worked example with a real tool

Draft, then attack your own draft:

```
Here is my draft AI-use rule for a 25-person marketing agency:
"Staff may use AI tools for drafting, but must not put sensitive client
data into them and must check all output before it goes out."

Act as a new hire on your first day. Give me 10 realistic situations where
this rule does not tell you what to do — be specific and include cases
involving client names, recorded calls, competitor screenshots, translated
copy, and images of people.

Then rewrite the rule as a 6-line guideline with: approved tool, prohibited
data list, verification duty, disclosure trigger, escalation contact.
```

What to point at afterwards: the model's ten situations are usually better than the room's, because it has seen the same ambiguity everywhere. The rewrite is a starting point, not the answer — learners must supply the approved tool name and the escalation contact, which the model cannot know. That gap is the point: the model drafts, the organisation decides.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out "employees must use AI responsibly" and ask who could follow it. Nobody.
2. **State the objective** — leave with a one-page guideline: approved tool, prohibited data, verification, disclosure, escalation.
3. **Recall prior learning** — the three checks from `TSC8-Basic-K2` and the privacy measures from `TSC8-Basic-A5`.
4. **Present the content** — the six parts, naming data not adjectives, checkability, generative-specific cases, disclosure, review date.
5. **Guide** — run the draft-and-attack example together; fill in the six parts on the board.
6. **Elicit performance** — teams draft their own guideline, then swap and try to break each other's with edge cases.
7. **Give feedback** — score each draft on one question: could a new hire apply it unaided? Mark the sentences that fail.
8. **Transfer** — each learner names the person who will own and review the document, and the date.

## What the framework doesn't mention but trainers need to know

- **Always pair the ban with the paved road.** Prohibition plus an approved alternative is a guideline; prohibition alone is a rumour.
- **The edge cases are the document.** The rule is one line; the eight worked examples are what people actually use. Budget most of the writing time for examples.
- **Managers enforce what they model.** If the team lead pastes client data, no document will hold.
- **Write for the least confident user, not the most.** The guideline's job is to make the safe action the easy one.
- **Review dates are not decoration.** Capability and product terms change quarterly; a two-year-old guideline names tools that no longer exist.

## Watch out

- **Do not write a guideline you cannot check.** Every clause should be observable in a sample, an outbox or a log.
- **Do not copy a template from the internet.** Data categories are jurisdiction- and industry-specific; NRIC, MediSave and case-trust details belong in the local version.
- **Do not imply legal advice.** Say what the organisation requires; route legal questions to the DPO or counsel.
- **The stale claim to retire:** "we'll ban it and the problem goes away." Bans without alternatives move the risk to personal phones, where you cannot see it at all.
