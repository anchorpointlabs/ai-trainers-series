---
id: 05.03.A.K6
tsc: 5
level: Advanced
code: K6
title: "Whose values are in the rubric: legal, cultural and socio-political lenses"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Whose values are in the rubric: legal, cultural and socio-political lenses

> **TSC #5 Generative AI Model Evaluation · Advanced · Knowledge K6**


> **Framework text (verbatim):** "Ethical dimensions of AI through interdisciplinary perspectives (e.g. legal, cultural, socio-political aspects)."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Knowledge · Bullet 6 of 13

**One-line version:** A rubric is a moral document with numbers attached, and the argument is about which values got in.

## What it is

This bullet asks the evaluator to read their own instrument as a social object. A rubric decides what counts as good, whose language counts as clear, whose politeness counts as respect, and which harms count as harms. The legal lens looks at obligation and liability; the cultural lens at what a specific community regards as decent; the socio-political lens at who gains, who is measured worse, and who was never in the test set.

## Deep expansion

### The concept

Evaluation looks neutral because it produces numbers. The numbers are downstream of choices that are not neutral: which tasks were sampled, which raters were recruited, which language the rubric is written in, which failures were named as failures.

A Singapore bank evaluating a service assistant rewards "concise, direct, professional English". Applied to a Mandarin-speaking auntie writing in fragments, or an uncle whose Singlish signals warmth rather than sloppiness, the same rubric scores them as difficult customers and the model as unhelpful. Nothing in the score says "this rubric encodes a class and language preference". It just looks like quality.

**Legal** asks what obligation the output triggers: defamation if the model invents a claim about a person, copyright if it reproduces a protected work, contract if the output becomes a term, discrimination law if a decision about a person is affected. Evaluation must test for the failure that triggers the obligation, not quality in the abstract. **Cultural** asks what is respectful in *this* community: multi-religious, multi-lingual, multi-generational, where the same register reads as warmth in one place and contempt in another. **Socio-political** asks who is represented in the training distribution, which dialects are treated as errors, whether the efficiency gain lands on the workers who carry the failures, and whether the deployment concentrates capability in an institution that already had it.

### The sub-concepts

**The rubric as a normative instrument.** Every clause contains a "should". Make it visible: "must state the next step so the customer is not left waiting" is auditable; "must be helpful" is not.

**Language equity.** Models are better in high-resource languages. In Singapore that means English, Mandarin and Malay behave differently from Tamil, and Singlish differently again. Averages hide this; slices expose it.

**Code-switching.** Real users mix languages mid-sentence. A system that fails on code-switched input fails on a large share of the population while scoring well on clean items.

**Representational harm.** Who appears in the image for "a company director", "a nurse", "a person with a disability". Countable, which makes it one of the few societal harms with a straightforward method.

**Allocation and quality-of-service harm.** The system works better for some users. Often measurable, frequently unmeasured.

**Standing and voice.** Were affected people involved in defining what good looks like, or represented by a product team's assumption about them.

### How it connects to the rest of the framework

`05.03.A.K5` is the formal instrument; this bullet is its interpretation and critique. `05.03.A.A6` turns the lens into methodology — how to actually measure societal impact. `05.02.I.K5` is the operational fairness level; this is where you question the principle itself. `TSC8` holds the organisational practice, `TSC9` the security and abuse dimensions alongside it.

### What is current as of November 2026

Multilingual quality remains uneven in ways vendors rarely advertise: the flagship lines (GPT-6.1 Sol and Terra, Claude 5.5, Gemini 3.1 Pro and 4 Argon) are strongest in high-resource languages and on English benchmarks, and regional variety — Singlish, Manglish, Tamil-English code-switching — is a known soft spot a Singapore evaluation must test directly. The second shift is that model policy is now regional: the same product can refuse different requests in different markets, so an evaluation run in one jurisdiction does not describe the system your users meet.

### Common misconceptions

- *"Ethics means the safety filter."* Moderation is one control. Most ethical failure in deployed systems is about quality distribution, language and representation, and none of it trips a filter.
- *"The rubric is neutral because it is numeric."* The numbers come from clauses written in a language by people with a view of what good looks like.
- *"We tested in English, which is the working language."* Your users are not all your staff, and your staff are not all fluent in the register your rubric rewards.

## How a student should understand it

**Mental model:** the school report card that grades "conduct" — a number quietly encoding one teacher's idea of a good child, applied to thirty children from thirty homes.

**Three things they can do after this bullet:**
1. Read a rubric and name the values embedded in three of its clauses.
2. Identify which user groups are missing from a test set, and what that omission hides.
3. Argue a legal, cultural and socio-political position on one system, and say what evidence each would need.

**Misconceptions to kill:** that ethics equals filters, that numbers are neutral, and that a set collected in Singapore is automatically culturally appropriate.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The kopitiam "good service" standard.** The boss says be "friendly and efficient". The young server who calls everyone "uncle" and chats scores well; the older auntie who is fast and terse scores badly, though the regulars prefer her. The rubric measured one cultural style of warmth and called it service. It breaks because a kopitiam can afford idiosyncrasy; a bank's assistant serves a whole population at once.

**The PSLE oral component.** The marking scheme rewards "standard English". A child who speaks fluent, expressive Singlish is marked down for a register the scheme treats as error. The scheme is not wrong to have a standard; it is wrong if nobody notices the standard is a choice.

### Worked example with a real tool

A regional team has written a rubric for a service assistant and wants its cultural assumptions tested. Paste this into Claude or Gemini:

```
Here is our evaluation rubric for a customer service reply assistant, written in
Singapore English by a product team in Singapore.

For each clause: (1) name the cultural or class assumption it contains, if any;
(2) say which customer group would be scored unfairly and how; (3) rewrite it to
measure the outcome (did the customer get what they needed) rather than the style
(how it sounded); (4) flag any clause a rater in Kuala Lumpur, Chennai or Manila would
read differently, and say what changes.

Be specific. Do not add new clauses; only work on the ones given.
```

What to point at afterwards: rewrites from "sounds professional" to "states the next step and the timeframe". The room resists — the original clauses feel obvious and the rewrites feel bureaucratic. That resistance is the lesson: the originals were a style preference, the rewrites are a testable standard.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — project two customer messages, one formal and one Singlish, ask who gets served better, then show the scores.
2. **State the objective** — learners can name the values in a rubric and rewrite a clause to measure outcome, not style.
3. **Recall prior learning** — the fairness and explainability material; ask who the explanation is written for.
4. **Present the content** — three lenses, language equity, code-switching, representational harm, standing and voice.
5. **Guide** — rewrite two clauses together, arguing about what "respectful" means to whom.
6. **Elicit performance** — groups take one clause each and produce a rewrite plus the group it protects.
7. **Give feedback** — check whether any rewrite smuggled the original style preference back in.
8. **Transfer** — each learner lists the three user groups least represented in their test set.

## What the framework doesn't mention but trainers need to know

- **Recruit raters who are not the product team.** Cultural competence cannot be simulated by a thoughtful engineer; it can be borrowed by asking the right people.
- **Language slices need enough items to say anything.** Ten Tamil items produce noise. If the population matters, the sample has to.
- **Regional policy divergence is an evaluation variable.** A system that refuses in one market and answers in another is two systems for evaluation purposes.
- **Some harms have no metric and still need a judgement.** Write it down, attribute it, revisit it. An unrecorded ethical judgement is one that gets reversed by whoever ships next.

## Watch out

- **Do not turn this into a lecture on right and wrong.** The advanced skill is reading an instrument for its assumptions, not holding correct opinions.
- **Do not use one culture as the "diverse" case.** Every rubric is cultural, including the one written in Singapore for Singapore.
- **Do not let the discussion stay abstract.** If the session ends without a rewritten clause and a named missing group, nothing was learned.
- **Do not claim a system is unbiased because a test passed.** State the slices you tested; the untested ones are unknown, not clean.
- **The stale claim to retire:** "we handle cultural issues in localisation." Localisation translates strings; it does not re-examine what the rubric counts as good.
