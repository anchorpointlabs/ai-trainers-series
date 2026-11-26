---
id: 03.01.B.A4
tsc: 3
level: Basic
code: A4
title: Best practices that survive a busy Tuesday
as_at: 2026-11-26
review_by: 2027-02-25
---

# Best practices that survive a busy Tuesday

> **TSC #3 Prompt Engineering · Basic · Ability A4**


> **Framework text (verbatim):** "Identify best practices for designing effective prompts."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 11 of 15

**One-line version:** A best practice earns the name only if it names the failure it prevents — and only if a tired person can still follow it at 5pm.

## What it is

Best practices for prompt design are the habits that reliably improve output across tasks and models. Identifying them means separating three different things that get mixed together in training rooms: transferable practice, model-specific trick, and organisational policy. Only the first belongs on a best-practice list; the other two need different labels and different owners.

## Deep expansion

### The concept

Most best-practice lists fail for one of two reasons. They are too long to remember, or they are a list of tricks that stopped working. The practitioner's discipline is to keep a short list, and to attach to each item the failure it prevents, because a practice whose purpose nobody can state will be dropped the first busy week — or worse, applied to a task where it does harm.

Seven survive scrutiny:

1. **State the task as one verb, and put it where attention is.** One operation per prompt. "Analyse and rewrite" produces the analysis or the rewrite, not both.
2. **Supply facts; never imply them.** The model cannot use what you did not type, and it will not tell you what it lacked.
3. **Say what done looks like.** A done-check converts a wish into a specification and makes review possible for someone else.
4. **Say what to do when the input does not support the task.** The failure line — NOT IN SOURCE, stop, ask, escalate — is the highest-value sentence in most prompts.
5. **Constrain the format enough to be checked.** A table with named columns is checkable; flowing prose is arguable.
6. **Write for the person who will run it, not for yourself.** If it needs a briefing, it is not finished.
7. **Give it a home and a version.** Owner, location, change log. Otherwise the next person rewrites it blind.

That is short enough to be remembered and specific enough to be reviewed.

### The sub-concepts

**Practice, trick, policy — label them.** Practice: works across models and tasks (supply facts). Trick: worked on one model family in one period (elaborate role stacks, "take a deep breath", threats). Policy: an organisational decision wearing prompt clothing ("never offer compensation"). Only practice goes on the list; tricks go in a "retired" appendix; policies go to whoever owns the policy.

**Retired practices are part of the list.** A best-practice document without a retired section accumulates folklore. Say plainly: do not start with "act as a world-class expert"; do not repeat an instruction for emphasis; do not make the prompt longer to make it seem thorough.

**Reviewability beats elegance.** The best practice a team can actually enforce is one that can be checked by reading the prompt for two minutes. "Be clear" cannot be reviewed. "Every prompt that runs on a schedule has a failure line" can.

**Practices cost something.** A failure line costs a sentence and, occasionally, an output the team must handle. Honest lists say what the practice costs, or they get quietly abandoned.

**One practice at a time.** Teams that adopt seven habits at once adopt none. Pick the one whose absence caused the last incident.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A6` (Prompt Design); see that entry for the user-level habits of clear task, supplied facts, stated limits and checking the reply. `TSC3-Basic-A1` supplies the element vocabulary these practices attach to, `TSC3-Basic-A8` is the misuse list they are designed to prevent, `TSC3-Basic-K7` is where the failure-line practice becomes a guardrail, and `TSC3-Basic-A3` is how you prove a practice actually helps rather than merely sounds right.

### What is current as of November 2026

Two practices have strengthened and two have weakened. Strengthened: supplying a labelled source and stating an output schema, because current models follow structure far more reliably than rhetoric, and because structured output modes reward specifying shape. Weakened: persona framing and length-as-thoroughness, both of which the current generation of models — the GPT-6 line, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon among them — largely ignore in favour of explicit rules.

The newer practice that belongs on the list: **decide what the model may do, not just what it may say.** With tool-using assistants in ordinary workflows, a prompt without a permissions decision is half a design.

### Common misconceptions

- *"Best practice means the longest prompt."* Length is a cost. The practices above shorten prompts as often as they lengthen them.
- *"Politeness improves output."* On current models, "please" is courtesy, not control. Structure is control.
- *"If it worked for someone on LinkedIn, it is practice."* That is a trick with an audience.
- *"Practices are optional once you are experienced."* Experience is mostly the judgement of when a practice does not apply — which requires knowing it exists.

## How a student should understand it

**Mental model:** the food-hygiene grade on the stall. It does not measure whether one plate was delicious; it measures whether the process makes a bad plate unlikely on a bad day.

**Things they can do after this bullet:**
1. State the failure each practice prevents, in one line.
2. Sort a list of prompt advice into practice, trick and policy.
3. Review someone else's prompt against the seven and name the two most important gaps.

**Misconceptions to kill:** that practices are tricks; that a long prompt is a careful prompt; that a practice without a stated cost will be followed.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hygiene grade.** Grade A is not a promise about today's chicken rice; it is evidence that the process survives a busy Saturday and an inspector. Where it breaks: inspections are external and periodic, while prompt review is internal and rare — which is why the list has to be short enough for a colleague to apply without an inspector.

**The pre-flight checklist.** Pilots run the same items every time, not because they forgot, but because the cost of one missed item is not recoverable in the air. Where it breaks: a checklist item is binary, while prompt practices are matters of degree — so the review asks "is there a failure line" rather than "is the failure line good".

### Worked example with a real tool

Take a prompt a team wrote for a recurring job — drafting responses to online reviews:

```text
You are a world-class customer experience expert. Please carefully and
thoroughly analyse the following review and write a thoughtful, professional
response that addresses all the customer's concerns in a warm and helpful way.
Make sure it is good.
```

Then the reviewed version, with each practice visible:

```text
Draft a public reply to the customer review below. [task, one verb]

Use only the facts in the review and the case note. [facts supplied]
If the review mentions a refund and the case note has no refund amount,
write "NOT IN SOURCE" instead of stating an amount. [failure line]

Reader: other prospective customers, not the reviewer. [reader]
Limits: 90 words, no discounts, no dates, no naming of staff. [constraints]
Shape: two short paragraphs; first acknowledges, second states one action.
[format]
Done means: a reader can tell what the business did about it. [done-check]
```

What to point at afterwards: the reviewed version is shorter in adjective count and longer in decision count. Then remove the failure line and run both on a review mentioning an amount that is not in the case note — the difference is one invented figure, and that is the entire argument for the list.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read the "world-class expert" prompt aloud and ask what it will actually control.
2. **State the objective** — by the end you will review a prompt against seven practices and name the two gaps that matter.
3. **Recall prior learning** — ask what their organisation's safety or hygiene checklist does, and why it is short.
4. **Present the content** — teach the seven with their failures, then the practice/trick/policy split, then the retired list.
5. **Guide** — review the review-reply prompt together, arguing about which gap is most expensive.
6. **Elicit performance** — pairs review a prompt from their own work and rewrite only the two highest-value gaps.
7. **Give feedback** — run before and after on one hard input. If nothing changes, the pair picked the wrong gaps.
8. **Transfer** — each learner adds one item to their team's checklist and removes one retired trick.

## What the framework doesn't mention but trainers need to know

- **Checklists are adopted through incidents.** The practice that gets followed is the one attached to the failure people remember. Use the room's own examples.
- **Politeness and personas are the hardest habits to retire.** They feel like skill. Show a persona-only prompt and a rules-only prompt on the same task, side by side, and let the output argue.
- **Best practice is not uniform across risk levels.** A prompt for internal brainstorming and a prompt for a customer refund need different rigour. Say which tier you are teaching.
- **A practice nobody owns decays.** The failure line written in March is wrong in September when the process changes. Assign the review, not just the practice.

## Watch out

- **Do not teach a list of twenty.** Nobody remembers twenty, and a list nobody remembers cannot be a standard.
- **Do not present tricks as practice.** It dates the course and it teaches learners to collect rather than diagnose.
- **Do not skip the cost of each practice.** Practices with hidden costs are the ones quietly dropped.
- **The stale claim to retire:** "be polite and say please, it improves results." Courtesy is for humans. Constraints are for models.
