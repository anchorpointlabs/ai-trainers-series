---
id: 03.01.B.A2
tsc: 3
level: Basic
code: A2
title: Describing a prompt technique so a colleague can actually use it
---

# Describing a prompt technique so a colleague can actually use it

> **TSC #3 Prompt Engineering · Basic · Ability A2**


> **Framework text (verbatim):** "Describe fundamental prompt design techniques."
>
> **TSC #3** Prompt Engineering · **Basic** · Ability · Bullet 9 of 15

**One-line version:** A technique is described well when a colleague can choose it, write it and check it without you in the room — five fields, one page, no adjectives.

## What it is

Describing a prompt technique means explaining it precisely enough to be used: what it is for, what it looks like when written, when it beats the alternatives, what it costs, and how to tell whether it worked. The framework asks for fundamentals — zero-shot, one-shot, instruction and domain prompting among them. The practitioner's standard is higher than a definition: the description has to survive being read by someone who cannot ask you a question.

## Deep expansion

### The concept

Most technique descriptions in circulation fail in the same way. They name the technique, give an example, and stop. "Use few-shot prompting for better results" is not a description; it is an advertisement. A colleague receiving it cannot decide between few-shot and a clear instruction, cannot tell whether their example is a good one, and will not know when the technique has stopped helping.

The repair is mechanical. Every technique card in a team library carries five fields:

- **Purpose** — the failure it prevents, in one sentence.
- **Shape** — what it looks like, as a real prompt fragment rather than a diagram.
- **When it wins** — the conditions, stated as tests the reader can apply.
- **What it costs** — context, maintenance, latency, leakage, review effort.
- **How to check it worked** — the observation that distinguishes success from the pleasant version of failure.

Five fields, one page. A team that keeps these for four techniques has a library; a team that keeps a slide deck of examples has a vocabulary.

### The sub-concepts

**Describe by contrast.** A technique is understood against its neighbour. Show the same input handled with a bare instruction and with one example, and the description writes itself. Contrast also reveals the cost honestly, which a single demonstration never does.

**Put the example inside the description.** Not "include one input-output pair" but the actual pair, formatted as it would be typed. Readers copy what they can see; abstractions get paraphrased into something else.

**Name the behaviour, not the brand.** "Chain of thought", "few-shot", "role prompting" are labels that drift and get redefined by marketing. Describe what the prompt does — "show two worked steps before the answer" — and the label can change without the card rotting.

**State the stopping condition.** Techniques stop helping. Few-shot examples stop helping when the input variety exceeds what one example covers. A card without a stopping condition licenses over-use.

**Keep the card next to the prompt.** A description filed in a shared drive and a prompt living in someone's account will diverge. Version them together or the description becomes fiction.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-A1` (Prompt Design); see that entry for the user-level description of zero-shot and one-shot prompting. `TSC3-Basic-K3` is the underlying knowledge this ability puts into words, `TSC3-Basic-A1` gives the element vocabulary a description needs, `TSC3-Basic-A4` is the practice list the cards should reflect, and `TSC3-Basic-A3` is what a reader does with two cards — compare them.

### What is current as of November 2026

The technique vocabulary has thinned. Several named techniques from the 2023 era — elaborate role stacks, "let's think step by step" as a magic phrase, prompt-length tricks — are now either built into reasoning models or simply ineffective, and cards describing them mislead. What has strengthened is the description of *structure*: labelled input blocks, explicit rules, schemas, and the separation of system-level instruction from user-level task.

The practical refresh for any team library: delete the cards for techniques that no longer change output, and add one card for the thing that now matters most — how to specify what the model may use as a source.

### Common misconceptions

- *"If they have the example, they have the technique."* An example without conditions is a trick copied into the wrong situation.
- *"More detail makes a better description."* Detail is only useful where it changes a decision. Five fields, not five pages.
- *"The name is the technique."* Names drift; behaviour does not.
- *"Describing is the easy version of doing."* Describing precisely is harder, and it is the test of whether you understood it.

## How a student should understand it

**Mental model:** the two-minute handover at the office photocopier — which button, which tray, what to do when it jams — and the test is whether the colleague can do it while you watch in silence.

**Things they can do after this bullet:**
1. Write a five-field card for one technique, with a real prompt fragment.
2. State the conditions under which the technique stops helping.
3. Read someone else's card and predict what it will do on a given input.

**Misconceptions to kill:** that an example is a description; that the label is the technique; that detail substitutes for decision criteria.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The photocopier handover.** "Press the green button" is not a handover. A handover is: double-sided for reports, tray two for letterhead, hold the door open if it jams, and call facilities if the screen flashes E4. Four facts, and the colleague can work alone. Where it breaks: a photocopier behaves identically every time, while the technique's effect depends on the input — so the card must describe conditions, not just steps.

**The relief cook's handover.** The stall owner leaving for two days writes: the laksa paste is in the second fridge, the broth needs the extra hour, do not serve after 8pm if the queue is short. Where it breaks: a relief cook can taste and adjust; a colleague following a technique card gets no feedback until the output is in front of them, so the card's check step has to be explicit.

### Worked example with a real tool

Write the card. Task: extracting action items from meeting notes, where a bare instruction keeps producing items nobody agreed to.

```text
TECHNIQUE: one-shot extraction with an explicit "not agreed" filter

PURPOSE
Stops the model turning discussion points into action items.

SHAPE
Input: <meeting notes>
Example:
  Notes: "Sarah said she'd check the vendor list by Friday. General
  agreement that pricing needs review, no owner named."
  Actions: [{"owner":"Sarah","action":"check vendor list","due":"Friday"}]
Now extract action items from the notes below in the same JSON shape.
Only include items with a named owner and a stated or implied deadline.
If a decision has no owner, put it in a separate "unassigned" list.

WHEN IT WINS
Notes are chatty; the team's definition of an action item differs from the
model's default; the JSON shape is consumed by something downstream.

COST
The example is now a specification — if the team changes the rule, the example
must change. It adds a short block to every run. The model may copy the example's
phrasing ("check vendor list") into unrelated items.

CHECK
Run it on notes containing exactly two real actions and four decisions.
Expect two items and four unassigned entries. If you get six items, the
example did not teach the filter.

STOPS HELPING
When notes come from several teams with different conventions — one example
cannot cover the range; switch to a rules block plus a schema.
```

What to point at afterwards: the card contains no adjectives and four decisions the reader can make alone. Then hand it to another pair and ask them to use it on their own meeting notes without asking a question. Every question they have to ask is a missing field.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read two descriptions of the same technique, one a slide bullet and one a card. Ask which one they could use tomorrow.
2. **State the objective** — by the end you will write a five-field card a colleague can apply without asking you anything.
3. **Recall prior learning** — ask how they hand over a task before going on leave; the fields are the same fields.
4. **Present the content** — teach the five fields, then contrast, then the stopping condition.
5. **Guide** — write the extraction card together, arguing about the "what it costs" field until it is honest.
6. **Elicit performance** — each learner writes a card for a technique they actually use, in twenty minutes.
7. **Give feedback** — cards are swapped and used cold. Questions asked by the reader are logged as missing fields.
8. **Transfer** — the team agrees where cards live and who updates them when the prompt changes.

## What the framework doesn't mention but trainers need to know

- **Descriptions are how a team scales past one expert.** The person who writes the best prompts is a bottleneck until their techniques are written down in a usable form.
- **The cost field is the one people omit.** It is also the field that prevents the technique being applied everywhere, which is the main way prompt libraries rot.
- **Cards need a review date.** Techniques stop helping quietly; a card with no review date is a card that will be trusted after it has expired.
- **A card is not a lesson plan.** It is a reference for someone already competent. Teaching still needs the worked example and the failure.

## Watch out

- **Do not let the room produce cards full of adjectives.** "Clear, specific and well-structured" describes nothing.
- **Do not accept a card with no stopping condition.** It is the field that carries the judgement.
- **Do not describe techniques you have not run on the current model.** Several well-known techniques no longer change anything, and describing them wastes the room's trust.
- **The stale claim to retire:** "prompt engineering is a list of named techniques." In November 2026 the useful descriptions are mostly about sources, structure and checking, not about named tricks.
