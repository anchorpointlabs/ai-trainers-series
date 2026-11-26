---
id: 08.03.A.A10
tsc: 8
level: Advanced
code: A10
title: Advocate for responsible AI development
as_at: 2026-11-26
review_by: 2027-02-25
---

# Advocate for responsible AI development

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A10**

> **Framework text (verbatim):** "Advocate for responsible and ethical development and use of generative AI technologies, including user privacy rights."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 14 of 14

**One-line version:** Advocacy is a risk, the evidence for it, and a path out — delivered to someone with the power to take the path.

## What it is

Advocacy at this level is organisational and public: making the case for privacy rights and responsible deployment to people who control budgets, roadmaps and release dates. It differs from complaint in three ways. It names a specific risk rather than a mood. It brings evidence — an incident, an audit finding, a test result, a cost. And it offers a path that the audience can actually take, with an owner and a date. Alarm without a path gets sympathy and no decision.

## Deep expansion

### The concept

Build the case in four moves.

**The risk, stated concretely.** Not "privacy is important" but "this feature will send customer NRIC numbers to an external API, and the vendor retains prompts for thirty days". A concrete risk can be argued with; a value cannot.

**The evidence.** Three kinds work: a near-miss or incident from your own organisation; a test result you ran, such as a red-team case that succeeded; and a comparable case from elsewhere — a regulator's finding, a tribunal ruling, a public breach. Evidence should be verifiable by the audience, which usually means a link, a log or a name.

**The cost of inaction.** State it in the audience's currency. For a board, that is regulatory exposure, remediation cost and reputational damage. For engineering, it is rework and incident load. For a product owner, it is launch delay after the fact rather than before it.

**The path.** A specific proposal with an owner and a sequence: redact at the boundary, switch to zero-retention terms, add a confirmation step, run the adversarial suite before release. The path must be cheaper than the risk, or it will be rejected — which is why advocacy includes designing the cheap version.

### The sub-concepts

**Know your audience.** A board responds to risk appetite and liability; a CTO to feasibility and schedule; a customer to assurance and control; a regulator to evidence of reasonableness. The same case is re-cut for each, not repeated louder.

**Credibility is the asset.** One overclaim — "this will definitely cause a breach" — costs the next ten accurate warnings. Say what you know, what you estimate, and what you do not know.

**Privacy rights as the concrete case.** Users have rights to be informed, to access, to correct, and increasingly to a human review of automated decisions. Advocacy for these is easiest when framed as a service commitment rather than a legal argument: tell people what happens to their data, and give them a route when it goes wrong.

**Coalition, not martyrdom.** Find the security team, the DPO, the customer-facing lead with complaints on file. A case with three internal sponsors is a decision; a case with one is a memo.

**Escalation is part of the toolkit.** When internal channels fail and harm is imminent, the routes are the DPO, internal audit, a regulator, or disclosure. Know them before you need them, and know the consequences.

**Follow through.** Advocacy ends when the control is in the build and monitored, not when the meeting ends.

### How it connects to the rest of the framework

`TSC8-Advanced-A1` is the gate where the advocated control lands; `TSC8-Advanced-A3` supplies the evidence a red-team finding provides; `TSC8-Advanced-A4` is the technical answer to a privacy risk you are advocating for; `TSC8-Advanced-A6` is how to argue about the policy itself; `TSC8-Advanced-K1` gives you the standards to cite instead of opinion.

### What is current as of November 2026

The advocacy climate has hardened in a useful way. "Responsible AI" claims are now checked: buyers ask for model cards and evaluation results, and the EU AI Act's transparency and high-risk obligations give an advocate a citation rather than a preference. Agentic features have created the sharpest privacy case in years — an assistant with tool access can move data to places no privacy review covered — and the vendors behind those capabilities, OpenAI's GPT-6 generation, Anthropic's Claude 5.5 and Google's Gemini 3.1 Pro and 4 Argon, publish retention and training-use terms that an advocate can quote precisely. In Singapore, PDPC guidance on AI recommendation and decision systems gives the privacy argument a local statutory anchor instead of a foreign one.

### Common misconceptions

- *"Advocacy means warning loudly."* Warning without a path is noise; the path is the work.
- *"The facts speak for themselves."* Facts are ignored daily; they need an audience, a currency and a proposal.
- *"Someone else owns this."* The person who noticed is the person who can raise it; that is the whole duty.
- *"One memo settles it."* Advocacy is a sequence: case, pilot, control, monitoring, review.

## How a student should understand it

**Mental model:** the colleague who reports a leak with a plumber's quote, not the one who shouts that the ceiling is wet.

**Things they can do after this bullet:**
1. Write a two-sentence advocacy statement with a risk, evidence and a path.
2. Re-cut the same case for a board and for an engineering lead.
3. Name the escalation route before it is needed.

**Misconceptions to kill:** advocacy equals alarm, evidence speaks for itself, and the responsibility belongs to someone more senior.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The safety officer with the near-miss report.** The effective one brings the incident, the cause, the fix and the cost of the fix; the ineffective one brings a reminder that safety matters. Both care equally; only one changes the schedule. Where it breaks: a factory near-miss is visible and physical, while a privacy near-miss is an absence nobody notices.

**The lift maintenance sticker again.** Advocacy is asking for the sticker: a named inspector, a date, a next-due date. It converts a value into a control. Where it breaks: you can see a lift certificate; you cannot see whether prompts were retained.

### Worked example with a real tool

```
Draft a two-sentence advocacy statement for user privacy in a new AI
feature, with evidence and a path. Then give me a five-slide outline of the
same case for a sceptical CFO, a CTO and a customer.
```

What to point at: the two-sentence version is easy and the five-slide version is where the skill lives. Look at slide three — the cost of inaction. Groups reliably write "reputational damage" and stop. Push for a number they can defend and a source they can cite. Then look at the path slide: if it costs more than the risk, the CFO will defer it, and the advocate has lost without an argument.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two emails about the same risk: one alarm, one case with a fix and a price. Ask which gets a meeting.
2. **State the objective** — produce a case with risk, evidence, cost and path for a named audience.
3. **Recall prior learning** — privacy techniques from `TSC8-Advanced-A4`; gates from `TSC8-Advanced-A1`.
4. **Present the content** — the four moves, the audience map, credibility.
5. **Guide** — draft the two-sentence statement together, then expand one.
6. **Elicit performance** — pairs write the five-slide case for their own organisation.
7. **Give feedback** — strike out any claim without evidence and any path without an owner.
8. **Transfer** — each learner books the meeting and sends the case within two weeks.

## What the framework doesn't mention but trainers need to know

- **Advocates need a cost estimate.** Without one, the proposal is a preference; with one, it is a decision.
- **The DPO is an ally, not a gatekeeper.** Bring them in early and the case gets stronger and cheaper.
- **Internal reputation compounds.** The person who is right twice gets listened to on the third.
- **Some advocacy fails, and that is information.** Record the refusal and the reason; it becomes the post-incident evidence.

## Watch out

- **Do not teach advocacy as public speaking.** It is evidence design and audience mapping.
- **Do not let learners overclaim risk.** "Will" instead of "could" destroys credibility in one sentence.
- **Do not skip the follow-through.** An unmonitored control is an unkept promise.
- **The stale claim to retire:** "We raised it with management." Raising is the first step; a control with an owner and a date is the last.
