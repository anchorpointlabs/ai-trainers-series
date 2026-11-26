---
id: 03.01.B.K3
tsc: 3
level: Basic
code: K3
title: Prompt construction techniques, and when each one earns its keep
as_at: 2026-11-26
review_by: 2027-02-25
---

# Prompt construction techniques, and when each one earns its keep

> **TSC #3 Prompt Engineering · Basic · Knowledge K3**


> **Framework text (verbatim):** "Techniques in prompt construction (e.g., zero shot prompting, one shot prompting, domain-based prompting techniques, instruction prompting, hyper-parameters such as temperature and sampling parameter)."
>
> **TSC #3** Prompt Engineering · **Basic** · Knowledge · Bullet 3 of 15

**One-line version:** Every construction technique fixes one specific kind of wobble and charges a specific price — the practitioner's skill is choosing by the failure, not by the fashion.

## What it is

Prompt construction techniques are the named ways of assembling a prompt: stating the task directly, supplying no examples or one or several, adding the rules of a particular field, and setting the generation parameters that control how the model samples its answer. At this level, knowing the names is not the skill. Choosing between them, and knowing what each one costs you afterwards, is.

## Deep expansion

### The concept

The framework lists these techniques as if they were a menu of equivalent options. They are not. Each one exists because a particular failure kept happening, and each one imports a maintenance obligation with the reliability it buys.

**Instruction prompting** is the default: a plain statement of the task with explicit constraints. It is the cheapest to write, the easiest to review, and the most portable across models. It fails when the output shape is unusual enough that the model has no strong pattern for it — a very specific house format, an in-house taxonomy, a naming convention.

**Zero-shot prompting** adds no example at all. It works well when the task is common in the model's experience — summarise, classify into obvious categories, rewrite in plain English. It fails on house conventions, because there is no way for the model to know that your organisation calls a refund a "service recovery".

**One-shot and few-shot prompting** supply worked examples, and they are the only reliable way to teach a dialect: your categories, your column names, your tone, the detail a borderline case deserves. The price is threefold — context consumed; a specification in disguise, which must change when the policy changes; and leakage, because a model shown one complaint about a late delivery will happily borrow its phrasing, or its facts, into the next answer.

**Domain-based prompting** injects the rules of a field. It is the most under-used technique and the most misunderstood, because it is usually taught as a persona. "You are an experienced lawyer" adds almost nothing; "apply these three clauses and this fee schedule, and flag anything the schedule does not cover" adds a great deal. Rules outperform roles: a persona tells the model who to sound like, rules tell it what to do.

**Hyper-parameters** — temperature and the sampling controls such as top-p — govern how the model picks among plausible continuations. Temperature near zero makes the choice conservative and repetitive; higher values spread it. Two practitioner facts: these settings control variance, not quality, and most chat interfaces do not expose them. Where they are hidden, you compensate in words — "give me five options, none repeating a word from the brief" does some of what a higher temperature does; "choose the most conservative option and say why" does some of what a lower one does.

### The sub-concepts

**Choose by failure.** Ask what went wrong last time. Format drift points to examples or an output schema; wrong categories point to definitions, not examples; generic tone points to missing reader information. Nothing here is solved by "a better prompt" in the abstract.

**Examples teach the boundary, including a bad one.** A single borderline example silently defines where the line sits. If your one example of "urgent" is arguable, every later classification inherits the argument.

**Instructions generalise; examples localise.** An instruction covers a family of inputs. An example covers a neighbourhood around itself. For a task with wide input variety, instruction plus a schema usually beats a pile of examples.

**Instruction hierarchy.** A prompt lands in a layer: system, developer or user. Team prompts belong in the durable layer, not retyped each time. A rule placed in a user message loses to a rule placed above it, and learners who only use chat never see this.

**Determinism is not on the menu.** Low temperature reduces variation; it does not guarantee the same answer tomorrow, because the model behind the endpoint may have been updated. A workflow that depends on exact repetition depends on a pinned model version, not on temperature zero.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-K5` (Prompt Design); see that entry for the user-level basics of each technique. `TSC3-Basic-K2` explains why any of them work at all, `TSC3-Basic-K7` covers the guardrails that sit above prompt-level tricks, and `TSC3-Basic-A2` is the ability to describe a technique clearly enough that a colleague can choose it without you.

### What is current as of November 2026

Three shifts have changed the selection calculus. Reasoning-capable models now expose a thinking budget as a de facto parameter: more deliberation helps on multi-step tasks and adds latency with little gain on simple ones, so the old advice "always use the biggest setting" is wrong in both directions. Structured output modes let you enforce a schema instead of describing one, which has made format-by-example less necessary. And prompt caching has made a long block of reference material or examples cheaper to reuse, which changes the economics of few-shot without removing its maintenance cost.

What has not changed: models still follow literal instructions more faithfully than rhetorical ones, which is why injecting rules beats assigning a persona on every current frontier family.

### Common misconceptions

- *"Few-shot always beats zero-shot."* It beats it on format and house conventions, and loses to a clear instruction plus a schema on wide-variety inputs.
- *"Temperature zero gives the same answer every time."* It reduces variation within one model version. It does not survive a model update.
- *"Domain prompting means telling it to act as an expert."* Roles change the accent; rules change the behaviour.
- *"More examples means more reliable."* More examples mean more to maintain, more context spent, and more chances for one bad example to define the boundary.

## How a student should understand it

**Mental model:** a toolbox where each tool fixes one wobble — and the person who reaches for the heaviest tool every time ends up with a prompt nobody dares to edit.

**Things they can do after this bullet:**
1. Name the failure they are trying to prevent, then choose the technique that prevents it.
2. Write a domain block as rules rather than a persona.
3. Explain what they lose by adding examples — context, maintenance, leakage.

**Misconceptions to kill:** that techniques are interchangeable; that a persona is a domain specification; that examples are free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The station announcement.** An MRT announcement is a template with blanks — that is instruction prompting. A recording of last week's announcement is one-shot: it shows you the rhythm and the register. The station-specific rules ("escalator closed, use Exit B, no bridging to the next platform") are the domain block, and they are the part that goes stale when the station is renovated. Where it breaks: a station announcement is read aloud identically every time, while the model will re-compose the template each run unless the format is enforced.

**Measured versus agak-agak.** A recipe that says "one teaspoon" behaves like low temperature: the same dish every time, and a bad dish repeated faithfully. "Season to taste" behaves like high temperature: sometimes excellent, occasionally inedible. Where it breaks: a cook tastes and adjusts; the model has no spoon.

### Worked example with a real tool

Task: sort 200 free-text feedback comments into four internal categories. First attempt, zero-shot:

```text
Classify each comment below as Service, Product, Billing or Other.
Reply with the category only, one per line, in the same order.

Comments:
1. Waited 40 minutes and nobody told me the queue was for collection only.
2. The app logged me out twice and lost my basket.
```

It will get most right and will miss the house distinction the team cares about — that a queue-management complaint counts as Service, not Other. So add one example, chosen deliberately at the boundary:

```text
Example:
Comment: "The queue snaked past the lift lobby and staff kept serving
walk-ins. I gave up."
Category: Service

Now classify the following, same rules. If a comment could fit two
categories, choose Service and add "//ambiguous" after the category.
```

What to point at afterwards: the example fixed the boundary and also fixed the output format — one clause did two jobs. Then point at the cost: that example is now part of the specification, so if the team redefines the category, the example must be updated by whoever owns the prompt, not by whoever notices.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show three outputs from the same task using zero-shot, one-shot and a domain block, and ask the room to guess which was which from the outputs alone.
2. **State the objective** — by the end you will pick a technique by naming the failure it prevents, and you will write the domain block as rules.
3. **Recall prior learning** — ask how they brief a relief driver on a delivery route: the destination (instruction), one run-along (example), the estate's quirks (domain).
4. **Present the content** — teach the five techniques as five prices, then parameters as variance control.
5. **Guide** — convert a persona prompt ("act as a lawyer") into a rules prompt together.
6. **Elicit performance** — pairs take one recurring task and write two versions: instruction-plus-schema, and one-shot. Both must state what they cost.
7. **Give feedback** — run both on the same messy input, compare, and name which failure each version prevented.
8. **Transfer** — each learner identifies which of their prompts is secretly an example-driven spec that nobody owns.

## What the framework doesn't mention but trainers need to know

- **Examples become specifications.** If the prompt is shared, the example is a policy. That is an ownership question, not a wording question.
- **Few-shot has a runtime cost.** Long example blocks consume context and add latency. For a prompt run fifty times a day, that is a real operating cost, not a theoretical one.
- **The persona habit is hard to unlearn.** Learners arrive believing "act as a senior accountant" is expertise. Show a persona-only prompt failing next to a rules-only prompt succeeding on the same question.

## Watch out

- **Do not demo temperature in an interface that has no temperature control.** It is the most common way to lose a Basic room, and the setting is invisible in every mainstream chat product.
- **Do not stack personas.** "You are a world-class expert lawyer who is also a teacher and a CFO" reads as noise and produces a confused register.
- **Do not let one-shot examples carry policy the room has not agreed.** The example is the strongest part of the prompt; whatever it encodes will be followed.
- **The stale claim to retire:** "turn the temperature up for creativity." Temperature turns up variance. Whether the result is creative or merely erratic is not something the dial decides.
