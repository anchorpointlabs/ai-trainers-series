---
id: 01.01.B.A1
tsc: 1
level: Basic
code: A1
title: Write prompts for different output types
as_at: 2026-11-26
review_by: 2027-02-25
---

# Write prompts for different output types

> **TSC #1 Generative AI Principles and Applications · Basic · Ability A1**

> **Framework text (verbatim):** "Write prompts to generate various types of generative AI outputs."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Ability · Bullet 9 of 13

**One-line version:** A prompt is a brief, and the brief has to name the output — text, image, video, code or table — because each mode has its own levers, and the same one-line request produces a usable draft in one mode and mush in another.

## What it is

This is an ability: the learner writes prompts, receives output, and improves the prompt. A prompt that works has five parts — task, context, audience, format, constraints — plus a sixth most trainers forget: a worked example of what good looks like. The mode decides which part carries the most weight. Text rewards structure and audience. Image rewards visual specificity and a stated medium. Video rewards a description of change over time. Code rewards inputs, outputs and constraints.

## Deep expansion

### The concept

Beginners write requests; practitioners write briefs. The difference is not length — a good brief can be four lines — it is whether the prompt has made the decisions the model would otherwise make for you. Every unstated decision is one the model makes from an average, and the average is never your house style.

Two more ideas for this bullet specifically. First, **output type is a decision, not a default**: a room that only ever asks for paragraphs gets paragraphs, when the same information could be a table, a checklist, a JSON object, a slide outline, a poster brief or a twenty-second script. Learners who can name the format save most of the editing they currently do. Second, **each mode fails differently, so each prompt prevents a different failure**: text fails by being generic or the wrong length, image by ignoring a spatial instruction or blending two concepts, video by squeezing four actions into five seconds, code by not running. One prompt pattern taught across all modes teaches the confidence without the competence.

### The sub-concepts

**The five-part brief, which works everywhere.** State the **task** (what to produce), the **context** (facts, source material, situation), the **audience** (who reads it, what they already know), the **format** (length, structure, medium) and the **constraints** (what to avoid, what must appear, house rules). Then add a **model answer** if you have one: a short example of the tone beats three paragraphs describing it.

**Text: structure, length and register.** Specify the shape (three paragraphs, five bullets, a table with these four columns), an upper bound on length rather than a target, and the register — to a client, a regulator, a colleague who is annoyed. If you have a house style, paste one paragraph of it.

**Image: medium, subject, composition, light, style.** Five layers: what kind of image (photo, flat illustration, 3D render, watercolour); the subject with specific attributes; what it is doing; the environment; the camera and composition (shot size, angle, framing, space for text); the lighting and colour. Two rules that surprise learners: image models have **no negation** — "a room with no chairs" summons chairs — and **no tolerance for conversational filler** — "could you please" is noise.

**Video: the lever is change over time.** A video prompt describes a state *and* a trajectory: subject, action, camera movement, pacing, environment. One beat per three to four seconds of clip is a working rule. Video prompts want natural sentences, not tag lists, and in image-to-video the appearance is already in the frame, so spend the words on motion and camera.

**Code and structured data: inputs, outputs, constraints, a test.** For code: language and version, exact input shape, exact output shape, environment, what not to use, and one example of correct behaviour — smallest runnable version first. For tables: name the columns and types, and ask for one row as an example. The schema is the lever, and it is the fastest route to reliable extraction from a pile of documents.

### How it connects to the rest of the framework

`TSC1-Basic-K1` supplies the five purposes a prompt is serving. `TSC1-Basic-A02` is the check that follows every prompt. `TSC1-Basic-K6` explains why a prompt can reduce but not fix hallucination. At Intermediate, `TSC2` turns these five parts into a full prompt architecture with examples and evaluation.

### What is current as of November 2026

- **One interface, several model families.** A chat product on OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line or Google's Gemini 3.1 Pro / Gemini 4 Argon will route a request to a text model, an image model or a code sandbox on its own. The learner still has to say which artefact they want; the routing is invisible.
- **Image models moved to natural language.** The tag-soup style belonged to an older generation. Current models respond better to a plain descriptive sentence with a stated medium, and the old quality tags can actively degrade realism.
- **Video prompts went cinematic.** Current models read camera language — shot size, lens, movement — and understand "slow dolly push-in" better than "make it dynamic". Clip lengths remain short; the prompt has to fit the duration.
- **Structured output is a first-class feature.** Most APIs accept a schema and chat products will produce a table on request, which makes "ask for the shape you need" practical rather than advanced.

### Common misconceptions

- *"A longer prompt is a better prompt."* Length helps only when it adds context or constraints. Longer with more unstated decisions is a longer average.
- *"The same one-line style works for every mode."* It does not. A one-liner can produce a decent paragraph and a useless image.
- *"Politeness improves output."* It does not, in any mode. It costs tokens and can confuse an image model.
- *"If the output is wrong, the model is bad."* Usually the brief left a decision open. Check what you did not specify before blaming the tool.
- *"Prompting is a bag of magic phrases."* What works is context, structure and iteration. Phrases circulate because they are memorable, not because they work.

## How a student should understand it

**Mental model:** briefing a freelancer you have never met, who is fast, literal, and has no idea what your organisation sounds like. Everything you leave out, they invent.

**Things they can do after this bullet:**
1. Write a text prompt specifying task, context, audience, format and one constraint, and get a usable first draft.
2. Write an image brief a designer could execute, with medium, subject, composition and light named.
3. Convert the same information into three output types on request: paragraph, table, outline.

**Misconceptions to kill:** that longer is better, that one style works across modes, and that the model is at fault when the brief was vague.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The wedding photographer's brief.** You do not say "take nice photos". You say: outdoor, evening, forty guests, want the couple walking in, warm tones, no stiff posing. The more decisions you make, the less the default shows. Where it breaks: the photographer asks you a clarifying question, and the model will not. You have to ask yourself.

**Ordering at the economy rice stall.** "Rice, two veg, one meat, curry over the rice, no gravy on the fish" gets you lunch. "Something nice" gets you whatever is at the front of the tray.

### Worked example with a real tool

One task, three output types, typed in sequence:

```text
We are running a fire drill on Friday at 3pm. The building has 6 floors and
the assembly point is the car park behind the block.

1. Write a two-sentence notice for the staff WhatsApp group.
2. Turn the same information into a 4-row table: What / When / Where / What to bring.
3. Write a brief for a poster: headline under 8 words, three bullets,
   and a description of the visual (flat illustration, two colours).
```

Then the image prompt, in an image-capable tool:

```text
Flat vector illustration, two-colour palette of navy and orange, of a calm
office worker in a lanyard walking toward a stairwell exit, seen from behind
at eye level, with a large empty area at the top for a headline. Clean
geometric shapes, no text in the image.
```

What to point at afterwards: the facts survive all four outputs, but the **unit** changes — sentence, row, seconds of attention, square of canvas. Then point at the last clause of the image prompt. "No text in the image" is the right way to handle a negation in images: describe what should be absent as a property of the design, and put lettering in afterwards. That one correction prevents the most common image failure in an office — garbled text baked into a poster.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — One task requested three ways: paragraph, table, list. Which would they actually send, and why?
2. **State the objective** — "You will write one brief that produces a usable draft first time, and one image brief a designer could execute."
3. **Recall prior learning** — From K1: five purposes, several modes. Which mode do they default to, and why?
4. **Present the content** — The five parts, then one slide per mode with its dominant lever.
5. **Guide** — Build the fire-drill brief on the projector, taking suggestions and typing them live.
6. **Elicit performance** — Each learner writes a text prompt and an image brief for a real task.
7. **Give feedback** — Swap and mark which of the five parts is missing. Almost always audience and format.
8. **Transfer** — Rewrite the weakest prompt, run both, compare side by side.

## What the framework doesn't mention but trainers need to know

- **Context beats cleverness.** Most quality gains come from the material you supply — a sample, a source, a template — not from wording.
- **Ask for the shape, not the content, when stuck.** "Give me the headings and the three questions each section must answer" is a better first move than "write the report".
- **Have the model interview you.** "Before you write, ask me the five questions you need answered" produces a better brief than most learners can write alone, and it teaches what a brief contains.
- **Iteration is the skill, not the first attempt.** A trainer who demos one perfect prompt teaches a trick; one who improves a mediocre prompt three times teaches the job.

## Watch out

- **Do not teach magic phrases.** No incantation survives a change of model, and learners who rely on them cannot adapt.
- **Do not demo image or video with a text-model habit.** Conversational politeness and negation are actively harmful there; say so before the demo, not after.
- **Do not let "write me a prompt" replace the brief.** The learner makes the decisions; that is the skill.
- **The stale claim to retire:** "there is one right prompt for each task." There is a brief that works for your purpose, and it improves as you learn what your purpose actually is.
