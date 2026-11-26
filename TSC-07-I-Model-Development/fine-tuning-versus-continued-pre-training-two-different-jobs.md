---
id: 07.02.I.K10
tsc: 7
level: Intermediate
code: K10
title: Fine-tuning versus continued pre-training: two different jobs
---

# Fine-tuning versus continued pre-training: two different jobs

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K10**


> **Framework text (verbatim):** "Intermediate fine-tuning and introduction to continuous pre-training."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 10 of 17

**One-line version:** Fine-tuning changes what the model does; continued pre-training changes what it has read — and most teams asking for the second actually need the first, or a retrieval index.

## What it is

Two stages that learners merge into one word. *Fine-tuning* (supervised fine-tuning, SFT) shows the model labelled input–output pairs and teaches behaviour: format, tone, task, refusals. *Continued pre-training* (CPT, increasingly called mid-training) runs more unsupervised next-token training over a domain corpus, shifting the model's base distribution — its vocabulary, notation and stylistic reflexes. They use different data, different schedules and different risks.

## Deep expansion

### The concept

The distinction is what the gradient is allowed to change. In SFT the model is graded on its *answer*, so it learns the mapping from instruction to response. In CPT the model is graded on predicting the *next token of a document*, so it learns how your domain writes — its abbreviations, structure, register. SFT is fast, cheap and precise; CPT is slow, expensive and diffuse. Choosing wrongly is the most common expensive mistake at this level: CPT on a policy manual does not make the model quote the manual, it makes the model *sound like* the manual and then invent plausible clauses.

### The sub-concepts

**SFT, full or parameter-efficient.** LoRA freezes the base weights and trains small low-rank adapters, which is why it fits on modest hardware and why several adapters can share one base model. QLoRA adds quantisation of the frozen base to cut memory further. Full fine-tuning still wins when the domain gap is large, the output format is unusual, or the base model is small; for most enterprise tasks a well-built LoRA is within reach of a full fine-tune and far cheaper to iterate.

**CPT mechanics.** Unlabelled domain text, next-token loss, a low learning rate with warmup, and — critically — a *replay* mixture of general data (a modest share of the batch) so the model does not forget how to hold a conversation while it learns your notation. New scripts or specialised vocabularies may need the tokeniser extended and the embedding matrix resized, which is a different operation with its own failure modes.

**What each buys.** CPT buys domain fluency: legal shorthand, clinical phrasing, a codebase's conventions, a language the base model handles weakly. SFT buys compliance: answer in this JSON, refuse this category, escalate in this tone. Factual recall is bought by neither reliably — retrieval buys that.

**Risks.** Catastrophic forgetting (measurable: run your general benchmark before and after), absorbing corpus errors and copyrighted text, cost overruns on long schedules, and licence questions about derivative weights.

### How it connects to the rest of the framework

`TSC7-Basic-K8` is the entry-level fine-tuning concept; `TSC7-Intermediate-K5` is the optimisation that keeps these runs stable; `TSC7-Intermediate-K8` builds the datasets; `TSC7-Intermediate-K4` is the metric panel that catches forgetting; `TSC7-Advanced-K10` and `TSC7-Advanced-K11` extend to advanced fine-tuning and preference alignment with RLHF/RLAIF.

### What is current as of November 2026

- **Mid-training became a named stage.** Labs and serious in-house teams describe a three-stage recipe — pre-train, mid-train, post-train — and the GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro / Gemini 4 Argon all show signs of heavy mid-training for context length and modality.
- **Preference tuning is standard after SFT.** The DPO family, and reinforcement learning against verifiable rewards for reasoning, are now the expected third step rather than an optional extra.
- **Parameter-efficient tuning is the default for enterprise.** QLoRA-class setups mean a single workstation-class GPU can produce a usable adapter, which has moved the constraint from hardware to data quality.

### Common misconceptions

- *"Fine-tuning adds knowledge."* It adds behaviour. Ask it for a fact it never saw and you get a confident, well-formatted invention.
- *"CPT is just a long fine-tune."* Different data (unlabelled), different loss (document tokens), different risk (forgetting the base capability).
- *"LoRA only changes style."* It changes behaviour effectively at this scale; what it changes poorly is deep factual knowledge.
- *"More epochs, better fit."* More epochs memorise the training set's phrasing and degrade general capability — the forgetting shows up last.

## How a student should understand it

**Mental model:** SFT is sending a staff member on a three-day course about your claim form. CPT is sending them back to school to relearn the trade's language. Both change the person; only one changes what they know how to say.

**Three things they can do after this bullet:**
1. Decide between prompting, retrieval, SFT and CPT for a stated failure.
2. Design a two-stage recipe with a replay mixture and a forgetting check.
3. Explain why "train it on our documents" is usually the wrong request.

**Misconceptions to kill:** that fine-tuning injects facts, that CPT is a bigger fine-tune, and that adapters cannot change behaviour.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The language school and the SOP.** Sending a new hire to Malay classes (CPT) makes them fluent in the language of the shop floor; handing them the company's claim form with three worked examples (SFT) makes them able to process a claim. Do only the second and they write fluent but wrong claims; do only the first and they are eloquent and still do not know your form. Where it breaks: the new hire can ask a colleague which form applies; the model has nobody to ask, so the missing half is noticed only when an output is wrong.

**Renovating versus rebuilding an HDB flat.** CPT is renovation: you inherit the pipes, the wiring and the neighbours, which is cheap and fast and means some problems are now permanently yours. SFT is buying new furniture: it changes the look without touching the structure. Where it breaks: renovation permits record what changed; continued pre-training usually does not, so the inherited structure is documented only by the checkpoint hash.

### Worked example with a real tool

A learner's model writes plausible but wrong insurance clauses. Type this into a coding assistant:

```
Write a two-stage training script:

Stage 1 (continued pre-training): unsupervised next-token training on
./corpus/*.txt (policy wording, 40MB) using the base model's own
tokenizer, sequence packing at 4096 tokens, lr 1e-5 with 200-step
warmup, and a replay mixture where 10% of each batch is general
web text. Checkpoint every 500 steps.

Stage 2 (SFT): LoRA r=32 on the stage-1 checkpoint using
./sft.jsonl (instruction/response pairs), masking loss on prompts.

Gates: before and after stage 1, run the same 100-item general
capability test and the 50-item clause-extraction test; print both
scores side by side so I can see what stage 1 cost me.
```

Point at the replay mixture (without it, stage 1 trades conversation ability for jargon and nobody notices until demo day), the two gates (CPT without a forgetting measurement is a gamble), and stage 2's masked loss — the model must be graded on the answer, not on repeating the instruction.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a model that sounds like a policy document and invents clauses.
2. **State the objective** — choose the right stage for a failure you actually have.
3. **Recall prior learning** — fine-tuning basics and dataset construction.
4. **Present the content** — SFT versus CPT, replay, forgetting, tokeniser.
5. **Guide** — trace one request ("make it talk like our legal team") to the right stage.
6. **Elicit performance** — teams classify six requests as prompt, retrieve, SFT or CPT.
7. **Give feedback** — debrief; the retrieval cases are the ones teams miss.
8. **Transfer** — each learner writes their recipe with gates named.

## What the framework doesn't mention but trainers need to know

- **Retrieval beats both for facts.** If the requirement is "knows our current prices", an index updated daily wins; a model trained on last quarter's price list is wrong forever.
- **CPT cost surprises people.** Long schedules on domain corpora are measured in GPU-days, and the marginal gain over a good SFT is often small.
- **Forgetting needs a baseline, not a vibe.** Run the general test before stage 1 and keep the report.
- **Adapter licence and base licence differ.** The terms that let you fine-tune a model may not let you redistribute the result.

## Watch out

- **Do not sell fine-tuning as knowledge injection.** It is the single most expensive misunderstanding in enterprise AI.
- **Do not demo CPT without the forgetting gate.** Learners copy the recipe and skip the check.
- **Do not teach "train on our documents" as the answer.** Ask what the failure actually is: format, tone, recall or reasoning.
- **The stale claim to retire:** "fine-tuning is how you add company knowledge." In November 2026 it is how you add company *behaviour*; knowledge lives in retrieval.
