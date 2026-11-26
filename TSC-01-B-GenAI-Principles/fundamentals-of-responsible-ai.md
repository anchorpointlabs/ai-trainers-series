---
id: 01.01.B.K7
tsc: 1
level: Basic
code: K7
title: Fundamentals of responsible AI
as_at: 2026-11-26
review_by: 2027-02-25
---

# Fundamentals of responsible AI

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K7**

> **Framework text (verbatim):** "Fundamentals of responsible AI."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 7 of 13

**One-line version:** Responsible AI is four or five principles applied at the point of deployment by a named human — not a vendor's web page, not a policy PDF, and not the compliance team's job.

## What it is

Responsible AI is the practice of using AI in a way that is fair, transparent, accountable and safe. Every one of those words is contested, and every one has a concrete workplace meaning: who could be treated unfairly by an output, whether people know a machine was involved, who can be named when it goes wrong, and whether the thing can do harm. This bullet teaches the principles; `TSC1-Basic-A05` turns them into the five questions a learner actually asks.

## Deep expansion

### The concept

The principles are cheap to state, which is why every vendor website states them. The work is in the translation, and one device makes it teachable: each principle answers a different question about the same system.

- **Fairness** — who could be treated worse than someone else, and would we notice?
- **Transparency** — can the person affected find out a system was involved, and how it reached its output?
- **Accountability** — whose name is on this if it is wrong?
- **Safety and robustness** — what happens under the wrong inputs, at the wrong moment, or under attack?
- **Human oversight** — can a person realistically overrule it?

A learner who can answer those five about their own workflow understands responsible AI. One who can recite the four principles but not answer the questions has memorised a poster.

The second idea that matters: **responsibility attaches to the deployment, not the model.** The provider is responsible for the model's behaviour in general. You are responsible for what you point it at, what data you feed it, who sees the output, and what happens next. That sentence reframes the topic for a business audience, and it is why a vendor's compliance page does not cover your use case.

### The sub-concepts

**Fairness, and the three doors bias walks through.** *Data*: the model absorbed whatever the corpus contained — who was depicted as a nurse, whose English was treated as correct. *Prompt*: whoever wrote the instruction decided who to optimise for, often without noticing; "a receptionist who will fit our team culture" carries an implicit candidate. *Process*: what you do with the output — if a human reviews only the rejections, the model is effectively deciding the acceptances. Trainers teach the first door almost exclusively, which leaves learners undefended against the two they control.

**Transparency and disclosure.** People are generally entitled to know when they are dealing with a machine, especially in service and hiring. In Singapore practice that means a clear statement at the point of interaction — the application acknowledgement, the chat window, the email footer — rather than a paragraph in a policy.

**Accountability.** It cannot be delegated to a vendor, a model or a committee. It is a named role with the authority to stop the workflow. The test worth teaching: if this is wrong tomorrow and someone asks who signed off, is there a name?

**Human oversight, defined concretely.** Four things at once: **authority** to reverse the output, **time** to review it, **information** to judge it, and **competence** to know when it is wrong. Remove any one and you have a rubber stamp. The commonest failure in practice is time — a reviewer with forty outputs an hour is not reviewing, they are clicking.

**Safety, robustness, and the security dimension.** Wrong inputs, adversarial inputs (instructions hidden inside a document or an email), and misuse. A system that reads from an untrusted source and can also send, write or pay is exposed regardless of what the model's policy says. Safety here is architecture, not a prompt.

**Privacy, and its separate law.** Personal data obligations under the PDPA are covered in `TSC1-Basic-K8`. Responsible AI is broader: a system can be PDPA-compliant and still unfair, unexplained or unaccountable. Say this explicitly, because "we comply with PDPA" is the commonest wrong answer in this area.

### How it connects to the rest of the framework

This bullet supplies the principles that `TSC1-Basic-A05` operationalises as five questions. `TSC1-Basic-K8` and `TSC1-Basic-A03` cover the data side. `TSC2-Basic-K07` covers guardrails, the technical expression of safety. At Intermediate and Advanced the same principles become formal governance, impact assessment and audit.

### What is current as of November 2026

- **Singapore's framework stack is three layers deep.** The Model AI Governance Framework (2020), the Generative AI Model Governance Framework (2024), and the Model AI Governance Framework for Agentic AI (22 January 2026). The third layer exists because agents act: "what happens when it is wrong" and "who is accountable" change character when the wrongness can be a payment or a record update.
- **AI Verify is the practical assurance route.** It gives an organisation something to point at when a client asks "how do you know?". It tests; it does not certify your judgement.
- **Agentic deployments made oversight urgent rather than theoretical.** With read-only tools oversight is a reading task; with write tools it is an approval task, and approval fatigue is the new failure mode — a human who has approved fifty correct actions will approve the fifty-first unread.
- **Disclosure expectations hardened in service and hiring.** The direction of travel is clear even where rules lag: tell people, and give them a route to a human.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Responsible AI is the compliance team's job."* It is the deployer's job, and the deployer is usually the business unit that chose the workflow.
- *"The model is biased, so we cannot use it."* Every model carries bias. The question is whether it reaches a decision that harms someone, and whether anyone would notice.
- *"We added a disclaimer, so we are covered."* A disclaimer does nothing when the output is the only thing the affected person sees.
- *"Human in the loop means oversight."* Only if the human can disagree, has time to look, and has seen the basis of the output.
- *"It is internal, so the risk is low."* Internal tools make employment decisions about internal people.

## How a student should understand it

**Mental model:** a five-line pre-flight checklist read out loud before take-off, with a named pilot. Not a philosophy, not a policy — a ritual with an owner.

**Things they can do after this bullet:**
1. Name the four or five principles and give a workplace example of each going wrong.
2. Identify the three doors bias walks through in a workflow they know.
3. Say what meaningful oversight would require in their context — authority, time, information, competence.

**Misconceptions to kill:** that it is legal's problem, that a disclaimer is a control, and that a human in the loop is oversight by definition.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The contractor with no licence.** You would not let someone renovate your flat because they showed a certificate from the manufacturer of their drill. The vendor's responsible-AI page is the drill certificate; the work is still on your premises, with your wiring, under your liability, and you will be the one explaining it to HDB.

**The MRT platform screen doors.** The doors do not make the train safe — the system does: sensors, staff, procedures, and a passenger who does not lean on them. Responsible AI is the whole system around the model. Where it breaks: platform doors behave identically every time, and a model does not.

### Worked example with a real tool

Use the model as the critic, not the subject:

```text
We use an AI assistant to shortlist candidates for a customer service role.
A recruiter pastes the job description and 60 CVs, and receives a ranked list
of the top 10. The hiring manager interviews those 10.

Act as a responsible-AI reviewer. For each of these, give me the specific
failure this workflow could produce and one concrete fix:
1. Fairness
2. Transparency to candidates
3. Accountability
4. Human oversight
5. Data and privacy
```

What to point at afterwards: the model produces a competent list, and the room should notice that **the fixes are process changes, not model changes** — a line in the acknowledgement email, a named owner, a rule that the recruiter reads the top 20 rather than the top 10, a stripping step before upload. That is the most useful shift in the whole bullet: responsible AI mostly changes the workflow, not the technology.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — Ask for "a photo of a nurse" or "a description of a CEO" and read what comes back. Let the room react before explaining.
2. **State the objective** — "You will run the principles over a workflow from your organisation and name one fix for each weak point."
3. **Recall prior learning** — From K4 and K6: the tool fails, and fails fluently. Who is responsible when it does?
4. **Present the content** — Principles as questions, not nouns. Then the three doors of bias.
5. **Guide** — Run the shortlisting prompt and mark which fixes are process and which are technology.
6. **Elicit performance** — Pairs take a workflow and write one line per principle.
7. **Give feedback** — Debrief the accountability line. It is almost always blank, and it is always what an auditor asks for.
8. **Transfer** — Each learner names one change they could make next week without a budget.

## What the framework doesn't mention but trainers need to know

- **Small organisations have no policy and no lawyer.** Your learners may *be* the governance function. Give them something they can run alone on a Monday.
- **Fairness testing needs a comparison, not an opinion.** The cheap version: run the same task with names, genders and postcodes varied, and compare.
- **Vendor assurance is about the model, not your use.** Every serious provider publishes a governance page and offers enterprise terms. Neither covers what your team pastes into it.
- **Agentic systems need the sixth question:** what may it do without asking? That is the 2026 addition and the 2025 text does not contain it.
- **Cost is the lever that changes behaviour.** A workflow that calls a frontier model for routine classification is irresponsible in money and energy at once.

## Watch out

- **Do not moralise.** Adult learners disengage from an ethics lecture and engage with a checklist applied to their own workflow.
- **Do not teach the principles as a memory test.** The four words are on every vendor site; the ability is the translation.
- **Do not accept "we comply with PDPA" as the whole answer.** Compliance is necessary and not sufficient; it says nothing about fairness or accountability.
- **The stale claim to retire:** "responsible AI slows innovation down." The version that slows delivery is the one discovered after launch, when the workflow has to be rebuilt.
