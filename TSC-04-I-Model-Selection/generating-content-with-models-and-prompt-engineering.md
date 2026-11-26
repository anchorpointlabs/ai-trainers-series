---
id: 04.02.I.K2
tsc: 4
level: Intermediate
code: K2
title: Generating content with models and prompt engineering
---

# Generating content with models and prompt engineering

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K2**

> **Framework text (verbatim):** "Process of generating content using various AI models, including prompt engineering techniques."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Knowledge · Bullet 2 of 11

**One-line version:** You are never evaluating a model — you are evaluating a model plus a prompt, and the prompt is the half you actually control.

## What it is

Generation is a short loop: choose a model whose modality fits, describe the task with context and an output contract, sample a response, check it against the goal, then revise either the prompt or the request. Prompt engineering is the craft within that loop — role, task, context, examples, format constraints, and step-by-step reasoning where the task needs it. It belongs in this skill because a model's measured quality depends on how it was prompted, so the two are assessed together.

## Deep expansion

### The concept

A generative model continues text. Everything a prompt does is raise the probability of the continuation you want and lower the probability of the continuations you do not. That is the whole mechanism, and it explains why every technique below works.

Four levers, in order of usefulness:

1. **Task clarity** — what to produce, not just the topic. "Summarise" is a topic; "summarise in three bullets for a claims officer, preserving figures" is a task.
2. **Context** — the source material, the audience, the constraints, the things that must not appear.
3. **Examples** — two or three demonstrations of the output you want, which anchor style far more reliably than adjectives like "professional" or "concise".
4. **Output contract** — length, structure, format. If a downstream system consumes the answer, specify the schema and demand nothing outside it.

Where prompting stops is worth stating precisely: it stops when you systematically measure quality across a dataset (that is evaluation), when you change the model itself (selection), and when the prompt is wrapped in versioning, retries and routing (LLMOps).

### The sub-concepts

**Clarity beats cleverness.** Most prompt failures are underspecification. If a human colleague could produce two very different outputs from your instruction, so will the model.

**Few-shot beats description.** Two well-chosen examples outperform a paragraph of style guidance, because they show rather than describe. Examples also fix format drift, which is the most common defect in production output.

**Reasoning on request.** For multi-step tasks, asking for the working out improves accuracy — the intermediate tokens act as scratchpad. For simple extraction it adds cost and latency for nothing, and reasoning modes amplify that.

**Iterate on the prompt, not the output.** Editing the model's answer teaches you nothing reusable. Editing the instruction, then re-running, is the part that compounds.

**Structured outputs are a contract, not a request.** "Please return JSON" is a plea. Constrained decoding against a schema is a guarantee, and where a platform offers it, use it instead of prompt-based pleading.

**Prompting is model-specific.** The same prompt frequently performs differently across families because instruction tuning differs. When comparing models, adapt the template minimally rather than concluding that one model "cannot follow instructions".

### How it connects to the rest of the framework

`TSC4-Intermediate-K1` explains why these techniques work — probability over the next token. `TSC4-Intermediate-A4` is the quality-and-coherence lens you apply to the result. `TSC4-Intermediate-A6` compares models fairly, which requires holding the prompt constant or adapting it per family. `TSC4-Intermediate-A2` extends today's prompting into domain and style control with examples. `TSC4-Intermediate-K4` covers the tool-level handling — settings and iteration discipline.

### What is current as of November 2026

For the 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — prompting has become less incantatory and more like specification:

- **Instruction-following improved enough that elaborate prompt tricks retired.** Persona priming, threats and "take a deep breath" rituals mostly stopped paying. Clear specification is now the differentiator.
- **Long context made example-stuffing cheaper but not free.** Twenty examples fit; they still cost tokens and prefill time, and three usually suffice.
- **Native structured output and tool calling moved a whole category of prompting into configuration.** JSON validity, function arguments and citation formats are enforced at the decoder, not coaxed in prose.

### Common misconceptions

- *"A better prompt can fix a model that cannot do the task."* Prompting buys compliance, not capability. Past a capability ceiling, more words do nothing.
- *"Longer prompts are more thorough."* Longer prompts dilute instruction and cost more per call. Precision, not volume.
- *"Politeness improves accuracy."* It occasionally changes style. It is not a reliability lever.
- *"If the model ignored my constraint, it is broken."* Usually the constraint was buried, contradicted by another line, or stated once among ten priorities.

## How a student should understand it

**Mental model:** a brief to a capable freelancer who has never met you. Vague briefs produce competent generic work; precise briefs produce the thing you needed.

**Things they can do after this bullet:**
1. Rewrite a weak prompt using the four levers and show the improvement.
2. Add two examples to fix a style or format problem.
3. Explain why a model evaluation must name the prompt used.

**Misconceptions to kill:** that prompting is about magic phrases, that model quality can be judged without holding the prompt fixed, and that a failed output means a failed model.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The renovation brief.** "Make it nice" gets you a contractor's taste. "Open kitchen, matte white cabinets, no downlights, keep the service yard" gets you your kitchen. Same contractor, same day rate — different brief.

**The new hire's first week.** You would not say "write something about our product". You would say what it is for, who reads it, how long, and show one example of a good one.

### Worked example with a real tool

Run the weak prompt, then the strong one, and let the room see the delta:

```text
Weak: "Write about our new clinic opening."

Strong: "You write for a neighbourhood clinic in Tampines.
Audience: residents aged 50+, many read Chinese at home but receive
this in English. Task: a 90-word notice announcing our new Queenstown
branch opening on 3 December, 8am-5pm weekdays.
Include: the MRT exit, that existing appointments continue.
Exclude: prices, superlatives, exclamation marks.
Format: one short paragraph, then three bullet points.
Tone example: 'Our Tampines clinic now opens at 7.30am, so you can
come before work.'"
```

What to point at afterwards: the strong prompt adds audience, constraint, exclusion, format and a tone example, and the output changes in all five dimensions. Then ask the room to break it deliberately — remove the exclusions, and watch the exclamation marks return.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run the weak prompt live; project the generic result.
2. **State the objective** — by the end you can turn a vague request into a five-part brief.
3. **Recall prior learning** — next-token prediction and why continuation probability is steerable.
4. **Present the content** — the four levers, few-shot, reasoning on request, output contracts.
5. **Guide** — rewrite one learner's real prompt together on screen.
6. **Elicit performance** — each pair rewrites a second prompt and tests it on a neighbour.
7. **Give feedback** — compare outputs; name which lever caused which change.
8. **Transfer** — each learner takes the brief back to a task they do weekly.

## What the framework doesn't mention but trainers need to know

- **Prompt hygiene is version control.** A prompt that lives in someone's notes app is not an asset. Registry, diff, owner.
- **Prompt length has a cost curve.** A 5,000-token prompt on every call pays for the prefill every time; caching helps, distillation helps more.
- **Model-specific templates are mandatory for failover.** A prompt tuned with one family's formatting conventions can degrade sharply on another.
- **Injection is a prompting problem with security consequences.** Any prompt that includes retrieved or user-supplied text can be overridden by it. Structure the prompt so data sits clearly apart from instructions.
- **Consistency is a prompt property too.** Two runs at high temperature will differ; if the workflow needs identical output, that is a sampling decision as much as a wording decision.

## Watch out

- **Do not teach "magic prompts".** They age out within a generation and teach the room to collect folklore instead of specifications.
- **Do not demo only on a creative task.** The room concludes prompting is for marketing. Show extraction and classification too.
- **Do not compare two models with two different prompts and call it a model comparison.** That is the single most common methodological error in the room.
- **The stale claim to retire:** "prompt engineering is dead because models got smart." Specification never dies; the tricks did.
