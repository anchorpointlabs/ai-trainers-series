---
id: 06.03.A.A5
tsc: 6
level: Advanced
code: A5
title: "Advancing the field: how application work becomes research"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Advancing the field: how application work becomes research

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A5**


> **Framework text (verbatim):** "Conduct research and advance the field of generative AI-powered applications."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 10 of 12

**One-line version:** Application research is a controlled comparison, honestly reported and reproducible by a stranger — a demo is not a contribution, and a negative result that saves others a quarter is.

## What it is

This is the ability to produce knowledge about building generative AI applications, not just applications: to run a controlled comparison of two architectures, report it with a baseline and a held-out set, and publish the harness so someone else can repeat it. The contribution can be a pattern, a dataset, an evaluation method, a reference implementation, or a well-evidenced negative result. What makes it research is the method, not the venue.

## Deep expansion

### The concept

Application research is cheap to start and easy to do badly. The failures are consistent: no baseline ("we tried the new retrieval and it felt better"), one variable changed alongside three others, a test set drawn from the same documents used to tune, costs omitted, and a write-up that cannot be repeated because the prompt was edited in a chat window and never saved.

The method is borrowed from any empirical discipline and adapted to a fast-moving artefact:

1. **A question with a falsifiable answer.** "Does a reranker improve answer accuracy on our support corpus, at what latency, for what cost?" — not "is RAG good".
2. **A baseline.** The current production system, measured the same way on the same set.
3. **One variable at a time.** Change the reranker, not the reranker and the chunk size and the model.
4. **A held-out evaluation set**, built before the change and untouched during tuning.
5. **A reproducible artefact** — prompts, versions, scripts, seeds, data snapshot.
6. **An honest report**, including what did not work and what it cost.

In application work the artefact *is* the contribution. A pattern described in prose is an opinion; a pattern shipped as a runnable harness with a result attached is knowledge.

### The sub-concepts

**Choosing a question worth answering.** Good application questions are ones practitioners are currently guessing about: does the reranker help at this corpus size, does chunk overlap matter here, does a guardrail judge agree with human reviewers, does an agent loop beat a single retrieval for multi-hop questions.

**The baseline discipline.** Without a measured baseline, an improvement is a feeling. The baseline is usually the boring existing system, and beating it is harder than it looks.

**Leakage.** If the evaluation questions were written while reading the retrieved passages, or if the corpus contains the answer keys, the result is inflated. Build the set from real user questions before the change.

**Ablation.** Remove one component at a time and report what each contributes. This is where most teams discover that half their pipeline is decoration.

**Cost and latency as results, not footnotes.** A technique that improves accuracy by two points and doubles latency is a different finding from one that improves it for free. Report both.

**Statistical honesty.** Twenty questions cannot distinguish two close variants. Say so, widen the set, or report the result as inconclusive — which is a finding.

**The artefact.** Repository, prompts, versions, scripts, sample data, and a README that lets a stranger reproduce the headline number.

**Ethics and consent.** User data in an evaluation is research data. Anonymise, get permission, or use synthetic cases; say which.

### How it connects to the rest of the framework

`TSC6-Advanced-K3` and `A4` give the techniques and trade-offs being tested. `TSC5` supplies the evaluation machinery — metrics, test sets, human judgement — that this ability applies to application questions. `TSC6-Advanced-A6` produces the automation that makes a reproducible harness cheap to run. `TSC7-Advanced-A7` is the model-development counterpart: same method, different level of the stack.

### What is current as of November 2026

- **Practitioner research has real venues.** Workshops, system tracks and dataset tracks now accept application findings, and engineering blogs with reproducible harnesses carry genuine weight in hiring and procurement.
- **Evaluation harnesses are shared infrastructure.** Open harnesses make a controlled comparison cheaper than ever, and the differentiator is the quality of your test set, not your tooling.
- **The half-life is short.** Findings about specific models expire in months; findings about architecture and evaluation method last years. Frame contributions to survive model churn.
- **Benchmark theatre is recognised and discounted.** Scores on public benchmarks that do not predict task behaviour are increasingly called out, which raises the value of narrow, honest, task-level studies.
- **Industry labs publish**, so the bar for novelty is set by teams with production data — and the credible niche for most organisations is the specific, the negative and the reproducible.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Research needs a lab and a budget."* A controlled comparison on two hundred real questions with saved prompts is research. The lab buys scale, not method.
- *"A demo is a contribution."* A demo shows possibility; research shows effect, with a baseline and a cost.
- *"Negative results are not publishable."* They are the most useful results in a fast-moving field, and the least written.
- *"Our A/B test is research."* Without consent, controls and a stated hypothesis, it is product experimentation — valuable, but a different thing.

## How a student should understand it

**Mental model:** the clinical audit cycle at a polyclinic. Measure current practice, change one thing, re-measure the same way, publish the numbers internally so the next clinic does not repeat the mistake.

**Three things they can do after this bullet:**
1. Turn a practitioner hunch into a falsifiable question with a baseline and one variable.
2. Build a held-out set before tuning, and state its limitations.
3. Produce a reproducible artefact and an honest one-page report, including cost and what failed.

**Misconceptions to kill:** that research requires a lab, that a demo counts as evidence, and that a negative result is a failure.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker recipe.** One stall cooking a great dish advances nobody. Writing the recipe, the heat level and the timing so that a second stall can cook it — that advances the trade. The harness is the recipe card.

**The polyclinic audit.** Every quarter: same measure, one change, re-measure, share. The audit is not exciting, and it is why the clinic improves while the one that "just tries things" does not. Where it breaks: clinical audits run on stable measures for years, while model behaviour shifts, so application research needs its evaluation set refreshed and dated.

### Worked example with a real tool

Ask for a study design, then attack its rigour:

```
I want to test whether adding a reranker improves answer accuracy on our
support corpus, enough to write up as an internal tech report.

Draft: the hypothesis, the baseline, the ablation, the metric, how to
build the test set without leakage, how many questions I need to say
anything meaningful, the cost and latency I must report, and the section
headings of the report.

Then flag anything in your own plan that would make the result
unpublishable or unconvincing.
```

What to point at afterwards: the plan will be competent and the sample-size reasoning will be vague — the honest answer is "more than twenty, and state the uncertainty". Then point at the last instruction: asking the model to critique its own plan is the cheapest rigour check available, and it will usually name leakage and missing baselines if pushed.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read two conflicting blog posts about the same technique, both confident, neither with a baseline.
2. **State the objective** — you will design a reproducible comparison and report it honestly.
3. **Recall prior learning** — they have built evaluations; now the evaluation answers a question nobody has answered.
4. **Present the content** — question, baseline, one variable, held-out set, artefact, honest report.
5. **Guide** — critique a deliberately flawed study together: three variables changed, no baseline.
6. **Elicit performance** — teams draft a one-page study plan on their own corpus.
7. **Give feedback** — identify leakage in each plan, and any claim the sample cannot support.
8. **Transfer** — they run the study next quarter and publish the harness internally.

## What the framework doesn't mention but trainers need to know

- **Publishing internally is enough to count.** A tech report other teams reuse advances the field inside the organisation; most of the value is local.
- **Save the prompts.** The most common irreproducibility is a prompt that existed only in a chat window.
- **Report the cost of the study itself.** Compute and human review hours are part of the finding.
- **Refresh or date the evaluation set.** A stale set silently measures the old problem.
- **Collaboration beats solo novelty.** A shared harness with two organisations tests more than two separate demos.

## Watch out

- **Do not let the room equate "we built it" with "we know it works".** The gap is the entire bullet.
- **Do not encourage publishing a result that cannot be reproduced** to hit a deadline; it damages the team more than silence.
- **Do not use customer data in a write-up** without consent and anonymisation, whatever the internal policy says about "internal only".
- **The stale claim to retire:** "only model labs produce research." In November 2026 the most cited application findings come from teams running real systems, precisely because their data is specific.
