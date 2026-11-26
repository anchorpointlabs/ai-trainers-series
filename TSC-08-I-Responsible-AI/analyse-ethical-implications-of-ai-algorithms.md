---
id: 08.02.I.A5
tsc: 8
level: Intermediate
code: A5
title: Analyse ethical implications of AI algorithms
as_at: 2026-11-26
review_by: 2027-02-25
---

# Analyse ethical implications of AI algorithms

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A5**

> **Framework text (verbatim):** "Analyse the ethical implications of AI algorithms (e.g., assess bias and fairness concerns)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 10 of 14

**One-line version:** Analysis is not an opinion about whether AI is good — it is a chain from mechanism to affected party to harm to evidence, with a named group at every link.

## What it is

Analysing ethical implications means producing a structured assessment of a specific system: what decision it makes, who is affected, through what mechanism it can go wrong, what kind of harm follows, how severe and reversible that harm is, and what evidence would confirm or refute the concern. "Who is treated unfairly" must name a group, not "users".

## Deep expansion

### The concept

An analysis has a shape, and the shape is what distinguishes it from a conversation. Seven components, in order:

1. **System boundary** — the model, its data, the retrieval corpus, the workflow, and the humans in it. Most analyses miss the workflow and therefore miss the incentive that produced the harm.
2. **The decision** — what actually changes for the person: approved, shortlisted, flagged, prioritised, ignored.
3. **Affected parties** — applicants, staff, third parties, future users who are not in the room.
4. **Mechanism** — the causal path: sampling, labels, proxies, prompt, retrieval, ranking objective.
5. **Harm** — allocative, representational, privacy, safety, autonomy, dignity.
6. **Severity, reversibility, scale** — a denied loan is reversible in principle and rarely in practice; a leaked record is never reversible.
7. **Evidence** — what you would measure, and what result would change your mind.

The last one is the test of whether an analysis is real. If no observation could refute the claim, the claim is not analysis, it is a position.

### The sub-concepts

**Fairness metrics are not interchangeable.** Demographic parity asks for equal approval rates regardless of qualification. Equal opportunity asks for equal approval rates among people who genuinely qualify. Predictive parity asks that a score of 0.8 mean the same thing in every group. Disparate impact compares selection rates against the four-fifths rule. They cannot all hold at once — pick one, say why, and record it.

**Counterfactual reasoning is the client-facing version.** "Would the decision change if only the name changed?" is a question a business owner understands immediately, and it tests for the proxy pathway more directly than any aggregate metric.

**Aggregate metrics hide the tail.** Report by slice, at the intersection of two attributes where the data allows it, and state the sample size so the room can see when a slice is too small to conclude from.

**The workflow is part of the algorithm.** A model that is 95% accurate, reviewed by an officer with 20 seconds per case, produces outcomes that are mostly the officer's behaviour. Analyse the socio-technical system, not just the model.

**Analysis of generative systems needs three extra questions.** What is in the retrieval corpus and who vetted it? What can the agent do, with whose permissions? What happens to the user's input after the session ends?

### How it connects to the rest of the framework

`TSC8-Intermediate-K3` supplies the mechanisms and the societal consequence; `TSC8-Intermediate-A6` is the group-and-culture lens on the same analysis; `TSC8-Intermediate-A3` is what you do once the mechanism is identified. `TSC8-Intermediate-K1` frames the four considerations the analysis covers, and `TSC8-Intermediate-A7` is where you check whether the framework you are analysing against actually demands this depth.

### What is current as of November 2026

The analytical surface has widened. Provider evaluations for the current generation are useful baselines but are not an analysis of your system, because they cannot see your corpus, your prompt or your workflow. Regulators increasingly expect a documented assessment rather than a stated conclusion, and ISO/IEC 42001 formalises it as an AI system impact assessment with a risk treatment plan.

Agentic systems add a component most templates lack: an action analysis. What can the system change in the world, under what permissions, with what approval, and what is the blast radius of a wrong action. A text-only analysis template will not surface that, and the omission is now the more dangerous one.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Analysis means running a bias metric."* A metric is one input. Without the mechanism and the affected group, it explains nothing.
- *"We did not intend harm, so there is none."* Intent is not in the causal chain.
- *"It is a black box, so nothing can be said."* You can analyse the data, the objective, the workflow, the incentives and the outcomes without opening the weights.
- *"One analysis covers the system."* Each materially different use, population or deployment context needs its own.

## How a student should understand it

**Mental model:** a structural survey before renovation. Not a mood about the building — a list of load-bearing walls, with measurements and a named engineer.

**Things they can do after this bullet:**
1. Write the seven components for a system in under a page.
2. Name the fairness metric they are using and the one they are giving up.
3. State the observation that would change their conclusion.

**Misconceptions to kill:** that a metric is an analysis, that good intent removes harm, and that opacity of the model means opacity of the consequences.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The HSA clinical trial protocol.** Questions are specified before the data arrives, the endpoint is defined in advance, and there is a stopping rule. An analysis written after seeing the results is a press release. Where it breaks: trials have one endpoint; an AI system has several affected parties with incompatible interests.

**The MRT flood-risk assessment.** It does not ask "will it flood", it asks where the water goes, which entrances are lowest, who gets stranded and what the response time is. Depth of mechanism, not a verdict.

### Worked example with a real tool

```text
A resume screener was trained on five years of hires and now ranks CVs. Recruiters see the
top 30 per role. An internal review found it favours CVs mentioning competitive sport and
"captain" roles.

Analyse it. For each of the seven components — boundary, decision, affected parties,
mechanism, harm, severity/reversibility/scale, evidence — write two sentences.
Then name the fairness metric you would report, the one you are deliberately not using,
and why. Finish with the one observation that would falsify your mechanism claim.
```

What to point at afterwards: the model will identify gender as the affected dimension and stop there. Push for the intersection — career gaps, caregiving, older applicants, polytechnic versus university pathways — and for the mechanism chain from "captain" to the historical hiring pattern. The falsification question is usually the one it answers worst, which is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out two CV summaries that differ only in hobby language and ask who gets shortlisted.
2. **State the objective** — by the end you can produce the seven-component analysis for a system you know.
3. **Recall prior learning** — revisit the proxy discussion and the postal code example.
4. **Present the content** — the seven components, the fairness metric menu, the falsification test.
5. **Guide** — work the screener example on the board.
6. **Elicit performance** — groups analyse a system from their own sector.
7. **Give feedback** — mark every affected party that was named vaguely, and every metric with no trade-off stated.
8. **Transfer** — each learner applies the template to a live project this month.

## What the framework doesn't mention but trainers need to know

- **The humans in the workflow are where bias often re-enters.** A fair model plus a quota-driven reviewer is an unfair system.
- **Document dissent.** If a team member flagged a concern and was overruled, that note is the most valuable line in the file later.
- **The affected-party voice is missing by default.** An analysis written entirely by the deploying organisation will systematically underestimate harm to people it never speaks to.
- **An analysis is a living document.** Model versions, corpora and populations change; a two-year-old assessment describes a system that no longer exists.

## Watch out

- **Do not accept a generic answer.** "Some groups may be disadvantaged" is not an analysis; make the learner name the group.
- **Do not let the metric substitute for the mechanism.** The number tells you there is a gap; only the mechanism tells you what to fix.
- **Do not let the analysis become a compliance artefact** completed after the decision was made.
- **The stale claim to retire:** "we cannot audit what we cannot explain." You can audit outcomes, data and workflow without explaining the weights.
