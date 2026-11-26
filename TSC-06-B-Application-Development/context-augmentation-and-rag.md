---
id: 06.01.B.K1
tsc: 6
level: Basic
code: K1
title: "Context augmentation: giving the model the right page before it answers"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Context augmentation: giving the model the right page before it answers

> **TSC #6 Generative AI Application Development and Deployment · Basic · Knowledge K1**


> **Framework text (verbatim):** "Concepts behind context augmentation for prompts (e.g., Retrieval Augmented Generation (RAG))."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Knowledge · Bullet 1 of 11

**One-line version:** The model does not need to be taught your documents — it needs to be handed the right page at the moment it answers.

## What it is

Context augmentation means putting the information a model needs into the prompt at request time, rather than assuming it already knows. Retrieval Augmented Generation (RAG) is the common pattern: search your own documents, take the best-matching passages, paste them into the prompt, and instruct the model to answer only from what it was given.

## Deep expansion

### The concept

A model's knowledge is frozen when training ends, and it is generic. It has never read your leave policy, your price list or last week's incident report. Ask it anyway and it will not shrug — it will produce a fluent answer assembled from everything *similar* it has seen. That is the failure that breaks trust in the first week of any pilot.

Context augmentation fixes this without retraining. **Fine-tuning changes how a model behaves; context augmentation changes what it knows right now.** The model does not need to be taught your handbook; it needs to be briefed, every time, like a consultant handed the file at the door.

The pattern has two halves that fail differently. Retrieval is ordinary search engineering. Generation is prompting. Many bad RAG answers are retrieval failures wearing a generation costume.

### The sub-concepts

**The context window is a desk, not a warehouse.** Everything the model can see for one request sits in that window: instruction, history, retrieved passages. The desk is finite and you pay for every item on it.

**Grounding.** An answer is grounded when each claim traces to a supplied source. That is what turns "the model thinks" into "the document says", and it is why RAG exists in regulated workplaces.

**Retrieval is not training.** Nothing is learned. Delete the index and the model is unchanged — which also means a stale index answers confidently and wrongly.

**The loop.** Index (chop documents into passages and store them) → retrieve (find the passages nearest the question) → augment (paste them in) → generate (answer with citations).

**Chunking and embeddings.** Passages become vectors — lists of numbers representing meaning — so "how much notice must I give" lands near a passage about resignation periods even though the words differ.

### How it connects to the rest of the framework

This bullet is the concept; `TSC6-Basic-A2` is the build; `TSC6-Basic-K4` names the frameworks that shorten it. `TSC7-Basic-K5` explains the embeddings underneath, `TSC6-Basic-K3` catalogues where it goes wrong, and `TSC5` supplies the evaluation that tells you retrieval is the problem.

### What is current as of November 2026

Context windows grew enormously and RAG did not die. Long context is expensive per request, slower, and models attend unevenly across very long inputs — the middle of a huge prompt gets weaker attention than the edges. Retrieval survives as a cost and attention technique, not just a knowledge technique.

- **Retrieval became agentic.** The model issues several searches, reads results, searches again. The current flagships — the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — do this natively when given a search tool.
- **Hybrid search plus reranking is the default.** Keyword and vector search together, then a reranker. Pure vector search is now a beginner's choice.
- **"Context engineering" became the term of art** — deciding what occupies the window. That is what this bullet is really about.

### Common misconceptions

- *"RAG trains the model on my documents."* It does not. Nothing is stored in the weights; the document is fetched fresh each time.
- *"With RAG it can't be wrong."* It can: the wrong passage was retrieved, or the right one was misread.
- *"Just paste the whole document in."* Fine for one short file. At forty pages it is expensive, slow and diluting.

## How a student should understand it

**Mental model:** an open-book exam. The student is clever but knows only what is on the page in front of them — and you choose the page.

**Three things they can do after this bullet:**
1. Explain why a chatbot invents policy details, and why the fix is supply rather than training.
2. Describe the four steps of the loop and say which one to check first when an answer is wrong.
3. Judge when a file upload is enough and when a real indexed corpus is required.

**Misconceptions to kill:** that RAG teaches the model, that grounding removes error, and that more context is automatically better.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The open-book exam.** Every learner has sat one. You bring the book, but you still have to find the right chapter under time pressure, and you can still misread the page. Retrieval quality is the index at the back; reading quality is the model. Where it breaks: an open-book exam assumes the book is complete, so learners must accept that a missing answer should produce "not stated".

**The colleague with no filing cabinet.** Brilliant, fast, has read everything public, has never seen a document in your office. You would not ask about your notice period without passing them the handbook.

### Worked example with a real tool

Create a project in ChatGPT, Claude or Gemini with a real 40-page staff handbook attached. Type:

```
Using only the staff handbook in this project, answer:
1. How many days' notice must a confirmed employee give to resign?
2. Quote the exact clause and give its clause number.
3. If the handbook does not cover this, say "not stated in the handbook"
   instead of guessing.
```

Then open a fresh chat with no document attached and ask question 1 alone.

What to point at afterwards: the first answer cites a clause you can verify in ten seconds; the second is confident, generic and probably wrong for your company. Same model, same question, different supply. Then ask something the handbook genuinely does not answer, and show that a well-instructed app says so instead of inventing one.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room for your company's resignation notice period, then ask the model with no document. It gets it wrong. Start there.
2. **State the objective** — by the end you can explain context augmentation, run the loop in a no-code tool, and tell a retrieval failure from a generation failure.
3. **Recall prior learning** — knowledge cutoff, hallucination and the finite context window from TSC #1.
4. **Present the content** — index, retrieve, augment, generate on the board, with the failure mode at each step.
5. **Guide** — do the handbook question together, narrating which chunk you expect back.
6. **Elicit performance** — pairs attach one document and write three questions: answerable, not answerable, ambiguous.
7. **Give feedback** — project two or three. Spend the time on "not in the document"; that is where trust is built.
8. **Transfer** — each learner names one corpus in their department worth indexing, and one reason it must not be.

## What the framework doesn't mention but trainers need to know

- **Retrieval quality does most of the work.** Chunking, cleaning and metadata beat prompt tweaking every time. Learners expect prompt magic; correct that early.
- **Permissions are part of RAG design.** If an HR document is retrievable by everyone, the app has leaked it regardless of what the interface shows. That is a PDPA conversation.
- **The index is a copy, and copies rot.** Ask who refreshes it. A RAG app with an unowned index becomes quietly wrong within a quarter.

## Watch out

- **Do not demo "RAG" by pasting three sentences into a chat.** That teaches copy-paste, not retrieval.
- **Do not let a citation pass as verification.** It tells you where to look, not whether the model read it correctly.
- **The stale claim to retire:** "RAG is a stopgap until context windows get big enough." Long context and retrieval now coexist, because cost, latency and attention still argue for supplying less, better.
