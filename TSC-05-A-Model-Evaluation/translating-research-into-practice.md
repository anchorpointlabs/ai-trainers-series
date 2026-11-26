---
id: 05.03.A.A5
tsc: 5
level: Advanced
code: A5
title: "From paper to practice: turning a research method into a Monday routine"
as_at: 2026-11-26
review_by: 2027-02-25
---

# From paper to practice: turning a research method into a Monday routine

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A5**


> **Framework text (verbatim):** "Translate research advancements into practical evaluation methodologies."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 11 of 13

**One-line version:** A method becomes a methodology only when someone else can run it without the author, on a budget, every week.

## What it is

This is the translation layer: taking a published technique — a judge calibration protocol, a counterfactual probe design, a preference-elicitation method — and reducing it to something a normal team can operate repeatedly. It is not summarising the paper. It is deciding what to keep, what to cut, what to automate, what to write down and what to warn about, so the method survives contact with real traffic.

## Deep expansion

### The concept

Papers optimise for demonstrating an effect under controlled conditions. Operating teams optimise for a repeatable signal under a schedule. Almost nothing transfers unchanged, and the failure is always the same: the team reproduces the paper faithfully, finds it costs three days per run, and abandons it in month two.

The discipline is **deliberate degradation with a stated cost**. Cut the method to what the decision requires, and record what the cut costs, so that when someone asks "is this as rigorous as the paper", the answer is a sentence rather than a shrug.

Four questions do most of the work. What is the smallest version that still answers our question? Papers often use five judges, three seeds and 2,000 items; your decision may be served by one judge, one seed and 150 stratified items. What must be automated, and what must stay human? Automate selection, scoring and reporting; keep human rating on a calibration sample, because that is where judgement lives. What breaks at our scale or in our data? A method validated on English news articles may behave differently on Singlish chat logs or scanned invoices. Who owns it in six months? A methodology with no owner decays into an unmaintained script.

### The sub-concepts

**The minimum viable instrument.** Runs in under an hour of analyst time per cycle, produces one number and one diagnosis, and can be trusted because it was calibrated once and rechecked on a schedule.

**Operationalising the construct.** "Helpfulness" must become clauses a rater can apply in thirty seconds. Every translation succeeds or fails here.

**Cost envelope.** Price the run: API calls, human minutes, engineering hours, storage. If it costs more than the decision is worth, it runs once and is quietly dropped.

**Prompt and rubric as versioned artefacts.** The method lives in text files under version control with a changelog. Without it, "we ran the evaluation" is unfalsifiable a month later.

**Failure-mode documentation.** What the instrument gets wrong, which segments it is unreliable on, what to do with an implausible result. This section decides whether a team trusts it.

**The runbook.** One page: when to run, what to feed it, what to look at, what to escalate. If it takes an hour to explain, it will not run.

**Adoption path.** Pilot on one team, publish the first result, then make it a gate in the release checklist. Adoption by mandate is complied with and not used.

### How it connects to the rest of the framework

`05.03.A.A4` produces the research this consumes; the two form the loop the framework implies. `05.03.A.K4` is the method family being translated and `05.03.A.A3` is the programme that houses the result. `05.03.A.A1` confirms on real users, so the translated method must output something the study can use. `05.02.I.A1` is the engineering substrate and `TSC6-I` supplies the deployment hooks that make a weekly run possible.

### What is current as of November 2026

The lag between publication and practice has compressed to months, partly because vendors publish their own evaluation methodology alongside model releases, partly because open harnesses let a new technique be run against your data the week it appears. The scarce skill is no longer knowing the method; it is deciding which of twenty plausible methods earns a permanent slot. Teams that added every technique they read about now run six half-maintained evaluations and trust none.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Translate means summarise."* A summary is a reading aid. A translation is a runbook, a cost and a failure-mode list.
- *"Reproduce the paper exactly to be rigorous."* Exact reproduction is a research activity. Operations needs the smallest defensible version, with the degradation recorded.
- *"If it is published, it is ready."* Most published methods assume a scale, a budget and a data quality a team does not have.

## How a student should understand it

**Mental model:** converting a restaurant recipe into a hawker stall's standard operating card — same dish, scaled to a wok, timed to a lunch queue, with a note on what to do when the gas runs low.

**Three things they can do after this bullet:**
1. Reduce a published method to a version that runs in under an hour of analyst time.
2. Write a runbook and failure-mode note a colleague can operate without you.
3. State what the reduction cost, in one sentence, when a reviewer asks.

**Misconceptions to kill:** that fidelity equals rigour, that documentation is overhead, and that a method is adopted when it is announced.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The recipe versus the stall.** A restaurant recipe serves four, plated, with a garnish nobody eats. A stall needs a version that holds over two hundred covers and can be taught to a new assistant in an afternoon. It breaks because a stall can taste as it goes, and an evaluation cannot taste 500 items.

**The CPF nomination form.** The policy is complex; the form is two pages. Somebody did the translation, and if they had simply published the policy most people would not have nominated anyone. Translation is the difference between a rule existing and a rule working.

### Worked example with a real tool

A team wants to adopt pairwise preference judging, but the paper's protocol takes three days. Reduce it. Paste this into Claude:

```
Here is a pairwise-preference judging protocol from a paper: [paste method section]

Constraints: 1 analyst, ~2 hours/week; ~400 new support replies/week; one judge
model available, a second doubles cost; the decision is whether to switch prompt
versions monthly.

Produce: (1) a reduced protocol that fits 2 hours/week, and exactly what you cut;
(2) for each cut, what can no longer be claimed; (3) the sampling rule — how to pick
60 items from 400 without biasing toward easy cases; (4) a one-page runbook: trigger,
inputs, steps, what to look at, when to escalate; (5) three failure modes, phrased for
a colleague who has never read the paper.

Do not add steps I did not ask for. Prefer fewer, cheaper, documented.
```

What to point at afterwards: point 2. Teams skip the "what can no longer be claimed" column, then overclaim three months later in a slide. Then point 3 — sampling is what everyone improvises and what determines whether the weekly number is comparable across weeks.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a method with a 40-item appendix and ask who in the room could run it next Tuesday.
2. **State the objective** — each learner has a reduced protocol, a runbook and a cost statement for one method.
3. **Recall prior learning** — the calibration and judging material; which parts were load-bearing?
4. **Present the content** — deliberate degradation, minimum viable instrument, cost envelope, versioning, adoption.
5. **Guide** — reduce the pairwise protocol together, arguing about what to cut first.
6. **Elicit performance** — teams translate one method they actually want to use.
7. **Give feedback** — review runbooks: if a colleague cannot execute it without asking a question, it is unfinished.
8. **Transfer** — each learner schedules the first run and names the owner.

## What the framework doesn't mention but trainers need to know

- **The recurring cost is the killer, not the build.** A method needing two analyst-days a month gets dropped in a busy quarter. Design for the worst week.
- **Comparability across runs matters more than absolute accuracy.** A stable, slightly biased weekly number beats an accurate one you cannot repeat.
- **Version everything, including the judge's system prompt.** Most "the number moved" investigations end at an unversioned prompt.
- **Write the failure-mode note before the first run.** Afterwards, everyone remembers the success.

## Watch out

- **Do not present a reduced method as equivalent to the paper.** State the cut and its cost in the same breath.
- **Do not automate the calibration sample.** That is the one place human judgement must stay.
- **Do not translate a method that answers a question nobody is asking.** Check the decision first; a well-run instrument for an irrelevant question spends trust.
- **Do not let the runbook become a document nobody opens.** One page, linked from the release checklist.
- **The stale claim to retire:** "we are waiting for the method to mature before adopting it." Methods mature in the open, and teams that wait are two cycles behind on the questions that matter.
