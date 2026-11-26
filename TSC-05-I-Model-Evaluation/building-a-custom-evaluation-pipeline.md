---
id: 05.02.I.A1
tsc: 5
level: Intermediate
code: A1
title: "Building a custom evaluation pipeline: from test set to decision"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Building a custom evaluation pipeline: from test set to decision

> **TSC #5 Generative AI Model Evaluation · Intermediate · Ability A1**


> **Framework text (verbatim):** "Implement custom evaluation pipelines for generative tasks."
>
> **TSC #5** Generative AI Model Evaluation · **Intermediate** · Ability · Bullet 9 of 12

**One-line version:** A pipeline is the difference between an opinion about a model and a number you can reproduce next month — same inputs, same scorers, same log, every run.

## What it is

A custom evaluation pipeline is the set of parts that take a versioned test set, run it through one or more model configurations, score the outputs by several methods, log everything, and produce a report with slices and intervals. Its defining property is reproducibility: anyone with the repository can re-run it and get the same numbers, and every number in the report can be traced back to the exact prompt and output that produced it.

## Deep expansion

### The concept

Everyone starts with a spreadsheet of prompts and a chat window. It works for a week and then fails in three predictable ways: nobody remembers which prompt version produced which score, the model was updated under the test, and the two people comparing results used different settings. A pipeline fixes those by making the choices explicit and the artefacts versioned.

The shape is always the same, whatever the tooling:

1. **Test set** — inputs, expected properties, slice labels, a version.
2. **Runner** — sends each input to a named model configuration, captures output, latency, tokens and cost.
3. **Scorers** — deterministic checks first, then reference-based metrics, then a rubric-backed judge, then a human review queue for the cases that matter.
4. **Store** — every record, so any score can be recomputed and any failure opened.
5. **Aggregate** — per slice, with intervals, plus a failure gallery.
6. **Gate and report** — a threshold that blocks a regression, and a one-page decision document.

The reason to build rather than buy is not that vendors are bad — several are good — but that the test set, the rubric and the gates are yours and nobody else has them. Those three are the asset; the harness is plumbing.

### The sub-concepts

**The test set is an artefact, not a file.** Version it, source it from real production inputs, include the awkward cases deliberately (misspellings, mixed languages, missing fields, long threads), hold out a portion you never tune against, and keep a canary set of items whose expected behaviour you know. Contamination is real: public benchmark items leak into training data, so private items are the only ones you can trust.

**The runner pins everything.** Model identifier and version, temperature and other parameters, system prompt version, retrieval index version if there is one, seed where supported. Log the request time. A score without its configuration is not reproducible.

**Layer the scorers, cheapest first.** A script checks format, required fields, banned phrases and citation presence for near-zero cost. Reference metrics (BLEU, BERTScore) check similarity where a reference exists. A judge model with the rubric scores judgement dimensions. Humans review the disagreements, the edge cases, and a random sample for calibration. Each layer catches what the one below cannot.

**Validate the judge like any other instrument.** Run it twice on the same items and measure how often it changes its mind; compare it against human scores on a sample; check for position and length bias by swapping the order of presented options. Report its agreement, not just its output.

**Log the whole record.** Input, output, model, parameters, scores, scorer versions, timestamps, cost, latency. When a score moves, you need to know whether the model, the prompt, the test set or the judge changed.

**Gate on regressions, not absolutes.** The most useful CI check is "this prompt change must not drop grounding below the last release by more than the interval". Absolute thresholds set the launch bar; relative gates protect it over time.

**Report once, in one page.** Decision rule, result with interval, per-slice table, failure gallery, cost and latency. If the pipeline produces forty pages, nobody reads the one that matters.

### How it connects to the rest of the framework

`TSC5-Intermediate-K4` gives the rubric the scorers implement; `K2` the metrics; `K6` the intervals and the gate's tolerance; `K3` the report's charts. `A2` analyses the distributions this pipeline emits, `A3` diagnoses what it finds, and `A4` closes the loop. `TSC5-Basic-A3` (propose improvements from findings) is the predecessor ability. On the engineering side, `TSC6-*` covers deployment into CI, and `TSC7-*` covers the training-side evaluation that this pipeline sits downstream of.

### What is current as of November 2026

Evaluation has consolidated into observability products — tracing, datasets, judges and dashboards in one place — and open harnesses remain popular for teams that need control. The judge is now treated as a component with its own tests rather than a magic scorer. Agentic systems have stretched the shape of the pipeline: the unit is a trajectory with intermediate steps, so the store has to hold spans, not just messages, and the scorers have to ask whether the task completed rather than whether one reply was good. Cost per evaluation run has become a line item, which is why layered scorers (cheap first, expensive last) is now standard advice rather than an optimisation.

### Common misconceptions

- *"A spreadsheet of prompts is a pipeline."* It has no versioning, no logging and no gate. It is a rehearsal.
- *"We can eyeball twenty outputs."* You can, once. You cannot eyeball the regression that a prompt change introduces next month.
- *"The pipeline is a one-off."* Its value is in the second run, and the tenth.
- *"More scorers means more confidence."* Correlated scorers add cost, not information.

## How a student should understand it

**Mental model:** the kaya toast line. Every slice goes through the same stations in the same order, and there is a quality check at the end. Skip the toaster and you do not blame the bread.

**Three things they can do after this bullet:**
1. Build a six-part pipeline for one real task, with a versioned test set and a log.
2. Add a regression gate that blocks a prompt change from shipping a worse result.
3. Trace any number in the report back to the exact prompt, output and configuration.

**Misconceptions to kill:** eyeballing is evaluation, the pipeline is disposable, and more scorers equals more truth.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The kaya toast line.** Same stations, same order, same check at the end — and when a customer complains, you can tell which station was cold. A pipeline gives you the same forensic ability on a model.

**The HDB BTO application system.** One form, one set of rules, one audit trail. Nobody argues about who was served because the process is identical for every applicant and every step is recorded.

### Worked example with a real tool

A minimal harness that shows the shape without hiding it — substituting your own model and scorer:

```python
import json, time
from openai import OpenAI

client = OpenAI()
ITEMS = json.load(open("testset_v3.json"))      # [{"id","input","slice"}]

def run(item, config):
    t0 = time.time()
    r = client.chat.completions.create(
        model=config["model"],
        temperature=config["temperature"],
        messages=[{"role": "system", "content": config["system"]},
                  {"role": "user", "content": item["input"]}],
    )
    return {"id": item["id"], "slice": item["slice"], "config": config["name"],
            "output": r.choices[0].message.content,
            "latency_s": round(time.time() - t0, 2),
            "tokens_out": r.usage.completion_tokens}

rows = [run(i, CONFIG_A) for i in ITEMS]
json.dump(rows, open("runs/2026-11-26_a.json", "w"), indent=1)
```

Then score the file separately, so that scoring can be re-run without paying for generation again:

```
You are scoring AI-drafted replies against our rubric. For each record
in the file, return JSON: id, grounded_1to5, complete_1to5, tone_1to5,
next_step_yes_no, gate_failure_reason_or_null.

Rubric: [paste rubric with anchors]
The source document for each id is in the "source" field. Judge only
against that source. If the reply states a fact not in the source,
grounded = 1 and set gate_failure_reason to "unsupported claim".
```

What to point at afterwards: generation and scoring are two files, and the score file records the judge model and rubric version. That separation is what lets you re-score the same outputs with a better rubric without re-running the models — and it is the thing almost every ad hoc evaluation lacks.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two numbers for the same model from two colleagues, both "correct", five points apart.
2. **State the objective** — you will build a six-part pipeline and re-run it to get the identical result.
3. **Recall prior learning** — the rubric from K4; ask what would be needed to apply it a hundred times.
4. **Present the content** — the six parts; versioning; layered scorers; judge validation; regression gates.
5. **Guide** — run the harness on ten items live, then break it deliberately (change temperature) and watch the log tell you why.
6. **Elicit performance** — pairs build the pipeline for their own task with a five-item test set.
7. **Give feedback** — inspect their logs: missing model version, missing seed, no slice labels.
8. **Transfer** — they add a gate to their repository and let it block one change.

## What the framework doesn't mention but trainers need to know

- **The expensive part is the test set, not the code.** Budget for the person who curates two hundred representative inputs and labels the slices. It is the highest-return hour in the project.
- **Judges drift when the vendor updates the model.** Pin the judge version like any other dependency, and re-validate on a schedule.
- **Store the raw output, always.** Paraphrased or truncated logs make failure analysis impossible and quietly destroy the ability to re-score.
- **Make the pipeline cheap enough to run on every change.** An evaluation that costs a day will be run quarterly, and a quarterly evaluation cannot gate anything.

## Watch out

- **Do not build the pipeline before the rubric.** You will automate the wrong measurement, efficiently.
- **Do not hide the scoring inside the generation loop.** Separating them is what makes re-scoring possible.
- **Do not demo a pipeline on a toy test set.** Learners copy the shape and the toy set with it.
- **The stale claim to retire:** "we'll do a proper evaluation once the product is stable." The pipeline is how you know when it is stable.
