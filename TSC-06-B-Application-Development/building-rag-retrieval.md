---
id: 06.01.B.A2
tsc: 6
level: Basic
code: A2
title: "Building retrieval: chunk, embed, retrieve, answer, and know which step failed"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Building retrieval: chunk, embed, retrieve, answer, and know which step failed

> **TSC #6 Generative AI Application Development and Deployment · Basic · Ability A2**


> **Framework text (verbatim):** "Apply context augmentation using Retrieval Augmented Generation (using vector databases and retrieval algorithms)."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Ability · Bullet 8 of 11

**One-line version:** Retrieval is a search problem wearing an AI costume — and search quality, not model quality, decides whether the answer is right.

## What it is

Applying RAG means building the loop end to end: split documents into passages, convert each passage into a vector, store vectors with their text and metadata, embed the question the same way, retrieve the nearest passages, and put them into a prompt that answers only from them. In practice it is four decisions and one discipline — measuring retrieval separately from generation.

## Deep expansion

### The concept

The concept is in `TSC6-Basic-K1`; this bullet is the build. Four decisions determine almost all of the quality, and none of them is the choice of vector database: how to cut the documents, how to represent meaning, how to search, and how to instruct the answer.

The vector database is the least interesting choice. Most of the failure learners experience as "the AI is wrong" is decision one, and most of the rest is decision four.

### The sub-concepts

**Chunking follows structure, not character count.** Cut where the document already cuts — clause, section, product record. Fixed-length chunking slices answers in half and produces a passage citing nothing. Overlap is a patch, not a strategy.

**The embedding model is a pair, not a file.** The same model must embed the corpus and the query. Change it and every stored vector becomes meaningless — the whole corpus is re-embedded, at cost.

**Retrieve wide, then narrow.** Fetch the top 20 and rerank to the 5 you send. The first search is cheap and recall-oriented; the reranker is the precision step.

**Metadata is the cheapest filter.** Department, version, effective date, access level. Filtering before similarity stops a 2019 policy outranking the current one — and stops documents the user may not see from entering the prompt at all.

**The answer prompt is part of retrieval.** Retrieval that finds the right passage still fails if the instruction lets the model improvise: answer only from sources, cite, and say "not in the provided documents" when the answer is absent.

**Measure the two halves separately.** For a test set of real questions with known answers, ask one thing: did the correct passage appear in the retrieved set? If yes and the answer is wrong, the fault is generation. If no, no prompt will save it.

### How it connects to the rest of the framework

`TSC6-Basic-K1` is the concept this implements; `TSC6-Basic-A1` supplies the prompt that consumes the passages; `TSC6-Basic-K4` names the libraries. `TSC7-Basic-K5` is the embeddings machinery, `TSC6-Intermediate-K4` and `TSC6-Advanced-K3` are the next rungs, and `TSC5` gives you the evaluation discipline to know which rung you need.

### What is current as of November 2026

- **Hybrid plus reranking is the default.** Keyword search catches identifiers — policy numbers, part codes, names — that vectors blur; vectors catch paraphrase that keywords miss. Using both is standard practice, not an optimisation.
- **Agentic retrieval replaced the single query.** Assistants rewrite the question into several searches, read, and search again. Better quality, higher cost, and "how many searches did it run" is now a monitored number.
- **Postgres won many small deployments.** Vectors next to relational data removed a whole service from the stack; for a team already running Postgres it is often the correct answer.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"RAG means uploading a PDF to a chat."* That demonstrates the concept. A build has chunking decisions, an index, metadata, retrieval parameters and an evaluation set.
- *"If retrieval returned something, the answer is grounded."* It returned *something*. Whether it returned the right thing is a separate question.
- *"Bigger chunks are safer."* Bigger chunks dilute the signal, cost more tokens and bury the answer inside irrelevant text.
- *"The vector database is the hard part."* It is the easiest part. Chunking and evaluation are the work.

## How a student should understand it

**Mental model:** the clerk who fetches five files for the partner. If the clerk brings the wrong five, the most brilliant partner in the firm still writes the wrong letter — and blames the filing.

**Three things they can do after this bullet:**
1. Build the loop end to end on a real document set, in code or a managed pipeline.
2. Set chunk size, overlap, top-k and a metadata filter, with a reason for each value.
3. Diagnose a bad answer as retrieval or generation failure using one concrete test.

**Misconceptions to kill:** that the vector database is the skill, that more context is better context, and that a plausible answer from retrieved text is grounded.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The library catalogue versus the shelf.** The catalogue tells you which shelf to walk to; it does not read the book for you. Embeddings are the catalogue, and if the catalogue is wrong no amount of reading speed helps. Where it breaks: a real catalogue is kept by a librarian with judgement — your index is kept by whatever script you wrote on Tuesday.

**The wanton mee stall's two cooks.** One fills the bowl, one finishes it. If the first cook gives the wrong noodles, the second cook's excellent sauce does not save the dish. Retrieval is the first cook; customers only ever complain about the dish.

### Worked example with a real tool

Build it in a notebook over a real document set with pgvector, Chroma or a managed service — the code is short — then test with the assembly prompt:

```
Answer staff questions using only the sources below.

Rules:
- If the answer is not in the sources, reply "Not in the provided documents"
  and name what is missing.
- Cite the source name and clause number after each claim.
- Do not combine sources to infer a rule that neither states.

SOURCES:
[1] {source_name} — {clause}
{chunk_text}

QUESTION: {user_question}
```

Then run a fixed set of ten questions: five the corpus answers, two it does not, three where two documents conflict.

What to point at afterwards: open the retrieved-chunks panel (Streamlit makes this easy) and show which passages were actually sent. For the failing question the correct clause is absent, and the authoritative-looking answer was assembled from a neighbouring clause. Then change the chunking from fixed length to section-based, re-index, and rerun the same ten questions. The score moves and the code barely changed — which is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a confidently wrong answer with a citation, then reveal the retrieved chunk. The room assumes the model lied; it did not.
2. **State the objective** — by the end you can build the loop, set the four decisions deliberately, and tell a retrieval failure from a generation failure.
3. **Recall prior learning** — the RAG loop and open-book exam from K1; embeddings from the tokenisation bullet.
4. **Present the content** — the four decisions, then the one measurement that separates the failure modes.
5. **Guide** — index a small document set together, run three questions, inspect the chunks each time.
6. **Elicit performance** — pairs take a real department document, choose a chunking strategy, and write five test questions including two unanswerable ones.
7. **Give feedback** — run two pairs' indexes against each other's questions. The strategy that looked reasonable on paper usually loses.
8. **Transfer** — each learner writes the evaluation set for their own corpus before any code, and names who maintains the index.

## What the framework doesn't mention but trainers need to know

- **Access control belongs in retrieval.** If the index holds documents a user may not see, filtering must happen before the passages enter the prompt. This is the highest-consequence mistake in the bullet.
- **Re-indexing is a scheduled job with an owner.** Documents change; indexes do not update themselves, and a stale index answers confidently and wrongly.
- **Embedding costs are paid twice** — once to build, again when the model or the chunking changes. Budget for the second.

## Watch out

- **Do not demo RAG with three sentences pasted into a prompt.** It teaches copy-paste, not retrieval.
- **Do not hide the chunks.** The moment the room sees what was retrieved, the conversation becomes engineering instead of blame.
- **The stale claim to retire:** "vector search alone is enough." Hybrid retrieval with a reranker is the 2026 baseline, because identifiers and exact phrases still matter in real documents.
