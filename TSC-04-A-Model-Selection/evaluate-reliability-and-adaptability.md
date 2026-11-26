---
id: 04.03.A.A3
tsc: 4
level: Advanced
code: A3
title: Evaluate reliability and adaptability
as_at: 2026-11-26
review_by: 2027-02-25
---

# Evaluate reliability and adaptability

> **TSC #4 Generative AI Model Selection · Advanced · Ability A3**

> **Framework text (verbatim):** "Evaluate the reliability and adaptability of advanced generative models for real-world applications."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Ability · Bullet 7 of 8

**One-line version:** Reliability is doing the same thing right next Tuesday; adaptability is doing the new thing right when Tuesday brings something you have never seen.

## What it is

Two independent axes, often confused because a good demo scores well on neither. **Reliability** is consistency of correct behaviour over time and across repeats: same input, same quality; week one and week twelve. **Adaptability** is graceful performance on inputs outside the training distribution — new products, new policies, new phrasing, new languages — without silently degrading or confidently guessing.

## Deep expansion

### The concept

A single impressive demo is evidence of one thing: that one output was good. Real-world applications need a distribution of outputs to be good, repeatedly, under conditions that change. That requires measuring *variance* and measuring *drift*, and both require time.

Reliability has a tail problem. Users remember the worst output, not the average one. A model averaging four-point-two out of five while producing an outright wrong answer in three per cent of cases is worse for a customer-facing system than a model averaging four-point-oh that never fails badly. Report p95 and the failure rate, not only the mean.

Adaptability has a discovery problem. You cannot test for a scenario you have not imagined, so you test for the *behaviour* under novelty: does it ask for missing information, does it decline when the source does not contain the answer, does it hold format under an unfamiliar input shape.

### The sub-concepts

**Repeat variance.** Run the same prompt several times. If the outputs disagree materially, your reliability is bounded by that spread, and a temperature setting is often the cause.

**Temporal drift.** Three kinds, all measurable. *Input drift* — users start asking different things (new products, new seasons, new complaints). *Retrieval drift* — average similarity of top retrieved chunks falls, meaning the knowledge base has not kept up. *Model drift* — the vendor updates a floating alias, or your own prompt and guardrails change. Only the first two are visible in your own telemetry; the third requires pinned versions to even detect.

**Refusal calibration, both directions.** Under-refusal is a safety failure; over-refusal is a usability failure. Both must be measured, and they trade against each other. A model that refuses nothing and a model that refuses everything are both broken, in opposite directions.

**Adaptability signals you can read without new labels.** Retry rate, regeneration rate, conversation abandonment, thumbs-down ratio, and how much a human edits a draft before sending. All of these fall out of normal usage and none requires an annotator.

**The stress test is a schedule, not an event.** A week of varied inputs with daily scoring is more informative than an afternoon of heroics. The point is to catch the day the behaviour changes.

### How it connects to the rest of the framework

`TSC4-Advanced-A2` varies inputs; this bullet adds time and repetition. `TSC4-Advanced-K3` supplies the version pinning that makes drift attributable. `TSC4-Advanced-A4` is the operational answer — monitoring and canary rollout are how reliability stops being a hope. `TSC4-Intermediate-A5` is the mechanics of one comparison; this is the sustained version. `TSC4-Advanced-K1` explains why p99 latency behaves nothing like the mean.

### What is current as of November 2026

With current frontier models, reliability has become the differentiator precisely because raw capability has converged:

- **Floating aliases still move.** Vendors refresh the model behind a name with little notice. Reliability engineering now means pinning a dated snapshot and scheduling deliberate re-evaluation, not trusting the endpoint to stay still.
- **Reasoning modes changed the variance profile.** A thinking mode trades repeatability and latency for accuracy on hard tasks; a fast mode is steadier and shallower. Reliability testing must specify which mode was tested.
- **Refusal behaviour is a live procurement issue.** Safety tuning tightened across the major vendors, and false refusals on legitimate professional content (clinical, legal, security) are now a common reason a technically strong model is rejected.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It got it right when I tried it."* Once is an anecdote. Reliability is a distribution.
- *"Reliability and adaptability are the same thing."* A model can be rock-steady on known inputs and collapse on anything new — or flexible and inconsistent. Different tests, different failures.
- *"We will notice if it degrades."* Without a baseline and a schedule, degradation is invisible; users just quietly stop using it.
- *"Higher temperature is always less reliable."* Higher temperature is more *varied*. For creative work that is the point; for extraction it is a defect.

## How a student should understand it

**Mental model:** a taxi driver you would recommend. Not the fastest lap on a clear road — the one who is the same competent driver at 2 a.m. in the rain, and who says "I do not know that address, let me check" instead of guessing.

**Things they can do after this bullet:**
1. Design a week-long stress test with a varied input set and a daily score.
2. Distinguish input drift, retrieval drift and model drift in a live system.
3. State a reliability claim in terms of failure rate and tail, not average.

**Misconceptions to kill:** that a demo predicts production, that adaptability and reliability are one axis, and that degradation announces itself.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT versus the taxi.** The MRT is less glamorous and arrives every four minutes in the rain. Reliability is that timetable; adaptability is the driver who reroutes when a road closes. You want both, and they are not the same quality.

**The regular kopitiam.** Same uncle, same kopi, every morning for nine years. That is reliability. The day the coffee machine breaks and he offers you tea instead without drama — that is adaptability.

### Worked example with a real tool

Run the same task five times and look at the spread, then change one condition:

```text
Summarise this complaint in three bullets: "The parcel arrived crushed,
two items missing, and your hotline kept me on hold for 40 minutes."

Run it five times at temperature 0.9, then five times at 0.2.
Note where the bullets disagree with each other.
```

What to point at afterwards: at the higher setting the *facts* stay but the emphasis, ordering and even which complaint is called primary shift. Ask the room which version they would put in front of a customer, and then: "if the summariser feeds a triage queue, does the variation matter?" That is where reliability stops being abstract — inconsistent summaries mean inconsistent routing, and the queue silently mis-prioritises.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show five runs of one prompt with visibly different answers, then ask "which one is the product?"
2. **State the objective** — by the end you can design a stress test and name the drift you would detect.
3. **Recall prior learning** — sampling settings and why output varies at all.
4. **Present the content** — repeat variance, the three drifts, refusal calibration, implicit signals.
5. **Guide** — build one week's test schedule together on the board.
6. **Elicit performance** — teams design a stress test for a named system and pick their thresholds.
7. **Give feedback** — debrief, correcting tests that only vary the prompt and never the world.
8. **Transfer** — each learner names the drift most likely to hit their own system first.

## What the framework doesn't mention but trainers need to know

- **Reliability is partly a product decision.** Larger context, stricter schemas and lower temperature all buy consistency at the cost of flexibility. Say which one you traded.
- **Silent vendor updates are the hardest reliability risk.** Pin the snapshot; keep a fallback prompt per model family; re-run the harness before switching.
- **Multi-provider failover is not free.** A prompt tuned for one family can break formatting on another, so the fallback needs its own tested template.
- **Users adapt around unreliability instead of reporting it.** Falling usage and rising edit distance are the early warnings; nobody files a ticket saying "it got worse".
- **Adaptability testing is where the Singlish cases earn their keep.** Code-switched input is the cheapest available proxy for "unseen distribution".

## Watch out

- **Do not present a demo as evidence of either property.** A demo proves one output; it is silent on both axes.
- **Do not let "it is stochastic" end the conversation.** Stochastic does not mean unmeasurable — pass rates and spreads are measurable.
- **Do not test reliability only on the happy path.** A model that is stable on easy inputs and wild on hard ones is unreliable exactly where it matters.
- **The stale claim to retire:** "the model does not change, so we do not need to re-test." The endpoint changes; the world changes; the data changes.
