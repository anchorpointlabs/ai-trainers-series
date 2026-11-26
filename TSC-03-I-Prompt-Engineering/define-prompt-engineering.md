---
id: 03.02.I.A1
tsc: 3
level: Intermediate
code: A1
title: Define prompt engineering
---

# Define prompt engineering

> **TSC #3 Prompt Engineering · Intermediate · Ability A1**

> **Framework text (verbatim):** "Define prompt engineering."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Ability · Bullet 7 of 13

**One-line version:** Prompt engineering is prompt design with a test set — the moment a prompt must work on inputs nobody has seen, writing clearly stops being enough.

## What it is

Prompt engineering is the systematic design, testing and refinement of the text sent to a model, so that it produces the intended output reliably across many inputs. It happens entirely at inference time: the model's weights are untouched, and everything the model needs must be inside the prompt. It covers two environments — ad-hoc conversation, and programmatic templates that run without a human in the loop.

## Deep expansion

### The concept

The definition has three parts and learners usually keep only the first. **Design**: choosing role, context, task, format. **Test**: running the prompt against a set of real inputs and scoring it. **Refine**: changing one thing at a time and re-running the set, because a fix for one case routinely breaks another.

The distinguishing word is *engineering*, and it has a precise threshold. Prompt **design** ends and prompt **engineering** begins when the prompt has to work reliably across **multiple unseen inputs, without a human editing it each time**. A prompt you tweak in a chat window until the answer looks right is design — skilled, useful, and dependent on your judgement in the loop. A prompt you ship into a template that runs on two hundred invoices at 2am is engineering: the judgement has to be moved into the artefact as rules, examples, schema and a failure branch, and then measured.

That threshold matters because it changes the deliverable. A designed prompt is a message. An engineered prompt is a small artefact with variables, an output contract, a version number and a set of inputs it is known to handle.

### The sub-concepts

**Four boundaries learners must be able to draw.** Each is a different intervention, and confusing them is the most common Intermediate-level error.

- **Prompt engineering versus prompt design** — the line above: unseen inputs, no human fix-up.
- **Prompt engineering versus context engineering** — prompt engineering writes the behavioural rules and the static template; context engineering builds the pipeline that fills the template's variables: history truncation, memory, retrieved documents, user profile, tool output. One writes the sentence; the other decides what goes in the blank.
- **Prompt engineering versus fine-tuning** — if you changed the text sent to the model, it is prompting; if you ran a training job and got a new checkpoint, it is fine-tuning. Prompting uses working memory; fine-tuning changes instinct.
- **Prompt engineering versus RAG** — retrieval is search infrastructure outside the model; prompt engineering is the instruction inside the payload that says how to use what was fetched ("answer only from the sources, cite them, abstain if absent").

**The engineering artefacts.** A prompt template with named variables. An output schema. An explicit failure branch for inputs that do not support the task. A pinned model version. A small evaluation set of twenty to fifty real cases with known good answers. Remove any one and the prompt is still a draft.

**The iteration loop.** Draft a minimal baseline, run the set, bucket the failures (format, boundary, reasoning, hallucination), fix one cause, re-run the whole set. The re-run is not bureaucracy: in prompting, fixing edge case fourteen regularly breaks happy path three, and only the full set shows it.

**Knowing when to stop.** Prompting is the cheapest intervention and therefore the first to try, but it has a ceiling. If the task is exact arithmetic, use code. If the facts live in a large changing corpus, use retrieval. If you need a style internalised across thousands of subtle cases, fine-tune. If the task needs approvals and retries, it is a workflow, not a prompt. An engineer's competence is partly knowing which of these they are looking at.

### How it connects to the rest of the framework

`TSC2-Basic-K7` is the concept of prompt design this bullet extends, and `TSC3-Basic-K1` is design when a colleague has to run your prompt. `TSC3-Intermediate-K1` supplies the frameworks an engineered prompt is assembled from, `TSC3-Intermediate-A2` is the practice discipline, `TSC3-Intermediate-A6` is what misuse looks like when a template ships, and `TSC3-Intermediate-A5` is the model-matching that keeps a template working after a version change.

### What is current as of November 2026

The phrase has been declared dead repeatedly since the first wave of chat models, and remains in job descriptions, because the work moved rather than vanished. In late 2026 it means three things:

- **Specification plus tests.** With the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon following explicit instructions and schemas closely, the marginal value of clever phrasing has fallen and the marginal value of a written contract and an evaluation set has risen.
- **System prompts are shipped products.** A support assistant's system prompt is a maintained artefact with an owner, a changelog and a regression suite — closer to configuration than to copywriting.
- **Context, tools and permissions are the hard part.** With agents, the prompt now states what the model may do as well as what it may say, and that decision cannot be delegated to a sentence.

### Common misconceptions

- *"Prompt engineering is finding magic phrases."* The phrases changed nothing durable; the structure did. Anyone selling a secret wording is selling folklore.
- *"It is just writing clearly."* Clear writing is necessary and insufficient. The engineering is the test set, the failure branch and the version control.
- *"It is dying because models are getting smarter."* Better models raise the ceiling on what one prompt can do; they do not remove the need to specify, test and check.
- *"It is the same as prompt design."* Design is a message; engineering is an artefact with a contract and a known failure mode.

## How a student should understand it

**Mental model:** the difference between asking a colleague for a favour and writing the standing operating procedure the whole shift will follow at 3am when you are not there. Both need clarity. Only one needs a test.

**Things they can do after this bullet:**
1. Define prompt engineering in one sentence, including the word *reliably*.
2. Place a given task on the design-versus-engineering line and say why.
3. Name the neighbouring discipline — context engineering, RAG, fine-tuning, workflow — that a failing prompt actually needs.

**Misconceptions to kill:** that it is magic wording; that it is only clear writing; that it is obsolete.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The WhatsApp order and the purchase order.** A WhatsApp message to your regular supplier works because you both know each other; when the message goes to a new supplier with no context, you need a purchase order with fields, a signature and a rejection path. Prompt engineering is writing the purchase order. Where it breaks: a purchase order is enforced by process, while a prompt is enforced only by how well you wrote it.

**The recipe and the kitchen SOP.** A recipe assumes a cook who tastes and adjusts. The SOP for a chain outlet specifies the gram weight, the holding time and what to do when the fryer is down — because the person following it may be on their first week. Same dish, different artefact, different rigour.

### Worked example with a real tool

Take a prompt the room has written, put it in a template, and give it five real inputs (two normal, two messy, one that should fail):

```text
v1
Summarise this complaint and say what we should do.

v2
Read the complaint below and return exactly:
- Issue: one sentence
- Severity: LOW | MEDIUM | HIGH (HIGH if a refund, injury or regulator is mentioned)
- Action: one sentence, addressed to the branch manager
- Missing: list any fact needed to act that the complaint does not contain

If the complaint contains no actionable issue, return "NO_ACTION" and stop.

<complaint>{{COMPLAINT_TEXT}}</complaint>
```

Run v1 on all five and tally which answers a manager could act on without asking a question. Then v2. What to point at afterwards: v1 is not badly written and it fails on the messy inputs — that is the difference between design and engineering. Then change one rule in v2, re-run all five, and show a case that got worse. That single move teaches the loop better than any slide.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a beautifully written prompt failing on a real, messy input.
2. **State the objective** — by the end you will define prompt engineering and place three tasks on the design-versus-engineering line.
3. **Recall prior learning** — what do they already know about prompt design and its elements?
4. **Present the content** — the definition, the threshold, the four boundaries, the artefacts.
5. **Guide** — build v2 of the complaint prompt together, arguing about the failure branch.
6. **Elicit performance** — pairs write a five-case test set for one of their own prompts.
7. **Give feedback** — run two pairs' sets; count how many answers are usable without follow-up.
8. **Transfer** — each learner names one prompt they will convert from design to engineering this month.

## What the framework doesn't mention but trainers need to know

- **Evaluation is the skill nobody teaches.** Twenty real cases with known answers beats any amount of prompt polish, and it is the thing learners will not do unless you make them do it in class.
- **Most production prompts are short.** The forty-line template with a schema and a failure branch outperforms the 600-word "mega prompt" almost every time.
- **The handover is the test.** If a colleague cannot run it correctly from the file alone, it is not engineered.
- **Version drift is real.** Providers update models; a prompt that worked in March can behave differently in September. Pinning a version and re-running the eval set is the cheap insurance.
- **Boundaries are examinable.** Learners are assessed on distinguishing prompting from fine-tuning and retrieval; teach the one-line test for each.

## Watch out

- **Do not teach a 200-line template as the ideal.** It signals that length is rigour, and it is unreviewable.
- **Do not demo without a test set.** A single successful run teaches the room that one success is evidence.
- **Do not oversell the job title.** The work is real; the mystique is not. Overselling gets you a sceptical IT manager and an hour of defensiveness.
- **The stale claim to retire:** "prompt engineering is dead, just talk to the model." Talking to the model is design. The engineering is what makes it survive Tuesday.
