---
id: 09.03.A.K4
tsc: 9
level: Advanced
code: K4
title: Red teaming for vulnerabilities
as_at: 2026-11-26
review_by: 2027-02-25
---

# Red teaming for vulnerabilities

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K4**

> **Framework text (verbatim):** "Red teaming for discovering vulnerabilities in generative AI models."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Knowledge · Bullet 4 of 12

**One-line version:** Red teaming is attacking your own system on purpose, with a written scope and a findings register, so the flaw is found by someone who will report it instead of someone who will exploit it.

## What it is

Red teaming is structured adversarial testing: a team plays the attacker against a defined target — the model, the application around it, or both — using realistic attack methods, and records what worked. It is a diagnostic method, not the security posture itself. The posture is the architecture, the controls and the response plan that come afterwards.

## Deep expansion

### The concept

Functional testing asks whether the system does what it should. Red teaming asks what else it will do. The distinction matters because a generative system has no closed list of correct behaviours — every input produces some output, and the interesting question is which inputs produce the output the developer did not intend.

"Red teaming" now covers two activities that trainers must separate, because they answer different questions and are performed by different people:

1. **Model-level (alignment) red teaming** — conducted by model labs, probing a base model for prohibited content: weapons instructions, hate speech, self-harm encouragement, political bias. It tests the model's training.
2. **System-level (security) red teaming** — conducted against your deployed application: its system prompt, retrieval pipeline, tools, guardrails, and integrations. It tests whether an attacker can extract another user's data, invoke an unauthorised action, or reach the internal network.

The framework bullet sits at the second, but a trainer who blurs them will produce learners who test the wrong layer. A model that refuses beautifully can still be made to send an email it should not send, because the refusal is trained behaviour while the email tool is architecture.

### The sub-concepts

**Scope and rules of engagement.** Which targets are in scope, which are out, who authorised it, what data may be used, where findings are stored, and who is told. Without this, red teaming is unauthorised penetration testing with a friendlier name.

**The attack families you actually run.** Direct prompt injection (the user tries to override the app's rules), indirect injection (a document, email, ticket or web page carries the instruction), prompt leaking (recover the system prompt and tool schemas), jailbreaks (bypass the model's own safety training — roleplay, encoding, fictional framing, many-shot priming, gradual escalation across turns, low-resource languages), exfiltration (get data out through a rendered image, a link or a tool), insecure output handling (model text into a browser, database or shell), supply chain (weights that execute code on load), resource exhaustion (runaway loops, spend attacks).

**Manual and automated together.** Automated suites give coverage and repeatability and belong in a pipeline; humans find the chains no suite encodes, especially multi-turn and multilingual ones. The two are complements, and running only one produces a comfortable illusion.

**Findings discipline.** Reproduce, minimise, classify, severity-rate, assign an owner, and log it. A finding that lives in a chat thread is folklore; a finding with a reproduction script is a ticket.

**The limits, stated plainly.** Red teaming proves presence of vulnerabilities, never absence. A clean run means the attacks you thought of did not work on the day you ran them.

### How it connects to the rest of the framework

K1 is the methodology that gives red teaming its catalogue and acceptance bar. A4 is the loop that turns findings into fixes. A1 folds each finding into the permanent test procedure. K3 is where a finding often lands, as a guardrail refinement. K5 carries accepted residual risk into the register. At Basic level, `09.01.B.A1` is the beginner's version — spotting obvious vulnerabilities.

### What is current as of November 2026

- **Tooling is mainstream.** Open-source attack suites and IMDA's Project Moonshot let a small team run structured campaigns, which raises the floor and lowers the excuse.
- **Multi-turn and agentic attacks dominate.** Attacks that unfold across a conversation, or that ride a tool chain, are more effective than single clever prompts — and most test suites still under-sample them.
- **Long context is a weapon.** Very large context windows make many-shot priming practical: dozens of fabricated examples that teach the model, in-context, to comply.
- **Model refusal improved; the class did not.** Current frontier models are harder to jailbreak than their predecessors, yet indirect injection and insecure output handling remain engineering problems in the application, not model problems.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Red teaming is for the big labs."* Labs red-team models. Your application — prompts, tools, data, permissions — is red-teamed by you.
- *"One exercise before launch is enough."* Attack families change monthly; a red team is a rhythm, not an event.
- *"Jailbreaking and prompt injection are the same thing."* A jailbreak targets the model's safety training; injection targets your application's instructions. Different targets, different fixes.
- *"We passed a thousand-prompt suite, so we are secure."* You proved those thousand did not work. The thousand-and-first is untested.

## How a student should understand it

**Mental model:** an unannounced fire drill run by someone whose job is to find the door that does not open — and who writes down which door it was.

**Things they can do after this bullet:**
1. Write a scope of engagement for a red-team exercise on their own system.
2. Name the attack family each test belongs to, and say what a success would look like.
3. Turn one finding into a reproduction script and a severity rating.

**Misconceptions to kill:** that it belongs only to labs, that it is a one-off, and that a clean suite equals safety.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Baggage screening with simulated threats.** Screeners are tested with images of contraband slipped into the live X-ray stream, because a screener who never sees a threat stops seeing threats. The difference: airport test items are known to the designer and the screener is the one measured; in red teaming the designer is the attacker and the system is measured.

**The SCDF audit before a fire-safety certificate.** Someone with authority walks the building trying the exits, not reading the floor plan. Where it breaks: the audit is pass/fail against a published code, whereas red teaming produces a distribution of weaknesses with no natural stopping point.

### Worked example with a real tool

Make the model commit to a family and a defence, not a list of ideas:

```
You are red-teaming a bank's customer chatbot. It has a system prompt with internal
escalation rules, a tool that reads the logged-in customer's transactions, and a
tool that emails a summary.

Write three attacks from three different families (choose from: direct injection,
indirect injection via an uploaded document, prompt leaking, encoding-based
jailbreak, many-shot priming, exfiltration).

For each: the exact text or sequence to send, the mechanism you expect to work,
what a successful result would look like on screen, and the single defender action
that would have stopped it.
```

What to point at afterwards: the exfiltration attack usually needs a rendering channel — a markdown image or a clickable link — and that is the moment learners see that the vulnerability lives in the application, not in the model's weights. Ask which of the three defender actions is deterministic and which is a classifier.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a one-line indirect injection hidden in a CV that changes a screening score.
2. **State the objective** — scope, run and record at least one attack per family.
3. **Recall prior learning** — what they already test before a release, and what they never test.
4. **Present the content** — the two kinds of red teaming, the families, the findings discipline.
5. **Guide** — run the prompt-leaking attack live and read the output together.
6. **Elicit performance** — pairs write one attack and one detection idea.
7. **Give feedback** — classify each attack into its family; check that it is reproducible.
8. **Transfer** — each learner writes the scope sentence for their own system.

## What the framework doesn't mention but trainers need to know

- **Authorisation is not a formality.** Attacking systems you do not own is a criminal matter in most jurisdictions, including Singapore.
- **Never red-team with real customer data.** Use synthetic records, or a masked copy with an access log.
- **Diversity beats volume.** One attack from each family finds more than a thousand variations of one.
- **Record the near-misses.** An attack that half-worked is the strongest signal in the register, and it is the one teams forget to log.
- **The report is a decision document.** For each finding: what it is, what it would cost, who fixes it, by when, or who accepts it.

## Watch out

- **Do not publish working exploits** against live products, and do not encourage learners to "try this on a site".
- **Do not conflate safety and security findings** in one register; the owners and the remedies differ.
- **Do not let the tool define the scope.** A suite that runs 500 prompts is evidence of effort, not coverage.
- **The stale claim to retire:** "red teaming is a pre-launch box to tick." As of November 2026 it is continuous, it runs in the pipeline, and its findings feed the same register as incidents.
