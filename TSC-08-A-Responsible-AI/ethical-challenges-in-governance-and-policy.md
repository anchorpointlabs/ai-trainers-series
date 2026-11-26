---
id: 08.03.A.K3
tsc: 8
level: Advanced
code: K3
title: Ethical challenges in governance and policy
as_at: 2026-11-26
review_by: 2027-02-25
---

# Ethical challenges in governance and policy

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Knowledge K3**

> **Framework text (verbatim):** "Ethical challenges in AI governance, policy-making, and global implications."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Knowledge · Bullet 3 of 14

**One-line version:** The model is global, the rules are local, and nobody owns the border.

## What it is

Governing AI means governing something that crosses jurisdictions faster than legislation can follow. A model trained in one country is deployed through a cloud region in a second, sold to a customer in a third and used by people in a fourth. The ethical challenges are not only "what is the right rule" but "whose rule applies, who can enforce it, and what happens where no rule reaches". Policy-makers are also choosing between two failure modes: rules so vague they cannot be applied, and rules so prescriptive they freeze the technology they were meant to steer.

## Deep expansion

### The concept

Three fault lines run through every cross-border governance discussion.

**Scope.** The EU AI Act follows the output: if a system's output is used in the EU market, the obligations travel with it, regardless of where the company or its servers sit. Singapore's PDPA governs personal data collected and used here, with its own rules on transferring data out. China's generative-AI measures apply to public-facing services offered to its users and require filing and security assessment before launch. None of these three is a global rule; together they cover most of the market a Singapore firm sells into.

**Enforcement.** A statute is only as strong as its inspectorate. The EU has a regulator, an enforcement calendar and turnover-based penalties. Singapore's horizontal AI framework is voluntary, with hard enforcement arriving through adjacent statutes — PDPA fines, MAS supervisory action, HSA device rules, POFMA and OCHA for online harms. ASEAN has guidance and no court. A learner who assumes "there is a law, therefore it is enforced" has misread the map.

**Values.** Jurisdictions disagree about what the underlying good is: autonomy and redress in the EU, communal harmony and social cohesion in Singapore, social stability and content control in China, innovation and free expression in the US federal posture. A vendor optimising for one gets accused by another of the opposite failure.

### The sub-concepts

**The value chain is the enforcement problem.** Responsibility is divided between model developer, deployer and cloud host, but harm lands on the person at the end. A deployer who cannot see inside the weights cannot prove the model was fair; a developer who never sees the use case cannot know it was misused. Regulators increasingly place the duty on the deployer because that is where the customer relationship lives — which is also where the least information sits.

**Fragmentation has a cost that falls on SMEs.** Compliance with three regimes means three impact assessments and three evidence packs. Larger firms absorb it; smaller ones either withdraw from markets or quietly ignore the strictest rule.

**Regulatory arbitrage is real but shallow.** Training in a permissive jurisdiction and deploying in a strict one does not escape the strict one's deployer obligations, and the commercial customer often imposes its own contract terms on top.

**Policy gaps concentrate where technology is newest.** Agents that execute transactions, synthetic media in elections, and model weights released openly all sit in spaces where the rules were written for a different shape of system.

### How it connects to the rest of the framework

`TSC8-Advanced-K1` names the standards; this bullet is what happens when they overlap and conflict. `TSC8-Advanced-A6` is the critique skill that turns this knowledge into an argument about a specific policy; `TSC8-Advanced-A5` is the dilemma analysis when both sides are defensible; `TSC8-Advanced-A8` is the interdisciplinary response, because no single regulator can close a gap alone.

### What is current as of November 2026

The EU AI Act's general-purpose model obligations now bite on providers whose systems are placed on the EU market, with systemic-risk thresholds triggering red-teaming and incident reporting — and enforcement attention shifting from paper compliance to incident handling. ASEAN's expanded guide on generative AI keeps the region's interoperability bet alive: voluntary national adoption, risk-tiered assessment, no shared court. Singapore's posture remains sectoral plus baseline, with the IMDA generative framework, AI Verify and Project Moonshot as the practical instruments, and PDPC advisory guidance giving the deployer responsibilities teeth. Meanwhile the systems being deployed are increasingly agentic, and no jurisdiction has settled rules for an agent that transacts.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"One country's rules apply everywhere."* Scope is territorial, output-based or market-based, and each jurisdiction defines it differently.
- *"If it is legal here, it is fine there."* Lawfulness is local; liability travels with the customer relationship and the contract.
- *"Voluntary means unenforced."* Voluntary frameworks are read as evidence of reasonableness inside statutory regimes with real penalties.
- *"Global standards mean a global rule."* Standards harmonise vocabulary and audit method, not obligations or enforcement.

## How a student should understand it

**Mental model:** one car driving from Singapore into Malaysia and Thailand. The car does not change; the highway code, the speed limit and the checkpoint do. Enforcement happens at the border, and the border is where the argument starts.

**Things they can do after this bullet:**
1. Name three cross-border governance questions for any deployment.
2. Explain why a voluntary framework can still carry consequences.
3. Identify where a policy gap sits for a new capability.

**Misconceptions to kill:** that rules travel with the model, that legality equals ethics, and that fragmentation is someone else's problem.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The same car, three highway codes.** You drive the same vehicle from Woodlands to Johor to Bangkok; the vehicle is compliant everywhere, the rules are not. Where it breaks: a car is inspected at the checkpoint, whereas data and model outputs cross borders without stopping.

**Three hawker licences for one recipe.** The same dish needs a different licence, different hygiene inspection and different labelling in each country, and the strictest market's requirements end up shaping the recipe for all of them. That is the Brussels effect in one sentence. Where it breaks: food standards are harmonised by trade agreements; AI rules largely are not.

### Worked example with a real tool

```
A model is trained in the US, deployed by a Singapore company, and used by
customers in Singapore and the EU. Name the three governance questions that
arise, the specific rule that answers each, and the one question none of the
rules answers cleanly.
```

What to point at: the answers converge on (1) which regime applies to the output, (2) where the personal data flows and on what basis, and (3) who is accountable when the vendor, the deployer and the cloud host all point at each other. The unresolved question is nearly always the third. Ask the room who they would name in an incident report — the silence is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a product page listing three compliance badges from three jurisdictions. Ask which one an incident would be judged under.
2. **State the objective** — name the three fault lines and apply them to one deployment.
3. **Recall prior learning** — the layer model from `TSC8-Advanced-K1`.
4. **Present the content** — scope, enforcement, values, with one named instrument each.
5. **Guide** — work the US-trained model example on the board.
6. **Elicit performance** — groups take a product they know and map its three questions.
7. **Give feedback** — correct scope assumptions and conflations of voluntary with unenforced.
8. **Transfer** — each learner writes the one-line answer to "who is accountable" for their own deployment.

## What the framework doesn't mention but trainers need to know

- **Enforcement capacity is the weak link everywhere.** Even strict regimes audit a small fraction of systems; disclosure and incident reporting do more work than inspection.
- **Regulators cooperate informally.** Cross-border MoUs and supervisory colleges exist and matter more than the public treaty landscape suggests.
- **SMEs carry disproportionate cost.** Any policy critique that ignores compliance cost will be dismissed by half the room.
- **"Global implications" is not only about law.** It includes labour displacement in outsourced data work, compute concentration and language coverage — none of which any statute currently prices.

## Watch out

- **Do not reduce the world to "EU strict, US loose".** Singapore's model is neither, and it is the one most learners will operate under.
- **Do not skip transfer rules.** Cross-border data flow is usually the first real legal question a Singapore project hits.
- **Do not imply harmonisation is coming soon.** Plan for fragmentation and price it in.
- **The stale claim to retire:** "AI has no borders, so law cannot reach it." Deployer obligations reach it very effectively.
