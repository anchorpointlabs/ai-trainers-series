---
id: 06.03.A.A3
tsc: 6
level: Advanced
code: A3
title: "Building a guardrail that did not exist yet"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Building a guardrail that did not exist yet

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A3**


> **Framework text (verbatim):** "Develop new guardrails and moderation controls to control inputs and outputs to prevent undesirable model behaviours."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 8 of 12

**One-line version:** Building a guardrail means turning a policy sentence into a mechanism, a test set, a threshold and a log — in that order, or it is just an opinion with a filter attached.

## What it is

This is the ability to create a control the market does not sell: a domain rule, a groundedness check, a numeric-claim detector, a tool-permission boundary. It starts from a policy stated precisely enough to test, chooses the cheapest mechanism that can enforce it, proves the mechanism on labelled cases, tunes the threshold against the real cost of each error, and ships it with telemetry and an owner.

## Deep expansion

### The concept

Off-the-shelf moderation answers one question: is this content acceptable in general? Most business risks need a different question: is this statement true to *our* records, permissible under *our* authority, and consistent with *our* policy? A general filter cannot know that a fee quote must match the current price list, or that an answer about a tenancy term must cite a clause.

So new guardrails are usually built at three layers at once:

1. **A policy sentence** — short, testable, and stated as a prohibition with a boundary: "the assistant must never state a course fee; it must direct the user to the fee schedule."
2. **A mechanism** — deterministic check, classifier, judge, schema constraint, or permission boundary.
3. **An evidence set** — cases that must be blocked, cases that must pass, and adversarial variants of both.

The build order matters. Teams that start with the mechanism (usually a prompt instruction) end up with a control they cannot measure, defend or improve. Teams that start with the policy sentence discover that most rules are enforceable deterministically, which is faster, cheaper and more explainable.

### The sub-concepts

**Write the policy as a test.** "Be careful about pricing" is not testable. "No numeric fee may appear unless it matches an entry in the current fee schedule; otherwise say the fee is in the schedule and link it" is testable, and it tells you the mechanism.

**Pick the weakest sufficient mechanism.** A regex on currency amounts plus a set-membership check against the schedule catches most violations for near-zero cost. A judge model handles the residual cases where the fee is implied rather than stated. Escalate only for what the cheap layer cannot catch.

**Build the two-sided test set.** Ten cases that must be blocked, ten that must pass. The must-pass set is the one teams skip, and it is the one that tells you your control is not destroying the product.

**Adversarial variants.** Rephrase, translate, split across turns, encode, embed in a document. A guardrail that only holds for the phrasing in the policy document is not a guardrail.

**Tune with a cost ratio.** State what a false block costs (a frustrated customer, an abandoned booking) and what a false pass costs (a wrong commitment, a compliance breach). The threshold follows from the ratio, and the ratio is a business decision the trainer should force the room to make explicitly.

**Instrument from day one.** Log the decision, the rule or score, the model and guardrail version, and the request ID. Without this you cannot tune, appeal or produce evidence for an auditor.

**Design the refusal.** What the user sees when blocked is part of the guardrail. A dead end generates support tickets and workarounds; "that fee is in the schedule — here is the link" preserves the journey.

### How it connects to the rest of the framework

`TSC6-Advanced-K2` is the theory this ability operationalises: control families, the two error types, and why effectiveness must be measured. `TSC6-Intermediate-A4` is deploying someone else's guardrail; this is building your own, which usually starts where that one fails. `TSC6-Advanced-A1` determines where in a multi-model pipeline the control sits — input, between hops, or output. `TSC-08` and `TSC-09` define the obligations the guardrail is enforcing.

### What is current as of November 2026

- **Judge models are good enough for nuanced policy at moderate volume.** Rubric-based checks on a frontier model handle "is this an implied commitment" better than any classifier, at a cost that only makes sense after cheaper layers have filtered the traffic.
- **Structured output and constrained decoding removed a whole class of guardrail.** If the answer must be valid JSON against a schema, malformed output is impossible rather than detected.
- **Classifier fine-tuning is cheap.** A few hundred labelled examples can produce a domain-specific detector, which is why "we cannot build that" is rarely true now.
- **Gateways made policy-as-code practical.** Rules attached to a model endpoint, versioned with the deployment, are becoming the default place to enforce controls.
- **Red-teaming is a service**, so the standard has risen: a guardrail is expected to survive an independent attempt, not just the team's own examples.

### Common misconceptions

- *"A prompt instruction is a guardrail."* It is a tendency. It has no measurable rate, no version, and no evidence trail.
- *"If it passes my tests, it works."* It passed your tests. Adversarial variants and production traffic are the real examination.
- *"The threshold is objective."* The threshold encodes a cost judgement. Someone senior should own it.
- *"The judge model is ground truth."* The judge is a model with its own errors, and it needs its own small evaluation.

## How a student should understand it

**Mental model:** the food-hygiene inspector writing a checklist for a cuisine the manual never covered. The principle is general; the specific risks — raw fish, room-temperature holding — require new lines, new tests, and a re-inspection.

**Three things they can do after this bullet:**
1. Convert a vague policy into a testable prohibition with a stated boundary.
2. Build a two-sided test set and choose a mechanism with a stated cost ratio.
3. Ship the control with a log, a version and a refusal message that keeps the user moving.

**Misconceptions to kill:** a prompt is a guardrail, passing your own tests is proof, and the judge is infallible.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The new stall, the old checklist.** The hygiene inspector's standard form covers cooked food, cold storage and hand-washing. A stall selling sashimi needs a new line: sourcing, temperature, parasite control. The inspector does not throw out the form — she adds a section, defines how it is checked, and re-inspects. That is developing a guardrail.

**The exam rubric for a new syllabus.** When the syllabus adds a component, the marker's rubric is rewritten, trialled on sample scripts, and adjusted when it punishes good answers. A guardrail with no trial on real cases is a rubric written the night before the exam.

### Worked example with a real tool

Build it with the assistant, then break it:

```
Our tuition-centre chatbot must never state a course fee.

Build me a guardrail with:
1. the policy in one enforceable sentence,
2. a deterministic check and a judge-based check,
3. ten test cases — five that must be blocked, five that must pass,
4. how I measure the false-positive rate in production,
5. what to log for an audit.
```

What to point at afterwards: the deterministic check is usually a currency pattern plus a lookup against the fee schedule, and it is genuinely good. The judge check will be described as if it were reliable — ask who evaluates the judge. Then run the must-pass cases: "is the fee refundable?" is not a fee statement, and a crude regex blocks it. That false positive is the lesson: the control must know what it is *not* guarding.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a chatbot quoting a fee from last year's brochure, and the complaint that followed.
2. **State the objective** — you will build a domain guardrail with evidence on both sides.
3. **Recall prior learning** — they know the control families and that effectiveness is measured; now they build one.
4. **Present the content** — policy sentence, mechanism ladder, test set, threshold, instrumentation.
5. **Guide** — write the policy sentence and the five must-pass cases together.
6. **Elicit performance** — teams build a guardrail for a rule from their own organisation.
7. **Give feedback** — block any design whose only layer is a prompt; challenge any test set with no must-pass cases.
8. **Transfer** — they add the guardrail to their release checklist with an owner and a review date.

## What the framework doesn't mention but trainers need to know

- **Guardrails need a human path.** Some blocks should route to a person, not a message. Design the escalation, not just the refusal.
- **False positives concentrate on vulnerable users.** People with unusual phrasing — second-language English, voice transcription, disability-related input — get blocked more. Test on them.
- **Version the rule, not just the code.** A threshold change is a behaviour change; it belongs in the changelog with a date and a reason.
- **The audit question is "show me".** Keep the decisions, not just the counts.
- **A guardrail that blocks everything is not safe, it is broken.** Track block rate as a health metric.

## Watch out

- **Do not let the room build a keyword list and call it done.** It is the exercise's most common failure and the easiest to defeat in the debrief.
- **Do not use real customer data in the exercise.** Synthetic cases, or properly de-identified ones.
- **Do not present a judge model as a compliance control** without saying it is a probabilistic layer needing its own evaluation.
- **The stale claim to retire:** "we will handle moderation with the provider's built-in filter." It handles general harm; it does not know your fee schedule, your authority limits or your tenancy clauses.
