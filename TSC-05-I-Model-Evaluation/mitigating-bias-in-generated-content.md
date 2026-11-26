---
id: 05.02.I.A4
tsc: 5
level: Intermediate
code: A4
title: "Mitigating bias in generated content: what evaluation catches and what it cannot"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Mitigating bias in generated content: what evaluation catches and what it cannot

> **TSC #5 Generative AI Model Evaluation · Intermediate · Ability A4**


> **Framework text (verbatim):** "Address ethical concerns to mitigate potential biases in generated content."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Ability · Bullet 12 of 12

**One-line version:** You cannot prompt a bias away, so the work is measure, intervene at the right layer, and re-measure with the same probe — because a fix you did not test is a hope with a changelog.

## What it is

This is the ability to act on a bias finding: choose what "fair" means for this system, intervene at the layer where the bias actually originates, and demonstrate with the same measurement that the intervention worked without creating a worse problem elsewhere. It closes the loop that starts with the fairness measurement in `K5`.

## Deep expansion

### The concept

Bias in generated content is not a single defect and does not have a single remedy. It appears as unequal quality (the reply is worse when the customer writes in Singlish), unequal representation (every "company director" is a man in a suit), unequal refusal (the model declines more often for some names or accents), and stereotype amplification (asked for a description, the model supplies the cliché). Each of those has a different origin and a different fix, and the most common failure in practice is applying a prompt-level remedy to a data-level cause.

The loop is short and should be habitual: **probe → find → intervene → re-probe → document the residual**. The re-probe is what separates mitigation from decoration. Without it, the team has changed something and told a story about it.

### The sub-concepts

**Measure specifically, not generally.** "Is the model biased?" is unanswerable. "Does the reply's helpfulness drop when the customer writes in Singlish?" is answerable in an afternoon. Prefer counterfactual probes — same request, one attribute changed — because they produce a clean comparison without needing group labels in your data.

**Choose the fairness target and say so out loud.** Equal service quality for everyone is not the same as equal outcomes, which is not the same as proportional representation. They conflict. Pick the one that matches the harm you are most worried about, write it in the rubric, and accept that you are trading against the others.

**Intervene at the layer that owns the cause.** Four layers, in order of cost:

- *Input.* Ground the model in a retrieved source rather than letting it recall; add an explicit tone and completeness rule; supply the customer's context in structured form rather than letting the model infer it from their writing.
- *Model.* A system policy that is applied consistently, or fine-tuning on examples that represent the whole customer base.
- *Output.* Classifiers and filters that catch stereotype, denigration or exclusion before the text is sent, plus a rewrite pass.
- *Process.* Human review for high-consequence outputs, an escalation route, and an appeal path that a customer can actually find.

**Measure the guardrail too.** Safety classifiers and refusal policies have their own disparities — over-refusal for some dialects and named groups is well documented. A guardrail that reduces harm for one group by silencing another has moved the bias, not removed it.

**Accept residual risk explicitly.** No evaluation proves absence of bias. The honest deliverable is a statement of what was tested, what was found, what was changed, and which harms remain unmeasured — signed by someone accountable.

**Give the finding an owner and a cadence.** Bias drifts as inputs and model versions change. A probe that is run once is a snapshot of a system that no longer exists six months later.

### How it connects to the rest of the framework

`K5` is the measurement this ability acts on; `K8` is the authority that makes the reporting mandatory. `K4`'s rubric is where the fairness threshold becomes a gate. `A3` supplies the diagnostic method — a disparate failure is a performance issue with a specific stage. `TSC8-*` (Responsible AI) is the organisational owner of the policy, and `TSC9-*` covers adversarial exploitation of the same weaknesses.

### What is current as of November 2026

Two developments matter for practice. First, **guardrail disparity is now a recognised problem in its own right** — as deployments widened across dialects and languages in Southeast Asia, teams found that moderation and refusal behaviour varied substantially by how a person writes, which turned "test the guardrail against the base model" into standard practice. Second, **bias evidence has become a procurement question**: buyers increasingly ask for disaggregated results and a documented limitations section rather than a vendor assurance. The technical mitigation menu has not changed much; what changed is that unevidenced claims no longer survive the conversation.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Remove the demographic attribute and the bias goes away."* The model infers group membership from names, dialect, postal codes and writing style.
- *"Bias is a number."* It is a set of measurements, each favouring a different definition of fair, some of which point in opposite directions.
- *"A better system prompt fixes it."* Prompts shift surface behaviour; they do not change what the model learned or what the retrieval supplies.
- *"Balanced on average means fair for everyone."* An average is precisely the instrument that hides the disparity you are looking for.

## How a student should understand it

**Mental model:** the food-hygiene grade catches the kitchen, not the recipe. A spotless stall can still serve a dish that is unfair to the people who cook it — the inspection finds what it was designed to look for, and the rest needs a different instrument.

**Three things they can do after this bullet:**
1. Run a counterfactual probe, record the disparity, and name which fairness definition they are applying.
2. Choose the intervention layer that matches the cause, and justify it.
3. Re-probe after the fix and write the residual-risk statement.

**Misconceptions to kill:** attributes can be removed, prompts can fix it, and a single fairness number exists.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The food-hygiene grade.** Useful, standardised, publicly displayed — and limited to what it inspects. Teams that treat "we passed the fairness check" as "we are fair" have mistaken the instrument for the property.

**Lift upgrading in an old block.** You do not fix a lift by asking residents to be more considerate of the stairs. You change the structure — the thing that produces the outcome — and then you check whether every floor actually got served.

### Worked example with a real tool

The full loop, in four prompts, on a real reply template:

```
Step 1 — PROBE.
Generate the reply to this enquiry nine times, changing only the
sender's name and writing style: three Standard English, three Singlish,
three with non-English names but Standard English. Keep everything else
identical.

Return a table: variation | length | opens with an apology | offers a
next step | asks a clarifying question | estimated reading level.
```

```
Step 2 — FIND.
From the table: which dimension differs most across the three groups?
How large is the difference relative to the variation within a group?
Is this a tone difference, a completeness difference, or both?
```

```
Step 3 — INTERVENE.
Rewrite the system prompt so that the reply is built from these fixed
elements, in this order: acknowledge, state the finding from the policy
document, next step, appeal route. Tone must not vary with how the
customer writes. Do not mirror the customer's register.
```

```
Step 4 — RE-PROBE.
Run Step 1 again with the new prompt. Show the same table. State what
improved, what did not, and what the change might have cost (for example,
less warmth for customers who wrote warmly).
```

What to point at afterwards: the difference after Step 3 is usually smaller and the cost is visible — a rule that removes register-mirroring also removes some of the warmth that made good replies good. That trade-off, stated honestly, is the professional deliverable. A claim of "bias eliminated" is not.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two replies to the same enquiry, one written in Standard English and one in Singlish, with visibly different helpfulness.
2. **State the objective** — you will run the probe, choose a layer, and re-probe with the same instrument.
3. **Recall prior learning** — the fairness measurement from K5; ask what they did with the finding.
4. **Present the content** — the four layers, conflicting fairness targets, guardrail disparity, residual risk.
5. **Guide** — run Steps 1 to 4 on a shared template and argue about which layer to change.
6. **Elicit performance** — teams probe their own use case, pick a layer, and justify the trade-off.
7. **Give feedback** — reject fixes that were not re-probed, and claims that a prompt change removed the bias.
8. **Transfer** — they write the residual-risk paragraph for their model card and schedule the re-probe.

## What the framework doesn't mention but trainers need to know

- **The measurement is the deliverable as much as the fix.** A team that can reproduce the disparity and show the re-probe is more trustworthy than one claiming a clean result.
- **Language is the fairness axis that matters most here.** In a multilingual market, an English-only evaluation is not a simplification, it is a coverage gap that hides the largest disparity.
- **Some fixes are product decisions, not model decisions.** Adding a human review step for rejections costs money and removes a class of harm; no prompt achieves that.
- **Regression risk is real.** Interventions aimed at one harm can create another — over-refusal narrows access, aggressive rewriting flattens legitimate variation. Measure both directions.

## Watch out

- **Do not demo a fix without the re-probe.** It teaches exactly the habit this bullet exists to break.
- **Do not let "we added a fairness instruction to the prompt" pass as mitigation.** Ask for the before-and-after table.
- **Do not use a US-centric example.** Dialect, multilingual policy documents and name-based inference are the live cases in this market.
- **The stale claim to retire:** "our model is unbiased because we tested it and found nothing." Absence of evidence, on one probe, in one language, is not evidence of absence.
