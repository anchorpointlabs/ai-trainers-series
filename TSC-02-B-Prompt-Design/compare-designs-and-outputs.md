---
id: 02.01.B.A8
tsc: 2
level: Basic
code: A8
title: Compare designs and outputs
---

# Compare designs and outputs

> **TSC #2 Prompt Design · Basic · Ability A8**

> **Framework text (verbatim):** "Compare prompt designs and corresponding AI outputs, including their suitability for different use cases in different domains."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 10 of 15

**One-line version:** Compare the designs and the outputs on the same three checks — true, complete, fit for the reader — and keep those checks separate from the question of which one you like.

## What it is

Comparing prompt designs means putting two versions side by side, naming exactly what differs, and judging the outputs that follow from each. Suitability is part of that judgement: the same facts written as a compressed staff log and as a public notice suit different readers, and neither is "better" in the abstract. Truth is a separate question. A well-formatted output with the wrong reopening time has failed, however suitable it looks.

## Deep expansion

### The concept

Comparison is where learners most often fool themselves, and the fooling is not dishonest — it is structural. Two replies arrive, one reads more pleasantly, and the pleasant one wins. The discipline this bullet asks for is a fixed set of checks applied to both, so that preference has to argue with evidence.

The method is simple enough to teach in three minutes and hard enough to practise for a term:

1. **Hold the facts constant.** Both prompts get the same source data. If the facts differ, you are comparing the data, not the design.
2. **Change one design variable.** Length, register, structure, format — one at a time. Two simultaneous changes make the result uninterpretable.
3. **Apply the same checks to both outputs.** Factual agreement with the source. Completeness against the list of required items. Fit to the format the use case demands.
4. **Judge suitability last, and say why.** "This one suits the staff log because three-second scanning matters more than grammar" is a judgement with a reason; "this one is nicer" is not.

### The sub-concepts

**Three checks, in this order.** Fact agreement first, because a beautiful lie is worse than an ugly truth. Completeness second, because a missed reopening time sends someone to a closed door. Format third, because it is the cheapest to fix and the easiest to over-value.

**Suitability is reader-dependent, not absolute.** A staff log wants fragments with a semicolon so it can be scanned in a queue. A public notice wants a full sentence with a subject and a verb, because it will be read by someone with no context. Both are correct answers to different questions.

**Domain changes the standard.** Retail and education use the same closure facts and different conventions: a shop's notice talks to customers, a school library's notice talks to parents and may need a date format they recognise. Comparing across domains is how learners discover that "the format" is never one thing.

**Fluency is not evidence.** The more polished output is often the one that added a friendly clause nobody asked for. Trainers should model suspicion of their own preference out loud.

**A comparison is a sample, not a proof.** One run of each design shows you what happened once. Variation means a difference could reverse on another day; say so rather than declaring a winner.

### How it connects to the rest of the framework

`TSC2-Basic-K2` is the mechanism that makes a design change visible; `TSC2-Basic-A5` gives you the elements to vary; `TSC2-Basic-A6` is the practice list these comparisons end up validating or rejecting; `TSC2-Basic-A1` is the technique description you compare against. At Intermediate level, `TSC5-Intermediate-K4` turns this three-check habit into a written rubric.

### What is current as of November 2026

Comparison has become easier to do at volume and easier to do badly. The late-2026 assistants — GPT-6-generation models, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — will happily generate five variants of a notice in one turn, which tempts learners to skip the checks and pick by feel. The useful 2026 discipline is the opposite: fewer variants, more runs per variant. It has also become normal to ask a model to critique two outputs against a stated rubric, which is a legitimate aid — provided the learner writes the rubric and still reads both outputs. A model grading its own writing tends to agree with itself.

### Common misconceptions

- *"Compare means pick the better one."* Compare means state the difference, then judge fitness for a named use.
- *"The more formal one is more suitable."* For a staff log it is worse: formality costs scanning speed.
- *"If both use the same facts, they're equally accurate."* Both can drop a fact. Completeness is a separate check.
- *"The one that reads better is the one to ship."* Reading pleasure and factual agreement are unrelated measurements.

## How a student should understand it

**Mental model:** two tailors, one set of measurements. Both used your numbers; one cut for a wedding, one for a worksite. The question is not which tailor is better, it is which garment the occasion needs — and whether either got the measurements right.

**Things they can do after this bullet:**
1. Name what differs between two prompts and what they share.
2. Apply the same three checks to both outputs.
3. Choose a design for a named use and justify it from the text.

**Misconceptions to kill:** that comparison produces a winner rather than a fit; that accuracy and completeness are the same check; that polish is evidence.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic notice and the staff memo.** The same clinic closure goes on the door as "Closed 2–4pm today. Reopens 4pm." and into the staff roster as "Clinic closed 2–4 (stock take); reopen 4." Nobody argues that one is better writing. They are two artefacts for two readers. Where it breaks: a clinic notice has a physical constraint — it must be readable at a glance from two metres — that a chat prompt cannot enforce.

### Worked example with a real tool

Run A and B in separate fresh chats.

```text
Use only these fictional facts.
Retail: Lark Books is closed on Monday. It reopens on Tuesday at 10:00.
Education: Pine School library is closed on Wednesday. It reopens on Thursday at 09:00.

For each domain, write an internal staff log with exactly two short fragments separated by a semicolon, using the labels Retail and Education. Include the place name, closure day, reopening day and time. Add no other facts.
```

```text
Use only these fictional facts.
Retail: Lark Books is closed on Monday. It reopens on Tuesday at 10:00.
Education: Pine School library is closed on Wednesday. It reopens on Thursday at 09:00.

For each domain, write a public notice as one full sentence, using the labels Retail and Education. Include the place name, closure day, reopening day and time. Add no other facts.
```

What to point at afterwards: identical facts, one design variable (compressed fragments versus full sentences). Put the four outputs in a grid and run the three checks down each column. Then ask the room to nominate an output for the staff log and one for the noticeboard, requiring a reason drawn from the wording. Finally, change one reopening time in A's output by hand and ask whether it is still suitable — the answer, "it is well formatted and wrong", is the sentence you want them to leave with.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "Would the same closure message be equally useful in a staff log and on a public notice?" Invite one reason.
2. **State the objective** — by the end you can compare two designs on three fixed checks and justify a fit.
3. **Recall prior learning** — the element list from `TSC2-Basic-A5`; the variability lesson from `TSC2-Basic-K2`.
4. **Present the content** — hold facts, change one variable, three checks, suitability last.
5. **Guide** — run A and B together and fill the grid on the board as a class.
6. **Elicit performance** — pairs repeat for the education domain and draft a one-sentence justification.
7. **Give feedback** — take three justifications; mark which are reasons and which are preferences.
8. **Transfer** — each learner brings two real templates from their workplace and compares them the same way.

## What the framework doesn't mention but trainers need to know

- **Learners compare with their taste, not their eyes.** Ask them to write the checks down *before* seeing the outputs; that single habit does most of the work.
- **"Suitable" needs a named reader.** Push for "suitable for the supervisor scanning a queue", not "suitable".
- **Both designs can fail the same check.** That is a finding about the facts, not the styles — and it is worth naming, because it stops the comparison becoming a beauty contest.
- **Repeated runs test the design; single runs test your luck.** If a difference matters, run each design three times before concluding.

## Watch out

- **Do not compare prompts with different facts.** It is the most common classroom error and it invalidates the exercise.
- **Do not declare a winner.** Ask for a fit and a reason; a winner ends the thinking.
- **Do not let the model judge without a rubric.** A model asked "which is better" will produce a confident answer with no basis.
- **The stale claim to retire:** "the best prompt is the one with the nicest output." In November 2026 a nicest-output comparison mostly measures tone; fitness and accuracy need their own checks.
