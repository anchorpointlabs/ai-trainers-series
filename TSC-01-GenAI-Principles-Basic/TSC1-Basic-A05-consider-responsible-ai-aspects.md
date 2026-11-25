# TSC1-Basic-A05 · The five questions to ask before you deploy anything

> **Framework text (verbatim):** "Consider responsible AI aspects of application of generative AI."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Ability · Bullet 13 of 13

**One-line version:** Considering responsible AI is a five-question check you run before a workflow goes live, not a policy document you signed when you bought the licence.

## What it is

This bullet is an ability, not a body of theory. It asks the learner to *do* something: bring the responsible-AI principles to bear on a specific application. In a Basic course that means one repeatable act — applying a short set of questions to a real workflow and being able to defend the answers.

## Deep expansion

### The concept

Responsible AI principles are cheap to state and easy to ignore, because they describe values rather than actions. The translation from principle to action happens at the point of deployment, and it takes the form of questions a non-specialist can actually answer:

1. **Who is affected by this output, including people who never use the tool?** A recruitment screener affects rejected candidates. A customer-service bot affects the customers who cannot reach a human.
2. **What happens, specifically, when it is wrong?** "A bad draft" and "a denied claim" are different failure classes. Name the consequence, not the risk.
3. **Can the affected person find out and object?** Disclosure, an explanation, an appeal route. If there is none, that is a decision, not an oversight.
4. **Is a named human accountable for this output?** Accountability cannot be delegated to a vendor or a model. If nobody's name is attached, nobody owns the error.
5. **What personal data does it touch, where does it go, and how long does it stay?** The privacy conversation, in one question.

Everything else in responsible AI — fairness, transparency, safety, oversight, environmental cost — lands inside one of those five.

### The sub-concepts

**Disclosure.** People are generally entitled to know when they are dealing with a machine, particularly in service and hiring. In Singapore practice this normally means a clear statement at the point of interaction rather than a line in a policy PDF.

**Bias, and where it actually enters.** Three doors: the training data (what the model absorbed), your prompt (who you told it to optimise for), and your process (what you do with the output — if a human only reviews the rejections, the model is effectively deciding the acceptances). Trainers tend to teach only the first.

**Human oversight, defined concretely.** Meaningful oversight means a person with the authority, time, information and competence to overrule. A rubber stamp after the fact is not oversight, and learners should be able to tell the difference.

**Vendor claims.** Every provider publishes a responsible-AI page. It describes their model, not your use. The obligation attaches to the deployment, which is yours.

**Environmental and cost responsibility.** Inference has a cost in energy and money. A workflow that calls a frontier model a thousand times a day to do work a rule could do is a responsible-AI issue as well as a budget one.

### How it connects to the rest of the framework

`TSC1-Basic-K07` supplies the principles this ability operationalises. `TSC1-Basic-K08` and `TSC1-Basic-A04` cover the data side. `TSC2-Basic-K07` covers guardrails, which are the technical expression of questions 2 and 3. At Intermediate, `TSC8` turns this into formal governance and impact assessment.

### What is current as of November 2026

- **Singapore's framework stack is now three layers deep:** the Model AI Governance Framework (2020), the Generative AI Model Governance Framework (2024), and the Model AI Governance Framework for Agentic AI (22 January 2026). The third exists because agents *act*. Questions 2 and 4 change character when the system can send an email, move money or modify a record.
- **AI Verify** gives organisations a testing and assurance route, which is useful when a client asks "how do you know?".
- **The National AI Impact Programme** (announced 2 March 2026, 10,000 enterprises and 100,000 workers, starting with accountancy and law) has pushed responsible-use questions into SMEs that had no AI policy at all eight months ago. Trainers are frequently the first person to raise them.
- **Agentic deployments make the "what happens when it is wrong" question urgent**, because the wrongness can now be an action rather than a sentence.

### Common misconceptions

- *"Responsible AI is the compliance team's job."* It is the deployer's job; the deployer is usually the business unit, not legal.
- *"The model is biased, so we cannot use it."* Every model carries bias. The question is whether the bias reaches a decision that harms someone, and whether anyone would notice.
- *"We added a disclaimer, so we are covered."* A disclaimer shifts nothing when the output is the only thing the affected person sees.
- *"Human in the loop" automatically means oversight.* Only if the human can realistically disagree.
- *"It is only internal, so the risk is low."* Internal tools make employment decisions about internal people.

## How a student should understand it

**Mental model:** a pre-flight checklist, five items, answered out loud before take-off. Not a philosophy, not a policy — a checklist with a named owner.

**Three things they can do:**
1. Run the five questions on a workflow from their own organisation in under ten minutes.
2. Identify who is affected but not using the tool.
3. Say what meaningful oversight would require in their context — time, information, authority.

**Misconceptions to kill:** that this is legal's problem, that a disclaimer is a control, and that a human in the loop is oversight by definition.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The contractor with no licence.** You would not let someone renovate your flat because they showed you a certificate from the manufacturer of their drill. The vendor's responsible-AI page is the drill certificate. The work is still yours, on your premises, with your liability.

**The five-point pre-flight.** Pilots do not debate safety philosophy before take-off; they read the same five items every time, out loud, in order. The value is the ritual, not the insight.

### Worked example with a real tool

A recruitment shortlisting workflow, run through the five questions:

```
1. Affected: 240 applicants, of whom 200 will never be interviewed and never
   learn a model was involved. Also the hiring manager, who will trust the list.
2. When wrong: a strong candidate is dropped silently. Consequence is invisible
   to us and serious to them.
3. Find out and object: currently no. Fix: state in the application
   acknowledgement that assisted screening is used, and offer a human re-review
   on request.
4. Accountable: the hiring manager by name, not "HR".
5. Data: CVs contain NRIC, address, photo, nationality, salary history. Strip
   before submission; confirm retention with the vendor's enterprise terms.
```

What to point at: question 3 produced a one-line change to an acknowledgement email, and question 5 produced a stripping step. Neither is a policy document, and both are defensible in an audit.

### Live demo or exercise

**Five questions, five minutes, their own workflow.** Each learner picks one AI use from their job — current or planned — and writes a one-line answer to each question. Then two pairs swap and challenge the weakest answer. The room discovers quickly that question 2 ("what happens when it is wrong") is the one nobody can answer, and that question 4 usually has no name.

## What the framework doesn't mention but trainers need to know

- **Small organisations have no policy and no lawyer.** Your learners may *be* the governance function. Give them something they can run without a committee.
- **The vendor's terms are part of the answer.** Data retention, training-on-inputs, sub-processors and regional processing are in the DPA, not the marketing page. Teach people to ask for the DPA.
- **Disclosure wording matters.** "This chat may be assisted by AI" is honest; "our team personally reviews every message" is not, if it is untrue.
- **Accessibility is a responsible-AI issue too.** A voice-only interface excludes; a chat-only service excludes differently. Rarely taught, frequently relevant.
- **The environmental argument is real but weak as a motivator.** Cost is the argument that changes behaviour. Use it, and mention energy honestly.
- **Agentic systems need a sixth question:** what may it do without asking? That is the 2026 addition, and the framework's 2025 text does not contain it.

## Watch out

- **Do not teach this as a list of principles to memorise.** The principles are on the vendor's website; the ability is applying them under time pressure.
- **Do not let "human in the loop" pass unchallenged.** Ask what the human sees, how long they have, and whether they have ever overruled.
- **Do not accept "we comply with PDPA" as an answer to question 5.** PDPA compliance is necessary and not sufficient — it says nothing about fairness or accountability.
- **Do not moralise.** Adult learners disengage from a lecture on ethics and engage with a checklist applied to their own workflow.
- **The stale claim to retire:** "responsible AI slows innovation." The version that slows delivery is the one discovered after launch, when the workflow has to be rebuilt.
