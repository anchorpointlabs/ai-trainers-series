---
id: 01.02.I.K3
tsc: 1
level: Intermediate
code: K3
title: "What a prompt actually changes: steering the distribution, not giving orders"
as_at: 2026-11-26
review_by: 2027-02-25
---

# What a prompt actually changes: steering the distribution, not giving orders

> **TSC #1 Generative AI Principles and Applications · Intermediate · Knowledge K3**


> **Framework text (verbatim):** "Impact of prompt engineering on the model outputs of generative AI."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Knowledge · Bullet 3 of 10

**One-line version:** A prompt does not command the model; it changes the evidence about what text should come next — so learn which lever moves which part of the answer, and test the change rather than trusting it.

## What it is

Prompt engineering changes output because the prompt is the conditioning context for a prediction. Every constraint you add narrows the region of the distribution the model samples from. At Intermediate level the skill is knowing which property of the output each lever controls, and how to prove the lever worked.

## Deep expansion

### The concept

Learners arrive with a command model of language: say it clearly and a competent assistant complies. Generative models are not compliant, they are *suggestible in a direction*. Given a vague task, the model produces the most statistically typical response to that task — precisely the generic answer the learner complains about. Given context, a format specification and two examples, it produces something close to a professional artefact, because that is what text in that shape looks like.

So prompt quality is mostly a **specificity and structure** problem, rarely a wording problem. "Be concise" describes an outcome; "exactly 120 words, three bullets, no adjectives" can be checked against the output.

### The sub-concepts

**Conditioning, not instruction.** Framing the task — "monthly commentary for a CFO who reads in 60 seconds" — moves the sampled region further than adding emphasis does.

**Specificity moves the target.** Audience, length, source, format and a missing-information rule each remove a family of plausible answers. Vague prompts do not get worse thinking; they get the most common phrasing of the task.

**Examples beat adjectives.** Two short input–output pairs fix format and register more reliably than a paragraph of description, because they show the distribution instead of describing it.

**Structure reduces variance.** Delimiters around source text, headings in the instructions, an explicit schema. When the model can see where the instruction ends and the data begins, it stops blending them.

**Context beats memory.** Supplying the document beats asking the model to recall it. Most "it got our policy wrong" complaints are prompts that asked the model to remember what it was never told.

**Model dependence.** A prompt is not portable: templates tuned on one vendor degrade on another, and prompts tuned on a fast tier degrade on a reasoning model that wants the problem statement, not step-by-step hand-holding.

### How it connects to the rest of the framework

`TSC1-Intermediate-K01` explains why conditioning works. `TSC1-Intermediate-A04` is the measurement half — no prompt change should be adopted without a before-and-after on a fixed set. `TSC1-Basic-A01` is the basic skill per output type, and `TSC3` (Prompt Engineering) is the technique catalogue this entry deliberately does not duplicate.

### What is current as of November 2026

Prompting is now less about clever phrasing than about **specification and control**. Reasoning models respond better to a clear problem statement with constraints and success criteria than to a scripted chain of steps; over-scaffolding one often makes output worse.

Structured outputs moved format enforcement out of the prompt altogether: where an API accepts a JSON schema, the platform guarantees the shape. Meanwhile "prompt engineer" as a job title has cooled while the skill of writing a precise brief has not — and knowing whether a change helped is still the hard part.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"There are magic phrases that unlock better answers."* Personas shift tone slightly and add no capability; the effect is small next to supplying the source document.
- *"Longer prompts are more thorough."* Past a point, extra text dilutes the instruction and pushes the key constraint out of effective attention.
- *"Prompt engineering is dead because models got smarter."* Models infer intent better; they did not acquire your documents, house style or definition of "concise".

## How a student should understand it

**Mental model:** the order slip at a hawker stall. Same stall, same wok, same cook — "less oil, no cockles, extra egg, takeaway" changes the plate. It cannot turn char kway teow into another stall's recipe, and it cannot fix fish that arrived unfresh.

**Things they can do after this bullet:**
1. Rewrite a vague prompt into a brief with audience, source, format, length and a missing-information rule.
2. Name which lever they changed and which property of the output should move.
3. Predict which of two prompts will be more consistent, and be right more often than not.

**Misconceptions to kill:** magic phrases, longer-is-better, and the idea that a prompt substitutes for missing data.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The PSLE composition brief.** "Write a good composition" produces the average Primary 6 essay; "150 words, one incident, show don't tell, set it in a wet market, end on a sound" produces something a teacher can mark. Same student, different brief. Where it breaks: a tutor asks questions; a model fills gaps silently.

**The renovation quotation.** "How much to renovate my flat?" gets a useless range. "Four-room resale, 90 sqm, kitchen and two bathrooms, no structural hacking, quote by item" gets a number you can compare.

### Worked example with a real tool

Same task, two prompts, in ChatGPT or Claude. Paste a small sales table first.

```
Weak: "Write a summary of this month's sales."
```

```
Strong: "You are writing the monthly sales commentary for a Singapore F&B
chain's management report. Audience: the CFO, who reads it in 60 seconds.
Using only the table above, write 120 words covering what changed, the two
biggest drivers, and one risk. Do not speculate beyond the numbers. If a figure
you need is not in the table, write 'not in data' instead of estimating."
```

What to point at: the weak version invents drivers and a cause — plausible, none traceable. The strong version's every claim maps to a row. Then ask for one sentence on *why* sales fell and watch it speculate again: the constraint holds until you relax it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show both commentaries; ask which they would send.
2. **State the objective** — by the end you can convert a vague request into a testable brief.
3. **Recall prior learning** — prediction and average-case fit.
4. **Present the content** — conditioning, specificity, examples, structure, model dependence.
5. **Guide** — rewrite one prompt live, taking suggestions from the room.
6. **Elicit performance** — pairs improve one prompt using an assigned lever.
7. **Give feedback** — compare on screen; name the lever behind each difference.
8. **Transfer** — each learner rewrites one prompt from last week and tests it on five items.

## What the framework doesn't mention but trainers need to know

- **Effects are not additive.** Fixing format can reduce coverage; adding examples can cause copying. Evaluate rather than stack.
- **Prompt injection is a prompt fact.** Any pasted page or email can carry instructions. Treat pasted text as data, never as commands.
- **Personal data in prompts is a PDPA question.** Prompts are transmitted, logged and sometimes retained — the prompt is a disclosure; `TSC1-Basic-K08` draws the line.

## Watch out

- **Do not teach jailbreaks in a corporate class.** They get copied into contexts where they cause harm, and they teach that prompting is a game of tricks.
- **Do not present a template as portable.** Say so before someone rolls it out across three platforms.
- **The stale claim to retire:** "adding please and a tip improves results." Such effects are small and unstable next to giving the model the right information.
