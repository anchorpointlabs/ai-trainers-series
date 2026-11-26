---
id: 05.03.A.K1
tsc: 5
level: Advanced
code: K1
title: "A/B tests and user studies: how to prove a generative model actually got better"
as_at: 2026-11-26
review_by: 2027-02-25
---

# A/B tests and user studies: how to prove a generative model actually got better

> **TSC #5 Generative AI Model Evaluation · Advanced · Knowledge K1**


> **Framework text (verbatim):** "A/B testing and user studies for generative AI systems."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Knowledge · Bullet 1 of 13

**One-line version:** An offline score tells you which model wins on last month's questions; only a randomised test on real users tells you whether anyone is better off.

## What it is

An A/B test splits a live population at random between two versions of a system — different model, prompt, retrieval set or interface — and compares a pre-declared outcome across the groups. A user study watches people do real work with the system, usually in small numbers, with a task, a think-aloud protocol and a mix of observation and measurement. Together they answer what a benchmark cannot: not "which model scores higher on our file" but "which version produces better outcomes for the people who use it".

## Deep expansion

### The concept

The core difficulty is the counterfactual. To know whether model B helped a user, you need to know what that same user would have done with model A, at the same moment. You cannot observe it. Randomisation is the substitute: two groups that are statistically interchangeable, one of which gets the change. Everything else — sample size, randomisation unit, pre-registered metric — exists to stop that substitution being quietly broken.

Generative systems break the textbook version in three places. The outcome is usually a human judgement, so it must be defined before it is measured. Users learn, so after a week they prompt better and the improvement gets attributed to the model. And sessions spill into each other, which is why request-level randomisation is usually wrong: a user who saw model A on Monday carries that experience into model B on Tuesday.

### The sub-concepts

**Unit of randomisation.** Randomise where contamination happens — user, account, branch, case. Request-level splits are cheap and frequently invalid.

**Primary versus guardrail metrics.** Declare one success measure in advance, plus things that must not worsen: escalation rate, handle time, complaint volume, cost per interaction. Otherwise "helpfulness" rises while the support queue fills.

**Novelty and primacy effects.** A new interface gets attention for a fortnight. Run past the novelty curve or you measure curiosity.

**Power and minimum detectable effect.** Decide the smallest difference worth acting on, then size the test. For most SMEs the honest answer is that their traffic cannot resolve the effect they care about in a month — that is a finding, not a failure.

**Blinding.** Raters must not know which version produced an output. Strip names, shuffle order, randomise position: position and length both bias scoring.

**Study designs that fit generative work.** Task-based think-aloud sessions; two-week diary studies; Wizard-of-Oz runs where a human answers behind a fake interface to test demand before building; and paired comparison, where one user sees two outputs and picks, far more sensitive than absolute scoring.

### How it connects to the rest of the framework

`05.02.I.A1` (custom evaluation pipelines) builds the harness a study depends on — no versioned items and logged outputs, no test. `05.02.I.K6` is the same statistics applied to users rather than items. `05.03.A.A1` is the execution side of this bullet; this entry is why the design looks as it does. `TSC4` supplies the alternatives being tested, and `TSC8` supplies the consent and fairness constraints on using real people and real data.

### What is current as of November 2026

The pipeline is now two-stage: cheap model-based screening to find a plausible winner, then a human-anchored test to confirm it. Two consequences. The judge has become a design constraint — if it prefers long answers, the pre-screen selects for length and the live test "confirms" it. And the flagship models of late 2026 (OpenAI's GPT-6 line through 6.1 Sol and Terra, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and 4 Argon) are close enough on ordinary tasks that differences now show up in tail behaviour: the hard 5%, agentic multi-step runs, long documents. Aggregate satisfaction has stopped discriminating; slice-level results have not.

### Common misconceptions

- *"We sent the prompt to two models and compared."* That is a paired comparison of two outputs — useful triage, no users, no randomisation. It cannot tell you whether anyone's work improved.
- *"More users always makes the test better."* Sample size cannot rescue a contaminated unit or an undefined metric.
- *"It was significant, so we ship."* Significance says the difference is probably not noise. It says nothing about migration cost, latency or the new failure mode.
- *"A user study is a focus group."* A focus group collects opinions about a thing; a user study watches behaviour with it.

## How a student should understand it

**Mental model:** a blind taste test at a hawker centre. Two bowls from the same stall, labels hidden, and you count who finishes the bowl — not who says it is nicer.

**Three things they can do after this bullet:**
1. Choose the correct unit of randomisation and say what contamination it prevents.
2. Write a pre-registered decision rule — metric, guardrails, minimum effect, stopping point — before any data exists.
3. Design a five-person think-aloud study that produces findings a live test can confirm.

**Misconceptions to kill:** that comparing two outputs is an A/B test, that significance equals value, and that user studies are qualitative decoration.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The blind taste test.** Two bowls of laksa, same stall, labels hidden; the question is not "which is nicer" but "which do people finish and order again". It separates preference from consequence. It breaks because tasters learn and tire, and nobody can taste bowl A for the first time twice.

**Double-marking the PSLE oral.** Two markers, same script, neither knows the other's score. Divergence is information about the rubric, not the child — which is exactly what blinded disagreement means in an evaluation.

### Worked example with a real tool

Forty archived enquiries, two candidate prompts, three colleagues scoring blind. Paste this into Claude or ChatGPT:

```
I have 40 customer enquiries with two draft replies each (reply_A, reply_B). The
order of A and B was randomised by a spreadsheet formula, so you cannot tell which
prompt produced which.

Build me: (1) a scoring sheet with case_id, rater, coherence 1-5, factual accuracy
1-5, actionability 1-5, would_send_unedited Y/N, one-line note; (2) a rater
instruction page under 150 words that never mentions "model" or "AI"; (3) a
disagreement summary reporting mean score per label and every case where raters
differ by 2 or more points.

Do not infer which label is the new version.
```

What to point at afterwards: the instruction page and the disagreement list. Learners expect the value to be in the scores. It is in the rubric they had to write before seeing outputs, and in the cases where three colleagues genuinely disagreed — the real finding, and usually cheaper to fix than a model change.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two replies to one complaint, take a vote, then reveal the room split evenly and nobody asked what happened to the customer.
2. **State the objective** — each learner can design a blinded comparison with a pre-declared decision rule.
3. **Recall prior learning** — the Intermediate rubric and test set: an A/B test is a rubric plus randomisation plus real people.
4. **Present the content** — the counterfactual, unit of randomisation, primary versus guardrail metrics, novelty effects.
5. **Guide** — work the 40-enquiry example, writing the decision rule before any scores exist.
6. **Elicit performance** — pairs design a study for their own product: who is randomised, what is measured, what would stop it.
7. **Give feedback** — swap designs; the reviewer's only job is to find where the counterfactual breaks.
8. **Transfer** — each learner names one live decision a proper test could settle, and one it cannot.

## What the framework doesn't mention but trainers need to know

- **Consent comes first.** Real customer text is personal data: a PDPA conversation in Singapore, a documented basis in the EU. Advanced learners get asked to sign off, so they need to know when to stop.
- **Most SMEs cannot power a live test.** Teach the fallback ladder — blinded paired comparison, then a small think-aloud study, then a live split when volume allows.
- **Instrumentation is the bottleneck.** Without outputs and outcomes logged with a version identifier, the study is impossible later — and that is decided long before evaluation starts.
- **Report the null.** A well-run test finding no difference is the most valuable output an evaluation team produces, and the one most likely to be buried.

## Watch out

- **Do not test on live customers without the approval chain.** Model changes can alter what people are told about money, health or eligibility. That needs sign-off and a rollback plan.
- **Do not let the judge and the contestant be the same model.** Self-preference will make your pre-screen agree with your conclusion.
- **Do not demo significance from twenty cases.** It teaches the room that statistics is decoration. Show the interval and say the sample is too small.
- **Do not report a satisfaction score as the outcome.** Ask what the user did next: sent it, escalated it, rewrote it, abandoned it.
- **The stale claim to retire:** "we will A/B test it after launch." The test set, the logging and the decision rule must exist before launch, or there is nothing to test with.
