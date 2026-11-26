---
id: 03.03.A.K5
tsc: 3
level: Advanced
code: K5
title: Extending models with RAG, tools, and LangChain
---

# Extending models with RAG, tools, and LangChain

> **TSC #3 Prompt Engineering · Advanced · Knowledge K5**

> **Framework text (verbatim):** "Techniques that extend capabilities of generative AI models (e.g., Retrieval Augmented Generation (RAG), external tools and libraries such as Langchain)."
>
> **TSC #3** Prompt Engineering · **Advanced** · Knowledge · Bullet 5 of 13

**One-line version:** The model stays the language engine; you supply the knowledge it never had and the hands it never had — retrieval, tools, and a library to wire them together.

## What it is

Three techniques that answer the same limitation. A model knows only what was in its training data and can only emit text. **RAG** fetches relevant passages from your own documents at question time and puts them in the prompt so the answer is built from them, with citations. **External tools** let the model call something deterministic — a search index, a database, a calculator, an internal API — and read back the result. **LangChain** is one library among several that assembles these parts: retrievers, prompt templates, model calls, output parsers. The idea underneath all three is division of labour: the model interprets and writes; the surrounding system holds knowledge and performs actions.

## Deep expansion

### The concept

Split what a model "knows" into two kinds. **Parametric** knowledge lives in the weights, frozen when training ended: broad, fluent, undated, unauditable. **Non-parametric** knowledge lives outside — in your files, your database, your ticket system — and is current, permissioned and citable. Prompt engineering alone can only work on the second kind if you paste it in by hand. RAG industrialises the pasting.

The boundary that matters in a classroom is the one between RAG and simply pasting a long document. Paste a fifty-page PDF into a million-token window and you have done long-context prompting: no selection step, so no retrieval. Search a ten-thousand-page repository, select the five pages that matter, and inject only those: that is RAG. The selection step is the definition.

The second boundary is between RAG and a tool call. Retrieval fetches *text for the model to read*. A tool call returns *a result the model acts on* — a leave balance, a parcel status, a computed total. If the answer is a number that lives in a system of record, retrieval is the wrong instrument; ask the system.

### The sub-concepts

**The pipeline.** Ingest (parse, chunk, embed, index), then at query time: rewrite the query, retrieve a wide candidate set, rerank to a few, and assemble a prompt that says what the passages are, what to do with them, and what to do when they do not contain the answer.

**Retrieval is where it breaks.** Dense vector search misses exact identifiers — invoice numbers, clause references, NRIC formats, drug names — because meaning compresses away precision. Keyword search misses synonyms. Production systems run both and rerank, and when a grounded answer is wrong, the first question is not "which model" but "what did the retriever actually fetch".

**The grounded prompt has three clauses.** Answer only from the supplied context; cite the source id after each claim; if the context does not contain the answer, say so explicitly. Without the third clause the model fills the gap from its weights, fluently.

**Tools are described, not coded, into the prompt.** A function's name, description and argument schema are prompt text. Vague or overlapping descriptions are why a model calls the wrong tool or invents a missing argument.

**The ReAct loop.** For multi-step work the model alternates reasoning, action and observation: think, call, read, think again. That loop is what "agent" means, and its failures are loops, invented parameters, and losing the original goal after several observations.

**Frameworks are convenience, not capability.** A retrieval-augmented answer can be built in a few dozen lines of Python. LangChain and its relatives buy structure for multi-step flows, and cost a layer of indirection when something breaks. Teach the pipeline first.

### How it connects to the rest of the framework

Bullet 1 (`TSC3-Advanced-K1`) is the routing decision that sends you here. Bullet 2 (`K2`) is context manipulation done by machine rather than by hand, and Bullet 3 (`K3`) is the prompt assembly at the end of the pipeline. Bullet 7 (`K7`) is the contrast case — putting knowledge in the weights instead of the window. `TSC6` covers building the application; this bullet is the concept a prompt engineer needs in order to specify it.

### What is current as of November 2026

- **Long context changed the arithmetic, not the conclusion.** With the late-2026 frontier models (GPT-6 generation, Claude 5.5, Gemini 3.1 Pro, Gemini 4 Argon) holding very large windows, small bounded corpora can be handled by loading everything — the pattern behind source-grounded workspace products. But an enterprise corpus is not bounded, sending a million tokens per query is slow and expensive, and attention still decays in the middle. Retrieval selects what the long context reads.
- **Agentic retrieval is now the default shape.** Rather than a fixed retrieve-then-answer pipeline, the model is given search as a tool and decides when to search, rewrite the query, and search again. Better on multi-hop questions, harder to audit.
- **Tool protocols standardised.** Connecting a model to internal systems is now mostly configuration rather than bespoke integration, which moved the practical skill from plumbing to tool description quality.

### Common misconceptions

- *"Once we connect our documents, the AI has learned them."* Nothing is learned. Passages are copied into one prompt; the next call starts clean.
- *"A two-million-token window makes RAG obsolete."* It makes small-corpus chunking unnecessary. It does not make a 500-million-token repository fit, cheap, or well-attended.
- *"It cited a source, so the source says that."* Citations are generated text. The claim, the citation and the passage have to be checked against each other.
- *"Vector search is smarter than keyword search."* Different failure modes. Exact identifiers are the classic vector miss.
- *"The framework is the architecture."* Swap the library and the architecture is unchanged; get the chunking wrong and no library saves you.

## How a student should understand it

**Mental model:** an open-book exam with a research librarian sitting beside the candidate — she fetches three pages from fifty thousand files, and the candidate is told to answer only from those pages and write down which page each fact came from.

**Things they can do after this bullet:**
1. Explain the difference between what the model knows and what retrieval supplies.
2. Decide, for a given question, whether it needs retrieval, a tool call, or neither.
3. Write the grounded prompt: context block, citation rule, abstention clause.

**Misconceptions to kill:** that RAG trains the model; that citations verify themselves; that retrieval is a model problem.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The librarian and the open book.** The candidate is brilliant and has memorised the textbook. Your company policy changed last Tuesday, so you hand over the three relevant pages and forbid outside knowledge. Where it breaks: a librarian can be asked to fetch again if the pages are wrong; a fixed RAG pipeline will confidently use whatever it retrieved, which is why evaluation matters.

**The barcode scanner and the supermarket aisle.** Keyword search is a barcode scanner: type "Panadol" and it finds the exact box, and finds nothing if you type "headache medicine". Vector search is the store layout: painkillers are shelved together regardless of spelling. Hybrid search walks the aisle *and* scans the barcode. Where it breaks: a supermarket is organised once by a merchandiser; an embedding space is organised by a model you did not design and cannot inspect.

### Worked example with a real tool

```text
You are answering from ONLY the document below. If the answer is not in the
document, say "not in the document". Do not use outside knowledge.

<document>
Refunds are accepted within 14 days of purchase with proof of purchase.
</document>

Question: What is the refund window?
```

Answer: 14 days, cited to the document. Now change the question to "Can I return an item after 30 days?" and run it again: the abstention clause should produce "not in the document". Then delete that clause and re-run — the model reasons its way to a plausible policy. That contrast is the entire lesson about grounding, and it takes ninety seconds.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the model a question about a policy it cannot know; show it guess confidently.
2. **State the objective** — explain the pipeline, choose between retrieval and a tool, write a grounded prompt with an abstention clause.
3. **Recall prior learning** — the difference between memorising for an exam and being allowed to bring notes.
4. **Present the content** — parametric versus non-parametric; the pipeline; hybrid retrieval and reranking; tool calls; where frameworks fit.
5. **Guide** — run the refund prompt, then the abstention variant, then the same question with a tool that returns a live order record.
6. **Elicit performance** — give three tasks; learners decide retrieval, tool or neither, and sketch the pipeline for the retrieval case.
7. **Give feedback** — debrief the choices. The usual error is choosing retrieval for a live transactional fact.
8. **Transfer** — each learner writes the grounded prompt template their team would need for one real document set.

## What the framework doesn't mention but trainers need to know

- **Ingestion quality dominates.** A parsed PDF with scrambled two-column text and flattened tables produces a retrieval system that cannot be fixed by prompting. Layout-aware parsing is the highest-leverage step, and the least glamorous.
- **Five questions diagnose almost any bad grounded answer.** Is the fact in the source at all? Did the parser mangle it? Did chunking sever the exception from the rule? Did retrieval miss it? Was it in the prompt but ignored? Teach the order; it converts blame into a fix.
- **Access control is a reason to use RAG, not a detail.** Permissions have to be enforced as filters at retrieval time. A shared index without them answers questions the asker is not allowed to ask.
- **Stale documents outrank fresh ones.** An older, longer policy often scores higher than the brief memo that supersedes it. Version metadata and de-indexing are part of the design.
- **Counting and listing are not retrieval questions.** "How many contracts expire this quarter" needs a query over structured data, not five similar paragraphs.

## Watch out

- **Do not let a citation pass unverified in front of the room.** Click it, read the passage, compare the claim. The habit is the lesson.
- **Do not build RAG for a document that fits in the prompt.** It adds failure modes for no gain.
- **Do not teach the library before the pipeline.** Learners who start with a framework learn configuration and never learn retrieval.
- **The stale claim to retire:** "the model searched the internet." Unless something explicitly fetched, it did not search — it predicted.
