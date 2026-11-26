---
id: 03.01.B.A3
tsc: 3
level: Basic
code: A3
title: Comparing prompt designs without fooling yourself
as_at: 2026-11-26
review_by: 2027-02-25
---

# Comparing prompt designs without fooling yourself

> **TSC #3 Prompt Engineering · Basic · Ability A3**


> **Framework text (verbatim):** "Compare prompt designs and corresponding AI outputs, including their suitability for different use cases in different domains."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 10 of 15

**One-line version:** A comparison is only worth running if the rubric existed before the outputs did — otherwise you are ranking your own preferences and calling it evidence.

## What it is

Comparing prompt designs means putting two or more candidate prompts against the same inputs, scoring the outputs against criteria decided in advance, and judging which design suits which use case. Done casually it produces a preference. Done properly it produces a decision a team can rely on, and a record of why.

## Deep expansion

### The concept

The default method in most offices is: write prompt A, get an output you like, write prompt B, get an output you like less, declare A better. Three things make that worthless — one input, no criteria, no blindness — and all three are fixable in twenty minutes.

The practitioner's version has five parts:

**A fixed input set.** Eight to ten real inputs, chosen to cover the range: a typical case, a messy case, an edge case, one where the correct answer is unusual. Judging on the case you had in front of you when you wrote the prompt is judging the prompt on its own training example.

**A rubric written first.** Four or five criteria with a simple scale, derived from the task's done-check. For a complaint summary: factual accuracy, coverage of the required columns, length compliance, actionability for the reader, and absence of invented content. Written before generation, because after generation the room scores whatever it happens to notice.

**Blind labels.** Outputs stripped of which prompt produced them, presented as A, B, C. Non-blind comparison reliably favours the design the reviewer argued for.

**Multiple runs.** A single run per design compares samples, not designs. Run each design on each input a few times, or at minimum run the ones that score suspiciously well again.

**A cost column.** Time to first usable output, tokens, review effort. A design that scores one point higher and takes four times as long to check is usually the worse design.

### The sub-concepts

**Three designs, not two.** A versus B is a coin flip; A, B and C shows you the shape of the trade-off — usually that the constraint which fixed one failure caused another. Three is also the point where the room stops arguing about favourites and starts describing differences.

**Suitability is domain-specific, and that is the real finding.** The framework's phrase "suitability for different use cases in different domains" is the part practitioners skip. A design that works for internal notes fails for customer-facing copy not because it is worse, but because the reader, the consequence of error, and the checking budget all differ. Write that down per domain.

**Accuracy is checked against a source, not against plausibility.** "Suitable" is not "true". The rubric must include a factual check performed against the input document, by a person, before any style score is recorded — otherwise the best-scoring design is often the most confidently wrong.

**Score the failure, not only the success.** Add a criterion for how the design fails: loudly (NOT IN SOURCE), quietly (a plausible fabrication), or by drifting off-task. Designs differ more in failure mode than in average quality, and the failure mode is what a team lives with.

**Write the decision, not just the scores.** "Design B for customer complaints; Design C for internal triage, because it tolerates missing owners" is the deliverable. A table of numbers with no decision gets re-run next month.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A8` (Prompt Design); see that entry for the user-level basics of comparing instructions and replies. `TSC3-Basic-K2` explains which lever each design is pulling, `TSC3-Basic-K3` is what the designs are built from, `TSC3-Basic-K4` is why the comparison must be run per mode rather than across modes, and `TSC3-Basic-A4` is the practice list the winning design should end up satisfying.

### What is current as of November 2026

Comparison has become cheaper and more necessary. Structured outputs let you score format compliance mechanically instead of by eye; evaluation tooling has moved from research code into ordinary product features; and long context means a single test input can be a whole document, so a ten-input set is now realistic rather than laborious.

The necessity comes from model churn. Behaviour shifts between versions behind stable product names, so a decision recorded last quarter is a hypothesis this quarter. Comparisons now carry a date and a model version, or they are folklore.

### Common misconceptions

- *"The output I liked best is the better design."* Preference is not a criterion, and it is heavily influenced by which prompt the reviewer wrote.
- *"One run each is enough."* One run each compares two samples. Run again before concluding.
- *"Higher quality wins."* Cost and failure mode usually decide, because the higher-quality design that fails quietly is the expensive one.
- *"A comparison is a one-off."* It expires with the model version.

## How a student should understand it

**Mental model:** the blind taste test at a hawker centre — same fish, same oil, coded bowls, and the score sheet written before the first bite.

**Things they can do after this bullet:**
1. Build a ten-input set and a five-criterion rubric before generating anything.
2. Run three designs blind and score them, including a failure-mode column.
3. Write a one-line decision naming the domain each design suits.

**Misconceptions to kill:** that liking an output is a comparison; that one run per design is a test; that a score without a cost column is a decision.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The blind taste test.** Two stalls, same fish, same oil, bowls labelled A and B, and everyone scores before the labels come off. The moment someone knows whose stall it is, the scoring changes. Where it breaks: tasters agree broadly on what tastes good, while prompt outputs can be pleasant and wrong — so the rubric needs a factual criterion that taste tests do not.

**The insurance comparison site.** Same cover, different exclusions, and the cheapest premium is usually cheapest because of a clause nobody read. Where it breaks: an insurance comparison has a standard set of fields; prompt designs differ in ways nobody thought to list, which is why the rubric must be written from the task, not borrowed.

### Worked example with a real tool

Task: turn a month of support emails into a weekly themes report. Three designs:

```text
Design A (bare instruction)
"Read these emails and tell me the main themes."

Design B (instruction + fixed schema)
"Group these emails into at most 5 themes. Output a markdown table:
Theme | Count | One example quote (max 15 words) | Suggested owner.
Use only the emails below. If a theme has fewer than 3 emails, fold it into
'Other'. Do not invent themes that are not evidenced by at least 3 emails."

Design C (one-shot + schema)
[One worked example of a 20-email batch with its finished table]
"Now do the same for the batch below. Same columns, same rules, same
'Other' threshold."
```

The rubric, written first:

```text
1. Every theme traceable to real emails (verify 3 quotes each)   /5
2. Counts add up to the batch size                                /5
3. Column shape exactly as specified                              /5
4. A manager could act on it without asking a question             /5
5. Failure mode if the batch has no clear themes: loud / quiet     L/Q
```

What to point at afterwards: B usually beats A on shape and traceability; C usually beats B on tone consistency but copies the example's phrasing and occasionally borrows its theme names. The finding is not "C wins" — it is "C for recurring weekly reports where the taxonomy is stable; B for ad-hoc batches where the topics are new". That sentence, with a date and model version beside it, is the deliverable.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two outputs and ask which is better. Then reveal that one is the same design run twice.
2. **State the objective** — by the end you will have run a blind three-way comparison and written the decision line.
3. **Recall prior learning** — ask how they choose between two vendors: criteria first, or a feeling then a justification.
4. **Present the content** — teach the five parts, then the failure-mode column and the domain sentence.
5. **Guide** — build the rubric together from the task's done-check, before any output exists.
6. **Elicit performance** — groups run three designs on a shared ten-input set and score blind.
7. **Give feedback** — compare score sheets. Where groups disagree, the criterion was ambiguous — which is itself the lesson about rubrics.
8. **Transfer** — each learner writes their own decision line and the date it expires.

## What the framework doesn't mention but trainers need to know

- **The rubric is the reusable asset.** Designs get rewritten; a good rubric transfers to the next design and the next model.
- **Disagreement between reviewers is data.** It usually means a criterion needs a definition, not that one reviewer is wrong.
- **Never compare across modes.** A text design versus an image design is not a comparison; compare within a mode against that mode's standard.
- **Record the model and date, always.** A comparison without them cannot be trusted in a quarter, and it will be quoted as if it can.

## Watch out

- **Do not run the comparison live without a prepared input set.** Live improvisation produces three outputs on one convenient input and a false conclusion.
- **Do not let the author of a design score their own.** Blind labels or a different scorer.
- **Do not present style preferences as quality.** If the rubric's only real criterion is "reads nicely", say so and stop calling it an evaluation.
- **The stale claim to retire:** "the newer model makes prompt comparison unnecessary." It makes it cheaper, and it makes it expire faster.
