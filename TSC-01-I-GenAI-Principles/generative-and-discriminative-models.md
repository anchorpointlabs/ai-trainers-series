---
id: 01.02.I.K4
tsc: 1
level: Intermediate
code: K4
title: "Generative and discriminative models: two ways to model the same data"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Generative and discriminative models: two ways to model the same data

> **TSC #1 Generative AI Principles and Applications · Intermediate · Knowledge K4**


> **Framework text (verbatim):** "Difference between generative and discriminative models."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Knowledge · Bullet 4 of 10

**One-line version:** A discriminative model learns where the boundary is; a generative model learns what the data looks like — and that difference decides which of them is allowed to make a decision about a person.

## What it is

Discriminative models learn the mapping from input to label — is this transaction fraudulent, will this customer churn, which category does this email belong to. Generative models learn the distribution of the data itself, which lets them produce new samples. Both are machine learning; they answer different questions, are evaluated differently, and carry different governance burdens.

## Deep expansion

### The concept

The clean statement: a discriminative model estimates the probability of a label given the input; a generative model estimates the probability of the input itself, optionally alongside the label. Everything practical follows.

Because the discriminative model only has to separate cases, it can be accurate, cheap and small — a few thousand labelled examples may be enough for a narrow decision, and its errors are inspectable in a confusion matrix. Because the generative model must represent the whole distribution, it needs far more data and compute, but it can produce an artefact nobody has seen before and transfer to a task it was never specifically trained for.

The framework asks for the difference as knowledge. At Intermediate level the learner should also hold the consequence: **the model that decides must be the model you can explain.** When a decision about a person is challenged — a loan declined, an applicant not shortlisted — "the model generated a paragraph" is not an answer. A boundary can be inspected, thresholded, tested for disparate impact and re-run deterministically. A sample cannot.

### The sub-concepts

**Two questions, not two eras.** Discriminative asks "which class?"; generative asks "what would this look like?". Neither is newer or more advanced, and most value already deployed in banks, logistics and government is discriminative.

**Data and label economics.** Discriminative training needs labels, which are expensive and often inconsistent; generative training needs volume, which is expensive in compute. The budget that decides most projects is labelling, not modelling.

**Evaluation differs in kind.** A classifier is scored with accuracy, precision, recall and a confusion matrix against held-out labels. A generated artefact has no single correct answer, so evaluation needs rubrics, pairwise comparison or human judgement — `TSC5` is that discipline.

**Failure modes differ.** Classifiers suffer drift, label bias and threshold errors. Generative models suffer fabrication, bias amplification and fluency without truth.

**The boundary has moved.** Embeddings from a language model plus a small classifier give a cheap, explainable decision built on a rich representation. Prompting a large model to classify works, but produces a decision with sampling variance and no threshold you can audit.

**Hybrids are the norm in production.** A moderation classifier screens the input, a generative model drafts, a classifier validates the output, and a rules engine holds the authority to act.

### How it connects to the rest of the framework

`TSC1-Basic-K05` gives the one-line version — decision versus creation — for user-level learners; this entry is the practitioner's version with the governance consequence attached. `TSC1-Intermediate-K01` is the prediction principle both rest on, `TSC1-Intermediate-A01` is where you decide which kind a use case needs, and `TSC4` (Model Selection) is the full selection framework.

### What is current as of November 2026

The practical default has shifted. Where a team once trained a bespoke classifier for every labelling task, the first experiment now tends to be a small model with a good prompt and a dozen examples, because current frontier models classify ordinary material competently with no training data.

What has not shifted is the governance line. Regulated decisions in Singapore still expect explainability, documented thresholds, human accountability and testing for disparate impact, which favours a discriminative model or a rules-plus-model hybrid. Meanwhile the discriminative layer has quietly grown: guardrail classifiers, prompt-injection detectors and content filters in front of generative systems are ordinary discriminative models, and they are the part of the stack that fails most visibly when wrong.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Generative is the newer, better version of discriminative."* Different jobs. A chatbot cannot replace a fraud model that must run in 40 milliseconds, deterministically, with an auditable threshold.
- *"A large model can classify, so we do not need a classifier."* It can, with sampling variance and no calibration. At volume, a tuned classifier is cheaper, more consistent and easier to defend.
- *"Bias is a generative problem."* Historical bias in labels is a discriminative problem first, and it is older than generative AI.

## How a student should understand it

**Mental model:** the NEA inspector and the chef. The inspector grades the stall against a checklist; the chef produces the dish. You would not ask the inspector to cook, and you would not let the chef award their own grade.

**Things they can do after this bullet:**
1. Classify any system they meet as generative, discriminative or hybrid, and say why.
2. Explain why a decision about a customer needs an explainable model, not a generated paragraph.
3. Choose the cheaper of the two when a task allows either.

**Misconceptions to kill:** that generative supersedes discriminative, that a chatbot can own a decision, and that "AI" means one thing.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The polyclinic triage nurse.** The nurse sorts: urgent, routine, refer. That is a decision made against criteria, and it is auditable — you can ask which criteria were applied. The doctor's referral letter is generated: fluent, contextual, hard to audit line by line. Both are essential; putting the letter in charge of triage would be a governance failure.

**The fishball noodle stall's chilli.** The stall decides how spicy — a setting, held constant, inspectable. The cook plates each bowl — a production, varying slightly each time. Customers complain about the second and audit the first.

### Worked example with a real tool

Take twenty customer emails and run the generative version, in ChatGPT or Claude:

```
Classify each email below into exactly one label: ACTION, FYI, or SPAM.
Return a table with columns: email number, label, confidence (high/medium/low),
and a one-line reason. Do not write anything outside the table.
```

What to point at: the confidence column is not calibrated — most rows come back "high", including the wrong ones. Run it twice and some labels change. Then describe the discriminative alternative: the same task as a small classifier trained on 500 labelled emails, with a confusion matrix you can show an auditor and a threshold you can move when the cost of a false negative changes. Close with the governance question: if the email is a complaint with a legal deadline, which system do you want deciding, and who signs off when it is wrong?

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two outputs: "spam / not spam" and a drafted reply to a complaint.
2. **State the objective** — by the end you can place a system and defend the placement.
3. **Recall prior learning** — Basic: decision versus creation.
4. **Present the content** — the two questions, data economics, evaluation, failure modes, hybrids.
5. **Guide** — sort six systems with the room, two aloud.
6. **Elicit performance** — pairs sort twelve systems and mark which must be explainable.
7. **Give feedback** — debrief the contested cases: screening, triage, moderation.
8. **Transfer** — each learner lists the decisions their team makes and marks which are made by a model they could explain.

## What the framework doesn't mention but trainers need to know

- **Latency and determinism are requirements, not preferences.** A fraud check inside a payment flow has a millisecond budget and must return the same answer twice. Sampling cannot meet that, and no prompt fixes it.
- **Labelling is the hidden project.** Most failed classifier projects fail on label definition and quality, not model choice. Budget for an adjudication process.
- **Hybrid patterns are the mature answer.** Retrieve, generate, validate with a classifier, human approves. Teach the pattern rather than a preference.

## Watch out

- **Do not imply discriminative means legacy.** Most deployed business AI is discriminative and will stay that way.
- **Do not let the room conclude a chatbot can sign off a credit decision.** Say plainly that it cannot, and name the human who must.
- **The stale claim to retire:** "generative models can't classify." They can — competently, and less reliably than a tuned classifier. Accuracy is not the issue; auditability and variance are.
