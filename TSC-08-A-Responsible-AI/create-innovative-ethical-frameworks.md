---
id: 08.03.A.A9
tsc: 8
level: Advanced
code: A9
title: Create innovative ethical frameworks
as_at: 2026-11-26
review_by: 2027-02-25
---

# Create innovative ethical frameworks

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A9**

> **Framework text (verbatim):** "Create innovative ethical frameworks and guidelines for emerging AI domains."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 13 of 14

**One-line version:** New domains rarely need new principles; they need the old principles turned into rules a system can be tested against.

## What it is

Creating a framework for an emerging domain means finding the assumption the existing framework makes that is no longer true, extending the principle that still applies, and writing rules concrete enough to be built, tested and enforced. Agents that spend money, synthetic media that is indistinguishable from record, and embodied systems that act in physical space all sit outside the documents written for a chatbot that returns text. The output is a short set of rules with triggers, thresholds, evidence and an owner — not a restatement of values.

## Deep expansion

### The concept

Begin with a gap analysis in one sentence: *what did the old framework assume about the world that has changed?* For content systems, the assumption was that generation was hard and distribution was easy. For agents, it is that a human reads the output before anything happens. For embodied systems, it is that consequences are reversible.

Then extend rather than invent. Almost every new domain is governed adequately by existing principles — human oversight, transparency, accountability, proportionality, contestability — and badly by existing rules. The creative work is in the translation from principle to rule:

- **Trigger.** What event invokes the rule? An agent attempting a transaction above a value; a system generating a likeness of a real person; a model acting without a human in the loop for more than N steps.
- **Threshold.** What quantity makes it bite? Value, duration, autonomy level, number of people affected.
- **Evidence.** What must exist to show compliance? A confirmation log, a signed manifest, a recorded override.
- **Exception path.** When may it be exceeded, by whom, with what record.
- **Owner and review date.** Who answers when it fails, and when is it revisited.

A rule with all five is a framework. A rule with only the first two is a slogan with a number in it.

### The sub-concepts

**Innovation is not novelty.** A renamed version of an existing framework with new section headings adds nothing. The test is whether a developer could build to it and an auditor could check it.

**Design for the failure you can foresee, and instrument the rest.** Emerging domains have unknown failure modes, so the framework should mandate logging, incident reporting and a review cadence — the mechanism for learning, not a prediction of what will be learned.

**Proportionality by autonomy.** The same capability deserves different friction at different levels of autonomy: suggest, act with confirmation, act and report. Most agent frameworks collapse these into one and are therefore either too strict to use or too loose to matter.

**Participatory drafting.** Frameworks written only by the deploying organisation encode its interests. Community, worker and civil-society input changes the thresholds, not just the preamble.

**Sunset clauses.** An emerging-domain rule written in 2026 should expire or be reviewed, because the domain will have changed. Permanent rules written against moving technology become obstacles.

**Avoid ethics washing.** A framework whose only enforcement is a webpage is a marketing artefact; say so and build the enforcement or drop the claim.

### How it connects to the rest of the framework

`TSC8-Advanced-K1` supplies the principles being extended; `TSC8-Advanced-K3` shows why a national framework may not fit a cross-border product; `TSC8-Advanced-A6` is the critique method that tells you whether your draft survives contact with an auditor; `TSC8-Advanced-A1` is where the new rule becomes a gate; `TSC8-Advanced-A8` is the team that drafts it.

### What is current as of November 2026

The clearest gap is agency. Current frontier systems now call tools, hold credentials and complete transactions, and the frameworks in force were written for systems that produced text a human would read. Emerging practice clusters around a few rules: explicit confirmation above a value threshold, a hard cap on spend per session, a step limit on autonomous loops, a full action log, and a human route to reverse any completed action. Content provenance is the second gap: signed manifests and statistical watermarks exist, but stripping metadata is trivial, so labelling rules need a detection story as well as a labelling duty. Both areas are being governed by vendor policy and procurement terms before any statute arrives.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A new framework needs new principles."* Usually it needs new rules for old principles.
- *"Flexible means no rules."* A framework with no thresholds cannot be complied with or audited; it is ignored.
- *"The vendor's usage policy is our framework."* Their policy governs their product; your obligations govern your use.
- *"We will write it once the technology settles."* The rules shape the technology; waiting means inheriting someone else's defaults.

## How a student should understand it

**Mental model:** the rules for e-scooters. Existing traffic law assumed vehicles with number plates and drivers with licences; personal mobility devices fitted neither, so Singapore wrote speed limits, registration and footpath rules — old principles about safety, new rules for a new object.

**Things they can do after this bullet:**
1. Name the assumption an existing framework makes that a new domain breaks.
2. Write one rule with trigger, threshold, evidence, exception and owner.
3. Explain what makes a framework testable rather than aspirational.

**Misconceptions to kill:** new domain means new principles, flexibility means vagueness, and vendor policy is your framework.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**E-scooter rules.** The road code assumed cars and licences. PMDs arrived, the harm was on footpaths, and the response was specific: speed limits, registration, bans in certain places, enforcement by officers. Old principle, new rules, an inspector. Where it breaks: an e-scooter is visible and its speed is measurable; an agent's autonomy is not visible to a bystander.

**Insurance for a new risk.** The clause is written after the first loss, in language the underwriter can price. Good framework design writes the clause before the loss and prices the uncertainty explicitly. Where it breaks: insurers have actuarial data; emerging AI domains do not.

### Worked example with a real tool

```
Write one concrete ethical rule for AI agents that can spend money on a
user's behalf. Then write its test.
Include: trigger, threshold, required evidence, exception path, owner, review
date, and the exact check an auditor would run to prove compliance.
```

What to point at: models produce "agents must act in the user's best interest" and stop — a principle, not a rule. Push for the threshold: above what value? Then the evidence: what does the log contain? Then the exception: who can approve, and is that approval recorded? The class will notice that the hard part is the number, and the number is exactly what a framework must contain.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — an agent buys something the user did not intend. Ask which rule was broken; there is no rule yet.
2. **State the objective** — write one testable rule with all five components.
3. **Recall prior learning** — human oversight models, HITL and HOTL, from the principles block.
4. **Present the content** — gap analysis, principle extension, the five components.
5. **Guide** — draft the spending rule together, arguing about the threshold.
6. **Elicit performance** — groups write a rule for a different emerging domain (synthetic likeness, embodied robot, agent emailing clients).
7. **Give feedback** — test each rule by asking how an auditor would check it.
8. **Transfer** — each learner takes their rule to a policy owner and asks for a review date.

## What the framework doesn't mention but trainers need to know

- **Thresholds are the political fight.** Whoever sets the number decides how much autonomy is allowed, and it is usually set by the vendor's default.
- **Instrumentation beats prediction.** Mandate logs and incident reporting; you will not predict the failure mode.
- **Emerging-domain frameworks are usually written by the deployer.** That is convenient and self-serving; say so.
- **A rule with no exception path will be broken silently.** Design the exemption and its record.

## Watch out

- **Do not let the class write a charter.** Principles are the easy half; the rule is the deliverable.
- **Do not copy a framework between domains.** The assumptions differ, and the copied threshold will be wrong.
- **Do not skip the auditor test.** If you cannot describe the check, the rule does not exist.
- **The stale claim to retire:** "There are no rules for agents yet." There are vendor policies, procurement terms and draft standards; the gap is enforceable public rules.
