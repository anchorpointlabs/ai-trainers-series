---
id: 09.02.I.A5
tsc: 9
level: Intermediate
code: A5
title: Conduct pre-deployment system testing
as_at: 2026-11-26
review_by: 2027-02-25
---

# Conduct pre-deployment system testing

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A5**

> **Framework text (verbatim):** "Conduct comprehensive pre-deployment system testing."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Ability · Bullet 9 of 10

**One-line version:** A comprehensive test is a plan with categories, repetition and a stated pass bar — and it is not finished until someone can read the results and decide.

## What it is

Conducting pre-deployment testing means designing and running a test programme across the whole system before launch: normal, edge, adversarial, integration and failure-mode cases, each with an expected outcome, repeated enough to see a pattern, recorded well enough to reproduce, and judged against an acceptance bar someone agreed to in advance.

## Deep expansion

### The concept

The tester's job is to produce a defensible answer to one question: "should this launch, and what would we be accepting if it did?" Everything in the plan serves that.

Three properties make a programme rather than an experiment. **Coverage**: every surface identified in the risk assessment has cases, including the ones nobody enjoys testing — retrieval filtering, tool arguments, rendered output, error paths. **Repetition**: because outputs vary, each case runs multiple times and the result is expressed as a pattern; a case that fails one time in five is a finding. **Falsifiability**: every case has a stated condition for pass, written before the run, so that the tester cannot rationalise the result afterwards.

The acceptance bar is a separate decision from the testing, and it belongs to the business. The tester supplies the numbers; someone accountable supplies the threshold. When those are confused, a bad result becomes an argument about interpretation rather than a decision.

### The sub-concepts

**The five categories.** Normal (does the main path work), edge (unusual but legitimate: mixed languages, long inputs, zero quantities, unusual names), adversarial (injection, jailbreak, leakage attempts, exfiltration attempts), integration (seams with retrieval, tools, auth, rendering, downstream systems), and failure modes (what happens when a dependency is down, a tool times out, a classifier errors — does it fail open or closed).

**Testing controls for their own failure mode.** The classifier is tested with paraphrases, encodings and multilingual variants, and also with legitimate traffic to measure false positives. The approval gate is tested with routine-looking actions. The sandbox is tested for egress, not for whether it runs code.

**Tool-call testing.** Not just "did the model choose the right tool" but "were the arguments validated", "was identity taken from the session", "was the call blocked when the context was tainted". Tool tests need a record of the proposed call, not only the final answer.

**Sampling and statistics, honestly.** Ten runs per case, at minimum, for anything probabilistic. Report counts, not adjectives. If a category is too large to test exhaustively, sample deliberately and say what was sampled.

**Automated suites.** Attack harnesses and prompt-evaluation frameworks can run hundreds of known cases in a pipeline. Their value is regression detection on every change; their limitation is that they test the attacks someone already published.

**Environment and version capture.** Model version, prompt version, corpus snapshot, tool configuration. A finding without these cannot be reproduced or fixed confidently.

**Cost and availability testing.** Token caps, iteration caps, rate limits, spend quotas — tested, not assumed. A public endpoint without them is a denial-of-wallet waiting for a bot.

**The report.** Coverage, results by category, failures with severity, residual risk, and a recommendation. One page for the decision-maker, an appendix for the engineer.

### How it connects to the rest of the framework

`TSC9-Basic-A3` is the individual contributor's version of this work. `TSC9-Intermediate-K1` supplies the control failure modes to test; `TSC9-Intermediate-A2` and `TSC9-Intermediate-A3` supply the controls themselves. `TSC9-Intermediate-A4` defines the surfaces that coverage must reach. `TSC9-Intermediate-A6` takes the test set forward into operation, replaying it on every change.

### What is current as of November 2026

Test tooling has become a pipeline component. Open attack suites and evaluation harnesses run against the late-2026 frontier — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — in minutes, and model providers expose evaluation endpoints that make A/B comparison routine.

- **Automation has moved the bottleneck to judgement.** The scarce resource is a person who can say what "pass" means for a policy question.
- **Version churn makes replay mandatory.** With models updating continuously, a launch without a replayed regression set is a launch on an untested build.

### Common misconceptions

- *"We ran the suite and it passed."* Which cases, how many runs, on which version, judged against which bar?
- *"Adversarial testing is the security team's part."* The security cases are a subset; the business cases are the ones that break trust.
- *"Integration testing is the vendor's problem."* The vendor tested a model, not your retrieval filter or your approval dialog.
- *"A failure found late means we delay indefinitely."* It means the decision is explicit: fix, contain, or accept in writing.

## How a student should understand it

**Mental model:** the inspection before a plane's first commercial flight — every system, every failure mode, a checklist signed by someone who can be asked about it later.

**Things they can do after this bullet:**
1. Write a test plan covering five categories with a pass condition per case.
2. Test a control for the failure mode it is known to have.
3. Produce a one-page report a decision-maker can act on.

**Misconceptions to kill:** that passing means working; that one run is a result; that the plan is complete without integration and failure-mode cases.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The vehicle inspection before COE renewal.** Brakes, lights, emissions, chassis — a fixed list, a stated standard, a certificate. Not a mechanic's opinion.

**The NDP rehearsal.** The parade is rehearsed in full, including the rain plan and the medical emergency, because the day itself gives no second chance. Failure-mode testing is the rain plan.

### Worked example with a real tool

Build the plan for an invoice-reading system, then check it for gaps:

```
Our system reads supplier invoices (PDF), extracts amount, supplier
and due date, and writes them into an accounting system.

Write one test case for each: normal, edge, adversarial, integration,
failure mode. For each, give the exact input, the expected behaviour,
the number of runs, and the pass condition. Then tell me which case
a team would most likely skip and what skipping it would cost.
```

What to point at afterwards: the skipped case is usually the integration one — the wrong amount written to the ledger because the extracted figure included GST. Adversarial cases get the attention; integration cases cause the incidents.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — describe a launch that passed every test and still paid a supplier twice, and ask which category was missing.
2. **State the objective** — by the end, they can write a five-category plan with pass conditions and a report.
3. **Recall prior learning** — UAT, inspection regimes, any checklist culture they know.
4. **Present the content** — coverage, repetition, falsifiability; the five categories; control failure modes; tool tests; the report.
5. **Guide** — build one case of each category for the invoice system.
6. **Elicit performance** — groups complete the plan and estimate run counts.
7. **Give feedback** — debrief: which pass conditions were written after seeing results.
8. **Transfer** — each learner converts one existing test into a case with a stated pass condition.

## What the framework doesn't mention but trainers need to know

- **Test the error paths.** What the system says when retrieval fails or a tool times out is part of the product, and it is usually untested.
- **Test with the corpus you will actually run.** A staging index of ten documents hides retrieval failures that appear at ten thousand.
- **Test the approval dialog, not just the action.** If the parameters are truncated on screen, the human is approving something they cannot see.
- **Keep the set after launch.** It is the asset that makes the next model change safe.

## Watch out

- **Do not sign off on coverage you cannot list.** "We tested broadly" is not a report.
- **Do not test against production data.** Use a staging copy with personal data removed.
- **Do not let a green dashboard stand in for judgement.** Automated suites report what they were told to look for.
- **Retire the stale claim:** "we tested the model, so we tested the system." In November 2026 the system is the pipeline around the model.
