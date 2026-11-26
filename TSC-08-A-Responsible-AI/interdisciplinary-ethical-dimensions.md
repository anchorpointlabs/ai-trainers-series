---
id: 08.03.A.K4
tsc: 8
level: Advanced
code: K4
title: Interdisciplinary ethical dimensions
as_at: 2026-11-26
review_by: 2027-02-25
---

# Interdisciplinary ethical dimensions

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Knowledge K4**

> **Framework text (verbatim):** "Ethical dimensions of AI through interdisciplinary perspectives (e.g. legal, cultural, socio-political, environmental aspects)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Knowledge · Bullet 4 of 14

**One-line version:** Ethics is four lenses on one decision, and the decision is where they disagree.

## What it is

Any real AI decision is simultaneously legal, cultural, socio-political and environmental. Legal asks whether it is permitted; cultural asks whether the people affected find it acceptable; socio-political asks who gains power and who is watched; environmental asks what it costs in energy, water and hardware. These lenses are not four separate subjects to be covered one after another — they are four readings of the same artefact, and the ethical work happens where the readings conflict.

## Deep expansion

### The concept

A single lens always produces a confident answer, and that confidence is the trap. Legal analysis says a facial-recognition system for crowd control is permitted under existing law; it says nothing about whether the people being scanned consented in any meaningful sense, whether the burden falls evenly across neighbourhoods, or what the compute and camera infrastructure costs. Cultural analysis says a Singlish-speaking assistant feels local; it says nothing about whether the underlying model was trained on data the speakers never agreed to provide.

Holding four lenses means producing four readings and then naming the tension. Sometimes the lenses reinforce: a system that is lawful, welcomed and cheap to run is rare but real. More often one lens buys what another pays for, and the ethical decision is which cost you accept and who you tell about it.

### The sub-concepts

**Legal.** What statute, contract and regulator permit — PDPA obligations on consent and notification, MAS FEAT for financial institutions, HSA rules for clinical tools, the EU AI Act where the output reaches Europe. Law is a floor. Everything above the floor is still a choice.

**Cultural.** What the affected community finds acceptable, including language. A model that handles standard English fluently and fails on Singlish, Malay or Tamil is not neutral — it distributes service quality by dialect. Representation matters too: an image tool that renders "CEO" one way and "cleaner" another encodes a hierarchy nobody voted for, which is representational harm even where no loan is refused.

**Socio-political.** Who holds the power the system consolidates. A workplace monitoring tool shifts bargaining power to the employer; an automated fraud flag that deactivates a delivery rider shifts risk onto the weakest party in the chain. This lens asks who can appeal, who can see the log, and who can turn it off.

**Environmental.** Compute is physical: electricity, water for cooling in a tropical data centre, and embodied carbon in short GPU refresh cycles. The ethical question is proportionality — routing ten million trivial classification calls through a frontier model when a small distilled model would do is a choice with a cost that appears on nobody's project budget.

**The conflict rule.** Name the two lenses in tension, state what each would have you do, then decide and record the reasoning. A decision without the recorded tension is indistinguishable from an accident.

### How it connects to the rest of the framework

`TSC8-Advanced-A7` is this bullet applied as an assessment; `TSC8-Advanced-A8` is the interdisciplinary team that carries it out; `TSC8-Advanced-K1` supplies the legal lens in standards form; `TSC8-Advanced-K3` is what happens when the legal lens differs by jurisdiction; `TSC8-Advanced-A5` is the dilemma analysis when two lenses cannot both be satisfied.

### What is current as of November 2026

Two lenses have moved fastest. The socio-political one now includes agentic systems that act without a human present, which changes who is accountable rather than merely who is watched. The environmental one has become a procurement question in Singapore specifically: data-centre efficiency standards and tropical cooling constraints make compute choices visible to facilities and finance, not just to engineers. Culturally, the practical instrument is the localised evaluation set — Singlish code-switching, Malay and Tamil coverage, local religious sensitivities — because generic benchmarks do not measure the failure that matters here. Current frontier models are more capable across languages than their predecessors, which raises the bar rather than removing the question.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"If it is legal, it is ethical."* Law is the floor. Most governance failures in the case literature were lawful at the time.
- *"Cultural fit means translation."* It means dialect, register, imagery and who is represented in the examples.
- *"Environmental cost is a facilities issue."* Model choice is an ethics decision with a measurable footprint.
- *"Four lenses means four meetings."* It means four questions asked of one decision, in one conversation, before it ships.

## How a student should understand it

**Mental model:** a four-lens camera pointed at one object. Each lens renders a true image, and none of them is the object.

**Things they can do after this bullet:**
1. Name the four lenses and give one question each.
2. Take a decision and produce four readings of it.
3. State a trade-off as a trade-off rather than as a conclusion.

**Misconceptions to kill:** legal equals ethical, culture equals language, and environment is someone else's department.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Buying an HDB flat.** Legality: do you meet the eligibility scheme. Culture: how close to your parents, which market. Socio-political: the ethnic integration policy deliberately shapes who your neighbours are. Environment: afternoon sun, cross-ventilation, distance to transport. Every buyer weighs all four, and the trade-offs are explicit in the paperwork. Where it breaks: HDB policy states its trade-offs; AI projects usually do not, which is exactly the gap this bullet fills.

**The four-language menu.** A hawker stall prints its menu in English, Chinese, Malay and Tamil. The dish is the same; the negotiation with each customer is not, and a stall that prints only English has made a decision about who it serves. Where it breaks: translation is the easy version of the cultural lens — the hard version is what the model assumes about the customer.

### Worked example with a real tool

```
A city wants AI CCTV for crowd control at large events.
Give me four short readings of this decision:
1. legal (which Singapore rules apply and what they require)
2. cultural (what residents will and will not accept)
3. socio-political (who is watched, who can appeal)
4. environmental (compute and infrastructure cost)
Then name the sharpest conflict between two lenses.
```

What to point at: models reliably produce the legal reading and reliably underweight the socio-political one, usually framing it as "public trust". Ask the room who would be scanned most often and who would never be scanned at all. That question, not the statute, is where the conflict surfaces — and it is the one a policy paper usually omits.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — one decision, four one-line readings on the board, all true and mutually uncomfortable.
2. **State the objective** — produce four readings and name one conflict.
3. **Recall prior learning** — bias and privacy bullets give the cultural and socio-political content.
4. **Present the content** — the four lenses with one Singapore instrument each.
5. **Guide** — work the CCTV example together.
6. **Elicit performance** — groups pick a decision from their own sector and run the four lenses.
7. **Give feedback** — challenge any group whose four readings do not conflict; they have not looked hard enough.
8. **Transfer** — each learner adds a conflict line to a live project document.

## What the framework doesn't mention but trainers need to know

- **The environmental lens is missing from most frameworks.** The IMDA and EU texts mention sustainability; almost no audit tests it. That makes it the easiest lens to drop and the easiest to be caught on.
- **Culture is not a checklist item.** It shows up in evaluation data, imagery, register and refusal behaviour — four different places, four different owners.
- **Power analysis makes rooms uncomfortable.** Expect resistance when you ask who benefits; that resistance is the lesson.
- **Lens conflicts need a decision owner.** Four readings with no decider is analysis theatre.

## Watch out

- **Do not let environmental become a slogan.** Concrete: model right-sizing, inference volume, cooling constraints.
- **Do not treat culture as folklore.** It is measurable in failure rates by dialect and in representation in outputs.
- **Do not imply every conflict resolves.** Some are accepted costs, and saying so honestly is better than a false synthesis.
- **The stale claim to retire:** "We did the legal review, so ethics is covered." The legal review covers one lens out of four.
