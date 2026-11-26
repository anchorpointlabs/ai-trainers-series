---
id: 03.02.I.A4
tsc: 3
level: Intermediate
code: A4
title: Apply prompt techniques for use cases
as_at: 2026-11-26
review_by: 2027-02-25
---

# Apply prompt techniques for use cases

> **TSC #3 Prompt Engineering · Intermediate · Ability A4**

> **Framework text (verbatim):** "Apply prompt techniques as necessary for use cases."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Ability · Bullet 10 of 13

**One-line version:** The technique is chosen by the failure you expect, not by which one sounds cleverest — matching is the skill, and applying it means the prompt someone else can run.

## What it is

Applying prompt techniques means selecting the technique whose mechanism addresses the difficulty of a specific task, then building it into a working prompt with a defined output and a failure branch. Few-shot for a format that resists description, chain-of-thought for dependent steps, role for register, schema for parseability, decomposition when one call is carrying several jobs. The skill is the match, not the collection.

## Deep expansion

### The concept

Every technique is a solution to a particular failure, which gives the whole topic a single organising question: **what will go wrong if I write the simplest possible prompt?**

- If the answer is "it will format it differently every time", you need examples or a schema.
- If it is "it will skip a step and get the arithmetic wrong", you need reasoning space or a tool.
- If it is "it will sound like a chatbot", you need a role and a style sample.
- If it is "it cannot know our policy", no prompt technique helps — you need retrieval or a supplied document.
- If it is "it is doing six jobs and failing at three", you need decomposition.

That diagnostic order matters because the most common Intermediate error is reaching for an ambitious technique to fix a problem that is actually missing facts or a missing specification. A chain-of-thought prompt over an absent policy document produces a beautifully reasoned wrong answer.

### The sub-concepts

**A working match table.** Teach it as a lookup, then insist on the test that confirms it:

- **Format or house style** → one or two few-shot examples, or a schema. Test: does the shape hold across five inputs?
- **Multi-step reasoning, policy tests, arithmetic** → chain-of-thought or a reasoning-tier model; arithmetic itself goes to a tool. Test: does the working match the answer?
- **Tone and register** → role plus a style sample, plus three explicit rules. Test: would you send it unedited?
- **Extraction** → field list, schema, verbatim rule, escape hatch. Test: does every value trace to the source?
- **Classification** → label definitions, one label per item, a borderline rule, balanced contrastive examples. Test: do two runs agree on the borderline case?
- **Long document** → summarise or extract the relevant sections first, then ask. Test: is the answer still grounded?
- **High-stakes discrete answers** → self-consistency: run several times, take the majority, or add an explicit verification pass. Test: does the answer survive a second opinion?
- **Repetitive volume** → template with variables plus a chain, not one heroic prompt. Test: does case 200 behave like case 2?

**One technique at a time.** Stack three and you cannot tell which one fixed the failure or which one introduced the next. Apply, test, then add.

**Applying means delivering.** A technique is not applied until it sits in a prompt with an output shape, a failure line and a name, so the next person can run and review it.

**Each technique has a price.** Few-shot costs tokens on every call; chain-of-thought costs latency and output tokens; decomposition costs orchestration and error propagation; self-consistency multiplies cost. Say the price when you recommend the technique, or it will be quietly abandoned.

**The escalation ladder.** Before technique, check the cheaper rungs: does a script solve it? Is a fact missing? Is the output shape unstated? Most "the prompt needs chain-of-thought" diagnoses are "the prompt needs a field list and a number from a calculator".

### How it connects to the rest of the framework

`TSC3-Intermediate-A3` is the family of techniques this bullet selects from, and `TSC3-Intermediate-K5` is the catalogue of use cases that supplies the task shapes. `TSC3-Intermediate-A5` adds the model dimension — the same match produces a different prompt on a reasoning tier. `TSC3-Intermediate-K1` supplies the frameworks, and `TSC1-Intermediate-A2` is the underlying set of uses — summarise, infer, reason, transform, augment — that the tasks belong to.

### What is current as of November 2026

The matching table has shifted because models absorbed some techniques.

- **Reasoning tiers absorbed chain-of-thought.** On the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon, a reasoning tier often out-performs a hand-written "think step by step" instruction. The technique becomes: choose the tier, then ask for the answer, and require the working only where a human must audit it.
- **Schemas absorbed format few-shot.** Native structured output enforces shape, so examples are now spent on judgement rather than braces and quotes.
- **Tools absorbed arithmetic.** For any figure that matters, the match is a tool call, not a better reasoning prompt. This is the single most useful correction at Intermediate level.
- **Decomposition partly absorbed by agents.** Tool-using assistants can plan and chain internally, but explicit chains remain more debuggable for production work — a point worth teaching honestly in both directions.

### Common misconceptions

- *"Collect techniques; more is better."* Techniques are tools with prices. A learner with five well-matched techniques outperforms one with twenty half-understood ones.
- *"Chain-of-thought improves every answer."* It improves multi-step reasoning and wastes tokens on lookup. On a reasoning model it can be redundant.
- *"One prompt can do the whole workflow."* Six jobs in one call is how you get an answer that plateaus and never improves, because you cannot see which job failed.
- *"If the technique did not work, the technique is bad."* More often the diagnosis was wrong: the failure was missing facts, not missing examples.

## How a student should understand it

**Mental model:** the golf bag. You pick the club for the lie, not the shiniest club in the bag — and a golfer carrying one club is not more focused, just worse. Where it breaks: a golf shot has one objective, while a work task often needs two techniques in sequence rather than one.

**Things they can do after this bullet:**
1. State the failure they expect, then name the technique that addresses it, then test.
2. Take a task solved with the wrong technique and re-solve it with the right one.
3. Explain the price of the technique they chose — tokens, latency, maintenance.

**Misconceptions to kill:** that technique equals solution; that chain-of-thought is universal; that one prompt can carry a workflow.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The zi char kitchen.** Wok for stir-fry, steamer for fish, claypot for claypot rice. The cook does not use the wok for everything because it is the biggest. Where it breaks: a kitchen has a fixed menu, while a prompt's "dish" is often invented on the spot — which is exactly why the diagnosis step exists.

**The golf bag.** Fourteen clubs, one swing. Where it breaks: as above.

### Worked example with a real tool

Task: how many staff are needed for a shift.

```text
WRONG MATCH (zero-shot, no reasoning space)
We need 3 cashiers from 10am to 8pm, with a 1-hour break each, and cover must never
drop below 2. How many staff-hours is that?

RIGHT MATCH (reasoning space + a calculator)
Work through this in steps before giving the final number:
1. State the total till-hours required.
2. State the break rule and how it affects coverage.
3. Compute the staff-hours needed, using the calculator for any arithmetic.
4. Then give the answer as: STAFF_HOURS: <number>, ASSUMPTIONS: <bullets>.

Rules: do not estimate if a calculation is possible. If an input is missing,
write NEEDS_INPUT and name it.
```

What to point at afterwards: the first prompt produces a plausible number with no working, and it is often wrong by the break. The second shows its steps, hands arithmetic to a tool, and names its assumptions — so a manager can disagree with the assumption rather than the total. That is the difference between applying a technique and decorating a prompt.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read a confident wrong total from a zero-shot arithmetic prompt.
2. **State the objective** — by the end you can diagnose a task's failure and match one technique to it, with a reason and a price.
3. **Recall prior learning** — what are zero-shot and few-shot, and what does each control?
4. **Present the content** — the diagnostic question, the match table, the escalation ladder.
5. **Guide** — match the shift-staffing task together, arguing for reasoning space plus a tool.
6. **Elicit performance** — pairs take a task from their work, write the expected failure, then the prompt.
7. **Give feedback** — swap and critique: is the technique matched to the stated failure, or to fashion?
8. **Transfer** — each learner names the technique they will stop using by default, and why.

## What the framework doesn't mention but trainers need to know

- **Diagnosis before technique is the whole ability.** Assessment will give a task, not a failure; learners must infer the likely failure to choose.
- **Techniques compose in sequence, not in a pile.** Extract, then reason, then format — three calls, each with one technique.
- **The cheapest intervention wins.** A delimiter, a field list and a failure line fix more production prompts than any advanced technique.
- **Some tasks belong to software.** Counting, totals, reconciliation and permissioned actions are not prompting problems, and saying so is part of teaching the ability honestly.
- **Price the technique out loud.** Chains add latency and error propagation; self-consistency multiplies cost; few-shot adds tokens to every call. Learners who do not hear the price cannot make the trade.

## Watch out

- **Do not teach thirty techniques.** Five, each with a failure and a price, produces judgement. Thirty produces a vocabulary test.
- **Do not demo chain-of-thought as a universal upgrade.** Show it winning on a dependent-steps task and losing on a lookup.
- **Do not let a technique substitute for evidence.** If the model cannot know the policy, no scaffold will supply it.
- **The stale claim to retire:** "add 'think step by step' and accuracy improves." It depends on the task and the model tier — and in 2026, on a reasoning model, often it does not.
