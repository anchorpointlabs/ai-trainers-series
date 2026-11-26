---
id: 03.03.A.A4
tsc: 3
level: Advanced
code: A4
title: Evaluate effectiveness across scenarios
---

# Evaluate effectiveness across scenarios

> **TSC #3 Prompt Engineering · Advanced · Ability A4**

> **Framework text (verbatim):** "Evaluate the effectiveness and adaptability of prompt engineering methods across diverse scenarios."
>
> **TSC #3** Prompt Engineering · **Advanced** · Ability · Bullet 11 of 13

**One-line version:** A prompt is fitted to the situations it was tested in — adaptability is measured by moving one variable and finding the exact place where it breaks.

## What it is

A method that works for a formal report may fail for a WhatsApp message; a prompt tuned on English may behave differently in Singlish or Mandarin; a template built for short enquiries may collapse on a forty-page submission. This ability is the deliberate stress test: change the scenario, hold the method, and find the variable that broke it — then adapt, and retest. The output of the exercise is not a pass mark. It is a named boundary.

## Deep expansion

### The concept

Every prompt encodes assumptions it never states: who the reader is, what register is appropriate, what a typical input looks like, what language the work happens in, which model reads it. When the scenario matches the assumptions the prompt looks robust; when it does not, the failure appears, and it usually appears as "the model is bad at X" rather than "the prompt assumed Y".

Adaptability testing makes the assumptions visible by moving them. Change the reader and the tone instruction becomes wrong, not just suboptimal. Change the channel and the length rule becomes a liability. Change the language and the format expectations shift, because conventions for a formal memo in English are not the conventions for the same memo in Chinese.

The discipline is one variable at a time, for the same reason as in optimisation: if you change audience *and* language *and* format, you learn that the adapted version works and nothing about why the original failed.

### The sub-concepts

**The five variables worth varying.** Who reads it (executive, frontline, regulator, customer), what register (formal, conversational, Singlish, bilingual), what language, what channel and format (report, WhatsApp, slide, form), and what the input distribution looks like (length, completeness, noise). A sixth is the reading model.

**The register gap is the most common break.** Formal summaries make poor WhatsApp messages and WhatsApp messages make poor board papers. The instruction "summarise this" contains no register at all, so the model supplies its default — which is competent, formal, and wrong for half your channels.

**Language is not translation.** A prompt that works in English may need the format instruction restated for Chinese (where the structural conventions differ), or the examples replaced, rather than merely translated.

**Model family is a scenario.** A prompt is coupled to the alignment of the model it was tuned on: some families respond better to XML-style tags, others to Markdown headings; reasoning-shaped models degrade under verbose step scripts. Before switching models, re-run the check rather than assuming portability.

**Domain is a scenario.** A taxonomy built for one department's complaints does not map onto another's. The categories look transferable and the edge cases are not.

**Portability trades against sharpness.** A prompt generic enough to survive every scenario does each one adequately. The professional move is a core prompt plus scenario-specific preambles, not one prompt stretched over everything.

### How it connects to the rest of the framework

Bullet 10 (`A3`) supplies the check you carry between scenarios — without a fixed criterion, adaptability testing becomes a series of impressions. Bullet 2 (`K2`) is the context lever that usually needs adjusting, and Bullet 1 (`K1`) is the prior question of whether this scenario is worth engineering at all. Bullet 13 (`A6`) composes scenario-specific stages into one pipeline, which is how mature teams handle genuinely diverse inputs.

### What is current as of November 2026

- **Register, not capability, is the usual break.** Late-2026 frontier models (GPT-6 generation, Claude 5.5, Gemini 3.1 Pro, Gemini 4 Argon) handle Singlish, code-switching and mixed-language input far better than earlier generations. What they still do not do is infer that you wanted an informal register for a WhatsApp message — you have to say so.
- **Long inputs became ordinary.** With very large context windows, a prompt built for a two-page enquiry is often asked to handle a forty-page submission. The failure mode moved from "does not fit" to "attends to the wrong part", which is a placement problem rather than a capacity one.
- **Cross-model portability got worse, not better.** Families diverged in their markup preferences and reasoning behaviour, so "it worked on the other one" is now a hypothesis to test, not a fact to rely on.

### Common misconceptions

- *"A good prompt works everywhere."* A good prompt works where it was tested. Everywhere else it is untested.
- *"The model can't do Singlish."* Usually it can; the prompt asked for a formal summary and got one. The gap is register, not language.
- *"Adapting means rewriting."* Usually it means adding one line — the audience, the channel, the length — and retesting.
- *"I tested it in one scenario, so I know it's effective."* You know it is effective there. That is a smaller claim.
- *"If it fails in the new scenario, the method is wrong."* The method may be fine and the assumption wrong. Name the assumption.

## How a student should understand it

**Mental model:** the same lesson plan taught to a polytechnic class and to a statutory board. The content survives; the examples, the pace and the jokes do not.

**Things they can do after this bullet:**
1. Run one method across two scenarios and name what changed.
2. Identify the single variable that broke it — audience, register, language, channel, input shape, or model.
3. Adapt with a targeted addition and retest against the same check.

**Misconceptions to kill:** that prompts transfer unchanged; that a language gap is a capability gap; that adaptation is rewriting.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The wok recipe on an induction hob.** Same ingredients, same instructions, different heat. The dish is not wrong; the method assumed a heat source it no longer has. Where it breaks: a cook notices and adjusts; a prompt fails silently, so the adjustment has to be deliberate.

**The circular read aloud versus printed.** The same words, delivered at a town hall and printed on a notice board, land differently — one needs shorter sentences, the other needs headings. Where it breaks: a human speaker adapts in real time; the model needs the adaptation written in.

### Worked example with a real tool

```text
Prompt: 'Summarise this meeting in 3 bullets for a formal report.'
Now run the same instruction, but the summary is for a WhatsApp message
to a colleague in Singlish.
```

Run both on the same meeting notes. The formal version produces three dense bullets with passive constructions — correct for a report, absurd in a group chat. The failure is not the model's; the instruction specified a formal report and got one. Now add the missing variable — "for a colleague, casual, Singlish, under 40 words, no jargon" — and run again. Then change only the language to Chinese and run a third time: the bullets usually get longer and more formal, because the format convention changed with the language. Three runs, three different variables, three different lessons.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show the formal summary and ask where it would be embarrassing to send.
2. **State the objective** — stress-test one method across two scenarios, name the breaking variable, adapt and retest.
3. **Recall prior learning** — a time they reused a template and it landed badly because the audience changed.
4. **Present the content** — the five variables, the register gap, the model-family gap, portability versus sharpness.
5. **Guide** — run the formal/WhatsApp pair, name the variable, adapt, retest.
6. **Elicit performance** — pairs take a prompt from their work and run it in a second scenario, changing one variable.
7. **Give feedback** — collect the breaks on the board and group them by variable. The pattern is usually register.
8. **Transfer** — each learner writes the adaptation line they will add for their second-most-common channel.

## What the framework doesn't mention but trainers need to know

- **Adaptation has a maintenance cost.** Five scenario variants of one prompt is five things to test after every model update. Prefer one core prompt plus a small scenario line to five forks.
- **Distribution shift is the quiet killer.** Prompts tuned on tidy enquiries meet messy forwarded emails with quoted threads. Sample real inputs, not the tidy ones.
- **Localisation is not translation.** Format, honorifics, date conventions and directness all shift. A translated instruction is not an adapted one.
- **Test before a model migration, not after.** The scenario test is the cheapest way to find out that the new model reads your markup differently.
- **Name the boundary in the documentation.** "Works for enquiries up to two pages, formal register, English" is more useful than "works well".

## Watch out

- **Do not treat Singlish as a party trick.** It is a legitimate register with real users, and it exposes the register assumption faster than anything else.
- **Do not conflate a domain gap with a model gap.** If the taxonomy does not fit the department, no model upgrade fixes it.
- **Do not adapt without retesting.** An adaptation is a new prompt with no evidence until it is run.
- **Do not change three variables and celebrate.** You have learned that something worked.
- **The stale claim to retire:** "we tested it on one use case, so it's ready to roll out." Roll-out is exactly the scenario where the untested variable appears.
