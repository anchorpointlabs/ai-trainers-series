---
id: 03.02.I.K6
tsc: 3
level: Intermediate
code: K6
title: Prompt design, model behaviour, and output diversity
---

# Prompt design, model behaviour, and output diversity

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K6**

> **Framework text (verbatim):** "Relationship between prompt design, model behaviour, and output diversity."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Knowledge · Bullet 6 of 13

**One-line version:** The prompt sets the width of the target — precision and diversity are one dial, and every unstated requirement is a dimension the model will vary along.

## What it is

Prompt design determines model behaviour, and model behaviour determines how much the output varies. A prompt that closes every dimension — reader, length, structure, stance, what counts as a correct answer — produces consistent output. A prompt that leaves dimensions open produces variation, which is either the point (ideation) or the defect (extraction). Diversity is therefore designed, not wished for, and it trades directly against precision.

## Deep expansion

### The concept

Learners usually explain variation as a property of the model: "it's random", "it's inconsistent", "temperature". The more useful explanation is that variation lives in the prompt's degrees of freedom. Every requirement you did not state is a choice the model makes freshly on each run — and it makes it plausibly, so the variation looks like judgement rather than chance.

That gives a clean model of the relationship:

- **Design closes or opens dimensions.** Constraints narrow the space of acceptable answers; open questions widen it.
- **Behaviour follows the closure.** A prompt with a reader, a length and a format behaves like a specification. A prompt without them behaves like a suggestion.
- **Diversity is the observed spread across runs and within a set.** It is a measurement, not a mood.

The consequence for teaching: when output is inconsistent, look for the unstated dimension before reaching for a setting. When output is repetitive, look for a constraint that closed a dimension you wanted open.

### The sub-concepts

**Three dials, in order of strength.** (1) The degrees of freedom in the prompt — strongest by far. (2) Examples — they lock pattern and format, and quietly kill diversity because the model copies their shape. (3) Sampling parameters — temperature, top-p, top-k — the dial learners reach for first and understand least. Temperature flattens or sharpens the probability distribution, so it changes word choice more than it changes substance: ten runs at high temperature often produce the same idea in different words.

**Diversity must be demanded, not hoped for.** "Give me ten ideas" usually returns three ideas and seven restatements. The instruction that works names the axis of difference: "each must target a different audience", "no two may share a mechanism", "none may use the words healthy, fun or community". Banning the obvious forces the model off its highest-probability path.

**Convergence is a feature for analytical work.** Extraction and classification want zero diversity: same input, same output, every time. That is bought with definitions, a schema, low temperature and an explicit rule for borderline cases — not with "be consistent", which specifies nothing.

**Determinism is not on the menu.** Temperature zero makes decoding greedy, but floating-point arithmetic across parallel hardware and mixture-of-experts routing can still flip a near-tie. Two runs can differ. Plan for it with checks and human review rather than with a hope that the setting guarantees reproducibility.

**Diverge, then converge.** The productive pattern for any creative task is two stages: generate wide at high temperature with an explicit demand for difference, then select and sharpen against stated criteria in a second call. The second call is where quality comes from; the first only supplies raw material.

**Sycophancy is a diversity failure.** A leading prompt — "don't you think this plan is too risky?" — collapses the distribution onto the user's opinion. Neutral framing restores the spread: "list the risks and the benefits, then state which dominates and why".

**Length is a behaviour lever, not formatting.** "One sentence" and "one page" do not produce the same content compressed differently; they change what the model decides is worth saying.

### How it connects to the rest of the framework

`TSC3-Basic-K2` gives the five levers of prompt design; this bullet is the precision-diversity trade-off those levers sit on. `TSC3-Intermediate-K3` is the wording that closes a dimension, `TSC3-Intermediate-K4` explains why piling on context narrows the output as well as diluting attention, and `TSC3-Intermediate-K5` is where the trade-off becomes concrete — the brainstorm shape versus the extraction shape. `TSC3-Intermediate-A2` carries the testing discipline that proves which dial moved.

### What is current as of November 2026

The dial has moved toward convergence. Reasoning tiers in the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon deliberate toward a single best answer, which is exactly what you want for analysis and exactly what you do not want for ideation. Practical consequences:

- **Pick the tier by the task.** Divergence wants the fast chat model; convergence wants the reasoning model. Using one for the other is the most common misconfiguration in 2026.
- **Structured output forces convergence.** A schema is a set of closed dimensions, and it makes outputs consistent at the cost of variety. That is the right trade for extraction and the wrong one for drafting options.
- **Sampling ranges are provider-specific.** Temperature scales are not comparable across families; a value that is "creative" on one model is "unhinged" on another. Teach the concept, not a universal number.

### Common misconceptions

- *"A vague prompt is more creative."* A vague prompt is more variable, which is not the same thing. It varies in length, register and structure as well as in ideas.
- *"Temperature is the creativity dial."* Temperature changes sampling, not substance. Prompt-level demands for difference do more work than any setting.
- *"Temperature zero gives identical output."* It gives greedy decoding. Hardware and routing can still produce a different token at a tie.
- *"Diversity means random."* Useful diversity is spread across a meaningful axis — audience, mechanism, cost — and randomness is only one way to get there.

## How a student should understand it

**Mental model:** the zoom on a camera. Wide angle takes in the whole scene and nothing in detail; telephoto isolates one subject and loses the context. There is no setting that does both — you choose, then decide whether to take a second shot.

**Things they can do after this bullet:**
1. Take a prompt and name the three dimensions it left open.
2. Write a precise version and a diverse version of the same task, and say which dimension each closes or opens.
3. Run one prompt three times and describe the variation in substance rather than in wording.

**Misconceptions to kill:** that vagueness is creativity; that temperature is the answer; that one run tells you anything about consistency.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The exam question.** "Discuss the causes of the war" versus "List three causes of the war, one sentence each." Same subject, different marking scheme, different answer. Where it breaks: an exam marker is consistent; a model will vary even under a tight instruction, which is why you check rather than assume.

**The buffet and the set lunch.** The buffet offers variety and you assemble something random; the set lunch is consistent and you eat the same thing every visit. Most offices need the set lunch for reporting and the buffet for the annual campaign.

### Worked example with a real tool

Two versions of one task, run side by side:

```text
PRECISE
List the three biggest risks in this plan as a table: Risk | Likelihood (H/M/L) |
Mitigation. No other text. If the plan does not state a mitigation, write NONE.

DIVERSE
Give 12 very different names for a pickleball club in Singapore.
Rules: no two may use the same idea (no repeats of 'smash', 'rally', 'net');
at least three must not be in English; none may contain 'club' or 'academy'.
```

Then the converge step: take the twelve names, ask for the best three against stated criteria — memorable, sayable at a void deck, no trademark clash. What to point at: the first prompt produces nearly identical tables on repeat runs; the second produces genuinely different candidates only because difference was specified; and the third call is where judgement enters.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask for "some ideas for a staff event" and show the ten near-identical suggestions.
2. **State the objective** — by the end you can deliberately widen or narrow a prompt and explain which dimension you moved.
3. **Recall prior learning** — what are the five levers of prompt design, and which one sets length?
4. **Present the content** — the three dials in order of strength, then diverge-then-converge.
5. **Guide** — run the pickleball pair together and label what changed.
6. **Elicit performance** — pairs write a precise and a diverse version for one of their own tasks.
7. **Give feedback** — run each three times; compare the spread. If the "diverse" version is uniform, the demand was too weak.
8. **Transfer** — each learner writes which tier and which setting they will use for ideation versus reporting.

## What the framework doesn't mention but trainers need to know

- **Consistency is an evaluation problem before it is a prompting problem.** To claim a prompt is stable you need several runs on several inputs, not one good output.
- **Examples are the quietest diversity killer.** Three near-identical few-shot examples produce three near-identical answers, forever.
- **"Creative" and "accurate" are different jobs with different costs.** Say which one the task needs before the room argues about temperature.
- **The reader's tolerance sets the dial.** A customer-facing draft needs variation reviewed; a monthly figure needs none at all.
- **Sycophancy shows up as agreement, not as error.** If every plan the room tests comes back "strong", the prompts are leading and the model is being polite.

## Watch out

- **Do not teach temperature as the first tool.** It is the third dial, and reaching for it teaches learners to fiddle instead of specify.
- **Do not demo creativity with one run.** One output proves nothing about spread; show three.
- **Do not let a reasoning model be the ideation demo.** It will converge, the room will conclude the model is uncreative, and the lesson will be wrong.
- **The stale claim to retire:** "turn up the temperature for creativity." Specify the axis of difference, then optionally raise the temperature — in that order.
