---
id: 07.02.I.K3
tsc: 7
level: Intermediate
code: K3
title: Multi-modal models: one shared space for text, image and sound
as_at: 2026-11-26
review_by: 2027-02-25
---

# Multi-modal models: one shared space for text, image and sound

> **TSC #7 Generative AI Model Development and Fine Tuning · Intermediate · Knowledge K3**


> **Framework text (verbatim):** "Multi-modal embeddings and models."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Intermediate** · Knowledge · Bullet 3 of 17

**One-line version:** A multi-modal model is two encoders taught to point in the same direction, so that a sentence and a photograph become comparable numbers.

## What it is

Multi-modal means a model handles more than one kind of data — text, image, audio, video, document layout — as input, output, or both. Two mechanisms make it work: a *shared embedding space* where different modalities become comparable vectors, and *connector architectures* that feed non-text encoders into a language model. This bullet is about the embeddings; the models are what you build on top.

## Deep expansion

### The concept

An embedding turns a thing into a point in space, positioned so that similar things are near each other. Multi-modality is the problem of making *different kinds* of thing land near each other: the phrase "plate of char kway teow" and a photograph of one should occupy roughly the same neighbourhood. That is not a property of either encoder alone; it is trained by showing millions of pairs and penalising pairs that land far apart. Once the space exists, everything from text-to-image search to zero-shot classification becomes arithmetic.

### The sub-concepts

**Contrastive alignment.** Image encoder and text encoder are trained together on paired data, with a loss that pulls matched pairs together and pushes mismatched pairs in the batch apart. The batch is the negative set, which is why batch size matters so much in this training. The result supports zero-shot classification: embed the class names, embed the image, take the nearest. One known artefact is the *modality gap* — images and text cluster in separate regions even when matched, so absolute similarity scores are not comparable across modalities.

**Connectors.** To let a language model "see", a vision encoder's output is projected into the model's token space — a simple MLP, a resampler, or a query transformer that compresses an image into a fixed number of tokens. The design question is always the same: how many tokens may an image cost? More tokens means finer detail and a larger context bill.

**Where they earn their keep.** Cross-modal retrieval (search a photo library by description), deduplication of near-identical assets, RAG over scanned documents and slide decks, clustering unlabelled media, and scoring generated images against their prompts.

**Where they fail.** Counting, dense tables, small print, spatial relations ("the cup left of the saucer"), and any domain where captions in the pre-training data were thin — Singlish, Malay and Tamil material is underrepresented relative to English web text, so alignment is weaker exactly where local deployments need it.

### How it connects to the rest of the framework

`TSC7-Basic-K5` is tokenisation and embeddings at the entry level; `TSC6-Intermediate-K4` covers the retrieval architectures these vectors feed; `TSC5-Intermediate-K2` includes the embedding-based metrics used to score generated media; `TSC7-Intermediate-K9` uses these encoders to filter synthetic data; `TSC7-Advanced-K4` goes to vision transformers as a research frontier.

### What is current as of November 2026

- **Multi-modality moved from bolt-on to native.** Current frontier models all accept images, documents and audio in the same interface, and early-fusion training has largely displaced the "attach a vision encoder afterwards" pattern for frontier models.
- **Dedicated embedding models became a product category.** It is now normal to buy text-and-image embeddings from one API rather than run two incompatible open models.
- **Document understanding absorbed a lot of OCR work.** Pages are increasingly handled as images by a vision-language model rather than by a text-extraction pipeline, with the trade-off being cost per page and silent misreads.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"It watches video."* It samples frames plus, sometimes, an audio track. Fast motion and events between frames are missed.
- *"High similarity means it matches."* Similarity is a ranking signal, calibrated only within one model and one preprocessing pipeline.
- *"More modalities is always better."* Every added modality adds a failure surface, a token cost and an evaluation you must write.
- *"Embeddings are interchangeable."* Vectors from different models, or different versions of one model, are not comparable and must be re-embedded together.

## How a student should understand it

**Mental model:** a hawker centre where every stall accepts the same currency. Each stall (modality) sells something different, but a price means the same thing anywhere in the building — as long as you stay in that building.

**Three things they can do after this bullet:**
1. Explain how text-to-image search works without a caption database.
2. Choose how many visual tokens a task can afford, and say what detail that buys.
3. Name three tasks where a vision-language model will fail predictably.

**Misconceptions to kill:** that the model sees video, that similarity is truth, and that embeddings are portable between models.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The bilingual signboard.** One concept, two scripts, same meaning — that is a matched pair in training. The signboard only works because someone aligned the two scripts; nobody expects a Tamil signboard to be understood by a reader who only knows English, which is exactly why under-represented languages align worse. Where it breaks: the signboard was aligned by a person who reads both scripts; a model's alignment is learned from whatever caption pairs it was given, and those are thinner for Tamil than for English.

**The food court price board.** Every stall lists prices in dollars, so you can compare a $4 noodle and a $12 fish head without converting. Where it breaks: the board is only trustworthy inside that one food court. Take the number to another building and it means nothing — the modality gap and the cross-model incompatibility in one image.

### Worked example with a real tool

A learner has 4,000 product photos with no usable tags and wants search by description. Type this into Claude or a coding assistant:

```
Using open_clip and the photos in ./catalogue (4000 jpgs):

1. Write a script that embeds every image once and caches the
   vectors to embeddings.npy with a matching filenames.json.
2. Normalise the vectors and build a numpy cosine-similarity search.
3. Accept a text query, embed it with the same model and tokenizer,
   and print the top 10 filenames with scores.
4. Print the score distribution for one query so I can see whether
   the ranking is meaningful or flat.
```

Point at the cache step (re-embedding 4,000 images because someone changed the query code is the most common waste), the shared-model requirement for query and index, and the score distribution — a flat distribution means the queries are outside what the model was trained to separate, which is a data finding, not a bug.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — type a description, watch the right photo surface from 4,000.
2. **State the objective** — build a working text-to-image index and know its limits.
3. **Recall prior learning** — embeddings and tokenisation from Basic.
4. **Present the content** — alignment, connectors, token budgets.
5. **Guide** — embed one image and one sentence live, show the similarity.
6. **Elicit performance** — pairs write three queries that *should* fail, then test them.
7. **Give feedback** — debrief the failures: counting, small text, Singlish.
8. **Transfer** — each learner names one folder in their job this could index.

## What the framework doesn't mention but trainers need to know

- **Re-embedding is a migration, not a refresh.** Changing embedder version invalidates every stored vector and every threshold tuned on the old ones; plan it like a schema change.
- **Faces and voices are personal data.** An image index over staff photos is a PDPA question before it is a retrieval question.
- **Caption quality caps alignment quality.** If your paired data was captioned by a template ("product image 4471"), the model learns the template, not the content.
- **Vector storage has a bill.** Millions of embeddings in memory is fine; billions needs an index and an operational owner.

## Watch out

- **Do not say the model "sees".** It maps pixels to vectors learned from pairs; that framing prevents most overclaiming in the room.
- **Do not compare similarity scores across models.** Learners will quote 0.31 versus 0.78 from two systems as if it meant something.
- **Do not skip the flat-distribution check.** Without it, a demo that returns ten random images looks like a success because something came back.
- **The stale claim to retire:** "multi-modal needs a special model." In November 2026 the default chat model is multi-modal; the specialist work is in embeddings, token budgets and evaluation.
