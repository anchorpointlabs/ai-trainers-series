---
id: 06.03.A.K3
tsc: 6
level: Advanced
code: K3
title: "Cutting-edge context augmentation: beyond pasting documents into the prompt"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Cutting-edge context augmentation: beyond pasting documents into the prompt

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Knowledge K3**


> **Framework text (verbatim):** "Cutting edge context augmentation techniques."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Knowledge · Bullet 3 of 12

**One-line version:** Basic RAG finds text that looks similar; the frontier is selecting, ordering and compressing the *right* evidence at the moment of the question — and knowing which trade you just made.

## What it is

Context augmentation is everything that puts outside knowledge into the prompt at inference time: retrieved passages, records, graph facts, tool output, conversation memory. Cutting-edge techniques are the ones beyond "embed the documents, take the top five by cosine similarity" — hybrid search, reranking, query decomposition, graph traversal, agentic retrieval loops, multimodal page retrieval, and deliberate context assembly. The discipline now has a name of its own: context engineering.

## Deep expansion

### The concept

The Basic version treats retrieval as a lookup: one question in, five chunks out. The advanced version treats it as a *selection problem under a budget* — the budget being tokens, latency, money and the model's attention. Three things changed the problem. Corpora got large enough that recall, not ranking, became the bottleneck. Context windows got long enough that "just include more" became technically possible and economically foolish. And questions got multi-hop — "which of our suppliers of the failed part is also overdue on ISO renewal" cannot be answered by any single chunk.

So frontier work splits into four moves: **find more candidates** (hybrid, multimodal), **rank them better** (reranking, query understanding), **connect them** (graphs, structured queries, iterative search), and **assemble them well** (dedupe, order, compress, cite). Most teams do only the first and wonder why quality plateaus.

### The sub-concepts

**Hybrid retrieval.** Lexical search (BM25-style) catches exact tokens — policy numbers, part codes, names, negations — that dense embeddings blur. Dense retrieval catches paraphrase. Fuse the two rankings rather than choosing; the combination is usually better than either alone and costs almost nothing.

**Reranking.** Retrieve wide (fifty candidates) with a cheap method, then score with a cross-encoder that reads question and passage together and keep the best five. In many systems this is the largest single quality gain per dollar, because the first-stage ranker was never designed to be precise.

**Query understanding.** Rewrite the user's question before searching: expand acronyms, resolve "it" from conversation, split a two-part question into two searches, or generate a hypothetical answer and search for that. Cheap, and it fixes the most common failure — searching for the wrong thing confidently.

**Chunking as architecture.** Chunk boundaries determine what can ever be found. Parent-child chunking retrieves a small precise passage but returns the surrounding section. Tables and clauses must stay whole, or retrieval returns a number with no column header.

**Graph and structured retrieval.** Entities and relationships support multi-hop questions and global summaries ("what are the recurring complaints across all tickets"). Text-to-SQL covers anything numeric and live. These are the tools for questions that similarity search structurally cannot answer.

**Agentic retrieval.** The model plans a search, reads results, notices a gap, searches again. It handles multi-hop and ambiguous questions well and costs latency, money and predictability — you cannot promise a fixed response time for a loop.

**Context assembly.** Ordering (put the strongest evidence last or first, consistently), de-duplication, compression, and stable citation identifiers so the answer can be traced to a clause.

### How it connects to the rest of the framework

`TSC6-Basic-K1` is the concept this extends — RAG as idea, not as technique. `TSC6-Intermediate-K4` names knowledge graphs specifically; this bullet covers the wider frontier and how the techniques combine. `TSC6-Advanced-A1` is building applications that use them; `TSC6-Advanced-A4` is articulating the trade-offs, which is a separate, harder skill. `TSC6-Advanced-K1` sets the budget that every one of these techniques spends.

### What is current as of November 2026

- **Long context changed retrieval's job, it did not remove it.** With million-token-class windows, a 300-page corpus can be pasted whole — but cost per query, latency, and attention dilution make selective retrieval still the default for anything at volume or anything that changes daily.
- **Reranking is standard, not advanced.** Most managed retrieval services include a reranker; the differentiator is now query understanding and assembly.
- **Agentic retrieval moved from research to product.** Assistants that search, read and iterate are common in 2026, and the design question is now how to bound the loop.
- **Page-level multimodal retrieval is routine for PDFs.** Retrieving a rendered page image rather than parsed text preserves tables and layout that text extraction destroys.
- **Graph retrieval is used where the questions are relational**, typically compliance, supply chain and case history — not as a universal upgrade.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Long context killed RAG."* It changed the economics. Freshness, cost per query and citation requirements keep retrieval central.
- *"Embeddings understand meaning."* They capture distributional similarity, and they are weak on identifiers, numbers, negation and rare names — which is exactly what business questions contain.
- *"Retrieve more, in case."* Extra passages dilute attention, add cost and increase contradiction. Precision beats volume.
- *"Chunk size is an implementation detail."* It is a design decision that fixes the ceiling on answer quality.

## How a student should understand it

**Mental model:** the difference between an index at the back of a book and a good librarian. The index finds words; the librarian asks what you actually need, walks two shelves over, and hands you the page with the table on it.

**Three things they can do after this bullet:**
1. Diagnose a retrieval failure as recall, ranking, chunking or query — and name the technique for that layer.
2. Design a retrieval stack for a stated question type, including what it cannot answer.
3. Explain why a graph or SQL path is needed for a given question rather than more chunks.

**Misconceptions to kill:** that long context makes retrieval unnecessary, that embeddings understand meaning, and that more context is safer.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The CPF statement.** Nobody reads all forty pages to answer "how much can I withdraw at 55". You need one page — but if the number sits in a table, the table must arrive with its column headings, or the number is meaningless. That is chunking in one sentence.

**The wet-market stall auntie.** Ask for "fish for curry" and she does not hand you every fish in the tank; she asks how many people, then picks one. Hybrid search is her knowing both the names and the look of the fish; reranking is her picking the best one for your purpose. Where it breaks: she has twenty years of context you do not have, which is precisely what query understanding tries to reconstruct.

### Worked example with a real tool

Ask the same question three ways and compare, in any chat tool with file upload:

```
Context: a 40-page tenancy agreement.

Question: "Can the landlord increase the rent mid-term, and by how much?"

Answer in two sentences, quote the clause number, and say which page
the clause is on.
```

Run it (a) with the whole document pasted, (b) with three chunks retrieved by similarity, (c) with retrieval plus a reranker or with the table page included manually. Point at what changes: the whole-document run is correct but slow and expensive; the naive-chunk run misses the rent-review clause because it was split across a page break; the reranked run returns the clause and the schedule table together. The lesson is that the failure had a *layer*, and the fix was at that layer.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a confident answer citing a clause that says the opposite. Ask where it came from.
2. **State the objective** — you will pick retrieval techniques by failure layer and defend the choice.
3. **Recall prior learning** — they built a basic vector RAG in the Basic course; now they debug it.
4. **Present the content** — the four moves: find, rank, connect, assemble.
5. **Guide** — take one multi-hop question and show why no single chunk can answer it.
6. **Elicit performance** — teams map their own corpus to a stack and list what it cannot do.
7. **Give feedback** — challenge every "we will just use a bigger context window" answer with cost and freshness.
8. **Transfer** — they write a one-page retrieval design note with the failure it accepts.

## What the framework doesn't mention but trainers need to know

- **Retrieval quality is measured, not felt.** Build twenty real questions with known correct sources; score recall at k and answer correctness. Without that set, every technique argument is taste.
- **Access control must happen at retrieval.** Filtering after retrieval leaks existence and snippets; permissions belong in the query, per user.
- **Freshness has an owner.** Indexing lag is invisible until someone quotes last quarter's price. State the lag and display the document date.
- **Citations change user behaviour.** When answers carry clause IDs, users check them — and checking is the control that makes the whole system safe.
- **Latency compounds.** Rewrite, retrieve, rerank, generate, verify: each hop adds. Budget it in milliseconds before choosing the stack.

## Watch out

- **Do not present the frontier as a default.** Most business questions are answered by hybrid search plus a reranker; graphs and agentic loops are for the questions that fail.
- **Do not benchmark on vendor demo corpora.** Your documents, your jargon, your tables.
- **Do not let a learner equate "more retrieved" with "better".** Show the contradiction case: two passages that disagree.
- **The stale claim to retire:** "RAG means vector search." In November 2026 it means a pipeline, and vector search is one stage of it.
