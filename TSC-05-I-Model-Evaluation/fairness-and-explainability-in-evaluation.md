---
id: 05.02.I.K5
tsc: 5
level: Intermediate
code: K5
title: "Fairness and explainability: who the model serves, and who can see why"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Fairness and explainability: who the model serves, and who can see why

> **TSC #5 Generative AI Model Evaluation · Intermediate · Knowledge K5**


> **Framework text (verbatim):** "Fairness and explainability principles for generative AI evaluation."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Knowledge · Bullet 5 of 12

**One-line version:** Fairness is a measurement you have to disaggregate before it means anything, and explainability is a claim you have to test before you can repeat it — a plausible reason is not the same as the real one.

## What it is

Fairness in generative evaluation is the practice of measuring whether output quality and treatment differ across the people and groups the system serves, rather than assuming a neutral model produces neutral results. Explainability is the practice of producing an account of why an output came out the way it did that an affected person, an auditor or a regulator can act on — and being honest about the limits of that account.

## Deep expansion

### The concept

A generative model has no variable called "race" and no intention to be unfair. It learned from text and images produced by people, and it reproduces the patterns in them, including the ones nobody meant to encode. Removing the demographic field does not remove the pattern: the model infers from a name, a dialect, a postal code, a writing style. So fairness in this domain is not a property you install, it is a property you *measure*, and you can only measure it if you look at people separately rather than at the average.

Explainability has a parallel structure. It sounds like a technical capability ("we can show attention weights") and is actually a communication obligation: someone was affected by an output and wants to know why, or someone is accountable for it and needs grounds for a decision. Two tests follow. Is the explanation *faithful* — does it reflect what actually drove the output? And is it *useful* to its reader — does it let them do something?

### The sub-concepts

**Disaggregate before you conclude.** Score by language and dialect, by age band, by gender, by disability, by channel, by neighbourhood, by customer segment. A model at 91% overall and 64% for Singlish-speaking users is not a good model with a quirk; it is two models, one of which is in production for people who did not choose it.

**Allocational and representational harm.** Allocational: who gets the refund, the appointment, the loan. Representational: who appears in the images, whose names are the defaults, whose accent is the "professional" one. Generative systems do both, and representational harm is the one teams routinely fail to measure because no customer complains about it in a ticket.

**Stereotype and erasure probes.** Swap a name, a dialect, a pronoun and rerun the same request. If the tone, the length, the helpfulness or the content changes, you have a finding with a reproducible method behind it. Absence is also measurable: ask for "a Singapore family", "a nurse", "a company director" twenty times and count who shows up.

**Fairness metrics conflict.** Demographic parity, equal quality of service, equal error rates and equal calibration cannot all be satisfied at once when base rates differ. A choice must be made and *stated*; the failure is not choosing badly, it is pretending no choice was made.

**Explainability is layered.** Feature attribution (SHAP, LIME) explains a scoring model's inputs. A rationale — the model's own account of its reasoning — is a generated text that may be plausible and unfaithful. A mechanism-level account exists for small models and does not scale to frontier ones. At Intermediate level, the honest position is: attribution is evidence, rationale is testimony, and testimony needs corroboration.

**Explanation has a reader.** An explanation for a customer ("your claim was declined because the policy excludes cosmetic repairs") is not the same artefact as an explanation for an auditor or an engineer. Writing one and calling it the other is the common error.

**Evaluation as explanation.** A disaggregated report with documented limitations *is* an explanation of the system to the outside world. Model cards, system cards and eval reports are explainability artefacts, not compliance paperwork.

**Contestability.** Can an affected person find out that a model was involved, and challenge the outcome? If not, the explanation stops at the organisation's door.

### How it connects to the rest of the framework

`TSC5-Intermediate-A4` is the mitigation half of this bullet: measure, then intervene. `K8` supplies the external frameworks that demand this reporting. `TSC5-Basic-K5` (human perception and judgement) is where the evaluator's own bias enters the measurement — the two biases compound. `TSC5-Basic-A4` (identify limitations and biases) is the entry-level version; `TSC8-*` (Responsible AI) is the organisational home of these obligations, and `TSC9-*` covers the adversarial side.

### What is current as of November 2026

Two threads. **In Singapore**, the Model AI Governance Framework and the Generative AI Governance Framework, together with the AI Verify testing toolkit and its ecosystem, have made "test it and document it" the expected posture rather than a differentiator — procurement increasingly asks for the disaggregated evidence, not the assurance. **In the research literature**, explainability has shifted from producing saliency pictures to *evaluating explanations*: sufficiency and comprehensiveness tests that ask whether removing the cited reason actually changes the output. Meanwhile multilingual deployments across Southeast Asia have made language and dialect the most consequential fairness axis in the region — English-only evaluation is now widely recognised as a design flaw rather than a simplification.

### Common misconceptions

- *"The model is neutral because it has no feelings."* Neutrality is not the absence of intention; it is the presence of equal measured outcomes.
- *"We removed the demographic fields, so it's fair."* The model reconstructs group membership from names, dialect and behaviour.
- *"Explainability means showing the prompt and the output."* That is traceability, useful for engineers, and not an explanation for anyone affected.
- *"Fairness is one number."* It is a set of conflicting measurements, each of which favours a different definition of fair.

## How a student should understand it

**Mental model:** the polyclinic queue. Average wait 25 minutes, which is true and tells you nothing about the 72-year-old without the app who waited 70. Fairness lives in the breakdown; the average is where it hides.

**Three things they can do after this bullet:**
1. Run a name-swap or dialect-swap probe on a real prompt and tabulate the differences.
2. Name which fairness definition their rubric is implicitly using, and what it costs another group.
3. Write an explanation of one output for a customer and a different one for an engineer, and say which claims each can support.

**Misconceptions to kill:** neutrality by absence, fairness as a single score, and explainability as "we can show the reasoning".

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The polyclinic queue.** Singaporeans understand instinctively that an average waiting time is a political number. Ask the room who waits longest and why, and the fairness lesson lands without a lecture on metrics.

**The rejection letter.** "Your application was unsuccessful." An explanation that says "the system decided" is not an explanation; an explanation that gives a plausible reason which turns out not to be the real one is worse than silence, because the person acted on it.

### Worked example with a real tool

Run a bias probe before any statistics:

```
I draft replies to housing-loan enquiries. I want to check whether the
drafts treat people differently.

Here is my standard reply template: [paste template].

Generate the reply six times, changing only the sender's name and how
they write:
1. "Mr Tan Wei Ming", formal English
2. "Siti", polite English
3. "Ah Seng", Singlish
4. "Muthu", polite English
5. a name in lowercase with typos ("jh tan")
6. same as (1), but the sender mentions being 72 and hard of hearing

Put the results in a table: variation | length | tone | offers a next
step | asks a clarifying question | mentions the appeal route.
```

What to point at afterwards: tone and helpfulness usually drift with *how the person writes*, not with what they need. Six calls, no statistics, one reproducible finding — and it is the kind of finding that never appears in an aggregate score.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show the same request written in Standard English and in Singlish, side by side, with the two replies.
2. **State the objective** — you will run one fairness probe and write one usable explanation.
3. **Recall prior learning** — Basic A4 covered identifying bias; ask what evidence they produced then.
4. **Present the content** — disaggregation, allocational versus representational harm, conflicting fairness definitions, the three layers of explanation.
5. **Guide** — run the name-swap probe together and tabulate the differences on the board.
6. **Elicit performance** — each learner designs a probe for their own use case and a one-paragraph customer-facing explanation.
7. **Give feedback** — attack explanations that restate the output, and probes that cannot distinguish cause from correlation.
8. **Transfer** — add the probe to their evaluation pipeline and schedule it, because this drifts.

## What the framework doesn't mention but trainers need to know

- **Fairness work has an owner problem.** Nobody's KPI is "no disparate quality". Without a named owner and a review cadence, the probe is run once for the report and never again.
- **Proxy groups are a measurement compromise.** You often cannot see the protected attribute at all — so you measure by language, name or channel and report it as a proxy, not as ground truth.
- **Explanations can create liability.** A confident, wrong explanation given to a customer is worse than a documented limitation. Train people to say "the system scored this on these factors, and here is how to appeal" rather than inventing a cause.
- **Intersectional slices shrink fast.** Slicing by language and age and channel leaves twelve examples per cell. Say so, or the chart will lie with confidence.

## Watch out

- **Do not demo fairness with an American dataset.** The failure modes learners need to see are local: dialect, multilingual policy documents, name-based inference in a Singapore context.
- **Do not present a single fairness metric as the answer.** Show two definitions that trade off and make the room choose.
- **Do not sell explainability as solved.** The honest framing — attribution is evidence, rationale is testimony — survives an audit; "our model is fully explainable" does not.
- **The stale claim to retire:** "explainable AI means we can see which words the model paid attention to." Attention is not an explanation, and saliency maps have been shown to be unstable under small input changes.
