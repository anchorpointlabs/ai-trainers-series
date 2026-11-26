---
id: 06.01.B.K4
tsc: 6
level: Basic
code: K4
title: "The developer stack: which tool earns its place at each layer"
as_at: 2026-11-26
review_by: 2027-02-25
---

# The developer stack: which tool earns its place at each layer

> **TSC #6 Generative AI Application Development and Deployment · Basic · Knowledge K4**


> **Framework text (verbatim):** "Developer tools and frameworks that accelerate development of generative AI applications."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Knowledge · Bullet 4 of 11

**One-line version:** A framework is a shortcut through work you would otherwise repeat — and every shortcut is a road you can no longer take.

## What it is

The toolchain for a generative AI application has recognisable layers: somewhere to call the model, something to orchestrate the steps, somewhere to store and search knowledge, a surface for the user, and something to watch it all. Knowing the layers matters more than knowing the product names.

## Deep expansion

### The concept

A generative AI application is rarely one call. It takes input, assembles context, calls the model, validates the output, logs what happened and shows the user something. Each of those is a small engineering problem with an off-the-shelf answer.

Frameworks exist because thousands of teams solved the same five problems in the same order. Adopting one buys speed and shared vocabulary; it costs a dependency, an abstraction you did not write, and an upgrade path you do not control. That trade is the whole knowledge item. A Basic learner does not need to master a framework — they need to recognise the layer they are standing on and know what lies beneath.

### The sub-concepts

**The layers.** Model access (vendor SDKs, an OpenAI-compatible endpoint, or plain `requests`); orchestration (LangChain, LlamaIndex, LangGraph, Semantic Kernel, agent SDKs); knowledge (pgvector, Chroma, Qdrant, Pinecone); interface (Streamlit, Gradio, Chainlit, a web framework); observability (Langfuse, LangSmith, Arize Phoenix); serving (vLLM, TGI, Ollama, llama.cpp); build environment (VS Code with Copilot, Cursor, Claude Code, Jupyter).

**Abstractions leak.** When the framework handles your case it saves days. When it does not, you debug someone else's code with no map. Understand the plain call before adopting the wrapper.

**The two-week rule.** If a framework takes longer to learn than the boring version takes to write, use the boring version. For one prompt and one API call, `requests` is proportionate, not amateur.

**Scaffolding is not architecture.** A tool that generates an app from a paragraph produces routes, screens, a database and a working happy path. It is real code you now own, including the parts you did not read.

### How it connects to the rest of the framework

`TSC6-Basic-K2` covers the no-code end of the same ladder; `TSC6-Basic-A1` is where the model-call layer gets configured properly; `TSC6-Basic-K6` decides whether any of it will run on the target machine. `TSC6-Intermediate-K5` (pipeline design) and `TSC6-Advanced-A2` (serving with TGI or vLLM) are the same layers at professional depth.

### What is current as of November 2026

- **The agent SDK consolidated.** Orchestration thinned into a few agent-first libraries; the 2023-era "chain everything" style is now considered over-engineering.
- **MCP became the connective tissue.** The Model Context Protocol — a standard way for a model to reach tools and data — is supported across the major assistants and IDEs, so a learner can attach a database without writing glue.
- **The build environment became an agent.** Claude Code, Codex and Cursor-class tools now write, run and debug alongside the developer. Knowing the tools means less syntax recall and more specification and review.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"More frameworks means more advanced."* Usually more surface area to maintain. The best stacks are short.
- *"The framework is the skill."* Frameworks turn over quickly. Retrieval, prompting and evaluation do not.
- *"Using an SDK locks me in forever."* A vendor SDK does; a generic client against an OpenAI-compatible endpoint does not. Know which you picked.

## How a student should understand it

**Mental model:** a kitchen. The framework is the prepped mise en place — diced, portioned, ready. It speeds up service; it does not cook the dish, and it does not tell you the fish is off.

**Three things they can do after this bullet:**
1. Name the six layers and place any tool they hear about on the right one.
2. Choose a proportionate stack for a small internal tool and justify each choice in a sentence.
3. Recognise when a framework costs more than it saves.

**Misconceptions to kill:** that tool count equals sophistication, that the framework is the durable knowledge, and that generated code is maintenance-free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT versus your own car.** The MRT is fast, cheap and predictable on the routes it serves. It will not drop you at your door, and when it fails you are on a platform with no alternative. Use frameworks for the journeys thousands of people take, and keep a plan for the last mile. Where it breaks: unlike the MRT, you can read the framework's source and patch it — which is exactly why teams over-invest.

**The zi char stall's prep bench.** Everything chopped and portioned before service. The wok still does the cooking, and the prep does not fix a bad ingredient. A framework is prep; your prompt and data are the ingredient.

### Worked example with a real tool

Put the room in a real decision. Type:

```
We need a policy Q&A bot for 200 staff. Documents live in a shared drive.
Answers must cite the clause. Budget is small, nobody on the team is a
full-time developer, and IT requires an audit log.

Recommend a stack, one choice per layer: model access, orchestration,
knowledge store, interface, observability. Give the simplest option that
meets the requirement and one sentence on why. Then tell me which layer I
should NOT build myself.
```

What to point at afterwards: the stack is reasonable and confidently wrong about at least one product detail — a renamed library, a feature that moved, a limit that changed. Place each recommendation on the layer diagram, then verify the specific claim against the vendor's own documentation before quoting it to IT. The verification habit is the exercise; the stack is just the vehicle.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two screenshots: a 30-line script that answers questions from a PDF, and a 900-line framework project that does the same. Ask which they would maintain.
2. **State the objective** — by the end you can place any tool on the six-layer map and choose a stack proportionate to the problem.
3. **Recall prior learning** — the RAG loop from K1; the no-code ladder from K2.
4. **Present the content** — the layer table, then the honesty test: what does this tool do that ten lines cannot?
5. **Guide** — choose the stack for one real use case together, arguing each layer down to the simplest option.
6. **Elicit performance** — groups fill in the six layers for their own use case, one sentence of justification each.
7. **Give feedback** — project two stacks and ask which layer each group over-built. It is always orchestration.
8. **Transfer** — each learner writes the stack they would propose at work, and the one layer they would refuse to own.

## What the framework doesn't mention but trainers need to know

- **Observability is the layer beginners skip and regret.** Without a trace you cannot answer "why did it say that on Tuesday". Ten minutes of logging beats a week of guessing.
- **Version pinning is a tool decision.** A framework that upgrades itself can break a working app overnight. Pin versions and log them.
- **The generated code is yours.** Licence, security and quality transfer the moment it lands in your repository.

## Watch out

- **Do not demo a stack you cannot debug live.** The room learns more from a competent traceback than from a polished build.
- **Do not let "there's a framework for that" end the conversation.** Ask what it does and what it costs to keep.
- **The stale claim to retire:** "you need LangChain to build an AI app." Most production apps in 2026 call the API directly and orchestrate in ordinary code.
