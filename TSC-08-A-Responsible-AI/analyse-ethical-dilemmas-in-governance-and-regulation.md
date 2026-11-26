---
id: 08.03.A.A5
tsc: 8
level: Advanced
code: A5
title: Analyse ethical dilemmas in governance and regulation
---

# Analyse ethical dilemmas in governance and regulation

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A5**

> **Framework text (verbatim):** "Analyse ethical dilemmas in AI governance, regulation, and global contexts."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 9 of 14

**One-line version:** A dilemma is two goods in tension; if one side is obviously wrong, you have a problem, not a dilemma.

## What it is

Analysis of a dilemma means laying out what each side protects, who holds each stake, what each option costs, and then arguing a position that a reasonable opponent could respect. In AI governance the recurring pairs are privacy against security, innovation against precaution, global consistency against local values, and one fairness metric against another. The work is not to find the option with no cost. It is to choose a cost knowingly, in public, and to record why.

## Deep expansion

### The concept

Most governance arguments fail before they start, because the parties define the dilemma as good against bad. Surveillance is "safety versus rights"; open weights are "innovation versus safety". Each framing guarantees that the other side is either naive or malicious, and no decision survives that.

The analytic move is to convert the dispute into four columns. **What each side protects** — the good, not the slogan. **Who holds it** — named stakeholders, including the ones who are not in the room. **What each option costs** — including the cost of doing nothing. **What would change your mind** — the evidence that would flip the recommendation. A position that cannot name the fourth is a preference.

Then apply a decision rule and say which one you used: precautionary (act only when the risk is understood), proportionality (the intrusion fits the benefit), harm minimisation (accept small harms to avoid large ones), or rights-based (some things are not tradeable at any price). Different rules give different answers on the same facts, and the rule you choose is itself an ethical commitment.

### The sub-concepts

**Steel-manning.** State the opposing case in its strongest form, better than its own advocates do. If you cannot, your analysis is a straw man with footnotes.

**Stakeholder asymmetry.** The people most affected are often least represented: the gig rider deactivated by a fraud model, the patient whose scan is triaged, the annotator who labelled the data. Naming them changes the options.

**Time horizon.** Deployers weigh this quarter; the affected weigh the next decade. Most dilemmas are disagreements about which horizon counts.

**Cross-border asymmetry.** A rule that is proportionate in one jurisdiction is excessive in another, and the product is often the same. The dilemma is whether to build to the strictest market or to fragment.

**Documented dissent.** A decision record that includes the losing argument is the mark of a serious process, and it is what makes the decision defensible later.

**The impossibility result.** When fairness metrics conflict mathematically, "choose the fairest" is not an option; someone must choose which fairness, for whom, and say so.

### How it connects to the rest of the framework

`TSC8-Advanced-K3` supplies the cross-border facts; `TSC8-Advanced-K4` supplies the four lenses that generate the tension; `TSC8-Advanced-A7` assesses the interplay formally; `TSC8-Advanced-A6` critiques the policy that resulted; `TSC8-Advanced-A1` is where the chosen position is recorded as a gate decision.

### What is current as of November 2026

Three live dilemmas define the period. Convenience against control: agents that transact on your behalf — the tool-use layer now standard in OpenAI's GPT-6 generation, Anthropic's Claude 5.5 and Google's Gemini 3.1 Pro and 4 Argon — remove a human from the loop precisely where oversight matters most. Openness against misuse: capable weights released openly distribute both innovation and misuse, and no regulator has resolved which cost is acceptable. Detection against privacy: systems built to spot synthetic media must scan everyone's media, which is a surveillance architecture built for a good reason. A trainer teaching only the 2020 dilemmas (bias in hiring, privacy in training data) is teaching history as though it were current events.

### Common misconceptions

- *"Every dilemma has a right answer if you think hard enough."* Some are genuinely undecidable on the evidence available; you choose and you monitor.
- *"Presenting both sides is analysis."* Both-sidesism without stakeholders, costs and a decision rule is a book report.
- *"Stakeholders means customers."* It means affected parties, including those who never interact with the system.
- *"The regulator will resolve it."* Regulators lag the dilemma by years; products ship in months.

## How a student should understand it

**Mental model:** two fire exits, one of which is locked for security. Both choices protect someone, and the argument is which protection you buy with which risk.

**Things they can do after this bullet:**
1. Reframe a good-versus-bad argument into two goods in tension.
2. Name the stakeholders, the costs and the evidence that would flip the decision.
3. State a defensible position and the rule it rests on.

**Misconceptions to kill:** dilemmas have clean answers, both sides is analysis, and only customers count as stakeholders.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Two fire exits, one locked.** Locking the side door stops theft; it also removes an evacuation route. Both measures protect people. The decision is made in a risk assessment, recorded, and revisited after every incident. Where it breaks: a building has an inspector who can require both; AI dilemmas often have no inspector at all.

**The COE system.** It trades access against congestion and is defensible on its own terms, yet nobody describes it as cost-free. Every driver pays a visible price for a collective benefit, and the argument is about the level, not the existence. Where it breaks: COE costs are priced and legible; the costs of an AI decision land on people who never see the price.

### Worked example with a real tool

```
A city proposes AI that scans public messages for threats.
Argue both sides in their strongest form, then state a position.
Include: what each side protects, who bears each cost, which decision rule
you are applying, and what evidence would change your mind.
```

What to point at: the model will produce balanced prose, and balanced prose is the failure mode. Ask which column names the people who will be scanned most and can least contest it. Then ask what evidence would flip each side — a question the output almost never answers well, and the one that separates analysis from opinion.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a headline where both sides are described as protecting children. Ask who is lying.
2. **State the objective** — reframe, map stakeholders, argue, and name the decision rule.
3. **Recall prior learning** — the four lenses from `TSC8-Advanced-K4`.
4. **Present the content** — the four-column method and the decision rules.
5. **Guide** — run the message-scanning case together, filling the columns.
6. **Elicit performance** — pairs take a dilemma from their own sector.
7. **Give feedback** — reject positions without a stated cost or a flip condition.
8. **Transfer** — each learner writes a 150-word decision note with the dissent recorded.

## What the framework doesn't mention but trainers need to know

- **The decision rule is usually implicit.** Surfacing it ("we are being precautionary here") is what makes a debate tractable.
- **Dissent is evidence of rigour.** A record with no dissent usually means no one was asked.
- **Reversibility matters more than optimality.** Prefer decisions you can unwind when the facts change.
- **Some dilemmas are budget disputes in disguise.** Ask what the option would cost and whether the money exists.

## Watch out

- **Do not let the class settle on "it depends".** That is the start of analysis, not the end.
- **Do not stage a debate without a decision.** Debate without a decision record trains rhetoric, not governance.
- **Do not import a US or EU dilemma as if it were local.** The stakeholders differ, and so does the law.
- **The stale claim to retire:** "Both sides have valid points." Everyone can say that; the skill is choosing and defending.
