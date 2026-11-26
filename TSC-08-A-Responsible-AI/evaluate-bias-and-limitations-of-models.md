---
id: 08.03.A.A2
tsc: 8
level: Advanced
code: A2
title: Evaluate bias and limitations of models
---

# Evaluate bias and limitations of models

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A2**

> **Framework text (verbatim):** "Evaluate biases, limitations and ethical implications of models, including using an evaluation dataset from various sources."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 6 of 14

**One-line version:** One dataset is a flattering mirror; bias shows up where the data changes.

## What it is

Ethical evaluation means testing a model on data drawn from several sources, disaggregating the results by group, and reporting limitations as findings rather than caveats. It is different from ordinary quality assurance in two ways: the test set is deliberately built to include the populations and dialects the model will actually meet, and the headline number is never the finding — the per-slice numbers are.

## Deep expansion

### The concept

A model that scores well overall can fail catastrophically on a subgroup, and aggregate accuracy hides it. If a group is two percent of the traffic, a model can be wrong on half of that group and still report 99 percent. The same arithmetic makes a fraud detector that says "no fraud" every time look accurate on a dataset where fraud is rare — it has learned nothing and reports everything.

So the unit of evaluation is the slice, not the model. For each slice you report the metric that matches the harm: true-positive rate where the harm is qualified people being rejected, false-positive rate where the harm is innocent people being flagged, calibration where a score is being read as a probability. And you report them together, because the fairness definitions are mathematically incompatible — you cannot simultaneously equalise selection rates, equalise error rates and keep scores calibrated when base rates differ. Choosing which one to satisfy is a decision with a stakeholder, not a computation.

### The sub-concepts

**The metric family.** Demographic parity: equal approval rates across groups. Disparate impact: the four-fifths rule, the unprivileged group's selection rate at least 80 percent of the highest group's — the standard in employment and lending audits. Equal opportunity: equal true-positive rates among people who actually qualify. Equalised odds: equal true-positive and false-positive rates. Predictive parity: a score means the same probability regardless of group. Counterfactual fairness: flip only the protected attribute and the prediction should not move. Each answers a different question, and the impossibility theorem says you cannot have all of them.

**Source diversity.** Evaluation sets should come from different populations, channels, time periods and languages. A support bot tested on tidy English tickets and deployed on Singlish voice notes has been tested on a different product.

**Benchmarks are proxies.** TruthfulQA measures a style of factual failure, BBQ a style of social bias, HarmBench a style of harmful compliance. They tell you how a model behaves on someone else's test, which is a starting point, not a verdict on your use case.

**Limitations to report explicitly.** Context limits, refusal behaviour, drift over time, sycophancy (agreeing with a false premise), and multilingual coverage gaps. Each has a test; each is usually omitted.

**Evaluator models need auditing too.** Using a model to grade thousands of outputs is efficient and introduces its own bias — calibrate the judge against a human-labelled sample before trusting its verdicts.

### How it connects to the rest of the framework

`TSC8-Advanced-A3` builds the adversarial cases this bullet's datasets need; `TSC8-Advanced-A1` consumes the report at the pre-deployment gate; `TSC8-Advanced-K4` explains why the cultural lens shows up as dialect slices; `TSC8-Advanced-A5` is the argument you have when two metrics point opposite ways.

### What is current as of November 2026

Subgroup reporting has moved from virtue to contract term: enterprise buyers now ask vendors for disaggregated evaluation results alongside the model card, and the major providers publish them — OpenAI's GPT-6 generation, Anthropic's Claude 5.5 and Google's Gemini 3.1 Pro and 4 Argon all ship system cards with safety and capability evaluations that a deployer can read before writing their own. In Singapore, Project Moonshot and AI Verify give teams a runnable harness rather than a spreadsheet. The gap that remains is localisation: generic benchmarks do not test Singlish code-switching, Malay or Tamil, so the evaluation set that matters is the one you build.

### Common misconceptions

- *"We hit 99 percent accuracy, so it is ready."* Accuracy is a vanity metric; the subgroup table is the finding.
- *"One good dataset is enough."* One dataset measures one population. Bias is a difference between populations.
- *"The benchmark says it is unbiased."* Benchmarks measure their own test distribution, not your customers.
- *"Bias is a model property, so swap the model."* Bias is a property of the model-in-context: your data, your prompt, your threshold.

## How a student should understand it

**Mental model:** a fitting room with one mirror and flattering light. You need three mirrors and daylight before you buy the suit.

**Things they can do after this bullet:**
1. Build an evaluation set from at least three sources with different populations.
2. Produce a disaggregated results table with the metric matched to the harm.
3. State one limitation as a finding with its test.

**Misconceptions to kill:** aggregate accuracy is readiness, one dataset is enough, and a benchmark verdict transfers to your use case.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The single blood test.** A "normal range" derived from one population flags healthy people from another as abnormal. The test is not broken; the reference data is unrepresentative. Where it breaks: a blood test has a lab standard behind it, while most AI evaluations have no agreed reference range at all.

**Four mirrors in a tailor's shop.** Each mirror shows something true and none shows everything; the tailor who uses one sells you a jacket that pulls at the shoulder. Where it breaks: mirrors do not contradict each other mathematically — fairness metrics do.

### Worked example with a real tool

```
Design a multi-source evaluation for a translation model used by a
Singapore public-facing service. It must expose dialect bias.
Give me: (1) the sources the test set should be drawn from, (2) the slices
to report, (3) the metric per slice, (4) three limitations I should state
in the report even if the numbers look fine.
```

What to point at: most answers list "English, Chinese, Malay, Tamil" and stop. Push on register and code-switching: the same language spoken differently by different Singaporeans. Then point at column four — the model will happily generate limitations, and the class should notice that a limitation without a test is a disclaimer, not a finding.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two results screens: 97 percent overall, 61 percent on one slice. Ask which number the vendor will quote.
2. **State the objective** — build a multi-source set and report per-slice metrics.
3. **Recall prior learning** — proxy variables from the bias discussion; why removing columns fails.
4. **Present the content** — the metric family, the impossibility, source diversity.
5. **Guide** — build the translation evaluation together.
6. **Elicit performance** — groups draft a slice table for their own model.
7. **Give feedback** — correct mismatched metrics (parity where the harm is false rejection).
8. **Transfer** — each learner specifies the one slice their current test set is missing.

## What the framework doesn't mention but trainers need to know

- **Threshold choice is a policy choice.** Moving a cut-off changes who is approved; that decision belongs to a business owner, documented.
- **Evaluation decays.** Production data drifts; a report from last quarter describes a system that no longer exists.
- **Label quality dominates everything.** If the ground truth was labelled by one team in one language, every metric inherits that view.
- **Refusal rates are a bias metric.** A model that answers fluently in English and refuses in Malay has a coverage problem, not a safety success.

## Watch out

- **Do not present one fairness metric as "the" fairness metric.** Teach the family and the conflict.
- **Do not let a vendor's benchmark table end the discussion.** It measures their test, not your users.
- **Do not accept "we will monitor it in production" as an evaluation.** Monitoring finds drift; it does not find the bias you never tested for.
- **The stale claim to retire:** "The model is unbiased." Say: "on these slices, with this metric, at this threshold, we measured this."
