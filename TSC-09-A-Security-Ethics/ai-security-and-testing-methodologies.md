---
id: 09.03.A.K1
tsc: 9
level: Advanced
code: K1
title: AI security and testing methodologies
as_at: 2026-11-26
review_by: 2027-02-25
---

# AI security and testing methodologies

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K1**

> **Framework text (verbatim):** "Methodologies of AI model security and testing."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Knowledge · Bullet 1 of 12

**One-line version:** A methodology turns "we tested it and it seemed fine" into "here is what we are defending, here is the attack list we ran, and here is the score that blocks a release".

## What it is

A methodology for AI security is a written, repeatable procedure with three parts: a threat model of the system being deployed, a catalogue of the attack classes tested against it, and an acceptance bar that decides pass or fail. It exists so two teams securing two similar systems reach comparable standards, and so a decision made in March can still be defended in November.

## Deep expansion

### The concept

Conventional application security rests on one assumption: code and data can be separated. A database driver sends a query structure and its values through different channels, so a value can never become a command. An LLM has no such separation. The developer's system prompt, the retrieved document and the user's message are concatenated into one sequence of tokens and read by the same attention mechanism. There is no parser to reject a malformed instruction, because every sequence of tokens is valid input and produces some output.

That single architectural fact changes what "secure" can mean. You cannot patch the interpreter; you can only contain it. A methodology is how containment becomes deliberate rather than accidental: which controls sit where, which attacks are tried before release, and what result stops the launch.

For the learner the shift is from activity to evidence. "We ran a red team" is an activity. "We ran these nine attack classes against this release candidate, found two bypasses, fixed both, re-ran the suite with zero bypasses and added a regression case for each" is a methodology — and it is the only version that survives an audit or an incident review.

### The sub-concepts

**Threat model, one line.** Who attacks, through what surface, to get or destroy what. For a model-backed system the surfaces are the prompt, the documents it retrieves, the tools it can call, the way its output is rendered, and the model artefact itself. Writing that sentence is the cheapest security work available, and skipping it is the most common failure.

**Test catalogue.** The attack classes worth naming out loud: direct prompt injection, indirect injection through data the system reads, prompt leaking, jailbreaks, data exfiltration, insecure output handling (model text handed to a browser, a database or a shell), model supply chain (weight files that execute code when loaded), data poisoning, and resource exhaustion including runaway agent loops.

**Acceptance bar.** A number, a scope and a date. "No successful system-prompt extraction in two hundred attempts across four languages, on this build" is an acceptance bar. "It felt solid" is a mood.

**The lethal trifecta as a scoping tool.** Private data, untrusted input and an outbound channel in one workflow is the configuration where an attacker can read your data and send it out. If all three legs exist, the catalogue must include exfiltration tests, not only content tests.

**Layers with different physics.** Deterministic code — identity taken from the session, permissions, schema validation — holds under attack. Classifiers hold probabilistically. Human gates hold only while the human is awake. A methodology assigns each risk to the layer that can carry it, and states what happens when that layer fails.

### How it connects to the rest of the framework

`09.01.B.K1` is the what (fundamentals of model security) and `09.01.B.A3` is the beginner's version of pre-deployment testing; this bullet is the discipline that organises both. Forward: K4 supplies the attacks, A4 closes the loop from finding to fix, A1 keeps the procedure current, K3 governs the classifiers, K5 carries residual risk into the enterprise register, and A6 decides where the gate sits.

### What is current as of November 2026

Better models have not solved this. Instruction-hierarchy training in the current frontier line — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — reduces how often a model obeys an embedded instruction, but the vulnerability class stays architectural, so containment is still the control that holds. Three shifts matter for teaching:

- **Agency is the default.** Tool use and agent frameworks moved from demo to product, so the catalogue now has to cover multi-step behaviour — a tool chain, a browser session, a scheduled task — and not just one reply.
- **Testing tooling is a market.** Automated attack suites and evaluation harnesses are now commercial products and open-source projects, and IMDA's Project Moonshot offers a Singapore-contextualised option. That raises the floor, and tempts teams to mistake tool output for assurance.
- **Guardrails are layered and priced.** Classifier shields, structured-output enforcement and policy checks in the orchestration layer are standard, and each adds latency and cost, so a methodology budgets for them instead of assuming them free.

### Common misconceptions

- *"The vendor's model is safety-tuned, so security is handled."* Vendors train refusal of universal harms. They know nothing about your refund limit, your row-level permissions, or your customer's inbox.
- *"It is internal, so nobody attacks it."* An internal assistant that reads external email, tickets or PDFs is attacked through those documents.
- *"We added an injection detector, so injection is solved."* The detector is itself a model with false negatives and false positives; design as if an injection will get through.
- *"AI security is application security with a new name."* The overlap is real at the output boundary — model text into a browser is still cross-site scripting. The root cause is new, which is why patching works at the boundary and fails for the injection itself.

## How a student should understand it

**Mental model:** a fire-safety plan for a building still on the drawing board — it names the exits, the drills, and the inspection that lets the building open.

**Things they can do after this bullet:**
1. Write a one-line threat model for any AI feature in their own organisation.
2. Name the attack classes that apply to it, and the two that do not.
3. State an acceptance bar as a number, a scope and a date.

**Misconceptions to kill:** that a vendor supplies security, that internal means safe, and that a passing suite proves absence of vulnerabilities rather than the presence of effort.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The VICOM inspection and the driving test.** Both are methodologies, not opinions: a fixed set of checks, a published pass standard, and a record that follows the vehicle or the driver. Two inspectors examining the same car should reach the same verdict; if they do not, the checklist is the problem. Where it breaks: vehicles are deterministic and the test is finite, while a model's input space is unbounded, so the inspection samples rather than proves.

### Worked example with a real tool

Ask for the artefact, not an essay. In ChatGPT, Claude or Gemini:

```
You are a security engineer. System under review: a customer-service chatbot that
(a) reads PDFs uploaded by customers, (b) queries an orders database through a tool
bound to the logged-in user, and (c) can email a summary to that customer.

Produce:
1. A one-line threat model: who attacks, via what, to get what.
2. The five highest-value attack classes from [direct injection, indirect injection,
   prompt leaking, exfiltration, insecure output handling, supply chain,
   denial-of-wallet], and why each applies here.
3. One acceptance bar for each of your top three — written as a number, a scope and
   a date.
```

What to point at afterwards: the model produces a plausible catalogue without difficulty, and that is the lesson — the catalogue is the easy part. The discipline is in step three, where a bar must be testable, and in noticing that the indirect injection arrives inside the customer's PDF, which no front-door filter ever inspects.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a support bot following an instruction hidden inside a customer's PDF.
2. **State the objective** — by the end you can write a threat model, a short test catalogue and an acceptance bar for one feature.
3. **Recall prior learning** — ask what they already test before a normal software release.
4. **Present the content** — the three parts of a methodology, and why the interpreter cannot be patched.
5. **Guide** — build the threat model for the three-tool chatbot together.
6. **Elicit performance** — pairs write an acceptance bar for one attack class.
7. **Give feedback** — project two bars and ask which is testable and which is a wish.
8. **Transfer** — each learner applies it to a live or planned feature in their own job.

## What the framework doesn't mention but trainers need to know

- **The methodology has to survive a model swap.** Foundation models are updated and deprecated underneath applications; a suite pinned to a version is the only way to notice a behaviour change.
- **Scope the catalogue to the trifecta.** Teams that test everything test nothing well. Data sensitivity, input trust and agency tell you where depth belongs.
- **Logging is part of the methodology.** Without the assembled context, the retrieved chunks and the tool-call arguments, an incident cannot be reconstructed — which means it cannot be fixed or defended.
- **The economics are real.** Denial-of-wallet is an availability attack priced in tokens: an unauthenticated endpoint with no spend cap is a budget incident waiting for a bot.
- **Nobody owns "security" generically.** Name the person who signs the acceptance bar, or the bar is decorative.

## Watch out

- **Do not demo an attack on a live third-party product** without permission; use your own test endpoint or a documented public example.
- **Do not present a guardrail as a boundary.** Say plainly that classifiers reduce frequency and deterministic controls bound impact.
- **Do not let the catalogue become the deliverable.** A beautiful test plan with no run record is theatre.
- **The stale claim to retire:** "prompt injection will be fixed in the next model generation." As of November 2026 it remains a property of putting instructions and data in one context window, which is why containment, not patching, is the control.
