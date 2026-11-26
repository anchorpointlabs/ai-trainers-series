---
id: 03.02.I.K4
tsc: 3
level: Intermediate
code: K4
title: Context window limits and how to work within them
as_at: 2026-11-26
review_by: 2027-02-25
---

# Context window limits and how to work within them

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K4**

> **Framework text (verbatim):** "Context window limitations, long context implications and strategies to work within them."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Knowledge · Bullet 4 of 13

**One-line version:** The context window is working memory, not storage — and a document that fits is not the same as a document that gets read.

## What it is

The context window is the maximum number of tokens a model can hold in one request — everything you send plus everything it generates, counted together. Its limit is a hard ceiling, but its real constraint is softer and more important: attention is not spread evenly across it, so quality degrades before the ceiling is reached. Working within the window means choosing what earns a place in it, and where.

## Deep expansion

### The concept

Two numbers matter and learners usually know only the first. The **advertised** window is the marketing figure — the largest input the model will accept. The **effective** window is the amount of context it can still reason over accurately. Between them sits a stretch where the model accepts your document, answers confidently, and quietly ignores the clause on page 42.

The mechanism is attention. Every token computes a weight against the tokens before it, and those weights are normalised across the sequence. Add thousands of tokens of boilerplate and each instruction gets a smaller share. Empirically, recall across a long prompt is U-shaped: strongest at the very start, strong at the very end, weakest through the middle. That single fact explains most of the advice in this bullet — put the rules where attention is, put the instruction last, and stop stuffing.

### The sub-concepts

**Input plus output share one budget.** A long document leaves less room for the answer, and truncated answers look like model failure. If the output must be a 40-row table, the input has to leave room for it.

**Cost and latency scale with length.** Every query pays for the whole payload, every time. Pasting a 60-page report into every turn is not just slower; it is a recurring bill for material the model mostly ignores.

**Attention dilution is the practical failure.** More context is not more information. Ten relevant paragraphs plus fifty irrelevant ones is worse than the ten alone, because the irrelevant ones create competing, plausible-looking evidence — the classic "which year's policy applies" blend.

**The strategies, in order of value.**
1. **Put the instruction last** (and repeat the core rule after a long document block). This is free and fixes a surprising share of "it ignored me" complaints.
2. **Compress the input** — summarise or extract the relevant sections first, then ask the question of the summary. Two short calls beat one enormous one.
3. **Retrieve rather than paste.** For a large or changing corpus, fetch only the few passages that matter. This is the industrial answer, and Intermediate learners should be able to describe it in one sentence: search first, then ask.
4. **Split the task.** A chain of small prompts each with a small, clean context outperforms one prompt carrying everything.
5. **Start fresh with a brief.** When a thread has accumulated dead ends and corrected instructions, write a six-line summary of the decisions so far and open a new chat.
6. **Use files and tools instead of prose.** For arithmetic, counting and lookups, a tool call is smaller and exact where a pasted table is large and unreliable.

**When long context genuinely wins.** If the corpus is small, static and needs holistic reading — one 60-page statute, a set of ten related contracts — loading the whole thing beats chunked retrieval: no boundary loss, no missed cross-reference, and prefix caching makes the repeat cost tolerable. The judgement is about corpus size and change rate, not about which approach is fashionable.

### How it connects to the rest of the framework

`TSC3-Intermediate-K2` lists the window among the structural limits of foundation models; this bullet is the working discipline that follows. `TSC3-Intermediate-K3` explains why order matters at all, `TSC3-Intermediate-K1` turns that into an assembly order, and `TSC3-Intermediate-A2` carries the same advice into general practice. For why retrieval beats pasting at scale, the retrieval material in the core knowledge set is the reference.

### What is current as of November 2026

Advertised windows are now very large: current frontier models all accept inputs that would have been unthinkable three years ago, and all price long inputs differently from short ones. Three things have not changed:

- **Effective is below advertised.** Every frontier model shows degraded recall in the middle of a very long input. A bigger window moves the cliff; it does not remove it.
- **Caching changed the economics, not the attention.** Reusing a static prefix is much cheaper and faster, which makes "load the whole small corpus once" a sound pattern — and makes "paste a different 200 pages every turn" as wasteful as ever.
- **Retrieval is still the answer for large corpora.** Company knowledge bases are measured in millions of documents; no window holds them, and no price list makes sending them per query sane.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The window is a million tokens, so I can paste everything."* You can paste it. You cannot rely on the middle of it, and you will pay for all of it on every call.
- *"It forgot because the model is weak."* It forgot because the instruction was 40 pages above the question, or because thirty distractors outvoted the one right paragraph.
- *"Always start a new chat."* Starting fresh loses context you may need. The discipline is to carry forward a written brief, not to abandon the work.
- *"Long context makes retrieval obsolete."* Long context makes retrieval unnecessary for small, static, whole-document reading. It does nothing for a corpus that changes daily.

## How a student should understand it

**Mental model:** the boss reading a 50-page proposal. Page one gets full attention, page fifty gets full attention, pages 22 to 35 get a skim. If your instruction is on page 27, it was never read — and the boss will still give you an answer.

**Things they can do after this bullet:**
1. Explain the difference between the advertised and effective window in one sentence.
2. Take an over-long prompt and cut it to the three things that matter, then show the output improved or held.
3. Diagnose "it ignored my instruction" as a position problem before blaming the model.

**Misconceptions to kill:** that fitting means reading; that more context is more information; that a fresh chat is always the fix.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The goldfish with a PhD.** Brilliant, widely read, and its memory of this conversation lasts exactly as long as the conversation does. Where it breaks: the goldfish forgets everything; the model remembers the first and last thing you said rather well — which is why the placement advice works at all.

**The MRT luggage rack.** There is a rack. It will physically hold your suitcase, your colleague's box and someone's durian. Whether anything is still findable when you reach your stop is a different question from whether it fitted.

### Worked example with a real tool

Paste a genuinely long document — ten pages of a policy PDF — with the instruction at the **top**:

```text
Using the policy below, tell me the notice period for resignation during probation.
[10 pages of pasted policy]
```

Run it. Then rerun with the same document and the instruction **repeated at the bottom**, plus a narrower ask:

```text
[paste document]

From the policy above only, state the notice period for resignation during
probation, quoting the sentence that says it. If the policy does not state it,
write NOT IN POLICY.
```

Then a third version: ask for a 200-word summary of the sections on resignation first, then ask the question of that summary. Point at the difference between version one and three: less context, more accuracy, lower cost. That is the whole bullet in ninety seconds.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a 10-page paste and the model's answer that ignores line one.
2. **State the objective** — by the end you can cut a long prompt to its essentials without losing the answer.
3. **Recall prior learning** — what do they remember about how the model attends to a prompt?
4. **Present the content** — window, effective window, U-shaped attention, then the six strategies in priority order.
5. **Guide** — run the three-version demo together and score each on accuracy and cost.
6. **Elicit performance** — pairs take a real long document from their work and produce a compressed version.
7. **Give feedback** — compare outputs; where the compressed version loses a fact, identify what was cut and whether it mattered.
8. **Transfer** — each learner writes their personal rule for when to paste, when to summarise, and when to open a new chat.

## What the framework doesn't mention but trainers need to know

- **Output tokens are part of the budget and the bill.** Learners rarely realise a long answer costs money and can truncate mid-table.
- **Retrieval is not an advanced topic.** At Intermediate level, "search the folder first, then paste the three relevant pages" is a complete and correct description of the pattern.
- **Chunk boundaries lose meaning in ways that look like model error.** A clause retrieved without its exception is worse than no clause at all — and this is a data problem, not a prompting problem.
- **Security depends on the window.** Everything pasted in is trusted by the model unless you tell it otherwise, which is why delimiters and "treat as data" instructions belong in this lesson.
- **Cost literacy is part of the skill.** A team that pastes a whole department's documents into every prompt has built a recurring expense and an information-governance problem at the same time.

## Watch out

- **Do not equate context with memory.** Nothing is stored. The window is a per-request working set that disappears when the request ends.
- **Do not demo "paste everything and ask" as a trick.** It works often enough to mislead, and fails exactly where accuracy matters.
- **Do not teach retrieval as a vendor product.** Teach the shape: index, search, paste the few, cite them.
- **The stale claim to retire:** "the newest model has a huge window, so context management is solved." The window grew; the attention curve did not.
