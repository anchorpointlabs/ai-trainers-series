---
id: 05.03.A.K2
tsc: 5
level: Advanced
code: K2
title: "Explainable AI: reading a model's reasons without believing them"
---

# Explainable AI: reading a model's reasons without believing them

> **TSC #5 Generative AI Model Evaluation · Advanced · Knowledge K2**


> **Framework text (verbatim):** "Explainable AI (XAI) for understanding model decision-making."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Knowledge · Bullet 2 of 13

**One-line version:** An explanation is a second output from the same system, and it deserves the same suspicion as the first.

## What it is

Explainable AI is the set of methods that account for why a model produced the output it did — which parts of the input mattered, which features drove a score, what would have had to change for a different answer. In generative systems the explanation is usually more generated text, which is what makes the topic hard: the thing explaining has the same failure modes as the thing explained.

## Deep expansion

### The concept

Two questions hide under "explainability", and conflating them is the commonest error at this level. The first is *mechanistic*: what in the computation caused this output. The second is *communicative*: what does this stakeholder need in order to act correctly. A developer debugging a retrieval failure and a compliance officer signing off a credit-letter generator need different accounts of the same event, and neither needs the other's.

For a classifier the output space is small, so an explanation can be an attribution over input features. For a generative model the input is often a long prompt plus retrieved documents, and the "decision" is a sequence of token choices. Attribution across 4,000 tokens is not an explanation anyone can use, which is why generative XAI has drifted toward behaviour-level accounts: counterfactual probes, slice-level failure patterns, and rubric-grounded justifications a human can check.

The line to teach is **faithfulness versus plausibility**. A plausible explanation reads well and matches what a human would say. A faithful one reflects the computation. Language-model rationales are reliably plausible and only sometimes faithful — they are produced after the answer, by a system optimised for text that looks like reasoning.

### The sub-concepts

**Chain-of-thought as evidence, not transcript.** Current traces are useful signals and unreliable records: summarised, sometimes edited, often rationalised afterwards. Treat them as a hypothesis to test.

**Counterfactual explanation.** Change one attribute, hold everything else fixed, observe whether the output moves. The most defensible method for generative systems, because it is an experiment rather than a narrative.

**Attribution and saliency.** Highlighting influential tokens. Good for locating a problem fast; prone to instability, where near-identical inputs give very different attributions — itself a finding about robustness.

**Concept-based explanation.** Report behaviour in human concepts — seniority, location, product line — rather than tokens, so the stakeholder can read it.

**System explanation, not model explanation.** Often the honest account is "this reply drew on these three policy clauses and skipped the escalation check". That is a pipeline explanation, and it is more actionable than anything the model says about itself.

### How it connects to the rest of the framework

`05.03.A.K3` turns the counterfactual idea into a research direction; `05.03.A.K4` covers judged scoring, where the judge must state why, not only what. `05.02.I.K5` (fairness and explainability principles) is the Intermediate version. `TSC8` carries the obligation to explain to affected people — a legal requirement, not a design nicety — and `TSC7` supplies the mechanistic interpretability work.

### What is current as of November 2026

Reasoning models made traces a product feature: GPT-6.1 Sol and Terra, Claude 5.5 and Gemini 3.1 Pro all expose some form of reasoning summary, and each describes it as a summary. Explanations are now abundant and cheap, so the scarce skill has moved from generating one to testing one. The second shift is regulatory: assurance conversations now ask how a system reached an output, not just how accurate it is, and "the model said so" no longer survives a procurement review.

### Common misconceptions

- *"It explained its reasoning, so we can see how it thinks."* You can see what it wrote about its reasoning; the two are related, not identical.
- *"XAI means showing the user the prompt."* The prompt is an input. It says what was asked, not what was used.
- *"Attention was on the salary field, so salary drove the decision."* Attention is one signal, not a causal claim.
- *"Explanations are for regulators."* The highest-value use is internal: a probe that survives is how you find the bug before the auditor does.

## How a student should understand it

**Mental model:** the hawker explaining why his char kway teow is better. The explanation is composed after the cooking, usually sincere, sometimes the actual reason — and the wok does not know what he said.

**Three things they can do after this bullet:**
1. Tell a plausible explanation from a faithful one, and design a test that separates them.
2. Pick the artefact that matches a named stakeholder instead of defaulting to a chat transcript.
3. Run a counterfactual probe on a real output and report what changed.

**Misconceptions to kill:** that traces are transcripts, that attention implies causation, and that explanation is a compliance deliverable rather than a debugging tool.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The mamak shop receipt.** Ask the cashier why the bill is that amount and you get a fluent reconstruction — "two teh tarik, one roti" — which may be right, may be inferred from the total, and is delivered with equal confidence either way. Change one item and see whether the explanation tracks it. It breaks because a cashier can genuinely remember.

**The PSLE composition comment.** "Good structure, weak ending" is plausible. Mark the same essay twice, blind, and see whether the comment is stable. Unstable comments describe the marker, not the essay — the point about attribution methods.

### Worked example with a real tool

A team is shortlisting candidates with a summarisation assistant and wants to know whether the rationale is real. Paste this into Claude with three anonymised CV summaries:

```
Here are three candidate summaries and my ranking (1, 2, 3).

For each candidate, quote the three phrases from the summary you believe most
influenced the ranking. Then re-rank the same three with those phrases deleted and
everything else unchanged, and tell me: whether the order changed; which phrase was
doing the work; and one phrase I expected to matter that did not.

Work only from the text given. Do not restate the rationale in general terms.
```

What to point at afterwards: cases where deleting the quoted phrases does not move the ranking — that rationale was decoration. Where it moves wildly, the decision rested on a single phrase: a fairness problem, not just a robustness one.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the model to explain a decision, change one word, ask again, and project both answers.
2. **State the objective** — learners can run a counterfactual probe and judge whether an explanation is faithful enough to act on.
3. **Recall prior learning** — a rubric is a human explanation of a score, and it can be wrong in the same ways.
4. **Present the content** — mechanistic versus communicative, plausible versus faithful, the artefacts and their audiences.
5. **Guide** — run the shortlisting probe on the projector, thinking aloud about what counts as evidence.
6. **Elicit performance** — pairs design a one-attribute counterfactual on one of their own outputs.
7. **Give feedback** — debrief probes that changed nothing: a robust decision, or an explanation never connected to it?
8. **Transfer** — each learner writes the one-sentence explanation they would give an affected customer and checks the system supports it.

## What the framework doesn't mention but trainers need to know

- **Explanation is a design decision.** Where it appears, at what granularity, for whom. Treated as a model property, it becomes a debug panel nobody in the business can read.
- **Unstable explanations are your cheapest signal.** Two near-identical inputs giving different attributions is a robustness problem found for free. Look for it; do not average it away.
- **The audience sets the standard of proof.** An engineer needs reproducibility, an auditor a documented control, an affected person a reason they can contest. One artefact cannot serve all three.
- **Explanations create liability.** Once you tell a customer why, that account becomes the organisation's position. Be true at the level of the pipeline, not just fluent at the level of the sentence.

## Watch out

- **Do not present a reasoning trace as inner monologue.** It is a summary, sometimes a reconstruction. Overclaiming loses a technical audience immediately.
- **Do not demo attribution on a toy sentence and generalise.** Long prompts and retrieved context behave differently, and the demo will not survive the first real document.
- **Do not let XAI become a ritual.** A generated "explanation" attached to every decision, unread and untested, is worse than none: it manufactures assurance.
- **Do not ignore the human in the loop.** An explanation an operator cannot act on has failed, however faithful it is.
- **The stale claim to retire:** "explainability trades off against accuracy." For generative systems the binding constraints are faithfulness and usability — and a system you cannot diagnose is a system you cannot improve.
