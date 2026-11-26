---
id: 07.01.B.K6
tsc: 7
level: Basic
code: K6
title: "Loss functions and metrics: what the training number does and does not tell you"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Loss functions and metrics: what the training number does and does not tell you

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K6**


> **Framework text (verbatim):** "Loss functions and evaluation metrics for generative tasks."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 6 of 15

**One-line version:** The loss is the number the model is optimising; the metric is the number you care about — and the two are never quite the same thing.

## What it is

A loss function is the single number a training run is trying to make small. An evaluation metric is a number you compute afterwards to judge whether the output is any good. For generative tasks the common losses are cross-entropy (for text and anything token-like), reconstruction error (for autoencoders and diffusion) and adversarial loss (for GANs); the common metrics are perplexity, BLEU and ROUGE for text, FID and CLIP-style scores for images, and structured human review for everything that matters.

## Deep expansion

### The concept

Training is an optimisation loop with one objective. The loss function defines that objective precisely, and the model will pursue it with no judgement about whether it is the right objective. This is the most important sentence in the bullet: **whatever you measure, the model will maximise, including the parts you did not intend.**

For a language model the loss is cross-entropy on the next token. At each position the model outputs a probability for every token in the vocabulary; cross-entropy asks how much probability it assigned to the token that actually came next. Assign 99% to the right token and the penalty is tiny. Assign 1% and the penalty is large. Average that over millions of positions and you have a single number that goes down as the model gets better at predicting text.

**Perplexity** is just `exp(loss)`. It reads as "how many equally likely options the model was effectively choosing between". Lower is better, and it is comparable only between models using the same tokeniser — a trap that catches almost everyone once.

Metrics are a different species. BLEU compares your output to a reference translation by counting overlapping n-grams; ROUGE does something similar for summaries, favouring recall; FID compares the statistics of generated images to real ones. Every one of them is a proxy, and every one can be gamed or satisfied while the output is still unusable.

### The sub-concepts

**Cross-entropy.** The default for text. Penalises confident wrong answers hardest.

**Reconstruction loss.** Used by autoencoders and diffusion: how far is the reconstruction from the original. Often paired with a KL term that keeps the latent space well-behaved.

**Adversarial loss.** The GAN game: the generator's loss is the discriminator's confusion. Unstable by construction, which is why GAN training needs careful balancing.

**Perplexity.** Loss in a human-readable unit. Only meaningful within one tokeniser.

**BLEU, ROUGE, METEOR.** Reference-overlap metrics. Cheap, reproducible, and weakly correlated with whether a human finds the output useful.

**FID and CLIP score.** Image metrics. FID measures distributional distance to a reference set; CLIP score measures text-image alignment. Both are proxies for human judgement, not substitutes.

**Validation loss.** The same loss computed on held-out data. The moment validation loss starts rising while training loss falls, you are overfitting, and the run is telling you to stop.

### How it connects to the rest of the framework

`TSC7-Basic-K4` (data preparation) determines whether the loss is honest — duplicates make it artificially low. `TSC7-Basic-K7` (optimisation) is the machinery that reduces it. `TSC7-Basic-K9` (evaluation methodologies) is the fuller treatment of metrics. `TSC5-Basic-K3` and `TSC5-Basic-K4` cover evaluation from the evaluator's seat, and this bullet is the same material from inside the training loop. `TSC7-Basic-A5` (identifying limitations) depends entirely on reading these numbers correctly.

### What is current as of November 2026

The industry has largely stopped treating benchmark overlap as evidence of quality. BLEU and ROUGE survive in academic comparison and regression tests, but practitioners working with the GPT-6 generation, Claude 5.5 or Gemini 4 Argon rely on task-specific evaluations and human or model-assisted review — partly because a strong model can produce a fluent paraphrase that scores badly on n-gram overlap while being obviously better.

Two shifts worth teaching. First, **preference-based evaluation is now standard**: rather than scoring one output, you show two and ask which is better, which is far more reliable than an absolute score. Second, **loss is no longer visible** for closed models — you get outputs and a bill, not a training curve. Basic learners must therefore be able to evaluate without a loss, which is exactly what TSC #5 trains.

### Common misconceptions

- *"Lower loss means a better model."* Lower loss means better at the training objective. If that objective is a proxy, you have optimised the proxy.
- *"Perplexity is comparable across models."* Only with the same tokeniser and the same test set. Otherwise the number is noise.
- *"BLEU 0.4 means 40% good."* It is an n-gram overlap statistic with no percentage interpretation.
- *"If the loss goes down, training is working."* Watch validation. Training loss always goes down; that is what training does.
- *"Metrics replace human review."* They filter. A human still decides.

## How a student should understand it

**Mental model:** the PSLE marking scheme. A rubric can be applied consistently and still reward an essay nobody would publish. The rubric is the loss; the essay is the output; a good teacher reads both.

**Three things they can do after this bullet:**
1. Read a training log and say whether the run is learning, overfitting or stuck.
2. Name one metric per modality and one thing it fails to capture.
3. Explain why you would not compare perplexity across two different models.

**Misconceptions to kill:** that the loss is the goal rather than the proxy, that a metric is a grade, and that a falling training curve means success.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food hygiene grade.** A stall with an A has passed an inspection; it does not mean the char kway teow is good. The grade is real, standardised and useful — and it is not the thing you actually came for. BLEU is that grade.

**The taxi meter.** The meter measures distance travelled. Take a route that maximises the meter and you have optimised the metric while ignoring the passenger's actual need, which is to arrive. Every generative model is a taxi driver that will take the meter-maximising route if you let it.

### Worked example with a real tool

In Colab, compute the two numbers on the same held-out batch and see them move together — until they do not:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
batch = tok(["The stall closes at 9pm because", "Please confirm your"],
            return_tensors="pt", padding=True)

with torch.no_grad():
    out = model(**batch, labels=batch["input_ids"])
print("loss:", out.loss.item(), "perplexity:", torch.exp(out.loss).item())
```

What to point at afterwards: the two numbers are the same information in different clothes. Then generate from the same model and read the text aloud — ask the room whether the perplexity number predicted the quality. It usually does not, and that gap is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a training curve that falls smoothly and a sample output that is nonsense. Ask how both can be true.
2. **State the objective** — by the end you can read a loss curve, name a metric per modality, and say what each one misses.
3. **Recall prior learning** — from TSC #5 they evaluated outputs; now they see the number that produced them.
4. **Present the content** — loss versus metric, cross-entropy, perplexity, BLEU/ROUGE/FID, validation.
5. **Guide** — run the snippet, then generate text and compare the number to the reading experience.
6. **Elicit performance** — pairs write one metric and one failure mode for three tasks: translation, summarisation, image generation.
7. **Give feedback** — correct the pair that says "BLEU 0.6 = 60% correct"; use it to explain n-gram overlap.
8. **Transfer** — each learner names the acceptance test they would use for a model in their own work.

## What the framework doesn't mention but trainers need to know

- **The tokeniser trap is the most common analytic error in the field.** Two models with different vocabularies produce incomparable perplexities. Say it twice.
- **Metrics get gamed once they become targets.** If a team is rewarded on BLEU, BLEU rises and quality may not. This is old news in every measurement discipline and new news in every AI team.
- **Human evaluation needs a rubric, not a vibe.** "Which is better" without criteria produces noise. Teach a three-criterion rubric: correctness, completeness, tone.
- **Closed models give you no loss.** A Basic learner whose only experience is an API may never see a training curve. Make sure the concept lands anyway.

## Watch out

- **Do not present a single metric as the answer.** Show at least two and where they disagree.
- **Do not compare perplexity across model families.** It is the demo that looks clever and is quietly wrong.
- **Do not skip validation loss.** It is the only defence against "the training number looked great".
- **The stale claim to retire:** "BLEU above 0.4 is production-ready." In November 2026 no serious team ships on an n-gram overlap score; it is a regression test, not a release gate.
