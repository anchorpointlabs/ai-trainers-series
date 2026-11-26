---
id: 07.02.I.K6
tsc: 7
level: Intermediate
code: K6
title: Explainability for generative models: what you can actually show
---

# Explainability for generative models: what you can actually show

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K6**


> **Framework text (verbatim):** "Model interpretability and explainability methods for generative models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 6 of 17

**One-line version:** An explanation is only worth anything if changing the thing it names changes the output — everything else is a plausible story.

## What it is

Interpretability is the set of methods for saying why a model produced a particular output. For generative models that question is too broad to answer directly, so the work is narrowing it: why this token, why this region of the image, why this refusal, why not the alternative. The methods split into input attribution, internal inspection, behavioural testing and by-design auditability — and they have very different evidential weight.

## Deep expansion

### The concept

Prediction models could be explained with feature importances because the output was one number. A generative model outputs a whole artefact, so "explanation" must be defined before it can be measured. The standard that matters is *faithfulness*: does the explanation actually track the computation, or does it merely look convincing? Gradient saliency looks convincing and is often unfaithful. A counterfactual test is dull and usually faithful. Learners arrive expecting a dashboard; what they need is a small set of tests they can defend.

### The sub-concepts

**Input attribution.** Saliency maps, integrated gradients and Shapley-style methods assign credit to input features. For images they are weak but inspectable; for text they are close to useless at token level, because removing one token changes the prompt entirely. They also saturate: a confident model produces flat, uninformative gradients.

**Internal inspection.** Probing classifiers test whether a concept is linearly recoverable from activations; the *logit lens* reads intermediate predictions; *activation patching* swaps a component between runs to see what changes. Sparse autoencoders decompose activations into sparser, more nameable features, which has made feature-level claims far more credible than they were — while the underlying problem of superposition, many concepts sharing one direction, remains.

**Behavioural and counterfactual testing.** Change one property of the input and check the output changes in the expected direction: swap the customer's name, change the currency, add an instruction to be terse. This is the cheapest, most defensible evidence available to a practitioner, and it doubles as a regression test.

**By-design auditability.** Constrain what the system can emit (schemas, allowed tools), require citations, log refusals and guardrail hits, and publish a system card. Most real audit requests are satisfied here rather than by any interpretability technique.

### How it connects to the rest of the framework

`TSC7-Intermediate-K1` introduces explainability as a concept; `TSC7-Intermediate-K7` uses the same machinery to test for bias; `TSC8` is the responsible-AI frame these methods serve; `TSC9` needs them when investigating prompt injection and data leakage; `TSC5` treats documented evaluation as the practical substitute for explanation.

### What is current as of November 2026

- **Chain-of-thought is no longer accepted as an explanation.** It is generated text that may be post-hoc rationalisation; reasoning-capable models from the GPT-6 generation, Claude 5.5 and Gemini 4 Argon produce traces that are useful for debugging and unsafe as evidence of cause.
- **Feature-level interpretability matured.** Sparse-autoencoder work moved from papers to tooling, giving teams a way to name behaviours rather than point at heatmaps.
- **Documentation became the compliance product.** Model cards, system cards and governance testing frameworks such as AI Verify now carry more audit weight than any visualisation.

### Common misconceptions

- *"The chain of thought shows how it reasoned."* It shows text that resembles reasoning, produced by the same next-token process as the answer.
- *"Attention weights tell you what mattered."* They tell you where the model looked, in one layer, in one head, in one forward pass.
- *"If you can't explain it, you can't ship it."* Plenty ships with documented evaluation, known failure modes and human review instead.
- *"Explainability is a regulator's problem."* It is a debugging tool first; most of its value is found by engineers, not auditors.

## How a student should understand it

**Mental model:** the kopitiam uncle's secret recipe. Ask him why the laksa is good and you get a warm, coherent story about prawn heads and patience. Send the bowl to a lab and you get the actual composition. Both are useful; only one settles a dispute.

**Three things they can do after this bullet:**
1. Reframe "explain the model" into a specific, testable question.
2. Run a counterfactual test suite and report what changed and what didn't.
3. Distinguish, in writing, between an explanation and a justification.

**Misconceptions to kill:** that chain-of-thought is reasoning, that heatmaps are evidence, and that explainability is only for compliance.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The secret recipe.** The uncle's account of his laksa is a post-hoc story: it may be true, it may be flattering, and it is shaped by what he thinks you want to hear. The lab test can't tell you it tastes good, but it can tell you what is in the bowl. Chain-of-thought is the story; counterfactual testing is the lab. Where it breaks: the uncle can be asked again tomorrow and tell a different story; a model's explanation is regenerated on demand and will do the same, which is why the lab matters.

**The food hygiene inspector.** The inspector does not ask the stallholder to explain his cooking. She checks refrigeration logs and observes practice. By-design auditability is that checklist — boring, boring, and the thing that actually protects you. Where it breaks: a checklist can pass while the food is bad, so never let documentation replace evaluation.

### Worked example with a real tool

A learner wants to know whether their support model actually uses the customer's order status. Type this into Claude or a coding assistant:

```
I have a support model behind an API. Write a counterfactual
test harness (Python, pytest) that, for 50 saved tickets:

1. Calls the model with the original ticket and records the reply.
2. Re-runs each ticket with exactly one change: order status
   flipped, customer name replaced with a fake, currency changed,
   and the refund amount removed.
3. Diffs the replies (embedding distance plus an LLM judge that
   labels each pair: uses-the-fact / ignores-it / contradicts-it).
4. Prints a per-attribute table and saves pairs where the output
   did not change, for manual reading.
```

Point at step 2 (one change at a time — two changes and you learn nothing), the "did not change" bucket (a model ignoring the order status is the finding that matters), and the requirement that the judge label be checked by a human on a sample, because the judge is a model too.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a confident wrong answer plus its plausible chain-of-thought.
2. **State the objective** — turn "explain it" into a test you can run.
3. **Recall prior learning** — the explainability concept from K1.
4. **Present the content** — attribution, inspection, counterfactuals, by-design.
5. **Guide** — run one counterfactual live and read the diff together.
6. **Elicit performance** — pairs design three counterfactual tests for a use case.
7. **Give feedback** — critique for faithfulness: would the test catch a real failure?
8. **Transfer** — each learner picks one behaviour worth logging in production.

## What the framework doesn't mention but trainers need to know

- **Explanations can increase over-trust.** Users shown a rationale accept wrong answers more readily; the interface around an explanation matters as much as the explanation.
- **Faithfulness testing is not standard practice.** Most teams ship attributions without ever perturbing the input to check they move.
- **Tooling is fragmented.** Interpretability libraries lag behind new architectures, so the method that works on your model may be the one you write yourself.
- **Documentation has to be maintained.** A system card describing last quarter's model is a liability, not a control.

## Watch out

- **Do not demo attention heatmaps as explanation.** They are the most over-claimed artefact in this field and the correction costs you credibility.
- **Do not let chain-of-thought into an audit pack unlabelled.** Say "generated rationale, not verified reasoning".
- **Do not teach interpretability as compliance theatre.** The value is debugging; frame it that way and the room stays honest.
- **The stale claim to retire:** "we can't explain generative models, so we can't govern them." In November 2026 governance runs on evaluation, documentation and behavioural tests — all available now.
