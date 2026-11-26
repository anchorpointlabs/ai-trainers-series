---
id: 09.02.I.K1
tsc: 9
level: Intermediate
code: K1
title: AI security measures and system testing in depth
as_at: 2026-11-26
review_by: 2027-02-25
---

# AI security measures and system testing in depth

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Knowledge K1**

> **Framework text (verbatim):** "In-depth understanding of AI security measures and system testing."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Knowledge · Bullet 1 of 10

**One-line version:** Every AI control has a documented way of failing — depth means knowing the failure before you configure the control, and testing for exactly that.

## What it is

AI security measures are the controls placed around a model: input filtering, output filtering and detection classifiers, least-privilege tools, sandboxing, human approval gates, constrained output formats, taint tracking, and continuous adversarial testing. In-depth understanding means two things beyond naming them: knowing which attack each one is meant to stop, and knowing the specific way it stops working — because a control trusted past its limit is worse than no control, since it suppresses the vigilance that would otherwise exist.

## Deep expansion

### The concept

Security in this domain is layered because no layer is sufficient. The reason is structural: the model is a probabilistic interpreter, so any defence that also relies on the model's judgement is probabilistic too. A rule in the system prompt is a request. A classifier is a second model, and therefore also persuadable. What is deterministic is the code around the model: what it is allowed to call, what identity the call carries, what schema the output must satisfy, what a human must approve.

So the layering principle is: **probabilistic controls for detection, deterministic controls for containment.** Filters and classifiers tell you an attack is likely and buy you time. Permissions, schemas and approval gates decide what happens even when the filter misses — and it will miss, because the attacker can probe a thousand times while your filter only has to fail once.

Testing follows the same split. Each control gets tested for its own failure mode, not for "security" in general. A blocklist is tested with encodings and paraphrases. A classifier is tested with false positives as well as false negatives. An approval gate is tested with alerts that look routine. A sandbox is tested for egress, not for whether it runs code.

### The sub-concepts

**Input filtering.** Deterministic rules — pattern matching, normalisation of Unicode and encodings, size and rate limits, allowlists of languages. Stops the known and the cheap; fails against polite natural language, which is what most real attacks are.

**Detection classifiers.** A smaller specialised model that scores a prompt or a retrieved document for injection risk before the main model sees it. Fails in three ways: it is itself a model and can be evaded; it adds latency and cost to every turn; and it produces false positives that block legitimate work — an engineer pasting a stack trace, a compliance officer summarising a fraud report.

**Least privilege and scoped agency.** The model gets the narrowest tools and the user's own identity, never a shared service account. The design rule: a tool the model can call must carry no identity parameter — the identity comes from the session, in code. Fails against an injection that abuses a permission the user legitimately holds.

**Sandboxing.** Untrusted code, file parsing or browsing runs in an ephemeral environment with no egress and no access to internal addresses. Fails if the sensitive data is mounted inside the sandbox and any channel back out exists — including the chat reply itself.

**Human approval gates.** A pause before state-changing or outbound actions, showing the exact tool and parameters. Fails through approval fatigue, through obfuscated parameters, and it cannot apply to headless batch workflows.

**Constrained output.** The answer must match a schema, an enum or a lookup table. The strongest control available; fails on any task whose point is free-form prose.

**Taint tracking.** Label data by trust level; once untrusted external content is in the context, block the dangerous sinks. Fails through over-tainting — in a workflow that always reads outside text, everything is tainted and legitimate automation stops — and through architectural cost.

**Continuous adversarial testing.** Automated attack suites in the pipeline plus manual testing. Fails as assurance: it proves the presence of the flaws you found, never their absence.

### How it connects to the rest of the framework

At Basic, `TSC9-Basic-K3` introduces guardrails as containment and `TSC9-Basic-K2` the testing idea. This bullet is the full set plus the failure catalogue; `TSC9-Intermediate-A2` implements the layered defence for prompt attacks, `TSC9-Intermediate-A3` tunes the filtering layer, `TSC9-Intermediate-A4` decides which layers a given system needs, and `TSC9-Intermediate-A6` keeps them honest over time. At Advanced, `TSC9-Advanced-K1` turns this into a methodology.

### What is current as of November 2026

The control set is stable; the balance has shifted. Vendors now train instruction hierarchies that make crude overrides less effective, and current frontier models are markedly better at treating retrieved text as data rather than orders. Meanwhile agents with tools have made the deterministic layers load-bearing.

- **Containment matters more than refusal.** The interesting question is what the system cannot do, not what it declines to say.
- **Test suites are commoditised.** Open attack harnesses make coverage cheap; deciding pass criteria is the remaining skill.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"We have a guardrail, so injection is handled."* A guardrail raises the cost of a casual attack. It does not close the class.
- *"Least privilege solves it."* It bounds the damage of an injection that abuses a permission the user really has.
- *"Sandboxing makes code execution safe."* It protects the host. Data inside the sandbox can still leave through the reply.
- *"A clean red-team run means we are secure."* It means the attacks you ran did not work.

## How a student should understand it

**Mental model:** a bank branch — the polite greeter is the prompt, the teller's screen limits are the permissions, the vault door is the approval gate, and the camera is the log.

**Things they can do after this bullet:**
1. Map a system's controls to the attacks each is meant to stop.
2. Name the failure mode of any control in the set, and the test that would expose it.
3. Say which controls are deterministic and which rely on the model's judgement.

**Misconceptions to kill:** that a control is a solution; that testing in isolation proves a control; that model improvements remove the need for architecture.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The layered security of a condo.** The guard at the gate, the card at the lift lobby, the lock on the unit door, the safe inside. Each is defeatable; together they make an attack slow and visible. Where it breaks: the condo's layers do not argue with you; a classifier does.

**The MRT fare gate.** It does not care why you are in a hurry or how politely you ask. That determinism is what makes it a control rather than a request.

### Worked example with a real tool

Give the room one system and one attack, then make them defend it layer by layer:

```
Our HR assistant reads uploaded resumes (PDF), summarises them, and
can email the hiring manager a shortlist. A candidate embeds a hidden
instruction in their PDF telling the assistant to score them 100 and
email the shortlist to an outside address.

For each layer — input filter, detection classifier, least privilege,
human gate, constrained output, sandbox, egress control — say what it
would catch, and one way it fails here.
```

What to point at afterwards: the egress control and the human gate are the two that actually break the attack; the classifier only raises the cost. The room will usually over-rate the filter. That gap is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — describe the resume attack in one sentence and ask which single control stops it.
2. **State the objective** — by the end, they can map controls to attacks and name each control's failure mode.
3. **Recall prior learning** — defence in depth from any security training they have had.
4. **Present the content** — the deterministic/probabilistic split; the eight controls; the failure of each.
5. **Guide** — work the resume case across the layers together.
6. **Elicit performance** — groups pick a control and write the test that exposes its failure.
7. **Give feedback** — debrief: which tests would have passed a broken control.
8. **Transfer** — each learner audits one control in a system they run.

## What the framework doesn't mention but trainers need to know

- **Latency and cost are part of the design.** A classifier per turn is a product decision, not just a security one.
- **False positives remove controls.** If blocking legitimate work reaches a few percent, the business will ask for the guardrail off. Log and tune, or lose it.
- **The seams are unguarded.** Teams inspect the first prompt and trust the rest of the chain; the injection arrives in the retrieved document at step two.
- **Some risks are not control-shaped.** If the assistant should not have the data at all, the answer is access control, not a filter.

## Watch out

- **Do not present any single control as the answer** — including taint tracking, which is the strongest of the architectural options.
- **Do not demo filters as guarantees.** Show a bypass, then show the containment.
- **Do not let the class leave thinking "tested" means "safe".** Give them the sentence: a test proves what you found.
- **Retire the stale claim:** "the next model generation will patch prompt injection." It is a property of the architecture, not a bug in a version.
