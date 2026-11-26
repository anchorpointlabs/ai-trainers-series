---
id: 08.01.B.A2
tsc: 8
level: Basic
code: A2
title: Compare ethical issues in AI applications
as_at: 2026-11-26
review_by: 2027-02-25
---

# Compare ethical issues in AI applications

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Ability A2**

> **Framework text (verbatim):** "Compare ethical issues in AI applications."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Ability · Bullet 6 of 10

**One-line version:** Ethical weight is not a property of the technology — it is a property of the decision the system touches, how bad the harm is, and whether the person harmed can get it undone.

## What it is

Comparing ethical issues means placing AI uses on a scale rather than treating them as uniformly risky or uniformly harmless. Three questions do most of the work: **how bad is the harm, can it be reversed, and who bears it?** Two supporting factors matter for AI specifically: how much the system decides on its own, and how many people it touches.

## Deep expansion

### The concept

Learners arrive with one of two failure modes. Either everything is terrifying ("AI will take over") or nothing is ("it's just a tool"). Both are comparisons that failed to happen.

The comparison matters because scrutiny is a finite resource. An organisation that applies the same review to an internal meeting-summariser as to a credit-scoring model will either paralyse itself or, more likely, quietly exempt everything and review nothing. Risk tiering is not bureaucratic tidiness; it is how the high-stakes cases get the attention they need.

The reframe that makes this click: you are not comparing *technologies*, you are comparing *decisions*. The same model, same vendor, same price, can be a low-risk use when it drafts an internal agenda and a high-risk use when it ranks redundancies. What changes is not the model. It is whose life the output moves.

### The sub-concepts

**Harm severity and probability.** The two axes of the IMDA matrix. A system that mislabels a photo of a cat is trivial; one that mislabels a patient's scan is not, even at the same error rate. Probability matters too — an error that occurs in one case in a thousand is a different governance problem from one that occurs in one case in three, even where the harm per case is identical.

**Reversibility.** Can the harm be undone? A wrong product recommendation is corrected by buying something else. A wrongly denied loan, a wrongly terminated employee, a wrongly flagged fraud suspect — these leave a record, a delay, sometimes a permanent mark. Irreversible harm earns a higher tier at lower probability, because there is no second chance to get it right.

**Who is affected, and whether they can refuse.** A tool used by staff on their own work is different from one applied to people who never chose it: applicants, patients, tenants, recipients of a benefit. The second group usually has no visibility, no consent and no leverage. The distillation's contestability principle is the test — if the affected person has no route to challenge the output, treat the use as higher risk than the harm estimate alone suggests.

**Allocative versus representational harm.** Allocative harm withholds something material: a job, a loan, a bed, an interview. Representational harm demeans or erases a group in language and imagery — the image generator that produces one demographic for "CEO" and another for "cleaner". Allocative harm is usually tiered higher because it is measurable and consequential; representational harm is easier to dismiss and harder to prove, which is why it needs naming.

**Autonomy and scale, the two AI-specific multipliers.** A system that advises a human sits lower than one that decides; a system that decides and acts — sending, paying, terminating — sits higher again, because the error lands before anyone can intercept. Scale multiplies everything: an error rate that is tolerable across 200 internal documents is not tolerable across 200,000 customer decisions.

**The four tiers.** The distillation's working scheme: **prohibited** (manipulation, social scoring, non-consensual deepfakes — do not build), **high risk** (consequential decisions about people: credit, employment, medical triage, education admission, essential services — conformity assessment, independent audit, human sign-off, continuous monitoring), **limited** (customer-facing chatbots, recommendation, support triage — disclosure, guardrails, sampling audits), **minimal** (internal productivity with human review — ordinary software controls). Learners should be able to place a use and name the *action* the tier requires, not just the label.

**Comparing two uses, not two systems.** When a learner says "which is more ethical, ChatGPT or Gemini", the question is malformed. The comparison is: which *use* carries more risk, and separately, which *provider* handles your data better (that is `TSC8-Basic-A3`).

### How it connects to the rest of the framework

`TSC8-Basic-A1` runs the four questions on a decision; this bullet decides how much depth that run deserves. `TSC8-Basic-K4` supplies the risk catalogue you are ranking. `TSC8-Basic-A3` is the provider comparison that people confuse with this one. `TSC8-Basic-A4` turns the tiers into a written rule about which uses need what.

### What is current as of November 2026

Tiering has become semi-formal, which helps and misleads. The EU AI Act's high-risk annex names the categories — biometrics, critical infrastructure, education, employment, essential services including credit and insurance, law enforcement, migration, justice — and Singapore's sector regulators (MAS for financial decisions, HSA for clinical software) impose their own gates. A learner who can map a use onto those categories can talk to a compliance team immediately.

The misleading part: frontier models from OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon all handle the same low-risk drafting task about equally well, so pilot comparisons between them say nothing about ethical weight. The weight comes from the deployment, not the model card.

### Common misconceptions

- *"All AI uses carry similar risk because it's the same technology."* The same model drafting an agenda and ranking redundancies are two different ethical objects.
- *"If the error rate is low, the risk is low."* Low-probability, irreversible harm still lands in a high tier.
- *"Internal tools are automatically low risk."* An internal tool that decides who gets promoted is not low risk.
- *"Bias is the only ethical issue."* Privacy, accountability, autonomy and reversibility all move the tier independently.
- *"Tiering is a compliance formality."* It is the mechanism that buys the high-risk case its review time.

## How a student should understand it

**Mental model:** A&E triage. A sprained ankle and a heart attack both arrive at the same department; they do not get the same team, the same monitors or the same urgency. Triage is not a judgement about the patient's worth — it is a judgement about what the condition needs.

**Things they can do after this bullet:**
1. Place two AI uses on the four tiers and name the action each tier requires.
2. Answer the three questions (harm, reversibility, who) for a use in their own work in under two minutes.
3. Explain why a low error rate does not lower the tier for irreversible harm.

**Misconceptions to kill:** that all uses are equally risky; that error rate is the same thing as risk; that internal equals safe.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**A&E triage, P1 to P4.** As above. Where it breaks: triage is done by trained nurses against a published protocol, while AI tiering is often done by whoever fills in the intake form — so the analogy explains the logic, not the reliability.

**PSLE marking versus a class quiz.** A national exam gets multiple markers, moderation and a review of borderline scripts. A class quiz gets a tick and a smiley. The stakes set the process, not the subject. Where it breaks: exam processes are centrally mandated, and AI processes usually are not.

### Worked example with a real tool

Give the model the rubric, then make it defend the placement:

```
Tier these three uses as prohibited, high, limited or minimal risk, using
four factors: severity of harm, reversibility, who is affected, and how
much the system decides on its own.

(a) AI drafts a party invitation for staff.
(b) AI screens loan applications and recommends approve/reject.
(c) AI summarises public news for an internal newsletter.

For each: state the tier, the factor that drove it, the control the tier
requires, and what evidence would move it up or down a tier.
```

What to point at afterwards: (b) will be tiered high and for the right reason, but the model usually under-weights "who is affected and can they refuse" — applicants never chose the system and cannot see the score. Ask the room what the applicant's appeal route would be. If nobody can answer, the tier was right for the wrong reason.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two headlines on the board: a chatbot writing birthday messages, and an algorithm denying insurance claims. Ask which deserves a committee.
2. **State the objective** — place any use on the four tiers, justify with the three questions plus autonomy and scale, name the required control.
3. **Recall prior learning** — the risk catalogue from `TSC8-Basic-K4`; today you rank it.
4. **Present the content** — severity × probability, reversibility, who is affected, allocative vs representational harm, autonomy and scale, the four tiers and their actions.
5. **Guide** — tier the three examples together, then re-tier them with "the model decides and acts automatically" added.
6. **Elicit performance** — each table tiers four uses from their own industry and writes the control each needs.
7. **Give feedback** — challenge the two predictable errors: treating internal as minimal, and treating low error rate as low risk.
8. **Transfer** — each learner writes the one use in their team that is currently under-tiered, and to whom they will raise it.

## What the framework doesn't mention but trainers need to know

- **Tiering is where governance fights happen.** The argument is almost never about the label; it is about the cost of the controls the label triggers. Teach learners to argue about controls, not labels.
- **Under-tiering is the common sin, not over-tiering.** Nobody gets in trouble for treating a low-risk tool carefully; people get in trouble for the reverse. Expect resistance and name it early.
- **The affected-party question is the fastest quality check.** Ask "who are they and can they say no" and watch half the room re-tier their own answer.
- **Scale changes the answer, not the principle.** A 2% error rate is an anecdote at 100 decisions and a scandal at 100,000; the tier logic is identical.

## Watch out

- **Do not let the exercise become a ranking game with no consequences.** Every tier must be followed by "so what does this require" — otherwise it is trivia.
- **Do not compare vendors when the bullet asks you to compare uses.** Redirect to `TSC8-Basic-A3` and say why the distinction matters.
- **Do not quote tier definitions you cannot source.** The four-tier structure is the EU AI Act's; Singapore's frameworks are voluntary and use their own language. Attribute carefully.
- **The stale claim to retire:** "high risk means the technology is dangerous." High risk means the *decision* is consequential. The same model is minimal risk in the next room.
