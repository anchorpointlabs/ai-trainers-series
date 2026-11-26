---
id: 06.03.A.A4
tsc: 6
level: Advanced
code: A4
title: "Choosing between context augmentation techniques: the trade-off table"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Choosing between context augmentation techniques: the trade-off table

> **TSC #6 Generative AI Application Development and Deployment · Advanced · Ability A4**


> **Framework text (verbatim):** "Articulate trade-offs from using different context augmentation techniques."
>
> **TSC #6** Generative AI Application Development and Deployment · **Advanced** · Ability · Bullet 9 of 12

**One-line version:** There is no best augmentation technique — there is a defensible choice for a stated query mix, change rate and audit requirement, written down where a sceptic can attack it.

## What it is

This is the ability to compare augmentation approaches and defend the choice: fine-tuning, pasting the whole corpus, naive vector retrieval, hybrid search with a reranker, graph traversal, agentic retrieval loops, or plain parametric knowledge. Articulating the trade-off means producing the table — options against criteria — and then a recommendation with a named cost, a named risk and the condition that would reverse it.

## Deep expansion

### The concept

Every augmentation technique buys something and pays for it. The mistake learners make is asking "which is most accurate", because accuracy is a property of the question type, and the question type is a distribution, not a single example.

The decision is driven by four properties of the setting:

- **Query mix.** Factual lookup, comparison, multi-hop reasoning, summarisation across many documents, or numeric aggregation. Similarity search fails at the last two in ways no amount of tuning fixes.
- **Change rate.** A policy that changes monthly makes baked-in knowledge wrong by design. A stable technical standard tolerates it.
- **Audit requirement.** If someone must see the clause behind an answer, you need retrieval with source identifiers, and fine-tuning is disqualified regardless of quality.
- **Volume and latency.** The same technique can be right at ten queries a day and wrong at a hundred thousand.

The Advanced skill is writing that as a decision memo a non-specialist can follow — with the criteria named, the numbers labelled as estimates, and the reversal condition stated. A trade-off you cannot articulate is a preference.

### The sub-concepts

**Accuracy is question-shaped.** Retrieval wins on lookup and citation; long-context paste wins on "summarise this whole document"; graphs win on multi-hop relationships; fine-tuning wins on style, format and narrow behaviour. None of them wins everything, and a benchmark is not your traffic.

**Freshness is a maintenance cost.** Retrieval updates itself every time the index is refreshed. Fine-tuning requires a new training run. Pasting requires nothing but pays per query. Choose the maintenance model you can actually staff.

**Latency compounds by hop.** Rewrite, search, rerank, generate: each adds. Agentic loops multiply it. State the budget before the design, or the design will set the budget.

**Cost per query, not cost per token.** A cheap model with a huge pasted context can cost more than a better model reading four passages. Do the arithmetic for a thousand queries, not one.

**Auditability is a feature, not paperwork.** Citations, retained retrieval snapshots and versioned indices are what let you answer "why did it say that" three months later.

**Data exposure changes the risk class.** Pasting a customer record into a third-party model is a different decision from retrieving an internal vector store you control. That belongs in the table.

**Failure modes differ in kind.** Retrieval fails by missing or by returning the wrong passage — visible. Fine-tuning fails by confidently blending stale facts — quiet. Graphs fail by schema drift. Match the failure you can detect to the risk you can carry.

### How it connects to the rest of the framework

`TSC6-Advanced-K3` is the technique knowledge; this ability is the judgement applied to it, which is why they are separate bullets. `TSC6-Advanced-A1` consumes the decision — the augmentation choice is one line of a multi-model architecture. `TSC6-Advanced-K1` supplies the cost side of the table, and `TSC6-Advanced-A2` supplies latency reality. `TSC4` covers the fine-tune-versus-prompt decision from the model-selection angle.

### What is current as of November 2026

- **Long context made "paste it all" a legitimate row in the table** for medium corpora with low query volume and high freshness sensitivity — a row that did not exist three years ago.
- **Hybrid search plus a reranker is the default recommendation**, and being able to say why it is the default — and when it is not — is now the differentiator.
- **Agentic retrieval is chosen for multi-hop questions** and bounded with a step limit and a cost ceiling, because an unbounded loop is an unbounded bill.
- **Graph retrieval is justified by question shape**, typically compliance, supplier and case-history work, not by ambition.
- **Managed retrieval services hide the machinery**, which makes the trade-off conversation easier to have and easier to get wrong: the defaults are invisible.

### Common misconceptions

- *"Hybrid plus reranker is best practice for everyone."* It is the best default for lookup over changing documents. For a stable manual and low volume, whole-document paste is simpler and better.
- *"Cheaper is always better."* A technique that fails the audit requirement is infinitely expensive when the auditor arrives.
- *"Latency is an infrastructure problem."* The augmentation design sets the floor; no server tuning recovers three sequential model calls.
- *"We will decide later."* Deferring the choice usually means one gets built by accident and defended afterwards.

## How a student should understand it

**Mental model:** choosing how to get to work. MRT, bus, Grab, own car — each is best for a different trip, and "best" depends on time, cost, predictability and who is paying. Nobody argues that one mode is universally superior.

**Three things they can do after this bullet:**
1. Produce a trade-off table for a stated case with criteria, estimates and a recommendation.
2. Name the condition under which their recommendation would be wrong.
3. Defend a choice to a non-technical stakeholder in two minutes without jargon.

**Misconceptions to kill:** that one technique is universally best, that cost dominates, and that the decision can be deferred without consequence.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**MRT, bus, Grab, car.** The MRT is cheap, fast and predictable until it is not — a breakdown is rare and total. Grab is flexible, surge-priced, and available at 2am. The car is fastest until you need parking. That is retrieval versus long-context paste versus agentic loops: different failure profiles at different costs. Where it breaks: transport options are stable for years, while augmentation techniques change every quarter, so the table needs a review date.

**The renovation quote.** Cheap, fast, good — pick two, and the contractor who says all three is lying. Any augmentation design that claims best accuracy, lowest cost and least maintenance is the same lie in technical language.

### Worked example with a real tool

Make the assistant produce the memo, then audit it:

```
Compare four ways to answer questions from our 900-page HR policy:
(1) fine-tune a model on the policy, (2) paste the whole document on
every query, (3) vector retrieval of the top five passages,
(4) hybrid search with a reranker.

Score each on accuracy, latency, cost per 1,000 queries, build effort,
maintenance, auditability and data exposure. Label any number as an
estimate. Then recommend one, and state what would change your mind:
the policy changes monthly, and an auditor must see the source clause.
```

What to point at afterwards: the assistant will produce a clean table and will invent prices unless told otherwise — which is why "label any number as an estimate" is in the prompt, and why the room should replace them with their own. Then point at the reasoning: monthly change plus a clause requirement eliminates fine-tuning, and the pasted-document option loses on cost at volume. The memo, not the table, is the deliverable.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two teams, same corpus, opposite choices, both defended confidently. Ask who is right.
2. **State the objective** — you will write a one-page decision memo with a reversal condition.
3. **Recall prior learning** — they know the techniques; now they must choose under constraints.
4. **Present the content** — the four setting properties and the criteria list.
5. **Guide** — fill the table for the HR policy case together.
6. **Elicit performance** — teams fill it for their own corpus and write the recommendation.
7. **Give feedback** — attack each memo as a sceptical finance lead: "why not the cheapest", "what if the policy changes weekly".
8. **Transfer** — they bring the memo to their next architecture review instead of a slide.

## What the framework doesn't mention but trainers need to know

- **The table is political.** Cost sits with one sponsor, accuracy with another, risk with a third. Naming the owners turns a technical memo into a decision.
- **Estimates must be labelled.** An invented cost table is worse than no table, because it will be quoted in a budget meeting.
- **Hybrid designs are the honest answer more often than pure ones.** Most production systems use paste for small stable corpora and retrieval for the rest.
- **Review dates belong on the memo.** Long context changed this decision once already; assume it will again.
- **The cheapest failure is a wrong answer nobody notices.** Weight detection cost in the table, not just prevention.

## Watch out

- **Do not let the room vote on a technique by preference.** Force criteria and a reversal condition.
- **Do not present your own preferred stack as the answer.** The trainer's job is the method, and the class will have cases where you are wrong.
- **Do not accept a memo without a cost figure per thousand queries**, even as a labelled estimate; the absence is the tell that nobody owns the budget.
- **The stale claim to retire:** "RAG is always better than fine-tuning." In November 2026 the honest sentence is "they solve different problems, and the audit requirement usually decides".
