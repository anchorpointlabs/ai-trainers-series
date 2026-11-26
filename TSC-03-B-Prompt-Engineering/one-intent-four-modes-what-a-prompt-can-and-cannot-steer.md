---
id: 03.01.B.K4
tsc: 3
level: Basic
code: K4
title: One intent, four modes: what a prompt can and cannot steer
as_at: 2026-11-26
review_by: 2027-02-25
---

# One intent, four modes: what a prompt can and cannot steer

> **TSC #3 Prompt Engineering · Basic · Knowledge K4**


> **Framework text (verbatim):** "Impact of prompts on different modes of AI output."
>
> **TSC #3** Prompt Engineering · **Basic** · Knowledge · Bullet 4 of 15

**One-line version:** The same intent has to be re-written for every output mode, because each mode has a different surface you can steer — and a different way of failing quietly.

## What it is

Generative models produce text, images, audio, video, code and structured data, and a prompt steers each of them through a different set of controls. In text you can instruct behaviour. In an image you can only describe appearance. In code you can specify a contract and then check it by running it. Knowing which controls exist in which mode is what stops a practitioner from pasting a good text prompt into an image model and concluding the tool is bad.

## Deep expansion

### The concept

The framework asks for the impact of prompts on different output modes. The practitioner's version of that question is sharper: *what is the controllable surface of this mode, and what does that mode do when you under-specify it?*

Text is the most instruction-like mode. You can say "argue the opposite", "cut this by half", "do not mention price", and the model will attempt all three. Its quiet failure is fluency: a wrong answer that reads well.

Images swing the other way. You cannot instruct an image to be persuasive, honest or on-brand in the abstract. You describe subject, framing, light, material, style, and what must be absent. Its quiet failure is confidence: an image that looks exactly like a real product or a real person, generated from a description that never mentioned either.

Code is the only mode with a built-in test. You specify language, inputs, outputs, and the edge cases that must not crash — and then you run it. Its quiet failure is plausibility: code that reads correctly and fails on the empty list.

Voice and video add performance dimensions — pace, emphasis, pronunciation of local names, what appears on screen while something is said — and only some of those are steerable from the prompt.

Structured data is the most mechanical: the prompt should specify keys, types and what to do with missing values, and the platform should enforce the schema rather than trusting the prose.

### The sub-concepts

**Description replaces instruction.** In image and video modes the prompt is a specification of appearance. Learners who write "a professional poster that will make people trust us" are writing a brief for a designer, not a prompt for a model. The translation is: subject, composition, lighting, typography, palette, and the negative list.

**Legibility is a separate problem.** Ask an image model for a poster with a headline and you are asking for two things at once — a picture, and correctly spelled words inside it. Text in images has improved markedly, but it is still the part to check first, especially with local names and addresses.

**Code is judged by execution.** A prompt for code should state the contract: language and version, input shape, output shape, what to do on bad input, and one example case. Then run it. Reading code and believing it is a category error the room will make if you let them.

**Performance dimensions in voice and video.** Pace, pause, emphasis, pronunciation. If a script contains "Ng" or "Geylang", the prompt has to say how it is said, or the voice model will choose for you. The same applies to on-screen text in video, which needs to be specified separately from the narration.

**Mode switching is translation, not copy-paste.** The intent survives; the sentence does not. A practitioner keeps the intent statement fixed and rewrites the controls for each mode, which is also why one person can be excellent at text and poor at image prompting without being inconsistent.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-K3` (Prompt Design); see that entry for the user-level basics of mode differences. `TSC3-Basic-K2` supplies the levers that get re-expressed here, `TSC3-Basic-K3` supplies the techniques that stop working when the mode changes, and `TSC3-Basic-A3` is how you compare two designs within one mode rather than across modes.

### What is current as of November 2026

The modes have converged into single products and diverged in behaviour. One chat surface now handles text, image, voice and file analysis, but the prompt that works in each is still written differently, and the current frontier families differ more in their image and voice behaviour than in their text behaviour. Two practical shifts: image models now render legible text well enough that poster work has moved from "generate then rebuild in a design tool" to "generate and correct", and code models with repository context have made "specify the contract, then run the tests" the normal working method rather than an advanced one.

Voice has moved from turn-taking to real-time conversation, which makes pacing instructions matter more than pronunciation instructions — the model now decides when to stop talking.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The same prompt works in every mode."* It does not survive translation. The intent survives; the controls do not.
- *"An image prompt is just a longer text prompt."* Length is not the variable. Describing appearance is a different act from instructing behaviour.
- *"If the code looks right, it is right."* Code that reads well and fails on an empty input is the standard failure, not an unusual one.
- *"Video is a sequence of image prompts."* Continuity, motion and audio sync are separate problems the prompt has to address.

## How a student should understand it

**Mental model:** a translator working across four languages. The message stays the same; the sentence has to be rebuilt each time, and a literal translation is how you get laughed at.

**Things they can do after this bullet:**
1. State the controllable surface of each mode in one line.
2. Rewrite one intent as a text prompt, an image prompt and a code contract.
3. Name the quiet failure of each mode and the check that catches it.

**Misconceptions to kill:** that a prompt is portable across modes; that an image prompt is instruction; that code can be verified by reading.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The HDB notice in four channels.** The same notice goes up as a lift-lobby poster, out as a WhatsApp broadcast, over the PA system, and as a letter to residents. Same facts, four completely different constructions — a poster that reads like a letter is a bad poster. Where it breaks: the four channels all accept the same words in different arrangements, while image and code modes do not accept the same words at all.

**The recipe written three ways.** The same dish appears as a recipe card (text), a photo (image), and a set of timings on a kitchen timer (code: inputs, outputs, limits). Where it breaks: a photo of the dish can look perfect while the recipe is wrong, which is exactly the image-mode failure.

### Worked example with a real tool

One dataset, three modes. Take a CSV of 300 learner feedback scores, and one intent: tell the training manager what happened.

Text, in ChatGPT or Claude:

```text
Using only the attached CSV, write 120 words for a training manager who will
read this on a phone before a 9am meeting. Lead with the overall direction,
then the one group that differs most, then one recommendation. Quote no more
than two numbers.
```

Image, in an image model:

```text
A single clean bar chart image, 16:9, white background, midnight blue bars,
one highlighted bar in amber, no title text, no axis labels, generous margins.
```

Code, in a code assistant:

```text
Write Python 3.12 using pandas only. Function summarise(path) returns a dict:
{"n": int, "mean": float, "by_group": {group: float}}.
Raise ValueError with the message "EMPTY" if there are no rows.
Treat missing scores as excluded, not zero. Include one assert for each rule.
```

What to point at afterwards: three prompts, one intent, and only one of them can be checked by running it. The image prompt has no truth condition at all — a beautiful chart of the wrong numbers passes. That asymmetry is the lesson, and it is the reason the image output needs a human looking at it beside the source data.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a handsome generated poster with the wrong date on it. Ask how many people would have caught the date.
2. **State the objective** — by the end you will state the controllable surface of each mode and rewrite one intent three ways.
3. **Recall prior learning** — ask who has sent the same message by email and by voice note; the difference they already know is the lesson.
4. **Present the content** — teach the four surfaces and the four quiet failures, then the translation rule.
5. **Guide** — rewrite the training-summary intent together, mode by mode, on screen.
6. **Elicit performance** — groups of three each take one mode for a task from their own work and write the prompt plus the check.
7. **Give feedback** — run all three, then run the checks. The mode whose check cannot be automated is the one that needs the human.
8. **Transfer** — each learner names one task where they have been using the wrong mode.

## What the framework doesn't mention but trainers need to know

- **Mode choice is a design decision that precedes prompting.** If the output must be auditable, code or structured data beats prose. If it must persuade, image plus text beats text alone.
- **Image prompts have almost no factuality guarantee.** Anything with a number, date, price or address inside an image needs a human read against the source.
- **Code prompts are where learners get over-confident fastest.** The remedy is mechanical: always ask for assertions, always run them.
- **Voice prompts carry brand risk that text does not.** A mispronounced name in a customer-facing recording is a small but memorable failure, and it is fixed by writing the pronunciation into the prompt.

## Watch out

- **Do not demo image generation as "the fun one" without a correctness check.** It teaches that images are decoration rather than output.
- **Do not compare modes by quality.** Text versus image is not a fair contest; compare each mode against its own standard.
- **Do not let the room believe code output is verified because it looks tidy.** Run it, on the empty input, in front of them.
- **The stale claim to retire:** "the model can't do text in images." In November 2026 it can, reasonably — which means the check has moved from "is it gibberish" to "is it correct".
