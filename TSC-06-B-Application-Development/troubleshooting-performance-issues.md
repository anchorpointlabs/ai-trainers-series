---
id: 06.01.B.A4
tsc: 6
level: Basic
code: A4
title: "Performance troubleshooting: slow, wrong and expensive are three different bugs"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Performance troubleshooting: slow, wrong and expensive are three different bugs

> **TSC #6 Generative AI Application Development and Deployment · Basic · Ability A4**


> **Framework text (verbatim):** "Troubleshoot performance issues (e.g., follow standard procedures)."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Ability · Bullet 10 of 11

**One-line version:** You cannot fix a performance problem you have not measured, and the average is the number most likely to mislead you.

## What it is

Performance troubleshooting is the standard procedure applied to a defined metric: baseline, reproduce, measure before changing, change one variable, measure again, record the result. For AI applications the metric has four faces — latency, cost, quality and reliability — and they trade against each other, which is what makes this different from ordinary tuning.

## Deep expansion

### The concept

"Performance" is not one thing. It is at least four, and they move in opposite directions. **Latency**: how long the user waits, and separately how long until the first word appears. **Cost**: tokens in, tokens out, cached tokens, calls per request. **Quality**: whether the answer is still right after you made it faster. **Reliability**: error and timeout rates, and how gracefully it degrades.

Every fix for one usually damages another. A smaller model is faster and cheaper, possibly worse. More retrieved passages give better recall, slower and dearer. More retries hide errors, add load and add cost. The procedure keeps those trades visible instead of accidental.

The other discipline is statistical honesty. A single slow request is an anecdote; the average hides the tail. What users experience is the tail, and p95 is the number that decides whether the app feels broken.

### The sub-concepts

**Baseline before fix.** Write down the current number with its conditions: which model, which prompt, how many retrieved passages, what time of day. Without a baseline, "it feels faster now" is the only available verdict.

**Time to first token versus total.** Streaming makes an app feel responsive without making it faster. Both numbers matter and they are quoted separately.

**Four usual suspects, in order.** The prompt or context grew; retrieval widened; the model or version changed; retries are storming on 429. Each has one measurement that confirms it.

**Cost per request is arithmetic.** Input tokens, cached input tokens, output tokens, times the number of calls. Output is usually the expensive part, and reasoning modes bill for thinking you never see.

**Levers, cheapest first.** Prompt and response caching; routing easy requests to a small model; batching work that does not need to be interactive; then reducing context; then changing model.

### How it connects to the rest of the framework

`TSC6-Basic-K3` explains the errors that masquerade as performance problems — a timeout is often a 429 in disguise; `TSC6-Basic-K5` is the general procedure this specialises; `TSC6-Basic-A5` is where the offending settings live. `TSC6-Advanced-K1` (compute efficiency) and `TSC5` (evaluation) are what prove the speed-up was not a quality loss.

### What is current as of November 2026

- **Reasoning modes made latency spiky.** Current flagships think before answering, so a request that took a second in chat mode can take several times longer with no code change. Spikiness, not average slowness, is the new normal.
- **Prompt caching changed the cost model.** For apps with a long, stable system prompt, caching removed most of the repeat cost — provided the prompt never changes.
- **Latency varies by region**, and a deployment serving Singapore users from a distant region pays a per-request penalty no prompt engineering fixes.

### Common misconceptions

- *"The model is slow."* Often the model is fine and retrieval is doing a full-table scan, or three calls that could run in parallel are serialised.
- *"Add retries."* Retries on a rate limit make it worse. Backoff and jitter are the fix; persistence is not.
- *"Switch to a smaller model first."* Measure first. If the time is in retrieval, a smaller model buys nothing and costs quality.

## How a student should understand it

**Mental model:** the MRT at 8am. The train is not slow; the platform is crowded and the doors take longer to close. You fix the crowding, not the train.

**Three things they can do after this bullet:**
1. Baseline p50 and p95 latency, cost per request and error rate before touching anything.
2. Work the four suspects in order and name the measurement that would confirm each.
3. State the trade — speed, cost, quality or reliability — every time they propose a fix.

**Misconceptions to kill:** that speed is free, that the average represents the experience, and that retrying is a fix.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker queue that forms at the wrong end.** The wok is fast; the queue is at the ordering counter because one person takes orders and payment together. Adding a second wok changes nothing. Where it breaks: unlike a stall, you cannot see your own queue without instrumentation, which is why measurement is not optional.

**The taxi meter.** The fare is distance plus the time spent stationary in traffic. Token cost behaves the same way: you pay for thinking time as well as output.

### Worked example with a real tool

Take a real symptom — "the FAQ bot got slow after we added the new documents" — and paste the measurements in:

```
Our RAG FAQ app went from ~2s to ~9s per answer after we added 400 new
documents. Settings: top-k = 20, no reranker, same model as before.
Over 50 requests: retrieval 6.1s (p50), 11.4s (p95); model call 1.9s (p50),
2.6s (p95); error rate 2%, all 429.

Give me three hypotheses ranked by likelihood, and for each the single
measurement that would confirm or eliminate it. Then tell me which fix gives
the largest improvement for the least risk to answer quality, and what to
measure afterwards to prove it worked.
```

What to point at afterwards: the arithmetic already localises it — retrieval is six of the nine seconds, so the model is innocent and the likely fix is indexing and narrower retrieval, not a smaller model. The learner collected the numbers; the assistant only organised them. Then ask what quality risk narrower top-k introduces, and how they would check it — which is where evaluation enters and the numbers stop being enough.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two recordings of the same app, one streaming. Ask which is faster. Neither; one only *feels* faster.
2. **State the objective** — by the end you can baseline four metrics, work the four suspects, and state the trade in every fix.
3. **Recall prior learning** — triage from K3, procedure from K5, parameters from A1.
4. **Present the content** — the four faces, p50 versus p95, the suspects in order, the levers cheapest first.
5. **Guide** — read a real trace together and identify which step consumed the time.
6. **Elicit performance** — groups get a measurement table and must produce three ranked hypotheses, one confirming measurement each, and one fix with its trade.
7. **Give feedback** — the group that proposed "smaller model" defends it against the group that found the retrieval bottleneck.
8. **Transfer** — each learner writes the four metrics they would monitor and where the numbers come from.

## What the framework doesn't mention but trainers need to know

- **Instrument first, always.** Ten lines of timing around retrieval and the model call answer more than a week of prompt tweaking.
- **Streaming is a perception fix.** Say it plainly, or learners report an improvement an auditor cannot find.
- **Cost surprises come from output length and retries**, not input length. Cap output, then check retry counts.

## Watch out

- **Do not quote latency figures from memory.** Provider latency varies by region, model and hour; measure on the day.
- **Do not teach "downgrade the model" as a first move.** It is the most likely to damage quality and the least likely to be the bottleneck.
- **The stale claim to retire:** "a bigger model is always slower." Reasoning modes and routing have broken the simple relationship between size, speed and price.
