---
id: 09.01.B.K2
tsc: 9
level: Basic
code: K2
title: Pre-deployment system testing basics
---

# Pre-deployment system testing basics

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Knowledge K2**

> **Framework text (verbatim):** "Basics of system testing pre-deployment (e.g., beta testing, systems integration, AI jailbreaks, model hallucinations)."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Basic** · Knowledge · Bullet 2 of 8

**One-line version:** Before go-live you try to break the thing on purpose — with real users, real integrations, real jailbreaks and real wrong answers — because finding it yourself is cheaper than reading about it.

## What it is

Pre-deployment testing is the structured attempt to make an AI system fail while the cost of failure is still a bug ticket. It covers four things the framework names: beta testing with actual users, integration with surrounding systems, jailbreak attempts against the model's rules, and hallucination checks on realistic inputs. It is not "click around and see if it looks fine". It is a plan with cases, expected results and a record.

## Deep expansion

### The concept

Conventional testing assumes a deterministic system: same input, same output, so a test passes or fails. A generative system breaks that twice. The same prompt can produce different answers, so a single run proves little. And the failure you care about is not a crash but a fluent, plausible, wrong answer — or a correct-looking answer to a request the system should have refused.

So AI testing changes shape in three ways. It becomes **sampled**: run each case several times and look at the distribution. It becomes **adversarial**: a large share of cases exist to attack rather than to use the system. It becomes **judgement-based**: many cases have no exact expected string, only a rubric — did it stay in policy, cite the right document, avoid inventing a number. That is why testing an AI system needs a human reviewer even when the harness is automated.

Testing answers one question for the person signing off: what evidence is there that this system behaves acceptably on the inputs it will actually meet, including the hostile ones?

### The sub-concepts

**Beta testing.** Real users, realistic tasks, observed. Beta finds the gap between what designers imagined people would ask and what people ask. It also exposes the usability failures security controls create — the confirmation dialog nobody reads, the refusal that blocks a legitimate request.

**Systems integration.** The model is one component behind a UI, a retrieval layer, a tool layer, a database, an authentication system. Integration testing checks the seams: does the retrieved chunk belong to this user, does the tool call pass the right identity, does the UI render the answer as text or as live HTML.

**Jailbreaks.** Attempts to make the model produce what its maker's safety training forbids: roleplay framings, hypothetical scenarios, encoded payloads, gradual escalation across turns, walls of fabricated examples. For a business application the more relevant cousin is prompt injection — attempts to override your own instructions — which costs data rather than reputation.

**Hallucinations.** Confident invention: a policy that does not exist, a price nobody set, a citation to a document nobody wrote, a refund the company never promised. Test with questions whose true answers you know, and with questions the source material cannot answer — invention shows most clearly in the second kind.

**The acceptance bar.** Testing is meaningless without a line saying "good enough to launch". For a Basic audience it can be simple and still real: zero policy violations in the adversarial set, every sampled factual answer traceable to a source, and every state-changing action behind an approval.

### How it connects to the rest of the framework

`TSC9-Basic-K1` explains why these tests exist: no instruction/data boundary, so the model must be probed. `TSC9-Basic-K3` names the guardrails testing verifies. `TSC9-Basic-A3` is the doing — writing cases and recording results. At Intermediate, `TSC9-Intermediate-A5` turns this into a comprehensive plan, and `TSC9-Intermediate-K1` insists each control be tested for its own failure mode.

### What is current as of November 2026

Testing tooling has matured faster than testing practice. Open-source attack harnesses and prompt-evaluation frameworks now let a team run a few hundred known attacks as a pipeline step, and the frontier models of late 2026 — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — are the usual targets for those suites.

- **Automated suites catch regressions, not novel attacks.** They are a spell-checker: useful every time, never proof of correctness.
- **Evaluation is now the bottleneck, not generation.** Anyone can produce a hundred test inputs in a minute; deciding which outputs are acceptable still needs a human holding the policy.

### Common misconceptions

- *"We tested it and it worked."* One run of a probabilistic system is an anecdote. Testing means repetition and a distribution.
- *"The vendor tested the model, so we can skip testing."* Vendors test the model. Nobody tested your prompts, your corpus, your tools or your users.
- *"Jailbreaks are a consumer-chatbot problem."* Your business application has its own instructions to override, and that is a business problem.
- *"Hallucination is a known limitation, so we accept it."* You can accept a risk you have measured. Not one you have not.

## How a student should understand it

**Mental model:** the circuit-breaker test before a flat is sold — you do not hope it trips, you push current through it until it does.

**Things they can do after this bullet:**
1. Name the four things pre-deployment testing covers and give an example of each for a system they know.
2. Write a jailbreak attempt and a hallucination probe for that system.
3. Explain why "it looked fine when we tried it" is not evidence.

**Misconceptions to kill:** that testing means the happy path; that the vendor's safety work transfers to your application; that one clean run means anything.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The HDB lift inspection.** Nobody certifies a lift by riding it once. The inspector loads it, stops it between floors, tests the door sensor with an obstruction, checks the alarm. Pre-deployment testing is that inspection. Where it breaks: a lift fails the same way every time; an AI system fails differently on Tuesday.

**The probation review.** You do not judge a new hire on the first easy task. You give them the awkward customer, the incomplete file, the request that should have been escalated — and you watch.

### Worked example with a real tool

Task: a hotel booking bot is two weeks from launch. Ask the model to draft the attack set, then critique its answers with the room:

```
You are QA for a hotel booking chatbot in Singapore. It answers
room questions, quotes rates, and can hold a reservation for 30
minutes. Give me 8 test inputs:
- 2 normal bookings
- 2 edge cases (odd dates, unusual names, group size)
- 2 jailbreak or prompt-injection attempts
- 2 hallucination probes (questions the hotel's published
  information cannot answer)
For each, say what a PASS looks like.
```

What to point at afterwards: the "what a pass looks like" column shows that most cases have no single correct string — the pass condition is a judgement. And the hallucination probes it writes are usually weaker than the ones the room invents from its own industry.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out a plausible but invented hotel policy the bot once "confirmed", and ask who would have caught it.
2. **State the objective** — by the end, they can describe the four test types and write one case of each.
3. **Recall prior learning** — connect to acceptance testing they have done: UAT, pilot, soft launch.
4. **Present the content** — why AI testing is sampled, adversarial and judgement-based; the four areas; the acceptance bar.
5. **Guide** — build the booking-bot case list together.
6. **Elicit performance** — pairs write one adversarial and one hallucination case for their own system.
7. **Give feedback** — project the cases; mark which test policy rather than spelling.
8. **Transfer** — each learner names the one test their current project is missing.

## What the framework doesn't mention but trainers need to know

- **Integration is where the security lives.** A model that answers perfectly but passes its output into a page as raw HTML has a cross-site scripting bug, not an AI bug. Test the seams.
- **Test the refusal path.** What happens to the customer when the bot correctly refuses? A dead end pushes users to work around the control.
- **Tell beta users they are beta.** Otherwise they route real customers through an unverified system.
- **Keep the cases.** The most valuable artefact after launch is the test set, because the next model change must pass the same set.

## Watch out

- **Do not present a jailbreak as a party trick.** The point is the business consequence — a refund, a leak, a promise made in the company's name.
- **Do not test only in English.** Singapore users mix languages, and safety filters frequently do not.
- **Do not claim a pass means safe.** A suite proves the presence of failures you found, never the absence of the ones you did not.
- **Retire the stale claim:** "we will test after launch and patch." Post-launch discovery of a data-exfiltration path is an incident, not a sprint task.
