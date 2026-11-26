---
id: 07.01.B.A1
tsc: 7
level: Basic
code: A1
title: "Reading a problem statement before choosing a model"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Reading a problem statement before choosing a model

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Ability A1**


> **Framework text (verbatim):** "Analyse problem statements and requirements to select and implement appropriate generative models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Ability · Bullet 11 of 15

**One-line version:** The model choice is downstream of six questions, and a learner who cannot answer them is not selecting a model — they are shopping.

## What it is

This is the ability to take a business problem in plain language, extract the requirements that actually constrain a technical solution, and turn those into a model choice you can defend. It is not "pick the biggest model". It is deciding what the output must be, how good is good enough, what it may cost, where the data may live, and whether the task is generation at all.

## Deep expansion

### The concept

Most failed AI projects fail at the framing stage, not the modelling stage. Someone says "we want AI for our claims process" and a team starts fine-tuning a model before anyone has established whether the task is classification, extraction, summarisation or generation — and those four need different models and different evaluations.

The six questions that do the work:

1. **What is the output?** Text, structured fields, an image, a decision, an action. Structured output usually means a smaller model plus a schema, not a bigger model.
2. **How will we know it is right?** If nobody can write down an acceptance test, the project is not ready. "Sounds good" is not a criterion.
3. **What data exists, and may we use it?** Volume, labelling, licence, personal data. This single question eliminates most options.
4. **What are the operating constraints?** Latency, throughput, cost per request, offline versus online, on-premise requirement.
5. **What is the risk of being wrong?** A drafting aid and a medical triage tool have different tolerances for error.
6. **Build, buy or adapt?** Prompt a hosted model, retrieve context into it, fine-tune an open model, or train something from scratch. In practice the order of preference is exactly that.

### The sub-concepts

**Task type before model family.** Generation, extraction, classification, ranking, transformation. Naming the type narrows the field immediately.

**The baseline.** A hosted model with a careful prompt is the baseline every other option must beat. Skipping it is how teams spend three months to match a two-hour prompt.

**Constraints as filters.** On-premise rules out hosted APIs. Sub-second latency rules out large reasoning models. A 2,000-document corpus rules out training from scratch.

**The sufficiency threshold.** "Good enough" is a number agreed before you start: a pass rate on a written rubric, a maximum error rate on a critical field. Without it, no result is ever acceptable.

**Reversibility.** Prefer the option that is cheapest to abandon. Prompting is reversible; a fine-tuned model with a bespoke pipeline is not.

### How it connects to the rest of the framework

`TSC4-Intermediate` is the fuller discipline of model selection — benchmarks, capability profiles, cost curves. `TSC6-Basic-K1` is the retrieval option. `TSC7-Basic-K8` is the fine-tuning option, and this bullet decides whether you reach it. `TSC7-Basic-A5` (identifying limitations and proposing improvements) is the loop that follows once you have chosen. `TSC5-Basic-K2` gives you the criteria to write the acceptance test this bullet demands.

### What is current as of November 2026

The decision has shifted from "which model is most capable" to "which is capable enough at an acceptable price". The GPT-6 generation, Claude 5.5 and Gemini 3.1 Pro are all broadly competent at general work; the differentiators that matter in a requirements conversation are context size, latency, tool use, data residency and price per token. Open-weight families — Llama, Qwen, Mistral, SEA-LION — have closed enough of the gap that on-premise and fine-tuned options are routinely viable.

The practical consequence: a requirements document that ends in "use the best model" is now the least useful kind. The useful document names the threshold, the constraint and the fallback.

### Common misconceptions

- *"Start with the most capable model and work down."* Start with the cheapest thing that might work and measure. Capability you cannot afford is not capability.
- *"The problem statement is the requirement."* A problem statement is a symptom. "Our agents take too long to answer" might be a knowledge problem, a UI problem or a training problem.
- *"Fine-tuning is the serious option."* Fine-tuning is one option, usually third. Prompting and retrieval come first for good reasons.
- *"We will know it when we see it."* Then you will not know when to stop, and the project will drift.

## How a student should understand it

**Mental model:** a renovation quote. Before anyone buys tiles, you agree on the flat, the budget, the deadline and whether the walls are load-bearing. The tiles are the model, and they are the last decision, not the first.

**Three things they can do after this bullet:**
1. Turn a paragraph of business need into the six questions, answered or explicitly flagged as unknown.
2. Write an acceptance test with a threshold before any model is tried.
3. Defend a build/buy/adapt choice in one paragraph, naming what would change your mind.

**Misconceptions to kill:** that the biggest model is the safe choice, that the stated problem is the requirement, and that "good enough" can be decided after seeing results.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The renovation quote.** A contractor who quotes before measuring is selling, not building. Requirements analysis is the measuring. It is also where you discover the client wants a different flat.

**The polyclinic triage.** A patient says "I feel terrible". The nurse does not immediately prescribe; they ask four questions and route accordingly. Most of the value is in the routing, and the routing depends on questions, not on the strongest medicine available.

### Worked example with a real tool

Give the room this brief and this prompt, typed into Claude or ChatGPT:

```
Brief: "Our HR team spends too long answering staff questions about
leave policy. We want AI to help. We have 40 policy PDFs, an intranet,
and staff who mostly use phones."

Act as a solutions architect. Do not recommend a model yet.
1. Restate the problem as a task type.
2. Ask me the six questions you need answered.
3. Then give me three options ranked by reversibility, with the
   evidence I would need to choose between them.
```

What to point at afterwards: the model will ask about output format, accuracy threshold and data residency — the questions the brief omitted. Then note that its first ranked option will almost always be retrieval over the PDFs, not fine-tuning. The learner's job is to check that reasoning, not accept it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out a vague brief and ask who would start coding today. Let three hands go up, then show the cost.
2. **State the objective** — by the end you can convert a brief into six answered questions and a defensible choice.
3. **Recall prior learning** — from TSC #6 they know RAG; from K8 they know fine-tuning. Now they choose.
4. **Present the content** — the six questions, the build/buy/adapt ladder, the acceptance threshold.
5. **Guide** — do one brief together on the whiteboard, leaving two questions unanswered on purpose.
6. **Elicit performance** — pairs take a brief from one learner's actual job and produce a one-page decision record.
7. **Give feedback** — challenge any record without a threshold; ask what number would make them abandon the option.
8. **Transfer** — each learner brings one real request back to their team and runs the six questions on it.

## What the framework doesn't mention but trainers need to know

- **The unanswered question is the finding.** A requirements session that ends with everything answered is usually a session where nobody pushed. Flag unknowns explicitly in the record.
- **Data permission outranks capability.** If the corpus cannot legally be used, the strongest model is irrelevant. Ask early, in writing.
- **The baseline is a political tool.** Showing that a careful prompt matches a proposed fine-tune saves budgets and credibility. Do it before, not after, the build.
- **Write the decision down.** One page: problem, threshold, options, choice, what would change it. Teams that skip this repeat the analysis every quarter.

## Watch out

- **Do not let the room jump to model names.** The moment someone says "we should use GPT-6", ask which of the six questions that answers.
- **Do not present fine-tuning as the advanced answer.** It is a tool with a narrow fit, and over-recommending it is the most common consultant error in this space.
- **Do not accept "accuracy" as a requirement.** Ask accuracy on what, measured how, by whom.
- **The stale claim to retire:** "pick the model with the best benchmark scores." In November 2026 benchmark leadership moves monthly and rarely predicts performance on a specific, narrow, well-specified task.
