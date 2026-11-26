---
id: 03.03.A.A2
tsc: 3
level: Advanced
code: A2
title: Analyse prompt nuances and model behaviour
as_at: 2026-11-26
review_by: 2027-02-25
---

# Analyse prompt nuances and model behaviour

> **TSC #3 Prompt Engineering · Advanced · Ability A2**

> **Framework text (verbatim):** "Analyse the nuances of prompts and their influence on AI model behaviour."
>
> **TSC #3** Prompt Engineering · **Advanced** · Ability · Bullet 9 of 13

**One-line version:** Read the output, name the property that is wrong, and point to the words in the prompt that produced it — that trace is the skill, and it replaces guessing.

## What it is

This ability is diagnostic rather than generative. Given an output you did not want, find the cause in the prompt: the verb that set the length, the missing audience that made the tone generic, the example that overrode the instruction, the clause buried where attention decays. Then change one thing and confirm the shift. Learners who can do this stop re-rolling and start editing; learners who cannot keep saying "the model is being weird".

## Deep expansion

### The concept

Every word in a prompt changes the probabilities of the words that follow. Three mechanisms explain most of the sensitivity:

- **Tokenisation.** The model does not read words, it reads tokens. "Summarise", "summarise" and "SUMMARIZE" are different token sequences with different associations. That is why capitals feel like emphasis — they change the input, not the authority.
- **Latent association.** Words that appeared together in training occupy neighbouring regions of the model's internal space. "Act as a MAS compliance auditor" pulls in a cluster of vocabulary, structure and caution. "Give me business advice" pulls in a different cluster. The framing selects which cluster answers.
- **Compounding.** Each generated token conditions the next. A one-word change that alters the first sentence changes the whole answer by the fifth, because the model is now continuing a different text.

The practical consequence is that wording is never neutral, and the effect is not always in the direction you expect. "Explain" produces length and structure; "summarise" produces compression; "critique" produces judgement and a different emotional register entirely. None of these is a synonym of the others in a prompt.

### The sub-concepts

**The verb is the operation.** Summarise, explain, list, rank, critique, extract, rewrite, check. Each implies a shape, a length and a stance. Most disappointing outputs are a verb mismatch: the learner wanted "check" and wrote "review".

**Nouns carry scope.** "The leave policy" is the whole document; "the leave policy as it applies to contract staff" is a subset with a different answer. Unscoped nouns invite the model's default scope, which is "the general case".

**Modality is instruction strength.** Must, should, may, prefer, consider. "Should" leaves room; if a constraint is hard, say it as a hard constraint and put it where it will be attended to.

**Quantity words are unmeasurable until you make them so.** "Brief", "concise", "detailed" are relative. "Three bullets, under fifty words, no preamble" is checkable — and checkability is the difference between a specification and a wish.

**Examples outrank adjectives.** A prompt that says "under fifty words" beside a hundred-and-twenty-word example will produce long outputs. The example is the instruction; the sentence is decoration.

**Persona steers tone, not knowledge.** A role changes vocabulary, structure and caution. It does not add facts, and theatrical roles ("world-class genius") add nothing measurable while adding words.

**Position is a lever.** The same clause at the top, in the middle of a pasted document, and at the end produces three different amounts of compliance.

**Agreement is not evidence.** Asking "are you sure?" invites the model to assume you are correcting it, so it apologises and flips a correct answer. Self-correction works when anchored to something external — a source, a calculation, a rubric.

### How it connects to the rest of the framework

Bullet 8 (`A1`) is the reverse operation — choosing levers to produce a shape. Bullet 3 (`K3`) is the ordering that this analysis justifies, and Bullet 12 (`A5`) is the refining loop that follows a good diagnosis. Bullet 10 (`A3`) turns the diagnosis into a measurement, so a suspected cause is confirmed rather than believed. `TSC3-Basic` covers the levers at a descriptive level; this bullet is the causal reading.

### What is current as of November 2026

Current frontier models are less sensitive to the theatrical side of prompting than their predecessors. Role-play flattery buys little; explicit rules, supplied sources and a checkable format buy a lot. Two nuances survive and matter more:

- **Sensitivity moved from style to specification.** The model will now infer a reasonable tone from context; it will not infer which four fields you needed in the table.
- **Model families have dialects.** Some respond best to XML-style tags, others to Markdown headings; reasoning-shaped models degrade when given verbose step scripts. An analysis performed on one family does not transfer as fact to another — it transfers as a hypothesis.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Wording is neutral — it either has the instruction or it doesn't."* Every verb, noun and quantifier is an instruction. There is no neutral phrasing.
- *"The model is random, so I can't predict."* It is stochastic, not arbitrary. Change one word and the shift is usually directional and repeatable.
- *"If it got it wrong, ask if it's sure."* That is the reliable way to make a correct answer wrong.
- *"It ignored my rule on purpose."* The rule was contradicted by an example, buried in the middle, or arrived after the model had already committed.
- *"It's the model's fault."* Sometimes. Far more often it is the prompt's, and the trace will show which.

## How a student should understand it

**Mental model:** a referral letter. "Please assess" gets an assessment; "please exclude a fracture" gets an X-ray request. Same patient, same doctor, one changed phrase, a different pathway.

**Things they can do after this bullet:**
1. Take an output and name the prompt wording that produced its length, tone and structure.
2. Change one word and predict the direction of the shift before running it.
3. Explain why an example can override an explicit instruction.

**Misconceptions to kill:** that wording is neutral; that randomness excuses analysis; that agreement is confirmation.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The aircon man.** "Service" gets a wipe and a top-up; "chemical wash" gets a dismantled unit. Two words, different work, different invoice. Where it breaks: a technician knows the trade and will clarify; a model will not clarify — it will do the cheaper interpretation and say nothing.

**The MCST circular.** "Residents should refrain from…" versus "Residents must not…" produces two different conversations at the guardhouse. Wording is the policy. Where it breaks: a circular is read by people who argue back; a prompt is obeyed literally, including the parts you did not mean.

### Worked example with a real tool

```text
Prompt: 'Explain the new leave policy.'
Output: a 400-word explanation.

Now: 'Summarise the new leave policy in 2 bullets.'
```

Then two more edits, one at a time: change "must submit" to "should submit" and watch the firmness of the procedure disappear; change "list the steps" to "rank the steps by risk" and watch a different output shape appear entirely. Ask the room to predict each before running it. The predictions that fail are the useful ones — they show which words the room believed were decorative.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show the 400-word "explain" output and the two-bullet "summarise"; ask what single word did that.
2. **State the objective** — trace an output feature to its cause in the prompt, predict a one-word shift, then verify.
3. **Recall prior learning** — a time a colleague misunderstood an instruction because of one word, and what it cost.
4. **Present the content** — the three mechanisms; verb, noun, modality, quantity, examples, position; the sycophancy trap.
5. **Guide** — run the explain/summarise pair, then must/should, predicting first.
6. **Elicit performance** — pairs get a prompt and its output, highlight the causal wording, propose one change with a predicted effect, then test it.
7. **Give feedback** — compare predictions with results. Wrong predictions identify the words the room over-trusted.
8. **Transfer** — each learner takes one recurring complaint about AI output and writes the trace plus the one-word fix.

## What the framework doesn't mention but trainers need to know

- **Diagnose before editing.** The order is: read the output, name the property, find the cause, change one thing, re-run. Learners skip to step four and learn nothing.
- **Some behaviour is not in the prompt.** If the model lacks the fact, no wording fixes it. Distinguishing a prompt defect from a knowledge defect is the first fork in the diagnosis.
- **Upgrades change the sensitivity map.** A prompt tuned on one snapshot behaves differently after an update. Any analysis has a date.
- **Verbose reasoning hides the cause.** When the model writes three hundred words of rationale, the wording that mattered may be three paragraphs up. Ask for the answer first, then a short justification, when diagnosing.
- **Learners over-attribute to persona.** The most common wrong analysis in a classroom is "it wasn't expert enough". It is nearly always missing scope, missing data or a competing example.

## Watch out

- **Do not let "the model is random" end the discussion.** It is the sentence that stops learning.
- **Do not demo a change that shifts everything at once.** One word, one prediction, one run.
- **Do not praise a fluent wrong answer in front of the room.** Fluent and faithful are different properties, and the room will copy what you admire.
- **Do not analyse without the prompt visible.** Tracing requires the actual text, not the learner's memory of it.
- **The stale claim to retire:** "it got better because I said please." Politeness correlates with nothing worth relying on; structure and supply do.
