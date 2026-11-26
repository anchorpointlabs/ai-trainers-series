---
id: 05.02.I.K1
tsc: 5
level: Intermediate
code: K1
title: Why generative evaluation has no answer key, and what replaces it
---

# Why generative evaluation has no answer key, and what replaces it

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K1**


> **Framework text (verbatim):** "Theoretical foundations of generative AI evaluation."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 1 of 12

**One-line version:** A classifier can be marked right or wrong against an answer key; a generative model cannot, so evaluation becomes measurement — define the construct, sample the inputs, quantify the doubt.

## What it is

The theoretical foundation of generative evaluation is measurement theory applied to open-ended output. There is no single correct answer to compare against, so quality has to be defined, operationalised into indicators, sampled across a test set, and reported with an honest account of how uncertain the result is. Everything else at Intermediate level — metrics, charts, statistics, pipelines — is machinery bolted onto that one admission.

## Deep expansion

### The concept

Classifier evaluation is trivial in principle and hard in practice. Generative evaluation is hard in principle. Ask a model to classify a support ticket as billing or technical and there is a right answer. Ask it to draft the reply and there are forty acceptable replies, several bad ones, and no key.

That absence does not make evaluation impossible. It makes it a measurement problem, and measurement has a discipline older than computing. You name the property you care about (the construct), you choose signals that stand in for it (indicators), you take a sample rather than a census, and you report the result with its error. A number without a construct is a number nobody can defend in a procurement meeting.

The practical consequence: at this level the learner stops asking "which model is best" and starts asking "best at what, measured how, on which inputs, and how sure are we". Those four questions are the foundation. They are also, usefully, the four questions that a vendor's benchmark slide cannot answer.

### The sub-concepts

**The construct comes first.** "Quality" is not a construct, it is a word. The construct is task-shaped: *a reply that answers the customer's question using only the facts in the policy document, in a tone the firm would sign, with a clear next step*. Different task, different construct, different evaluation. If two teams get different scores for "quality", they are usually measuring different constructs and have not noticed.

**Three families of instrument.** Intrinsic measures compare the output to references or to a model of language (BLEU, BERTScore, FID). Extrinsic measures ask whether the downstream task succeeded (was the ticket resolved, did the code run). Human judgement asks whether a person finds it good. Each answers a different question and carries a different bias; a mature evaluation uses at least two families and reports when they disagree.

**Proxy, not truth.** Every generative score is a proxy for the construct, never the construct itself. BLEU is a proxy for adequacy in translation. A judge model's score is a proxy for a human's judgement. Once a proxy is treated as the thing, the evaluation stops finding problems and starts certifying them.

**Sample, not census.** You test on forty emails, not on the four million you will receive. That is fine, as long as everyone in the room knows the result has a sampling error and the test set was drawn from somewhere defensible.

**The instrument is fallible too.** The judge model has biases. The human rater drifts by mid-afternoon. The metric has blind spots. Evaluation theory at this level means treating the measuring device as a device — something with error — rather than as a window.

### How it connects to the rest of the framework

`TSC5-Intermediate-K4` is where the construct gets written down as a rubric; `K2` supplies the instruments; `K3` is how you see a distribution instead of a mean; `K6` is how you quantify the doubt this entry keeps insisting on. `TSC5-Intermediate-A1` is the apparatus that runs all of it. Below this, `TSC5-Basic-K2` (accuracy, diversity, coherence, novelty) is the vocabulary of constructs; `TSC5-Basic-K5` (human perception) is the first warning that the instrument has error. `TSC4-Intermediate-*` (Model Selection) consumes these results, and `TSC8-*` (Responsible AI) sets constraints the evaluation must respect.

### What is current as of November 2026

Three shifts matter. **Leaderboards have lost authority.** Teams now build small, private, task-shaped test sets because public benchmarks are contaminated and because the frontier models of late 2026 — the GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — are separated less by capability than by behaviour on a specific task. **LLM-as-judge is now the default instrument**, which means judge validation (agreement with humans, stability across re-runs) has become part of the method rather than an optional extra. **The frontier has moved to trajectories.** For agents, "correct" is no longer one good reply; it is whether the task got done in an environment, in how many steps, at what cost.

### Common misconceptions

- *"Evaluation means running the benchmark."* A benchmark is someone else's construct. Useful for a first filter, useless as evidence for your task.
- *"If it can't be measured objectively, it can't be evaluated."* Human judgement is measurement — with error, which is why you design for agreement and moderation instead of pretending it away.
- *"A higher score means a better model for us."* Only if the test set matches your inputs and the metric matches your construct.
- *"Evaluation is a phase before deployment."* It is a loop: offline now, online after, re-run whenever the prompt, the data or the model version changes.

## How a student should understand it

**Mental model:** a taste panel, not a thermometer. There is no instrument that reads "quality" off a dish; there is a rubric, several tasters, a protocol, and a result reported with a margin.

**Three things they can do after this bullet:**
1. Write the construct for their own task in one sentence, with three dimensions.
2. Say, for any score they are shown, which family of instrument produced it and what it cannot see.
3. Explain why a single evaluation run is evidence rather than proof.

**Misconceptions to kill:** that evaluation needs an answer key, that a benchmark score settles a procurement decision, and that a number without a stated construct is meaningful.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The Met Service forecast.** "70% chance of rain" cannot be marked right or wrong on any one day. It becomes a good forecast or a bad one over a season of comparisons against what actually happened. Generative evaluation works the same way: one run tells you little, a repeated, sampled, calibrated process tells you a great deal. Breaks where weather has an objective outcome and quality usually does not.

**The PSLE oral exam.** Two examiners, a rubric, and a moderation process, because Singapore long ago accepted that a single examiner's impression is not a measurement. Point out what the exam system does that most AI teams skip: it *calibrates* the examiners and checks their agreement.

### Worked example with a real tool

Ask any chat model to turn a business situation into an evaluation plan, and note how eagerly it will invent the construct for you if you let it:

```
I run the customer-service inbox for a small logistics firm in Jurong.
We want AI to draft replies to delivery-delay complaints.

Do not write the plan yet. First ask me five questions about what a
good reply means in this business.

Then produce:
1. The construct, in one sentence, with three dimensions.
2. For each dimension, one indicator a script can check and one that
   needs a human.
3. What 40 test emails must include to be a fair sample.
4. The decision rule: what result would make us adopt it.
```

What to point at afterwards: notice that without the instruction to ask questions it produces a confident generic plan — a construct it invented, for a business it has never seen. That is the failure this bullet exists to prevent, and it takes ten seconds to demonstrate.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — put a classifier's 94% accuracy next to a generative model's "it wrote something reasonable". Ask why the second number is missing.
2. **State the objective** — you will write a construct and a sampling plan for one real task.
3. **Recall prior learning** — the four Basic criteria; ask which of them is measurable without a human.
4. **Present the content** — answer key versus measurement; the three instrument families; proxy, sample, fallible instrument.
5. **Guide** — build the construct for a shared example (a clinic's appointment reminder) as a class.
6. **Elicit performance** — each learner writes a construct and three dimensions for their own task.
7. **Give feedback** — attack vague constructs ("helpful", "professional") until they become checkable.
8. **Transfer** — they bring the construct to the next session where the rubric is built.

## What the framework doesn't mention but trainers need to know

- **Evaluation is mostly a labelling problem, and labelling is the expensive part.** Budget conversations about "evaluation" are usually conversations about who will read 400 outputs and how their time is protected.
- **Test sets rot.** Inputs drift, models change, and old test sets leak into training data. An evaluation set is a living asset with an owner, not a file on someone's desktop.
- **Construct validity is the failure nobody catches.** A perfectly reliable pipeline measuring the wrong thing produces beautifully stable nonsense. Ask "would a good output score well here?" before asking "is this reproducible?"
- **The evaluation is a political document.** It will be quoted in procurement, in audit, and in an incident review. Write it so it survives being read by someone who wants to disagree.

## Watch out

- **Do not teach "objective equals good".** The most cited evaluations in industry are human-judgement studies with careful protocols.
- **Do not demo a public leaderboard as if it were an evaluation.** It teaches the exact habit this bullet is meant to break.
- **Do not let the room leave believing a judge model is a substitute for a human panel.** It is a cheap, fast, biased instrument that needs calibrating against one.
- **The stale claim to retire:** "you can't evaluate generative AI because there's no right answer." You cannot *grade* it. You can measure it — which is harder, more useful, and the whole subject of this level.
