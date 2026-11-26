---
id: 03.02.I.A7
tsc: 3
level: Intermediate
code: A7
title: Analyse bias and design mitigating prompts
as_at: 2026-11-26
review_by: 2027-02-25
---

# Analyse bias and design mitigating prompts

> **TSC #3 Prompt Engineering · Intermediate · Ability A7**

> **Framework text (verbatim):** "Analyse potential bias in foundation model responses and design prompts that mitigate the bias."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Ability · Bullet 13 of 13

**One-line version:** The model returns the average of everything it read; your prompt decides whether that average becomes a stereotype or a checked assumption.

## What it is

Analysing bias means finding where a model's response is skewed — a default assumption about a person, an omission from a list, a load of framing, a register that treats one variety of English as correct — and tracing it to its source. Designing mitigating prompts means writing instructions and structures that stop the obvious amplification, and being honest about the part that no prompt can fix.

## Deep expansion

### The concept

Bias in a foundation model has four sources, and they need different responses:

1. **Training data.** Historical text is skewed. What is written about nurses, CEOs, engineers and domestic workers reflects who wrote, about whom, and how often.
2. **Alignment.** Preference data encodes the tastes of the people and guidelines that shaped it: what counts as helpful, polite, balanced.
3. **Coverage.** Tokenisers and corpora represent languages and dialects unevenly, so quality is not equal across the languages a Singapore workplace actually uses.
4. **Your prompt.** Framing, examples, defaults and unstated assumptions — the only source you control completely.

A mitigating prompt cannot remove sources one to three. It can stop them being amplified, and it can make them visible enough for a human to correct. That distinction is the professional core of this bullet: claiming a prompt "removes bias" is both false and a governance risk.

### The sub-concepts

**Where bias shows up in output.** Defaults: the nurse is "she", the engineer "he", the CEO "he", the domestic worker "she". Omissions: a list of "leaders in the sector" with one demographic in it, or a policy summary with no mention of part-time staff because the source assumed full-time. Framing: loaded adjectives that pre-judge ("the aggressive negotiator", "the emotional complainant"). Register: a model that rewrites Singlish into standard English while calling it "correcting errors". Coverage: strong English, thinner Malay and Tamil, weakest on code-switched input.

**Detection methods that take a minute.**
- **Swap test.** Change the name or pronoun and re-run. If the answer changes in substance — suitability, tone, assumed competence — you have found a default.
- **Counterfactual ask.** "Give the same advice assuming the nurse is male." If the advice changes, the assumption was doing work.
- **Completeness audit.** Ask for a list, then ask what is missing from it. Compare against the population the list claims to describe.
- **Language test.** Ask the same question in two languages and compare specificity, hedging and terminology.
- **Repeat runs.** Bias shows as the modal answer, so one run is not evidence; three runs reveal the default.
- **Ask for the reason.** If the model asserts an attribute ("she is likely to prefer…"), ask why. The justification exposes whether it is evidence or prior.

**Mitigation inside the prompt.**
- **Neutral language rule with an example.** "Use gender-neutral phrasing: 'the nurse said they would check', not 'she would check'." A rule plus a demonstration beats "be unbiased", which specifies nothing.
- **Ask only for what the task needs.** "Do not state gender, age or ethnicity unless it changes the recommendation." Most bias enters as irrelevant detail.
- **Force structural coverage.** Columns per group, "one example from each segment", "include the exception as well as the rule". Structure prevents the silent omission.
- **Balance and diversify examples.** Few-shot sets teach distributions; five examples of one kind teach one kind.
- **Two-pass review.** Generate, then run a second call: "review this draft for stereotyped assumptions and list them before rewriting". It catches what the first pass produced.
- **Human review where consequences are real.** Hiring, credit, discipline, medical triage, public statements. A prompt is not a fairness control.
- **Keep the counter-case.** Ask for the strongest counter-example to any general claim; it is the cheapest de-biasing move available.

**Automation bias is the other half.** A formatted, confident answer is trusted more than a scruffy correct one. Mitigation is procedural: a named reviewer, a documented check, and a rule about which decisions may not be delegated.

**Your evaluation set is a bias too.** If every test case is a full-time professional with an English name, the prompt will look unbiased and fail the room.

### How it connects to the rest of the framework

`TSC1-Intermediate-K5` explains inherited bias in training data and preprocessing — the upstream cause this bullet deals with at the prompt. `TSC1-Intermediate-A3` is reading an output for what is wrong, which is the detection half. `TSC3-Intermediate-A6` covers misuse, including the decisions that should never be delegated, and `TSC3-Intermediate-K6` explains why diversity of output is not the same as fairness.

### What is current as of November 2026

Current frontier models are noticeably better than their predecessors at avoiding explicit stereotypes in English when asked directly. Four things remain true:

- **Defaults persist in the long tail.** Common occupations and famous roles are handled; the locally specific — a Singapore SME's operations manager, a part-time mature worker, a dialect-speaking customer — still gets defaulted.
- **Dialect is still treated as error.** Models will "correct" Singlish toward standard English unless told the register is intentional. For a trainer, that is a live example of bias as a quality judgement.
- **Generation drifts back.** Image and video models still default to narrow representations of professions and ages, and text models drift back toward the mean when prompts are vague — which is why the neutral rule must be in the prompt, not in the hope.
- **Over-correction is a failure mode too.** Aggressive balance instructions produce bland, hedged output that names every group and says nothing. Mitigation is not maximal caution.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The model is neutral because it is a machine."* It is an average of written history, with preferences layered on top.
- *"Bias means race and gender."* Also age, language, class, disability, occupation, family status, and the register a workplace treats as professional.
- *"One re-prompt fixes it."* A re-prompt fixes one output. The fix is a rule in the template plus a test in the eval set.
- *"If the output is balanced, it is fair."* Balance in tone can coexist with an unfair decision. Fairness is about the decision and who reviews it.

## How a student should understand it

**Mental model:** a mirror with a slight curve. It reflects the room, but it bends it — and once you know the curve, you can stand where the reflection is honest. You do not pretend the mirror is flat.

**Things they can do after this bullet:**
1. Run a swap or counterfactual test on a real output and describe the default it exposed.
2. Write a mitigating prompt with a neutral rule, an example, and a coverage constraint.
3. Separate what the prompt can fix from what needs a process or a human decision.

**Misconceptions to kill:** that the machine is neutral; that bias is only about protected characteristics; that a better prompt is a substitute for accountability.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The standard form with no field for it.** A leave form that only has a field for "annual leave" quietly tells every part-timer and every flexi-worker that they are an exception. Nobody wrote a discriminatory rule; the omission does the work. Prompts do this constantly — they ask for the typical case and the atypical one disappears.

**The curved mirror.** As above. Where it breaks: a mirror shows you the distortion immediately; a model's default looks like a fact, which is why the swap test exists.

### Worked example with a real tool

Start with the sentence every cohort recognises:

```text
Output: "The nurse told the patient she would check on him."
Re-prompt: "Rewrite this so the nurse's gender is not assumed. Use neutral phrasing
throughout, and do not change any other detail."
```

Then a harder one — a hiring-oriented prompt, where the bias is structural rather than pronominal:

```text
Draft a shortlist summary for these five candidates against the role requirements.

Rules:
- Assess only against the stated requirements. Do not comment on age, gender,
  nationality, family status or school prestige.
- Quote the evidence for each judgement from the CV. If evidence is missing for a
  requirement, write NO EVIDENCE — do not infer from the candidate's background.
- Note any requirement where none of the five candidates has evidence.

<candidates>{{CV_TEXTS}}</candidates>
```

What to point at afterwards: the first prompt fixes a pronoun; the second fixes a *decision*. Then run the swap test live — change one candidate's name and school and re-run; if the ranking moves while the evidence does not, the room has just watched bias happen and cannot argue with it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a "typical customer profile" the model generated, then reveal how narrow it is.
2. **State the objective** — by the end you can detect a default with a swap test and write a prompt that stops the obvious amplification.
3. **Recall prior learning** — what did they learn about inherited bias in training data?
4. **Present the content** — the four sources, the detection methods, the mitigation moves, the limits.
5. **Guide** — run the nurse and shortlist examples together, deciding what belongs in the prompt and what belongs in process.
6. **Elicit performance** — pairs write a mitigating prompt for a real decision in their work and run the swap test on it.
7. **Give feedback** — compare results; identify which mitigations changed the output and which only changed the wording.
8. **Transfer** — each learner adds a neutral-language rule and a "no evidence" rule to their team template.

## What the framework doesn't mention but trainers need to know

- **Bias mitigation has a credibility problem.** Overclaiming destroys trust with the sceptics in the room. Teach the limits before the techniques, and the techniques land better.
- **Local examples matter more than global ones.** A Singapore classroom's own defaults — language, accent, school, nationality, age — are the ones learners will recognise and act on.
- **The mitigation must be testable.** "Be fair" is not a rule. "Do not state gender unless relevant, quote evidence, write NO EVIDENCE when absent" is a rule someone can audit.
- **Fairness lives in the process.** Who reviews, who is accountable, what is logged, what may not be delegated — a prompt cannot carry those.
- **Watch the over-correction.** A model told repeatedly to avoid bias will produce hedged, useless prose. Say that out loud, or the room will conclude the whole topic is theatre.

## Watch out

- **Do not use anyone in the room as the example.** Use constructed cases; the point is the pattern, not the person.
- **Do not let the lesson become an ethics lecture.** Twenty minutes of theory and no swap test teaches nothing that survives the week.
- **Do not claim a prompt de-biases a model.** It mitigates amplification and surfaces the default; the weights are unchanged.
- **The stale claim to retire:** "the model has no feelings, so it has no bias." Bias is a property of the data and the decision, not of the model's intentions.
