---
id: 09.02.I.K3
tsc: 9
level: Intermediate
code: K3
title: Risk assessment methodologies
as_at: 2026-11-26
review_by: 2027-02-25
---

# Risk assessment methodologies

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Knowledge K3**

> **Framework text (verbatim):** "Risk assessment methodologies."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Knowledge · Bullet 3 of 10

**One-line version:** A methodology is what stops risk assessment from being a tour of everyone's anxieties — it makes two teams, looking at the same system, reach comparable answers.

## What it is

A risk assessment methodology is a repeatable procedure for identifying what could go wrong, estimating how likely and how bad it would be, and deciding what to do. The common ones in AI work are the risk matrix (likelihood against impact), bowtie analysis (threats and consequences mapped around a single event), and the four-axis scoring specific to AI systems: data sensitivity, tool reach, trust boundary of inputs, and how the output is consumed.

## Deep expansion

### The concept

Risk assessment answers a decision question: is this system acceptable as designed, and if not, which change buys the most reduction per dollar? An unstructured discussion cannot answer that, because every participant weights the risks they personally fear. A methodology does three jobs: it forces coverage (have we looked at data, tools, inputs, outputs?), it makes comparison possible (is this worse than that?), and it produces a record that survives the meeting.

The most important methodological point for AI is that the likelihood of an attack is not what you are estimating. Attackers are adaptive; a control with a 99% success rate fails routinely against someone who tries a hundred times. So for adversarial risks, likelihood is better read as "how exposed is this surface" — is it on the public internet, does it ingest third-party documents, does it hold valuable data — rather than "how often do we think someone will try".

Impact, by contrast, is usually easier and should be estimated in the organisation's own currency: money, personal data affected, regulatory exposure, downtime, reputation, safety of a person. If you cannot say which currency, the risk is not yet understood.

### The sub-concepts

**The risk matrix.** Two axes, three or four bands each, producing a grid from low to critical. Its virtue is speed and shared vocabulary; its weakness is false precision — two people can put the same risk in different cells and both be reasonable.

**The four-variable AI matrix.** Because generic likelihood × impact hides the AI-specific drivers, it helps to score four concrete axes instead: data sensitivity (public → regulated personal data), tool reach (none → funds, code, external mail), input trust (curated → anonymous internet plus third-party documents), output consumption (human reads it → fed into a database or another agent). The combination places the system in a tier, and the tier dictates the minimum controls.

**The lethal trifecta.** Three capabilities together — access to private data, exposure to untrusted input, ability to communicate externally or change state — mean an attacker can use the second to take the first and send it out through the third. Any system with all three is in the critical zone regardless of how the individual axes score. Breaking one leg is usually cheaper than adding controls to all three.

**Bowtie analysis.** A single unwanted event in the centre; threats and their controls on the left (prevention); consequences and their controls on the right (mitigation). It is the right tool when the event is well defined — "customer data emailed to the wrong recipient" — because it makes the difference between preventing and containing explicit.

**Agile risk.** Assessment embedded in the delivery cycle rather than performed once at the end: a short risk note per increment, reviewed as the design changes. It suits AI because the system changes every time the prompt, corpus or model version changes.

**Calibration and review.** A methodology that produces twenty critical risks has failed. Force ranking, name the top three, and set review dates. Reassessment is triggered by change, not only by the calendar.

### How it connects to the rest of the framework

`TSC9-Basic-A2` is the individual risk note this methodology aggregates into a register. `TSC9-Intermediate-K4` puts the methodologies into a management framework with tiers and cadence. `TSC9-Intermediate-A4` runs the comprehensive assessment; `TSC9-Intermediate-A1` turns the ranked risks into mitigations. `TSC9-Intermediate-K1` supplies the control set that the tier requires.

### What is current as of November 2026

Assessment practice has been reshaped by agency. Current frontier models are routinely deployed with tools, so assessments that stop at "the model's outputs" miss the part that matters.

- **Tool reach is now the dominant axis.** Two systems on the same model can differ by an order of magnitude in risk because one can send email and the other cannot.
- **Regulators and buyers both want the register.** PDPA obligations and enterprise procurement now ask for evidence of assessment, which makes the artefact as important as the analysis.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"We assessed it at design time, so we are done."* The model, the corpus and the users have changed since design time.
- *"Likelihood means someone will probably try."* For adversarial risk, exposure matters more than your estimate of intent.
- *"Everything is high risk."* A ranking where everything is critical is a ranking that has not been done.
- *"The bowtie is the same as the matrix."* The matrix compares risks; the bowtie analyses one.

## How a student should understand it

**Mental model:** the triage nurse — not a diagnosis, but a fast, consistent sorting that decides who gets seen first and who can wait.

**Things they can do after this bullet:**
1. Score three AI risks on a likelihood × impact matrix and justify the placement.
2. Use the four AI axes to place a system in a risk tier.
3. Draw a bowtie for a named failure and identify prevention versus containment controls.

**Misconceptions to kill:** that gut feel is an assessment; that adversarial likelihood is a guess about intent; that all risks deserve equal urgency.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic triage board.** A patient with chest pain, a sprained ankle and a prescription refill all want to be seen. The board sorts them by urgency, not by who is loudest. Where it breaks: clinical triage has decades of outcome data; AI risk tiers are newer and rougher.

**The bowtie as a road junction.** The junction is the event. On the left, the roads that lead into it and the barriers on each; on the right, the roads out and the barriers after. Nobody argues that one barrier is enough.

### Worked example with a real tool

Run the scoring with the model as scribe, then challenge its placements:

```
Score these three risks for a customer-support assistant that can
issue refunds up to $200 and reads incoming customer emails:
(a) it invents a refund promise,
(b) it leaks another customer's order details,
(c) it gives a rude reply.
Use likelihood x impact with 3 bands, and say which single risk you
would fix first and why.
```

What to point at afterwards: the model will often rank (a) highest because it is frequent. The room should notice that (b) is an exfiltration path created by the combination of email reading and refund authority — and that (c) costs reputation but little else. Then ask what changes if the refund limit disappears.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — put three risks on the board and ask for a show of hands on which is worst; note the disagreement.
2. **State the objective** — by the end, they can run a matrix, a four-axis tier check and a bowtie.
3. **Recall prior learning** — any workplace risk register or safety assessment.
4. **Present the content** — the three methods; exposure versus intent; the lethal trifecta; calibration.
5. **Guide** — score the support-assistant risks together and argue the placements.
6. **Elicit performance** — groups draw a bowtie for one failure.
7. **Give feedback** — debrief: which bowties put all the controls on the prevention side.
8. **Transfer** — each learner scores one risk from their own project and names the top one.

## What the framework doesn't mention but trainers need to know

- **The matrix is a conversation tool, not a measurement.** Use it to surface disagreement, then resolve it with evidence.
- **Include the data path, not just the model.** Most AI incidents are data incidents with a language model in front of them.
- **Name the currency of impact.** "High" means nothing until someone says dollars, records, or hours of downtime.
- **Re-score after every model change.** A tier set for last quarter's model may be wrong for this one.

## Watch out

- **Do not teach the matrix as arithmetic.** Multiplying 4 × 3 to get 12 invites false confidence.
- **Do not skip the trifecta check** because the axes look moderate individually.
- **Do not accept scores with no evidence.** Ask what observation produced the number.
- **Retire the stale claim:** "risk assessment is a one-off gate before launch." In November 2026 it is a standing item tied to version changes.
