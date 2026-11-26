---
id: 03.03.A.A3
tsc: 3
level: Advanced
code: A3
title: Evaluate prompt engineering techniques
as_at: 2026-11-26
review_by: 2027-02-25
---

# Evaluate prompt engineering techniques

> **TSC #3 Prompt Engineering · Advanced · Ability A3**

> **Framework text (verbatim):** "Evaluate the performance and limitations of prompt engineering techniques."
>
> **TSC #3** Prompt Engineering · **Advanced** · Ability · Bullet 10 of 13

**One-line version:** Write the marking scheme before you read the scripts, or you are not evaluating — you are choosing.

## What it is

A technique is a hypothesis: few-shot will fix the boundary cases, chain-of-thought will fix the arithmetic, the schema will fix the formatting. Evaluating is running the experiment — a fixed check, a set of inputs, a score per criterion, and a stated limitation at the end. The deliverable is not "it works". It is "it passes four of five on format and three of five on faithfulness, and it fails when the input has no date".

## Deep expansion

### The concept

Evaluation fails for one reason above all others: the criterion is decided after the output is seen. A model produces something fluent, the reader is impressed, and the rubric is reverse-engineered to fit. That is not measurement, and it cannot distinguish two prompt versions, because both will be judged against whichever output arrived first.

The fix is administrative, not technical: write the pass/fail sentence before generating anything. Then run the same inputs through both versions and score. It is the same discipline as marking exam scripts against a scheme rather than against the best script you have read.

The second half of the bullet is *limitations*. Every technique has a ceiling and a domain. Few-shot fixes boundary confusion and introduces label bias. Chain-of-thought fixes multi-step arithmetic and wastes tokens on lookups. Structured output fixes parsing and starves the model of space to reason, unless the schema puts a reasoning field first. A technique described without its failure mode has not been evaluated, only admired.

### The sub-concepts

**Deterministic checks first.** Valid JSON, an allowed label, a required field present, a word count in range, a forbidden string absent. These are free, instant and unambiguous — use them wherever the criterion allows, and reserve human or model judgement for qualities a rule cannot express.

**A judge needs a rubric, not a mood.** If you use a model to grade, give it the criteria, the scale, and an instruction to quote the evidence. Unguided judges reward length and confidence.

**Build a small test set, deliberately mixed.** Twenty to fifty real inputs: the routine majority, a substantial share of awkward ones (ambiguous phrasing, missing fields, very long input), and a few adversarial ones (empty, contradictory, out of scope). A set drawn only from easy cases measures nothing.

**Score per criterion.** One number hides the trade. A technique can improve format validity while degrading faithfulness — common with aggressive formatting constraints.

**Compare like with like.** Same model snapshot, same temperature, same inputs, same grader. A comparison across two models measures the models.

**Cost is a criterion.** Self-consistency at five runs costs five times the tokens; a two-stage chain doubles latency. A technique that improves accuracy by a point at triple the cost is a decision, not a victory.

**Watch for regression.** Fixing case fourteen routinely breaks case three. Re-run the whole set after every change, or the improvement is unverified.

### How it connects to the rest of the framework

Bullet 3 (`TSC3-Advanced-K3`) is the optimisation loop this bullet makes honest; Bullet 6 (`K6`) is the harness that automates it; Bullet 11 (`A4`) applies the same check to a *different* scenario, which is how you discover the limitation. Bullet 12 (`A5`) uses the score to decide what to change next. `TSC5` covers evaluation as its own discipline, including model-level benchmarking.

### What is current as of November 2026

- **Model-as-judge is now the practical grader** for qualities that resist rules — faithfulness, tone, completeness — when it is given a rubric and a scale. It is also a known source of bias toward its own family's style, which is why paired human checks on a sample still matter.
- **Evaluation moved into the delivery pipeline.** Running the test set on every prompt change, and on a sample of live traffic, is ordinary practice rather than a quarterly exercise. With the late-2026 frontier models (GPT-6 generation, Claude 5.5, Gemini 3.1 Pro, Gemini 4 Argon) changing behaviour across versions, an untested prompt is an unpinned dependency.
- **Public benchmarks stopped being a proxy.** Leaderboard position does not predict performance on your twenty inputs. Local evaluation is the only evidence that transfers.

### Common misconceptions

- *"It feels better."* Then it is not evaluated. Write the criterion and check.
- *"It passed my example."* One input is a coin toss. Twenty mixed inputs is a measurement.
- *"Accuracy is one number."* Format, faithfulness, abstention, latency and cost are separate scores, and they trade.
- *"A technique that worked once keeps working."* Models, data and prompts drift. The score has a date.
- *"The judge said it was good."* A judge without a rubric rewards length and confidence. Give it criteria and ask for evidence.

## How a student should understand it

**Mental model:** PSLE marking. The scheme is written before the scripts arrive, two markers score independently, and a discrepancy triggers review — never "this one feels like an A".

**Things they can do after this bullet:**
1. Write a three-criterion check for a prompt, with a scale and a pass threshold.
2. Run two prompt versions on five inputs and produce a score per criterion.
3. State one limitation of a technique from the results, in a sentence someone else could act on.

**Misconceptions to kill:** that fluency is quality; that one example is a test; that a technique has no ceiling.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**PSLE marking.** The scheme exists before the scripts, because otherwise the first good script defines the standard. Where it breaks: examiners are trained to a common standard and moderated; your judge is a model or a tired colleague, so the rubric has to be written down and applied mechanically.

**The taste test with a score sheet.** Two brands of chicken rice, ten tasters, five criteria — rice, chilli, portion, price, queue. Where it breaks: tasters agree on deliciousness; prompt quality criteria are more contested, so the criteria have to be defined in words that a stranger could apply.

### Worked example with a real tool

```text
Rubric: the answer must (1) give the correct total, (2) show working,
(3) be under 80 words. Score each prompt's output 0-3.
```

Run three variants on the nurse-staffing calculation: plain, chain-of-thought, and chain-of-thought with a word limit. Score all three against the same rubric. The plain version often scores 1 (right total, no working); CoT scores 2 (right total, working, too long); CoT with a limit scores 3 or drops to 2 because compression clipped the working. Point at the last case: the third criterion fights the second, and only a per-criterion score reveals it. That is what "limitations" means in practice.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two outputs, ask which is better, then reveal that the room used different criteria.
2. **State the objective** — write a rubric, score two versions, and state a limitation from the numbers.
3. **Recall prior learning** — how they mark a colleague's draft, and whether they say the criteria out loud first.
4. **Present the content** — rubric before results; deterministic versus judged checks; test-set mix; per-criterion scoring; cost and regression.
5. **Guide** — score two versions together on the board, arguing each mark.
6. **Elicit performance** — learners write a rubric for their own prompt and score three versions of it.
7. **Give feedback** — swap rubrics. The usual finding is criteria that cannot be applied by a stranger.
8. **Transfer** — each learner adds one deterministic check to a prompt they run weekly.

## What the framework doesn't mention but trainers need to know

- **Sample size is the hidden variable.** Five cases tells you about five cases. If the answer matters, twenty is the floor and the mix matters as much as the count.
- **Judges have house bias.** A model grader favours its own family's phrasing. Rotate the judge or anchor it with examples of acceptable and unacceptable answers.
- **Inter-rater disagreement is information.** When two humans score the same output differently, the criterion is vague — fix the rubric before blaming the model.
- **Score the abstention case explicitly.** A prompt that is right on answerable inputs and invents on unanswerable ones is dangerous, and a test set of answerable inputs will never show it.
- **Write the score down.** An evaluation with no record is an opinion that was briefly held.

## Watch out

- **Do not grade by vibe in front of the room.** The room copies what you do, not what you say.
- **Do not use a rubric so vague that everything passes.** "Accurate and professional" is not a criterion.
- **Do not compare across models and call it a prompt comparison.** Hold the model fixed.
- **Do not hide the failures.** The interesting part of the debrief is which criterion failed and why.
- **The stale claim to retire:** "it passed the benchmark, so it's good." Your twenty inputs are the benchmark that matters.
