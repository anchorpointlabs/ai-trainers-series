---
id: 05.01.B.A4
tsc: 5
level: Basic
code: A4
title: Identify limitations and potential biases in generative models
as_at: 2026-11-26
review_by: 2027-02-25
---

# Identify limitations and potential biases in generative models

> **TSC #5 Generative AI Model Evaluation · Basic · Ability A4**


> **Framework text (verbatim):** "Identify limitations and potential biases in generative models."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Ability · Bullet 10 of 11

**One-line version:** Knowing a model has limits is not enough — the skill is catching the limit *in a live output*, by probing for bias instead of waiting to notice it, and by checking every claim against what the model was actually given.

## What it is

This is the ability to look at a model's actual output and spot where it is limited or biased — not in theory, but in front of you. It means actively probing for bias rather than passively hoping to notice it, checking claims against the source material, and asking what the model assumed and what it silently left out. The output is a list of *specific* limitations and biases found in a *specific* generation.

## Deep expansion

### The concept

Bias and limitation are invisible in normal use — they are only visible when you look for them. A biased model does not print "WARNING: BIAS"; it produces output that looks normal and quietly reflects the bias in its training data. The ability is therefore a *scanning* discipline, not a noticing one: run the checks every time, because the failure is designed to look like success. Detection methods, applied deliberately, turn "I hope it is not biased" into "I checked and here is what I found."

### The sub-concepts

**The counterfactual probe.** The single most powerful Basic-level bias test: take the same prompt and swap one protected attribute — a name, a gender, an age, a dialect — and watch whether the output changes. If "John" and "Mei Ling" get materially different treatment for the same facts, you have found bias. It is cheap, immediate, and needs no statistics.

**The source check.** Does every factual claim trace back to something you actually gave the model, or something you can verify? A claim with no source is a candidate hallucination — a limitation, not a fact.

**The assumption scan.** What did the model assume that was not stated? That the doctor is male, that the borrower is high-income, that the customer speaks English? Assumptions are where unstated bias hides.

**The omission check.** What did the model *not* say? A summary that drops the one caveat, the one risk, the one minority viewpoint, is biased by omission — and omission is the easiest bias to miss because there is no wrong sentence to point at.

### How it connects to the rest of the framework

This is the ability that operationalises `TSC5-Basic-K4` (limitations) — K4 is *knowing* the limits exist, A4 is *finding* them in a live output. It is the hands-on half of `TSC5-Basic-K5` (human judgement), because the probe is how you correct for your own fluency bias. It also feeds `TSC5-Basic-A5` (identify ethical concerns), which is the ethics-specific version of the same scanning habit.

### What is current as of November 2026

The bias has shifted from *obvious* to *subtle*. Late-2026 models no longer produce the crude stereotypes that earlier generations did — instead, bias shows up as differential *quality*: the model is slightly more careful, more respectful, or more accurate for one group or dialect than another. That makes the counterfactual probe more important, not less, because the failure is now a difference in tone and reliability rather than an overt slur. The other shift: **Singapore's multilingual reality is the test bench** — a model that is excellent in English and weak in Tamil or Singlish is exhibiting a limitation that most global benchmarks never measure.

### Common misconceptions

- *"I would notice bias if it were there."* Bias is invisible precisely because it is plausible. It is found by probing, not by noticing.
- *"If the model is polite, it is not biased."* Politeness can *be* the bias — a model that is warm and careful with one group and terse with another.
- *"Bias means the model is bad or broken."* Bias is inherited from training data and affects every model. Identifying it is routine evaluation, not an accusation.

## How a student should understand it

**Mental model:** a food inspector who does not wait to get sick — she tests the dish for what she cannot taste. A model's bias is the contaminant you cannot see; the probe is the test that reveals it.

**Three things they can do after this bullet:**
1. Run a counterfactual probe on one model output — swap a name or gender — and report whether the output changed.
2. Check one factual claim in an output against its source, and flag it as hallucinated if it does not trace back.
3. Name one assumption and one omission in a given output.

**Misconceptions to kill:** "I'd notice it", polite = unbiased, and bias = broken model.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The job interviewer who has a type.** Two candidates with identical CVs, different names and photos, and the interviewer just "feels better" about one. Nobody wrote a rule that says "prefer this group" — the preference is baked in and invisible. The only way to find it is the controlled test: same CV, change the name, watch the reaction change. That is the counterfactual probe, and it is exactly what you run on a model.

**The exam paper that only some students can read.** If a question is written in a way that assumes a particular background, students without that background fail it silently — not because they are less able, but because the question was biased. A model's output can assume the same things; the omission check is looking for the background it quietly assumed.

### Worked example with a real tool

Run the counterfactual probe live. Give the same facts, change only the name, and compare:

```
Write a one-paragraph performance review for a project manager,
given these facts: delivered late twice this year, but each delay
was caused by a supplier. The manager's name is [Alex / Priya].
```

What to point at afterwards: run it with "Alex" and again with "Priya" (or any two names that differ only in the attribute you are testing). If the two paragraphs differ in tone — one framed as "diligent under difficult circumstances", the other as "needs to manage vendors better" — the model has just demonstrated bias, and the room has just performed a real detection. Then add the omission check: did the review mention the supplier-caused delays at all, or silently blame the manager?

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run the Alex/Priya probe live before saying a word; let the room see the two paragraphs differ.
2. **State the objective** — you will scan any output for limitations and bias using four checks.
3. **Recall prior learning** — they know the limitations (K4) and their own judgement biases (K5); the probe defeats both.
4. **Present the content** — counterfactual probe, source check, assumption scan, omission check.
5. **Guide** — run one probe and one source check together on a shared output.
6. **Elicit performance** — each learner probes one output and reports what they found.
7. **Give feedback** — confirm the real findings, and point out the "bias" calls that were actually just neutral outputs (false positives happen too).
8. **Transfer** — on their next AI task, they run the counterfactual probe before trusting the output.

## What the framework doesn't mention but trainers need to know

- **False positives are part of the skill.** Not every difference between two probes is bias — some are chance or wording. The learner needs to distinguish "consistent, systematic difference" from "one-off variance". Teach them to probe more than once.
- **Omission bias is the one everyone misses.** There is no wrong sentence to point at, so it goes unnoticed. Train the question "what did it *not* say that it should have?"
- **Multilingual performance is a limitation to test in Singapore.** Standard English vs Tamil vs Singlish is a real, measurable limitation gap in most global models. It is the most locally relevant probe a Singapore classroom can run, and it doubles as model-selection evidence.

## Watch out

- **Do not teach learners to hunt for bias with a hammer.** The goal is accurate detection, not confirmation — a learner who *wants* to find bias will find it everywhere, including where it is not. Teach the controlled probe and the false-positive check.
- **Do not present the counterfactual probe as proof.** One swapped name showing a difference is a *signal* to investigate, not a verdict. Say "this warrants a closer look", not "this model is biased."
- **The stale claim to retire:** "modern models don't have bias problems anymore." The bias got subtler, not rarer — and a model that is politely biased is harder to catch, which makes the probe more necessary, not less.
