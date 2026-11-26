---
id: 07.03.A.K11
tsc: 7
level: Advanced
code: K11
title: Alignment by preference: how RLHF and RLAIF actually change a model
as_at: 2026-11-26
review_by: 2027-02-25
---

# Alignment by preference: how RLHF and RLAIF actually change a model

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K11**


> **Framework text (verbatim):** "Fine-tuning models to align with human preferences using reinforcement learning (e.g., Reinforcement Learning from Human Feedback (RLHF), Reinforcement Learning from AI Feedback (RLAIF))."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 11 of 20

**One-line version:** Preference tuning teaches a model which of two answers people prefer — which is a narrow, gameable signal, and the entire craft is keeping the optimisation from exploiting it.

## What it is

Preference-based alignment is the final training stage in most frontier pipelines. Humans (or a capable model, in RLAIF) rank pairs of responses; those rankings train a reward model or directly update the policy, so the model becomes more helpful, more careful and more in line with a written set of principles. It changes behaviour, not knowledge.

## Deep expansion

### The concept

The classical pipeline has three stages. **Supervised fine-tuning** teaches the response format from demonstrations. **Reward modelling** fits a scorer to pairwise preferences — "for this prompt, A is better than B" — under an assumption that preference is a smooth function of quality. **Reinforcement learning** then optimises the policy against that scorer, with a penalty keeping it close to the reference model so it does not drift into nonsense that happens to score well.

The critical insight is that the reward model is a *proxy*, and optimisation is very good at finding the proxy's weaknesses rather than the thing it was meant to represent. This is Goodhart's law with a gradient: as you push, you get longer answers, more confident tone, more flattery, more bullet points — whatever the annotators rewarded incidentally — until the proxy and the real goal diverge.

**DPO** (direct preference optimisation) skips the explicit reward model and trains directly on preference pairs with a closed-form objective. It is cheaper and more stable, and it is now the common starting point; the same over-optimisation risk remains, just expressed differently.

**RLAIF** replaces human annotators with a model applying written principles — a constitution — which scales cheaply and consistently but imports that model's blind spots and its interpretation of the principles.

### The sub-concepts

**Preference data quality.** Guidelines, annotator training, agreement measurement and adjudication matter more than the algorithm. A reward model trained on inconsistent labels learns the inconsistency.

**KL control.** The penalty against the reference model is the brake. Too little and the model degenerates into reward-hacking text; too much and nothing changes. It is a dial that must be tuned per dataset, not a constant.

**Known biases.** Length bias (longer looks better), sycophancy (agreement looks helpful), and style bias (confident tone reads as correct). Each has to be countered in the guidelines, the data or the objective.

**Evaluation of alignment.** Preference win-rates against a baseline, plus a capability regression suite, plus targeted probes for the behaviours the policy was meant to fix. A model can win every preference comparison and get worse at arithmetic.

### How it connects to the rest of the framework

`TSC7-Advanced-K10` is the rung below on the ladder — supervised and continued pre-training supply the base this stage shapes. `TSC8-Intermediate-K6` covers the governance and policy side; `TSC9-Basic-K4` covers the safety failure modes preference tuning is meant to reduce. `TSC5-Intermediate-K8` is the ethics framework the constitution should reflect.

### What is current as of November 2026

Preference tuning has become routine rather than exotic: open tooling for DPO-style training and for RLAIF with rubric-based judges means small teams now run alignment passes on domain data. The frontier labs' late-2026 releases — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and 4 Argon — describe their differences largely in terms of behaviour under long, tool-using tasks, which is the fingerprint of preference and rubric tuning rather than raw capability. The live argument is how much of the annotator's job can be given to a judge model without laundering that model's preferences into the product.

### Common misconceptions

- *"RLHF makes the model truthful."* It makes it preferred on the prompts and guidelines used. Truth is not directly observable, so it is only indirectly rewarded.
- *"Alignment adds knowledge."* It reshapes behaviour on knowledge the model already has.
- *"RLAIF is objective because it is automated."* It is consistent, not objective; the judge's biases become the policy's biases.
- *"Higher reward means a better model."* Higher reward is the definition of over-optimisation once you pass the point where the proxy holds.

## How a student should understand it

**Mental model:** a restaurant training its staff on mystery-shopper scores. Push the staff hard enough on the score and you get free desserts and long goodbyes — not better food.

**Three things they can do after this bullet:**
1. Explain the SFT → reward model → RL chain and where DPO fits.
2. Name three preference biases and how each is countered.
3. Design an evaluation that would catch capability regression after alignment tuning.

**Misconceptions to kill:** that alignment equals truthfulness, that AI feedback is neutral, and that a rising reward is progress.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The mystery shopper.** Staff optimise what the shopper measures. If the checklist rewards greeting speed, you get fast greetings and slower service. Where it breaks: a shopper visits occasionally, whereas a reward model scores every single token.

**The PSLE tuition arms race.** Everyone optimises the same signal, the signal stops discriminating, and the underlying skill is unchanged. Preference tuning is the arms race at gradient speed.

### Worked example with a real tool

Have the class design preferences rather than consume them:

```
We are building a customer-service assistant for a telco.
We want it helpful, but it must not promise refunds it cannot
authorise, and it must not be sycophantic.

1. Write four preference guidelines an annotator could apply
   consistently, including how to handle a confident-sounding
   answer that is wrong.
2. Design ten prompt pairs where the "nicer" answer is worse.
3. What would you measure to prove the model did not get more
   sycophantic? Give the exact comparison.
4. How would you detect that our reward model learned to prefer
   long answers?
```

What to point at afterwards: question 4 is answered by checking reward against length correlation on a held-out set. Most classes have never considered that the scorer itself has a diagnosable bias — which is the whole point of the exercise.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two responses, one flattering and wrong, one blunt and right; ask which a preference model would pick.
2. **State the objective** — design preference guidelines and a regression check.
3. **Recall prior learning** — the fine-tuning ladder from `TSC7-Advanced-K10`.
4. **Present the content** — the three-stage pipeline, DPO, RLAIF, KL, biases.
5. **Guide** — write two guidelines together and test them on real pairs.
6. **Elicit performance** — teams write four guidelines plus probes.
7. **Give feedback** — swap guidelines and find the ambiguity.
8. **Transfer** — each learner names the behaviour their organisation would most need to shape, and how they would measure it.

## What the framework doesn't mention but trainers need to know

- **Annotator selection is a values decision.** Who labels determines what the model prefers; that is a governance question disguised as logistics.
- **Sycophancy is the default failure in commercial settings.** It maximises satisfaction scores and destroys advice quality.
- **Keep the capability suite separate from the preference suite.** They measure different things and are often anti-correlated.
- **Document the constitution.** If principles shaped the behaviour, the principles are part of the product specification.

## Watch out

- **Do not present RLHF as "making AI safe".** It reduces specific behaviours on specific prompts; it does not guarantee safety.
- **Do not skip the length-bias discussion.** It is the most reliably reproducible artefact and the easiest to demo.
- **Do not run a live RLHF demo.** Training time and instability make it a poor classroom spectacle; show curves and pipelines instead.
- **The stale claim to retire:** "alignment solves hallucination." In 2026 preference tuning changes tone and refusal behaviour; grounding and evaluation are what reduce unsupported claims.
