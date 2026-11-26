---
id: 07.02.I.A6
tsc: 7
level: Intermediate
code: A6
title: Data transformation: shaping examples so the model learns the right thing
---

# Data transformation: shaping examples so the model learns the right thing

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Ability A6**


> **Framework text (verbatim):** "Apply data transformation techniques to improve model learning."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Ability · Bullet 16 of 17

**One-line version:** Training data is not your documents — it is a shaped example of the behaviour you want at inference, and the shaping is the skill.

## What it is

Transformation changes how a record is *represented* rather than what it says: formatting into the model's template, normalising units and dates, restructuring a spreadsheet into instruction–response pairs, masking the loss to the answer, augmenting for variety, ordering for curriculum. The aim is to make the learning signal match the behaviour you will ask for in production.

## Deep expansion

### The concept

The single test for any transformation is train–inference parity: will the model see, at inference time, the same shape of input it saw during training? Most transformation bugs fail this test invisibly. A model trained on bare questions and deployed inside a template with a system prompt learns a distribution it never saw, and the loss curve stays beautiful while production quality sags. Transformation is where you decide what the model is actually graded on, so it deserves design attention, not a one-line format conversion.

### The sub-concepts

**Representation and formatting.** Apply the model's own chat template and special tokens; keep role markers consistent; normalise dates, currencies and units so the same fact is not encoded three ways; canonicalise entity names so the model does not learn that "Pte Ltd" and "Private Limited" are different companies. Store one canonical form and generate variants from it.

**Loss targeting.** Mask the loss on prompt tokens so the model is graded on its answer. Decide the truncation policy explicitly: repeatedly cutting long answers mid-sentence teaches the model that answers end abruptly. Weighting or label smoothing is worth trying only after the basics are right.

**Restructuring.** Turn a Q&A spreadsheet into instruction–response pairs with varied phrasings of the instruction; assemble multi-turn conversations from ticket threads in chronological order; prepend a short plan or reasoning before the answer where it can be verified; include hard negatives that are close to correct.

**Augmentation and ordering.** Paraphrase instructions to break surface memorisation; back-translate for linguistic variety; swap entities counterfactually; then order the data — a gentle easy-to-hard curriculum with diversity-aware shuffling often trains better than random order, and packing short examples reduces padding waste.

### How it connects to the rest of the framework

`TSC7-Intermediate-K8` covers selection and cleaning, of which this is the shaping half; `TSC7-Intermediate-A4` is the pipeline these transformations live in; `TSC7-Intermediate-K4` explains the loss and metrics the transformations target; `TSC7-Intermediate-K9` supplies synthetic augmentation; `TSC7-Intermediate-A7` reuses the same shaping for continued pre-training text.

### What is current as of November 2026

- **Chat templates are per-model and still a common bug.** Building on the GPT-6 generation, Claude 5.5 or Gemini 3.1 Pro through managed fine-tuning hides some of this; open-weight tuning does not.
- **Reasoning traces became a transformation target.** Training on a plan-then-answer structure is common, with the caveat that only verifiable traces should be trusted as targets.
- **Structured output training matured.** Teaching a model to emit a schema is now routine, and it interacts with constrained decoding at inference.

### Common misconceptions

- *"Transformation is just formatting."* It is decisions about what gets graded, what gets truncated and what counts as the same fact.
- *"Longer examples are richer."* They are more expensive and more prone to truncation; a tight example teaches the same behaviour.
- *"Converting to chat format is trivial."* It is the most frequent silent failure in open-weight fine-tuning.
- *"Augmentation always helps."* Augmentation that shifts the label teaches a false rule at scale.

## How a student should understand it

**Mental model:** the stall's mise en place. Same chicken, same chilli — but cut to the size the wok needs, portioned per plate, and lined up so service runs. Bad prep cannot be fixed by a better wok.

**Three things they can do after this bullet:**
1. Transform a source export into training examples that match inference exactly.
2. Choose a truncation and masking policy and state its consequences.
3. Run a parity check between a training example and a live production request.

**Misconceptions to kill:** that formatting is cosmetic, that longer is better, and that augmentation is free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Cutting ingredients for the wok.** The same chicken thigh is diced for hor fun and sliced for curry chicken. Nothing about the chicken changed; the cut determines what the wok can do with it. A model is the wok: the cut decides the dish. Where it breaks: a cook can re-cut the chicken mid-service; a dataset is cut once, and every later prompt is served from that cut.

**Practising in exam format.** A student who only practises answering verbally freezes when handed a written paper with a fixed structure. Training on a different shape from the exam is the same mistake, and the student's knowledge is not the problem. Where it breaks: the student is told the format before the paper; the model's exam is live traffic, which nobody gets to preview.

### Worked example with a real tool

A learner has a CSV of 2,000 question–answer rows. Type this into a coding assistant:

```
Transform faq.csv (columns: question, answer, product) into training
data for an instruct model:

1. Render each row with the model's chat template: system prompt with
   the product name, user = question, assistant = answer.
2. Produce 3 instruction variants per row (direct question, "Help me
   with...", and a terse keyword form), then deduplicate variants.
3. Mask loss on system and user tokens; assert the assistant span is
   non-empty and under the max length, and report how many rows would
   be truncated at 2,048 tokens.
4. Emit JSONL plus a parity check: take 20 rows, render them the same
   way the production API will, and assert the token sequences match.
```

Point at step 3's truncation report — the answers that would be cut are the ones the model will learn to cut — and step 4, the parity check: it is ten lines of code that prevent the most common class of silent fine-tuning failure.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a fine-tune that works in the notebook and fails behind the API.
2. **State the objective** — transform a source file into parity-checked examples.
3. **Recall prior learning** — cleaning and splitting from K8.
4. **Present the content** — representation, loss targeting, restructuring, ordering.
5. **Guide** — render one example by hand in the template together.
6. **Elicit performance** — teams transform 100 rows of their own data.
7. **Give feedback** — debrief: does the rendered example match production?
8. **Transfer** — each learner adds a parity assertion to their pipeline.

## What the framework doesn't mention but trainers need to know

- **Template drift breaks models quietly.** A base-model upgrade that changes the template invalidates a fine-tune built on the old one.
- **Tokenizer quirks show up in the data.** Whitespace, special characters and emoji can split differently than expected; check a sample of tokenisations, not just the text.
- **Truncation is a behaviour, not a limitation.** Whatever you cut, the model learns to imitate.
- **Augmentation changes the evaluation too.** If you augment the test set, the metric no longer reflects production.

## Watch out

- **Do not treat template mismatch as a minor detail.** It is the most common cause of "the fine-tune did nothing".
- **Do not pad examples to a uniform length.** Padding teaches the model to produce padding.
- **Do not augment without a label-invariance test.** Show the pair and ask whether the correct answer changed.
- **The stale claim to retire:** "just convert it to JSONL." In November 2026 the conversion is the modelling decision.
