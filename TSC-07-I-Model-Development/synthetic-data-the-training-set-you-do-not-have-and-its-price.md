---
id: 07.02.I.K9
tsc: 7
level: Intermediate
code: K9
title: Synthetic data: the training set you do not have, and its price
---

# Synthetic data: the training set you do not have, and its price

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K9**


> **Framework text (verbatim):** "Synthetic data generation."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 9 of 17

**One-line version:** Synthetic data is a photocopy of what a model already believes — useful, cheap, and blurred a little more with every generation.

## What it is

Synthetic data is training material produced by a model or a simulator rather than collected from the world: generated instruction pairs, simulated dialogue, diffusion-generated images, physics-simulator rollouts, tabular rows sampled from a fitted generator. It exists because real data is often scarce, private, expensive, dangerous to collect, or simply unavailable for the edge case you care about.

## Deep expansion

### The concept

A generator is a compressed summary of its own training distribution, steered by your prompt. Ask it for a thousand examples of a rare failure and you get a thousand plausible variations of what it already associates with that failure. That is genuinely useful — but it means the long tail you were trying to capture is exactly what the generator is worst at. The engineering question is not "can we generate data" but "how do we keep generated data from quietly replacing the world it was supposed to approximate".

### The sub-concepts

**Methods.** *Self-instruct* takes a handful of seed tasks and asks a model to invent more in the same shape. *Evol-Instruct* mutates prompts toward greater difficulty and diversity. *Distillation* turns a stronger model's outputs into a smaller model's training set. For images and audio, diffusion generates the samples; for robotics and driving, simulators generate trajectories with labels for free; for tabular data, fitted generators preserve column relationships without real rows.

**Quality gates.** Diversity (distinct-n, cluster coverage — is every generated batch a variation of three sentences?), label fidelity (does the generated caption actually describe the generated image?), judge screening plus human spot-checks, and a *real-data holdout* that never appears in training. The holdout is the only defence against circular evaluation: if the test set is also synthetic, you are measuring self-consistency.

**Narrowing and collapse.** Training repeatedly on model output erodes the tails of the distribution: rare phrasings, unusual cases and minority styles disappear first. In practice the effect is manageable with a real-data anchor, human-authored seeds, aggressive filtering and a bounded synthetic ratio — but it is real, and it is worst exactly where your product needs to handle unusual input.

**Provenance and law.** Synthetic data derived from personal data is not automatically anonymised: if it can be re-identified, it is still personal data under PDPA. And many model providers' terms restrict using outputs to train a competing model. Both questions arrive before the pipeline does.

### How it connects to the rest of the framework

`TSC7-Intermediate-K8` treats synthetic data as one augmentation source among several; `TSC7-Intermediate-K4` supplies the metrics that must include a real-data holdout; `TSC7-Intermediate-K7` is the bias risk that amplification creates; `TSC7-Advanced-K7` covers advanced generation and its limits; `TSC8` and `TSC9` own the governance and leakage questions.

### What is current as of November 2026

- **Verifiable synthetic tasks won.** Generated examples with checkable answers — code that runs, arithmetic, structured extraction — are trusted because a verifier, not a judge, scores them. Open-ended generation is still screened by models and sampled by humans.
- **Frontier post-training openly relies on it.** The GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro / Gemini 4 Argon are all post-trained on substantial synthetic mixtures, which has made "what ratio of real to synthetic" a normal interview question.
- **Collapse anxiety moderated into mixture engineering.** The conversation moved from "synthetic data destroys models" to "keep an anchor of real data and measure the tails".

### Common misconceptions

- *"Synthetic data is free."* Generation, filtering, deduplication and human spot-checks cost real money; the saving is in collection, not in total effort.
- *"Synthetic data is private by definition."* Only if it cannot be linked back to a person — which is a testable property, not a label.
- *"If the judge approves it, it's good."* The judge shares the generator's blind spots; agreement between them is not evidence.
- *"More synthetic data fixes a weak dataset."* It amplifies whatever the generator already believes, including the gap you were trying to fill.

## How a student should understand it

**Mental model:** practice papers written by the tutor. Excellent for volume, shaped entirely by what the tutor thinks the exam looks like — and if the tutor is wrong about one topic, every paper drills the mistake.

**Three things they can do after this bullet:**
1. Design a generation pipeline with seeds, filters and a real-data holdout.
2. Measure diversity and label fidelity instead of trusting sample eyeballing.
3. State the legal questions before generating anything from customer data.

**Misconceptions to kill:** that it is free, that it is automatically anonymous, and that a judge model is validation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The photocopied recipe.** Photocopy a chicken rice recipe ten times and the tenth copy is legible but blurry — the chilli proportions have drifted. Each generation is a copy of a copy, and the drift is always toward the average. Where it breaks: a photocopy degrades once per copy; a model trained on its own output degrades fastest exactly where the original was least confident.

**The tuition teacher's mock papers.** A tutor who has seen five years of past papers writes excellent mocks. A tutor who has only seen other tutors' mocks writes confident papers about the wrong syllabus. That is a student model trained on a teacher's output without a real exam to check against. Where it breaks: the student can sit one real past paper to test the tutor; a synthetic pipeline with no real holdout never finds out.

### Worked example with a real tool

A learner needs 2,000 extra examples of invoice-extraction requests but has only 200 real ones. Type this into a coding assistant:

```
Build a self-instruct pipeline for invoice extraction:

1. Load 200 real (document, json_answer) pairs as seeds.
2. For each seed, call the model in batches of 10 to produce 10
   variants: different vendor names, currencies (SGD/MYR/USD),
   layouts described, and 2 deliberate edge cases (missing GST
   number, handwritten total).
3. Validate every generated answer against the JSON schema and
   re-extract from the generated document text; discard if the
   answer cannot be verified.
4. Deduplicate by prompt embedding at cosine > 0.95 and report
   how many survive per cluster.
5. Hold out 100 of the 200 real pairs untouched; train only on
   synthetic + the other 100, then evaluate on the real holdout.
```

Point at step 3 — schema-plus-round-trip validation turns generation into something a verifier can check — step 4 (diversity, not volume), and step 5: training on synthetic and testing on synthetic proves nothing at all.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — 200 real examples beating 5,000 synthetic ones on a real holdout.
2. **State the objective** — build a gated generation pipeline with a real anchor.
3. **Recall prior learning** — augmentation and dedup from K8.
4. **Present the content** — methods, gates, narrowing, legal questions.
5. **Guide** — write one seed prompt and inspect ten outputs critically.
6. **Elicit performance** — teams draft their pipeline diagram with gates marked.
7. **Give feedback** — debrief: which gate would catch a drifted generator?
8. **Transfer** — each learner names one dataset in their job that could be augmented.

## What the framework doesn't mention but trainers need to know

- **Evaluation circularity is the default failure.** If no real holdout exists, the reported metric is self-consistency dressed as accuracy.
- **Validation labour is the hidden cost.** Someone must read samples; a pipeline with no human gate drifts for months unnoticed.
- **Mixture ratios need recording.** The real-to-synthetic ratio is a configuration decision that should be in the model card, not in someone's notebook.
- **Generation inherits phrasing.** Models learn the generator's stylistic tics from synthetic text, and that is visible to users long before it shows in metrics.

## Watch out

- **Do not overclaim collapse.** It is real, contested in magnitude, and manageable with anchors — say that, not the dramatic version.
- **Do not validate with the same model that generated.** Use a verifier where possible, a different model second, and humans always.
- **Do not skip provenance.** Which model, which prompt version, which date — without it you cannot reproduce the dataset or defend it.
- **The stale claim to retire:** "synthetic data means we have unlimited data." In November 2026 it means unlimited copies of the same beliefs, which is a different thing.
