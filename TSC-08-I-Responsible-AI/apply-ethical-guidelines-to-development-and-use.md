---
id: 08.02.I.A1
tsc: 8
level: Intermediate
code: A1
title: Apply ethical guidelines to development and use
---

# Apply ethical guidelines to development and use

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A1**

> **Framework text (verbatim):** "Apply ethical guidelines to AI development and use, considering fairness, accountability, transparency and sustainability etc."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 6 of 14

**One-line version:** A guideline you applied once is a document; a guideline you re-run at every gate is a control.

## What it is

Applying ethical guidelines means taking the checks the framework names — fairness, accountability, transparency, sustainability — and running them at each stage of build, test and deploy, then acting on whatever they flag. The output of each run is not a feeling but a recorded decision: fixed, accepted with a reason, or stopped.

## Deep expansion

### The concept

Guidelines fail at the handover. A governance team writes the policy, an engineering team writes the code, and nothing travels between them except a PDF. The gap is not bad faith; it is that the policy speaks in principles and the sprint speaks in tickets. Application is the translation layer: each principle becomes a question with an owner, a stage and an artefact.

There are two traps in teaching this bullet. The first is treating it as a single review at the end, which cannot undo a data decision made in month one. The second is treating it as an audit performed on someone else, which leaves the people making the decisions untouched. Applied guidelines are run by the team that is building, at the moment of the decision, and checked by someone independent afterwards.

The final piece is what happens to a flag. Most teams can generate a finding; few can close one. The professional habit is to force the flag into one of three outcomes — **fix it, accept it in writing with a named accepter, or stop** — because an unclosed flag is how an organisation learns to ignore its own checklist.

### The sub-concepts

**Checkpoints, not a review.** Each stage owns the check that is cheapest there. Design: who is affected and what could go wrong. Data: is every affected group represented, and are the labels defensible. Build: are the guardrails and permissions in place. Evaluation: are the metrics disaggregated. Deployment: is AI use disclosed and is there a named owner. A single review before launch can only catch what is still catchable.

**Two questions per check.** What would failure look like *here*, concretely? And who signs if it fails? A check with no named signer is a suggestion.

**Flag to decision, in writing.** Fix, accept, or stop — with a name and a date against each. The acceptance route is the one learners forget, and it is the one that keeps delivery moving without pretending the risk is gone.

**Proportionality.** A spam filter and a credit model should not pass the same gate at the same depth. Depth follows severity of harm and scale of population, which is why risk tiering comes before checklists.

**It applies to use, not only development.** Most Singapore organisations never train a model. They buy one, or their staff use one. The same checks apply to procurement (what does the vendor document?) and to sanctioned use (is the tool approved, is the data allowed?).

**Evidence is the artefact.** An assessment is a table of metrics by group, a model card, a disclosure script, a named owner in a register. If the check produced no artefact, it produced no evidence, and the organisation cannot show it did anything.

### How it connects to the rest of the framework

`TSC8-Intermediate-K1` supplies the four considerations being applied; `TSC8-Intermediate-A8` is where these checkpoints get designed into the lifecycle; `TSC8-Intermediate-A3` is what you do after a fairness check flags something; and `TSC8-Intermediate-A7` is how you decide whether the guideline you are applying is worth applying. `TSC8-Intermediate-K5` is the legal floor underneath all of it.

### What is current as of November 2026

Application has become cheaper and more mechanical. Singapore's AI Verify and Project Moonshot toolkits produce test evidence that used to require a consultant, and evaluation suites now run in a build pipeline rather than in a quarterly review. Enterprise buyers increasingly ask for that evidence, which means applying guidelines is now also a commercial skill.

The harder change is agentic systems. When a model can call tools, the "deployment check" is no longer only about disclosure — it is about permissions, approval steps and a kill switch. A guideline that was written for a chatbot that answers questions does not automatically cover a system that sends emails. The GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon all support tool use, so this is the default condition rather than an edge case.

### Common misconceptions

- *"We have a policy, so we have applied it."* A policy is an intention. Application leaves evidence at a stage.
- *"This is the developers' job."* It is the business owner's job to require it, the developers' job to produce it, and an independent function's job to check it.
- *"The checks slow delivery down."* Unclosed flags slow delivery down far more, usually in the quarter after launch.
- *"The check passed."* A check that finds nothing may be a check that looks at nothing. Ask what it would have caught.

## How a student should understand it

**Mental model:** the pre-flight checklist in a cockpit. It exists because the same two pilots fly the same aircraft every day and still forget the same four things, and because nobody wants the alternative.

**Things they can do after this bullet:**
1. Pick the two checks that matter most at a given stage and say what each would flag.
2. Produce the artefact that proves the check ran.
3. Close a flag as fix, accept or stop, with a name against it.

**Misconceptions to kill:** that a policy is an application, that checks belong to one role, and that a green result means nothing was found.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The VICOM inspection before COE renewal.** Nobody enjoys it, everybody does it, and it catches the brake problem before the expressway does. Where it breaks: a car is inspected annually because it degrades predictably; a model can change the moment a prompt or corpus changes, so the interval has to follow change, not the calendar.

**The hawker stall's daily temperature log.** The log exists so that the day the fridge fails, somebody notices in the morning rather than at dinner. A log that is always "ok" is either excellent practice or an unopened notebook — you cannot tell from the log alone, which is why spot checks exist.

### Worked example with a real tool

```text
We are deploying a customer-support assistant next week. Run the four checks at the
deployment stage only.

For each of fairness, accountability, transparency and sustainability give me:
- what failure would look like for this specific tool,
- the one question I must be able to answer before launch,
- the artefact that answers it,
- the role that signs.

Then rank the four by how likely this team is to skip each one, and tell me the single
cheapest control I could add in a day.
```

What to point at afterwards: the model will produce four tidy rows and then, in the ranking, quietly reveal the pattern — transparency and sustainability get skipped because nobody is measured on them. That ranking is the useful output, and it is the one a learner can take back to their own team.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask how many checks their last release passed, and who signed.
2. **State the objective** — by the end you can run a stage check and close the flag.
3. **Recall prior learning** — connect to the four considerations from K1.
4. **Present the content** — stage-by-stage checks, two questions per check, three ways to close a flag.
5. **Guide** — run the deployment check on the support assistant together.
6. **Elicit performance** — pairs run the check for their own project's current stage.
7. **Give feedback** — mark any flag that was raised and not closed.
8. **Transfer** — each learner adds one check to their team's release template.

## What the framework doesn't mention but trainers need to know

- **Somebody must have the authority to stop.** A check without a stop power is a suggestion box. Name the veto holder before you need them.
- **Checks detach from ownership at scale.** A check that worked for one prototype silently disappears when the prototype becomes a product with three squads.
- **Cost is part of the decision.** A fairness fix can require a data-collection programme. Saying "fix it" without a budget is how the flag gets parked.
- **The sustainability check is usually one line**, and one line is better than nothing: which model tier, what volume, what alternative was considered.

## Watch out

- **Do not demo with production data**, and do not screenshot a real customer record into a slide.
- **Do not let a passing test be reported as "bias solved".** It means this test found nothing at this threshold.
- **Do not teach the checklist as the goal.** The goal is a decision that would have gone differently.
- **The stale claim to retire:** "we do an ethics review before launch." In November 2026 the review is a pipeline, and the pipeline runs on every change.
