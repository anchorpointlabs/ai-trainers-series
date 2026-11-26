---
id: 05.01.B.K3
tsc: 5
level: Basic
code: K3
title: Qualitative evaluation and user feedback: judging what numbers can't
as_at: 2026-11-26
review_by: 2027-02-25
---

# Qualitative evaluation and user feedback: judging what numbers can't

> **TSC #5 Generative AI Model Evaluation · Basic · Knowledge K3**


> **Framework text (verbatim):** "Qualitative evaluation methods and user feedback analysis."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Knowledge · Bullet 3 of 11

**One-line version:** Some of the most important things about an AI output — tone, usefulness, whether a real person would send it — cannot be counted, only judged, so evaluation has to include humans, not just metrics.

## What it is

Qualitative evaluation is judging output quality through human judgement instead of numbers: reading the output, watching a user react, asking whether it was useful. User feedback analysis is the disciplined version of that — collecting what users say and do with the output, then turning it into patterns you can act on. It is the half of evaluation that metrics cannot replace.

## Deep expansion

### The concept

A metric can tell you an output is grammatically correct and factually grounded; it cannot tell you it was *useful*, *appropriate in tone*, or *worth sending*. Those are human judgements. Qualitative evaluation treats the human — the evaluator or the end user — as the measuring instrument, and treats their reactions as data. The skill is doing that *systematically* rather than by "vibe": asking the right question, collecting the reaction without leading it, and separating "I liked it" from "it did the job".

### The sub-concepts

**Expert review.** A knowledgeable person reads the output against a checklist and gives a structured verdict. Slow, expensive, but the gold standard for judging quality and catching what a novice would miss.

**User feedback, explicit and implicit.** Explicit is what users *say* — a thumbs-up, a rating, a comment. Implicit is what users *do* — did they copy the output, edit it heavily, regenerate it, or abandon the task? The implicit signals are usually more honest, because they cost the user nothing.

**The editing distance.** One of the most useful implicit signals: how much did a human have to change the AI's output before using it? A draft that ships unedited is a success; a draft the user rewrote by half is a red flag, even if nobody complained.

**Leading versus open questions.** "Was this helpful?" produces polite yeses. "What did you have to fix?" produces the truth. Qualitative method lives or dies on question design.

### How it connects to the rest of the framework

This bullet is the human half of `TSC5-Basic-K2` (the four criteria) — the criteria are *what* you judge, and this bullet is *who* does the judging and *how* you capture it. It pairs with `TSC5-Basic-K5` (human perception and judgement), which is about *why* human judgement has biases to manage, and with `TSC5-Basic-A1` (collect user feedback), which is the hands-on ability this knowledge underlies.

### What is current as of November 2026

The shift is that **implicit signals have become the cheap, dominant feedback channel.** Because most people use models through a chat surface that logs copy, edit and regenerate events, organisations now read behaviour directly instead of running surveys. The other shift is a caution: **LLM-as-a-judge has started replacing some expert review** — a strong model grades outputs at scale. At Basic level the teaching point is unchanged: a human still has to calibrate and spot-check the judge, because an automated judge inherits all the biases in `TSC5-Basic-K5`.

### Common misconceptions

- *"Qualitative means informal."* It means *human* — and done properly it is more rigorous than a metric, because it asks the question a metric cannot phrase.
- *"User feedback means surveys."* Surveys are the smallest, most biased part of it. What users *do* beats what they *say*.
- *"A 4.2-star average tells me the model is good."* It tells you people were willing to click stars — not whether the output was used, edited, or quietly abandoned.

## How a student should understand it

**Mental model:** a food court with no prices and no wait — you judge a stall by watching who queues, whether plates come back clean, and what regulars actually order, not by a printed star rating.

**Three things they can do after this bullet:**
1. Turn "was it good?" into a non-leading question like "what did you have to fix?"
2. Name one explicit and one implicit user signal, and say which they trust more and why.
3. Explain why "no complaints" is not the same as "it was useful."

**Misconceptions to kill:** qualitative = informal, feedback = surveys, and star ratings = truth.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker queue.** Nobody filled in a survey at the famous stall; the queue *is* the feedback. What people do — queue, return, finish the plate, tell a friend — is implicit feedback, and it is more reliable than any comment card. The stall owner reads the queue and the leftovers the way a trainer reads edit distance and copy rates.

**The colleague who says "nice" but fixes everything.** Ask a colleague to review your draft and they say "looks good", then hand back a page of red ink. The red ink is the real feedback; the "looks good" is politeness. Qualitative evaluation is learning to ask for the red ink.

### Worked example with a real tool

Have a learner generate one email draft in any model, then run a tiny structured review with two questions:

```
Draft an email to a customer explaining a one-week delivery delay.

After you read it, answer two things — not "is it good":
1. What exactly did you have to change before you would send it?
2. Would you send it as-is to your own customer, yes or no?
```

What to point at afterwards: the list of "what I changed" is qualitative data — concrete, actionable, and specific to *their* standard. The yes/no is a blunt but honest signal. Neither is a metric; both are more useful than one.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room to think of a product they rated five stars but never used again. The gap between the rating and the behaviour is the whole topic.
2. **State the objective** — you will collect and read user feedback without leading it, and separate words from behaviour.
3. **Recall prior learning** — they just learned the four criteria; ask which criteria *need* a human to judge.
4. **Present the content** — explicit vs implicit, edit distance, non-leading questions.
5. **Guide** — run the email exercise together; collect the room's "what I changed" lists on a board.
6. **Elicit performance** — each learner drafts one output and has a partner review it with the two questions.
7. **Give feedback** — point out the leading questions that slipped in ("it's good, right?").
8. **Transfer** — for their next real AI task, log one implicit signal (did I copy it? edit it? abandon it?).

## What the framework doesn't mention but trainers need to know

- **Implicit signals are the modern goldmine.** Copy events, regeneration counts, edit distance, abandonment — these are free, continuous, and honest. A trainer who teaches only surveys is teaching the 2005 version of feedback.
- **Feedback needs a frame to be useful.** "Users are unhappy" is noise; "users in the finance team regenerate 40% of summarisation outputs" is a fixable finding. Teach learners to attach feedback to a task and a cohort.
- **The user is often wrong about *why*.** A user says "the model is stupid" when the real problem is a bad prompt or missing context. Qualitative evaluation means listening to the frustration, then diagnosing the cause separately.

## Watch out

- **Do not demo only a survey.** The framework says "user feedback analysis"; the modern, high-leverage version is behavioural signals. Teach the queue, not the comment card.
- **Do not treat qualitative as the soft option.** It is the *harder* option to do well — question design, sampling, and avoiding leading phrasing are all real skills. Do not let "it's just human judgement" undersell it.
- **The stale claim to retire:** "we have a five-star rating system, so we know how the model is doing." A star rating tells you how people felt for one second; it does not tell you whether the output was used.
