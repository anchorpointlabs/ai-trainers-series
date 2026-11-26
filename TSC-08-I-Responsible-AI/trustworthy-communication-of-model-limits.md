---
id: 08.02.I.K4
tsc: 8
level: Intermediate
code: K4
title: Trustworthy communication of model limits
---

# Trustworthy communication of model limits

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Knowledge K4**

> **Framework text (verbatim):** "Trustworthy and transparent communication of generative model capabilities and limitations."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Knowledge · Bullet 4 of 14

**One-line version:** Trust is built by naming the failure before the user finds it — the model will never volunteer its own limits, so somebody in the organisation has to.

## What it is

Trustworthy communication means stating plainly, to the people who depend on a system, what it does well, where it fails, and when a human must take over — then documenting that statement so staff, buyers and auditors can rely on it. It is not marketing with a disclaimer; it is an operational claim you are prepared to be held to.

## Deep expansion

### The concept

Generative models are fluent, and fluency reads as competence. A user who gets three good answers concludes the fourth will be good, because nothing in the interface says otherwise. The model cannot correct this — it does not know what it does not know, and it will produce a confident wrong answer at the same tone as a confident right one. The organisation has to supply the missing signal.

That is why this bullet sits under "trustworthy" rather than "clear": the purpose is not politeness, it is calibration. A user who knows the failure mode checks the output; a user who does not, ships it. Under-claiming is therefore a strategy, not modesty — a named limitation turns an eventual failure into an expected one, and an expected failure costs a correction rather than a relationship.

The second idea is the trust ledger. Trust accumulates slowly through accurate expectations and is spent in a single oversold feature. Teams that oversell to win adoption typically win the pilot and lose the renewal, because the first bad output arrives before the habit forms.

### The sub-concepts

**Disclosure.** The plainest layer: does the user know a machine is answering, and does the person subject to an automated decision know it? Several regimes now require this outright, and it is the cheapest of the four layers to get right.

**The capability note.** A short, honest statement of purpose, strengths, failure shape and required human step. Three to six lines, written for the person using the tool, not for the auditor. This is the artefact most teams are missing.

**The model card or system card.** Documentation of the underlying model: training data summary, evaluated capabilities, known limitations, intended and prohibited uses. Necessary, and insufficient — it describes the base model, not your retrieval corpus, your prompt, or your escalation rules.

**Limit shape beats limit rate.** "Sometimes inaccurate" is useless. "When asked about case law it will invent plausible citations" is actionable, because the user can act on the shape. Where you have measurements, give them; where you do not, describe the shape honestly.

**Limits are versioned.** Swap the model, refresh the corpus, change the system prompt, and the limits move. A capability note without a date and a version is a claim about a system that no longer exists.

**An escalation path is part of the honesty.** Telling someone the tool is unreliable without telling them what to do instead is just anxiety. Every limitation should carry the next step: verify against the source, route to a human, or refuse the task.

### How it connects to the rest of the framework

`TSC8-Intermediate-K1` names transparency as one of four considerations; this bullet is its communication half. `TSC8-Intermediate-K5` supplies the legal duties that make disclosure mandatory rather than merely wise. `TSC8-Intermediate-A9` is where a learner actually does this — raising the limit in front of a manager who would rather not. Upstream, `TSC1-Basic-K6` covers what the model cannot do reliably, which is the raw material for every capability note.

### What is current as of November 2026

Every serious provider now ships a per-release system card — the GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon all publish evaluated capabilities and known limitations. That has raised the baseline: enterprise procurement now asks for these documents, and a vendor who cannot produce one is treated as a risk.

Two shifts complicate the work. Agentic products require a second kind of statement — not only "what it can say" but "what it may do", including which tools it can call and what it can change without approval. And disclosure has become a legal obligation in several jurisdictions, including transparency duties for generative systems under the EU AI Act and Singapore's guidance that people be told in plain language when AI is used in a decision about them.

### Common misconceptions

- *"It is in the terms and conditions."* Terms are a legal instrument; notice is a communication. A clause nobody reads does not calibrate anybody.
- *"Users do not read the warnings anyway."* Professionals do, and the ones who do not are exactly the ones who will paste the output straight into a client email.
- *"Admitting limits will kill adoption."* Overselling kills retention. The failure arrives either way; the only variable is whether you warned.
- *"Our vendor's model card covers us."* It covers the base model. Your corpus, your prompt and your workflow are undocumented until you document them.
- *"Ninety-five percent accuracy is a limit statement."* It is an average. It says nothing about which five percent, or whether they cluster in one group or one use case.

## How a student should understand it

**Mental model:** the weight limit sign in a lift. It is not an admission that the lift is bad; it is the reason the lift can be used confidently, and the reason nobody is surprised when it stops at thirteen.

**Things they can do after this bullet:**
1. Write a three-line capability note that names a real failure shape and the human step that covers it.
2. Read a test log and describe how the model fails, not just how often.
3. Add the verification step to the workflow, so the note describes something true.

**Misconceptions to kill:** that terms and conditions count as notice, that limits are bad for adoption, and that the vendor's card documents your system.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The lift capacity sign.** Thirteen persons, stated at the door, before you are inside. Compliance is not the point; predictability is. Where it breaks: a lift's capacity is fixed for its life, whereas a model's limits change with the next version, so your sign needs a date on it.

**The zi char stall's chilli warning.** "Very spicy — not for everyone" does not lose the customer; it prevents the customer from blaming the stall. Where it breaks: chilli tolerance is personal and stable, whereas model failure is invisible until it happens.

### Worked example with a real tool

```text
Write a capability note for a chatbot that summarises internal policy documents.
It is accurate on content that exists in the documents and shaky when asked to
compare two versions or to state what the policy does not cover.

Constraints: maximum 80 words, plain English, no marketing adjectives, and it must
end with the one action the reader should always take.
```

What to point at afterwards: the model will produce something like "may occasionally be inaccurate" unless the constraint forces specificity. Ask it to rewrite naming the exact failure shape, and then ask what evidence would justify the claim — which is the conversation that reveals nobody has measured it yet.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show marketing copy beside the failure log for the same tool.
2. **State the objective** — by the end you can write a capability note a user can act on.
3. **Recall prior learning** — ask about a product that overpromised to them; what did they do next.
4. **Present the content** — the three audiences, the four layers, limit shape versus limit rate.
5. **Guide** — draft the summariser note together on screen.
6. **Elicit performance** — each learner writes a note for a tool they own.
7. **Give feedback** — swap notes; mark any sentence the reader could not act on.
8. **Transfer** — attach the note to the actual release checklist.

## What the framework doesn't mention but trainers need to know

- **Marketing ownership destroys the artefact.** If communications writes the note, it becomes a promise. The people who know the failure modes must write the limits, and communications may only shorten them.
- **Test the note on a real user.** Read it aloud to someone outside the team; if they cannot restate the limitation, it failed regardless of its accuracy.
- **The limit that matters most is often unmeasured.** Teams document what they tested, not what worries them. Ask what they would test with another two weeks.
- **Agents need action limits.** For an agent, "what can it do without asking" belongs in the note alongside accuracy.

## Watch out

- **Do not let "may hallucinate" be the whole note.** Every model does; the useful information is where and how.
- **Do not promise a fix date** unless engineering has committed to it in writing.
- **Do not let legal turn the note into boilerplate.** A note nobody finishes reading is a note nobody is calibrated by.
- **The stale claim to retire:** "we will disclose limits at onboarding." Onboarding is forgotten in a week; the limit belongs at the point of use.
