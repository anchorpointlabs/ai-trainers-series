---
id: 08.03.A.A8
tsc: 8
level: Advanced
code: A8
title: Devise interdisciplinary approaches
as_at: 2026-11-26
review_by: 2027-02-25
---

# Devise interdisciplinary approaches

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A8**

> **Framework text (verbatim):** "Devise interdisciplinary approaches to address ethical challenges in AI, including moderating AI-generated content as required."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 12 of 14

**One-line version:** No single discipline can see the whole problem, so the approach is the team, the handoffs and the person who owns the outcome.

## What it is

An interdisciplinary approach assembles the disciplines a problem actually needs — law, product design, engineering, community or domain expertise, operations — and produces a solution none of them would have produced alone. Content moderation is the canonical case: what is illegal, what is harmful but lawful, what a community will accept, what a classifier can detect, and who answers the appeal are five different questions owned by five different people.

## Deep expansion

### The concept

Start from the failure, not the org chart. Write down what goes wrong if only one discipline is in the room.

A lawyer alone produces a policy that is defensible and unusable: rules nobody can apply at the speed of a live feed. An engineer alone produces a classifier with a threshold and no policy, so over-blocking becomes a silent product decision. A designer alone produces a reporting flow nobody trusts. A community representative alone produces a list of grievances without an implementable rule.

The moderation stack is the worked example every learner should be able to draw. **Policy** defines categories, with worked examples and edge cases, in the languages the users speak. **Detection** runs classifiers, hash matching and provenance checks, knowing each has a false-positive and false-negative profile. **Human review** handles the ambiguous band, staffed by people with language coverage, psychological support and time — not a queue designed for throughput. **Appeal** gives the affected person a route to a human with authority to reverse. **Transparency** reports volumes, error rates and categories, so the policy can be argued about with evidence.

Each layer belongs to a different discipline, and the seams are where failures happen: a classifier tuned by engineering, a policy written by legal, an appeal route designed by nobody.

### The sub-concepts

**Team composition follows the harm.** Harms to a community need that community; harms to workers need workers or their representatives; harms from a model need someone who can read an evaluation report.

**The translator role.** Effective teams have at least one person fluent in two disciplines — an engineer who can read a statute, a lawyer who can read a confusion matrix. Without a translator, the handoffs fail politely.

**Language coverage is a staffing decision.** Moderating Singlish, Malay and Tamil requires people who read them; a model that handles standard English will not compensate.

**Over-blocking is a harm.** A moderation system that removes legitimate speech from a minority dialect has made a policy choice, and it should be measured and reported like any other error.

**Contestability.** Every automated action needs a human route to reverse it, with a response time and a named owner. The gig rider deactivated by a fraud model is the reference case.

**Accountability does not diffuse.** A committee can advise; one named person owns the outcome and the appeal statistics.

### How it connects to the rest of the framework

`TSC8-Advanced-K4` supplies the dimensions the team must cover; `TSC8-Advanced-A7` is the assessment the team produces; `TSC8-Advanced-A3` builds the adversarial cases moderation will face; `TSC8-Advanced-K3` explains why the legal boundary differs by market; `TSC8-Advanced-A10` is how the case for resourcing it gets made.

### What is current as of November 2026

Synthetic media broke the old moderation assumption that detection could be automated. Provenance metadata helps where it survives — signed manifests and statistical watermarks — but stripping metadata is trivial, so detection is probabilistic and appeal-heavy. Volume has also shifted: generative systems produce content at a rate human review cannot match, which pushes teams toward triage by risk rather than review by default. In Singapore the legal frame for online harms sits in OCHA and POFMA plus election-advertising rules, while platforms set their own broader policies — so the interdisciplinary team is negotiating three boundaries at once: illegal, harmful, and unwelcome.

### Common misconceptions

- *"Moderation is a classifier."* A classifier is one layer of five, and the other four are where trust is won.
- *"One team can own the whole stack."* Policy, detection, review, appeal and reporting are different skills with different failure modes.
- *"The law tells us what to remove."* Law sets a floor; platform policy goes further, and the gap is a judgement call.
- *"Users will report problems."* Most affected people leave rather than report, so silence is not evidence of success.

## How a student should understand it

**Mental model:** the hospital multidisciplinary team. Surgeon, radiologist, oncologist, nurse and medical social worker each see a different part of one patient; the treatment plan is written once, and one consultant owns it.

**Things they can do after this bullet:**
1. Name the disciplines a given problem needs and what each contributes.
2. Draw the five-layer moderation stack and assign an owner per layer.
3. Explain why a single-discipline solution fails at a named seam.

**Misconceptions to kill:** moderation is a model, one team can own it, and the law defines the whole policy.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hospital MDT.** No oncologist decides alone, and no plan exists without a named consultant who owns it. Where it breaks: a hospital has decades of shared protocol; a moderation team is usually assembled in months.

**The MRT disruption response.** Engineering isolates the fault, operations reroutes the crowd, communications tells passengers, police manage the platform, and one incident commander owns the outcome. Remove any one and the recovery fails in a different way. Where it breaks: a train fault has a visible end; a moderation policy never finishes.

### Worked example with a real tool

```
A community platform must moderate AI-generated content in English, Singlish,
Malay and Tamil. Design the approach.
Give me: (1) the disciplines to involve and what each decides, (2) the five
layers of the stack with an owner per layer, (3) the two seams most likely to
fail, (4) how an appeal reaches a human with authority to reverse.
```

What to point at: groups get policy and detection right and leave appeal blank. Ask who reads the appeal at 11pm on a Sunday, in Tamil, with authority to reverse the decision. That question exposes whether the approach is a design or a diagram, and it is the one regulators ask after an incident.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two moderation errors side by side: a missed threat and a removed legitimate post in Singlish. Ask which one makes the news.
2. **State the objective** — design the team, the stack and the appeal route.
3. **Recall prior learning** — contestability and automated decisions from the principles block.
4. **Present the content** — the five layers, the seams, the translator role.
5. **Guide** — draw the stack together for one platform.
6. **Elicit performance** — groups adapt it to a different harm (fraud ads, harassment, deepfakes).
7. **Give feedback** — probe staffing, language coverage and response times.
8. **Transfer** — each learner maps one live moderation or review process they own.

## What the framework doesn't mention but trainers need to know

- **Reviewer welfare is an ethical issue.** Sustained exposure to harmful content causes real harm; rotation, counselling and limits are part of the design.
- **Vendor moderation tools hide their error profile.** Ask for per-language false-positive and false-negative rates, and test them.
- **Transparency reports are a governance instrument.** Without published error rates, nobody can argue about the policy with evidence.
- **The appeal route is the cheapest trust-building investment.** It is also the first thing cut under cost pressure.

## Watch out

- **Do not design moderation as a purely technical problem.** The policy and appeal layers decide whether it is legitimate.
- **Do not assume English-language tooling generalises.** Test before promising coverage.
- **Do not let the committee become the accountable party.** Name a person.
- **The stale claim to retire:** "We have a moderation model." You have one layer of five.
