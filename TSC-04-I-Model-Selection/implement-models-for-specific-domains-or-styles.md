---
id: 04.02.I.A2
tsc: 4
level: Intermediate
code: A2
title: Implement models for specific domains or styles
as_at: 2026-11-26
review_by: 2027-02-25
---

# Implement models for specific domains or styles

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A2**

> **Framework text (verbatim):** "Implement models to create content in specific domains or styles."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Ability · Bullet 7 of 11

**One-line version:** A general model will write like a textbook until you show it three examples of how your organisation writes — examples are the mechanism, adjectives are decoration.

## What it is

Steering a model into a domain (clinical notes, legal correspondence, insurance wording, marketing copy) or a style (formal, plain-English, playful, terse) is done in four moveable parts: a role statement, a set of few-shot examples, a vocabulary and exclusion list, and an output contract. Implementing means assembling those parts so the result is repeatable, then attaching a check that catches drift.

## Deep expansion

### The concept

Style is a statistical pattern, not an instruction. Saying "write formally" moves the distribution slightly; showing two sentences of genuine formal correspondence moves it much further, because the model now has concrete continuations to match. Domain language works the same way — the fastest route to correct terminology is a sample that contains it.

The reliable recipe, in order:

1. **Role and audience** — who is writing, who is reading. This fixes register more cheaply than any adjective.
2. **Two or three examples** of real output in that voice, including one that is deliberately unremarkable. Exemplars that are too clever skew the output toward imitation of the exemplar rather than the register.
3. **Vocabulary in, vocabulary out** — the terms that must appear, and the terms that must not (jargon, competitor names, informal particles, emoji).
4. **Output contract** — length, structure, and what to do when the source material is insufficient.

Style drift is the characteristic failure: a long generation starts in the right register and decays toward generic prose by the fourth paragraph. The fix is either a shorter output, an example placed at the end as well as the start, or a self-check instruction.

### The sub-concepts

**Show, do not describe.** One example outranks a paragraph of style guidance. Two outranks one. Past three, returns collapse and token cost climbs.

**Separate domain knowledge from domain voice.** Knowledge comes from the source material you paste or retrieve. Voice comes from examples. Conflating them produces prompts that try to teach facts through style samples, which produces fluent fabrication.

**Constrain the things that leak.** Models default to American spelling, Western date formats, first names only, and generic corporate phrasing. For a Singapore deployment, specify: British spelling, DD Month YYYY dates, full names on first reference, local institution names spelled correctly. These are small, verifiable instructions that make output look professionally local.

**Use structured output for anything downstream.** A style that must also parse is two constraints; enforce the schema and let style live in the prose fields.

**Fine-tuning is the escalation, not the starting point.** When a style must hold across thousands of varied inputs and examples alone will not hold it, an adapter trained on a few thousand approved samples is the durable answer — and it becomes a maintained asset.

**Test style with a rubric, not a feeling.** Three binary checks — does it use our terminology, is it free of banned terms, is it within the length band — turn a taste argument into a measurement.

### How it connects to the rest of the framework

`TSC4-Intermediate-K2` is the prompting foundation this applies. `TSC4-Intermediate-A4` is the quality-and-coherence check applied to the output. `TSC4-Advanced-A1` places this on the wider adaptation ladder — style is usually a prompt problem before it is a tuning problem. `TSC4-Intermediate-K5` explains what a style fine-tune actually learns from its data.

### What is current as of November 2026

With current frontier models, style control has become more reliable and less mysterious:

- **Instruction following on register improved markedly.** Models now hold a house voice across a long document far better than two generations ago, which retires the "it always drifts by paragraph four" complaint in most cases.
- **Style anchoring via examples remains the strongest lever.** Longer context makes it cheap to include several full exemplars; three to five is now practical where one was once the limit.
- **Adapter-based brand voices are a productised service.** Where a voice must be indistinguishable across a large content operation, fine-tuning on approved copy is offered as a platform feature rather than a research project.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Say it is formal and it will be formal."* It will be slightly more formal. Show it, or accept the drift.
- *"One example is enough."* One example is a hint; two is a pattern; three is a register.
- *"The model knows our terminology."* It knows plausible terminology in your industry, which is not the same as yours.
- *"Style is cosmetic."* In regulated correspondence, style is compliance — a wrongly phrased commitment is a liability, not a tone issue.

## How a student should understand it

**Mental model:** a new speechwriter. You do not describe the CEO's voice in adjectives; you hand over three speeches and say "like this, not like that".

**Things they can do after this bullet:**
1. Steer a model into a named house style using role, two examples and an exclusion list.
2. Fix localisation defaults (spelling, dates, names) with explicit constraints.
3. Write three binary checks that catch style drift without a debate.

**Misconceptions to kill:** that adjectives control style, that domain vocabulary equals domain accuracy, and that style work is finished when the first output looks right.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The letters from a law firm.** Every firm's correspondence reads recognisably the same across partners. Nobody wrote a style guide that achieved that; they circulated precedents. Examples, in other words.

**The school teacher's red pen.** Marking a piece "be more formal" changes little; marking it against a model answer changes a lot.

### Worked example with a real tool

Two examples in, one rewrite out:

```text
Here are two sentences in our house style:
1. "We acknowledge receipt of your claim dated 3 November 2026 and
   will respond within ten working days."
2. "Please note that late submissions cannot be considered under
   clause 4.2 of the agreement."

Rewrite the following casual note in that style, under 40 words,
British spelling, no contractions, no exclamation marks:
"hey, got ur form but it's late so we can't process it, sorry!"
```

What to point at afterwards: the rewrite should be formal, cite the clause pattern, drop the apology, and stay terse. Then remove the examples and re-run — the output becomes generic and warmer. That contrast is the entire lesson, and it takes ninety seconds. Finally, ask the model to write four paragraphs instead of one, and watch the register sag by the third. Now the room understands why the check exists.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — same note rewritten with and without examples, side by side.
2. **State the objective** — by the end you can assemble role, examples, exclusions and contract for a named voice.
3. **Recall prior learning** — few-shot prompting and why continuation probability is steerable.
4. **Present the content** — the four parts, drift, localisation defaults, the rubric.
5. **Guide** — build the legal-tone prompt together on screen.
6. **Elicit performance** — pairs build a prompt for their own organisation's voice.
7. **Give feedback** — run two pairs' prompts on the same input and compare registers.
8. **Transfer** — each learner writes three binary style checks for a document type they produce.

## What the framework doesn't mention but trainers need to know

- **Exemplars carry content as well as style.** A model will happily borrow facts, figures and even names from your example. Use generic exemplars, or scrub them.
- **Style prompts fight output length.** Long generations drift. If the document is long, generate section by section with the contract repeated.
- **Terminology is a compliance surface.** In insurance and healthcare, a near-synonym can change the meaning of a commitment. Maintain a banned-terms list and test for it.
- **A style guide is the real deliverable.** The prompt is a by-product. If the organisation cannot write down its voice, the model will reflect that ambiguity faithfully.
- **Fine-tuning a voice is a maintenance contract.** Voices change with rebrands and regulators; an adapter must be retrained.

## Watch out

- **Do not use a real client letter as an exemplar.** Scrub it. Models reproduce structure and occasionally substance.
- **Do not judge style on one output.** Run three inputs; drift shows up across inputs, not within one lucky generation.
- **Do not claim a model "sounds like us" without a rubric.** That is how a brand team loses an argument it should win.
- **The stale claim to retire:** "we need to fine-tune to get our tone." In November 2026, three examples usually get you most of the way, and the rest is a decision about durability.
