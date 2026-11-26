---
id: 01.02.I.A3
tsc: 1
level: Intermediate
code: A3
title: "Reading an output for what is wrong: limits, bias and the shape of the gap"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Reading an output for what is wrong: limits, bias and the shape of the gap

> **TSC #1 Generative AI Principles and Applications · Intermediate · Ability A3**


> **Framework text (verbatim):** "Analyse limitations and potential biases in AI-generated content."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Ability · Bullet 8 of 10

**One-line version:** Reviewing generated content is not reading it — it is a four-pass audit for fabricated claims, missing voices, marker-driven judgements and false confidence, run against a checklist rather than a feeling.

## What it is

The ability to take any generated artefact and produce a written judgement of its limitations and biases: what is unsupported, what a domain expert would expect and did not get, whose case has been treated as the default, and where the confident tone outruns the evidence. The deliverable is not an opinion. It is a short review with items and reasons, which is what makes it usable in a workplace.

## Deep expansion

### The concept

Two things make this hard. First, generated text is *uniformly* fluent, so the sentence that is wrong looks exactly like the sentence that is right. Second, bias in generated content is rarely rude or obvious — it appears as a default, a framing, an omission, a category that was never considered. Neither defect announces itself, so the audit has to be structured.

Four limit families, and the check for each:

- **Knowledge limits** — the facts are stale, thin or invented. Check: trace every checkable claim to a source you can open.
- **Reasoning limits** — a step is invalid, or arithmetic is wrong. Check: re-derive the conclusion independently, especially any comparison or total.
- **Instruction limits** — it answered a neighbouring question, ignored a constraint, or dropped half the brief. Check: score the output against the brief's constraints one by one.
- **Calibration limits** — confidence does not track correctness. Check: sample ten outputs, mark each right or wrong, and see whether your own certainty tracked reality.

Four bias mechanisms, and how each shows up:

- **Representation** — the people, places or cases in the data are unrepresentative. Shows up as an international default voice, or a category that only exists in the majority case.
- **Historical** — the labels or the corpus encode past decisions. Shows up as a recommendation that reproduces an old pattern of who gets shortlisted, promoted or flagged.
- **Measurement** — the proxy recorded is a poor stand-in. Shows up as a judgement resting on a number that measures something adjacent.
- **Deployment** — the model is used on a population it was not built for. Shows up as a new context where the old thresholds do not mean what they meant.

### The sub-concepts

**Hallucination is a family, not a defect.** A fabricated citation, a confabulated figure, a drifted summary, a stale fact and a merged entity all fail differently and need different checks. Naming the sub-type tells the reviewer where to look.

**Omission is the bias you cannot see.** Ask what a domain expert would have included: a risk, a stakeholder, an exception, a minority case. A summary that is accurate on every sentence and silent on the decisive issue has still failed.

**The counterfactual test.** Take the output, remove the identity markers — names, gender, age, school, university, race, address — and run it again. If the judgement changes, the first output was reading markers rather than merit. It is the cheapest bias test available and it takes two minutes.

**Sycophancy as a limitation.** Models are trained toward agreement, so a leading question tends to get a confirming answer. "Are you sure?" produces apology, not verification. Ask for a re-derivation, or for the strongest case against the current answer.

**Framing.** The same facts can be presented as a success or a failure. Ask who benefits from this framing, and whether the opposite framing would also be defensible from the same evidence.

**Confidence and hedging as learned behaviour.** "I cannot verify this" and "certainly" are both post-training habits. Neither is a measurement of reliability.

### How it connects to the rest of the framework

`TSC1-Basic-K06` is the user-level list of limitations; this entry is the audit method. `TSC1-Intermediate-K05` is the upstream cause — data coverage, labelling, deployment. `TSC1-Intermediate-A04` supplies the measurement that turns an impression of bias into a number. `TSC8` (Responsible AI) and `TSC9` (security and ethics) hold the obligations this analysis serves.

### What is current as of November 2026

Vendors now publish system cards and bias evaluations, and practitioners should know exactly how little those transfer: they measure the vendor's test sets, not your population. Treat them as evidence of process, not of fitness.

Reasoning modes have reduced a class of arithmetic and multi-step errors without touching source fabrication — a model that thinks longer still invents a citation with total composure. Multimodal output has opened new bias surfaces that text-only reviewers miss: who is depicted by default, what "professional appearance" looks like, which skin tone the image model returns for "a Singaporean executive". And agentic output has made the stakes asymmetric: an error that is drafted can be caught, an error that was acted on has already happened.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"If it were biased, I would notice."* You notice tone. Bias hides in defaults and omissions, which is why the counterfactual test exists.
- *"Bias means the model is rude or refuses things."* Refusal behaviour is a different topic. Bias here is structural: whose case is typical, whose is the exception.
- *"The guardrails handle it."* Guardrails catch categories of harmful content. They do not catch a shortlist that quietly favours one school.
- *"It is the vendor's responsibility."* You chose the use, the population and the prompt. Deployment bias is yours by construction.

## How a student should understand it

**Mental model:** the auditor ticking and tying a set of accounts. You do not read for the story; you check each line against a document, and you ask what should have been there and is not.

**Things they can do after this bullet:**
1. Run the four-pass read on any output and produce a review with items.
2. Name the specific hallucination sub-type and the specific bias mechanism in a given case.
3. Run a counterfactual test and interpret a changed judgement correctly.

**Misconceptions to kill:** that bias is visible, that fluency signals correctness, and that guardrails remove the need for review.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The HDB flat viewing.** You notice the fresh paint, the new flooring and the good light. You do not notice the slow leak behind the wardrobe until the neighbour mentions it. Fluency is the fresh paint; omission is the leak.

**The NEA inspection.** A hygiene grade is not a vibe — it is forty-odd checkpoints, some of which are about what should be there (a hand basin, a covered bin) rather than what is wrong. That is why a bias review needs a checklist, including a "should be present" list.

### Worked example with a real tool

Use four short CVs (synthetic, never real). In ChatGPT or Claude:

```
From the four CVs above, write a 100-word paragraph recommending who to
shortlist for the operations executive role, and give the single strongest
reason for each recommendation.
```

Then, in the same thread:

```
Now redo the task: remove all names, universities and graduation years,
and present the four candidates as A, B, C, D in a different order. List any
recommendation that changed, and say why it changed.
```

What to point at: whether the ranking flips. If it does, the first output was reading markers, not merit — and neither output carried any warning that it had done so. Then run the claim trace: ask for one statistic supporting the recommendation, and show how plausible the invented number looks. Two checks, two minutes, one review.

### Live demo or exercise

**Audit in four passes.** Give pairs one generated artefact — a policy summary, a performance comment, a product description — and four headings: unsupported claims, missing voices, marker-driven judgements, confidence mismatch. Ten minutes, then each pair reports one finding of each type. The "missing voices" column is always the emptiest and the most revealing.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show the same recommendation before and after removing names; ask what changed.
2. **State the objective** — by the end you can produce a written review with named defects.
3. **Recall prior learning** — the data stage where bias enters; the limits taught at Basic.
4. **Present the content** — four limit families, four bias mechanisms, the four-pass read.
5. **Guide** — run the CV counterfactual live.
6. **Elicit performance** — pairs audit a supplied artefact under four headings.
7. **Give feedback** — debrief; insist on naming the mechanism, not just the symptom.
8. **Transfer** — each learner audits one output they produced at work last week and logs the review.

## What the framework doesn't mention but trainers need to know

- **Bias review needs domain expertise.** A generalist can find unsupported claims; only the HR practitioner knows what a fair shortlist looks like. Pair the reviewer with the specialist.
- **The review itself is the artefact.** In a dispute, "we reviewed it" is worth nothing and a dated checklist is worth a great deal. Make the review a deliverable, not a step.
- **Singapore has expectations here.** Fair employment guidelines, PDPA obligations on personal data, and sector rules in finance all assume a human is accountable. Mention that the law exists and route specifics to legal.
- **The counterfactual should be routine, not exceptional.** Any output that ranks, scores, shortlists or assesses a person gets the swap test before it is used.

## Watch out

- **Do not use real CVs, real complaints or real performance reviews in class.** Synthetic or redacted only, and say so.
- **Do not declare a model "unbiased" after one test.** Passed one counterfactual is not cleared; it is sampled.
- **Do not let the room conflate bias with toxicity.** They are different failures with different controls, and treating them as one is how bias review gets skipped.
- **The stale claim to retire:** "AI is objective because it is just maths." The maths is fine; the data and the deployment are not neutral, and neither is the choice of what to measure.
