---
id: 05.01.B.K2
tsc: 5
level: Basic
code: K2
title: The four fundamental evaluation criteria: accuracy, diversity, coherence, novelty
as_at: 2026-11-26
review_by: 2027-02-25
---

# The four fundamental evaluation criteria: accuracy, diversity, coherence, novelty

> **TSC #5 Generative AI Model Evaluation · Basic · Knowledge K2**


> **Framework text (verbatim):** "Fundamental evaluation criteria for generative AI (e.g., accuracy, diversity, coherence, novelty)."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Knowledge · Bullet 2 of 11

**One-line version:** Evaluating a generative model is not "is it good?" — it is four separate questions asked one at a time, because a model can be great on one and terrible on another.

## What it is

Generative AI output is judged on four distinct criteria: accuracy (is it factually right), coherence (does it hang together logically), diversity (does it produce a range of genuinely different outputs), and novelty (does it produce something new rather than regurgitating its input). Each answers a different question, and no single score can stand in for all four.

## Deep expansion

### The concept

The framework's four criteria exist because "good output" is not one thing. A model can be *accurate* but *boring* (correct and identical every time), or *diverse* but *incoherent* (many different answers, none of them logical). A learner who evaluates on a single gut feeling will miss the exact failure the model is exhibiting. The discipline of evaluation is the discipline of separating these four so that a fix can be aimed at the right one.

### The sub-concepts

**Accuracy.** Does the output match the facts, or match a correct reference answer? For factual tasks this is the non-negotiable. For creative tasks it matters less. The failure mode is hallucination — confident, fluent, wrong.

**Coherence.** Does the output hold together — logical flow, no self-contradiction, correct references from one sentence to the next? A model can be factually correct and still incoherent, the way a list of true facts is not yet a report.

**Diversity.** Given the same prompt many times, does the model produce genuinely different outputs, or the same one reworded? Diversity matters for brainstorming and creative work; it is also a warning sign when a model *can't* vary — a sign of mode collapse or over-alignment.

**Novelty.** Does the output add something that was not in the prompt or the training data, rather than echoing the input back? Novelty is the difference between "summarised my words" and "gave me an idea I did not have."

### How it connects to the rest of the framework

These four are the home base. `TSC5-Intermediate-K2` (BLEU, Inception Score, FID) is how these four get *measured with numbers* at Intermediate level; `TSC5-Basic-K4` (limitations) is what accuracy looks like when it fails; `TSC5-Basic-A2` (interpret metrics) is the ability half of this same bullet. The four criteria also quietly connect to `TSC2-Basic-K2` — *how prompts shape content* — because the prompt largely decides which of the four you are even asking for.

### What is current as of November 2026

Two shifts matter. First, **accuracy has become the dominant workplace criterion** — in most Singapore offices the model is doing summarisation, extraction and Q&A, where a fluent-but-wrong answer is the worst possible outcome, so accuracy (and its close cousin *faithfulness* to source) now dwarfs the others in practical importance. Second, **diversity is the criterion that over-alignment quietly kills** — the late-2026 generation of heavily safety- and preference-tuned models can fall into repetitive, samey outputs, which is exactly why the framework keeps it on the list even though most business users never think to measure it.

### Common misconceptions

- *"Accuracy and coherence are the same thing."* A model can state true facts in a jumbled, contradictory order. They are separate checks.
- *"Diversity means the model is unreliable."* Sometimes. But for brainstorming, high diversity *is* the requirement — you want twenty different angles, not one answer twenty times.
- *"If the output is new to me, it is novel."* Novelty means new *to the model's own pattern*, not new to the reader. A model can echo the prompt's phrasing and still surprise a learner who has not noticed.
- *"One overall score is fine."* It never is — the four trade off against each other, and an average hides which one broke.

## How a student should understand it

**Mental model:** a car review. "Is it a good car?" is four questions — is it reliable (accuracy), does it drive smoothly (coherence), does it come in configurations that fit different people (diversity), and does it do anything the competitors don't (novelty). No one reads a review that just says "it's good."

**Three things they can do after this bullet:**
1. Take any model output and tag which of the four criteria it fails on, using the right word (not just "bad").
2. Explain why a model can be accurate but not novel, using a real example from their own work.
3. State which criterion matters most for a given task *before* generating anything.

**Misconceptions to kill:** accuracy = coherence, "one overall score is fine", and diversity = unreliability.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The PSLE composition.** The framework's own example. A teacher does not mark an essay with a single "good" — she checks content (accuracy: are the facts right), flow (coherence: does it hang together), that each child wrote something different (diversity: no two essays should be identical), and originality (novelty: is there a fresh idea or is it memorised). Four columns on the same mark sheet. The moment you frame it this way, every learner in a Singapore classroom already knows how to do it.

**The durian stall.** Accuracy is whether the fruit is actually ripe; coherence is whether the flesh is whole or mush; diversity is whether the stall offers Mao Shan Wang *and* D24 *and* XO; novelty is the stall that serves durian in a way you have not seen. All four, one fruit.

### Worked example with a real tool

Ask any model to write two short product slogans for a single SME, twice, and compare. In ChatGPT or Claude:

```
Write two short marketing slogans for a neighbourhood bakery in Toa Payoh.

Now write two more — make them as different as possible from the first two.
```

What to point at afterwards: the first two show you the model's *default* range (diversity), the second two test whether it can be pushed wider (novelty under instruction). Check the slogans for factual sense (accuracy — do they describe a bakery, not a barber?) and for whether each one stands alone (coherence). Four criteria, one exercise, two minutes.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two outputs: one fluent-but-false, one true-but-jumbled. Ask which is "better".
2. **State the objective** — you will name the four criteria and apply them to any output.
3. **Recall prior learning** — they already mark work (compositions, reports); ask what columns they use.
4. **Present the content** — define the four, one line each, with the PSLE mark-sheet framing.
5. **Guide** — mark one shared output together, tagging each criterion pass or fail.
6. **Elicit performance** — each learner generates one output and marks it on all four.
7. **Give feedback** — correct wrong tags (the learner who says "incoherent" when they mean "inaccurate" is the common one).
8. **Transfer** — learners bring tomorrow's real task and state up front which criterion it needs most.

## What the framework doesn't mention but trainers need to know

- **Accuracy and faithfulness are cousins, not twins.** The framework says "accuracy"; practitioners increasingly care about *faithfulness* — does the output stay true to the source document it was given. At Basic level, fold faithfulness into "accuracy against the source" without a new word.
- **The four criteria conflict.** Push diversity up and coherence can drop; optimise novelty and accuracy often suffers. Teach the trade-off, not the checklist.
- **Most learners will never see a numeric score for these.** They will judge by eye. So the deliverable skill is *labelling* a failure with the right criterion, not computing a metric — that is Intermediate.

## Watch out

- **Do not reduce this to "accuracy is what matters".** That flattens the framework into one column and quietly deletes creativity work. Name all four every time.
- **Do not invent example scores.** Do not say "this model scored 92% coherence" — at Basic level there is no number to point at, and a fabricated statistic will be quoted back at you.
- **The stale claim to retire:** "you can't measure quality, it's all subjective." The four criteria *are* the measurement — subjective at Basic (human judgement) and quantified at Intermediate (BLEU, FID). What you cannot do is collapse it into one number and call it a day.
