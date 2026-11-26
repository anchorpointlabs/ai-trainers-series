---
id: 04.02.I.A6
tsc: 4
level: Intermediate
code: A6
title: Analyse the impact of model variations on output quality
---

# Analyse the impact of model variations on output quality

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A6**

> **Framework text (verbatim):** "Analyse the impact of model variations on output quality for specific tasks."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Ability · Bullet 11 of 11

**One-line version:** A newer version is not automatically better for your task — the only evidence that counts is your task, your cases, your score.

## What it is

"Variations" covers four different things that are often blurred together: different **sizes** of the same family, different **versions** of the same size, different **modes** (fast versus reasoning), and different **fine-tunes** of the same base. Each changes output quality in a task-specific way. Analysing the impact means building a small, honest test, running the variants through it, and reporting the difference with the sample size attached.

## Deep expansion

### The concept

Model families are marketed as ladders — bigger, newer, better. For a specific task, the ladder often flattens: a smaller model matches a frontier one on schema extraction, a middle version beats the newest on a narrow classification, and a reasoning mode that wins on multi-step planning loses on tone.

The method is deliberately modest. Ten to thirty representative cases, a criterion written before the run, each variant tested on the identical inputs, and a result expressed as a count rather than an adjective. It takes an hour and it replaces a month of opinion.

### The sub-concepts

**Write the criterion first.** Before seeing any output, decide what counts as a pass: required fields present, tone acceptable, no invented figures, length within band. Criteria written afterwards always fit the winner.

**Small samples lie in both directions.** At thirty cases, a single flipped case moves the score by more than three points. A two-point difference is noise. Say this out loud before the room debates a close result.

**Test the slice that matters.** An overall pass rate hides the failing subgroup. If the task is regulatory correspondence, the cases that decide the verdict are the awkward ones, not the typical ones.

**Separate capability from compliance.** A newer version may reason better and format worse. Both are quality; they fail differently, and a change in one can mask a regression in the other.

**A variant change is a release event.** New version, new mode, new adapter — each needs the same gate as a code change. "It is just a model update" is how behaviour shifts without anyone noticing.

**Attribute before you conclude.** If you also changed the prompt, the temperature or the examples, you cannot attribute the difference to the model. One change at a time.

### How it connects to the rest of the framework

`TSC4-Intermediate-A5` is the settings version of this experiment; this bullet is the model version. `TSC4-Intermediate-A4` supplies the quality criteria you score. `TSC4-Advanced-A2` scales this from a spot check to a stratified evaluation set. `TSC4-Advanced-A3` asks whether the difference persists over time. `TSC4-Advanced-K3` is why the version must be pinned in the first place.

### What is current as of November 2026

For the 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — variation testing has become routine rather than occasional:

- **Within-family differences on narrow tasks are now small.** The gap between tiers on schema extraction or classification is often unresolvable at small sample sizes, which makes price and latency the deciding factors.
- **Mode variation can exceed version variation.** Fast versus reasoning mode within one model can matter more to your task than the step between two generations.
- **Vendors refresh snapshots on their own schedule.** With roughly annual retirement cycles, re-testing after an alias update is now a recurring operational task, not a one-off project.

### Common misconceptions

- *"Newer is better."* Newer is newer. Its advantage is task-specific and sometimes negative.
- *"Bigger is always more accurate."* Bigger is broader. On a narrow, well-specified task the curve flattens early.
- *"We can tell from the demo."* A demo is a curated sample. One good output proves nothing about the distribution.
- *"A two-point difference is a real difference."* On thirty cases it is inside the noise.

## How a student should understand it

**Mental model:** a taste test. Same dish, two cooks, no labels, a scorecard written before anyone tastes. Marketing does not get a vote.

**Things they can do after this bullet:**
1. Build a five-to-thirty-case test for a stated task and write the pass criterion.
2. Run two variants and report the result with the sample size.
3. State when a difference is too small to act on.

**Misconceptions to kill:** that new means better, that a demo is evidence, and that a small numeric difference is a finding.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The two bak chor mee stalls.** The famous one has the queue. The one two streets away may suit your taste better, and the only way to know is to eat both on the same day. Reputation is a leaderboard; your palate is your test set.

**The phone upgrade.** The new model has a better camera and worse battery. "Better" depends on whether you take photos or make calls.

### Worked example with a real tool

Design the test, then read the result honestly:

```text
Design a 5-question test to compare two model versions on
customer-support replies. Say exactly what you would score,
and what result would make you switch.
```

What to point at afterwards: good answers specify the inputs (an angry complaint, a refund query, a wrong-address issue, a policy question with no answer in the source, and one Singlish message), the scoring (facts correct / tone acceptable / length under 120 words / no invented policy), and a switch threshold stated in advance. Weak answers say "compare which is better". The difference between those two answers is the whole competency.

Then run the honest-sample conversation:

```text
Version A scored 8/10 and Version B scored 7/10 on your five cases.
What can you conclude, and what would you need to conclude more?
```

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two versions' outputs side by side, unlabelled, and ask which is newer.
2. **State the objective** — by the end you can build a variant test with a criterion and report the result honestly.
3. **Recall prior learning** — settings versus models, and why one change at a time matters.
4. **Present the content** — the four kinds of variation, criterion first, sample size, slicing, attribution.
5. **Guide** — build the five-case test together for a task the room recognises.
6. **Elicit performance** — pairs write their own criterion and switch threshold.
7. **Give feedback** — debrief, challenging thresholds written after the result was known.
8. **Transfer** — each learner schedules a re-test for the moment their vendor updates a snapshot.

## What the framework doesn't mention but trainers need to know

- **Version changes are silent.** A floating alias can move overnight. Without a pinned snapshot you cannot even tell that a variation happened.
- **Prompt templates are model-specific.** A test that reuses another family's template measures template fit, not model quality. Adapt minimally and say that you did.
- **Fine-tunes are variants too.** A tuned model must be compared against its own base, not only against other models, or you cannot tell what the tuning bought.
- **Latency and cost belong in the same table.** A variant that is one point better and three times slower is usually the wrong variant.
- **Write the result down.** Variant tests that live in a chat thread get repeated every quarter. A one-page record ends the argument permanently.

## Watch out

- **Do not let a vendor's benchmark settle the question.** It was measured on someone else's distribution.
- **Do not test on the cases you tuned on.** That measures memorisation.
- **Do not report a single number without the sample size.** "94 per cent" on five cases is one case away from 80 per cent.
- **The stale claim to retire:** "we will upgrade when the new model comes out." Upgrade when your test says the new model is better for your task — and not before.
