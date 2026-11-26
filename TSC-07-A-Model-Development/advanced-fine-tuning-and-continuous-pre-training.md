---
id: 07.03.A.K10
tsc: 7
level: Advanced
code: K10
title: Continuous pre-training and the fine-tuning ladder, rung by rung
as_at: 2026-11-26
review_by: 2027-02-25
---

# Continuous pre-training and the fine-tuning ladder, rung by rung

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K10**


> **Framework text (verbatim):** "Advanced fine-tuning techniques and continuous pre-training techniques."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 10 of 20

**One-line version:** There is a ladder — prompt, retrieve, adapt, fine-tune, continue pre-training — and most teams climb two rungs too far because the top rungs feel more like real engineering.

## What it is

Advanced fine-tuning is the set of methods that change a pre-trained model's behaviour with additional training: parameter-efficient adaptation (LoRA, QLoRA and relatives), full supervised fine-tuning, preference-based methods, and *continuous pre-training* — further next-token training on a large unlabelled domain corpus so the model absorbs a vocabulary and body of knowledge it never saw. Choosing among them is an economic decision as much as a technical one.

## Deep expansion

### The concept

The ladder exists because each rung costs more and risks more than the one below:

1. **Prompt and context.** Free, reversible, no artefact. If it works, stop.
2. **Retrieval.** Cheap, updates instantly when facts change, keeps provenance. Solves knowledge, not behaviour.
3. **Parameter-efficient fine-tuning.** Teaches *form* — tone, schema, task decomposition, refusal style — with a small adapter. Cheap to train, cheap to serve, easy to roll back.
4. **Full fine-tuning.** Changes the weights broadly. Needed when behaviour must be deep or the adapter is not enough; risks forgetting and is expensive to serve many variants.
5. **Continuous pre-training.** Domain adaptation at scale: legal, biomedical, a low-resource language, code for an unusual platform. Expensive, needs a large corpus, and is the only rung that adds *knowledge density* rather than style.
6. **Pre-training from scratch.** Almost never the right answer for an organisation. Worth naming so the conversation ends.

The decision rule that survives contact with reality: *fine-tuning changes how a model behaves; pre-training changes what it knows.* Teams routinely fine-tune to teach facts, then wonder why the facts do not stick.

### The sub-concepts

**LoRA and its variants.** A low-rank update is added to selected weight matrices, so you train a small number of parameters against a frozen base. Rank, target modules and learning rate matter more than most hyperparameters. QLoRA quantises the frozen base to fit larger models on smaller hardware. Adapters can be merged for serving or kept separate and swapped per tenant.

**Continuous pre-training mechanics.** Continue the original objective on domain text, usually at a much lower learning rate with a warmup, and *mix in* a proportion of general data (replay) to resist catastrophic forgetting. Use the same tokeniser; a domain-specific tokeniser change means a new embedding table and a much bigger project.

**Schedules and checkpoint selection.** Cosine with warmup, or a warmup-stable-decay shape that lets you branch from the stable phase and decay cheaply. Select checkpoints on a held-out task evaluation, never on training loss, and always re-run a general capability check to catch forgetting.

**Data construction for fine-tuning.** Loss masking so the model is trained on the answer and not on your prompt boilerplate; consistent chat templates; packing sequences; and a deliberate mix of hard negatives and refusal examples.

**Forgetting is the tax.** Every rung above prompt changes something you did not intend. The control is a fixed regression suite — twenty prompts covering general ability — run after every run.

### How it connects to the rest of the framework

`TSC7-Intermediate-K10` introduces continuous pre-training; this bullet is the full ladder and its economics. `TSC7-Basic-K8` covers supervised and parameter-efficient fine-tuning at entry level. `TSC7-Advanced-K11` is the alignment rung above this one, `TSC7-Advanced-K8` produces the corpus, and `TSC5-Intermediate-K4` is the evaluation that decides whether a rung helped.

### What is current as of November 2026

Two things have settled. First, LoRA-style adaptation is the default for domain behaviour; full fine-tuning is reserved for cases where it demonstrably wins. Second, continuous pre-training has become common in regulated and language-specific settings — including work on Southeast Asian languages — because a general model's coverage of local terminology, statutes and registers is thin. Serving-side support for many adapters on one base has made multi-tenant customisation practical, which changes the calculus: you can now have twenty variants without twenty deployments.

### Common misconceptions

- *"Fine-tuning will teach the model our product catalogue."* It teaches behaviour; facts belong in retrieval.
- *"More epochs means better learning."* Past a point it memorises the training set and degrades on everything else.
- *"LoRA is a cheap version of real fine-tuning."* It is a different, often better tool: reversible, composable and cheaper to serve.
- *"Continuous pre-training is just more fine-tuning."* It uses unlabelled text at far greater volume and a different objective.

## How a student should understand it

**Mental model:** a ladder where each rung doubles the cost and halves the reversibility. Climb only as far as the problem forces you.

**Three things they can do after this bullet:**
1. Place a requirement on the correct rung and justify it.
2. Design a LoRA run with a regression suite that would catch forgetting.
3. Say when continuous pre-training is justified and what corpus it needs.

**Misconceptions to kill:** that fine-tuning installs facts, that more epochs help, and that the top rung is the professional choice.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The specialist course.** Pre-training is general schooling; fine-tuning is a two-week course on your company's forms; continuous pre-training is sending the employee back for a full diploma in a new field. You do not enrol someone in a diploma to teach them one form. Where it breaks: the employee remembers the old job, whereas a model overwrites it — which is exactly why replay data exists.

**The tailor versus the alteration.** LoRA is an alteration you can unpick; full fine-tuning is recutting the garment.

### Worked example with a real tool

Make learners decide before they train:

```
We are a Singapore law firm. A general model gets our internal
precedent memos wrong: it uses the wrong citation format, misses
our house style, and does not know our internal matter codes.

Options: prompt, retrieval, LoRA fine-tune, continuous
pre-training, full fine-tune.

1. Assign each of the three problems to the cheapest rung that
   actually solves it, and say why.
2. For the LoRA option, specify the data you would collect, how
   many examples, and how you would mask loss.
3. Give me the regression suite: five prompts that must not get
   worse.
4. What would make you escalate to continuous pre-training?
```

What to point at afterwards: the citation format and house style belong to LoRA; the matter codes belong to retrieval or structured lookup; nothing here justifies continuous pre-training unless the firm has a large corpus of unlabelled specialist text. Most learners over-assign to fine-tuning, which is the correction the exercise is designed to produce.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — three problems, one model, and a bill for each rung.
2. **State the objective** — assign requirements to rungs and defend the cost.
3. **Recall prior learning** — supervised fine-tuning from `TSC7-Basic-K8`.
4. **Present the content** — the ladder, LoRA mechanics, replay, schedules, forgetting.
5. **Guide** — walk the law-firm example together.
6. **Elicit performance** — teams place their own requirements on the ladder.
7. **Give feedback** — challenge every escalation and every regression suite.
8. **Transfer** — each learner writes the smallest experiment that would settle their case.

## What the framework doesn't mention but trainers need to know

- **The regression suite is the deliverable, not the model.** Without it you cannot tell improvement from drift.
- **Data quality dominates hyperparameters.** Two hundred clean, consistent examples beat two thousand sloppy ones.
- **Serving cost differs by rung.** Adapters can be hot-swapped; full fine-tunes usually cannot.
- **Continuous pre-training needs legal review of the corpus.** Licence and personal-data questions arrive before the training does.

## Watch out

- **Do not demo a successful fine-tune without showing what got worse.** It builds false confidence.
- **Do not teach LoRA as a magic setting.** Rank and target modules are decisions with consequences.
- **Do not let the class believe pre-training from scratch is achievable.** It is a distractor that eats a whole session if you let it.
- **The stale claim to retire:** "fine-tune on your documents to teach the model your business." In 2026 that is a retrieval problem, and pretending otherwise produces confident wrong answers.
