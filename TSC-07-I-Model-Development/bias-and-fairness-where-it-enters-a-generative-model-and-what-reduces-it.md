---
id: 07.02.I.K7
tsc: 7
level: Intermediate
code: K7
title: Bias and fairness: where it enters a generative model and what reduces it
as_at: 2026-11-26
review_by: 2027-02-25
---

# Bias and fairness: where it enters a generative model and what reduces it

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K7**


> **Framework text (verbatim):** "Techniques for mitigating bias and ensuring fairness in generative outputs."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 7 of 17

**One-line version:** A generative model reflects the crowd it learned from — and a crowd is never a representative sample by accident.

## What it is

Bias here means a systematic skew in outputs across groups of people, languages or contexts. Fairness is the standard you choose to judge that skew against. Neither lives in one line of code: bias enters through the pre-training corpus, the annotation process, the training objective and the humans whose preferences shaped the final model. Mitigation therefore has four separate fronts, and only one of them is "fix the dataset".

## Deep expansion

### The concept

A model trained to maximise the likelihood of its corpus reproduces that corpus's centre of gravity, including its omissions. If a corpus describes nurses as women and engineers as men, the model's default completion is not a mistake — it is an accurate summary. Changing it means changing what the model is rewarded for, which is why fairness work is a data, objective and evaluation problem at once. The uncomfortable part for practitioners: fairness definitions conflict. Equal accuracy across groups and equal outcomes across groups are different targets, and choosing one is a policy decision that belongs in the system card, not in the loss function.

### The sub-concepts

**Where it enters.** Representation (whose text, whose images, whose language), labelling (annotators applying their own norms), the objective (majority patterns dominate), the preference step (a small group of raters defines "good"), and deployment (a prompt in Singlish may land in a much weaker part of the distribution than the same prompt in standard English).

**Data-side mitigation.** Balance and reweight; remove duplicated stereotyped text, which acts as an implicit amplifier; add counterfactual variants — the same scenario with swapped names, genders, ethnicities — so the model sees the attribute as irrelevant; and record provenance so you can audit later.

**Model-side mitigation.** Diverse preference data in the alignment step; fine-tuning on balanced exemplars; constrained decoding against blocklists, which is blunt and visible to users; and instruction-level guards. Architectural "debiasing" objectives have weak evidence for large generative models and should not be sold as a fix.

**Evaluation.** Disaggregated metrics by group, stereotype probes (occupation-by-gender, crime-by-ethnicity in completions), dialect robustness tests, red-team corpora, and human reading of the worst failures. One aggregate fairness score hides exactly the subgroup that fails.

### How it connects to the rest of the framework

`TSC7-Intermediate-K4` supplies the metric discipline that disaggregation requires; `TSC7-Intermediate-K6` gives the probing methods; `TSC7-Intermediate-K9` matters because synthetic data can amplify a skew as easily as correct it; `TSC8` is the responsible-AI frame; `TSC5-Intermediate-K5` states the fairness principles being operationalised.

### What is current as of November 2026

- **Providers publish bias evaluations in system cards.** The GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro / Gemini 4 Argon ship with demographic-representation and stereotype evaluations, which gives buyers something to cite — and something to check rather than trust.
- **Image generation improved and did not solve it.** Prompt-to-portrait defaults are more balanced than two years ago, yet occupational and age defaults persist.
- **Multilingual coverage widened while dialect coverage stayed thin.** Singlish, Malay and Tamil inputs still behave measurably differently from standard English, which matters more in Singapore deployments than headline benchmark parity.

### Common misconceptions

- *"Bias is a data problem."* It is also an objective problem and a rater problem; cleaning the corpus does not fix a preference model trained on a narrow group.
- *"Check demographic balance and you're done."* Intersectional, dialect and socio-economic skews survive a two-group check.
- *"Adding 'diverse' to the prompt fixes it."* It changes the surface of one output and nothing about the distribution.
- *"There is one correct definition of fairness."* There are several, they conflict, and the choice must be documented.

## How a student should understand it

**Mental model:** a mirror in a room. It reflects accurately — but only what is actually standing in front of it. Change who is in the room, not the glass, and the reflection changes.

**Three things they can do after this bullet:**
1. Name the four entry points for bias in a system they are building.
2. Write a disaggregated evaluation that would catch a subgroup regression.
3. State which fairness definition they chose and why, in writing.

**Misconceptions to kill:** that data cleaning is sufficient, that "diverse" prompts are mitigation, and that fairness is one number.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The estate survey.** A town council surveys residents about a new facility, but only households that answer the door in English respond. The report is accurate about the people who answered and wrong about the estate. A generative model's "opinion" is that survey, run at internet scale. Where it breaks: a town council can go back and knock on the doors that did not answer; a model cannot re-survey the internet, so the missing households stay missing.

**The class photo.** Ask thirty classes for a photo and the same children end up in front. Nobody instructed it; the photographer asked "who wants to be in front" and the confident ones stepped forward. Preference data works exactly like that — the raters who answer most confidently define the model's manners. Where it breaks: the teacher can see who stepped forward; in preference data nobody records who was never asked, so that bias never appears in the log.

### Worked example with a real tool

A learner is building a resume-screening assistant and wants to know whether it treats equivalent candidates differently. Type this into Claude or a coding assistant:

```
Write a bias probe for a resume-summary model.

1. Take 20 real resumes. Create counterfactual versions by swapping
   only the name and inferred gender/ethnicity signals, keeping
   skills and experience identical (use clearly synthetic names).
2. Generate a summary for each version at temperature 0.
3. Score each summary for: number of leadership words, hedging,
   and any mention of "culture fit"; also compute embedding
   similarity to the original summary.
4. Report mean difference between original and swapped versions
   per attribute, with a paired test.
5. Save the 10 largest divergences for human reading.
```

Point at step 1 (change one attribute only), step 4 (paired comparison, because the same resume is the control), and step 5 — the divergences tell you whether the model is picking up a signal you never intended to give it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — the same prompt with two names, two very different summaries.
2. **State the objective** — design a probe that would catch that in production.
3. **Recall prior learning** — metrics and slicing from K4, probing from K6.
4. **Present the content** — entry points, four mitigation fronts, conflicting definitions.
5. **Guide** — write one counterfactual pair together and compare outputs.
6. **Elicit performance** — teams build a five-pair probe set for their domain.
7. **Give feedback** — debrief: did the probe isolate one variable?
8. **Transfer** — each learner adds a disaggregated metric to their eval plan.

## What the framework doesn't mention but trainers need to know

- **Local language is a fairness issue.** A model that handles English beautifully and Singlish poorly produces a two-tier service, and no demographic metric will show it.
- **Fairness and utility trade off.** Aggressively blocking gendered completions degrades legitimate use; the trade-off is a business decision to document.
- **Bias work needs an owner.** Evaluations that nobody reads quarterly are decoration; assign the review.
- **Synthetic data can launder a skew.** Generated examples inherit the generator's defaults, so augmentation must be checked, not assumed.

## Watch out

- **Do not claim a technique "removes" bias.** The honest claim is measurable reduction on named probes, with residual risk stated.
- **Do not use one metric.** A single fairness score invites gaming and hides the subgroup that matters.
- **Do not run stereotype demos for laughs.** The room remembers the joke and not the mitigation.
- **The stale claim to retire:** "we'll fix bias after launch." In November 2026 the probe set is a week of work and the reputational cost of skipping it is measured in months.
