---
id: 05.02.I.A3
tsc: 5
level: Intermediate
code: A3
title: "From score to cause: diagnosing performance issues in evaluation data"
---

# From score to cause: diagnosing performance issues in evaluation data

> **TSC #5 Generative AI Model Evaluation · Intermediate · Ability A3**


> **Framework text (verbatim):** "Analyse performance issues based on evaluation data."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Ability · Bullet 11 of 12

**One-line version:** A low score is a symptom; the ability is reading the failures until a taxonomy appears, then changing one thing at a time to find which stage actually caused it.

## What it is

This is the diagnostic ability that turns evaluation results into a cause. It means reading a sample of failures, labelling them into an error taxonomy, localising the failure to a stage (prompt, retrieval, model, data, product), and confirming the localisation with a controlled change. It ends with a fix that is aimed, and with evidence that the fix worked on the same test set.

## Deep expansion

### The concept

The reflex when a score is low is to change the model. It is almost always the wrong first move, for a simple reason: in a generative application, the model is one component among several, and the other components fail more often and more cheaply to fix. Retrieval misses the policy clause; the prompt does not specify the output format; the test set includes an input type the product never sends in practice; the document was scanned and the text extraction was bad. The model faithfully answered a question nobody asked.

Diagnosis is therefore an exercise in evidence discipline. You cannot fix what you cannot label, and you cannot label what you have not read. The highest-value hour in most evaluation projects is reading a hundred failures and writing a short taxonomy — not because the taxonomy is sophisticated, but because it converts a diffuse sense of "bad" into a count of things that can each be fixed.

### The sub-concepts

**Read the failures first, in bulk.** A hundred outputs, opened, read, and annotated in your own words. Twenty is not enough: generative failures are long-tailed and the pattern only appears past the obvious cases. Do this before opening a dashboard.

**Build a taxonomy that is small and actionable.** Six to ten categories: fabricated fact, missing required element, wrong policy interpretation, format break, wrong tone, unhelpful refusal, ignored instruction, truncated. Each category must map to a different fix, or it belongs in the same bucket as its neighbour.

**Count, then slice.** Once labelled, the counts tell you where the score went. Then cross-tabulate against slice: if fabricated facts concentrate in one document type, the cause is likely retrieval or extraction; if they are spread evenly, it is more likely the model's tendency to fill gaps.

**Localise the stage with counterfactual probes.** Change exactly one thing and re-run the failing items:

- Same prompt, better context → tests retrieval and grounding.
- Same context, stricter prompt → tests instruction-following.
- Same everything, stronger model → tests capability.
- Same everything, cleaner input (properly extracted text) → tests the data pipeline.

If only one probe moves the failures, you have found the stage. If none do, your taxonomy is probably wrong, and that is also a finding worth the hour.

**Distinguish a regression from a longstanding weakness.** Compare against the previous run's records. A drop that appears at the same time as a prompt edit is a regression; a failure present in every version is a capability limit and needs a product decision, not a fix.

**Check the test set before blaming the model.** The input may be malformed, out of the intended scope, or duplicated. A surprising share of "failures" are test-set errors, and finding them early saves a week.

**Treat cost and latency as performance.** A solution that raises quality by doubling latency may be a worse product. Performance issues include the ones the customer feels.

**Reproduce before you fix.** If you cannot re-run the failing case and see it fail again, you cannot tell whether your fix worked.

### How it connects to the rest of the framework

`A1` supplies the records; `K4` supplies the rubric dimensions that become your failure categories; `K6` tells you whether the drop you are chasing is real; `A2` shows you which slice to look at. `TSC5-Basic-A3` (propose improvements from findings) is the entry-level version of the same loop. Upstream, `TSC6-*` covers the application-side troubleshooting this feeds, and `TSC7-*` the model-side debugging when the cause really is capability.

### What is current as of November 2026

Error analysis as a named practice has become standard rather than artisan: teams keep a failure taxonomy per product and label every evaluation run against it, so the categories accumulate evidence over time. Agent pipelines now emit traces with a span per step, which makes localisation much easier — you can see whether the failure happened in the retrieval call, the tool call or the final synthesis. Judge models are increasingly used to *triage* failures into candidate categories, with a human confirming; the rule that has settled is that machine clustering proposes and humans name.

### Common misconceptions

- *"Low score, so swap the model."* Most failures in a generative application are not model failures.
- *"Look at the worst examples."* The worst examples are often pathological inputs. The informative ones are the typical failures in the middle of the distribution.
- *"Add more instructions to the prompt."* Prompt bloat is a common *cause* of instruction-following failures, not a fix for them.
- *"If it fails 5%, it's the model's fault."* Five per cent may be entirely explained by one document type going through a broken extraction step.

## How a student should understand it

**Mental model:** the MRT delay post-mortem. Train fault, signalling fault, or a passenger incident — three different owners, three different fixes, and the report's first job is to separate them before anyone is blamed.

**Three things they can do after this bullet:**
1. Read twenty failures and produce a six-category taxonomy with counts.
2. Run a one-variable probe matrix and localise the failure to a stage.
3. Say whether a finding is a regression or a longstanding limitation, with the evidence.

**Misconceptions to kill:** low score means bad model, worst examples are most informative, and more prompt instructions is a fix.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT delay post-mortem.** Nobody fixes a delay by buying new trains until the report says where the delay started. The discipline is separating the stages, and it is the same discipline here.

**The clinic's fever.** A fever is a symptom shared by twenty conditions. Treating every fever with the same medicine is what you do when you have no diagnosis — and it is exactly what "just use a bigger model" is.

### Worked example with a real tool

Start with the taxonomy, not the fix:

```
Here are 20 failed replies from our evaluation, each with the source
document and the customer email.

1. Label each failure with ONE primary cause, in my own words, and give
   the label in three words or fewer.
2. Group the labels into a taxonomy of at most 6 categories.
3. For each category, tell me which is more likely: the retrieval missed
   the relevant clause, the prompt was unclear, the model invented
   something, or the input was malformed. Say why you think so.
4. What single change would test your top hypothesis, and what result
   would confirm it?
```

Then the probe matrix the class fills in together:

```
Probe                          Changed         Failures fixed / 20
Baseline                       —               0
Better context (gold clause)   retrieval       14
Stricter format instruction    prompt          2
Stronger model                 model           3
Cleaner extracted text         data            11
```

What to point at afterwards: two probes moved most of the failures, which means two causes and two owners. The model upgrade — the instinctive first move, and the expensive one — fixed three. That table is the deliverable skill of this bullet.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a 62% score and ask what everyone would do first. Write the answers up; most will say "change model".
2. **State the objective** — you will produce a taxonomy and localise the cause with one-variable probes.
3. **Recall prior learning** — the rubric dimensions from K4 become the failure labels.
4. **Present the content** — read-then-count, taxonomy design, the four probes, regression versus limitation, test-set errors.
5. **Guide** — label ten failures on the board as a class and argue about two ambiguous ones.
6. **Elicit performance** — teams label their own twenty failures and propose one probe.
7. **Give feedback** — collapse over-fine taxonomies, split ones that mix causes with symptoms.
8. **Transfer** — they run the probe on their own pipeline and report the stage.

## What the framework doesn't mention but trainers need to know

- **Failure taxonomies are product knowledge.** The same six labels do not fit a support bot and a code assistant. Rebuild per product, and keep the labels stable enough to compare over time.
- **The fix often belongs to someone else.** If the cause is document extraction, the model team cannot fix it, and the evaluation has just done its most useful job: routing.
- **Watch for fix-induced regressions.** A stricter prompt fixes format failures and creates refusals. Always re-run the full test set after a targeted fix, not just the failing items.
- **Some failures should be accepted.** A model that fails 2% of out-of-scope inputs while refusing them politely may be correct behaviour. Diagnosis includes deciding what "good" would even look like.

## Watch out

- **Do not diagnose from aggregate numbers.** If the session never opens a single failure, it is a lecture about charts.
- **Do not let the room propose a fix in the first ten minutes.** The instinct is the thing being trained out.
- **Do not confuse correlation with cause in slices.** "Fails more on long documents" may mean "fails more on scanned documents", which are also long.
- **The stale claim to retire:** "we need a better model." Sometimes true. Far more often the evidence points at the two hundred lines around the model.
