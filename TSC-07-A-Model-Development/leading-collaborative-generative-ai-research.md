---
id: 07.03.A.A8
tsc: 7
level: Advanced
code: A8
title: Leading collaborative R&D: the operating system for multi-party research
---

# Leading collaborative R&D: the operating system for multi-party research

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A8**


> **Framework text (verbatim):** "Lead collaborative research and development of generative models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 19 of 20

**One-line version:** Multi-party research fails on coordination long before it fails on science — so the leader's job is a charter, a shared evaluation harness and a plan for the day the partnership ends.

## What it is

Leading collaborative R&D means running a programme where several organisations contribute to one research goal: a company with domain data, a university with method expertise, a national compute provider, a public agency as a first customer. The technical work is the same as independent research; what changes is that data, credit, IP, timelines and incentives are all negotiated, and every one of them can stop the project.

## Deep expansion

### The concept

Four things determine whether a consortium produces anything:

**A shared, falsifiable problem.** "Improve generative models for clinical text" is unmanageable. "Reduce clinician correction rate on discharge summaries by X against a frozen baseline, evaluated by a common harness" is workable. The problem statement is the governance document.

**A common evaluation harness.** Disagreement about metrics is the standard way collaborations die. Build one harness, run it in every partner's environment, and treat divergence as a finding. This is also what makes results comparable across sites.

**Explicit data terms.** What may be accessed, by whom, on which hardware, for how long, and what survives the project. Data often cannot move — federated or enclave arrangements are the norm — and pretending otherwise stalls the work for months.

**IP and publication terms written before the first experiment.** Who owns jointly developed methods, who may publish, what review window industry partners get, and how background IP is distinguished from foreground IP. Collaborations that defer this discover it at the most expensive moment.

### The sub-concepts

**Incentive mismatch.** Academia rewards novelty and publication; industry rewards deployment and advantage; public agencies reward service reliability. A programme that does not give each partner a deliverable it values will leak effort.

**Federated and enclave research.** Training or evaluating across sites without centralising data. Adds security review, slows iteration, and is often unavoidable with health or citizen data.

**Credit and authorship.** Contribution models, authorship order, and acknowledgement of engineering work that does not appear in a paper. Resentment about credit is the most common cause of quiet withdrawal.

**Compute as a shared resource.** Allocations, queues and cost attribution. Making compute visible prevents both starvation and free-riding.

**Exit and sustainability.** What happens when the grant ends: who maintains the harness, who owns the model, whether it is released openly. Designing the exit at the start is what turns a project into infrastructure.

### How it connects to the rest of the framework

`TSC7-Advanced-A7` is the individual craft this scales; `TSC7-Advanced-A9` is the deployment that justifies the partnership. `TSC8-Advanced-A2` covers the governance structures, and `TSC9-Advanced-K5` covers the cross-border data questions that appear as soon as partners sit in different jurisdictions.

### What is current as of November 2026

Collaboration has shifted toward shared evaluation and shared data rather than shared model training: training a frontier model jointly is beyond most consortia, whereas building a domain benchmark, a data card and a reproducible harness is achievable and genuinely useful. Open-weight releases have made it possible for a university partner to fine-tune and evaluate a model locally, which changes the shape of partnerships — the lab contributes method and evaluation, the industry partner contributes data and deployment. Expect due diligence on a partner's evaluation practices as much as on its data.

### Common misconceptions

- *"A memorandum of understanding is a plan."* It is an intention. The plan is the harness, the data schedule and the decision rights.
- *"Everyone wants the same outcome."* They want different deliverables from the same project; name them.
- *"Open publication is a detail."* It is usually the term that decides whether industry participates at all.
- *"More partners means more capacity."* Past a point it means more meetings and slower decisions.

## How a student should understand it

**Mental model:** a gotong-royong where everyone brings a dish, and someone has to decide the menu, the kitchen schedule and who washes up.

**Three things they can do after this bullet:**
1. Write a problem statement precise enough to be a contract.
2. Draft data terms and a publication-review clause before the first experiment.
3. Stand up one evaluation harness that every partner runs.

**Misconceptions to kill:** that collaboration is a personality skill, that IP terms can wait, and that all partners want the same thing.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The community clean-up.** Everyone agrees it is a good idea; the difference between a clean estate and a photographed one is a rota, a supply of brooms and someone accountable for the skip. Where it breaks: volunteers can leave, whereas partners have contracts.

**The hawker centre's shared chiller.** Shared infrastructure works when somebody owns the cleaning schedule and the temperature log.

### Worked example with a real tool

Draft the charter, not the model:

```
Partnership: a hospital group, a university lab, and a national
compute centre, to improve discharge-summary drafting.

1. Write the problem statement so it can be evaluated by a third
   party who was not in the room.
2. Draft the data terms in five bullets: access, location, who
   sees what, retention, deletion.
3. Propose the IP split: background, foreground, and the eval
   harness itself.
4. Publication: review window, what may be withheld, and who
   decides.
5. The exit: who maintains what after 24 months.
```

What to point at afterwards: question 1 is where learners write a mission statement instead of a measurable claim. Question 5 is the one nobody prepares and everybody needs. The harness in question 3 is the detail that experienced people notice — whoever owns it controls the definition of success.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a partnership that produced two papers and no deployable system.
2. **State the objective** — produce a five-part charter a lawyer could review.
3. **Recall prior learning** — the experimental design from `TSC7-Advanced-A7`.
4. **Present the content** — problem statement, harness, data terms, IP, incentives, exit.
5. **Guide** — draft the hospital charter together.
6. **Elicit performance** — teams write a charter for a real or plausible partnership.
7. **Give feedback** — swap and negotiate; the friction is the lesson.
8. **Transfer** — each learner identifies one partner they would approach and the first artefact they would share.

## What the framework doesn't mention but trainers need to know

- **The evaluation harness is the political artefact.** Own it or be measured by someone else's definition.
- **Data rarely moves.** Design for enclaves and federated evaluation from day one.
- **Meetings scale worse than code.** A shared repository beats a monthly sync.
- **Plan the sustainability question early.** A harness nobody funds dies with the grant.

## Watch out

- **Do not present collaboration as purely technical.** The failure modes are contractual and interpersonal.
- **Do not skip the incentive discussion.** Unnamed incentives become unnamed resentment.
- **Do not let a partner's metric become the project's metric by default.** Agree it in writing.
- **The stale claim to retire:** "consortiums must train models together." In 2026 shared evaluation and shared data are where the value is.
