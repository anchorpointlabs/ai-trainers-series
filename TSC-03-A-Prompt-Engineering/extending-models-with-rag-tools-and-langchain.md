---
id: 03.03.A.K5
tsc: 3
level: Advanced
code: K5
title: Extending models with RAG, tools, and LangChain
---

# Extending models with RAG, tools, and LangChain

> **TSC #3 Prompt Engineering · Advanced · Knowledge K5**

**IMDA requirement:** Techniques that extend capabilities of generative AI models (e.g., Retrieval Augmented Generation (RAG), external tools and libraries such as Langchain).

**What it means:** A model only knows its training data. **RAG** fetches your own documents and feeds them in so the model answers from them (and cites them). **External tools** let it call APIs, search, or run code. **LangChain** is a library that wires these pieces together. All three share one idea: the model stays the language engine; you supply the knowledge and the hands.

**The learner must be able to:**
- Explain the difference between what the model knows and what RAG supplies.
- Describe when to use RAG vs. a tool call.
- Sketch the pipeline: query → retrieve → inject → generate.

**Lesson Plan Ideas:**
1. Ask a question the model cannot answer (a private policy), show it guessing, then show the RAG answer.
2. Draw the RAG pipeline on the board.
3. Learners identify which of three tasks needs RAG, which needs a tool, which needs neither.
4. Debrief the choices.

**Exercise (with the exact prompt):**
```text
You are answering from ONLY the document below. If the answer is not in the document, say 'not in the document'. Do not use outside knowledge.

<document>

Question: What is the refund window?
```
Expected: the model answers from the document and says 'not in the document' when the fact is absent.

**Common mistakes:**
- Thinking the model 'looked it up' on its own — retrieval must be built.
- Trusting the answer because it cites a source, without checking the source says that.
- Using RAG when the fact is already in the model's training data.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf
- [rag-and-retrieval.md](../core-knowledge/rag-and-retrieval.md)

