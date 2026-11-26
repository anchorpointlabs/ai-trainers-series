---
id: 05.02.I.K7
tsc: 5
level: Intermediate
code: K7
title: "Evaluators are users: interface design for fair human judgement"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Evaluators are users: interface design for fair human judgement

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K7**


> **Framework text (verbatim):** "Human-computer interaction principles for adaptive and personalised evaluation."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 7 of 12

**One-line version:** The rating you get depends on the form you handed the rater, so evaluation design is interface design — blind, short, anchored and adapted to the judge, or the measurement is measuring the room.

## What it is

This is the application of human-computer interaction principles to the act of evaluating: how the rating task is presented to a human (or an automated judge standing in for one), how much of it they do in a sitting, what they are shown alongside the output, and how the task adapts to who they are and what they know. It treats the evaluator as a user with limited attention, a drifting standard and a domain, rather than as a measuring instrument that happens to be a person.

## Deep expansion

### The concept

Every evaluation with a human in it is a user interface, and interface choices silently produce findings. Show the model name and the rater will find what they expected. Always put model A on the left and position bias appears. Ask for forty ratings in a row and the standard tightens or loosens by item thirty. Ask a nurse and a lawyer to rate "medical accuracy" and you have measured their training, not the model.

HCI has spent decades learning that people are consistent, biased and load-limited — which is exactly what a good evaluation protocol needs to account for. The principles transfer almost unchanged: reduce extraneous cognitive load, calibrate the user, randomise what should be neutral, and adapt the task to the person rather than forcing the person to adapt to the task.

"Adaptive and personalised" in the framework has two readings, and both are worth teaching. The protocol adapts to the *evaluator* — their expertise, their fatigue, which items are worth their time. And the system being evaluated adapts to *its users* — personalisation, which then has to be evaluated for consistency and fairness rather than only for average satisfaction.

### The sub-concepts

**Cognitive load and fatigue.** Rating quality drifts within a session. Keep sessions short (twenty to thirty items), force a break, and put a known-quality anchor item at the start, middle and end — if the rater scores the same anchor differently at the end, that is drift, measured.

**Blind comparison.** Hide the model identity. Randomise which output appears left or right. Position and identity effects are strong in humans and, as it turns out, in judge models too, which is why the same protocol now protects both kinds of rater.

**Paired rather than absolute scoring.** "Which of these two is better for this task?" is more reliable than "score this out of five", because the comparison is concrete and the rater's personal scale cancels out. Absolute scores are still useful for thresholds; use them sparingly.

**Anchors and calibration.** Show exemplars at 1, 3 and 5 before the session, and score a handful of gold items where the answer is known. Raters who fail the gold items get retrained, not overruled.

**Adaptive item selection.** Spend the expensive human attention where it changes the decision: items where two models disagree, items near the threshold, items from the slices that matter. Rating everything uniformly wastes most of the budget on items that were never in doubt.

**Personalisation by expertise.** A domain expert should rate the domain slice; a generalist should rate tone. Matching rater to slice is a design decision, and mismatching it is how "the model is bad at legal drafting" turns out to be "the raters were not lawyers".

**Feedback loops that do not anchor.** Showing raters their agreement with the group after the session improves calibration; showing it during the session induces conformity. Timing is the whole design.

**The report as an interface.** The decision-maker is also a user: one screen, a recommendation, the interval, and a route to the evidence. A fifty-page appendix is not transparency, it is a way of not deciding.

### How it connects to the rest of the framework

`TSC5-Basic-K5` (human perception and judgement) establishes that the evaluator is fallible; this bullet is the design response. `TSC5-Intermediate-K4` supplies the rubric that the interface renders; `K3` is the visual layer of the same problem; `K5` explains why blind comparison matters for fairness as well as validity. `TSC5-Intermediate-A1` implements the review queue these principles govern, and `TSC-04` (Model Selection) consumes the resulting preference data.

### What is current as of November 2026

Blind pairwise comparison became the default way to present text quality, largely because it is the only format that survived the arrival of judge models — the same interface works for a human and for a model, and the same biases show up in both. Annotation tooling now ships with rater calibration, gold items and inter-rater statistics as standard rather than bespoke. Multimodal evaluation has pushed interface design forward: side-by-side image and video comparison with synchronised playback, and diff views for edits. The open problem is agentic evaluation, where the rater has to judge a trajectory rather than a reply and the interface has to show steps without drowning the reader.

### Common misconceptions

- *"Humans are the ground truth."* Humans are the most flexible instrument available and the least stable one. Ground truth is a protocol, not a person.
- *"Blind is enough."* Blind removes identity bias; it does nothing about order, fatigue, or a rater who does not know the domain.
- *"More raters is always better."* Ten raters trained the same way on the same rubric give you one opinion ten times.
- *"The tool does not affect the rating."* The tool is the rating's environment, and environments shape behaviour.

## How a student should understand it

**Mental model:** the polyclinic triage form. Same nurses, better form, better triage. Nobody blames the nurse for a form that asks the wrong question in the wrong order.

**Three things they can do after this bullet:**
1. Design a twenty-item blind comparison session with randomised order, anchors and a break.
2. Detect rater drift using a repeated anchor item.
3. Decide which items deserve human attention and which can be scored automatically.

**Misconceptions to kill:** humans are objective, blinding is sufficient, and the interface is neutral.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The PSLE oral examiner.** Forty children in a day. The first ten are marked strictly, the middle twenty drift, the last ten are marked generously because the examiner is tired and wants to go home. That is why Singapore moderates oral marks. Any evaluation with a human in it needs the same moderation, and most do not have it.

**The NEA inspector's checklist.** The inspector is not asked "is this kitchen clean?" but a fixed sequence of checkpoints in a fixed order. The form carries the standard so the inspector does not have to.

### Worked example with a real tool

Have the room design the session before running it:

```
I need to compare two AI models on 20 customer emails. Design the rating
session for me:

1. A 5-point rubric with a one-line anchor at 1, 3 and 5.
2. The presentation order, so that neither model is always first and I
   cannot tell which is which.
3. Two anchor items where I already know the right answer, and where to
   place them in the session.
4. How many items before a break.
5. What to record so I can check afterwards whether my ratings drifted.
6. How to decide which items a second rater should see.
```

What to point at afterwards: the model will produce a protocol that is better than most teams' ad hoc process, and the room should notice that none of it required a tool — only decisions made before the first rating. Then run four items live and check whether anyone can guess which model produced which.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show one output labelled "Model A, the expensive one" and the same output labelled "Model B, the cheap one"; collect two different scores for identical text.
2. **State the objective** — you will design a rating session that a sceptic would accept.
3. **Recall prior learning** — Basic K5 on human perception; ask what they concluded then.
4. **Present the content** — load, blindness, pairing, anchors, adaptive sampling, expertise matching, the report as interface.
5. **Guide** — build the twenty-item session design on the board, then run four items live.
6. **Elicit performance** — pairs design a session for their own use case, including the drift check.
7. **Give feedback** — critique protocols that rate everything, hide nothing, or use ten raters with the same training.
8. **Transfer** — they run a real session on ten items and report the drift finding.

## What the framework doesn't mention but trainers need to know

- **Rater time is the binding constraint.** Twenty ratings per rater per session, and a domain expert's hour costs more than a month of API calls. Design the evaluation around that budget, not around the metric.
- **Judge models inherit interface biases.** Put the same blind, randomised, anchored protocol around a judge that you would around a human, or you have automated the bias rather than removed it.
- **Agreement between raters is a design output.** Low agreement usually means an ambiguous anchor or a mismatched domain, not bad raters. Fix the rubric before replacing the person.
- **Personalised evaluation raises its own fairness question.** If the system behaves differently for different users, "average satisfaction" hides exactly the thing worth measuring — see `K5`.

## Watch out

- **Do not run a rating exercise where the room can see the model names.** You will spend the debrief arguing about brands.
- **Do not ask for a single overall score.** It invites the room to average four different questions into a feeling.
- **Do not let the interface become the finding.** A slick comparison tool produces confident preferences; make sure the protocol underneath earns them.
- **The stale claim to retire:** "we'll get the team to eyeball a hundred outputs." That is not an evaluation, it is a meeting with extra steps — unless the eyes are blinded, anchored, rested and recorded.
