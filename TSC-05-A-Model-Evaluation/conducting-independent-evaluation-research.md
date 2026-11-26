---
id: 05.03.A.A4
tsc: 5
level: Advanced
code: A4
title: "Doing research that counts: from a hunch to a claim others can check"
---

# Doing research that counts: from a hunch to a claim others can check

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A4**


> **Framework text (verbatim):** "Conduct independent research and contribute to the advancement of generative AI evaluation."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 10 of 13

**One-line version:** A contribution is not a novel finding; it is a finding someone else can reproduce without you in the room.

## What it is

This ability is about producing evaluation knowledge rather than applying it: framing a researchable question, grounding it in what is known, running a protocol that isolates the effect claimed, reporting inconvenient results, and publishing enough artefact that an independent party could re-run it. At Advanced level, independent research usually means a small, well-designed study on a real system, not a paper with forty authors.

## Deep expansion

### The concept

The gap between a practitioner and a researcher is not intelligence or resources. It is **discipline about claims**.

A practitioner says "the new prompt seems better on our tickets". A researcher says: "on 300 held-out tickets, rubric-scored blind by two raters, the new prompt raised the pass rate by a margin that survives a paired test, and the effect disappears on tickets with attachments, which we did not expect." The second sentence is longer because it has been built to be attacked.

Four properties make a claim research-grade. **Specified**: population, task, version of everything, scoring method. **Controlled**: the comparison isolates the thing claimed — if two things changed, the result is about the pair. **Replicated**: over items and seeds, not one lucky sample. **Revealed**: negative results, failed conditions and excluded items are in the report. None of this needs a university. All of it needs refusing to round up.

### The sub-concepts

**The researchable question.** "Does a rubric-first prompt reduce verbosity bias in an LLM judge, on our 200 support replies" is researchable. "How do we make evaluation better" is not. The test: a negative answer must be informative. If every outcome supports your position, you have a thesis.

**Grounding before building.** Search prior work on the specific effect, including vendor documentation and blog posts. Most "novel" findings reproduce something already known; knowing that saves months and sharpens the question.

**Construct validity.** You measure a proxy. Name the construct, name the proxy, state the gap. A judge score proxies quality; inter-rater agreement proxies rubric clarity.

**Ablation.** Change one component at a time — rubric, examples, judge model, order, temperature. Without it you know a bundle worked, which is not a finding about any part.

**Pre-registration, lightly.** Write the prediction, sample and analysis before running. An hour's work, and the difference between a result and a rationalisation.

**Honest statistics.** Effect sizes with intervals, not just p-values; correction for the comparisons you actually made; the unit of analysis stated, and clustering accounted for.

**Artefacts.** Prompts, item sets (or a synthesised equivalent), scripts, judge versions, raw scores. Gold standard is a stranger re-running it; realistic standard is a stranger seeing exactly what you did.

### How it connects to the rest of the framework

`05.03.A.K3` and `05.03.A.K4` define the frontier and methods this work contributes to. `05.03.A.A5` is the translation of exactly these results into practice — research produces method, method produces evidence, evidence produces the next question. `05.02.I.K6` is the statistical base, `05.03.A.K5` governs the ethics of using real data, and `05.03.A.A6` is the neighbouring research ability applied to societal impact.

### What is current as of November 2026

Independent evaluation research is more feasible than ever: API access to frontier models is cheap relative to a decade ago, open harnesses exist, and vendors publish rubrics and judge disclosures that give an outsider something to test. The countervailing pressure is contamination — once a finding is published it can enter a training set, so research increasingly publishes *procedures* and held-out sets rather than fixed items. The most-cited work of the period is less about a new metric than about showing an existing metric measured the wrong thing.

### Common misconceptions

- *"Research needs a lab and a grant."* It needs a question, a protocol, and the discipline to report what happened.
- *"More benchmarks means more research."* Running a published benchmark is evaluation. Building a validated instrument is research.
- *"If the effect is large it does not need statistics."* Large effects with a clustered sample and a biased judge are how most retractions start.

## How a student should understand it

**Mental model:** a hawker applying for a food-hygiene award. Not "my food is good" but "here is what I did, here is the record, come and check the kitchen yourself".

**Three things they can do after this bullet:**
1. Turn a hunch into a question with a falsifiable prediction and a stated sample.
2. Design an ablation that separates the components of a bundle.
3. Write up a result so someone else could disagree with it on the evidence.

**Misconceptions to kill:** that novelty is the contribution, that a single run is a finding, and that inconvenient results can be left out.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tuition centre's claim.** "Our students improve by two grades." Compared to whom, measured how, over what period, and were the ones who left counted? Every question that embarrasses the tuition centre is a question an evaluation must answer about itself.

**The hawker's award inspection.** The inspector does not taste the food and declare it good. They check the fridge temperature log, the supplier receipts and the handwashing. Research is the log, not the compliment.

### Worked example with a real tool

A learner suspects the judge is biased toward long answers. Turn it into a study. Paste this into Claude:

```
I want to test whether an LLM judge is biased toward longer answers, in one day, on
120 support replies, with one judge model and two hours of human rating.

Design it: (1) the hypothesis as a falsifiable prediction with a direction; (2) the
treatment — how to lengthen an answer without adding information, specified precisely
enough that another person would make identical edits; (3) the control; (4) how to
score both sets blind and what statistic to use; (5) the confound this design does NOT
control for, and how to report it; (6) a results template with blanks, including a
blank for the null outcome.
```

What to point at afterwards: the padding rule. Nearly every failed study of this kind changes length *and* content, then attributes the effect to length. Then the results template: writing the null branch before running is the cheapest protection against motivated reading.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — present a vendor blog claim and ask what would have to be true for it to be false.
2. **State the objective** — each learner has a design with a falsifiable prediction and an ablation.
3. **Recall prior learning** — counterfactual design; research is the same discipline with a publication obligation.
4. **Present the content** — specified, controlled, replicated, revealed; ablation; pre-registration; artefacts.
5. **Guide** — design the verbosity study together, arguing about the padding rule.
6. **Elicit performance** — individuals write a one-page design for their own question.
7. **Give feedback** — peers attack it; the standard is "would a negative result be believable from this protocol".
8. **Transfer** — each learner commits to one small study and one artefact they will publish internally.

## What the framework doesn't mention but trainers need to know

- **Most internal research dies at data access.** Agree the dataset and build the join key before designing the analysis.
- **Ethics review is not only for universities.** Using customer data in a study you intend to publish needs sign-off, often a data-sharing agreement.
- **Contamination constrains publication.** Publish procedures and held-out sets; be careful about releasing items that will become training data.
- **A single-author study is credible if the artefacts are.** Reviewability substitutes for institutional weight.

## Watch out

- **Do not claim causation from a comparison that changed several things.** Say "the bundle", not "the rubric".
- **Do not report a p-value without the effect size and the unit of analysis.**
- **Do not hide the conditions where the effect vanished.** Those rows are the most interesting and the first a reviewer asks about.
- **Do not publish an eval set you still rely on.** Once released it is contaminated for your own use.
- **The stale claim to retire:** "we cannot do research, we are a practitioner team." The binding constraint is protocol discipline, and that is learnable in a day.
