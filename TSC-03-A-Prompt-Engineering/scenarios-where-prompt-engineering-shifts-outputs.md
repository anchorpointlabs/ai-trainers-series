---
id: 03.03.A.K1
tsc: 3
level: Advanced
code: K1
title: Scenarios where prompt engineering shifts outputs
as_at: 2026-11-26
review_by: 2027-02-25
---

# Scenarios where prompt engineering shifts outputs

> **TSC #3 Prompt Engineering · Advanced · Knowledge K1**

> **Framework text (verbatim):** "Scenarios where prompt engineering significantly influences outputs."
>
> **TSC #3** Prompt Engineering · **Advanced** · Knowledge · Bullet 1 of 13

**One-line version:** Prompt engineering pays off where the brief is ambiguous, the stakes are high or the shape of the answer matters — and pays nothing where a lookup, a formula or a spreadsheet would do.

## What it is

Prompt engineering is the deliberate design of instruction, context and output format so a model's response becomes predictable across many inputs, not lucky on one. The framework's word is *significantly*: the skill is not "write prompts" but "recognise the situations where the prompt is the lever that moves the result". Those are a minority of workplace tasks, and naming the others is half the competence.

## Deep expansion

### The concept

A prompt is a conditioning sequence: every token in it shifts the probability of every token that follows. That produces two different effects. It can raise the **mean** — a better answer than the lazy version. It can also cut the **variance** — the same shape of answer when the prompt runs on a hundred different inputs. Learners notice the first in a chat window; the second is what a process can be built on.

So "significant influence" is a property of tasks with room for interpretation. Where the task is fully specified — tax at 9%, a column sum, today's date — the prompt has nowhere to act. Where it is under-specified, the prompt does almost all the work, and the gap between a vague one and a structured one is the gap between advice and an artefact.

Five scenarios where the prompt reliably moves the result:

1. **An ambiguous brief with a known reader.** "Summarise this" has no answer; "five bullets for a director deciding whether to approve, lead with cost" does.
2. **A high-stakes review.** Contract or claim checking needs an abstention branch and a citation rule, or the model fills gaps confidently.
3. **An output that must fit a shape.** A roster, a table, a JSON payload the next system will parse. Format is the deliverable.
4. **Many similar items.** One template across two hundred enquiries needs edge-case rules, or the two hundredth breaks it.
5. **Multi-step reasoning.** Eligibility, constrained rostering, calculations with a rule attached.

Four where it does not: **deterministic work** (arithmetic, date maths, counting — use code); **facts the model cannot have** (after cut-off, behind permissions — retrieval, Bullet 5); **a single lookup** (open the document); **a task with no acceptance test** (if nobody can say what correct looks like, no wording makes it reliable).

### The sub-concepts

**Teach the decision order, not the technique list.** Ask in sequence: can code do this deterministically? Are the facts outside the model? Does one clean prompt with a schema and a reasoning step hit the standard? Do examples or a two-stage chain close the gap? Fine-tuning last. Learners who memorise the order stop using a generative model to add up a column.

**Signal density beats length.** Repetition, warnings and thirty micro-rules dilute attention across more tokens. A short prompt with a task, a source, three constraints and a format routinely beats a three-page one, and is maintainable.

**Structure, not vocabulary.** The gain comes from role, supplied context, ordered steps, constraints and output format — not from a magic phrase or politeness.

**Design versus engineering.** Design is a good instruction for one task with a human reading the reply. Engineering begins when one prompt must work on unseen inputs without a person fixing it. This bullet sits on the engineering side: the scenarios that matter repeat.

### How it connects to the rest of the framework

`TSC2-Basic` is the design layer — audience, tone, structure for a one-off. Bullet 2 (`TSC3-Advanced-K2`) names the three levers; Bullet 3 (`K3`) is ordering and the optimisation loop; Bullet 9 (`A3`) is how you prove help happened; Bullet 11 (`A4`) is whether it survives another scenario. `TSC1-Basic-K06` supplies the ceiling, and Bullet 5 (`K5`) covers what this bullet says to route elsewhere.

### What is current as of November 2026

Current frontier models tolerate a vague brief far better than their 2023 ancestors. Three consequences:

- **The weight moved from phrasing to supply.** When the model can infer a reasonable structure, clever wording buys less and the right source, example and checkable format buy more.
- **Planning models reward a goal, not a script.** Telling a model that plans its own steps to "think step by step, then step 1, step 2…" adds latency and can degrade output.
- **The ceiling relative to other tools dropped.** Retrieval and tool calling became ordinary product features, so more tasks now belong on the "route it elsewhere" side. The scenario test matters more, not less.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A longer prompt is a better prompt."* Length without structure is noise; extra words that carry no constraint dilute the ones that do.
- *"There is a magic phrase."* There is a task statement, material, constraints and format. Incantation-hunting never develops judgement.
- *"If prompting fails, prompt harder."* Often the answer is a spreadsheet, a query, a retrieval step or a human.
- *"It worked, so the prompt is good."* One run on one input is an anecdote. Bullet 9 exists to answer the twentieth input.

## How a student should understand it

**Mental model:** briefing a very fast contractor who has read everything, has never been to your office, and will never ask a clarifying question — it guesses, confidently, and the guess is what you get.

**Things they can do after this bullet:**
1. Sort six real tasks into prompt / code / retrieve / ask a human, and defend the sort.
2. Write weak and structured versions of one request, and predict which parts of the output differ.
3. Name the acceptance test before writing the prompt.

**Misconceptions to kill:** that prompting is universal; that length equals quality; that a fluent answer is a correct one.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**"Cook something nice" at a zi char stall.** Say that and you get *a* dish — the most common one the kitchen knows. Say "hor fun, two persons, less oil, no cockles, dabao" and you get dinner. Where it breaks: a stall has a fixed menu, while a model will attempt anything; the analogy teaches specification, not capability.

**The complaint form with a free-text box.** The same complaint in a blank box is read differently by every officer; in fields — category, date, amount, remedy sought — it gets processed. Where it breaks: forms are fixed in advance, prompts are written per task, so the learner is the form designer.

### Worked example with a real tool

```text
Weak: Help me with the staff roster.
```

```text
Strong: You are the admin for a 12-person clinic. Build next week's roster.
Each staff works 5 days, max 2 weekends a month, and Nurse A cannot work
Friday. Output a table with day, shift, and staff name. If any constraint
is impossible, say which one and why.
```

What to point at: the weak prompt returns advice *about* rostering. The strong one returns a table you could use, or a named conflict. Then delete the last sentence and re-run — the model quietly puts Nurse A on Friday. The deletion is the lesson: one sentence defined behaviour at the boundary.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — each learner writes the vaguest instruction they have given an AI this month; read three out.
2. **State the objective** — decide, for any task, whether better prompting will help, and what to do instead when it will not.
3. **Recall prior learning** — what makes a work instruction good for a new staff member: who, what, by when, what to do if information is missing.
4. **Present the content** — the five scenarios, the four negative cases, then the decision order.
5. **Guide** — run the roster pair, delete the boundary sentence, watch it fail.
6. **Elicit performance** — pairs write weak and strong versions of one of their own tasks and predict the difference before running both.
7. **Give feedback** — project two pairs; ask which difference came from structure and which from luck.
8. **Transfer** — each learner names one task they will route away from prompting this week, and to what.

## What the framework doesn't mention but trainers need to know

- **The acceptance test is the missing fifth lever.** "Significantly influences" is unmeasurable without one. Writing the pass/fail sentence before the prompt converts opinion into evidence.
- **The workflow after the output decides the format.** A draft that must be pasted into a system that strips tables is not a good output. Ask what happens next.
- **Cost and latency are part of "significantly".** The same task on a frontier model and a small fast tier can differ by an order of magnitude in price and seconds.
- **Most value is transformation, not creation.** Summarise, rewrite, extract, convert, check. Trainers who demo only poetry misrepresent where the hours are.

## Watch out

- **Do not demo one lucky run.** Show the same prompt on three inputs, or the room learns that prompting is a performance.
- **Do not overclaim.** "It understands your business" is false and will be quoted back at you.
- **Do not teach tricks as the skill.** "Act as a world-class expert" is decoration; supplied material and explicit rules are not.
- **The stale claim to retire:** "a clever enough prompt can do anything a fine-tune can." Prompts, retrieval, tools and training each have a job; the scenario test is how you pick.
