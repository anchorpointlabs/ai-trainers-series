---
id: 05.02.I.K4
tsc: 5
level: Intermediate
code: K4
title: "Writing the rubric before you look at the output: task-specific criteria"
---

# Writing the rubric before you look at the output: task-specific criteria

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K4**


> **Framework text (verbatim):** "Task-specific evaluation criteria and success metrics."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 4 of 12

**One-line version:** Decide in advance what "good" means for this task, at what point it fails outright, and what result would make you ship — because a criterion invented after seeing the output is a justification, not a test.

## What it is

Task-specific criteria are the dimensions on which output quality is judged for one particular job, each with a weight, an anchor description of what a good and a bad example looks like, and a threshold. Success metrics are the few numbers that decide adoption. Together they turn "is this good enough?" into a decision that two people can reach independently and agree on.

## Deep expansion

### The concept

The Basic-level criteria — accuracy, coherence, diversity, novelty — are universal vocabulary. They are not a rubric. A rubric for *drafting replies to delivery complaints* might score factual grounding in the policy document, completeness of the answer, tone, and whether a next step is offered; accuracy in the abstract would be a poorly specified slice of the first of those.

The reason to fix criteria before looking at outputs is not procedural tidiness. It is that humans are excellent at constructing criteria to fit what they have just seen. Show a manager a fluent, warm, wrong reply and they will start valuing warmth. Write the rubric first and the same reply fails the grounding gate. This is the single most useful discipline in the whole subject, and it costs twenty minutes.

A workable rubric has four parts: dimensions, weights, anchors, and a gate. Most teams write only the first and then wonder why their scores do not predict anything.

### The sub-concepts

**Dimension.** The named property being judged: *grounded in source*, *answers the question asked*, *complies with format*, *appropriate tone*, *actionable next step*, *no unsafe content*. Between four and seven dimensions; more than that and raters start trading off silently.

**Weight.** Some dimensions matter more. Weighting makes the trade-off explicit instead of leaving it to the rater's mood. Weights should sum to something and be visible in the report.

**Gate.** A hard fail that overrides the average. Unsafe content, invented policy, or a wrong price is a gate: no amount of good tone compensates. Gates are how rubrics survive contact with risk officers.

**Anchor.** A description of what level 1, 3 and 5 look like, with a real example attached. "Tone: 3 = polite but generic; 5 = warm, specific to the customer's situation, no blame" is an anchor. "Tone: good" is a wish.

**Threshold from consequence.** The pass mark comes from what happens when the model is wrong: a refund issued in error, a safety instruction missed, a customer annoyed. Two tasks with identical rubrics can have different thresholds because the cost of error differs.

**Coverage of the input space.** The criteria only mean something across a test set that includes the awkward inputs — the complaint written in Singlish, the email with the order number missing, the one with three questions in it. Criteria plus a soft test set equals a good score and a bad deployment.

**The decision rule, written down.** "Adopt if grounded ≥ 95% and no gate failures across 200 samples, at cost below X." Written before the run, it cannot be reverse-engineered afterwards.

### How it connects to the rest of the framework

`TSC5-Intermediate-K1` is the theory that demands a construct; this bullet is the construct made operational. `K2` provides the automatic metrics that stand in for some dimensions, `K3` the charts that show the rubric's results by slice, `K6` the test of whether a gap between two models on a dimension is real. `TSC5-Intermediate-A1` builds the pipeline around the rubric; `A3` uses rubric labels as its failure taxonomy. `TSC5-Basic-K2` is the general version of this skill; `TSC4-Intermediate-*` compares candidate models on rubrics like this one.

### What is current as of November 2026

Rubrics have become executable. Because a judge model can be given the rubric as a policy document, the quality of the rubric is now the main lever on evaluation quality — a vague criterion produces a vague judge and a number that looks precise. Teams increasingly split criteria into what a script can assert (format, required fields, citation present, no banned phrases) and what needs judgement (tone, completeness, helpfulness), and run both. Published domain rubrics for support, summarisation and medical writing are now common starting points, and the good ones ship with anchors rather than dimensions alone.

### Common misconceptions

- *"The criteria are the same for every task."* That is what makes a rubric useless. Grounding matters enormously for a policy question and barely at all for a slogan brainstorm.
- *"We'll know good when we see it."* You will — and what you see will be fluent, which is why the rubric exists.
- *"More criteria means more rigour."* Past seven dimensions, raters stop applying them and start guessing.
- *"The rubric is a formality before the real test."* The rubric *is* the test; the model run is just the data collection.

## How a student should understand it

**Mental model:** the driving test. You are not scored on being a good driver in general; you are scored on specific competencies, and mounting the kerb fails you instantly no matter how smooth the rest of the drive was.

**Three things they can do after this bullet:**
1. Write a five-dimension rubric for their own task, with anchors at 1, 3 and 5.
2. Name the gate — the one failure that cannot be averaged away.
3. State the adoption threshold and the decision rule before any model is run.

**Misconceptions to kill:** criteria are universal, gates are optional, and a high average excuses a catastrophic tail.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The driving test.** Specific competencies, weighted, with instant-fail items. Nobody passes by being "generally good at driving". The instant-fail list is the gate, and every learner already understands why it exists.

**The food-hygiene checklist versus "is the food nice".** Two different instruments for two different questions. The hygiene inspector scores checkpoints and can shut a stall; the customer scores deliciousness and cannot. A rubric that mixes them produces a number that serves neither purpose.

### Worked example with a real tool

Have the room build the rubric against a real artefact, then test it on a real output:

```
I need a marking rubric for AI-drafted replies to delivery-delay
complaints at a logistics SME.

Before writing it, ask me: what happens when a reply is wrong? What tone
do we sign? What must every reply contain?

Then give me:
1. Five dimensions, with weights that add to 100.
2. Anchors at 1, 3 and 5 for each dimension, in one line each.
3. The one gate that overrides the total score.
4. A pass threshold, and the reasoning for it in terms of cost of error.
5. The decision rule I should write down before I test any model.
```

What to point at afterwards: the model will produce a plausible rubric in one pass, and its anchors will be bland ("clear and professional"). Force the room to rewrite two anchors with a real example attached. That rewrite is the skill; generating the skeleton was never the hard part.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a warm, fluent, factually wrong reply and ask the room to score it out of ten.
2. **State the objective** — you will leave with a rubric, a gate and a decision rule for your own task.
3. **Recall prior learning** — the four Basic criteria; ask which one is doing all the work in this task.
4. **Present the content** — dimensions, weights, anchors, gates, thresholds from consequence.
5. **Guide** — build the delivery-reply rubric on the board, anchors and all.
6. **Elicit performance** — each learner drafts a rubric for their own task and scores three real outputs with it.
7. **Give feedback** — compare scores across learners; where two people differ by two points, the anchor is the problem.
8. **Transfer** — they test the rubric against a second model and report where the rubric itself broke.

## What the framework doesn't mention but trainers need to know

- **Agreement is the quality test for a rubric.** Have two people score the same twenty outputs. Disagreement above one point on any dimension means the anchor is underspecified, not that the rater is careless.
- **Judges inherit rubric ambiguity.** A judge model will smooth over vague criteria by inventing an interpretation, and it will do so consistently — which looks like reliability and is not validity.
- **Criteria drift after deployment.** What counts as an acceptable tone moves; so does the policy the reply must be grounded in. Review the rubric on a schedule, and note the version with every score.
- **Write the rubric in the language of the business.** "Grounded in policy" survives a compliance review; "hallucination-mitigated" does not.

## Watch out

- **Do not let the room score outputs before the rubric exists.** The whole lesson is lost in that one shortcut.
- **Do not confuse a rubric with a prompt.** The rubric judges the output; a prompt is how you ask for it. Putting rubric language in the prompt is fine, but it does not replace the independent check.
- **Do not ship a rubric with no gate.** Risk conversations end the moment someone asks what happens when the model is confidently wrong.
- **The stale claim to retire:** "we'll define success metrics after the pilot." After the pilot, the metrics describe what the model happened to do well.
