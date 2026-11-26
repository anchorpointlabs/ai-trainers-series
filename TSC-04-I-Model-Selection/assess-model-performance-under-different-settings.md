---
id: 04.02.I.A5
tsc: 4
level: Intermediate
code: A5
title: Assess model performance under different settings
as_at: 2026-11-26
review_by: 2027-02-25
---

# Assess model performance under different settings

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A5**

> **Framework text (verbatim):** "Assess model performance under different settings."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Ability · Bullet 10 of 11

**One-line version:** Half of what people call model quality is a settings decision — so test the setting before you blame the model.

## What it is

Performance is not a fixed property of a model; it is a property of a model under a configuration. Temperature, output length limit, sampling cut-offs, the prompt itself, and whether reasoning is enabled all move the result. Assessing performance means holding the task constant, changing one setting at a time, and comparing outputs against a criterion you wrote down first.

## Deep expansion

### The concept

The final layer of a language model produces a score for every token in its vocabulary. A softmax turns those scores into probabilities. Sampling decides which token actually gets picked. **Temperature** scales the scores before that conversion: near zero it flattens everything except the winner, making the choice nearly deterministic; above one it raises the odds of less likely tokens, buying variety at the cost of accuracy.

That single mechanism explains most observed behaviour: why an extractor is steadiest at the bottom of the range, why a brainstorm improves as you raise it, and why a compliance summary at high temperature can quietly change a figure.

Assessing performance then becomes a controlled experiment. Same task, same inputs, one setting changed, criterion fixed in advance, results recorded. Without the criterion, the comparison degenerates into picking the output you preferred.

### The sub-concepts

**Temperature: the variance dial.** Low values for extraction, classification, summarisation destined for review, and anything you will diff against a previous run. High values for ideation, variants and creative drafting. In between for conversational use, where a little variation reads as natural.

**Nucleus and top-k: the tail filters.** They trim the improbable tail so the model cannot wander into nonsense. Set them, then leave them alone unless you have a specific reason; adjusting three dials at once makes the result unattributable.

**Output length limit: a budget with a cliff.** Too low truncates mid-sentence and mid-schema. Too high invites padding. For structured output, set it just above the expected maximum.

**Reasoning modes: a setting with a price.** Enabling extended reasoning improves multi-step accuracy and costs latency and tokens. For extraction or rewriting, it is money spent for nothing.

**Repeat runs, not single runs.** One output at one setting is an anecdote. Five outputs at each setting tells you the spread, and the spread is what determines whether the setting is viable in production.

**Fair comparison hygiene.** Identical inputs, identical instructions (adapted only where a model family requires its native format, and noted when you do), recorded settings, and a criterion written before you look.

### How it connects to the rest of the framework

`TSC4-Intermediate-K4` is the handling discipline this measurement depends on — recording what you changed. `TSC4-Intermediate-A6` is the model-variant version of the same experiment. `TSC4-Intermediate-A4` supplies the quality and coherence criteria you score against. `TSC4-Advanced-A3` is the same discipline sustained over time, where settings and versions both drift.

### What is current as of November 2026

With current frontier models, settings work has changed shape:

- **Reasoning effort became a selectable setting, not a hidden property.** You now choose between a fast answer and a deliberated one, with materially different latency and token cost. It belongs in the same test harness as temperature.
- **Some platforms hide sampling parameters behind defaults.** Where temperature is not exposed, prompt structure and reasoning mode become the controllable variables — which makes recording the prompt version even more important.
- **Determinism remains aspirational.** Even at the floor of the temperature range, batching and floating-point arithmetic can flip near-tied tokens, so a pinned setting is "highly consistent", not "identical".

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Temperature zero gives the same output every time."* It maximises consistency. It does not guarantee identity.
- *"Settings are advanced features."* They are the difference between a tool that feels random and one that is dependable.
- *"Higher quality means higher temperature."* Higher temperature means more variety. For most enterprise tasks variety is a defect.
- *"We tested it once and it was fine."* You tested one sample from a distribution.

## How a student should understand it

**Mental model:** a camera's exposure triangle. Change aperture alone and you learn what aperture does. Change three dials and you have a photo and no knowledge.

**Things they can do after this bullet:**
1. Run the same task at two settings and describe the difference in variance, not just in wording.
2. Pick a defensible setting for extraction, for drafting and for chat, with a reason for each.
3. Design a fair comparison: same inputs, one change, criterion fixed first.

**Misconceptions to kill:** that one run is a result, that temperature equals quality, and that settings can be tuned by feel.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The aircon remote.** Fan speed, temperature, swing. Change one and wait; change three and you cannot tell what did what.

**The karaoke volume.** At low volume the song is the same every time you sing it. Turn it up and you start improvising — sometimes brilliantly, usually not.

### Worked example with a real tool

Run the same creative task at two settings and compare, then change the task type and watch the conclusion invert:

```text
Task 1 (creative): "Write three taglines for a new bubble tea shop
in Jurong East." Run at temperature 0.2, then 0.9. Which gave more
varied output, and which was steadier?

Task 2 (extraction): "Extract the total amount and the due date from
this invoice: [paste]. Return JSON only." Run at 0.9 five times,
then at 0.2 five times. Which setting would you ship?
```

What to point at afterwards: for taglines the high setting wins and the low setting produces three near-identical lines. For extraction the high setting occasionally reorders a date into American format or adds conversational text that breaks the parse. The same dial, two opposite verdicts. That is the lesson — settings are chosen per task, never globally.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run one prompt at two temperatures; project both; ask which is "the" answer.
2. **State the objective** — by the end you can choose a setting per task and justify it with observed variance.
3. **Recall prior learning** — token prediction and probability.
4. **Present the content** — temperature, tail filters, length limits, reasoning modes, repeat runs, fair comparison.
5. **Guide** — run both tasks above together and record the spread.
6. **Elicit performance** — pairs pick a third task and predict the right setting before testing.
7. **Give feedback** — compare predictions with results; the misses are the useful part.
8. **Transfer** — each learner writes the setting policy for one workflow they own.

## What the framework doesn't mention but trainers need to know

- **Settings interact with prompts.** A prompt with three examples tolerates higher temperature than one with none, because the examples pin the form. Tune them together.
- **Variance has a business cost.** Inconsistent outputs mean inconsistent routing, inconsistent tone and unreproducible complaints. Sometimes the right setting is the boring one.
- **Record settings with every evaluation.** An evaluation without recorded settings cannot be repeated, and repetition is the only way to distinguish improvement from noise.
- **Small differences are usually noise.** A two-point change on a small sample is not a finding. Say so before the room argues about it.
- **Reasoning mode is a setting with a bill attached.** It triples token consumption on some tasks for no gain. Test it against the fast mode before enabling it by default.

## Watch out

- **Do not present one run as evidence.** Any slide built on a single output is a slide that will be contradicted live.
- **Do not change the prompt and the setting together.** You will learn nothing and the room will learn the wrong habit.
- **Do not claim a setting is "best".** It is best for a task and a criterion. Name both.
- **The stale claim to retire:** "temperature 0 makes it reproducible." It makes it consistent; determinism is a different promise.
