---
id: 03.03.A.K3
tsc: 3
level: Advanced
code: K3
title: Prompt optimisation and sequencing of instructions
as_at: 2026-11-26
review_by: 2027-02-25
---

# Prompt optimisation and sequencing of instructions

> **TSC #3 Prompt Engineering · Advanced · Knowledge K3**

> **Framework text (verbatim):** "Nuances of prompt optimisation and its role in generating tailored outputs (e.g., sequencing of instructions in prompts)."
>
> **TSC #3** Prompt Engineering · **Advanced** · Knowledge · Bullet 3 of 13

**One-line version:** A prompt is read in order and edited one change at a time — sequencing decides what the model weighs, optimisation decides what you actually know.

## What it is

Two ideas share this bullet. **Sequencing** is the order in which a prompt's parts appear: identity, standing rules, examples, source material, the task, the output format. That order is not cosmetic, because a model reads left to right and attends unevenly. **Optimisation** is the loop that improves a prompt against evidence: define the contract, capture a baseline, change one thing, re-measure, keep the version only if the whole set improves.

## Deep expansion

### The concept

Instructions do not arrive simultaneously. The model reads them in sequence, and each part conditions how the next is interpreted — a rule that arrives after a long document has to compete with everything the document already established, while the same rule placed at the end arrives immediately before generation and carries the most weight of all. Order therefore decides not just what is included but what is *operative*.

The second idea is that optimisation is an experiment, not an act of writing. Beginners optimise by rewriting the whole prompt and keeping whichever version feels better; that produces a prompt nobody can explain and no way to tell which change did the work. Experts hold everything still and move one variable: the position of the rules, the presence of an example, the wording of the constraint. Then they re-run every earlier test input, because fixing case fourteen very often breaks case three — a regression that a single-example check will never reveal.

### The sub-concepts

**Write the contract first.** Inputs (what varies), outputs (fields, allowed values, format) and the abstention rule (what to say when the answer is not present). The contract is what makes "better" measurable; without it, optimisation is taste.

**Sequence for attention and for caching.** Standing rules and examples at the top give the model a frame and give the provider a cacheable prefix. The long source sits in the middle. The task, constraints and output schema sit last, right before generation. This ordering satisfies both the attention curve and the cost model.

**Keep the data away from the instructions.** Interleaving instructions through a pasted document is the commonest sequencing error: the model cannot tell which sentences are rules and which are content, and long documents then override the brief.

**Reason before label.** Inside a JSON output, put the reasoning field before the classification field. Generation is left to right, so a label placed first is a guess that the reasoning then rationalises — the model commits before it thinks.

**Diagnose before editing.** Bucket the failures: format breakage, boundary confusion between two categories, a reasoning leap, a guess where the source was silent. Each bucket has a different fix, and editing before bucketing is how prompts accumulate contradictory rules.

**Prune before adding.** Every addition costs attention. If a rule has never changed an output, it is paying rent for nothing.

### How it connects to the rest of the framework

Bullet 2 (`TSC3-Advanced-K2`) supplies the levers being sequenced — branches, context, refinement. Bullet 9 (`A3`) is the rubric that makes optimisation measurable, and Bullet 12 (`A5`) is the same loop applied to one output rather than to a prompt. Bullet 6 (`K6`) is where this becomes infrastructure: templating, versioning and batch runs. Bullet 1 (`K1`) is the prior question of whether optimisation is worth doing at all.

### What is current as of November 2026

Three things have changed the practice. **Prompt caching** made static-prefix-first ordering a line item: a stable rule block at the top of a repeated prompt is now materially cheaper, not just better attended. **Structured output modes** moved format from described to enforced, so fewer instructions are needed at the bottom and the schema does the work. And **prompt drift** became ordinary: providers update models behind aliases, so a prompt optimised in March can quietly degrade. Current frontier families each respond better to their own markup habits, so an ordering tuned on one family should be re-checked, not assumed, on another. Pin the dated model version alongside the prompt version.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Optimising means rewriting."* Rewriting changes five variables and teaches you nothing. Change one, re-measure.
- *"The model learns from my corrections in this chat."* It reads the transcript; it does not update its weights. If a correction worked, it worked as context — write it into the prompt.
- *"Order is cosmetic."* Same words, different order, different output. That is the demonstration, not the theory.
- *"If a rule is ignored, shout it."* Capitals and "IMPORTANT!!!" change tokenisation, not attention. Move the rule, or remove what is competing with it.
- *"It passed on my example, so it is optimised."* One example is a coin toss; twenty inputs is a measurement.

## How a student should understand it

**Mental model:** a prescription slip. Patient, drug, dose, frequency, signature — each field in its place. Reorder them and the pharmacist cannot fill it, even though every word is present.

**Things they can do after this bullet:**
1. Explain, with an example, why instruction order changes the output.
2. Run a two-version comparison where only the order of constraints changed.
3. Describe and execute a one-variable optimisation loop with a fixed check.

**Misconceptions to kill:** that optimisation is rewriting; that a chat correction persists; that order is decoration.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The prescription slip.** Every clinic in Singapore uses the same field order, and a slip with the dose written where the patient's name belongs is not "an unusual prescription" — it is an invalid one. Where it breaks: a prescription is read by a trained human who will query it; a model will not query, it will interpret, which is why a mis-ordered prompt fails silently rather than being rejected.

**One knob at a time at the sound check.** At a community event the technician raises one channel, listens, lowers it, then moves to the next. Turn everything up together and the room is loud and unintelligible. Where it breaks: a sound check has an obvious target — the audience can hear it; a prompt's target has to be written down first, which is the point of the contract.

### Worked example with a real tool

```text
Version A: Summarise this report in 3 bullets, keep it under 50 words,
write for a busy director.

Version B: Write for a busy director. Summarise this report in 3 bullets,
keep it under 50 words.

<report>
```

Run both on the same report. The outputs differ in emphasis — B tends to lead with the decision or cost, A with the topic — because the audience instruction arrived first and coloured what counted as a summary. Then rebuild the good version properly: report first, then task, then constraints, then format, with a reasoning field ahead of any label. Point at the count of changed variables: one in A→B, five in the rebuild. Only one of those comparisons is evidence.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run A and B live, project both, ask which is "correct".
2. **State the objective** — sequence a prompt deliberately and run a one-variable optimisation loop with a written check.
3. **Recall prior learning** — how a good briefing note is laid out: context, then ask, then deadline and format.
4. **Present the content** — the assembly order, the reason-before-label rule, the diagnose-then-edit loop.
5. **Guide** — take the room's weakest prompt and improve it together, one change per run, logging each.
6. **Elicit performance** — pairs take a prompt from their work, define a three-point check, and run three single-variable versions.
7. **Give feedback** — compare logs. Groups that changed two things at once cannot attribute the result, which is the debrief.
8. **Transfer** — each learner writes the contract for one prompt they will maintain, and pins the model version beside it.

## What the framework doesn't mention but trainers need to know

- **Optimisation needs a fixed cost budget.** Running a prompt forty times to tune it is fine in a project and unacceptable in a live workflow. Decide the number of runs before you start.
- **Position interacts with length.** A 200-word prompt is read almost uniformly; a 20,000-token prompt is not. The ordering rules matter in proportion to how much you paste.
- **Few-shot examples can contradict the rules.** If the instructions say "under 50 words" and the example is 120 words, the model follows the example. Audit examples against rules — this is the single most common sequencing defect in handover prompts.
- **Long prompts fail quietly.** The model obeys roughly two-thirds of a thirty-rule prompt and no error appears anywhere. Fewer, tested rules beat a comprehensive list.
- **A prompt that cannot be diffed cannot be optimised.** Store it as text in a file, not as a memory of what you typed last week.

## Watch out

- **Do not optimise against one favourite input.** It produces a prompt that handles your example and nothing else.
- **Do not present a single before-and-after as proof.** Show the full set, including the cases that got worse.
- **Do not tidy the prompt for elegance.** Optimisation is for output quality; a messy prompt that works beats a beautiful one that does not.
- **Do not skip the abstention case.** A prompt that is never tested on an unanswerable input will invent an answer when one arrives.
- **The stale claim to retire:** "the model remembers your correction." Each turn is a fresh read of the text; persistence has to be written in.
