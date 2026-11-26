---
id: 09.02.I.A1
tsc: 9
level: Intermediate
code: A1
title: Develop mitigation strategies
---

# Develop mitigation strategies

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Intermediate · Ability A1**

> **Framework text (verbatim):** "Develop mitigation strategies for identified risks."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Intermediate** · Ability · Bullet 5 of 10

**One-line version:** A mitigation is a change that makes the risk measurably smaller — if you cannot say what it changes and how you would know, it is not a strategy, it is a mood.

## What it is

Developing a mitigation strategy means pairing each identified risk with a specific intervention, choosing among the available kinds, trading cost against effect, and accepting explicitly whatever risk remains. It is engineering judgement applied to a register: the risk is given; the design of the response is the work.

## Deep expansion

### The concept

The menu is older than AI. **Prevent**: stop the condition existing — do not give the assistant write access, do not put personal data in the corpus. **Detect**: catch it when it happens — output filters, classifiers, anomaly alerts. **Respond**: limit the damage once it is happening — human approval gates, rate limits, kill switches. **Recover**: restore and learn — backups, incident review, test-set additions. **Avoid**: decline the use case. **Transfer**: contract or insure the residual, which works for money but not for a leak.

AI-specific mitigations slot into the same four buckets, which is a useful thing to tell learners: nothing here is exotic risk management, it is ordinary risk management applied to a component that can be talked into things.

Two disciplines separate a strategy from a wish list. First, **mechanism**: name the thing that changes. "Better prompting" is not a mechanism unless you can say which rule, enforced where. Second, **measurement**: name the evidence that the mitigation worked — a test case that now fails to break it, a block rate, a query that no longer returns data.

And the third, which is organisational rather than technical: **residual risk needs a signature**. After the mitigation, something remains. Someone with authority should accept it in writing, because otherwise it will be discovered later, by a customer.

### The sub-concepts

**Matching mitigation to risk type.** A hallucination risk is reduced by grounding, citation and a human review step — not by an input filter. A prompt-injection risk is reduced by architecture: least agency, identity in code, approval gates, egress control. An over-blocking risk is reduced by tuning and by measuring the block rate. Choosing a control that does not touch the failure mode is the most common error in the room.

**Cost against effect.** Rank mitigations by how much risk they remove per unit of effort, latency, cost and user friction. Removing write access from an assistant is cheap and removes an entire class of harm; adding a classifier to every turn costs money forever and removes less.

**Defence against the adaptive attacker.** A mitigation that reduces the chance of success by 90% still fails against someone who tries a hundred times. For adversarial risks, the useful question is what the system cannot do — permissions, schemas, approvals — rather than what it usually declines.

**Break the trifecta.** When private data, untrusted input and outbound capability coexist, the cheapest mitigation is usually to remove one leg: make the reading assistant unable to send, or the sending assistant unable to read third-party documents.

**Second-order effects.** A mitigation can create a new risk: an aggressive filter that blocks legitimate work pushes users to a personal account; a human gate that appears too often gets clicked through. Name the side effect in the plan.

**Re-test and review.** A mitigation is a hypothesis. It goes into the test set, and the register entry gets a review date.

### How it connects to the rest of the framework

`TSC9-Basic-A2` produces the risk note this answers. `TSC9-Intermediate-K3` scores the risk so mitigations can be ranked; `TSC9-Intermediate-A4` runs the assessment that generates the list. `TSC9-Intermediate-A2` is the mitigation set for the prompt-hack family specifically, `TSC9-Intermediate-K1` supplies the control catalogue, and `TSC9-Intermediate-A6` checks whether the mitigation still holds a quarter later.

### What is current as of November 2026

The cheap structural mitigations have become easier to implement, and therefore harder to justify skipping: identity from the session token, narrow tools, and approval gates are standard patterns in agent frameworks. The late-2026 frontier — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — also reduces the frequency of crude jailbreaks, which tempts teams to rely on model behaviour instead of architecture.

- **Model improvement is not a mitigation you control.** Treat it as a bonus, not a control on the register.
- **Agent frameworks ship with permission models.** Use them; a tool with no identity parameter is now a design default, not a clever trick.

### Common misconceptions

- *"We will tell the model to be careful."* A request, not a mechanism, and it competes for attention with the attack.
- *"We need the strongest control available."* You need the cheapest control that addresses this failure mode.
- *"The mitigation is done once it is deployed."* It is a hypothesis until a test confirms it and a review date keeps it honest.
- *"Residual risk does not need saying."* Unstated residual risk is the risk that becomes an incident nobody owned.

## How a student should understand it

**Mental model:** home security — a lock, a light on a timer, a camera, and insurance. You do not rely on one, and you know exactly what the insurance does not cover.

**Things they can do after this bullet:**
1. Pair a named risk with a mitigation that touches its actual failure mode.
2. Rank two mitigations by effect per unit of cost and defend the ranking.
3. State the residual risk and who accepts it.

**Misconceptions to kill:** that care is a control; that stronger is better; that a deployed mitigation is a proven one.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The shop's cash handling.** You do not solve theft by telling staff to be honest. You use a till with a drawer count, two people for large refunds, and a camera. Each is a different kind of mitigation — detect, prevent, deter — and together they make theft hard and visible.

**The umbrella in a thunderstorm.** An umbrella helps; it does not make you safe. The mitigation must match the hazard, and you still decide whether to go out.

### Worked example with a real tool

Give the room a risk and make them generate, then rank, mitigations:

```
Risk: our support bot sometimes includes another customer's order
details in a reply, because the retrieval step does not filter by
account.

Give me six mitigations. For each: the kind (prevent, detect,
respond, recover), what it changes, what it costs in latency or user
friction, and how we would prove it works. Then rank them by effect
per unit of cost.
```

What to point at afterwards: the highest-ranked mitigation is almost always the retrieval filter — a data-layer change with no user friction — while the output redaction they will also propose is a backstop, not the fix. The lesson is that the cheapest effective change is usually architectural.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read out "we will be more careful" as a mitigation and ask the room to sign it off.
2. **State the objective** — by the end, they can pair, rank and evidence a mitigation, and state residual risk.
3. **Recall prior learning** — any workplace controls they have implemented (stock, cash, safety).
4. **Present the content** — the six kinds; matching to failure mode; cost versus effect; the trifecta; second-order effects.
5. **Guide** — work the retrieval-leak example together.
6. **Elicit performance** — pairs write and rank mitigations for a risk from their own register.
7. **Give feedback** — debrief where a proposed control did not touch the failure mode.
8. **Transfer** — each learner adds a mitigation, an owner and a review date to one live risk.

## What the framework doesn't mention but trainers need to know

- **Mitigations interact.** Two teams each adding a filter can produce a system that refuses everything; review the combination.
- **Some mitigations are organisational.** A rule that only certain staff may upload documents can be stronger than any model-side control.
- **Friction has a budget.** Every approval dialog spends it; users have a finite tolerance before they route around the system.
- **Write the mitigation in the register, not in a deck.** The register is what the next engineer reads.

## Watch out

- **Do not accept a mitigation you cannot test.** If there is no test, there is no verification.
- **Do not let "monitor it" pass** without an owner, a threshold and a frequency.
- **Do not confuse reducing likelihood with reducing impact.** Both are legitimate; they are different purchases.
- **Retire the stale claim:** "the model will get better, so this risk will fade." In November 2026 the same improvements also make the system more capable of acting, which raises impact.
