---
id: 08.01.B.A1
tsc: 8
level: Basic
code: A1
title: Apply ethical principles in decisions
---

# Apply ethical principles in decisions

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Ability A1**

> **Framework text (verbatim):** "Apply ethical principles in decision-making related to AI."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Ability · Bullet 5 of 10

**One-line version:** Applying principles means stopping at the decision point, asking four questions out loud, and letting a bad answer change what you were about to do.

## What it is

This ability converts knowledge of principles into a habit at the moment of decision. Four questions, asked before the decision is made: **is it fair, is it transparent, is it accountable, is it safe?** If any answer is no, the decision changes — scope, oversight, disclosure or timing. The output is not a feeling that ethics was considered; it is a decision you can defend to the person affected.

## Deep expansion

### The concept

Everyone in the room will say they consider ethics. Almost nobody does it at the right moment. The failure pattern is consistent:

1. The decision gets made for operational reasons — speed, cost, headcount.
2. Someone raises a concern afterwards.
3. The team assembles principles to justify what they already decided.

That third step is where "ethics" becomes decoration, and it is the behaviour this bullet exists to break. The discipline is to run the questions *before* the choice is fixed, when changing course is still cheap, and to record the answer so it can be revisited when the context shifts.

The second thing this ability requires is knowing where the decision actually sits. Many learners believe they are not decision-makers because they do not sign the purchase order. But the person who chooses which data goes in, who writes the system prompt, who decides whether a human reviews the output, and who tells the customer that a bot answered — each of those is an ethical decision, and most of them belong to the practitioner, not the executive.

### The sub-concepts

**The four questions, made concrete.** Fairness: would this produce a materially different outcome for a comparable person with a different background, and can I explain why? Transparency: does the person affected know AI is involved and know what it did? Accountability: which named human answers if this goes wrong? Safety: what is the worst outcome, and what would stop it? Abstract versions get vague answers; the "different person, worst outcome, named human" phrasing produces decisions.

**Harm severity against likelihood, which sets the oversight level.** The IMDA framework's classic matrix maps probability of harm against severity of harm to decide whether a human must be **in the loop** (approves every case), **on the loop** (monitors and can intervene), or **out of the loop** (no routine human involvement). Low severity and low probability can run automated; high severity never does. Learners should be able to place their own use on that grid and say which oversight mode it earns.

**Oversight that is real, not theatrical.** A human in the loop with ninety seconds per case, no visibility into why the model decided, and a speed target is not oversight. It is a signature on someone else's decision. Genuine oversight requires time, uncertainty information, domain knowledge and the authority to override without career cost. The test to teach: ask the reviewer to name the last case they rejected and why. If they cannot, the loop is decorative.

**Proportionality.** Before asking "can we make this ethical", ask "should this exist in this form". The intrusiveness of the system must be proportionate to the problem it solves, and the non-AI alternative must have been considered. Classroom biometric attendance to measure "engagement" is the distillation's example of a solution in search of a problem.

**Contestability and redress.** Every decision that can harm a person needs a route to challenge it: a channel, a meaningful explanation, a fresh look by an empowered human. If there is no appeal path, the first three questions were answered on paper only.

**Recording the decision.** A one-line decision record — use case, questions asked, answers, who approved, review date — is the difference between a habit and a claim. It also survives staff turnover, which is when most governance evaporates.

### How it connects to the rest of the framework

`TSC8-Basic-K1` supplies the principles; this bullet is where they are used. `TSC8-Basic-A2` decides how *much* scrutiny a given use deserves — you run the same four questions on everything, but not with the same depth. `TSC8-Basic-A4` writes the result down as a team guideline. `TSC8-Basic-A6` is the companion habit on the output side: scepticism about what the model produced, where this bullet is judgement about what you do with it.

### What is current as of November 2026

Two practical changes. First, the oversight conversation has matured from "is there a human?" to "can the human actually see enough?" Products built on OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon now surface reasoning summaries and confidence signals in many interfaces, which gives a reviewer something to check — and creates a new trap, since a fluent rationale persuades even when it is wrong.

Second, agentic delegation has made the accountability question urgent. An assistant that can send, book, pay or delete makes decisions continuously, so "who approved this action" must have an answer per action class, not per project. The EU AI Act's high-risk obligations and Singapore's sector rules (MAS for financial decisions, HSA for clinical ones) both push in the same direction: named human, logged override, appeal route.

### Common misconceptions

- *"Ethics is considered at project approval, so we're done."* The decisions that matter happen weekly, inside the workflow, long after approval.
- *"I'm not senior enough to make an ethical decision."* Choosing what to paste, what to disclose and whether to check are all yours.
- *"If the process is compliant, the outcome is ethical."* Compliance is the floor; a lawful decision can still be an unfair one.
- *"The human in the loop covers accountability."* Only if that human has time, information and authority.
- *"We'll handle the appeal if someone complains."* An appeal route designed after the harm is a complaint-handling exercise, not redress.

## How a student should understand it

**Mental model:** the SAF risk assessment before a live-firing exercise. You walk the ground, name the hazards, state the controls, and a named commander signs. Nobody thinks the form prevents the accident; the *walk* does, and the signature is how you know it happened.

**Things they can do after this bullet:**
1. Run the four questions on a live decision in under five minutes and state the answer to each.
2. Place a use on the severity-by-likelihood grid and say whether it earns in-the-loop, on-the-loop or out-of-the-loop oversight.
3. Write a two-line decision record that would let a successor defend or reverse the choice.

**Misconceptions to kill:** that ethics happens at approval rather than at the decision; that a compliant process guarantees a fair outcome; that a human clicking approve is accountability.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The SAF risk assessment.** As above. Where it breaks: a risk assessment is mandated and audited, while most AI decisions have no form at all — which is exactly why the learner must supply the discipline themselves.

**The clinic's second signature.** A polyclinic doctor can prescribe, but a controlled drug needs a second clinician's signature and a reason recorded. Accountability is not a feeling of responsibility; it is a name next to a reason. Where it breaks: the second signatory here has full case visibility, which an AI reviewer often does not.

### Worked example with a real tool

Use the model as a challenger, not an oracle:

```
Decision on the table: we auto-approve customer refunds under $50 with no
human check. Volume is about 300 a day.

Act as a sceptical risk reviewer. For each question, give the strongest
argument AGAINST this decision and the cheapest control that answers it:
1. Fairness — who could be treated differently and not know it?
2. Transparency — what does the customer believe is happening?
3. Accountability — who signs when a refund is wrong or abusive?
4. Safety — what is the worst week this design could produce?

Then state the single condition you would insist on before launch.
```

What to point at afterwards: the model will propose controls that cost money (manual sampling, appeal button) and will usually miss that the customer believes a human approved it. That gap is the transparency question, and it is the one learners skip.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "You approved a refund bot. A customer was refused three times by the bot and then went to the press. Who is answerable, and to whom?"
2. **State the objective** — run four questions on a real decision, place it on the oversight grid, record the answer.
3. **Recall prior learning** — `TSC8-Basic-K1`'s five principles; today you use four of them as a checklist, not a lecture.
4. **Present the content** — the four questions, severity × likelihood, HITL/HOTL/out-of-loop, proportionality, contestability, decision record.
5. **Guide** — work the refund example with the model as challenger; fill the decision record on the board.
6. **Elicit performance** — each learner brings one live decision from their own work and produces a decision record plus one condition.
7. **Give feedback** — mark each record for: named human, appeal route, review date. Missing any of the three is the common failure.
8. **Transfer** — pairs swap records and try to reverse each other's decision from the record alone. If they cannot, the record is not good enough.

## What the framework doesn't mention but trainers need to know

- **Decision rights are usually unclear, and that is the finding.** When a learner cannot say who approves, the correct output of the exercise is "escalate the ambiguity", not "assume it's fine".
- **Cheap controls win arguments.** Sampling 20 cases a week, an appeal button, and a disclosure line cost almost nothing and answer three of four questions. Lead with those, not with committee reviews.
- **Record the "no" decisions too.** The uses you declined to build are the strongest evidence of a functioning process, and they vanish from memory within a quarter.
- **Ethics speed matters.** A process that takes six weeks to approve a meeting-notes summariser will be routed around. Fast lanes for low-risk uses are what protect the slow lane for high-risk ones.

## Watch out

- **Do not let the four questions become a form.** If the answer is always "yes, yes, yes, yes", the trainer should challenge one answer live until it is not.
- **Do not accept "the vendor handles that".** Deployment decisions are the deployer's, and the tribunal cases say so.
- **Do not teach ethics as a brake.** The framing that lands with operators is that governance is what lets you drive at speed without crashing.
- **The stale claim to retire:** "ethics slows us down." Unrecorded decisions slow you down far more the first time one is challenged.
