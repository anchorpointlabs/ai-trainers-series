---
id: 05.03.A.A7
tsc: 5
level: Advanced
code: A7
title: "Advocacy that holds up: making responsible evaluation the default"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Advocacy that holds up: making responsible evaluation the default

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A7**


> **Framework text (verbatim):** "Advocate for responsible and ethical development and use of generative AI technologies."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 13 of 13

**One-line version:** Advocacy inside an organisation is not a moral argument won; it is a default changed — and defaults change when the evidence arrives in the language of the person who signs.

## What it is

This ability is about moving an organisation — a team, a vendor relationship, a procurement process, a policy — toward responsible evaluation using evidence and argument rather than exhortation. In practice: framing the case in terms the audience already cares about, building artefacts others can use without you, escalating when a line is about to be crossed, and being willing to be corrected in public when the evidence turns.

## Deep expansion

### The concept

The naive model of advocacy is: state the harm, appeal to ethics, wait for agreement. It fails predictably, because the person you are persuading has different incentives, a different time horizon and a different set of risks on their desk. The advanced skill is **translation into the audience's own risk language**, and it usually does not sound like ethics at all.

Four audiences, four arguments, one body of evidence. **To the CFO:** cost of a bad release, rework, contractual exposure, and the price of the evaluation itself — with ranges and with what is not counted. **To the engineering lead:** a faster feedback loop, fewer escalations from the business, a harness that answers questions they already have. **To legal and compliance:** documented controls, an audit trail, the ability to answer a regulator in a week instead of a month. **To the business owner:** the risk that a bad customer-facing output becomes their Friday-night problem, and the specific slice where it fails.

Ethics is the reason *you* care. It is rarely the reason the room moves. That is not cynicism; it is how institutions work, and pretending otherwise is why so many well-argued memos go unread.

### The sub-concepts

**Evidence over assertion.** One well-built counterfactual pair, or one disaggregated result showing a group served worse, changes more minds than a principles document. Bring the artefact.

**Framing to incentive.** Same finding, different opening sentence per audience. A service-quality gap is a fairness problem to one reader and a churn risk to another; both are true.

**Policy versus practice.** Writing a responsible-AI policy is easy and changes little. Changing a release checklist, a procurement clause or a default setting changes behaviour. Aim at the artefact, not the statement.

**The minimum viable control.** Ask for the smallest thing that will actually be done: a calibration sample, a stop rule, one review gate. Large asks get deferred; small ones get adopted and grow.

**Proportionate escalation.** Know the difference between a concern to log, a risk to raise, and a line to refuse. Refusing without a documented trail is theatre; complying without a record is complicity. Map the route before you need it.

**Public commitment and correction.** Publishing what you found, including what you got wrong, is the cheapest way to build the credibility that makes the next argument land.

**Standards and community participation.** Contributing to a framework, an assurance toolkit or an open evaluation set extends influence well beyond your own organisation.

### How it connects to the rest of the framework

`05.03.A.K5` and `05.03.A.K6` supply the obligations and lenses that justify the ask; `05.03.A.A6` supplies the societal-impact evidence that makes it persuasive. `05.03.A.A3` is where advocacy usually lands — the charter, the kill criteria, the review gate. Upstream, `TSC8` holds the organisational practice this ability strengthens, and `TSC9` often provides the easiest entry point, because security concerns get budget faster than ethical ones.

### What is current as of November 2026

Procurement has become the most effective lever. Buyers now ask vendors for evaluation evidence — judge identity, rubric, disaggregated results — and a vendor that cannot produce them loses deals, which has done more for evaluation practice in two years than a decade of principles documents. Inside organisations the same shift is visible: evaluation is moving from research courtesy to release gate, and the advocates who succeed made that gate cheap to pass. The failure mode of the period is ethics theatre — a principles statement, a responsible-AI committee, and no change to any checklist.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Advocacy is compliance."* Compliance answers "may we". Advocacy asks "should we, and can we show it". The second is a design activity.
- *"One strong memo changes minds."* Memos are read once. Gates, defaults and checklists are encountered weekly.
- *"Being right is enough."* Being right and unread is indistinguishable, from the organisation's point of view, from being wrong.

## How a student should understand it

**Mental model:** the safety officer at a construction site. Nobody is persuaded by a talk on the value of life; they are persuaded by a checklist at the gate, a harness easier to wear than to leave off, and a stop-work authority everyone has seen used once.

**Three things they can do after this bullet:**
1. Rewrite one finding for two audiences without changing the evidence.
2. Name the artefact — checklist, clause, default — that would change behaviour, and propose the smallest version.
3. Map the escalation route for a concern before it becomes urgent.

**Misconceptions to kill:** that ethics arguments win on merit, that policy equals practice, and that a single document is a strategy.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The displayed food-hygiene grade.** The stall did not get cleaner because of a lecture on hygiene. It got cleaner because the grade is displayed, customers look, and the inspection is routine. Visible, repeated, cheap to pass — that is the whole design.

**The platform screen doors.** Nobody argues about platform safety now. A physical control was installed and behaviour changed without persuasion. The best responsible-AI controls feel like screen doors: they make the unsafe action slightly harder than the safe one. It breaks because screen doors cost millions and never get uninstalled, while a review gate can quietly rot.

### Worked example with a real tool

A learner must persuade a management committee to fund a quarterly evaluation cycle. Stress-test the argument first. Paste this into Claude:

```
I need to argue for a standing quarterly evaluation of our customer-facing assistant,
to a committee with a CFO, a COO and a head of risk. Ten minutes.

My evidence: three slices where pass rate is materially lower (non-English queries,
queries with attachments, queries about fees); one incident last quarter where an
incorrect fee answer reached 40 customers; cost estimate 6 person-days per quarter
plus API spend.

Give me: (1) the strongest 120-word version in the CFO's language; (2) the strongest
120-word version in the risk lead's language; (3) three objections each will raise and
a one-line answer to each that does not overclaim; (4) the smallest control I could ask
for if the full ask is refused, that would still change behaviour; (5) the one slide we
should show, described in a sentence.

Do not include any statistic I did not give you.
```

What to point at afterwards: point 4. Advocates ask for the whole programme, get deferred, and conclude the organisation does not care. The professional move is the minimum viable control that survives a budget cut — and it is usually what grows into the programme a year later. Point 3 is the discipline check: if an answer to an objection needs a number you invented, the case is not ready.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read the same finding written for an engineer and for a CFO, and ask which one gets funded.
2. **State the objective** — each learner has a 120-word case for one audience and a minimum viable control.
3. **Recall prior learning** — the frameworks and impact methods; ask who must be convinced for either to matter.
4. **Present the content** — four audiences, policy versus practice, minimum viable control, escalation, public correction.
5. **Guide** — build the committee case together, cutting every adjective.
6. **Elicit performance** — pairs write the case for their own organisation and the smallest ask.
7. **Give feedback** — peers play the sceptical CFO; any claim without evidence is struck out.
8. **Transfer** — each learner names the one artefact they will try to change in the next month.

## What the framework doesn't mention but trainers need to know

- **Credibility is spent and slow to earn.** One overclaimed result costs a year of influence. Say "we do not know" early and often.
- **Allies are usually already inside.** The risk lead, the contact-centre manager and the engineer quietly fixing bad outputs are your coalition; find them before you need them.
- **Timing beats eloquence.** An incident is when a control becomes affordable. Have the proposal written before the incident.
- **Document the refusal.** If a risk is accepted, get the acceptance in writing with a name and a date. That record protects the organisation, not just you.

## Watch out

- **Do not moralise at a management committee.** They have heard it; they need a decision they can defend.
- **Do not overclaim an evaluation result to win the argument.** It will be audited, and the loss is permanent.
- **Do not propose a control you cannot operate.** An unmaintained gate is worse than none, because it certifies what it does not check.
- **Do not treat escalation as a last resort you never reach.** Map it early, use it proportionately, keep the trail.
- **The stale claim to retire:** "responsible AI is a culture problem." Culture is what the checklist, the gate and the visible grade produce. Change the artefacts and the culture follows.
