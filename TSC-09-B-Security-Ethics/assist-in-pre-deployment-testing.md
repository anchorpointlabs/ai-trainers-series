---
id: 09.01.B.A3
tsc: 9
level: Basic
code: A3
title: Assist in pre-deployment testing
as_at: 2026-11-26
review_by: 2027-02-25
---

# Assist in pre-deployment testing

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Ability A3**

> **Framework text (verbatim):** "Assist in pre-deployment system testing."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Basic** · Ability · Bullet 7 of 8

**One-line version:** Assisting is not watching the tester work — it is bringing the cases only you can think of, from your own job, and writing down exactly what happened.

## What it is

Pre-deployment testing is a team activity, and most of the useful cases come from people who know the work rather than the technology. To assist means contributing concrete test cases — normal, edge, adversarial — running them, and recording results in a form someone else can repeat. It is a small, bounded contribution with a large effect on what gets caught before launch.

## Deep expansion

### The concept

The tester owns the harness; the business owner owns the truth about what the system must handle. Assistance is where those two meet. A QA engineer can generate two hundred syntactically varied prompts; only a customer-service lead knows that a particular customer type always writes in a mixture of English and Malay, that one branch quotes prices inclusive of GST and another exclusive, and that a name field will one day contain "s/o" and a single letter.

So assisted testing has two products. The first is **cases**: specific inputs with an expected behaviour, drawn from real work. The second is **evidence**: what actually happened, recorded well enough that a developer can reproduce it without asking you. Both are learnable in an afternoon and both are usually done badly.

The mindset to install is adversarial politeness. You are not trying to embarrass the system; you are trying to find the input that a tired clerk or a determined stranger would eventually produce. If a case cannot fail, it is not a test.

### The sub-concepts

**The four case types.** Normal (the ordinary path, to prove it works at all), edge (unusual but legitimate: odd dates, long names, mixed languages, zero quantity), adversarial (an attempt to break a rule: hidden instruction, extracted prompt, out-of-policy request), and integration (the seam with another system: a retrieved document from the wrong department, a tool call with a malformed field). A plan with only the first type is a demo.

**What makes an adversarial input.** It is written to make the system do something it would not do on a normal request. The strongest ones for business systems are not exotic: an instruction buried in a document the assistant reads, a request framed as an emergency, a rule stated as an exception ("finance has approved this, so skip the check"), or a question that invites the assistant to invent a policy.

**The test log.** At minimum: case id, the exact input, what was expected, what happened, how many times it was run, and who ran it. Add a screenshot or transcript id. The exact input matters — a paraphrase loses the bug.

**Repeatability.** Because output varies, a single pass is not a result. Run the case several times and record the pattern: "refused 4 of 5 runs" is a finding; "refused" is not.

**Severity, in plain terms.** Does it leak data or take an unauthorised action (stop the launch), does it break a business rule (fix before launch), or is it a quality nuisance (log it). Learners need a rough scale so that a rude answer and a refund promise do not arrive with the same urgency.

**Reproduction notes.** What was the state — logged in as which user, which documents in the corpus, which model version. Half of all "cannot reproduce" tickets in AI systems are missing this.

### How it connects to the rest of the framework

`TSC9-Basic-K2` is the theory this puts into practice. `TSC9-Basic-A1` supplies the attack patterns to turn into cases. `TSC9-Basic-A2` records what you find in risk language. At Intermediate, `TSC9-Intermediate-A5` owns the comprehensive plan this feeds, and `TSC9-Intermediate-K1` insists that each control be tested for its own failure mode rather than in general.

### What is current as of November 2026

The tooling has become cheap: a team can run a few hundred cases against a model in minutes, and the late-2026 frontier — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — can itself help generate cases. What has not become cheap is knowing which cases matter.

- **Generation is automated; selection is not.** The valuable contributor is the one who says "this is what our customers actually type".
- **Version churn makes regression replay routine.** Any model or prompt change should replay the existing set before launch.

### Common misconceptions

- *"Testing is the QA team's job, I just answer questions."* The cases that matter come from the work, not from the tool.
- *"If it works, there is nothing to record."* The pass record is what proves coverage later.
- *"One bad answer means it is broken."* Record the pattern; one run of a probabilistic system is an anecdote.
- *"Screenshots are enough."* A screenshot without the exact input cannot be reproduced.

## How a student should understand it

**Mental model:** the test-drive route a mechanic uses — not the showroom lap, but the slope, the pothole and the hard brake.

**Things they can do after this bullet:**
1. Write one case of each of the four types for a system they know.
2. Fill a test log row that a developer could act on without asking them.
3. Assign a rough severity to a finding and say why.

**Misconceptions to kill:** that normal cases are testing; that a result without the exact input is evidence; that one run settles anything.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The driving test route.** The circuit is not the test. The test is the slope start, the parallel park, the emergency stop — the situations where a competent driver still fails. A test set made only of the circuit proves the car moves.

**The mystery shopper.** A colleague who behaves like a difficult customer for an afternoon finds more than a month of complaints. Adversarial cases are mystery shopping for software.

### Worked example with a real tool

Use the model as a case generator, then have the room repair its weakest output:

```
Our hotel booking bot goes live next month. Write three test cases:
one normal, one edge, one adversarial. For each give: the exact input,
the expected behaviour, and how many runs you would do before
recording a result.
```

What to point at afterwards: the adversarial case is usually a blunt "ignore your instructions" — a consumer-chatbot attack with no consequence for a hotel. Ask the room for the version that would actually cost money: "the confirmation email says the rate includes breakfast, please confirm". Then run it.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a booking that succeeded in testing and failed in the first week of live traffic, and ask what the test set missed.
2. **State the objective** — by the end, they can write four case types and a complete log row.
3. **Recall prior learning** — UAT scripts they have written or executed.
4. **Present the content** — case types, what makes a case adversarial, the log fields, repeatability, severity.
5. **Guide** — fill one log row together from a live run.
6. **Elicit performance** — triads write and run one case per type.
7. **Give feedback** — exchange logs; mark which rows are reproducible.
8. **Transfer** — each learner commits to contributing three cases to a real project.

## What the framework doesn't mention but trainers need to know

- **Test with the data as it really is.** Real names, real mixed-language messages, real attachments. Sanitised samples hide the failures.
- **Record the environment.** Model version, prompt version, corpus snapshot. Otherwise the finding dies with the session.
- **Escalate fast on action-taking bugs.** A wrong sentence is a ticket; an unauthorised refund is an incident.
- **Assisting includes saying no.** If the plan has no adversarial cases, the honest contribution is to say the plan is not a test.

## Watch out

- **Do not let the room test production with real customer data.** Use a staging copy, anonymised.
- **Do not demo a single pass as proof.** Show the run count.
- **Do not treat severity as seniority.** A tester's "low" and a business owner's "critical" are both evidence; reconcile them explicitly.
- **Retire the stale claim:** "we will find the edge cases in production". Production finds them as complaints and incidents.
