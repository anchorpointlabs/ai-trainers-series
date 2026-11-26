---
id: 08.02.I.A3
tsc: 8
level: Intermediate
code: A3
title: Mitigate bias and ethical risks
as_at: 2026-11-26
review_by: 2027-02-25
---

# Mitigate bias and ethical risks

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A3**

> **Framework text (verbatim):** "Implement strategies to mitigate bias and ethical risks in AI systems."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 8 of 14

**One-line version:** A mitigation is real only if it touches the cause — everything else is a gesture with a slide.

## What it is

Mitigating bias and ethical risk means choosing and implementing an intervention that reduces a named risk — in the data, the model, the output or the workflow — and then verifying that it worked. The choice depends entirely on a causal claim: this specific mechanism produced this specific disparity, so this specific intervention addresses it.

## Deep expansion

### The concept

Most mitigation fails for one of two reasons: it addresses a symptom, or nobody checked afterwards. A filter that blocks certain words does not remove a model's bias in tone; it hides the cases the filter was written for. A rebalanced training set does address the cause, but only if the disparity actually came from the sampling.

So the sequence is fixed. **Name the mechanism**, **choose the layer**, **implement**, **re-measure by group**, **record the residual**. Learners want to start at step three, because step three is the satisfying one, and step one is the one that takes a day of looking at data.

The second half of the concept is that mitigation always costs something, and somebody has to accept the cost. Calibrating thresholds per group to equalise true-positive rates will change false positives somewhere; making the assistant warmer to every name may make it warmer than your brand wants. The decision is a trade, and a trade made silently is a trade nobody owns.

### The sub-concepts

**Match the layer to the cause.** Five layers, roughly in order of durability:

1. **Data** — fix the sampling, correct the labels, add the missing cases. Most durable, slowest.
2. **Model** — constraints, reweighting, adversarial debiasing during training. Needs ML capability.
3. **Output** — post-processing calibration, groundedness checks, tone filters. Fast, treats symptoms.
4. **Process** — a human gate before the decision takes effect, with the time and information to use it.
5. **Scope** — do not use the model for this decision. Underused, and often correct.

**Guardrails are not mitigation.** A prompt filter or an output classifier is a control against a known failure pattern; it does not change the distribution that produces the pattern. Say this plainly, because "we added a filter" is the most common false closure in the field.

**Human gates need engineering.** A reviewer who clears 400 cases an hour is not a control. Real gates have time per case, the underlying evidence visible, an uncertainty signal, and no penalty for overriding.

**Verify by group, not overall.** Re-run the disaggregated evaluation after the fix. An overall improvement can hide a subgroup that got worse, which is common when you rebalance a dominant group's representation.

**Record the residual.** Some disparity will remain. State its size and direction in the model card. A named residual is a managed risk; an unmentioned one is a surprise waiting for a journalist.

### How it connects to the rest of the framework

`TSC8-Intermediate-K3` gives the mechanisms you are mitigating; `TSC8-Intermediate-A5` is the analysis that identifies which mechanism is operating; `TSC8-Intermediate-A4` is the privacy-performance trade-off that often constrains the fix. `TSC8-Intermediate-A8` is where mitigation becomes a pipeline step rather than a project, and `TSC8-Intermediate-A1` is the checkpoint at which it gets run.

### What is current as of November 2026

Mitigation tooling has consolidated around three practices: disaggregated evaluation suites run in CI, guardrail classifiers sitting in front of and behind the model, and red-team case libraries that grow with every incident. Singapore's Project Moonshot supplies both adversarial test recipes and localised evaluation material, which matters because a fix tuned to an American benchmark can leave the Singlish and Malay cases untouched.

Agents change the risk shape. For an agent, the highest-value mitigations are often permissions rather than filters: least-privilege tool access, an explicit approval step before any state-changing action, and a spend or step limit that stops a loop. The GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon all support tool use, so a mitigation plan that only covers text output is incomplete.

Model swaps also invalidate mitigation. A prompt that fixed a tone problem on one version may not hold on the next, which is why the change-control rule matters more than any individual fix.

### Common misconceptions

- *"We added a filter, so it is fixed."* You blocked the cases you thought of. The distribution is unchanged.
- *"The vendor fixed their model."* Their fix addresses their base model, not your corpus or your prompt.
- *"One mitigation is enough."* Bias usually has more than one mechanism; a durable fix often combines data work with a process gate.
- *"The metric improved, so the harm is gone."* Check which group improved and which group paid for it.

## How a student should understand it

**Mental model:** water coming through a wall. You can paint over it (output filter), fix the pipe (data), or stop using the room (scope). All three are legitimate; only one addresses the leak, and you should know which one you chose.

**Things they can do after this bullet:**
1. Name the mechanism behind a disparity before naming a fix.
2. Choose a mitigation layer and say what it costs and who accepts the cost.
3. Verify the fix by group and record what remains.

**Misconceptions to kill:** that a filter is a fix, that improvement overall means improvement for everyone, and that one intervention closes the issue.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The wet market drain.** The floor floods every afternoon. Mopping (a guardrail) gets you to closing time; re-grading the drain (the data) stops it happening. Both are work; only one is a fix. Where it breaks: a drain is visible, whereas the mechanism behind a model disparity is usually inferred from data rather than seen.

**The kopitiam "less sugar" order.** If the instruction stops at the counter and never reaches the kitchen, the drink arrives sweet and everyone blames the server. Prompt-level instructions that the retrieval step overrides behave exactly like this.

### Worked example with a real tool

```text
Our assistant gives shorter, colder replies when the customer's name suggests a
non-Chinese ethnic group. We have 300 sample conversations showing it.

1. What are the three most likely mechanisms, and what evidence would distinguish them?
2. For each mechanism, name the mitigation layer (data, model, output, process, scope)
   and what it would cost.
3. Design the check that tells us, after the fix, whether it worked — including which
   groups we compare and what we do if one gets worse.
```

What to point at afterwards: the model will propose prompt changes first, because they are cheap and it likes them. That is the symptom layer. Push it to justify a mechanism, and the answer usually moves to retrieval or fine-tuning data, which is where the real fix lives.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — play two replies to the same complaint, different names, and ask the room to spot the difference.
2. **State the objective** — by the end you can pick a mitigation that addresses a mechanism and verify it.
3. **Recall prior learning** — return to the proxies discussion from K3.
4. **Present the content** — five layers, guardrails versus fixes, human gate design, residual recording.
5. **Guide** — work the tone example through the three mechanisms.
6. **Elicit performance** — pairs take a risk from their own system and design a fix.
7. **Give feedback** — challenge every fix that has no verification step.
8. **Transfer** — each learner writes the change-control rule for their team.

## What the framework doesn't mention but trainers need to know

- **Mitigation has a budget.** A data-collection programme can cost more than the model. Say so, or the fix gets parked.
- **The affected group should test the fix.** Teams consistently mis-specify what "warmer" or "clearer" means for a group they are not in.
- **Residual risk needs a number.** "Reduced" is not a management statement; "disparate impact ratio moved from 0.71 to 0.86" is.
- **Fixes expire.** Every model version, corpus refresh and prompt change is a reason to re-run the check.

## Watch out

- **Do not claim "bias removed".** Claim what the measurement shows, at what threshold, on which groups.
- **Do not let a filter be presented as the fix** in a demo; a sceptical engineer will ask what happens to the case the filter does not match.
- **Do not hide the trade-off.** If equalising rates costs precision, the business needs to know before launch, not after.
- **The stale claim to retire:** "we will fix bias in the next model version." Bias is a property of your data and workflow, and the next version inherits both.
