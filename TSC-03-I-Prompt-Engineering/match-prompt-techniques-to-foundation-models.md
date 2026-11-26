---
id: 03.02.I.A5
tsc: 3
level: Intermediate
code: A5
title: Match prompt techniques to foundation models
as_at: 2026-11-26
review_by: 2027-02-25
---

# Match prompt techniques to foundation models

> **TSC #3 Prompt Engineering · Intermediate · Ability A5**

> **Framework text (verbatim):** "Identify which prompt techniques are best-suited for specific foundation models."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Ability · Bullet 11 of 13

**One-line version:** A prompt is coupled to the model's post-training — same words, different model, different result — which is why you test rather than transplant.

## What it is

Matching techniques to foundation models means knowing that families and tiers differ in how they read instructions: which delimiters they were trained on, whether they reason internally, how strictly they follow format constraints, how verbose they default to, when they refuse. The skill is to test a technique against your model on your task, adapt it, and re-test when the version changes.

## Deep expansion

### The concept

Two prompts that differ only in wording can behave identically on one family and differently on another, because models are shaped by post-training: the instruction pairs they were fine-tuned on, the preferences they were aligned to, the formats that dominated both. A prompt written for one family quietly encodes those assumptions — XML tags because Claude handles them well, a hand-written reasoning scaffold because a chat model needs one, a particular role stack because it once helped.

The consequence is a discipline, not a preference: the portable part of a prompt is the **substance** — task, supplied facts, output schema, failure branch. The **decoration** — delimiter style, persona stack, magic phrases — is where the family-specific behaviour lives. So matching means keeping the substance and testing the decoration on the model in front of you.

### The sub-concepts

**Dialects.** Claude models are comfortable with XML tags and use nesting well; GPT-line models read Markdown headings and JSON schemas readily; reasoning tiers in every family respond best to a clean statement of the task and the output contract. The same content, retagged, can move format compliance by a visible margin — which is a five-minute test, not a belief to argue about.

**Tier matters more than brand.** Within one family the fast tier and the reasoning tier behave more differently than two families at the same tier. Extraction and classification want the fast tier at low temperature; multi-step analysis and policy tests want the reasoning tier; ideation wants the fast tier because deliberation converges.

**Strictness of instruction-following varies.** "Exactly three bullets, no preamble" is obeyed literally by some models and approximated by others. Test format compliance as a separate property from answer quality — a model that gets the content right and the shape wrong is unusable in a pipeline.

**Verbosity and refusal posture vary.** Defaults for length, hedging and declining differ. "Be concise" is a weak instruction everywhere and a different instruction on each model. An abstention rule must be tested, because aligned models are trained to be helpful and will guess.

**Version drift is the quiet failure.** Floating aliases change under you; snapshots do not. Pin the version, keep the twenty-case test set, and re-run it before and after any migration. Prompt drift — a prompt degrading because the model or the input distribution changed — is the reason a prompt is never "done".

**The portability checklist.** Before moving a prompt: does the format hold? does it stay grounded in the supplied text? does it abstain when it should? is the length right? what did latency and cost do? Twenty cases answer all five.

### How it connects to the rest of the framework

`TSC3-Intermediate-K2` is the model landscape this bullet responds to, including its limits. `TSC3-Intermediate-A3` is the technique family being matched, `TSC3-Intermediate-A4` is the task-side match, and `TSC3-Intermediate-A1` is where version pinning and evaluation become part of the definition. `TSC3-Intermediate-K4` matters because context size and effective context differ by model.

### What is current as of November 2026

Convergence in capability, divergence in behaviour and price. The GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the Cyber variant), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon all follow schemas reliably and all offer reasoning tiers, which makes three practices standard:

- **Choose the tier before the technique.** Most "this prompt needs chain-of-thought" diagnoses are really "this task needs a reasoning tier" — and the reverse, where a reasoning tier is being spent on field extraction.
- **Keep prompts thin across families.** The task, the facts, the schema and the failure line move well. Persona stacks, magic phrases and elaborate role-play do not, and current models largely ignore them.
- **Test on your own twenty cases when a version changes.** Benchmarks will not tell you whether your invoice extraction still handles the stamp across the total.

### Common misconceptions

- *"A good prompt works on any model."* The substance travels; the behaviour does not. Format compliance and verbosity change first.
- *"The newest model is best for my task."* The newest reasoning model can be slower, dearer and worse at ideation than a fast tier. Match, then measure.
- *"If it fails on a new model, add more instructions."* Usually the fix is to remove scaffolding the new model does not need, or to restate the output contract.
- *"Testing is for engineers."* Twenty cases in a spreadsheet is the whole method, and it is a trainer-level skill.

## How a student should understand it

**Mental model:** the same recipe on a different stove. Induction responds in seconds and scorches; gas is slower and forgiving. You do not change the ingredients; you change the heat and the timing. Where it breaks: a stove is predictable, while a model can be updated overnight without telling you.

**Things they can do after this bullet:**
1. Run one prompt on two models and name three behavioural differences, not preferences.
2. Adapt a prompt for a reasoning tier by removing the scaffolding it no longer needs.
3. State which model and version produced a result, and why that matters to the reviewer.

**Misconceptions to kill:** that prompts are portable; that newest equals best; that more instructions compensate for a mismatch.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Two colleagues, one instruction.** Tell a detail-oriented auditor and a fast-moving sales lead "summarise this for management" and you get two different documents. Same words, different training. Where it breaks: colleagues ask clarifying questions; models do not.

**The rental car abroad.** Same controls, different places — the indicator stalk is on the other side and you signal with the wipers for the first day. Where it breaks: a rental car is a fixed model, while the model may be swapped mid-lease.

### Worked example with a real tool

Take one prompt and run it as-is on two tools:

```text
You are a meticulous senior analyst. Think step by step. Here are three customer
complaints. For each, classify severity as LOW, MEDIUM or HIGH with one line of
reasoning, and output a markdown table with columns ID | Severity | Reasoning.
```

Then the adapted version for a reasoning tier:

```text
Classify each complaint below as LOW, MEDIUM or HIGH severity using these definitions:
LOW — no money, no safety, no regulator involved.
MEDIUM — money or a repeated failure, no safety issue.
HIGH — refund demanded, injury mentioned, or regulator referenced.

Return a table: ID | Severity | Reason (one line, quote the phrase that decided it).
If the complaint does not fit any definition, use UNCLASSIFIED and say why.

<complaints>{{COMPLAINTS}}</complaints>
```

What to point at afterwards: the first prompt's persona and "think step by step" do the work on a chat model and add noise on a reasoning tier; the second replaces scaffolding with definitions — the part that actually decides borderline cases. Same task, adapted prompt, better audit trail.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run one prompt on two models and project both outputs.
2. **State the objective** — by the end you can adapt a prompt to a model tier and justify what you removed.
3. **Recall prior learning** — what do they know about how foundation models are trained and aligned?
4. **Present the content** — dialects, tiers, strictness, drift, the portability checklist.
5. **Guide** — adapt the classification prompt together, arguing about definitions versus scaffolding.
6. **Elicit performance** — pairs adapt one of their prompts for a different tier and note what they dropped.
7. **Give feedback** — run both versions on the same three inputs; compare format compliance, not just content.
8. **Transfer** — each learner writes the model and version into their prompt header, and the date they tested it.

## What the framework doesn't mention but trainers need to know

- **"Which model" is a commercial decision as well as a technical one.** Price per token, latency, data handling and procurement all belong in the answer, and none of them are in the prompt.
- **Model routing is now normal.** Triage to a fast tier, escalate hard cases to a reasoning tier. Intermediate learners should understand the shape even if they never build it.
- **Do not let the course become a brand argument.** Show differences, name the families, refuse to declare a winner.
- **Version pinning is a review requirement.** If a decision was made on a model output, the reviewer needs to know which model and when.
- **Open-weight models change the calculus.** For a narrow, high-volume task, a small fine-tuned model can beat a frontier model on cost and consistency — which is a different course, but the same matching logic.

## Watch out

- **Do not demo on a single input.** Differences show up on the awkward case, not the happy one.
- **Do not teach a leaderboard as knowledge.** Rankings change monthly and measure benchmarks, not your invoice format.
- **Do not blame the model for a stale prompt.** Check the input shape and the version before concluding anything.
- **The stale claim to retire:** "one prompt, every model." That was never true, and with reasoning tiers it is less true than it was.
