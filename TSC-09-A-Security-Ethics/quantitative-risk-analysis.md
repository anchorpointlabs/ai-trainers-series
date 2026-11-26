---
id: 09.03.A.K6
tsc: 9
level: Advanced
code: K6
title: Quantitative risk analysis
---

# Quantitative risk analysis

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Knowledge K6**

> **Framework text (verbatim):** "Quantitative risk analysis techniques (e.g., Monte Carlo simulation, decision tree analysis)."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Knowledge · Bullet 6 of 12

**One-line version:** A number with a range beats a colour with a feeling — not because the number is true, but because it can be argued with, compared and revisited.

## What it is

Quantitative risk analysis replaces verbal risk bands with estimates of likelihood and impact, combined by explicit rules. Two standard techniques do most of the work: **Monte Carlo simulation**, which samples uncertain inputs many times to produce a distribution of outcomes, and **decision tree analysis**, which lays out choices, chances and costs so alternatives can be compared on expected value.

## Deep expansion

### The concept

Low / medium / high is a vocabulary, not a measurement. It compresses two dimensions into one word and hides the reasoning, so two people can agree on "medium" while meaning opposite things — one thinking of a nuisance, the other of a regulatory breach. The moment risk is expressed as "probability × impact", disagreement becomes productive: you can ask which input is disputed, test that input, and see whether the decision changes.

The value of quantification is therefore not precision. It is **decomposability**. A number like "expected loss of about $30,000, driven mostly by the chance of a data-exposure incident" invites a challenge to the probability, the impact, or the assumption that both are independent. "High" invites nothing.

The honest framing for trainers: these techniques make assumptions visible and comparable. They do not make the future known, and a confident decimal is a red flag rather than a sign of rigour.

### The sub-concepts

**Expected value.** Multiply probability by impact and add across scenarios. It is the workhorse, and it has a known blind spot: it treats a small chance of a catastrophic loss as equivalent to a large chance of a small one. For severe, irreversible harms — a discriminatory denial of credit, a leaked customer database — expected value understates what matters, and a threshold or a hard rule belongs instead.

**Monte Carlo.** Identify the uncertain inputs (probability of an incident, cost per incident, detection delay, number of affected records), give each a range and a shape, then sample the combination thousands of times. The output is a distribution: a median, a range, and the chance of exceeding a limit. Its power is in showing that uncertainty in inputs produces a much wider range of outcomes than intuition suggests. Its danger is that a simulation looks authoritative while resting entirely on the ranges someone guessed.

**Decision tree.** Nodes for decisions, branches for chance events, costs at the leaves. Work backwards, weighting each branch by its probability. The exercise below is the standard shape: comparing launching now against delaying to test.

**Sensitivity analysis.** Vary one input at a time and see which one moves the answer. Usually one or two inputs dominate, and those are where measurement effort should go — not where the spreadsheet is prettiest.

**Single loss expectancy and annualised loss.** A classic insurance-style decomposition: asset value × exposure factor gives the loss per event; multiply by the annual rate of occurrence for the yearly figure. Crude, and useful precisely because it forces you to name the asset and the frequency separately.

**Cost of the control.** Every mitigation has a price — engineering time, latency, false positives, spend. A risk decision is only complete when the control cost sits on the same scale as the risk it reduces.

### How it connects to the rest of the framework

K5 needs these numbers to fill a register meaningfully; without them, appetite statements cannot be tested. A5 writes the thresholds that the numbers inform. A6 decides which gate consumes the analysis. K3's false-positive and false-negative rates are the inputs a guardrail decision needs. K1's acceptance bar is, in effect, a quantified risk threshold.

### What is current as of November 2026

- **Token economics made AI risk priceable.** Spend per request is knowable per model tier, so a denial-of-wallet exposure can now be estimated rather than described — and the same arithmetic justifies routing cheap tasks to cheaper models.
- **Agent loops added a new loss shape.** Runaway tool use produces fast, bounded, dollar-denominated losses, which is exactly the case where a cap outperforms an estimate.
- **Vendor pricing moves.** Comparing GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon on cost per task is now part of the risk case for a design, not a procurement afterthought.
- **Regulatory penalties are writable into the model.** Where statute sets a maximum penalty as a share of turnover, the impact term has an upper bound you can look up rather than invent.

### Common misconceptions

- *"Quantification means certainty."* It means explicit assumptions. The distribution is the output; the precision is an artefact of the arithmetic.
- *"Monte Carlo needs special software."* A spreadsheet with a random-number column and a thousand rows does the job for teaching, and for many real decisions.
- *"If I cannot quantify it, it does not count."* Unquantified harms still happen; the correct move is to quantify what you can and put a hard rule around what you cannot.
- *"Expected value settles the decision."* It settles comparisons. Rules, thresholds and reversibility settle the rest.

## How a student should understand it

**Mental model:** a weather forecast. Nobody thinks "70% chance of rain" is a claim about the future; they still take the umbrella, and they still know the forecast is a distribution rather than a promise.

**Things they can do after this bullet:**
1. Convert a "high/medium/low" rating into a probability, an impact and a range.
2. Build a decision tree for a launch-or-delay choice and read the expected cost.
3. Say which input the answer is most sensitive to, and how they would test it.

**Misconceptions to kill:** that numbers end arguments, that simulation requires special tools, and that severe-but-rare harms can be averaged away.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Travel insurance.** You do not know whether the bag will be lost. You know roughly how often it happens and what replacement costs, and you buy cover accordingly. Nobody calls that paranoid; everybody calls a "medium risk" label useless. Where it breaks: insurance prices many independent events, while one AI incident can be correlated across thousands of customers at once.

**COE bidding.** You form a distribution over the next round's price, pick a bid, and accept that a tail outcome is possible. The decision is made under uncertainty with a number, not a feeling — which is exactly the skill being taught.

### Worked example with a real tool

```
You are a risk analyst. Compare two options for an AI feature.

Option A — launch now: 60% chance of a data-exposure incident costing $50,000;
40% chance of no incident.
Option B — delay two weeks to test: testing costs $5,000, and reduces the incident
probability to 20% (same $50,000 impact if it happens).

1. Draw the decision tree in text.
2. Compute the expected cost of each option.
3. State which option is cheaper and by how much.
4. Name the two assumptions that, if wrong, would flip the answer, and how you would
   test each one.
```

Expected cost: launch now is 0.6 × $50,000 = $30,000. Delay is $5,000 + 0.2 × $50,000 = $15,000. The delay is cheaper by $15,000. (These figures come from the exercise; they are illustrative, not benchmarks.)

What to point at afterwards: step four. The arithmetic took a minute; the judgement is in noticing that the answer flips if the incident cost is much lower, or if the delay slips to two months. Also point at what expected value ignores — a single $50,000 exposure is survivable, while a comparable regulatory penalty with a turnover-based maximum is not, and that difference belongs in a rule rather than an average.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two teams, same project, one says "medium", one says "high"; neither can explain why.
2. **State the objective** — build a decision tree and a range, and defend one choice with numbers.
3. **Recall prior learning** — how they justify a purchase or a hire under uncertainty.
4. **Present the content** — expected value, trees, Monte Carlo, sensitivity, the limits.
5. **Guide** — compute the launch-now branch together on the board.
6. **Elicit performance** — pairs complete the delay branch and the sensitivity question.
7. **Give feedback** — check whether the probability is stated as an assumption and whether a tail risk was handled by a rule.
8. **Transfer** — each learner quantifies one live decision from their own work.

## What the framework doesn't mention but trainers need to know

- **Probabilities in this domain are judgements.** Say so, and pair each number with who judged it and what evidence exists.
- **Correlation ruins averages.** One poisoned document read by ten thousand users is not ten thousand independent events.
- **Round to what you know.** "$30,000" is a claim of precision; "roughly $30,000, with a range of $10,000 to $80,000" is a claim of honesty.
- **The control cost is part of the answer.** A guardrail that costs more than the expected loss is a decision, not a failure.
- **Reversibility changes the maths.** A reversible experiment deserves a lower bar than an irreversible deployment, and no expected-value calculation will tell you which you are doing.

## Watch out

- **Do not let learners leave with a false decimal.** The teachable claim is "this is how to argue about risk", not "this is the risk".
- **Do not simulate what you have not defined.** A Monte Carlo over guessed ranges produces a confident guess.
- **Do not use expected value on catastrophic, irreversible harms.** Use it for comparisons and put a hard limit where the tail is unacceptable.
- **The stale claim to retire:** "quantitative analysis is for actuaries." As of November 2026, any team with a token bill and an incident log has the inputs to do this on a spreadsheet.
