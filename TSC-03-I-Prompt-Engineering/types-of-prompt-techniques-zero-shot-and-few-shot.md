---
id: 03.02.I.A3
tsc: 3
level: Intermediate
code: A3
title: Types of prompt techniques — zero-shot and few-shot
as_at: 2026-11-26
review_by: 2027-02-25
---

# Types of prompt techniques — zero-shot and few-shot

> **TSC #3 Prompt Engineering · Intermediate · Ability A3**

> **Framework text (verbatim):** "Identify the types of prompt engineering techniques (e.g., zero-shot and few-shot learning applied to foundation models)."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Ability · Bullet 9 of 13

**One-line version:** Zero-shot is asking and few-shot is showing — the choice is about where the pattern lives, in the words or in the examples.

## What it is

Zero-shot prompting gives the instruction with no worked example. One-shot gives exactly one input/output pair. Few-shot gives two to ten. Many-shot stuffs hundreds into a long context. The technique family exists because models learn patterns from examples placed in the prompt, so you can specify a format, a house style or a decision boundary by demonstration rather than description.

## Deep expansion

### The concept

Instruction and demonstration are two different ways of specifying the same task, and they fail differently. An instruction states the rule and relies on the model's ability to generalise from language. A demonstration shows the rule in action and relies on pattern-matching — which is the model's strongest ability, and the reason a single well-chosen example often beats a paragraph of adjectives like "professional" or "concise".

The mechanism is in-context learning: without changing a weight, the model picks up a pattern from what is in front of it. That is why the examples must be chosen, not collected — whatever is in them becomes part of the specification, including the parts you did not intend.

### The sub-concepts

**Zero-shot wins more often than learners expect.** For tasks well represented in training — summarise this, translate that, write a function — an instruction plus a format is enough, and it is the cheapest and fastest option. Reach for examples when the *format* is idiosyncratic or the *boundary* between categories is subtle.

**One-shot is a template, and templates over-generalise.** With a single example the model copies incidental details: if the example review is positive, the next answer skews positive; if the example uses a name, that name reappears. One example is best when all you need is layout — a report skeleton, an invoice header, a letter's shape.

**Few-shot is the workhorse, with two known biases.** Majority label bias: if four of five examples are APPROVED, the model over-predicts APPROVED. Recency bias: whichever label appears last gets an extra pull. Balance the classes, vary the order, and check the confusion on a small test set rather than trusting the examples to be neutral.

**Contamination is the quiet failure.** Models reuse names, figures and phrasing from examples in unrelated answers. The fixes are mechanical: abstract placeholders like [COMPANY_A], examples spread across different domains, wrapping in `<example>` tags, and an explicit rule — "do not reuse facts from the examples in your answer".

**Contrastive examples break stubborn boundaries.** When a model keeps confusing two categories, show one correct output and one incorrect output with a reason why it is wrong, clearly tagged. Positive examples alone teach the shape; a bad example teaches the edge.

**Few-shot chain-of-thought is a different technique wearing the same clothes.** The examples show the reasoning steps, not just the answer — which is how you transmit an organisation's particular method (an underwriting rubric, a leave-entitlement test) that a generic "think step by step" will not reproduce.

**Many-shot is now practical, and still expensive.** Hundreds of examples in a long context can adapt a model to a rare format or a legacy codebase when fine-tuning is unavailable. Without prompt caching the cost and latency are punishing, and poor ordering still degrades attention.

### How it connects to the rest of the framework

`TSC3-Intermediate-K1` places demonstration among the five frameworks. `TSC3-Intermediate-A4` is the matching decision — when examples rather than reasoning or decomposition are the right intervention. `TSC3-Intermediate-A5` covers the model-specific twist: reasoning tiers need fewer examples and can be hurt by many. `TSC3-Intermediate-K5` names the use cases where examples earn their tokens, chiefly classification and house style.

### What is current as of November 2026

Three changes and one constant.

- **Format examples have been partly replaced by schemas.** With native structured output in the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon, you no longer need three examples to teach JSON shape — you need a schema. Examples are now spent on *judgement*, not punctuation.
- **Reasoning tiers need fewer examples.** A deliberating model often performs worse with heavy few-shot scaffolding, because the examples compete with its internal process. Test with zero or one before adding more.
- **Many-shot is viable with caching.** Static example blocks at the front of a prompt are cheap to reuse, which makes dozens of examples affordable for a narrow, high-volume task.
- **The constant:** example selection is still a data problem. A biased or contaminated example set produces a biased, contaminated prompt no matter how good the model is.

### Common misconceptions

- *"More examples are always better."* Past a handful, the returns flatten and the biases accumulate. Examples fix format and boundaries, not missing facts.
- *"Examples are only about formatting."* They set tone, length, decision boundaries and implicit content — which is why contamination happens at all.
- *"Zero-shot means no context."* It means no worked example. You still supply the document, the constraints and the output shape.
- *"Examples are neutral."* They are a specification with a distribution. If every example is a happy case, you have taught the model that happy cases are the norm.

## How a student should understand it

**Mental model:** teaching a new hire. You can describe how to fill in the claim form (instruction), or hand them two completed forms from last month (demonstration). The second works faster — and it also teaches them whatever was odd about those two forms.

**Things they can do after this bullet:**
1. Convert a zero-shot prompt into few-shot and say what the examples are meant to control.
2. Decide, for a given task, whether examples or a clearer instruction is the cheaper fix.
3. Audit an example set for label imbalance, contamination and accidental facts.

**Misconceptions to kill:** that more examples always help; that examples only carry format; that zero-shot means context-free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The folder of sample letters.** Every office has one — "follow this format". New staff copy the shape and accidentally copy the client's name too. That accident is contamination, and it is worth showing live.

**The driving instructor.** Some things you demonstrate ("check mirror, signal, turn"), some you describe. Demonstration wins for sequences that are hard to put into words; description wins when the sequence is simple and the demonstration would take ten minutes.

### Worked example with a real tool

Release notes, three ways:

```text
ZERO-SHOT
Write a product update in the style of our release notes.

ONE-SHOT
Here is one of our release notes:
---
Version 4.2 — Faster exports
Exports now finish in one pass. Saved filters carry over to the new dashboard.
---
Now write one for: bulk delete for saved searches, admin-only, with an undo window.

FEW-SHOT
[two examples spanning a feature, a fix and a breaking change, with
<example> tags and a rule: do not reuse names or numbers from the examples]
```

What to point at afterwards: the one-shot version matches the layout and invents a plausible-but-wrong version number; the few-shot version matches layout *and* the house convention of no exclamation marks; then show an example containing "Acme Corp" and watch it surface in an unrelated answer. Fix it live with the placeholder rule.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a one-shot output that copied the example's customer name.
2. **State the objective** — by the end you can convert a prompt to few-shot and justify each example you chose.
3. **Recall prior learning** — what did they learn about in-context learning and the context window?
4. **Present the content** — zero, one, few, many; then the two biases and contamination.
5. **Guide** — convert the release-notes prompt together, choosing examples deliberately.
6. **Elicit performance** — pairs build a three-example set for a classification task from their work.
7. **Give feedback** — run each set on two borderline inputs; check whether the labels are balanced and the boundary is taught.
8. **Transfer** — each learner writes the example-hygiene rule into their team template.

## What the framework doesn't mention but trainers need to know

- **Examples teach more than you intend.** Length, tone, certainty and even formatting habits transfer. Review examples as you would review the prompt.
- **Some problems cannot be fixed with examples.** Missing facts, stale knowledge and permissioned data need retrieval or a tool, not another sample.
- **Order is a variable.** Alternate the labels; do not finish on a run of the same class.
- **Maintenance cost is real.** Examples age. A house style that changes in July leaves a prompt teaching last year's voice.
- **The reason to prefer instructions:** they are shorter, cheaper and easier to review. Use examples when the pattern resists description, not as a default.

## Watch out

- **Do not build example sets from only successful cases.** The boundary is taught by the awkward ones.
- **Do not let examples carry facts the model should get from the source.** That is how a prompt starts inventing policy.
- **Do not add examples to a reasoning failure.** If the failure is a skipped step, examples of correct steps may help; if it is a missing fact, they will not.
- **The stale claim to retire:** "few-shot always beats zero-shot." On current reasoning models it frequently does not, and it always costs more.
