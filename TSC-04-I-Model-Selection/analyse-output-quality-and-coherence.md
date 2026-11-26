---
id: 04.02.I.A4
tsc: 4
level: Intermediate
code: A4
title: Analyse output quality and coherence
---

# Analyse output quality and coherence

> **TSC #4 Generative AI Model Selection · Intermediate · Ability A4**

> **Framework text (verbatim):** "Analyse model-generated content for quality and coherence."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Ability · Bullet 9 of 11

**One-line version:** Fluent, confident and wrong is the default failure mode — so read every output twice, once for whether it is true and once for whether it holds together.

## What it is

Two lenses, applied separately. **Quality** asks: is this correct, relevant and complete for the request? **Coherence** asks: does it hold together — no self-contradiction, no drift, no broken reference between sentences or turns? A fluent answer can fail both. A clumsy answer can pass both. The skill is naming which lens failed, because that determines the fix.

## Deep expansion

### The concept

Fluency is the cheapest thing a language model produces. It is also the property human readers notice first, which makes it an unreliable proxy for the two properties that matter. This is why experienced reviewers read for the *claim*, not the sentence.

The practical method is a short checklist applied in order:

1. **Correctness** — is each factual claim true, and is it supported by the source material you supplied?
2. **Relevance** — does it address the actual question, including all its parts?
3. **Coherence** — does any sentence contradict another? Does a reference point to something that exists?
4. **Shape** — is it the length and structure requested?

Four checks, ninety seconds, and the failure distribution in the room changes immediately.

### The sub-concepts

**Hallucination has two flavours.** *Contradiction* is when the answer conflicts with the source you provided — the model has misread or overridden it. *Fabrication* is when the answer asserts something the source never contained. In strict enterprise use, both are failures even when the fabricated fact happens to be true elsewhere, because the system promised to answer from the document.

**The faithfulness ratio is the honest metric.** Break the answer into atomic claims, mark each as supported or unsupported by the source, divide. It sounds laborious; done informally it takes a minute, and it converts "seems fine" into a number you can defend.

**Coherence failures are structural, not grammatical.** Internal contradiction (starts at 3 p.m., arrive by 4 p.m.). Referential breakage ("this clause", when no clause was named). Drift (the third paragraph answers a different question). None of these are spelling errors, and none are caught by reading for style.

**Completeness is the invisible failure.** A three-part question answered in two parts reads perfectly. Ask a colleague to count the parts before judging the answer.

**Lexical similarity is a trap.** Two sentences can share almost every word and mean opposites — "you are eligible" versus "you are not eligible". Overlap scores and embedding similarity both rate those as near-identical. Never use word overlap as evidence of correctness.

**Diversity and novelty matter for creative work, not for extraction.** If you are generating marketing angles, ten variations of one idea is a failure. If you are extracting a total, variety is a defect.

### How it connects to the rest of the framework

`TSC4-Intermediate-K2` is where the prompt that produced this output came from — most quality failures are specification failures. `TSC4-Intermediate-A5` shows how settings move these properties. `TSC4-Advanced-A2` scales the check from one output to a dataset. `TSC4-Advanced-A3` is the same analysis over time. `TSC4-Advanced-K2` explains why fabrication happens at all.

### What is current as of November 2026

For the 2026 frontier — OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon — three things changed the analysis:

- **Grounding improved where retrieval is used.** Answers that cite a source are more often faithful to it, which shifts the review burden from "is this invented" to "did it cite the right passage".
- **Reasoning modes reduced arithmetic and multi-step errors** while leaving tone and framing errors untouched. The failure profile moved rather than shrank.
- **Verbosity stayed a defect.** Longer, better-formatted answers still read as more authoritative, and reviewers still over-reward structure. Style-controlled evaluation exists precisely because of this.

### Common misconceptions

- *"It reads well, so it is right."* Fluency and correctness are independent. This is the single most expensive misconception in the room.
- *"The facts are right, so the answer is good."* A correct answer that misses half the question, or contradicts itself, is still unusable.
- *"If it cites a source, it is grounded."* Check that the cited passage actually says what the sentence claims. Citation and support are different things.
- *"Similarity to a reference answer proves quality."* Word overlap fails on negation, numbers and paraphrase.

## How a student should understand it

**Mental model:** marking a student's essay for content and for argument, separately. Good grammar earns nothing if the argument contradicts itself.

**Things they can do after this bullet:**
1. Apply the four checks to an output and name which one failed.
2. Distinguish contradiction from fabrication in a grounded answer.
3. Reject a word-overlap score as evidence of correctness, with the reason.

**Misconceptions to kill:** that fluency implies accuracy, that a citation implies support, and that a high similarity score implies a correct answer.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The confident insurance agent.** A pitch delivered smoothly with the wrong coverage details is more dangerous than a hesitant one with the right details. Salesmanship is fluency; the policy is the content.

**The MRT announcement.** "Please mind the gap" is perfectly coherent. If it said "please mind the gap, and please do not mind the gap", you would notice the contradiction within one second — that is what you are training the room to do with model output.

### Worked example with a real tool

Start with the deliberately broken one:

```text
Grade this output for quality and coherence:
"The event is on Friday. It starts at 3 pm. Please arrive by 4 pm."
```

The room usually spots it in under five seconds, and that is the point — they can do this. Then move to the hard case, where fluency hides a contradiction:

```text
Summarise this policy for a customer:
"Refunds are available within 14 days of delivery, provided the item is
unused. Items marked final sale are non-refundable. Refunds on final
sale items are processed within 7 days of request."
```

What to point at afterwards: a fluent summary will state both that final-sale items cannot be refunded and that their refunds are processed in seven days. The source contradicts itself, and a good answer *flags the contradiction* rather than picking one side. That is the highest-value behaviour this bullet teaches, and almost nobody asks for it in the prompt.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — the 3 p.m./4 p.m. example, which everyone catches, to build confidence.
2. **State the objective** — by the end you can separate quality from coherence and say which failed.
3. **Recall prior learning** — what generation actually does, token by token.
4. **Present the content** — the four checks, contradiction versus fabrication, the overlap trap.
5. **Guide** — mark the contradictory policy summary together.
6. **Elicit performance** — pairs review two outputs and write one sentence per failure.
7. **Give feedback** — debrief, rewarding those who flagged the source contradiction rather than resolving it silently.
8. **Transfer** — each learner reviews one output from their own work with the four checks.

## What the framework doesn't mention but trainers need to know

- **Most quality complaints are prompt complaints.** Before blaming the model, check whether the instruction specified the audience, the length and the source. It usually did not.
- **Ask the model to flag insufficiency.** "If the source does not answer this, say so" is a one-line instruction that removes a large share of fabrication.
- **Coherence decays with length.** Check the fourth paragraph, not the first; drift lives at the end.
- **Human reviewers over-reward formatting.** Bold headings and bullet lists raise perceived quality. Score content before style, or the style wins.
- **The reviewer is a single point of failure.** Two reviewers on a sample of twenty outputs will disagree, and the disagreement is the most useful data you will collect that week.

## Watch out

- **Do not grade on fluency.** It is the easiest trap to fall into and the hardest to unteach.
- **Do not accept "the model said it, so it must be in the document".** Open the document.
- **Do not demo only obvious errors.** The 3 p.m. example teaches detection of the trivial. The valuable cases are fluent, plausible and wrong.
- **The stale claim to retire:** "we can eyeball it." Eyeballing is where this bullet starts, not where it ends.
