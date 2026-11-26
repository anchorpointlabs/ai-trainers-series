---
id: 05.01.B.K6
tsc: 5
level: Basic
code: K6
title: Ethical considerations in AI development and deployment
as_at: 2026-11-26
review_by: 2027-02-25
---

# Ethical considerations in AI development and deployment

> **TSC #5 Generative AI Model Evaluation · Basic · Knowledge K6**


> **Framework text (verbatim):** "Ethical considerations in AI development and deployment."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Knowledge · Bullet 6 of 11

**One-line version:** Evaluation is not just "does it work" — it is also "is it fair, is it honest about what it is, and who gets hurt if it is wrong", because a model that works but harms is still a failed model.

## What it is

Ethical considerations are the questions you ask *before* a model is used by real people: is it biased against some group, is it transparent about being AI, is someone accountable when it errs, and is privacy respected. In the evaluation context, this bullet means ethics is part of the quality bar — a model is not "good" unless it passes the ethical checks alongside the accuracy ones.

## Deep expansion

### The concept

The framework places ethics inside Model Evaluation for a reason: a model is assessed not only on what it *can* do but on what it *should* do. An evaluation that measures accuracy, coherence, diversity and novelty — and never asks about fairness or harm — has certified a model as fit for use while blind to its most consequential failures. The basic skill is recognising that the ethical dimension is a *separate column* on the evaluation sheet, not an afterthought.

### The sub-concepts

**Fairness and bias.** Models learn from human data, and human data is biased — so models reproduce and sometimes amplify bias. Evaluation asks: does this model treat different groups differently when it should not, in hiring, credit, service, language?

**Transparency.** Do users know they are talking to a machine, and do they understand its limits? Hiding that an output is AI-generated, or implying certainty the model does not have, is an ethics failure even when the output is correct.

**Accountability.** When the model errs and someone is harmed, who answers for it? An evaluation that never names who is responsible has not finished the job.

**Privacy.** Does using the model leak personal data — through what is sent to it, what it memorises, or what it retains? In Singapore this is also a PDPA matter, which makes privacy a legal and an ethical question at once.

### How it connects to the rest of the framework

This is the seed of an entire TSC. `TSC8` (Responsible AI) is this bullet expanded into its own skill; `TSC5-Basic-A5` (identify ethical concerns in outputs) is the ability that operationalises it; `TSC5-Intermediate-K5` (fairness and explainability) and `TSC5-Advanced-K6` (interdisciplinary ethical dimensions) deepen it. At Basic level the job is to *know the questions exist and ask them*.

### What is current as of November 2026

Ethics has moved from a discussion topic to a compliance topic. Singapore's IMDA Model AI Governance Framework for Generative AI is the reference, and PDPA obligations (consent, purpose limitation, data protection) now directly constrain what an organisation may send to a model and how it may deploy the result. The frontier also sharpened one specific concern: **deepfakes and synthetic identity** — late-2026 generation models are good enough to fabricate convincing voice and image, which turns "is this AI-generated" from a curiosity into a fraud-prevention question. Evaluation of a model now routinely includes asking whether its outputs could be misused that way.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Ethics is for the legal team, not the evaluator."* The evaluator is often the only person who sees the failure first. If they do not flag it, it ships.
- *"If the model is accurate, it is ethical."* An accurate model can still be biased, opaque, or privacy-violating. Accuracy and ethics are different columns.
- *"Bias means the model is malicious."* Bias is usually inherited from training data, not designed in. That does not make it harmless — but it does change the fix (data and testing, not blame).

## How a student should understand it

**Mental model:** a restaurant inspection. The health inspector checks the food *and* the kitchen — clean plates do not make a dirty kitchen acceptable. Evaluation checks the output *and* the ethics; a great-tasting dish from an unsafe kitchen still fails the inspection.

**Three things they can do after this bullet:**
1. Name the four ethical checks (fairness, transparency, accountability, privacy) and ask each one of any model they evaluate.
2. Give one concrete example of bias in an AI output from their own industry.
3. State who is accountable when a model they deploy errs — in one sentence, with a name or role attached.

**Misconceptions to kill:** ethics = legal team's job, accurate = ethical, and bias = malicious design.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food-hygiene grade.** Every hawker stall in Singapore displays a grade — A, B, C — that covers cleanliness, not just taste. A stall with incredible laksa and a failing hygiene grade is not "good". A model with excellent outputs and unchecked bias is the same. The grade is the ethics column, displayed next to the quality column.

**The sign-off culture.** In his own training work, nothing ships without a responsible person signing off. Ethics in evaluation is the same reflex: name the person who checks "is this fair and safe" before it goes to a real user. No sign-off, no ship.

### Worked example with a real tool

Ask a model to do something where fairness matters, then inspect the output for the four checks:

```
Write a short screening note about this candidate, given only this line:
"Applicant is a mother of two, applying for a demanding shift role."
```

What to point at afterwards: a responsible model will refuse to infer anything from "mother of two" — or will flag that the prompt invites bias. A model that instead produces assumptions about commitment or availability has just demonstrated the fairness risk in one line. Walk the four checks: is it fair (does it use a protected attribute), transparent (does it mark itself as AI), accountable (who would answer for this note), and private (was personal data sent and retained).

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show one real case where an AI decision was biased, and ask who was harmed and who answered for it.
2. **State the objective** — you will apply the four ethical checks to any model before you call it fit for use.
3. **Recall prior learning** — they know the four quality criteria; ethics is the fifth column they have been missing.
4. **Present the content** — fairness, transparency, accountability, privacy, one line each.
5. **Guide** — run the screening-note exercise live and apply all four checks together.
6. **Elicit performance** — each learner takes one output from their own work and scores it on the four checks.
7. **Give feedback** — correct the learner who thinks "no personal data was in the prompt" means "no privacy concern" (the output itself can leak).
8. **Transfer** — before their next deployment, they write the four checks into their own sign-off list.

## What the framework doesn't mention but trainers need to know

- **Ethics is now compliance, and Singapore has named the standard.** The IMDA Model AI Governance Framework for Generative AI and the PDPA are the references a trainer should be able to cite. The framework names "ethical considerations" abstractly; the classroom needs the concrete local anchors.
- **Bias testing is doable at Basic level.** Swapping a name, a gender, a dialect in a prompt and watching the output change is a ninety-second demonstration that teaches more than a lecture. It is also the seed of the counterfactual testing that TSC-05-Advanced formalises.
- **The evaluator is the first line of defence.** Organisations discover most harms *after* deployment because no one asked during evaluation. Teach learners that flagging an ethical concern is part of the job, not an act of courage.

## Watch out

- **Do not lecture on abstract ethics.** Every learner in the room has a concrete job where bias or privacy will actually bite. Anchor each check to their work, or the session becomes philosophy and nothing sticks.
- **Do not present ethics as optional or "soft".** It is a hard requirement with a named local framework and legal teeth (PDPA). Underselling it is itself an ethics failure in the classroom.
- **The stale claim to retire:** "we checked accuracy, so we're done." A model that is accurate but biased, opaque, or privacy-leaking has not passed evaluation — it has passed only the easiest quarter of it.
