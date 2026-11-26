# The decay model

## Why the first version was wrong

Volume 1 was organised by **framework position** — TSC number, proficiency level, K/A anchor. That is the right structure for a compliance map and the wrong structure for a knowledge library, because it treats every fact as equally durable. Tokenisation and "GPT-6.1 Terra launched on 26 October" were sitting in the same container, with the same implied shelf life, which is absurd: one is good for a decade, the other for a quarter.

The fix is not more topics. It is a **decay model**: every entry declares how fast it rots, and the format changes accordingly.

---

## The four tiers

### DURABLE — `DUR`

**Half-life:** years to decades. **What it is:** the mechanism. How tokens work, why attention degrades over long context, what an embedding is, why a model hallucinates, how retrieval differs from fine-tuning, what a diffusion step does.

**Rules:**
- No product names in the title. No version numbers anywhere in the body except as illustrations.
- If a model is mentioned, it is a *class* ("reasoning models", "small fast tiers"), never a SKU.
- Teach it with an analogy and a demo that works on any tool.
- It should still be true if every vendor disappeared tomorrow.

**In class:** this is where depth lives. Analogies, board sketches, five-minute practice. It is also the only tier that is safe to build a two-day course around.

### LIVING — `LIV`

**Half-life:** weeks to a quarter. **What it is:** the moving surface — model families and versions, pricing, context sizes, deprecation dates, product features, what a tool can and cannot do this month.

**Rules:**
- Every entry carries **"As at: [date]"** in the header and an explicit **Expires:** line.
- Every fact must be traceable to a **primary source** — the vendor's own documentation or changelog. Not a blog, not a YouTube summary, not a LinkedIn post.
- The entry does not try to be complete. The complete list lives in the **Living Register** (a CSV you update in thirty minutes a month); the entry teaches how to read that list.
- The teaching goal is not "know the current model". It is "know how to check, and how often to bother".

**In class:** ten minutes maximum. Show the deprecation page. Show how to find the current lineup. Then move on, because the point is the method.

### EVENT — `EVT`

**Half-life:** a fixed date; relevance decays but never vanishes. **What it is:** an incident, a release that changed something, a policy shift, a court ruling, a security scare — Black October, the agentic AI governance framework, a model release that broke a common workflow.

**Rules:**
- Written once, **dated forever**. Never silently updated; corrections are appended with a date.
- It becomes a **case study**, not a news summary. The structure is: what happened → what actually caused it → what the headline got wrong → three teaching angles → discussion questions.
- One event per month is plenty in a classroom. More than that and the course becomes a news feed.
- The value is in the *misreading*. Every event has a popular wrong version, and correcting it is the lesson.

**In class:** ten to fifteen minutes, usually as an opener or a closer. Events are the cheapest way to make an abstract risk concrete.

### TECHNIQUE — `TEC`

**Half-life:** split. **What it is:** a practical craft with knobs — video generation parameters, image prompting, structured output schemas, API settings.

**Rules:**
- Every technique entry is physically divided into **the method** (durable: how to think about the knobs) and **the fields** (living: a dated table of what exists this quarter).
- Never teach the field list as knowledge. Teach the method, then show the field table as an example of applying it.
- Include one "read the schema" demonstration. The transferable skill is opening the request body, not memorising `camera_fixed`.

**In class:** demo-heavy, fifteen to twenty minutes, always ends with the learner doing it rather than watching it.

---

## The test for which tier you are writing

Ask: **what would make this wrong?**

| Answer | Tier |
|---|---|
| A new model release | Living |
| Nothing, or a genuine research result | Durable |
| It happened on a date and cannot unhappen | Event |
| A vendor renaming a field | Technique (method durable, fields living) |

If you cannot answer, you are probably writing a **living** entry disguised as a durable one. That is the most common failure in AI training material, and it is why decks feel stale six weeks after they are built.

---

## The refresh ritual

| Cadence | What | Time |
|---|---|---|
| **Monthly** | Run `python scripts/living.py stale`. Update the [Living Register](../concepts/living/register.csv): current models, versions, prices, deprecations. Move superseded rows to the [archive](../concepts/living/archive.md) with the date. Re-stamp every entry you touched. | 30–45 min |
| **Quarterly** | Re-check TEC field tables against vendor documentation; re-read LIV entries for anything now wrong; archive superseded claims rather than deleting them. | 2 hours |
| **Annually** | Re-read the DUR entries for mechanism drift — e.g. reasoning models made parts of the Chain-of-Thought lesson obsolete, and that had to be re-taught rather than deleted. | half a day |
| **On occurrence** | Write the EVT entry within a week, while the sources are still live and the misreading is still circulating. | 1–2 hours |

The ritual matters more than the volume. A library of 40 entries refreshed monthly beats 200 entries refreshed never.

---

## What this does to a course design

A two-day AI course built entirely on living content is obsolete before the next intake. A course built entirely on durable content feels like a history lecture. The workable ratio:

- **70% durable** — the mechanism, the judgement, the analogies.
- **20% technique** — hands on the knobs, with the field table on screen.
- **10% living and event** — what changed, what it means, why the headline was wrong.

And the living slice is the part you rebuild before **every run**, not every year. That is the whole discipline: the durable 70% is an asset, the living 10% is a chore, and trainers who confuse the two either rewrite everything constantly or teach yesterday.

---

## Composition targets

| Tier | Target | Written | Note |
|---|---|---|---|
| DUR | 45–60 | 17 | The spine. Depth beats breadth. |
| TEC | 15–20 | 1 | One per major modality: video, image, audio, structured output, agents. |
| LIV | 8–12 | 1 | Model families, pricing, deprecations, product surfaces, regional availability. |
| EVT | unbounded | 1 | Grows by itself. Prune to the ones you actually teach. |

Sixty durable entries is a library. Two hundred living entries is a subscription service you cannot maintain alone. Aim for the first.

---

## Naming and IDs

`DUR-xx` · `TEC-xx` · `LIV-xx` · `EVT-xx`

Event entries carry their date in the header line, because the date is part of the fact. Everything else is a stable number that never gets reused.

The old Volume 1 IDs ([Tokens and tokenisation](../concepts/durable/tokens-and-tokenisation.md), [Chain-of-Thought (and when it makes things worse)](../concepts/durable/chain-of-thought.md), [Anatomy of a prompt](../concepts/durable/anatomy-of-a-prompt.md) and the rest) are all durable-tier entries and keep their numbers. The index now shows the tier in a column rather than implying it.

---

## Known gaps in v2

- **Durable depth is uneven.** Two entries on how models work, none yet on attention, diffusion, or the difference between pre-training and post-training.
- **Technique coverage is one modality.** Video has a table; image, audio and structured output do not.
- **Living coverage is one family.** There is a ChatGPT/Claude/Gemini lineage entry and a register, but nothing yet on pricing economics or on what is available in Singapore specifically.
- **Events are retrospective.** There is no forward watch — no mechanism for noticing the next Black October while it is happening, only for writing it up afterwards.
- **Archive discipline — in place.** Superseded register rows move to [the archive](../concepts/living/archive.md) with the date they stopped being true.
