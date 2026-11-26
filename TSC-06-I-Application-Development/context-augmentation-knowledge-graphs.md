---
id: 06.02.I.K4
tsc: 6
level: Intermediate
code: K4
title: Knowledge graphs: context augmentation that remembers relationships
as_at: 2026-11-26
review_by: 2027-02-25
---

# Knowledge graphs: context augmentation that remembers relationships

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Knowledge K4**


> **Framework text (verbatim):** "Concepts behind context augmentation techniques, such as knowledge graphs."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Knowledge · Bullet 4 of 12

**One-line version:** Vector search finds text that looks like the question; a knowledge graph knows what is connected to what — and multi-hop questions need the second one.

## What it is

Context augmentation is supplying a model with outside information at answer time instead of hoping the weights contain it. The Basic level teaches retrieval from chunks; this bullet covers the structural alternative — knowledge as entities and labelled relationships, a graph — so retrieval can follow links rather than compare similarity. The knowledge here is what a graph buys, what it costs, and when it beats a vector index.

## Deep expansion

### The concept

A vector store answers "which passages are most similar to this question". That works when the answer sits in one passage. It fails when the answer requires joining facts: *which suppliers would be affected if this one firm stopped?* No single chunk contains that. The chaining lives across documents, and similarity search has no way to walk it.

A knowledge graph stores knowledge as triples — subject, predicate, object: *(Sin Heng, supplies, Part 204)*, *(Part 204, used in, Product Y)*. Retrieval becomes traversal: start at the entity named in the question, follow the edges, collect the subgraph, serialise it into the prompt. The model's job shrinks from "find the answer in a pile of text" to "read a small, correct structure and explain it" — an easier job, and therefore a more reliable one.

### The sub-concepts

**Triples and schema.** A graph without a defined vocabulary becomes inconsistent edges — "supplies", "supplied_by", "vendor_of" for the same relationship. A small enforced predicate set is what makes traversal possible.

**Entity resolution.** The same supplier appears as "Sin Heng Pte Ltd", "Sin Heng" and "SHPL". Treat those as three entities and traversal silently under-answers. Deciding when two mentions are one thing is where most graph projects spend their effort.

**Extraction.** Graphs are usually built by running a model over documents to propose triples, then validating them. Extraction errors propagate into every later answer, so a confidence score and a human spot-check belong in the pipeline.

**Community summaries.** Build the graph, detect clusters of tightly-connected entities, pre-write a summary per cluster. Questions about themes across the whole corpus then retrieve a summary instead of a hundred chunks.

**Hybrid retrieval.** Production systems run vector search, keyword search and graph traversal together, then merge: the graph handles relations, vectors handle wording, keywords handle exact identifiers like part numbers.

**Traversal cost.** Every extra hop multiplies the nodes returned. Query depth is a deliberate parameter, not something left unbounded.

### How it connects to the rest of the framework

`TSC6-Basic-A2` is the RAG foundation — chunking, embedding, vector search — that this extends. `TSC6-Intermediate-K5` is where graph retrieval becomes a pipeline stage, and `TSC6-Advanced-K3` covers the frontier of augmentation. At Advanced level, `TSC6-Advanced-A4` asks for the trade-off articulation this bullet begins.

### What is current as of November 2026

Graph-based augmentation has moved from research pattern to product feature. Extraction with a strong model plus schema validation now yields a usable graph from a document set in days, so graph building is a pipeline rather than a consultancy engagement. The hybrid is the default: vendors ship vector-plus-graph retrieval together, making the question "how much graph" rather than "graph or vector". And agentic retrieval changed the loop — a tool-calling model can write and iterate its own traversal, which raises the value of a clean schema and lowers the value of a giant pre-built index.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A knowledge graph replaces the vector database."* It complements it. Graphs are poor at fuzzy wording; vectors are poor at relations.
- *"Graphs are automatically more accurate."* A graph built by an unvalidated extraction run is a confident map of things that are not true.
- *"You need a graph database to have a graph."* You need edges. A table of triples in Postgres is enough to prototype, and often enough to ship.

## How a student should understand it

**Mental model:** the family tree versus the photo album. The album finds the picture that looks most like this person; the tree answers "how is she related to me" — a question no photo contains.

**Three things they can do after this bullet:**
1. Given a question, say whether it is single-hop (vector is fine) or multi-hop (graph earns its keep).
2. Sketch five triples for a domain they know, with a consistent predicate vocabulary.
3. Name where extraction error would enter their graph, and how they would catch it.

**Misconceptions to kill:** graph replaces vector, graphs are automatically more accurate, and you need a specialist database to start.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**CNY visiting.** Someone at the door says "call me *yi po*". A photo album cannot tell you why; the family tree can — your mother's sister. The album is the vector store: great for "who does this look like", useless for "how are we related". Where it breaks: a family tree is stable for decades, while a business graph changes every time a supplier is added.

**The MRT network map.** Similarity search finds the station whose name most resembles what you typed. The network map tells you which line connects to which and how many interchanges it takes. Break: the map is drawn by one authority and is always current; a business graph is assembled from documents and is always slightly behind.

### Worked example with a real tool

Build a five-minute graph in the chat window before touching any database. In Claude:

```
Here are six facts about a small manufacturer.

Sin Heng supplies Part 118 and Part 204.
Part 118 goes into Product X. Part 204 goes into Product X and Product Y.
Jurong Metals supplies Part 204. Product Y is sold to Client A.

Turn this into triples (subject, predicate, object). Then answer:
if Sin Heng stops supplying, which products and which clients are
affected? Show the path you followed.
```

What to point at afterwards: the answer needs two hops (Sin Heng → Part 204 → Product Y → Client A), and no single input sentence contains it. Then ask the same question of a plain vector search over the same six lines — it retrieves a similar-sounding sentence and misses the chain. That comparison, in ninety seconds, is the whole argument for graphs.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room a multi-hop question about their own organisation, then watch the chat model guess.
2. **State the objective** — you will tell single-hop from multi-hop questions and choose the right retrieval structure.
3. **Recall prior learning** — they know chunking and vector search from Basic RAG (TSC6-Basic-A2).
4. **Present the content** — triples, schema, entity resolution, extraction, hybrid retrieval, traversal cost.
5. **Guide** — build the six-fact graph together and trace the two-hop path on the whiteboard.
6. **Elicit performance** — each table writes five triples from their own domain and one question those triples answer that text search cannot.
7. **Give feedback** — the common flaw is an inconsistent predicate; normalise it live in front of the room.
8. **Transfer** — they name one relational process in their work (supply chain, org structure, regulatory dependency) as a graph candidate.

## What the framework doesn't mention but trainers need to know

- **Maintenance is the real cost.** A vector index can be rebuilt from source documents at any time; a graph accumulates human judgement in its schema and its merges, and someone must own it.
- **Entity resolution is the project.** Budget most of the effort there. Trainers who skip it produce demos that collapse on real data.
- **Graphs make good audit trails.** Because the path is explicit, you can show *why* an answer was given — worth more than accuracy in regulated settings.
- **Start smaller than feels comfortable.** Forty entities and five predicates teach more in a week than a 400,000-node ingestion run does in a quarter.

## Watch out

- **Do not let the session become a graph-database tutorial.** Neo4j, Neptune or a Postgres table — the concept is the edges, not the engine.
- **Do not demo a hand-built graph as an automated pipeline.** Say plainly that a model built it and a human checked a sample.
- **Do not oversell accuracy.** A graph improves traceability and multi-hop recall; it does not fix a model that misreads clear text.
- **The stale claim to retire:** "RAG means vector database." In November 2026 retrieval is a family — vector, keyword, graph, agentic query loops — and picking one is an architecture decision.
