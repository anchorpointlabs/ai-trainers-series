---
id: 03.03.A.K7
tsc: 3
level: Advanced
code: K7
title: Fine-tuning on a RAG knowledge base
---

# Fine-tuning on a RAG knowledge base

> **TSC #3 Prompt Engineering · Advanced · Knowledge K7**

> **Framework text (verbatim):** "Modification of model configurations to optimise output (e.g., use of fine tuning based on RAG knowledge base)."
>
> **TSC #3** Prompt Engineering · **Advanced** · Knowledge · Bullet 7 of 13

**One-line version:** Fine-tuning changes how the model answers; retrieval changes what it has read — and "fine-tuning on a RAG knowledge base" means using your retrieved corpus to teach the first, not to store the second.

## What it is

This bullet is about changing the model rather than the prompt: adjusting configuration, up to and including training the weights on your own data. The phrase "based on RAG knowledge base" is the interesting part, and it is read two ways. The wrong way: pour the documents into the weights so the model "knows" them. The workable way: use question–answer pairs generated and verified over your corpus — retrieved chunks, hard negatives and all — as training data, so the model learns to read *your kind of evidence* and answer in *your house form*.

## Deep expansion

### The concept

Weights and window are different memory. **Fine-tuning** runs a training job that produces new weights; the behaviour is baked in and travels with the model. **Retrieval** puts text in the window at answer time; nothing is learned and the next call starts clean. Everything else in this bullet follows from that split.

The practical rule trainers should give — and repeat — is: *fine-tuning is for form, retrieval is for facts.* A tuned model can adopt a register, a structure, a classification taxonomy, a house vocabulary, a refusal style. It cannot reliably reproduce a clause verbatim, cannot forget a superseded policy on request, cannot enforce who may see which paragraph, and cannot cite a page. Weights compress lossily; that is what they are for. Facts that change, that must be quoted exactly, or that must be permissioned belong outside the model.

So what does "fine-tuning on a RAG knowledge base" buy? Three things. It teaches the model to answer *from supplied context* rather than from memory — including ignoring plausible-but-wrong chunks, which is a skill, not a default. It compresses the instructions: a prompt that needed fifteen hundred tokens of rules can become a fifty-token request because the format is now habitual. And it makes a small, cheap model perform a narrow task at a level that previously required the largest available one.

### The sub-concepts

**Retrieval-augmented fine-tuning (RAFT).** Train on examples of the form: question, a set of retrieved passages where some are distractors, and an answer that cites the right one — plus examples where the answer is absent and the correct response is to abstain. The model learns the reading discipline your pipeline needs, which is exactly where untuned models fail.

**Data is the constraint, not the algorithm.** A few hundred to a few thousand verified pairs, consistent in format, drawn from real questions. A hundred careful examples beat ten thousand scraped ones; contamination and inconsistent formatting teach the model your mistakes.

**Catastrophic forgetting is real.** Training hard on one narrow distribution can degrade general capability. Hold out a general test set alongside the domain one and compare before and after, or you will ship a specialist that cannot do anything else.

**Configuration is part of the bullet too.** Temperature, output limits, system-prompt defaults and tool permissions are all "model configuration". Turning temperature down for a factual workflow is a legitimate optimisation and costs nothing.

**Evaluate on held-out data.** Score the tuned model against the untuned model *plus retrieval* on the same test set. If the tuned model wins only when retrieval is removed, you have taught it to memorise, which is the failure mode you were trying to avoid.

**Both, in the right order.** The mature pattern is: retrieval supplies the facts, fine-tuning supplies the reading behaviour and the format, and the prompt stays small. Prompt engineering does not disappear; it becomes the thin layer that states this request's specifics.

### How it connects to the rest of the framework

Bullet 5 (`TSC3-Advanced-K5`) is the retrieval half of this contrast; Bullet 1 (`K1`) is the decision order that places fine-tuning last; Bullet 9 (`A3`) supplies the evaluation that tells you whether it worked. `TSC4` covers choosing a model to tune, and `TSC7` covers the training work itself. The one-line rule to carry across all of them: form into the weights, facts into the window.

### What is current as of November 2026

- **Parameter-efficient tuning is the default.** Adapting a model without retraining all of it is routine, which lowered the cost of the narrow-task case considerably.
- **Distillation became the common commercial motive.** A large frontier model — in late 2026 the GPT-6 generation, Claude 5.5 line, Gemini 3.1 Pro or Gemini 4 Argon — generates high-quality examples; a small tuned model learns to reproduce the behaviour on your task at a fraction of the cost per call.
- **Tuning is a product feature, not a research project.** Mainstream providers offer hosted tuning; the limiting factor moved from engineering to data curation and evaluation.
- **What did not change: the facts rule.** Tuned weights still cannot be edited clause by clause, audited, or permissioned. Every year someone tunes a model on policy PDFs and is surprised in month three.

### Common misconceptions

- *"Fine-tune on our documents so it memorises the policies."* It will produce plausible paraphrases with invented numbers, cannot forget the old version, and cannot cite. Use retrieval.
- *"Fine-tuning always beats RAG."* It costs more, iterates slower, goes stale and cannot be permissioned. It wins on form and on cost per call at volume, not on knowledge.
- *"More data fixes a weak result."* More inconsistent data teaches inconsistency. Fix the example quality and the task definition first.
- *"Once tuned, we do not need prompts."* You need a smaller prompt. The request still has to say what this call wants.
- *"Tuning is a one-off project."* It is a maintenance commitment: the corpus changes, the questions change, and the model needs re-tuning or re-evaluation on a rhythm.

## How a student should understand it

**Mental model:** sending a staff member to a six-month course versus handing them the current SOP folder. The course changes how they write and think; the folder tells them today's rules. You do not re-send someone to a six-month course every time a policy changes.

**Things they can do after this bullet:**
1. Distinguish weight changes from context injection, with a workplace example of each.
2. Decide, for three scenarios, whether to retrieve, tune, both, or neither.
3. Describe the training data a RAG-based tuning job would need.

**Misconceptions to kill:** that tuning stores facts; that tuning replaces retrieval; that data volume substitutes for data quality.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Night class versus the open binder.** Sending a clerk for a diploma in company letter-writing changes how they write for years and costs months. Updating the binder on the desk takes an afternoon. When the circular changes on Monday, you update the binder. Where it breaks: a person retains judgement and can ask; a tuned model has no way to flag that its training is out of date.

**The recipe versus the supplier list.** A chef trained in a cuisine keeps the technique even when suppliers change. The supplier list is checked each morning. Where it breaks: technique in a model is statistical, not deliberate — it will apply a learned format to the wrong facts without noticing.

### Worked example with a real tool

```text
You are deciding between RAG and fine-tuning for a clinic's SOP chatbot.
List one reason to use RAG alone, one reason fine-tuning alone would fail,
and one case where you would use both.
```

A good answer: RAG alone because the SOP changes quarterly and must be quoted exactly with a section reference; fine-tuning alone fails because retraining per policy revision is slower than re-indexing and the model would paraphrase dosages; both when the clinic also wants a fixed triage format and a consistent tone, and the volume justifies compressing the prompt. Point at the third answer: it is the realistic one, and it is the one learners skip because it sounds like hedging.

Then show a single training row for the RAFT pattern — question, two retrieved passages (one relevant, one about a different clinic), and an answer that cites the first and abstains on a follow-up — so the pattern is concrete rather than abstract.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask what happens when the policy changes the week after you "taught" the model your documents.
2. **State the objective** — separate form from facts, and choose between retrieval, tuning and both with reasons.
3. **Recall prior learning** — how the organisation onboards a new staff member versus how it distributes a revised circular.
4. **Present the content** — weights versus window; the form/facts rule; RAFT; the data and evaluation requirements.
5. **Guide** — work the clinic scenario together; then walk one RAFT training row.
6. **Elicit performance** — three scenarios per pair: tune, retrieve, both. Each needs a cost and a staleness argument.
7. **Give feedback** — debrief. Most groups choose tuning for facts; correcting that is the lesson.
8. **Transfer** — each learner writes the one-sentence rule for their team and where it should be documented.

## What the framework doesn't mention but trainers need to know

- **Tuning has an iteration cost the classroom hides.** A prompt change takes a minute; a tuning run takes hours plus evaluation. Workflows that change weekly cannot be tuned weekly — and you still need retrieval afterwards, because the pipeline does not shrink, only the prompt.
- **Evaluation must be held-out and paired.** Compare tuned-plus-retrieval against untuned-plus-retrieval on the same cases, or the result is uninterpretable.
- **Configuration tuning is the cheap win.** Temperature, output length, tool permissions and system defaults often deliver more than a training run, and learners overlook them because they are not exciting.
- **Nobody owns the dataset until someone is named.** Tuning data decays like any other asset; without an owner it becomes a snapshot of last year's process.

## Watch out

- **Do not imply tuning is a weekend job.** The plumbing is easy; the data curation and evaluation are what take the time.
- **Do not let "fine-tuning" become a synonym for "make it better".** Name the mechanism and the trade every time.
- **Do not demo a tuned model without the untuned baseline.** Without the comparison, the improvement is a story, not a result.
- **Do not skip the failure mode.** Show the invented dosage or the superseded clause — the room remembers the failure, not the architecture diagram.
- **The stale claim to retire:** "fine-tune it on all your PDFs and it will know everything." That is the misconception this bullet exists to kill.
