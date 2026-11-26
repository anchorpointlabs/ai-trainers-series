---
id: 09.03.A.A1
tsc: 9
level: Advanced
code: A1
title: Refine system testing procedures
---

# Refine system testing procedures

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A1**

> **Framework text (verbatim):** "Refine comprehensive system testing procedures."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Ability · Bullet 7 of 12

**One-line version:** Every attack that gets past your tests is a specification for the next version of your tests — and the procedure only earns the word "comprehensive" if it changes when it fails.

## What it is

Refining a testing procedure means improving the procedure itself: adding case classes that were missing, extending coverage to the parts of the pipeline nobody was testing, raising thresholds, and wiring the whole thing into the release gate so it runs without being asked. It is the maintenance discipline behind K1's methodology and A4's fix loop.

## Deep expansion

### The concept

A test procedure has four parts, and any of them can be the weak point: the **case classes** (what kind of attack you try), the **data** (which inputs represent each class), the **threshold** (what score counts as a pass), and the **execution context** (when it runs, against which build, and what happens on failure).

Most procedures fail at the third and fourth, not the first. Teams add another clever prompt to the list, then keep the pass criterion as "nothing obviously bad happened", and run the suite once, manually, before a launch that was already announced. The refinement discipline is unglamorous: convert each new failure into a reproducible case, define the pass bar numerically, and make the run automatic against the exact build that ships.

There is also a structural gap that recurs so often it deserves naming. Teams test the front door — the user's first message — and forget the middle of the pipeline. In a retrieval system the dangerous instruction usually arrives in step two, inside a retrieved document, long after the front-door filter has approved the conversation. Similarly, a test suite written for single-turn chat misses the multi-turn escalation that a real attacker uses, and a suite written for a model misses the tool call that actually causes harm.

### The sub-concepts

**Case-class taxonomy.** Name the classes and keep them stable across releases: direct injection, indirect injection via retrieved or uploaded content, prompt leaking, encoding and language evasion, multi-turn escalation, exfiltration attempts, output-handling exploits, tool misuse, resource exhaustion. A class with no test data is a known blind spot you have chosen to accept — write it down as such.

**Test data that represents the population.** Realistic prompts from real workflows, plus local language coverage. For Singapore deployments that means Singlish, Malay, Tamil and Chinese inputs, because an attack written in code-switching may pass a filter trained on standard English.

**Thresholds with a scope.** "No successful leakage in 200 attempts per class, on the release candidate, before sign-off" is a threshold. Pass rates also need a held-out set you did not tune against, or the number measures the tuning rather than the system.

**Execution in context.** The suite runs in the pipeline, against the pinned model version and pinned prompt version, and a failure blocks the release. Model or prompt changes re-trigger it automatically, because those changes are the ones that quietly invalidate last month's result.

**The incident-to-case conversion.** Every incident post-mortem ends with one artefact: a test case. This is the mechanism by which procedures improve, and the reason a procedure that never changes is a procedure that has stopped learning.

**Coverage of the whole pipeline.** Front door, retrieval, tool layer, output rendering, and the agent loop — each has its own entry path and therefore its own tests.

### How it connects to the rest of the framework

K1 defines the threat model and the acceptance bar this procedure implements. K4 supplies the attacks that populate the classes. A4 turns one finding into a fix and a regression case. A2 refines the guardrails that some cases exercise. K3's measurement depends on this suite being honest about what it covers. At Intermediate level, `09.02.I.A5` is the practitioner's version of running pre-deployment testing.

### What is current as of November 2026

- **Evaluation harnesses are products.** Automated suites, including IMDA's Project Moonshot, make it cheap to run hundreds of cases — which shifts the difficulty from running tests to choosing classes and thresholds.
- **Builds change underneath you.** Foundation models are updated and retired by providers; without version pinning, last month's pass is not evidence about this month's system.
- **Agents require multi-step cases.** A test that ends at the first reply cannot see a five-tool sequence that ends in an email, so the case format now needs to assert on the trajectory, not just the final text.
- **Long context invites long-form attacks.** Narrative and many-shot jailbreaks need their own class, because they fail differently from a short override.

### Common misconceptions

- *"We have a test set."* A set is data. A procedure is data plus classes plus thresholds plus an execution point.
- *"Testing happens at the end."* It happens at every change, or it happens once and misleads for a year.
- *"A 99% pass rate is good."* Aggregate pass rates hide the class that fails, and the failing class is what an attacker uses.
- *"The tests are the QA team's job."* The people who built the prompt and the tool calls know where the behaviour is fragile; QA does not.

## How a student should understand it

**Mental model:** a pre-flight checklist that gets a new line every time an aircraft type has an incident — the checklist is a memory of everything that has already gone wrong.

**Things they can do after this bullet:**
1. Take a finding and write it up as a reproducible case with an expected result.
2. Assign it to a class, then check whether the class has other members.
3. State the pass threshold and where in the pipeline the suite runs.

**Misconceptions to kill:** that a test set is a procedure, that aggregate pass rates mean safety, and that testing belongs to somebody else.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The aviation checklist.** Checklists grew because accidents happened and their causes were added as items. No pilot argues that the list is bureaucratic; the list is the accumulated memory of failure. Where it breaks: a checklist item is binary and checkable by a human, while a model test produces a probabilistic result that needs a threshold.

**The MOM incident-reporting loop.** A workplace injury is investigated, the cause is fixed, and the fix becomes an inspection item. A procedure that keeps inspecting for last year's cause and not this year's is how organisations repeat incidents.

### Worked example with a real tool

```
You are the test lead for a customer-support assistant with a retrieval step and an
email tool.

Fact: a jailbreak that hid the request inside a 900-word personal story passed all
existing tests.

1. Name the case class this belongs to and what distinguishes it from existing
   classes.
2. Write five seed cases for the class — vary length, framing, language (include
   Singlish and Malay), and where the instruction sits.
3. Define the pass threshold for the class.
4. Say where in the pipeline this runs, and what must happen when it fails.
5. List the two classes most likely to be missing next, and the evidence that would
   tell you.
```

What to point at afterwards: the distinction between "add a long prompt to the list" and "create a class with variation". The first is patching; the second is a procedure change. Point also at step four — a test that does not run automatically, against a pinned build, is a document rather than a control.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — the 900-word jailbreak, shown beside the tests that missed it.
2. **State the objective** — amend a procedure so the class is covered and gated.
3. **Recall prior learning** — what their own team does when a bug escapes to production.
4. **Present the content** — the four parts of a procedure and the pipeline gap.
5. **Guide** — write two seed cases for the new class together.
6. **Elicit performance** — pairs complete the threshold and the execution point.
7. **Give feedback** — test each threshold: is it measurable, scoped and dated?
8. **Transfer** — each learner amends the procedure for a system they own.

## What the framework doesn't mention but trainers need to know

- **Keep a held-out set.** A suite you tune against reports improving numbers forever.
- **Track coverage, not just pass rate.** Which classes exist, which have data, which are stubs.
- **Record the near miss.** A case that produced a partial leak is the most valuable entry in the suite.
- **The tests must outlive the team.** Put the classes and thresholds in the repository, not in a deck.
- **Cost per run matters.** Suites that are slow get skipped; a fast smoke class plus a nightly full run is the practical shape.

## Watch out

- **Do not present a green suite as proof of safety.** It is proof that known classes failed to work on that build.
- **Do not test only the front door.** Retrieval, tools and rendering are where the pipeline leaks.
- **Do not let the suite become a list of lucky prompts.** Variation within a class is the point.
- **The stale claim to retire:** "we test before launch." As of November 2026 tests run on every change, against pinned model versions, or they describe a system that no longer exists.
