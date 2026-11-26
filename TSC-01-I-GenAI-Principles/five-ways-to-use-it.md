---
id: 01.02.I.A2
tsc: 1
level: Intermediate
code: A2
title: "Five ways to use it: summarise, infer, reason, transform, augment"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Five ways to use it: summarise, infer, reason, transform, augment

> **TSC #1 Generative AI Principles and Applications · Intermediate · Ability A2**


> **Framework text (verbatim):** "Demonstrate the use of generation AI in diverse applications (e.g., summarisation, inference, reasoning, transformation of content, augmentation of content)."
>
> **TSC #1** Generative AI Principles and Applications · **Intermediate** · Ability · Bullet 7 of 10

**One-line version:** The five words in the framework are not synonyms for "use AI" — each moves the content a different distance from its source, and the distance is exactly what you pay for in checking.

## What it is

Five application families, each an operation on existing content: compressing it, drawing a conclusion from it, chaining conclusions across it, changing its form, or adding to it. Demonstrating them means showing one real task per family and being able to say what each one demands and where each one breaks.

## Deep expansion

### The concept

Learners treat these as five flavours of the same request. They are not. Each has its own distance from the source, its own characteristic failure and its own check:

| Family | What it does | Distance from source | The check |
|---|---|---|---|
| Summarise | Compresses, keeping the substance | Nearest — same claims, fewer words | Trace each point to a page |
| Transform | Same content, new form or register | Same content, new shape | Diff the facts, not the prose |
| Infer | States what the source implies but does not say | A step beyond the text | Quote the evidence per conclusion |
| Reason | Chains steps to a judgement | Several steps beyond | Test the first premise |
| Augment | Adds content that was not there | Furthest — new claims | Mark what the model supplied |

Order the families by distance and the bullet organises itself. A summariser that drifts is a bug; an augmenter that adds is doing its job, which is why it carries the largest verification bill.

### The sub-concepts

**Summarisation.** Compression under a budget: audience, length, focus. Faithfulness is the metric — every sentence traceable to the source, nothing outside it, and no smoothing over a contradiction the document actually contains. The classic failure is intrinsic: the text says revenue grew 12% on software while hardware fell 4%, and the summary says hardware grew. Directional summaries beat generic ones: "focusing on indemnity, termination notice and governing law" produces something usable; "summarise this contract" produces something safe and vague.

**Inference.** Drawing a conclusion the source supports but does not state: which policy applies, whether a clause is a hard conflict, what category this complaint belongs to. The word is ambiguous in the framework — it means reasoning over given material, not the compute sense an IT audience will hear, so say which on the first slide. The failure is over-reading: bridging two facts with an invented third. Fix: require the quoted evidence behind each conclusion, and place the conclusion after the reasoning in the output.

**Reasoning.** Multi-step chains — eligibility across three rules, a scheduling clash across four rooms, root cause across five incidents. Reasoning modes make this family visible: the working appears, which is useful precisely because it can be checked. But visible working is a draft of an argument, not proof of one. A fluent chain built on a wrong first premise reads exactly like a correct one. Check the premise, re-derive one step by hand, and hand arithmetic to a calculator.

**Transformation.** The same content in a new form: report to slides, email thread to minutes, policy to checklist, English to Malay. Nothing should be added and nothing lost, which sounds safe and is not. Transformation drifts — the shape improves while a qualifier disappears, a date shifts, a condition is dropped because it did not fit the slide. Check by diffing facts against a field list, not by reading the prose for quality.

**Augmentation.** Two meanings to separate. Content augmentation adds to what exists: sparse notes into a structured brief, a three-line outline into a section. Context augmentation adds source material to the model's working memory before it answers — the retrieval sense. The first adds claims and needs marking; the second adds evidence and needs a citation check. Same word, opposite risk.

**Chains are the real workload.** Most tasks are two or three families in sequence: summarise forty interview transcripts, infer the five recurring complaints, transform them into a briefing. Errors compound at the handoff, and each step needs its own check — the citation check at step one does not protect the inference at step two.

### How it connects to the rest of the framework

`TSC1-Intermediate-A01` chooses which step of a job deserves one of these operations; this bullet is the menu it chooses from. `TSC1-Intermediate-K03` explains why format and coverage respond to prompting while knowledge does not — which is why transformation is more steerable than reasoning. `TSC1-Intermediate-A03` audits the failures named here; `TSC1-Intermediate-A04` measures them. `TSC3` is the prompt craft per family, and `TSC6-Basic-K01` covers context augmentation in the retrieval sense.

### What is current as of November 2026

Summarisation has become a product rather than a prompt. NotebookLM answers only from uploaded sources, refuses when the answer is absent, and cites to the paragraph; long-context models hold whole document sets rather than retrieved snippets.

Reasoning is now a selectable mode on most models, so that family has a visible cost: more deliberation, latency and tokens, and a working trace you can inspect. Transformation has moved into side-by-side editing surfaces, where a learner highlights one paragraph instead of regenerating a document. Augmentation in the retrieval sense is the default architecture for private material; the trade is chunk-level precision against full-document recall.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Summarising and analysing are the same thing."* One compresses what is there; the other concludes something not written down. They fail and are checked differently.
- *"It cited a source, so the conclusion is proven."* A citation is an address to inspect. It proves a page said something, not that the page is right or fairly read.
- *"Reasoning mode means the reasoning is correct."* It means the working is available. Correctness is what you check it for.
- *"Transformation is safe because nothing new is added."* Content drifts while the format improves; the vanished qualifier is invisible in a prettier slide.
- *"Augmentation means the model read my document."* Usually it means the model added its own knowledge to it. Only one of those is grounded.

## How a student should understand it

**Mental model:** five distances from the page. A photocopier with a shrinking setting, a translator with a house style, a detective, an analyst building a case, and a ghostwriter. The further from the page, the more of the output is yours — and the more of it you have to answer for.

**Things they can do after this bullet:**
1. Name which family a given task belongs to, and therefore which check applies.
2. Write one directional summary, one evidence-backed inference and one transformation of the same source.
3. Mark, in any augmented draft, which sentences came from the source and which the model supplied.

**Misconceptions to kill:** that the five are interchangeable, that a citation proves a conclusion, and that a prettier format is a safer one.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clerk and the file.** One clerk handles the same file five ways: writes the minutes (summarise), answers "which policy covers this claim" (infer), works out whether two meetings can share a room (reason), turns the file into a letter to the resident (transform), and fleshes out the officer's rough notes into a full report (augment). Same file, five different levels of accountability — and the last one, the clerk's own words, is the one the clerk signs.

**The MRT map versus the route plan.** A summary is the map — everything, scaled down, no new stations. An inference is "you are probably going to Bishan". A reasoning chain is the route with interchanges. A transformation is the same journey in another language. An augmentation is a suggested detour: useful, and entirely the model's idea. Where it breaks: the map is checked against the territory, so the class should say who holds the territory.

### Worked example with a real tool

One source, three families, in NotebookLM with a 30-page HR policy uploaded as the only source:

```
1. Summarise the sections dealing with part-time staff in no more than
   6 bullets. Quote the clause number for each bullet.
```

```
2. A part-time employee works 22 hours a week and has been with us for
   9 months. Using only the policy, state which benefits apply and quote
   the clause you relied on for each.
```

```
3. Turn the answer above into a one-page notice for staff, plain English,
   no clause numbers, no benefit that was not in your previous answer.
```

What to point at: the summary quotes clause numbers, so the check is a click. The inference must carry a quote per conclusion — remove the requirement and watch it bridge gaps it was not entitled to bridge. The transformation must not add a benefit absent from step two; ask the room to find the drift. Three families, one source, three checks, ten minutes.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a summary, an inference and a transformation of the same paragraph; ask which one could get someone in trouble.
2. **State the objective** — by the end you can name the family and the check for any task in your week.
3. **Recall prior learning** — fluency is uniform across right and wrong; the model has no truth signal.
4. **Present the content** — the distance ladder, one failure and one check per family.
5. **Guide** — run the three-prompt chain above together, live.
6. **Elicit performance** — pairs take one document and produce a summarise, an infer and a transform, each with its check stated.
7. **Give feedback** — debrief where the inference over-read and where the transformation drifted; those two are always present.
8. **Transfer** — each learner labels their five most common tasks with a family and a check, and names the one they have treated too lightly.

## What the framework doesn't mention but trainers need to know

- **The five are a menu, not a maturity ladder.** Nobody progresses from summarising to augmenting. The task decides.
- **"Inference" needs disambiguating on the first slide.** Half an IT room will hear "model inference" and the bullet stops making sense to them.
- **Most workplace value sits in summarisation and transformation**, not inference and reasoning. Those two are the impressive demos and the smaller share of the hours.
- **One prompt pattern does not transfer across families.** A good summarisation prompt is a bad reasoning prompt; the constraints that help one hurt the other.
- **Chains need a check at every joint.** The common failure is a verified summary feeding an unverified inference into a confident notice.

## Watch out

- **Do not demo reasoning on arithmetic.** Counting and column sums fail for mechanical reasons; use a calculator and say so, or the demo teaches the wrong lesson about the family.
- **Do not summarise a document with a contradiction without pointing at how it got smoothed.** That is the most instructive failure in the room.
- **Do not accept an inference without its evidence quote.** Once the room sees that quotes can be demanded, they stop treating conclusions as verdicts.
- **Do not present augmentation as "the AI wrote it for me".** Present it as a draft with two colours in it: sourced and supplied.
- **The stale claim to retire:** "AI cannot reason" and its twin "AI reasons like a person". It produces a checkable chain of steps. Checkable is the operative word, and it is enough to be useful and not enough to be trusted.
