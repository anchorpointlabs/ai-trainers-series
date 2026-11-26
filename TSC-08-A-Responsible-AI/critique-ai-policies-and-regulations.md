---
id: 08.03.A.A6
tsc: 8
level: Advanced
code: A6
title: Critique AI policies and regulations
---

# Critique AI policies and regulations

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A6**

> **Framework text (verbatim):** "Critique AI policies, regulations, and ethical guidelines."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 10 of 14

**One-line version:** A policy is good if a stranger could comply with it, an inspector could catch a breach, and a victim could point to the rule that failed them.

## What it is

Critiquing a policy means testing whether it does what it claims, not whether you agree with its tone. Four tests do most of the work: is it clear about who must do what, when and to what standard; is it enforceable, with detection, penalty and capacity; does it cover the risks and actors that matter; and does it have an owner and a review date. A critique that does not end in a specific amendment is a complaint.

## Deep expansion

### The concept

Read any AI policy and mark every sentence with one of three labels: **obligation** (someone must do something), **aspiration** (someone hopes something), **decoration** (someone likes the sound of it). Most published policies are 10 percent obligation and 90 percent aspiration. That ratio is the first finding.

Then run the four tests.

**Clarity.** Who is the duty holder — developer, deployer, vendor, user? What triggers the duty? What standard must be met, and how would a court or regulator know it was met? "Appropriate safeguards" fails all three. "A documented impact assessment, reviewed by a person independent of the build team, before first production use" passes.

**Enforceability.** Is there a detection mechanism — audit, logging, incident reporting, whistleblower channel? Is there a consequence — fine, licence condition, market exclusion, contract? Is there capacity — does anyone inspect? A rule with no inspector is a norm, not a regulation, and should be described as one.

**Coverage.** Which harms are addressed, and which are absent? Common gaps: downstream use by third parties, open-weight release, procurement, workplace monitoring, content moderation labour, environmental cost, and systems that act rather than advise.

**Ownership and revision.** A named owner inside the organisation, and a review date. Policies without dates rot silently.

Two failure modes are worth teaching as a pair. **Vagueness** produces a document everyone can sign and no one can be held to. **Over-prescription** produces rules that are already obsolete — specifying a technique rather than an outcome, so compliance means using last year's method. The craft is prescribing outcomes with evidence, not methods.

### The sub-concepts

**Voluntary versus statutory.** Singapore's IMDA framework is voluntary and the PDPA is not; a critique should name which it is critiquing and what consequence attaches. Voluntary frameworks are read as evidence of reasonableness — weaker than law, stronger than nothing.

**Instrument choice.** Bans, licensing, disclosure, audit mandates, liability rules, procurement conditions and standards each fail differently. A ban is clear and blunt; disclosure is cheap and easily ignored; liability is slow but changes behaviour upstream.

**Proportionality.** Friction must match risk. A rule that requires a full audit for an internal meeting summariser will be routed around, and the routing-around will spread to the high-risk cases.

**The evidence base.** Regulations are usually written after an incident. Ask which incident, and whether the rule would have prevented it, or only the last one.

**The improvement.** Every critique must propose an amendment: a clause, an owner, a metric, a date.

### How it connects to the rest of the framework

`TSC8-Advanced-K1` gives you the instruments being critiqued; `TSC8-Advanced-K3` explains why a rule that works in one jurisdiction fails in another; `TSC8-Advanced-A5` supplies the dilemma analysis when a rule trades one good for another; `TSC8-Advanced-A1` is where the critique lands as a gate requirement; `TSC8-Advanced-A9` is where you write the missing rule.

### What is current as of November 2026

The critique landscape has shifted from "should there be rules" to "these rules do not fit the systems". The EU AI Act's high-risk obligations are being applied through guidance and standards that are still maturing, so much of today's critique is about implementing acts rather than the statute. Singapore's model — voluntary horizontal framework plus statutory teeth in PDPA, MAS, HSA and online-safety law — is increasingly cited as the pragmatic alternative to omnibus legislation, and it deserves critique on its own terms: it depends on regulators reading frameworks as evidence, which is a softer chain than a statutory duty. The clearest gap everywhere is agentic systems: a rule written for a chatbot that answers does not govern an assistant that transacts, and the providers shipping those systems — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and 4 Argon — are setting de facto norms faster than any legislature.

### Common misconceptions

- *"Critique means I do not like it."* Critique means it fails a test, and here is the amendment.
- *"If it is law, it works."* Enforcement capacity decides; many statutes are unenforced.
- *"More rules mean better governance."* Over-prescription gets routed around and discredits the whole framework.
- *"Singapore has no AI law, so nothing applies."* The PDPA, MAS rules, HSA device regulation and online-safety statutes all bite.

## How a student should understand it

**Mental model:** the lift certificate. It is enforceable because there is a sticker with an inspector's name, a date and a next-due date. A policy with no sticker is a poster.

**Things they can do after this bullet:**
1. Label every clause obligation, aspiration or decoration.
2. Run the four tests and name the weakest link.
3. Draft one amendment with an owner, a metric and a date.

**Misconceptions to kill:** critique equals taste, law equals enforcement, and more rules equals better.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**"Please drive carefully" versus "speed camera at this junction".** Both express a wish about driving; only one changes behaviour, and only because detection, penalty and capacity exist. Where it breaks: traffic enforcement is cheap and automatic; AI audits are expensive and manual, which is why disclosure and incident reporting do more work than inspection.

**The lift certificate.** Stuck inside the lift, dated, signed, with a next inspection due. Nobody reads it until the lift stops — then it is the only thing that matters. Where it breaks: lifts fail visibly; a biased model keeps working.

### Worked example with a real tool

```
Critique this policy line: "AI use should be ethical and responsible at
all times." Then rewrite it.
Give me: (1) the clauses that are obligation, aspiration or decoration,
(2) which of the four tests it fails and why, (3) a rewritten clause with a
duty holder, a trigger, a standard, a consequence and a review date.
```

What to point at: the rewrite is the deliverable, and models will produce a decent one — then ask the class to weaken it back to what their organisation would actually pass. That negotiation, between what is right and what is signable, is the real skill, and it is invisible in a policy library.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two policy extracts: one vague, one enforceable. Ask which would survive an incident.
2. **State the objective** — run four tests and produce one amendment.
3. **Recall prior learning** — the standards from `TSC8-Advanced-K1`, the enforcement gap from `TSC8-Advanced-K3`.
4. **Present the content** — obligations versus aspirations, the four tests, the two failure modes.
5. **Guide** — critique the "ethical at all times" line together.
6. **Elicit performance** — groups critique a real policy from their own sector.
7. **Give feedback** — strike out critiques that do not propose a clause.
8. **Transfer** — each learner submits one amendment to a policy they are actually bound by.

## What the framework doesn't mention but trainers need to know

- **Most AI policy in Singapore is procurement policy.** The contract clause is where requirements become real.
- **Frameworks are read as evidence.** In the absence of an AI statute, following IMDA guidance is how an organisation shows reasonableness after a breach.
- **Regulators are under-resourced.** Assume low inspection capacity and design for self-reporting and disclosure.
- **Language matters more than length.** A rule a busy manager cannot restate from memory will not be followed.

## Watch out

- **Do not critique tone.** "It sounds corporate" is not a finding.
- **Do not confuse a standard with a law.** Say which one you are testing.
- **Do not propose rules you cannot imagine enforcing.** That is how policy libraries fill with decoration.
- **The stale claim to retire:** "Ethics guidelines are enough." They are the preamble; obligations are the policy.
