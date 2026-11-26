---
id: 05.03.A.A6
tsc: 5
level: Advanced
code: A6
title: "Measuring what leaks: methodologies for societal impact and ethical harm"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Measuring what leaks: methodologies for societal impact and ethical harm

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A6**


> **Framework text (verbatim):** "Develop innovative methodologies for evaluating the societal impact and ethical implications of generative AI."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 12 of 13

**One-line version:** Harms of this kind are distributed, delayed and counterfactual — so the methodology has to measure populations and absences, not just bad outputs.

## What it is

This ability is about building evaluation methods for effects that never appear as a wrong answer: who is represented and who is not, which groups get a worse service, what a system does to a labour market or a public conversation, and what would have happened without it. The methods combine disaggregated measurement, structured audits, adversarial probing, longitudinal monitoring and qualitative work with affected communities — and they need a different standard of evidence from a rubric score.

## Deep expansion

### The concept

Four properties make societal harm hard to measure, and each demands a different response. It is **distributed** — not in one output but in a rate across a population: who gets shortlisted, who gets a worse translation, whose dialect is treated as error — so the method is disaggregation, with the group definition itself a contested decision. It is **delayed** — effects surface after adoption, when behaviour has changed around the system — so the method is longitudinal monitoring with a baseline and a schedule. It is **counterfactual** — the comparison is a world that did not happen — so the method is the strongest available proxy: a control group, a comparable market, a before-and-after with confounders named. And it is **contested** — stakeholders disagree about whether something is a harm — so the method is structured deliberation with documented positions.

A second distinction does most of the teaching work: **representational** harm (how groups are depicted) versus **allocative** harm (how opportunities and quality of service are distributed). The first is measurable by counting outputs; the second needs outcome data. Most teams measure the first and claim the second.

### The sub-concepts

**Disaggregation.** Every headline metric reported by language, age band, disability status, income proxy, region. The finding is usually in the gap, and the gap is invisible in the average.

**Representational audits by counting.** Generate a batch for a neutral prompt ("a company director", "a person receiving care", "a family in an HDB flat"), code the outputs on attributes, compare to a defensible baseline. Crude, replicable, and far more persuasive than an anecdote.

**Adversarial and edge-case probing.** Seeded red-teaming with patterns drawn from the community in question, not invented ones. The generator gives volume; the seed determines relevance.

**Impact assessment.** A structured document — data protection, human rights, algorithmic — naming affected parties, the mechanism of effect, severity and mitigations. Its value is the forced enumeration.

**Longitudinal and drift monitoring.** A fixed panel run on a schedule, plus tracking of the live input distribution. Harm often appears as drift, not as a bad release.

**Qualitative and participatory work.** Interviews, diary studies, deliberative panels, community review of test items. Not decoration — this is how you learn which slices matter and what counts as harm.

**Counterfactual policy comparison.** Where a comparable jurisdiction, market or cohort exists, use it, and name the confounders.

### How it connects to the rest of the framework

`05.03.A.K6` supplies the lenses this operationalises and `05.03.A.K5` the obligations the assessment must satisfy. `05.03.A.A2` provides the schema and slices disaggregation depends on; `05.03.A.A1` provides the study machinery for the qualitative work; `05.03.A.A7` is what you do with the findings. `TSC8` holds the organisational practice and `TSC9` the security and abuse dimensions that intersect.

### What is current as of November 2026

Agentic systems widened the surface: an assistant that books, files and pays can produce allocative harm directly, not only through text. Evaluation is consequently moving from content audits to **action audits** — what the agent did, on whose behalf, with what authority, and who bore the cost of a wrong action. Assurance expectations have hardened too: buyers ask for disaggregated results and impact assessments, and a vendor reporting only an average is at a disadvantage in procurement. The methodological weak point is unchanged — measuring the effect on people who never touch the product.

### Common misconceptions

- *"Societal impact equals a toxicity score."* Toxicity is one narrow, well-instrumented harm. Representation, service quality and labour effects are larger and less measured.
- *"If the average is fine, the system is fair."* Averages are where disparities hide.
- *"We cannot measure this, so we will note it as a risk."* Much of it is countable. A risk-register entry is often a decision not to look.

## How a student should understand it

**Mental model:** the food-hygiene inspector who checks the whole kitchen, not the plate in front of you, and who writes down the fridge temperature at 3am when nobody is watching.

**Three things they can do after this bullet:**
1. Pick the right method for a named harm: disaggregation, audit by counting, longitudinal panel, impact assessment or participatory study.
2. Report a result by slice with the group definitions made explicit.
3. Write an impact assessment that names affected parties and the mechanism, not just the category.

**Misconceptions to kill:** that harm is an output property, that an average answers a fairness question, and that unmeasurable means unexaminable.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The block's lift breakdown.** "Average wait 40 seconds" is true and useless if most floors wait 15 seconds and the 12th, where the elderly residents live, waits four minutes. The average is not a lie; it answers a different question.

**The hawker centre cleaning contract.** Nobody can see the effect of cutting cleaning from three times a day to two — until a month later, when the tray-return rate drops. The harm is spread across a month and a hundred tables, which is why it needs a panel and a baseline rather than an inspection.

### Worked example with a real tool

An image feature for a recruitment brand needs a representational audit. Paste this into Claude with a batch of generated images described or attached:

```
We generated 60 images for the prompt "a confident professional at work in Singapore".

Build a coding sheet and a defensible audit: (1) define 6 dimensions judgeable from the
image alone — apparent age band, apparent gender presentation, setting, attire
formality, visible assistive devices, apparent ethnicity category; (2) for each,
state the defensible baseline for Singapore and where the data would come from, or say
it does not exist; (3) produce the coding table, one row per image; (4) report the
distribution per dimension and flag any dimension where one category exceeds 60%;
(5) state three things this audit cannot tell us, and the method that would.

Do not infer intent. Report counts only.
```

What to point at afterwards: point 2. The room wants to compare against "the population", and the honest answer is that a defensible baseline is itself a research question. Point 4 gives the crude but persuasive result — one category dominating. Point 5 is the discipline: a representational audit says nothing about whether anyone was harmed.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show an "average wait 40 seconds" dashboard beside a per-floor breakdown.
2. **State the objective** — each group has chosen a method for one named harm and written its baseline problem.
3. **Recall prior learning** — the cultural and socio-political lenses; which harms did they predict?
4. **Present the content** — the four properties, representational versus allocative, the method families and their limits.
5. **Guide** — run the representational audit on the projector and argue about the baseline.
6. **Elicit performance** — groups specify method, slice and baseline for a harm in their own product.
7. **Give feedback** — review for methods that cannot separate the system's effect from the world's.
8. **Transfer** — each learner names one metric they will disaggregate next quarter.

## What the framework doesn't mention but trainers need to know

- **Group definitions are political.** Every slice boundary is a decision with winners; record who chose it.
- **Small slices produce noise that looks like a finding.** Ten items per group is not enough to claim a disparity. Aggregate or collect more.
- **The baseline problem is unsolved and unavoidable.** "Compared to the applicant pool" is a different claim from "compared to the population".
- **Participatory work takes months.** Budget it, or do not claim it.

## Watch out

- **Do not reduce this to a checklist that produces a green tick.** An audit that always passes is measuring the auditor.
- **Do not moralise in place of measuring.** State the count, the baseline and the gap; let the room conclude.
- **Do not use a synthetic population as a stand-in for an affected community.** Synthetic data is for coverage, not for testimony.
- **Do not measure representation and claim allocation.** Different harms, different evidence.
- **The stale claim to retire:** "societal impact is too diffuse to evaluate." Some of it is; much of it is a count by slice, and the count is the entry ticket to the harder conversation.
