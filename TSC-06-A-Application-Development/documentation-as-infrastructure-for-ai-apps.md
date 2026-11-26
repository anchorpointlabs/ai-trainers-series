---
id: 06.03.A.A7
tsc: 6
level: Advanced
code: A7
title: "Documentation as infrastructure: the knowledge base that keeps an AI app alive"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Documentation as infrastructure: the knowledge base that keeps an AI app alive

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A7**


> **Framework text (verbatim):** "Document and update knowledge bases for AI tools and applications."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 12 of 12

**One-line version:** In an AI application the documentation is load-bearing — it is the corpus the model answers from, the runbook the on-call engineer follows, and the record that proves what the system was told to do.

## What it is

This is the ability to build and maintain the written layer of an AI application: architecture decisions, prompt and model versions, evaluation results, runbooks, known-failure libraries, and — crucially — the source corpus the application retrieves from. It includes the discipline that keeps all of it current: an owner per document, a version, a review date and a changelog.

## Deep expansion

### The concept

"Knowledge base" means two things in this domain, and the Advanced skill is recognising that they obey the same rules.

The first is **documentation for people**: what the system does, why it was built that way, how to operate it, what has already failed. The second is **the corpus the application retrieves from**: the policies, manuals, price lists and FAQs that the model quotes. The first determines whether the system can be maintained. The second determines whether its answers are correct. Both rot in the same way — silently, from the edges — and both are fixed by the same habits: a single source of truth, an owner, a version, and a date.

There is a third audience now. Agents read documentation: tool descriptions, API schemas and instruction files are written text that a model interprets at runtime. A vague tool description is not a style problem; it is a behaviour problem. Documentation quality has become functional quality.

### The sub-concepts

**Architecture decision records.** One page per significant choice: the decision, the alternatives rejected, the reason, the date. "Why did we choose retrieval over fine-tuning" is answered in thirty seconds, three years later, and it is the document auditors and successors ask for.

**The prompt library with rationale.** Every production prompt, versioned, with the failure it was written to fix and the model it was tested on. Prompts edited in a chat window and pasted into code are the most common cause of irreproducible behaviour.

**Evaluation baselines.** The test set, the scoring method, the last result, and the date. Without a stored baseline, every future change is argued from memory.

**Runbooks that were actually run.** Not "how to restart the service" written from imagination, but the steps someone followed during an incident, with the surprises included.

**A known-failure library.** Each incident becomes an entry: symptom, cause, detection, fix, and the check that now catches it. This is the highest-value document in the set and the one nobody assigns.

**The corpus inventory.** Which sources feed retrieval, who owns each, how often it changes, how it is ingested, and what the freshness guarantee is. Answer quality is bounded by this table.

**Review dates and ownership.** Every entry has a name and a date. Documents without an owner are archaeology.

**Agent-facing text.** Tool descriptions, parameter docs and instruction files written for a model to read: precise, unambiguous, and tested by observing whether the model uses the tool correctly.

### How it connects to the rest of the framework

`TSC6-Advanced-A6` produces the tools whose behaviour must be written down; `TSC6-Advanced-A3` produces guardrails whose policies and thresholds belong in the record. `TSC6-Advanced-K3` governs the retrieval corpus that this ability maintains, and `TSC6-Intermediate-K3`/`A2` are the deployment context. `TSC-06-Basic-K5` is the learner-level habit of reading the vendor's documentation; this is the professional habit of writing your own.

### What is current as of November 2026

- **Agent-readable documentation became a design surface.** Tool descriptions in the MCP style are now interfaces a model interprets, and teams are discovering that rewriting a description changes behaviour more reliably than rewriting a prompt.
- **Documentation hygiene is answer quality.** In retrieval-based applications, duplicated, outdated or contradictory source documents produce contradictory answers, so corpus curation is now an engineering task with an owner.
- **Docs-as-code is normal in engineering teams**, with review, version history and CI checks for links and schema validity — which makes the "update" half of this bullet achievable rather than aspirational.
- **AI-assisted drafting is widely used and requires verification.** Generated documentation is fluent and can be confidently wrong about your system; the model supplies structure, the team supplies facts.
- **Retention and access rules tightened.** Documentation about AI systems increasingly contains prompt text, evaluation data and model identifiers, which brings classification and access control with it.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Documentation is for auditors."* Its first user is the engineer on call at 3am, and the second is the person who replaces you.
- *"We will write it at the end."* The end never arrives, and the reasoning is gone by then.
- *"The wiki is the knowledge base."* A wiki without owners, dates and a single source of truth is a rumour archive.
- *"The model can answer questions about our own system."* It cannot; it will invent a plausible architecture. Documentation is how the system knows itself.

## How a student should understand it

**Mental model:** the family recipe book. A dish that lives only in one cook's hands dies with that cook; written down with quantities and heat, it survives and improves.

**Three things they can do after this bullet:**
1. Produce the minimum document set for an AI application and assign an owner and review date to each.
2. Write an architecture decision record with the rejected alternatives included.
3. Audit a retrieval corpus for duplication, staleness and contradictions, and state the freshness guarantee.

**Misconceptions to kill:** that documentation is paperwork, that it can wait until the end, and that the model knows your system.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The family recipe book.** Grandma's sambal is legendary and unrecorded; when she stops cooking, it is gone. The stall that writes it down — grams, heat, timing — can train a successor and survive its founder. Where it breaks: a recipe is stable for decades, while AI documentation has a review cycle measured in months, so the book needs dates, not just pages.

**The lift maintenance log.** The log is what makes the lift safe and the contractor accountable: every service, every fault, signed. Nobody reads it until something goes wrong — and then it is the only thing that matters. An AI application's records are the same artefact.

### Worked example with a real tool

Ask for the skeleton, then fill it with reality:

```
Here is our internal AI assistant: retrieval over 40 policy documents,
a frontier model, three guardrails, two prompt templates, deployed on a
managed endpoint.

Produce a documentation set:
1. a one-page architecture record with the decisions and the alternatives
   we rejected,
2. a runbook for five likely failure modes,
3. a prompt changelog table with a "why" column,
4. the review cadence and owner for each document,
5. a corpus inventory table with freshness for each source.

Ask me for anything you need before you start.
```

What to point at afterwards: the model will invent your failure modes and your policy owners. That is fine — the skeleton is the value, and the blanks are the exercise. Then look at point five: the corpus inventory is the document that most improves answer quality, and it is the one nobody has. If the room can fill it for their own corpus, they have done the bullet.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show an incident where the fix took four hours because nobody knew which prompt was live.
2. **State the objective** — you will produce a minimum document set with owners and dates, and audit one corpus.
3. **Recall prior learning** — they have built and debugged the system; now they make it survivable.
4. **Present the content** — the two knowledge bases, the document set, the update discipline.
5. **Guide** — write one architecture decision record together, including the rejected option.
6. **Elicit performance** — teams draft their document set and audit ten documents for staleness.
7. **Give feedback** — reject any document without an owner; challenge "the wiki" as a source of truth.
8. **Transfer** — the set is committed with the code, and the review date is in the team calendar.

## What the framework doesn't mention but trainers need to know

- **Write the document you would want at 3am**, not the one that satisfies a template. Symptom-first, then cause, then fix.
- **Postmortems must produce a document change.** If an incident adds no entry to the known-failure library, the next team repeats it.
- **Deprecate loudly.** Old documents that stay online are worse than missing ones, because retrieval will quote them.
- **Test the runbook in a drill.** A runbook nobody has executed is a hypothesis.
- **Documentation is a security surface.** Prompt text and evaluation data can leak system behaviour; classify and restrict.

## Watch out

- **Do not demo generated documentation without auditing it.** The room will copy the pattern and ship a confident fiction about their own system.
- **Do not let the exercise become a template-filling contest.** The test is whether a stranger could operate the system from the documents.
- **Do not skip the corpus side.** Most trainers document the code and forget that the answers come from documents nobody curates.
- **The stale claim to retire:** "documentation is the last step." In November 2026, when agents read your descriptions and retrieval quotes your sources, documentation is part of the runtime.
