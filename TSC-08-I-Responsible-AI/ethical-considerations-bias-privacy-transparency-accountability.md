---
id: 08.02.I.K1
tsc: 8
level: Intermediate
code: K1
title: Ethical considerations — bias, privacy, transparency, accountability
as_at: 2026-11-26
review_by: 2027-02-25
---

# Ethical considerations — bias, privacy, transparency, accountability

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Knowledge K1**

> **Framework text (verbatim):** "Ethical considerations in AI development, (e.g., bias, privacy, transparency, accountability)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Knowledge · Bullet 1 of 14

**One-line version:** The four considerations are not a poster on the wall — they are four decisions you make while building: whose data the model learned from, whose data it touches, who can see why it decided, and whose name is on the failure.

## What it is

Ethical considerations in AI development are the four risks that turn up in nearly every system: **bias** (the model treats some groups worse), **privacy** (it touches personal data it may not need), **transparency** (people cannot tell that AI is in use, or why it decided), and **accountability** (no named person answers when it harms someone). For a developer these are not values to hold but constraints to design against, each with an owner, a test and an artefact that proves the test was run.

## Deep expansion

### The concept

The framework says "ethical considerations", which sounds like a discussion. In engineering terms it is a short list of failure classes, and each one has a place in the pipeline where it is cheap to fix and a place where it is expensive.

Bias is created before the first line of model code, in what you chose to train on and how you labelled it. Privacy is decided in the data architecture — what you collect, what you send to an external API, how long you keep it. Transparency is decided in the interface and in the documentation you publish. Accountability is decided in the organisation chart, which is the only one of the four you cannot fix with engineering.

That mapping is the whole lesson. Learners arrive thinking ethics is a review that happens at the end, run by someone else, producing a document nobody reads. The correction is that three of the four are engineering decisions made by the people in the room, and the fourth is a management decision the room usually avoids.

### The sub-concepts

**Bias lives in data and labels, not in malice.** A model trained on ten years of past hires learns the pattern of past hires, including the parts of that pattern nobody wrote down. It has no concept of fairness to violate; it reproduces the distribution it was shown, then applies it to people who were never in the distribution.

**Privacy is about the smallest data that does the job.** Data minimisation is not an IT policy, it is a design rule: if the task needs a postcode and a transaction count, the name and NRIC are not required. The moment a prompt leaves your perimeter for a third-party API, the data question becomes a contract question.

**Transparency has three separate layers, and learners collapse them.** First, *disclosure*: does the user know a machine is answering? Second, *documentation*: is there a model or system card stating what it can and cannot do? Third, *explanation*: can you say why this particular decision came out this way? A system can pass the first and fail the third, which is exactly what a loan applicant experiences.

**Accountability needs one name.** "The AI team" is not accountable; a committee is not accountable. The IMDA framework and the EU AI Act both push towards a named human with the authority to stop the system, because a decision with no owner is a decision that will be defended by blaming the vendor, the data or the model.

**The four conflict with each other.** More transparency (logging every prompt) costs privacy (logs contain personal data). Stronger privacy (heavy anonymisation) can cost accuracy, which is bias by another route if the loss falls unevenly. Trainers should say this early: there is no configuration that satisfies all four maximally, only a documented, defensible balance.

### How it connects to the rest of the framework

This bullet is the map of the whole TSC. `TSC8-Intermediate-K3` takes bias to its societal consequence; `TSC8-Intermediate-K4` is the communication half of transparency; `TSC8-Intermediate-K5` supplies the frameworks and the legal floor that give these four their structure. On the ability side, `TSC8-Intermediate-A3` is how you mitigate, `TSC8-Intermediate-A4` is the privacy-versus-performance trade-off made explicit, `TSC8-Intermediate-A5` is the structured analysis, and `TSC8-Intermediate-A8` is where the four become gates in a lifecycle.

### What is current as of November 2026

The four considerations have moved from the ethics page to the procurement form. Enterprise buyers now ask vendors for a model card, a bias evaluation summary, data-retention terms and an incident-contact clause before signing — which means a developer who cannot produce these artefacts loses the deal, not just the argument.

Frontier providers publish system cards for each release: the GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon. Those cards cover the base model. They cannot cover your RAG corpus, your system prompt or your escalation workflow — which is where most deployed bias and privacy harm actually originates.

Two shifts matter for teaching this bullet. Agentic systems make accountability urgent, because the model now acts rather than suggests, so "who approved this action" becomes a real question with a real answer required. And testing has become routine: Singapore's AI Verify and Project Moonshot toolkits let a team run fairness and safety checks as part of a build rather than commissioning a study.

### Common misconceptions

- *"We deleted the race and gender columns, so the model cannot discriminate."* It reconstructs them from proxies — postal code, school, mother tongue, NS vocation. Deleting the column also blinds your audit, because you can no longer measure the disparity. Keep the attribute out of the features; keep it in an access-controlled audit table.
- *"We only call an API, so governance is the vendor's problem."* The deployer carries the liability. The vendor cannot see your documents, your prompts or your customers.
- *"Transparency means publishing the model."* For almost no organisation is that the requirement. It means disclosing AI use, documenting limits, and being able to explain an individual outcome.
- *"Accountability means the AI team owns it."* The business owner of the workflow owns it. The AI team builds the controls that let them own it safely.
- *"Bias is a model bug you patch once."* It is a property of data, decision and context together, and it returns when any of the three changes.

## How a student should understand it

**Mental model:** a car with four systems, not four slogans — brakes (bias), door locks (privacy), dashboard (transparency) and a logbook with the driver's name in it (accountability). You do not "believe in" brakes; you fit them, test them, and record the test.

**Things they can do after this bullet:**
1. Name the four considerations and point to the pipeline stage where each is decided.
2. Write a one-line risk register entry per consideration: harm, design decision, artefact, owner.
3. Tell a vendor exactly which documentation they must supply before you deploy their model.

**Misconceptions to kill:** that bias is fixed by deleting a column, that a vendor absorbs your liability, and that transparency means open-sourcing weights.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The expressway.** Ethics is the shared belief that people should not die on the road. Safety engineering is the airbag, the ABS, the crumple zone. Governance is LTA and the Traffic Police: COE quotas, VICOM inspections, ERP, speed limits, demerit points. You can drive at 90 km/h on the PIE *because* those systems exist, not in spite of them. Where it breaks: road rules are enforced by the state, workplace AI by contract, procurement and occasionally a regulator — so the enforcement is weaker and the organisation must supply its own police.

**The hawker stall sign versus watching the chef.** Transparency is the sign: "cooked by a robot, contains peanuts and prawns, chicken from Malaysia." Explainability is asking why your laksa was saltier than your friend's and getting a real answer. Use this when learners treat the two words as synonyms.

### Worked example with a real tool

```text
We are about to deploy an assistant that drafts replies to customer complaints for a telco,
using the last two years of complaint emails as its knowledge base.

For each of the four considerations — bias, privacy, transparency, accountability — give me:
1. The specific harm, described concretely for this tool.
2. The design decision that prevents it.
3. The artefact that proves the decision was made.
4. The role that owns it.

Then tell me which of the four this team is most likely to skip, and why.
```

What to point at afterwards: the model will almost always assign accountability to "the team" or "the AI governance committee" — correct it to one named role. It will also offer "remove personal data from the emails" as the privacy fix, which is right but incomplete; ask what happens to the customer's name in the drafted reply, and to the email sitting in the vendor's logs.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a one-line headline about an AI system that denied something to a group, and ask who signed off.
2. **State the objective** — by the end you can map the four considerations onto a pipeline and assign an owner to each.
3. **Recall prior learning** — ask what "fair" meant in the last performance review they ran; surface how much judgement was involved.
4. **Present the content** — the four, the pipeline stage for each, the artefact for each.
5. **Guide** — work the telco example on screen, one consideration at a time.
6. **Elicit performance** — pairs take a tool from their own work and fill the four-row table.
7. **Give feedback** — project two tables; find the missing owner and the deleted column.
8. **Transfer** — each learner names the one consideration their team currently ignores.

## What the framework doesn't mention but trainers need to know

- **Four is a teaching number, not a complete list.** The governance literature runs to twelve principles — fairness, accountability, transparency, explainability, privacy, safety, robustness, human oversight, contestability, reproducibility, proportionality, sustainability. Four is what a developer can hold in working memory; say so, so learners are not surprised later.
- **Fairness is a choice among incompatible metrics.** Demographic parity, equal opportunity and predictive parity cannot all hold at once on the same data. Somebody in the organisation has to pick, and that pick is a business decision, not a maths result.
- **The vendor's supply chain is part of your ethics.** Data annotators, scraped corpora, licensing — none of it appears in the four words, all of it appears in a due-diligence questionnaire.
- **Middle managers decide whether this is real.** If a team lead is measured on shipping date only, the four considerations are theatre regardless of what the policy says.

## Watch out

- **Do not demo with real customer data**, not even "anonymised" exports. Use a synthetic table and say it is synthetic.
- **Do not let "the AI decided" enter the room.** It is accountability laundering, and it is the sentence that loses the court case.
- **Do not present a human-in-the-loop tick-box as oversight.** If the reviewer clears 400 cases an hour, the human is decoration.
- **The stale claim to retire:** "AI ethics is a compliance deck." In November 2026 it is a set of tests in the build pipeline and a set of clauses in the vendor contract.
