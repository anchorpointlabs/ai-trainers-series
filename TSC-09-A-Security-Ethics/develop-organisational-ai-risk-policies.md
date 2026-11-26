---
id: 09.03.A.A5
tsc: 9
level: Advanced
code: A5
title: Develop organisational AI risk policies
---

# Develop organisational AI risk policies

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A5**

> **Framework text (verbatim):** "Develop organisational AI risk management policies."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Ability · Bullet 11 of 12

**One-line version:** A policy is the sentence an organisation can point to after something goes wrong — so it must say who may do what, who decides, and what happens when they do not.

## What it is

An AI risk policy converts individual judgement into an organisational standard: what is permitted, what requires approval, who is accountable, what evidence must exist, and how the rule is enforced. It is written so that two employees in different departments reach the same decision on the same question, and so an auditor or a regulator can check whether the organisation did what it said.

## Deep expansion

### The concept

The reason policies exist is not bureaucracy; it is variance. Without a written rule, the answer to "may I paste a client contract into a public chatbot" depends on which manager is asked, what day it is, and how much deadline pressure exists. Variance of that kind is invisible until it produces an incident, and then it is indefensible, because the organisation cannot show that it had a position at all.

A usable policy has five properties, and most bad policies are missing two of them:

- **Scope** — which people, which tools, which data, which activities.
- **Decision rules** — prohibited, permitted, permitted with approval. Naming the middle tier is what makes the policy practical; a binary allow/ban forces everything ambiguous into a grey zone.
- **Accountability** — a named role, not a committee, for each class of decision.
- **Evidence** — what must exist to prove compliance: an approval record, a log, a completed assessment.
- **Enforcement** — how the rule is checked, by whom, and with what consequence.

Policies also have to be *readable*. A twenty-page document that no engineer opens is not a control; a two-page rule with three worked examples and a one-line escalation path changes behaviour. The test of a policy is whether a new joiner can apply it without asking.

### The sub-concepts

**The five policies a mature organisation needs.** They are distinct and they are usually conflated:

1. **Acceptable use** — which tools employees may use, what data may go in, what must be checked before output is used, what is prohibited outright (pasting personal data into consumer tools, automated meeting transcription without consent).
2. **Risk classification and lifecycle** — how a project is tiered, and which artefacts each tier requires at each gate.
3. **Data governance and provenance** — how training and retrieval data is acquired, what consent or exception applies, how personal data is redacted, what copyright boundaries hold.
4. **Vendor and procurement** — the clauses required before buying anything with a model inside it: no training on your data, notification when the underlying model changes, breach notification, audit rights, indemnity.
5. **Incident response and decommissioning** — severity levels, who declares an incident, how the system is stopped, who is notified, how long logs are kept.

**The prohibited list earns its place.** A short list of things the organisation will not do — social scoring of individuals, emotion inference in hiring, non-consensual synthetic media, unapproved autonomous financial actions — does more work than a long list of aspirations.

**Approval thresholds, not approval moods.** "Customer-facing systems require sign-off by the risk owner" is enforceable. "Significant AI use needs review" is not, because significance is decided by the person seeking approval.

**The exception path.** Real policies need a documented way to say yes to a case the rule did not anticipate, with a named approver and an expiry date. Without it, people route around the policy and the policy loses authority.

**Review and versioning.** Models, tools and law change; a policy with no review date is a historical document. Version numbers and a change log make the policy auditable.

### How it connects to the rest of the framework

K5 sets the appetite the policy encodes; a policy with no appetite behind it is a preference. A6 designs the gates where the policy is applied. A3 operates the moderation policy this suite supports. K1 and K3 supply the technical standards a policy can cite — "approved guardrail configuration" means something only if the configuration is defined somewhere. At Intermediate level, `09.02.I.K4` covers risk frameworks and trust-and-safety practice.

### What is current as of November 2026

- **Shadow AI is the enforcement problem.** Employees use consumer assistants on personal devices; a policy that only bans drives usage underground. The workable pattern is a sanctioned internal tool with zero data retention plus network-level controls on uploads to unsanctioned services.
- **Vendor clauses are the new due diligence.** Providers now change model versions on their own schedule, so notice periods, version pinning and no-training-on-your-data terms are policy requirements rather than legal niceties.
- **Disclosure duties are explicit.** Policies increasingly require telling users when they are dealing with an AI and when content is synthetic.
- **Sector regulators read your policy.** Where a supervisor or data-protection authority asks what the organisation's position was, the written policy and its approval records are the answer.

### Common misconceptions

- *"A policy is a ban."* A policy is a decision structure. Bans without a permitted path produce shadow use.
- *"Policy is legal's job."* Legal supplies constraints; the operating rules come from the people who run the work.
- *"We sent an email, so we have a policy."* An email is not versioned, not scoped, not enforced and not evidence.
- *"If it is not in the policy, it is allowed."* Silence in a policy is a gap, and gaps get read whichever way suits the reader.

## How a student should understand it

**Mental model:** the workplace safety rulebook — short, posted, drilled, and cited in the incident report. Nobody thinks it exists to slow the work down; it exists because the alternative is a site where nobody agrees what safe means.

**Things they can do after this bullet:**
1. Draft one clause with scope, rule, accountability and evidence.
2. Place a scenario into prohibited, approval-required or permitted.
3. Name how the clause would be checked, and by whom.

**Misconceptions to kill:** that policy equals prohibition, that legal owns it alone, and that a circulated email counts.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Cash-handling limits at a bank branch.** A teller may approve up to a stated amount, above which a supervisor signs. The rule is written, the threshold is a number, the approval is recorded, and the audit checks the records. Nobody argues that the limit insults the teller's judgement. Where it breaks: cash is countable and AI risk is not, so the AI version of the limit is a risk tier rather than a dollar amount.

**The workplace safety file.** Every site has one, it is inspected, and after an incident the first question is what the file said. A policy is that file for AI.

### Worked example with a real tool

```
You are the head of risk for a 600-person professional-services firm in Singapore.
Staff are pasting client documents into consumer chatbots.

Draft one policy clause, in this structure:
1. Scope — who and what it covers.
2. Rule — prohibited / permitted with approval / permitted, stated as a test a
   person can apply in ten seconds.
3. Accountability — the role that approves exceptions, and the role that owns the
   clause.
4. Evidence — what record proves compliance.
5. Enforcement — how it is checked, how often, and what happens on a breach.
6. The one exception you would allow, and its expiry.

Then rewrite the clause for a reader who has ninety seconds.
```

What to point at afterwards: step two. Learners write rules that sound right and cannot be applied — "confidential information must not be shared externally" fails on the first shared screen. The workable version names categories: personal data, client-identifiable material, unpublished financials, source code. Then point at step six: an exception with an expiry is what keeps the rule credible.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — three employees, three different answers to the same question.
2. **State the objective** — write one enforceable clause with all five properties.
3. **Recall prior learning** — a policy at work they have actually used, and one they ignored.
4. **Present the content** — the five properties and the five-policy suite.
5. **Guide** — draft the prohibited tier for the firm together.
6. **Elicit performance** — pairs write the clause and the exception.
7. **Give feedback** — apply the ten-second test to each clause.
8. **Transfer** — each learner drafts the clause their organisation most needs.

## What the framework doesn't mention but trainers need to know

- **A policy you cannot enforce teaches contempt.** Check the evidence requirement is collectable before publishing the rule.
- **Policies conflict.** The AI acceptable-use policy, the data-protection policy and the procurement policy will disagree; reconcile them or staff will cite the one that suits.
- **Make the safe path faster than the unsafe one.** Approval in a day beats a ban in a quarter.
- **Localisation is not cosmetic.** Consent norms, PDPA obligations, and multilingual staff mean the examples have to be local to be recognised.
- **Publish the prohibited list internally.** People cannot comply with rules they cannot read.

## Watch out

- **Do not present the policy as a legal shield.** It is evidence of intent; it does not transfer liability away.
- **Do not write clauses with no role attached.** "The organisation must ensure" is nobody's job.
- **Do not confuse policy with procedure.** Policy says what; the SOP says how. Both are needed, and mixing them makes both unusable.
- **The stale claim to retire:** "we banned ChatGPT, so we are covered." As of November 2026 the exposure is shadow use and vendor model changes, neither of which a ban addresses.
