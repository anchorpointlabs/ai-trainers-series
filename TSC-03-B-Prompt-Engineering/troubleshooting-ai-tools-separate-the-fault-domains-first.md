---
id: 03.01.B.K5
tsc: 3
level: Basic
code: K5
title: Troubleshooting AI tools: separate the fault domains first
as_at: 2026-11-26
review_by: 2027-02-25
---

# Troubleshooting AI tools: separate the fault domains first

> **TSC #3 Prompt Engineering · Basic · Knowledge K5**


> **Framework text (verbatim):** "Techniques in troubleshooting AI tools."
>
> **TSC #3** Prompt Engineering · **Basic** · Knowledge · Bullet 5 of 15

**One-line version:** Most AI failures are not model failures — and the technique that saves the most time is deciding which of six fault domains you are actually in before changing anything.

## What it is

Troubleshooting an AI tool means working out why the output was not what you needed, in a way that produces evidence rather than guesses. The techniques are a small set: separate the fault domains, make the failure repeatable, cut the prompt down until it works, and change one variable per run. They cost ten minutes and save hours of speculative rewriting.

## Deep expansion

### The concept

Learners arrive with one tactic: reword the prompt. It fails often enough to be dangerous, because a reworded prompt that happens to work teaches nothing about what was wrong, and the fault returns next week wearing different clothes.

The practitioner's first move is classification. Six domains produce almost every failure:

1. **The prompt** — ambiguous, conflicting, or missing a fact.
2. **The input** — the file, row, encoding or format you supplied.
3. **The model** — the version, its capability ceiling on this task, or a routing change behind the product.
4. **The account or quota** — limits, region, plan tier, feature flags.
5. **The interface** — file-size caps, unsupported formats, attachment handling.
6. **The environment** — network, browser, VPN, corporate proxy.

Each domain has a different cheap test, and the tests do not overlap. That is the point of naming them: it stops the room from treating every symptom as a wording problem.

### The sub-concepts

**Make it repeatable before you explain it.** Run the same prompt again, unchanged, in a fresh session. If the failure vanishes, you are dealing with variance, not a bug — and variance is a real finding worth recording, because a task that fails one time in five cannot be handed to a colleague without a checking step. If it reproduces, you now have something you can bisect.

**Bisect the prompt.** Strip it to the smallest version that still shows the failure, then add clauses back one at a time. Long prompts fail for structural reasons — a buried instruction, a contradiction between two rules — and bisection finds the clause responsible instead of the whole prompt being rewritten on suspicion.

**Change one variable per run.** Model, prompt, input, session. Two changes at once and you have learned nothing, even if it works.

**Use the tripod test.** Same prompt, three places: a new session, a different model, and (if available) the API rather than the chat interface. If it fails only in the interface, you are in domain 5. If it fails everywhere, you are in domain 1 or 3, and the difference between those two is whether a stronger model fixes it.

**Read the actual error.** "Something went wrong" is an interface message; the detail is usually in the browser console, the API response, or the provider's status page. A 429, a context-length error and a content-policy refusal look identical to a learner and require three different responses.

**Log the run, not the feeling.** Prompt version, model, input, time, what happened. This is the artefact that makes the second occurrence cheap and makes an escalation credible.

### How it connects to the rest of the framework

This is the practitioner-level view of `TSC2-Basic-K1` (Prompt Design); see that entry for the user-level basics of checking the prompt, the connection and the service. `TSC3-Basic-A5` is the symptom vocabulary you classify with, `TSC3-Basic-A6` is the ordered procedure and the escalation threshold, `TSC3-Basic-K7` is what to put in place so the failure cannot recur, and `TSC3-Basic-K3` explains which technique changes the wording problem once you have confirmed it is one.

### What is current as of November 2026

Three things have moved. Reasoning-capable models now fail differently: a truncated or unhelpful answer is often a thinking-budget problem rather than a prompt problem, and the fix is a setting, not a rewrite. Long context windows have moved many failures from "it forgot" to "it attended to the wrong part", which makes bisection more useful than adding more material. And platform churn is now the dominant source of "it worked yesterday" — model versions are retired and rerouted behind stable product names, so the practitioner habit that matters most is recording which model version produced an acceptable result, not merely which product.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It gave a bad answer, so the prompt needs rewriting."* Four of the six domains are not the prompt, and two of them produce answers that look like prompt problems.
- *"If it works now, it is fixed."* A single success after a change is not evidence, especially with a sampling model. Run it a few times.
- *"The error message tells you what happened."* It tells you what the interface decided to show you. The detail is elsewhere.
- *"Deleting the chat deletes the problem."* It deletes the evidence. Copy the prompt and the output first.

## How a student should understand it

**Mental model:** the electrician's first question — is it the appliance, the socket, or the fuse box? Nobody rewires a house because a kettle stopped boiling.

**Things they can do after this bullet:**
1. Name the six fault domains and one cheap test for each.
2. Bisect a long prompt down to the clause that causes the failure.
3. Produce a run log that a colleague or a support desk can act on.

**Misconceptions to kill:** that every failure is a wording problem; that one success proves a fix; that the visible error message is the diagnosis.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The electrician.** Light not working: check the bulb, then the socket, then the breaker, then whether the block has power. Four tests, thirty seconds, in a fixed order — and no electrician starts by rewiring. Where it breaks: an electrician can measure voltage; you cannot see inside the model, so your tests are behavioural and therefore probabilistic. That is why you run each one more than once.

**The hawker's "is it the stove or the gas".** The wok is not hot. Before blaming the wok, check the gas valve, then the ignition, then whether the whole row lost supply. Where it breaks: gas either flows or it does not, while a model can produce a plausible answer with a subtle fault in it — there is no equivalent of "no flame".

### Worked example with a real tool

Symptom a learner brings: "The summary it gave me this morning was cut off halfway."

```text
Run 1 — same prompt, same session: still cut off.
Run 2 — new session, same prompt: still cut off.
Run 3 — same prompt, shorter input (first 20 rows instead of 400): complete.
```

That is enough to place the fault: not the wording, not the account, but input volume against an output limit. Now bisect the instruction instead of guessing:

```text
Take this 400-row file and produce a summary table with one row per complaint
type, count, and one example line. If the table exceeds 40 rows, group the
long tail into "Other".
```

What to point at afterwards: the third run proved the prompt was fine and the workload was the problem; the added clause is a *containment* measure, not a fix. Then show the log entry — prompt version, model, three runs, what changed — because that entry is what turns a complaint into a diagnosis.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — put a truncated answer on screen and ask the room to write down their first fix. Most will say "reword it".
2. **State the objective** — by the end you will place a failure in one of six domains, and you will have bisected one real prompt.
3. **Recall prior learning** — ask how they handled a printer that would not print: paper, then cable, then driver, then the queue. They already know ordered tests.
4. **Present the content** — teach the six domains, then repeatability, bisection and the tripod test.
5. **Guide** — take one live failure from the room and classify it together, out loud, with the cheap test for each candidate domain.
6. **Elicit performance** — pairs bring a prompt that misbehaved and bisect it until they can name the clause or clear the prompt.
7. **Give feedback** — compare logs. The winning pair is the one whose log lets another pair reproduce the failure without asking a question.
8. **Transfer** — each learner writes the four-line log template into their own notes and uses it for a week.

## What the framework doesn't mention but trainers need to know

- **Variance is a finding, not a nuisance.** A task that works four times out of five is unsafe to automate without a check, and the practitioner needs language for that which is not "the AI is moody".
- **Model retirement is the most common "it broke" in production.** Anything that depends on a specific behaviour needs the version recorded and a re-test scheduled.
- **Interface and API behave differently.** File handling, context limits and safety filters are not identical across surfaces. A prompt validated in chat is not validated in the API.
- **The log is the deliverable.** Teach the log as an output of troubleshooting, not an afterthought. It is also the difference between a helpful escalation and a complaint.

## Watch out

- **Do not accept "it works now" as a close.** Ask for three runs.
- **Do not troubleshoot by rewriting only.** The room will follow whatever you model; if you rewrite first, they will rewrite forever.
- **Do not spend the session on platform outages.** Provider status is a link, not a lesson.
- **The stale claim to retire:** "AI is non-deterministic so you cannot debug it." You cannot reproduce it exactly; you can absolutely characterise it.
