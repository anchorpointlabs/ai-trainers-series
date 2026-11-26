---
id: 08.01.B.A3
tsc: 8
level: Basic
code: A3
title: Compare AI systems on compliance, IP, privacy, environment
as_at: 2026-11-26
review_by: 2027-02-25
---

# Compare AI systems on compliance, IP, privacy, environment

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Ability A3**

> **Framework text (verbatim):** "Compare AI systems based on considerations such as compliance with intellectual property, data privacy and environmental impact."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Ability · Bullet 7 of 10

**One-line summary:** Choosing a tool is a risk purchase, not a feature purchase — two providers with the same capability can leave you with very different liability.

## What it is

This ability is comparing AI products and providers on the things that decide whether you can use them safely: what they do with your data, who owns what comes out, what happens when it goes wrong, and what the thing costs to run. Compliance is a selection criterion, weighed alongside capability and price — not a footnote added after the decision.

## Deep expansion

### The concept

Most tool selection in SMEs runs on three columns: does it work, does it look nice, what does it cost. The ethical criteria appear only when someone in legal asks, which is usually after the pilot.

The reframe for learners: you are not buying a model, you are buying a set of contractual and technical commitments. The model will be replaced by the vendor within a year; the commitments are what you actually live with. Two products that answer your prompt identically can differ completely on whether your input trains their model, who indemnifies you for a copyright claim, and whether you get notice before the underlying model changes under you.

The second reframe: the comparison is not "which vendor is ethical". It is "which vendor's terms fit this use". A consumer product with generous terms may be perfect for drafting internal notes and disqualifying for customer data. Fit is use-specific, which is why the same organisation can legitimately choose different providers for different tasks.

### The sub-concepts

**Data handling: the first filter.** Four questions decide most of it: Is input retained, and for how long? Is it used for training? Can the setting be changed, and who can change it? Where is it processed? Zero-retention terms on enterprise tiers are now common, which is why the honest answer to many privacy problems is "buy the enterprise tier" rather than "train staff harder".

**IP: input and output.** On input, the question is whether the provider claims rights over what you upload. On output, two things matter: whether the provider indemnifies you against third-party copyright claims, and whether it offers filters that block reproduction of public code or text. An indemnity is a contract term, not a marketing claim — ask for the clause.

**Accountability and audit.** Can you get a model or system card describing training data, known limitations and evaluation results? Is there an audit-log export? Will the provider tell you before deprecating a model version, and how much notice? Can you test their endpoint yourself with a red-teaming tool? These are the questions that separate a supplier from a partner.

**Certifications and frameworks.** ISO/IEC 42001 is the certifiable AI management standard, the analogue of ISO 27001 for security; ISO/IEC 23894 covers AI risk management. SOC 2 reports cover controls, not ethics. Singapore's AI Verify and Project Moonshot are open toolkits you can run yourself — AI Verify for predictive models, Moonshot for LLM evaluation and red-teaming. A certification tells you a process exists; it does not tell you this model is fair for your population.

**Environmental footprint.** Compare on task, not on brand: how large is the model the product actually routes to, is there a smaller tier for routine work, does the vendor publish efficiency information, and where does inference run? Right-sizing is the lever the buyer controls. A product that sends every keystroke to a frontier model costs more money and more energy than one that routes simple requests to a small model.

**Price per outcome, not per seat.** The relevant comparison is cost per completed task including human review. A cheap tool that needs heavy checking is expensive; an expensive tool that returns verifiable output with citations may be the cheaper option once the checking time is counted.

### How it connects to the rest of the framework

`TSC8-Basic-K2` gives the three checks this bullet applies to a purchase. `TSC8-Basic-A2` decides how much rigour the use deserves, which sets how deep this comparison goes. `TSC8-Basic-A4` writes the outcome into the team's rules — including which tools are approved. `TSC8-Basic-A5` covers the controls you apply once data is inside the chosen tool.

### What is current as of November 2026

The gap between consumer and enterprise terms has widened, and it is now the single most useful thing a trainer can teach. Across the major product lines built on current frontier models, organisational tiers consistently offer retention controls, admin logging and contractual protections that the free tiers do not. Same model, different risk.

Two other shifts: model deprecation is now a planning problem, since vendors retire checkpoints on their own schedule, so notice periods belong in the contract; and provenance metadata (the C2PA standard) is appearing in more generated media, which gives buyers a verification option that did not exist before.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"All the big providers are basically the same on compliance."* They are similar in capability and materially different in terms.
- *"We don't train models, so governance is the vendor's problem."* Deployment liability stays with you; the vendor cannot see your workflows, prompts or customers.
- *"Open weights are safer because they run on our servers."* Self-hosting solves data egress and transfers all safety, patching and indemnity burden to you.
- *"A certification means the system is ethical."* It means a management process was audited, not that this use is fair.
- *"Greenest option is the smallest model."* It is the smallest model that meets the quality bar — an under-powered model that needs three retries is not efficient.

## How a student should understand it

**Mental model:** three renovation quotes. The cheapest is cheapest because it excludes the warranty, the permit and the disposal. You are not comparing price; you are comparing who carries what when something goes wrong.

**Things they can do after this bullet:**
1. Build a five-row comparison table (retention, training use, IP indemnity, audit/logging, model size) for any two providers.
2. Find the red flag in a provider's terms in under ten minutes.
3. Explain to a manager why the free tier is not an option for customer data, in one sentence.

**Misconceptions to kill:** that providers are interchangeable on compliance; that a vendor's certification covers your use; that price per seat is the cost.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Three renovation quotes.** As above. Where it breaks: renovation defects surface in months, while AI data-handling problems may surface years later, after the contract has been renewed twice.

**The VICOM inspection.** A used car with a valid inspection is not a good car — it is a car that passed a point-in-time check on specific items. Where it breaks: VICOM tests the physical vehicle against a fixed list; AI audits test a moving target against a standard that is still being written.

### Worked example with a real tool

Paste two providers' terms of service and let the model do the diff, then verify it:

```
Here are the data-processing sections from two AI providers (pasted below).
Build a comparison table with rows: retention period, use for training,
sub-processors, data location, IP indemnity, notice before model changes,
audit rights.

Then list, for each provider, the three questions I must ask their sales
team before signing, and flag any sentence that is ambiguous rather than
merely unfavourable.
```

What to point at afterwards: the model reads terms competently and will still invent a clause that is not there, or miss that "may use aggregated data" is a training permission. The lesson: use the model to structure the comparison, then read the two sentences it cites yourself.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two providers' retention clauses side by side; ask which the room would sign, then reveal what each actually permits.
2. **State the objective** — produce a five-row comparison and one red flag for a real tool your team uses.
3. **Recall prior learning** — `TSC8-Basic-K2`'s three checks; today they become purchase criteria.
4. **Present the content** — data handling, IP in/out, accountability and audit, certifications, environment, cost per outcome.
5. **Guide** — build the comparison table together from two real terms pages.
6. **Elicit performance** — pairs run the comparison for a tool their organisation already uses and report the red flag.
7. **Give feedback** — correct "the vendor is responsible" and "certified means safe"; insist on clause-level evidence.
8. **Transfer** — each learner writes the three questions they will ask before the next AI purchase.

## What the framework doesn't mention but trainers need to know

- **Free tiers are the actual risk in most SMEs.** Shadow AI is a procurement failure. If the sanctioned tool is worse than the consumer one, people will use the consumer one.
- **Contract terms beat marketing pages.** Teach learners where to look: data processing addendum, sub-processor list, indemnity clause, deprecation policy.
- **Model deprecation is an unglamorous, high-impact risk.** A workflow built on a specific checkpoint breaks when the vendor retires it; notice periods and version pinning belong in the deal.
- **Ask for the model card before the demo.** A vendor who cannot produce one has told you something useful.
- **Do not outsource the environment question to the vendor.** Ask what the product routes to and whether a smaller tier exists for routine work.

## Watch out

- **Do not let the comparison become a spreadsheet with no owner.** Every criterion needs someone who will check it and a date when it was last checked.
- **Do not treat certifications as a pass.** Say plainly what ISO/IEC 42001 covers and what it does not.
- **Do not compare on capability alone.** Two models producing the same output can carry completely different liability.
- **The stale claim to retire:** "compliance is legal's job." The person who chooses the tool has already made the compliance decision.
