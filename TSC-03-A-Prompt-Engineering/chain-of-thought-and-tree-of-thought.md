---
id: 03.03.A.K4
tsc: 3
level: Advanced
code: K4
title: Chain-of-Thought and Tree of Thought
as_at: 2026-11-26
review_by: 2027-02-25
---

# Chain-of-Thought and Tree of Thought

> **TSC #3 Prompt Engineering · Advanced · Knowledge K4**

> **Framework text (verbatim):** "Advanced prompt techniques (e.g., Chain-of-Thought, Tree of Thought prompting)."
>
> **TSC #3** Prompt Engineering · **Advanced** · Knowledge · Bullet 4 of 13

**One-line version:** Chain-of-Thought buys the model a working-out page — more generated tokens before it commits to an answer; Tree of Thought buys it several candidates and a reason to discard some.

## What it is

**Chain-of-Thought (CoT)** instructs the model to produce intermediate steps before the final answer, either by a trigger phrase ("work through this step by step") or by worked examples that show the steps. **Tree of Thought (ToT)** generalises it: generate several candidate next steps, evaluate them, abandon the dead ends, and continue down the best one. Both are ways of spending more generated text — and therefore more computation — before the answer is fixed. Neither makes the model correct; both make some classes of error less likely and others easier to see.

## Deep expansion

### The concept

A model writes one token at a time, and every token it has already written is context for the next. The consequence is mechanical: an answer produced on the first token has exactly one token's worth of computation behind it, while an answer produced after four hundred tokens of working has four hundred tokens of conditioning. "Think step by step" is not an instruction to think; it is an instruction to *spend tokens on intermediate states*, which changes what the final token is conditioned on.

That explains the pattern of results. CoT helps where the answer depends on several intermediate quantities — arithmetic, multi-condition eligibility, rostering under constraints, a chain of policy rules. It does nothing where there is nothing to compute: a lookup, a definition, an extraction from a document you supplied. Applying it there costs tokens, latency and, on some tasks, accuracy, because the model fabricates a rationale for an answer it already knew.

ToT adds search. Instead of one path, the model produces several candidate first steps, judges them, drops the weak ones and proceeds. That is the right shape for combinatorial problems — sequencing, scheduling, architecture choices — where an early wrong assumption poisons everything downstream and backtracking is the only recovery.

### The sub-concepts

**Zero-shot CoT.** A trigger phrase appended to the task. Cheapest form, works on multi-step logic, and is the version learners will actually use.

**Worked-example CoT.** Examples that demonstrate *your* steps, not generic ones. Essential where the organisation has a required procedure — an underwriting rubric, a claims checklist — that the model would not invent.

**Self-consistency.** Run the same CoT prompt several times at a non-zero temperature and take the majority answer. It trades cost for reliability on tasks with a discrete answer, and it is useless for open writing, where outputs cannot be voted on.

**Plan-and-solve, least-to-most, step-back.** Variants that put the structure in the prompt: plan then execute; decompose then solve in order; state the principle then apply it. Each fixes a specific failure — skipped steps, missed sub-problems, distraction by surface detail.

**Tree of Thought is an architecture.** Branch, evaluate, backtrack, continue. In a single prompt ("consider three experts who disagree, then decide") the branches tend to collapse into agreement within a paragraph, because the model is optimising for a coherent essay, not a search. Real ToT needs separate calls or explicit scoring.

**The steps are text, not a transcript.** A model that reaches a wrong answer can produce a convincing derivation of it. The written reasoning is evidence about the answer, not proof of how it was reached — so verification beats introspection.

### How it connects to the rest of the framework

Bullet 3 (`TSC3-Advanced-K3`) is where the reasoning field must sit inside a structured output — before the label, never after. Bullet 6 (`K6`) is where CoT gets measured against its cost. Bullet 9 (`A3`) supplies the rubric that catches a fluent derivation ending in a wrong number. Bullet 13 (`A6`) composes CoT into staged pipelines, and Bullet 5 (`K5`) supplies the thing that actually settles arithmetic: a tool.

### What is current as of November 2026

Current frontier models increasingly plan before answering without being asked. Three practical consequences:

- **Forcing verbose CoT on a model that already reasons can hurt.** It adds latency, inflates output length, and sometimes derails a plan the model had already formed. Ask for the answer plus a short justification, and ask for the full derivation only when you need to audit it.
- **The skill moved from eliciting steps to specifying and checking them.** What is scarce now is not a prompt that says "think step by step" but one that names the steps the organisation requires and defines what makes the answer acceptable.
- **ToT survives as multi-candidate generation.** Generating several options in parallel and selecting against explicit criteria is cheaper and more reliable than simulating branching inside one prompt — which is why it now looks less like a prompting trick and more like a pipeline.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Step by step means correct."* It means more computation, not correct computation. A confidently wrong derivation is common.
- *"The model shows how it thought."* It shows plausible text that supports its answer. Those are different objects.
- *"Tree of Thought is asking for three opinions."* Without branch evaluation and pruning, three opinions become one blended opinion.
- *"CoT helps every task."* It is wasted on lookups and can degrade simple classification.
- *"More reasoning is always better."* Past the point where the answer is determined, extra steps add cost and new opportunities for error.

## How a student should understand it

**Mental model:** the exam scratch paper. Nobody multiplies 17 by 24 in half a second; everybody can do it with a page and thirty seconds.

**Things they can do after this bullet:**
1. Explain why intermediate steps help on multi-step tasks but not on lookups.
2. Write a CoT prompt for a workplace calculation with the steps they require named.
3. Decide when a branching approach is worth its cost, and when one answer plus a check is enough.

**Misconceptions to kill:** that reasoning text proves correctness; that ToT is a phrase; that CoT is a default.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Blurting versus scratch paper.** Ask the room: "17 times 24, answer in half a second, first number that comes out." Somebody says 380. Give them paper and the same thirty seconds and they get 408. Where it breaks: a person's scratch paper is private and reliable; the model's is part of the output, so it changes the answer it is reasoning toward — which is why the written steps need checking, not trusting.

**The chess player's three lines.** Before moving, a strong player sees three continuations, rejects two, and plays the third. That is ToT: branching, evaluating, discarding. Where it breaks: the player has a lifetime of evaluation built in; a model's evaluation is another generation, and a weak evaluator makes branching expensive theatre.

### Worked example with a real tool

```text
A clinic sees 42 patients a day. Each visit takes 12 minutes. How many
full-time nurses are needed if each works 7.5 hours? Work step by step and
show each calculation.
```

The output should show minutes per day (504), minutes per nurse (450), the division (1.12), and then flag that 1.12 nurses means two people or one plus overtime. Point at the last step: the arithmetic is exact and the *decision* is still a judgement, which is where a human belongs.

Then run the same question without "work step by step" and compare. Often the answer is right and the working is absent — which is fine if you only needed the number, and useless if you have to defend it to an auditor. Then run a ToT-flavoured version for the rostering variant: ask for three candidate rosters, the constraint each one violates, and a recommendation. Point at how much longer it is, and ask whether the extra length changed the decision.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — the 0.5-second multiplication, then the paper.
2. **State the objective** — write a step-naming CoT prompt, and judge when branching is worth the cost.
3. **Recall prior learning** — how they show working in a tax computation or a claim form, and why the assessor wants it.
4. **Present the content** — why tokens are compute; the three CoT forms; ToT as search; the verification rule.
5. **Guide** — run the nurse calculation together; annotate each step; then run it with a wrong premise to show a confident wrong derivation.
6. **Elicit performance** — learners write a CoT prompt for a rostering or budget task of their own, naming the steps their organisation requires.
7. **Give feedback** — test two learners' prompts on a deliberately ambiguous input; debrief where the steps drifted.
8. **Transfer** — each learner adds a "show the calculation, then state the answer in one line" rule to a prompt they will reuse.

## What the framework doesn't mention but trainers need to know

- **Separate the working from the deliverable.** A CoT answer pasted into a client email reads like a transcript of anxiety. Ask for the working in one block and the answer in another, or the reader gets both whether they want them or not.
- **CoT is not a substitute for a tool.** Arithmetic, date maths and counting should go to a calculator or code. Teaching CoT as the fix for arithmetic teaches a workaround, not a solution.
- **Visible reasoning is a disclosure decision.** If the prompt handles customer data, the derivation may quote it. Decide whether the working is shown or logged, and note that some models return only a summary of their thinking — which pushes the verification burden onto the output and its sources.

## Watch out

- **Do not demo only successes.** Show a case where the steps are fluent, the arithmetic is wrong, and the model is unbothered.
- **Do not teach CoT as a universal upgrade.** It is a tool for multi-step logic and a waste elsewhere.
- **Do not let "consider three experts" pass as Tree of Thought.** Show what real branching costs and requires.
- **Do not confuse a longer answer with a better one.** Length is a by-product of reasoning, not the goal.
- **The stale claim to retire:** "just add 'think step by step' and it becomes reliable." In November 2026 that phrase is often redundant — and reliability comes from named steps and an external check.
