# RAG-01 · Retrieval-Augmented Generation, explained without jargon

**Framework home** — New GenAI TSC #6 Generative AI Application Development and Deployment, **Basic to Intermediate**: K *concepts behind context augmentation for prompts, including RAG*; A *apply RAG using vector databases and retrieval algorithms*.

---

## What it actually is

RAG is an **open-book exam**: rather than trust what the model absorbed in training, you find the relevant pages at question time and put them in front of it.

1. **Index.** Documents are cut into passages, each turned into a vector — numbers that place it by meaning — and stored.
2. **Retrieve.** The question is vectorised too, and the nearest chunks fetched — similarity by meaning, not keyword, so "how much notice must I give" can pull a clause on "termination period".
3. **Generate.** Question and chunks go to the model together, told to answer from them.

It reduces hallucination without removing it: retrieval can miss the right chunk, chunking can split an answer across a page break, a chunk can be stale, the model can ignore what it was handed. Each looks like a fluent, confident answer.

What makes it work is unglamorous: chunking that follows document structure, permissions enforced at retrieval, citations to the clause, a named owner of freshness.

To judge a product, ask three questions its documents should answer, then one they cannot: a good one admits it, a bad one invents.

## Why it matters at work

An internal policy assistant answering from last year's circular produces a wrong entitlement, then a wrong approval. The failure is quiet.

## The student lens

**Mental model to install:** a librarian fetches three pages, and the model answers from those three. It never saw the shelf.

**Misconceptions you will hear:**
- *"RAG means it knows our documents."* It gets a few excerpts, each time.
- *"RAG stops hallucination."* It removes the commonest cause and leaves the rest.
- *"More documents is better."* More near-misses for the same slots.

**Five-minute practice:** upload one policy document, ask what it answers, then ask what it cannot, and watch whether it admits the gap.

## The adult educator lens

**Analogy:** asking a colleague to answer from the file rather than from memory. Where it breaks: the colleague notices an incomplete file and says so; the model answers anyway.

**Three-minute demo:**
1. Upload a leave policy. Ask how many days of childcare leave apply, and show the citation.
2. Ask something split across two clauses — eligibility in one, the cap in another. Show the half-answer and name chunking.
3. Ask about a policy not in the document; watch it refuse or invent.

**Board sketch:** DOCUMENTS → INDEX → MODEL, arrows labelled "chunk and embed, refreshed on change" and "top few chunks only". Circle INDEX: "permissions live here".

**Where it goes wrong in class:** someone says "so we index the whole shared drive". Two things break. Permissions: an index is a copy, and a copy inherits none of your access control unless you build it in. Freshness: nobody owns the refresh.

**Check for understanding:** "The system answers from a superseded policy. Which step failed, and who should have caught it?" (Indexing or retrieval; the document owner.)

## Say this out loud

"RAG doesn't teach your AI your documents. It hands it three pages a librarian chose — so check who chose them."

## Content hook

**LinkedIn opener:** "Everyone selling 'chat with your documents' is selling RAG. Nobody sells the part that matters: which three pages it picks."

**Carousel idea:** "Four questions to ask before buying a document chatbot", good answer against bad.
