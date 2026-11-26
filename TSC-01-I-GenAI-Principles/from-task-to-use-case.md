---
id: 01.02.I.A1
tsc: 1
level: Intermediate
code: A1
title: "From task to use case: applying the principles before you prompt"
as_at: 2026-11-26
review_by: 2027-02-25
---

# From task to use case: applying the principles before you prompt

> **TSC #1 Generative AI Principles and Applications · Intermediate · Ability A1**


> **Framework text (verbatim):** "Apply understanding of generative AI principles to use cases."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Ability · Bullet 6 of 10

**One-line version:** A use case is one step in a job, with a named input, a named operation and a named check — and if you cannot state all three, you do not yet have a use case, only an intention.

## What it is

Applying the principles means taking a job someone actually does and deciding, with reasons drawn from how the model works, which step it should perform, what it must have in front of it, and who checks the result. The output is not a prompt. It is a one-page decision a manager can approve or reject.

## Deep expansion

### The concept

Learners arrive with "can AI do this?" — the wrong question, because it invites a yes or no about a whole job. The practitioner question is "which step, fed with what, checked by whom". A whole-job request ("use AI for HR") has no owner, input or failure boundary, so it cannot be built, priced or refused. A step-level request ("draft the first reply to a candidate enquiry from the role brief, for a recruiter to edit") can be.

Five moves turn a task into a use case:

1. **Decompose.** Write the job as steps; mark each deterministic (a rule, a formula) or judgement-based. Generation belongs at the judgement steps only.
2. **Locate the truth.** Every output must be consistent with something — a policy, a contract, a spreadsheet. Decide where that source lives and whether it fits the model's working memory.
3. **Name the operation.** Summarise, infer, reason, transform or augment — `TSC1-Intermediate-A02`. Each carries a different verification bill.
4. **Predict the failure from the principle.** `TSC1-Intermediate-K01` is the forecast: thin patterns revert to the average, long inputs are attended unevenly, fluency is uniform across right and wrong.
5. **Set the check.** Who reads the output, against what, and what happens when it fails. A use case with no check is a liability with a demo attached.

### The sub-concepts

**Verifiability against cost of error.** Two axes decide whether a step is worth automating. Cheap to check, cheap to get wrong — let it run, spot-check weekly. Cheap to check, expensive to get wrong — automate the draft, keep the signature. Expensive to check, expensive to be wrong — do not start; the check costs more than the task. Drawn on a whiteboard, this quadrant settles most classroom arguments in ninety seconds.

**The input is most of the design.** Most failed use cases are input failures: a chat thread instead of the policy document, a summary instead of the source, a screenshot of a table instead of the table.

**Deterministic core, generative edge.** Where a rule decides — GST computation, leave entitlement, routing by keyword — use the rule. Generation sits where the language varies but the decision does not. Replacing a formula with a model is the most expensive mistake in this bullet.

**Scope discipline.** A use case that quietly grows a second operation acquires a second failure mode and a second check. "Draft the reply and decide whether to reject the candidate" is two use cases, and the second is the risky one.

**The human step is part of the design.** Time per accepted output, not accuracy alone, decides adoption. Saving four minutes of writing and adding six of checking is a net loss, however good the prose.

### How it connects to the rest of the framework

`TSC1-Intermediate-K01` supplies the mechanisms this ability applies; `TSC1-Intermediate-A02` supplies the menu of operations; `TSC1-Intermediate-A04` is how you prove the use case works rather than merely runs; `TSC1-Intermediate-A03` is the failure audit. `TSC4` (model selection) is the pricing and capability decision that follows, and `TSC6` is where the use case becomes a system. The Basic bullet `TSC1-Basic-K04` asks where generative AI helps at all; this asks which step, with what evidence and what check.

### What is current as of November 2026

Two product shifts have made "locate the truth" much cheaper. Source-grounded tools — NotebookLM most strictly — answer only from the documents you supply, refuse when the answer is absent, and cite to the paragraph. Search-first answer engines attach a footnote to each claim. Neither proves the claim, but both turn "where did this come from" from an investigation into a click.

The second shift is that a use case can now include an action. With tool access, the current frontier families complete sequences rather than return documents. The check moves from "read the output" to "approve the action", which is a governance decision. Structured outputs have meanwhile turned format compliance from a check into a constraint.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"We need to find a use case for AI."* The tool is looking for work. Start from a task that already costs hours or errors, then see whether a model belongs in it.
- *"Our use case is ChatGPT."* A product is not a use case. It has no input, no owner and no check.
- *"The demo worked, so the use case works."* A demo is one input and one output. A use case is a distribution, including the scanned page and the empty field.
- *"More automation is better."* The human check is a design element, not a phase we are growing out of.

## How a student should understand it

**Mental model:** the polyclinic triage nurse. The nurse does not treat anyone; the nurse decides which cases go to the doctor, which to the pharmacy, and which need an ambulance — and sends the ambiguous ones up rather than guessing. A use case is a triage decision about work.

**Things they can do after this bullet:**
1. Take one job from their own week and write its steps, marking deterministic against judgement.
2. Fill a one-page use-case card: input, operation, output, check, owner, failure mode.
3. Reject or defer a proposal with a stated reason instead of an opinion.

**Misconceptions to kill:** that the tool is the use case, that a demo is evidence, and that verification is optional overhead.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The zi char order.** "Cook something nice" gets you something edible and forgettable. "Sambal stingray, less chilli, no petai, for four people" gets you dinner. The use case is the order, not the wok — and the wok is the same wok either way. Where it breaks: a hawker can ask a clarifying question; a well-built use case has to have anticipated the answers.

### Worked example with a real tool

Procurement receives a 12-page vendor master services agreement and must compare it against the company's own procurement policy. In NotebookLM, upload both documents as sources, then:

```
Using only the two sources, list every clause in the Vendor MSA that conflicts
with the Procurement Policy. For each conflict: quote the MSA clause, quote the
policy rule it breaks, and say whether it is a hard conflict or a grey area.
If a clause is silent rather than conflicting, leave it out.
```

What to point at: the citation badges jump to the exact paragraph, so the check is a click, not a re-read. Then run the negative control — ask "Is this contract compliant with Singapore's Employment Act?" without uploading the Act. It refuses, and the refusal is the use case working: the tool cannot infer against a document it was not given. One demo, three lessons — input design, operation choice, the check.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask for one task from the room that eats an afternoon a week; write it on the board.
2. **State the objective** — by the end each pair has a use-case card someone else could build.
3. **Recall prior learning** — the principles: prediction, average-case fit, uneven attention.
4. **Present the content** — the five moves and the verifiability quadrant.
5. **Guide** — decompose the board's task together, out loud, including the reject option.
6. **Elicit performance** — pairs build a card for a task from their own work.
7. **Give feedback** — swap cards; the reader must be able to state the check without asking.
8. **Transfer** — each learner takes one card to their manager and one task they will deliberately leave deterministic.

## What the framework doesn't mention but trainers need to know

- **Data classification comes before the use case.** If the input contains NRIC numbers, patient data or unannounced financials, the licence tier decides whether the use case exists at all. Check the tier before the prompt.
- **The same use case is different on a consumer and an enterprise licence.** Copilot is the clearest example: the free web assistant, the M365 add-on and GitHub Copilot share a name and nothing else. Trainers who say "we will use Copilot" have not yet said which one.
- **Adoption is decided by rework, not accuracy.** Ask learners to time the check. A use case nobody has time to verify will be used unverified, which is worse than not using it.
- **Some tasks should stay deterministic and saying so earns credibility.** Summing a column, applying a leave formula, routing a form — a model here is slower, costlier and occasionally wrong.
- **Every use case needs an owner and a review date.** Without them the prompt outlives the policy it was written against.

## Watch out

- **Do not let the room leave with department-level use cases.** "AI for finance" is a slide, not a build. Push until the step is named.
- **Do not demo a use case you cannot verify live.** If you cannot show the check in front of the class, you are teaching confidence, not practice.
- **Do not present the quadrant as a score.** It is a conversation tool with judgement in it; the moment it becomes a number, someone will game it.
- **Do not equate a working prompt with a working use case.** The prompt is one component; the input, the check and the owner are the rest.
- **The stale claim to retire:** "AI projects fail because the model is not good enough." In most workplace failures the model was adequate and the input, the licence tier or the check was missing.
