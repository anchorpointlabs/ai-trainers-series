---
id: 05.03.A.A3
tsc: 5
level: Advanced
code: A3
title: "Leading an evaluation programme: from the question to the shipped decision"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Leading an evaluation programme: from the question to the shipped decision

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A3**


> **Framework text (verbatim):** "Lead generative AI evaluation projects from conception to implementation."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 9 of 13

**One-line version:** Evaluation is a product with users, a deadline and a decision attached — run it like one, or it becomes a report nobody reads.

## What it is

Leading an evaluation project means owning it end to end: framing the question the business needs answered, resourcing the work, sequencing it so evidence arrives before the decision it informs, keeping technical and non-technical stakeholders aligned, and delivering something that changes what happens next. The methods live in the other bullets; this one is about the project that contains them.

## Deep expansion

### The concept

Evaluation projects fail in three predictable ways, none of them statistical. **They answer the wrong question**: the team is asked "is this model good?" and produces a benchmark table, when the live decision was "is the cheaper model good enough that users will not notice on the cases that matter". Framing is the highest-leverage hour in the project. **They deliver after the decision**: a two-month evaluation of a migration that ships in three weeks is an obituary — the first evidence must land before the first irreversible commitment, even if thin and labelled as thin. **They deliver evidence without a recommendation**: a 40-page report with seven caveats leaves the choice to whoever is loudest.

### The sub-concepts

**The evaluation charter.** One page: the decision, its owner and date, the questions, the artefacts, what is out of scope, and the kill criteria — the result that would stop the project rather than refine it. It is what protects the team when a stakeholder asks for a tenth model to be included.

**Stakeholder map.** Engineering builds the harness, product owns the outcome, risk and compliance approve the data and the claims, procurement uses the evidence, affected users or their representatives need an answer. Each wants a different artefact on a different cadence. Naming them at the start prevents risk reviewing the report the week it is due.

**Theory of change.** If the evaluation finds X, then Y will happen. Writing it out exposes evaluations that cannot influence anything: if no decision is contingent on the result, it is research and should be scoped as research.

**Sequencing under uncertainty.** Cheap and coarse first — a judged sample of 200 items in week one — then expensive and precise only where the cheap pass left a real question.

**The evidence ladder.** Offline judged evaluation, then blinded human comparison, then a live test. Each rung costs more and answers less. State the rung your conclusion stands on.

**Handover and operations.** A runbook, pinned versions, a named owner and a refresh date. An evaluation only its author can run is a liability.

### How it connects to the rest of the framework

`05.03.A.A1` supplies the study, `05.03.A.A2` the framework, `05.03.A.K4` the methods the programme standardises. `05.03.A.A5` is often the programme's content. `TSC6` supplies deployment, because the evaluation exists to inform a shipping decision, and `TSC8` supplies the governance the charter must respect.

### What is current as of November 2026

Evaluation moved from research activity to operational function, which changed the leadership job. Programmes now run on a weekly cadence with a standing judged evaluation over production traffic, plus quarterly deeper studies. Model choice has become continuous — a new release from a major vendor every few weeks — so the programme's real product is not a report but a *repeatable comparison* that can be re-run in days. The failure mode of the period is the programme built around one big study, obsolete before it is printed.

### Common misconceptions

- *"Leading means project management."* Tracking tasks is the smallest part. Framing the question and protecting the team from scope drift is the job.
- *"The report is the deliverable."* The decision is the deliverable. The report is evidence.
- *"More models in the comparison makes it thorough."* Every added model doubles the analysis and halves the clarity. Compare the two or three that could plausibly ship.

## How a student should understand it

**Mental model:** a hawker stall changing its menu. You do not survey every customer for six months; you put the dish on for a week, watch what comes back on the trays, and decide before the rental review.

**Three things they can do after this bullet:**
1. Write a one-page charter with a named decision owner, a date, and kill criteria.
2. Sequence an evaluation so the first evidence lands before the first irreversible commitment.
3. Deliver a recommendation with its uncertainty and the rung of evidence it stands on.

**Misconceptions to kill:** that thoroughness is the goal, that the report is the product, and that a caveat-heavy report is cautious rather than evasive.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The renovation before the lease ends.** Eight weeks, fixed budget. The temptation is to specify everything perfectly; the professional move is to settle first what cannot be undone — the layout, not the tiles. Irreversible decisions get evidence first.

**The school's PSLE plan.** A principal does not test every child on every topic in week one. There is a diagnostic, targeted work, a mock, then the real thing — and everybody knows the mock is not the exam. That is what an honest evidence ladder sounds like.

### Worked example with a real tool

A team must evaluate three vendors in six weeks with a fixed decision date. Draft and stress-test the charter. Paste this into Claude:

```
Draft a one-page evaluation charter. Facts: decision is choosing one vendor for a
customer-service assistant, contract signed in 6 weeks. Decision owner: COO.
Three vendors, two frontier APIs, one on-premise. Real customer data cannot leave our
network for two of the three. Budget ~15 person-days plus API spend.

Include: the questions we can and cannot answer in 6 weeks; the evidence rung each
sits on; what we will do if we cannot test with real data; kill criteria (a result
that would stop procurement, not refine it); and the one-page format for the COO.

Then tell me the three ways this charter is likely to fail in practice.
```

What to point at afterwards: the "cannot answer in 6 weeks" list. Learners want a charter that promises everything; the professional version says what will remain unknown and what the team will do about it. Then the kill criteria — if nobody can name a result that would stop the procurement, this is a justification, not an evaluation.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — tell the story of an evaluation delivered two weeks after the contract was signed, and ask what went wrong first.
2. **State the objective** — each team has a charter a peer has attacked and that survived one revision.
3. **Recall prior learning** — the evidence ladder; ask which decision their last evaluation informed.
4. **Present the content** — charter, stakeholders, theory of change, sequencing, handover.
5. **Guide** — draft the six-week charter on the projector, arguing about the irreversible decision.
6. **Elicit performance** — teams write their own charter in twenty minutes.
7. **Give feedback** — swap charters; the reviewer looks for the missing decision owner and the absent kill criterion.
8. **Transfer** — each learner names the decision their next evaluation serves and the date it must land by.

## What the framework doesn't mention but trainers need to know

- **The decision date drives everything.** Work backwards from it; every methodology choice follows from how much time the decision allows.
- **Kill criteria are the most useful sentence in the charter.** They distinguish evaluation from advocacy, and they are what a sceptical sponsor respects.
- **Risk and legal are on the critical path.** Bring them the data plan in week one, not the approval queue in week six.
- **The programme needs a home.** A recurring owner, a recurring slot in a meeting, a number leadership sees. Otherwise it survives one cycle.

## Watch out

- **Do not accept "is the model good" as the brief.** Convert it into a decision, an outcome and a comparison.
- **Do not let scope grow to every model on the market.** Breadth is the commonest way an evaluation dies.
- **Do not deliver a report with no recommendation.** Hedging is not neutrality; it hands the decision to the most confident person in the room.
- **Do not skip the handover.** A programme that leaves with its author is not an implementation.
- **The stale claim to retire:** "we will do a thorough evaluation before we commit." In a market that ships a new model every few weeks, thorough means late. Sequence; do not postpone.
