---
id: 05.02.I.K2
tsc: 5
level: Intermediate
code: K2
title: "BLEU, Inception Score and FID: what they measure and what they miss"
as_at: 2026-11-26
review_by: 2027-02-25
---

# BLEU, Inception Score and FID: what they measure and what they miss

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K2**


> **Framework text (verbatim):** "Generative AI evaluation metrics and techniques (e.g., BLEU score, Inception Score Frechet Inception Distance)."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 2 of 12

**One-line version:** Three metrics from before the LLM era, still in every paper — each one cheap, reproducible, and blind in a different direction, which is exactly why they are quoted next to a human panel and never instead of one.

## What it is

BLEU, Inception Score and Fréchet Inception Distance are automatic metrics that produce a single number for generated output without a human in the loop. BLEU compares generated text to reference text by n-gram overlap. Inception Score and FID score generated images using the internal features of an image classifier. All three are proxies, all three are still used in reporting, and none of them measures what a business actually cares about.

## Deep expansion

### The concept

Automatic metrics exist because human judgement does not scale. You can run a metric over ten thousand outputs overnight for the price of a little compute; you cannot run a panel over ten thousand outputs before the sprint ends. So the field built cheap instruments, and the discipline at Intermediate level is knowing precisely what each instrument reads — because a metric quoted without its blind spot is a claim, not evidence.

The three named in the framework come from two different traditions and are often confused. BLEU is an *overlap* metric: it asks how much of the reference the candidate reproduces. Inception Score and FID are *distribution* metrics: they ask whether a set of generated images looks statistically like a set of real ones. One compares strings; the other compares clouds of features. Neither compares meaning, and neither knows your task.

### The sub-concepts

**BLEU.** Precision of n-gram matches between a candidate and one or more references, with a brevity penalty so that a model cannot win by emitting three confident words. It is corpus-level, designed for machine translation, and it ranges roughly 0–100 in the form everyone quotes. Its weaknesses are structural: it punishes correct paraphrase, it cannot see word order beyond n-grams, it rewards copying the reference's phrasing even when the copied sentence is wrong, and its value depends on tokenisation, so scores are only comparable within the same implementation. Use sacreBLEU if you must report it, and report the signature.

**Inception Score.** Push generated images through an Inception classifier. Good generations should be *confident* (one class clearly predicted) and *varied across the set* (the marginal distribution over classes is broad). IS is the exponentiated expected divergence between those two. Higher is better. It only knows the thousand classes the classifier was trained on, it rewards images that look like ImageNet photographs, and a set of near-identical but very confident images can score well because it never sees the real data.

**Fréchet Inception Distance.** Extract features from real and generated images with the same network, fit a multivariate Gaussian to each set, and measure the Fréchet distance between them. Lower is better. FID is the more honest of the two image metrics because it compares against the actual data. It still assumes the features are Gaussian, it is biased upward when the sample is small, and it shifts with resizing, compression and feature-extractor version — which is why FID numbers from different papers are not comparable unless the implementation is fixed. For video the same idea appears as FVD.

**The neighbouring metrics you will meet.** ROUGE (recall-oriented, built for summarisation), METEOR, chrF, BERTScore and CLIPScore (embedding similarity, closer to meaning), perplexity (how surprised a model is, not how good the text is), exact match and pass@k for code, and the judge-model score that now dominates text evaluation. Each is a different instrument; none is a general "quality".

**Metric-plus-task-or-nothing.** A metric number has three required companions: the task, the reference set, and the implementation. Drop any of them and the number becomes unfalsifiable.

### How it connects to the rest of the framework

`TSC5-Intermediate-K1` argues every score is a proxy; this bullet is the concrete case. `TSC5-Basic-K2` supplies the criteria these metrics are (badly) proxying — accuracy, diversity, coherence, novelty. `TSC5-Intermediate-K3` is how you show what a scalar hides; `K6` is how you decide whether a two-point difference is real; `A2` is the distributional reading these metrics flatten. On the model-building side, `TSC7-Basic-K6` covers loss functions and generative metrics from the training perspective — same numbers, different job.

### What is current as of November 2026

BLEU survives in translation and summarisation reporting but is rarely quoted alone; learned metrics (COMET-style for translation, BERTScore for general text) and pairwise judge preferences have taken over text quality. FID and FVD remain the default for image and video generation papers and remain criticised for exactly the reasons above — practitioners now fix sample size and implementation and report FID alongside a human or model-based preference measure. The bigger shift is that **the headline metric for text is now a judge**, which moves the blind spot from "does not understand meaning" to "inherits the judge's biases". The metric did not get objective; the bias moved.

### Common misconceptions

- *"BLEU of 40 means the output is 40% correct."* BLEU is not a percentage of correctness. It is an overlap statistic with no absolute meaning.
- *"Lower FID always means a better image model."* Across papers with different preprocessing and sample sizes, FID is not comparable at all.
- *"These metrics are obsolete, so ignore them."* They are cheap, reproducible and useful as regression detectors on a fixed test set — the mistake is treating them as quality.
- *"IS and FID measure the same thing."* IS reads confidence and variety without seeing real data; FID reads distance from real data. They can move in opposite directions.

## How a student should understand it

**Mental model:** three old instruments on a lab bench — a ruler, a thermometer, a set of scales. Each is precise, each measures one thing exactly, and none of them tells you whether the experiment worked.

**Three things they can do after this bullet:**
1. State what each of the three metrics computes, in one sentence, without a formula.
2. Name the blind spot of each before quoting a number from it.
3. Refuse a metric comparison that does not fix the task, the reference set and the implementation.

**Misconceptions to kill:** overlap equals meaning, FID is comparable across papers, and a metric number is a quality verdict.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Marking comprehension by matching the model answer.** A teacher with a marking scheme that rewards the exact phrases in the model answer will give full marks to the script that copies the phrases and half marks to the script that says the same thing in the child's own words. That is BLEU, faithfully. Breaks where the teacher can read for meaning and BLEU cannot.

**The food-hygiene grade.** A stall can hold an A and still serve mediocre char kway teow; the grade measures a checklist of hygiene checkpoints, not deliciousness. IS is that grade for images — a narrow instrument, honestly reported, widely mistaken for a quality rating.

### Worked example with a real tool

Paste two candidate summaries and one reference into ChatGPT or Claude:

```
REFERENCE: The port will close two berths from 3 to 9 June for dredging.
Container ships above 8,000 TEU will be diverted to the western terminal.
Feeder services are unaffected.

CANDIDATE A: Dredging work will shut two berths at the port between 3 and
9 June. Bigger container vessels will move to the western terminal, while
feeder services carry on as normal.

CANDIDATE B: The port will close two berths from 3 to 9 June for dredging.
Container ships above 8,000 TEU will be diverted to the western terminal.
Feeder services are unaffected, and all berths reopen on 10 June.

Rank these two for usefulness. Then tell me which one BLEU would score
higher, and why that ranking is wrong.
```

What to point at afterwards: B copies the reference's exact phrasing and adds one fact the reference never stated, so it wins on n-gram overlap while being the less trustworthy summary. A paraphrases correctly and loses. Overlap and meaning are different measurements, and this thirty-second demo lands harder than any explanation of the formula.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two outputs where the worse one scores higher on an automatic metric.
2. **State the objective** — you will name what each of the three metrics reads, and what it cannot see.
3. **Recall prior learning** — the four Basic criteria; ask which metric maps to which.
4. **Present the content** — overlap versus distribution; BLEU, IS, FID; the three companions every number needs.
5. **Guide** — work the two-summary example together and let the room argue about the ranking.
6. **Elicit performance** — pairs write a one-line "what this metric cannot see" for each of the three.
7. **Give feedback** — correct "BLEU measures accuracy" and "FID measures realism" into precise statements.
8. **Transfer** — learners write the metric clause for their own evaluation plan, including the implementation note.

## What the framework doesn't mention but trainers need to know

- **Implementation is part of the number.** Two teams computing FID on the same model can differ by more than the gap between two models. Pin the tool, the version and the sample size in the report.
- **Per-sentence BLEU is noise.** BLEU is defined at corpus level; averaging per-sentence BLEU is a common and meaningless practice.
- **Reference quality sets the ceiling.** If the references are mediocre, a perfect model cannot score well — and a model can learn to imitate mediocre references.
- **Learned metrics need calibration to your domain.** BERTScore and CLIPScore are closer to meaning but still need a check against human judgement on your own data before you trust the ranking.

## Watch out

- **Do not teach the formulas in depth.** At Intermediate level the learner needs the reading, not the derivation; the derivation belongs to postgraduate research.
- **Do not let anyone quote a number they did not compute.** "I read that this model gets FID 4.1" is a citation of someone else's pipeline.
- **Do not present the judge model as the modern replacement.** It replaced the *blind spot*, not the need for a panel.
- **The stale claim to retire:** "BLEU is outdated, nobody uses it." Plenty of translation and summarisation reporting still uses it, and knowing why it fails is the skill — not knowing that it exists.
