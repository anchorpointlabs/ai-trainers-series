# Agentic AI Platforms — Knowledge Distillation

> **Source model:** Gemini 4 Argon (`gemini-4-argon`) via i10x
> **Extracted:** 2026-11-26 (distillation run)
> **Status:** RAW distillation — exhaustive extraction, not yet cut into entry-template format.

---

# 1. DEFINITION AND BOUNDARIES

## What is an Agentic AI Platform / Framework?
An **agentic AI platform or framework** is a software system that wraps one or more foundational models (LLMs or multimodal models) inside a runtime execution loop capable of **autonomous goal pursuit**. Unlike static software, an agentic system dynamically decides its own control flow at runtime. 

To qualify as an agentic AI platform or framework, a system must possess five core properties:
1. **Dynamic Control Flow (The Loop):** The model, not a pre-written `if/else` script, decides what step to take next, how many steps to take, and when the goal is satisfied.
2. **Environment Coupling (Tools/Actuators):** The system can read from and write to external state (file systems, terminals, browsers, databases, APIs).
3. **State and Working Memory Management:** The system persists intermediate results, tool outputs, errors, and plans across multiple iterations of execution.
4. **Self-Correction / Reflection:** When an action fails (e.g., a compiler error, an HTTP 400 response, a missing UI element), the error is fed back into the model's context so it can alter its approach and retry without human intervention.
5. **Lifecycle & Governance Harness:** Built-in infrastructure for execution sandboxing, human-in-the-loop (HITL) approval gates, state checkpointing, and tracing.

* **Agentic Framework (e.g., LangGraph, CrewAI, OpenAI Agents SDK):** A developer library or SDK used by engineers to *construct* custom agent loops, state graphs, and multi-agent workflows in code.
* **Agentic Platform / Product (e.g., Claude Code, Devin, Manus, Operator):** A packaged, ready-to-run application or hosted runtime that comes pre-wired with an agent loop, system prompts, sandboxes, and built-in tools (bash, browser, editor) for end-users or developers.

---

## Exact Boundaries: What It Is vs. What It Is Not

### (a) Agentic Platform vs. Raw LLM Chat (e.g., standard ChatGPT, Claude.ai web chat without tools)
* **Control Flow:** A raw LLM chat is **single-turn request/response** (`User Prompt -> Model -> Text Output -> Stop`). An agentic platform is **multi-turn autonomous execution** (`User Goal -> [Think -> Act -> Observe -> Think -> Act]... -> Final Output`).
* **Side Effects:** A raw LLM chat cannot change the external world; it only emits tokens for a human to read and copy-paste. An agentic platform executes actions with real side effects (editing files, running shell commands, clicking buttons, charging credit cards).
* **Error Handling:** If a raw LLM generates buggy code, the human must copy it, run it, copy the stack trace, paste it back, and ask for a fix. An agent runs the code itself, reads `stderr`, and patches the code automatically inside the same turn.

### (b) Agentic Platform vs. an MCP Server (Model Context Protocol)
* **Role in the Stack:** An **MCP Server** has **zero intelligence, zero reasoning, and zero autonomy**. It is a standardized peripheral adapter (like a USB driver) that exposes tools, resources (data), and prompt templates over a standard JSON-RPC protocol (`stdio` or HTTP/SSE).
* **Relationship:** The **Agentic Platform** (such as Claude Code or Cursor) acts as the **MCP Host / Client**. The agent contains the brain (LLM + execution loop). When the agent decides it needs to query a PostgreSQL database or create a Jira ticket, it sends a structured request to the MCP Server. The MCP Server executes the deterministic query and returns raw data to the agent. An MCP server never decides *when* or *why* to run a tool.

### (c) Agentic Platform vs. No-Code Automation (e.g., Zapier, Make, standard n8n workflows)
* **Deterministic DAG vs. Probabilistic Loop:** Traditional Zapier or n8n workflows are **Directed Acyclic Graphs (DAGs)** defined at design time (`Trigger A -> Step B -> If X then C else D`). Even if Step B calls an OpenAI node to summarize an email, the *routing* is hardcoded by the human builder.
* **Exception Handling:** If an unexpected API format or edge case occurs in Zapier, the workflow crashes and throws an error alert. In an agentic system, the model inspects the unexpected payload, decides to query a schema tool or try an alternative tool, and adapts on the fly.
* *Note on Hybridization:* Modern n8n and Zapier now offer "AI Agent Nodes" inside their workflows. In that architecture, the outer n8n canvas remains a deterministic pipeline, while the specific Agent Node spins up an autonomous tool-calling sub-loop before handing control back to the deterministic pipeline.

### (d) Agentic Platform vs. Code Assistant / Autocomplete (e.g., GitHub Copilot Tab-Autocomplete, Supermaven)
* **Latency & Scope:** Code autocomplete operates synchronously at the cursor position within a `<200ms` latency budget, predicting the next 1 to 20 lines of text based on open tabs (Fill-In-the-Middle / FIM).
* **Loop vs. Prediction:** Autocomplete has no agent loop, cannot run terminal commands, cannot read compiler errors from a test suite, and cannot coordinate changes across 15 files simultaneously.
* **Agentic Coding (e.g., Cursor Agent Mode, Claude Code, Devin):** Operates asynchronously over seconds to hours. Given a prompt like *"Migrate authentication from JWT to session cookies and make sure all tests pass"*, an agent searches the codebase (`grep`/`glob`), edits 12 files, runs `npm test`, reads the 3 failing test outputs, fixes the bugs, and commits the branch.

---

# 2. THE COMPLETE LANDSCAPE

## 1. Anthropic: Claude Code, Claude Agent SDK, and Agentic Tooling

### (a) Claude Code
* **What it actually is:** Anthropic's official agentic coding tool that lives directly in the developer's local terminal (CLI), with integrations into VS Code, JetBrains IDEs, and GitHub Actions.
* **How it works:** Runs as a local Node.js/TypeScript client process on the user's machine. It connects directly to Anthropic's API (primarily Claude 3.7 Sonnet and Claude 4 Opus/Sonnet models with Extended Thinking). Instead of relying on fragile RAG vector embeddings of a codebase, it uses **agentic search**—executing native file system tools (`Glob`, `Grep`, file reads, directory listings) and `Bash` commands directly against the local workspace. It reads `CLAUDE.md` files in the repository root/subdirectories as persistent project memory and rules.
* **Capabilities:**
  * Full repository exploration, multi-file editing, git operations (branching, committing, resolving merge conflicts, opening PRs via `gh` CLI).
  * Executes shell commands, runs test suites, reads logs, and debugs failing builds autonomously.
  * Native **Subagent spawning** (`Task` tool): can spin up isolated child agents with separate context windows to do parallel research or deep file analysis without polluting the main agent's context window.
  * Full **MCP Client** support: connects to local or remote MCP servers (e.g., Sentry, Postgres, Linear, Slack).
  * Headless mode (`claude -p "..."`) for running inside CI/CD pipelines and automated scripts.
* **Real Limits:**
  * **Token burn rate:** Because it reads full files and runs multi-step grep/bash loops without vector truncation, complex sessions consume massive input/output tokens rapidly.
  * **Context compaction loss:** At ~95% context capacity, it auto-compacts (summarizes) history, which can drop exact line numbers or subtle architectural constraints discussed 30 turns earlier.
  * **Local environment risk:** Unless run inside a Docker container, any `Bash` command approved by the user (or run in `--dangerously-skip-permissions` mode) executes with the user's local OS privileges.

### (b) Claude Agent SDK (formerly Claude Code SDK)
* **What it actually is:** The programmatic TypeScript and Python SDK (`@anthropic-ai/claude-code` / `claude-agent-sdk`) that exposes the exact harness powering Claude Code so developers can build custom domain agents (beyond coding, such as SRE agents, financial analysis agents, legal review agents).
* **How it works:** Wraps the raw Anthropic Messages API with a production-ready agent loop, built-in file/bash tools, context compaction management, permission callbacks, custom MCP server registration, and session persistence.
* **Capabilities:** Allows engineers to embed Claude's agentic loop into backend services, custom UIs, or automated worker queues with strict programmatic tool-use callbacks (`canUseTool`), streaming intermediate thought/tool events, and structured JSON output enforcement.
* **Real Limits:** Locked strictly to Anthropic Claude models; relies on having a POSIX-like shell/filesystem environment if built-in bash/file tools are enabled.

### (c) Anthropic's Foundational Agentic Tooling (Computer Use, MCP, Extended Thinking)
* **Computer Use API:** Anthropic's native capability allowing Claude to interact with an arbitrary desktop GUI environment. It takes screenshots of a virtual display (`X11`/VNC container) and outputs pixel coordinates (`mouse_move`, `left_click`, `type`, `key`). *Limits:* Slow (2–5 seconds per click cycle), high token cost due to continuous image ingestion, fragile against high-DPI scaling or rapid UI animations.
* **Model Context Protocol (MCP):** Open-source protocol created by Anthropic (now an industry standard adopted by OpenAI, Google, Cursor, Microsoft) standardizing how agents connect to data sources and tools.
* **Interleaved / Extended Thinking:** Allows Claude models to emit private reasoning blocks *between* tool calls, enabling the model to re-evaluate a plan after seeing an unexpected tool output.

---

## 2. OpenAI: Codex, Operator, and OpenAI Agents SDK

### (a) OpenAI Codex (CLI & ChatGPT Cloud Coding Agent)
*(Note for Trainers: Do not confuse the legacy 2021 `code-davinci-002` model with the modern 2025 agentic products named **Codex CLI** and **Codex Cloud Agent**).*
* **What it actually is:** OpenAI's two-pronged software engineering agent suite:
  1. **Codex CLI (`@openai/codex`):** An open-source, lightweight terminal coding agent (similar to Claude Code) that runs locally on macOS/Linux.
  2. **Codex Cloud Agent (inside ChatGPT Pro/Team/Enterprise):** An asynchronous cloud software engineering agent powered by `codex-1` (a version of OpenAI's `o3` reasoning model specifically reinforcement-learned on real-world software engineering tasks and PR generation).
* **How it works:**
  * *Codex CLI:* Runs locally in the terminal, using OpenAI's Responses API (`o3`, `o4-mini`, `gpt-4.1`) paired with OS-level sandboxing (Apple `sandbox-exec` / Seatbelt on macOS, Docker/iptables on Linux) to execute shell commands and patch files safely.
  * *Codex Cloud:* Connects to a user's GitHub repositories, boots a dedicated isolated cloud container preloaded with the repo, runs in the background for 1 to 30 minutes writing code and running linters/tests, and presents a verifiable diff and PR.
* **Capabilities:** Multi-task parallel execution in the cloud (you can dispatch 10 bug fixes simultaneously across 10 isolated containers); verifiable execution citations (links every code change to terminal test logs); reads `AGENTS.md` files (OpenAI's equivalent to `CLAUDE.md`) for repo instructions.
* **Real Limits:** Cloud containers in Codex Cloud have restricted/disabled outbound internet access during execution for security, meaning the agent cannot easily `npm install` or `pip install` brand-new dependencies mid-run unless pre-configured in the environment setup script.

### (b) OpenAI Operator (and Computer-Using Agent / CUA)
* **What it actually is:** OpenAI's hosted consumer and prosumer web-browsing agent, powered by the **CUA (Computer-Using Agent)** model (`computer-use-preview` in the API), now integrated directly into ChatGPT as **ChatGPT Agent / Operator**.
* **How it works:** Spins up a remote headless Chromium browser in OpenAI's cloud. Rather than relying on brittle DOM scraping or site-specific APIs, CUA processes raw screenshots of the browser viewport using vision combined with reinforcement-learned chain-of-thought reasoning, and emits virtual mouse and keyboard actions.
* **Capabilities:** Can navigate complex, JavaScript-heavy websites, fill out multi-page forms, book travel, order groceries, manipulate spreadsheets in web apps, and handle pop-ups. Includes a **"Takeover Mode"** where the agent pauses and yields control of the remote browser window to the human user whenever login credentials, 2FA codes, CAPTCHAs, or payment confirmations are required.
* **Real Limits:**
  * Blocked by aggressive anti-bot WAFs (Cloudflare Turnstile, DataDome, Akamai) that detect datacenter IP addresses.
  * Cannot access local intranet web apps behind a corporate VPN (because the browser runs in OpenAI's cloud, not on the user's machine).
  * Slow execution compared to API integrations (a 10-step web checkout takes 1–3 minutes).

### (c) OpenAI Agents SDK (Successor to Swarm)
* **What it actually is:** OpenAI's official, lightweight, open-source Python and TypeScript framework (`openai-agents`) for building multi-agent applications. It is the production evolution of OpenAI's experimental `Swarm` framework.
* **How it works:** Built around four ultra-minimal primitives:
  1. **Agents:** LLMs configured with `instructions`, `tools`, and `output_type`.
  2. **Handoffs:** Specialized tool calls that transfer active control and conversation state from one agent (e.g., Triage Agent) to another (e.g., Refund Agent).
  3. **Guardrails:** Parallel validation checks that run concurrently on inputs or outputs and halt execution (`tripwire`) if safety or policy rules are violated.
  4. **Tracing:** Built-in telemetry that logs every tool call, handoff, and guardrail check to the OpenAI Dashboard.
* **Capabilities:** Built-in agent loop runner (`Runner.run()`), automatic Python-function-to-JSON-schema conversion, native MCP server support, voice agent compatibility, and model-agnostic provider interfaces (though optimized for OpenAI's Responses API and Chat Completions API).
* **Real Limits:** Intentionally minimalist. It does not provide complex cyclic graph orchestration, built-in distributed durable execution queues, or native RAG vector ingestion engines out of the box (unlike LangGraph).

---

## 3. Google: Gemini Agentic Tooling, ADK, Project Mariner, Jules, and Antigravity

### (a) Google Agentic Ecosystem (ADK, Vertex AI Agent Builder, A2A, Jules, Mariner)
* **What it actually is:** Google's full-stack enterprise and developer suite for building and running agents:
  1. **Google Agent Development Kit (ADK):** Google's open-source framework (Python/Java) for building multi-agent systems, optimized for Gemini 2.5 Pro/Flash and Vertex AI.
  2. **Agent2Agent (A2A) Protocol:** Google's open interoperability standard allowing agents built on different frameworks (LangGraph, CrewAI, ADK) and vendors to discover each other via "Agent Cards" and collaborate across enterprise boundaries.
  3. **Jules:** Google's asynchronous cloud coding agent integrated with GitHub that clones repos into a Google Cloud VM, plans fixes, runs tests, and creates PRs.
  4. **Project Mariner:** Google DeepMind's browser-use agent capability (available in Gemini Ultra / Vertex) that navigates web pages via DOM + visual rendering inside Chrome.
  5. **Gemini CLI:** Google's open-source terminal coding agent (`@google/gemini-cli`) offering a local CLI experience similar to Claude Code, backed by Gemini 2.5 Pro's 1M-token context window.

### (b) Google Antigravity
* **What it actually is:** Google's agent-first software development platform and IDE experience (powered by Gemini models). While traditional IDEs add an AI chat sidebar to a human text editor, Antigravity is designed around **autonomous agent orchestration** where developers supervise one or more asynchronous coding and verification agents working across editor, terminal, and integrated browser surfaces.
* **How it works:** Uses Gemini's native multimodal, long-context (1M–2M tokens), and tool-use capabilities to unify three environments inside one workspace:
  1. **Code Editor & Workspace:** Full repository state manipulation.
  2. **Terminal / Sandbox Execution:** Running build servers, compilers, and test runners.
  3. **Integrated Headless/Visual Browser Control:** The agent launches the local web app, opens a controlled browser instance, visually inspects the rendered UI, clicks elements, checks the browser console/network logs, and verifies that frontend changes actually work.
  4. **Artifact-Driven Verification:** Instead of forcing the developer to read thousands of lines of raw tool logs, the agent generates structured **Artifacts**—task lists, implementation plans, architectural diffs, and browser walkthrough recordings/screenshots—for human review and approval gates.
* **Capabilities:** Multi-agent background task dispatch ("Mission Control" style management), autonomous full-stack verification (backend + live frontend browser testing), native MCP integration, and cross-file refactoring leveraging Gemini's massive context window.
* **Real Limits:** High compute footprint when running concurrent local dev servers, browser automation, and multi-agent loops simultaneously; requires strong task boundary definition so parallel agents do not create conflicting edits on the same files in a working tree.

---

## 4. Nous Research: Hermes (Hermes 3 / Hermes 4 & Hermes Agent Framework)

* **What it actually is:** An open-weights family of frontier fine-tuned models (**Hermes 3**, **Hermes 4**, built on Llama 3.1 / Qwen / DeepSeek bases by **Nous Research**) paired with the open-source **Hermes Agent** runtime (`hermes-agent`). It is the premier open-source, self-hostable alternative to closed vendor agent models.
* **How it works:**
  * **Model Level:** Trained specifically on structured synthetic and real-world agent trajectories for native **ChatML formatting**, deterministic JSON schema adherence, multi-turn function calling, explicit `<tool_call>` and `<tool_response>` XML/special tokens, and deep `<think>` reasoning traces.
  * **Hermes Agent Runtime Level:** A full-featured open-source autonomous agent system created by Nous Research that runs in the terminal or via messaging gateways (Telegram, Discord, Slack, CLI). It features a persistent cross-session learning loop, built-in skill synthesis (the agent writes and saves its own reusable skills/tools in markdown/code), subagent spawning, cron job scheduling, and sandboxed execution backends (Docker, Modal, Daytona, SSH, local).
* **Capabilities:**
  * **100% Open & Local Capable:** Can run completely air-gapped on local enterprise GPUs (via `vLLM`, `SGLang`, `llama.cpp`, or `Ollama`) with zero data leaving the premises, or via OpenRouter/Nous Portal APIs.
  * **Unsteered / Neutral Alignment:** Unlike commercial APIs that frequently refuse benign security testing, red-teaming, or unconventional automation workflows due to hyper-sensitive safety filters, Hermes is trained to follow system instructions neutrally and accurately.
  * **Self-Improving Skill Memory:** Automatically extracts procedural memory (`SKILL.md`) from complex solved tasks so future runs do not repeat trial-and-error discovery.
* **Real Limits:**
  * Running the largest, most capable variants (e.g., 70B or 405B parameters) locally requires serious enterprise GPU VRAM (e.g., 2x–8x H100/A100s), whereas smaller 8B/14B variants struggle with deep 30-step multi-file coding loops compared to Claude Opus/Sonnet or `o3`.

---

## 5. Muse

*(Note for Trainers: In the agentic AI ecosystem, **"Muse"** refers to two distinct, major technologies depending on whether the training tracks Enterprise/Autonomous Agents vs. Real-Time World/Game Engineering Agents. Both must be understood clearly so trainers never conflate them.)*

### (a) Muse as an Autonomous Creative / Multimodal & Workspace Agent (and Muse AI Tooling)
* **What it actually is:**
  1. **Unity Muse:** An integrated agentic suite for 3D/real-time developers that uses natural language and workspace awareness to generate C# behavior scripts, create finite-state-machine behavior trees (`Muse Behavior`), generate textures/sprites/animations, and wire them directly into a scene hierarchy.
  2. **Muse (Spatial / Agentic Canvas & Creative Research Platforms / Origin-Muse variants):** Canvas-first and multimodal creative agent environments where agents collaborate with users across spatial boards, documents, audio/video assets, and code—acting as proactive thought-partners and execution workers rather than linear chat boxes.
* **How it works:** Connects domain-specific action handlers (scene graph manipulators, asset generators, code compilers, or spatial canvas nodes) to an LLM orchestrator so that natural language requests compile directly into executable project mutations (such as assembling an NPC patrol behavior tree or restructuring a project board).
* **Capabilities:** Bridges unstructured multimodal assets (2D/3D, audio, rich text, spatial cards) with structured execution logic (state machines, C# scripts, project graphs).
* **Real Limits:** Domain-specialized; cannot serve as a general-purpose enterprise DevOps or ERP orchestration engine.

### (b) Microsoft Muse (WHAM - World and Human Action Model)
* **What it actually is:** Developed by Microsoft Research in collaboration with Ninja Theory, **Muse** is a landmark generative AI **World and Human Action Model (WHAM)** trained on over 1 billion images and controller action sequences (7+ years of continuous human gameplay data).
* **How it works:** While text agents predict `[Text Thought -> API Tool Call -> Text Observation]`, Microsoft Muse is an action-conditioned autoregressive transformer that models `[Visual Environment State + Controller Action -> Next Environment State]`.
* **Capabilities:** Understands 3D physical space, object permanence, game physics, and reactive controller inputs in real time; used for training embodied agents, rapid gameplay prototyping, and simulating interactive environments.
* **Real Limits:** High GPU inference cost per frame; bounded to physical/virtual simulation domains rather than text-based enterprise workflow automation.

---

## 6. Cursor (Anysphere)

* **What it actually is:** The dominant AI-native code editor (a heavily customized fork of VS Code) featuring deeply integrated synchronous autocomplete (`Cursor Tab`), inline editing (`Cmd+K`), and an autonomous multi-file coding agent (**Cursor Agent / Composer** and **Background Agents**).
* **How it works:**
  * **Hybrid Indexing + Agentic Search:** Upon opening a project, Cursor computes Merkle trees of the repository and uploads encrypted file chunks to build a cloud vector index (Turbopuffer) for instant semantic codebase search (`@Codebase`), combined with local grep/file-read tools.
  * **Cursor Agent Loop:** Powered by frontier models (Claude 3.7/4 Sonnet, GPT-4.1, `o3`, Gemini 2.5 Pro) paired with Cursor's custom small fast-apply models. The agent plans edits, applies diffs across multiple files via a custom high-speed speculative decoding model ("Fast Apply"), reads real-time **LSP (Language Server Protocol) diagnostics** (red squiggly compiler/linter errors) directly from the IDE, runs terminal commands, and iterates up to 25 tool calls per loop (before asking to continue).
  * **Project Rules (`.cursor/rules/*.mdc`):** Scoped instruction files that inject architecture standards and tool constraints based on file glob patterns.
  * **Background Agents:** Cloud-hosted remote VMs that clone your GitHub repo and allow you to fire off multiple asynchronous coding tasks in parallel from inside the IDE or web dashboard.
* **Capabilities:**
  * Instant visual diff review (Accept/Reject per hunk or per file) directly in the editor.
  * Full **MCP Client** integration (supports `stdio` and `SSE` MCP servers configured in `.cursor/mcp.json`).
  * Automatic linter/typecheck error feedback loop without needing to manually run terminal build scripts.
* **Real Limits:**
  * **Closed Source Client:** Proprietary fork of VS Code; enterprise security teams must explicitly evaluate its cloud indexing (though "Privacy Mode" disables persistent server storage).
  * **25-Step Loop Cap:** By default, Cursor's foreground agent pauses after 25 sequential tool calls to prevent runaway token loops, requiring human confirmation to continue long tasks.
  * **Context Window Compression:** To keep latency low and costs predictable on flat-rate plans, Cursor aggressively truncates and summarizes file contexts compared to raw CLI agents like Claude Code.

---

## 7. Devin (Cognition Labs)

* **What it actually is:** The pioneer fully autonomous, cloud-hosted AI Software Engineer built by Cognition. Unlike IDE assistants that pair-program *with* a human on their local laptop, Devin operates as an independent remote teammate with its own cloud workstation.
* **How it works:**
  * When assigned a task (via Slack, Jira, Linear, GitHub issue, or Devin's web UI), Devin spins up an isolated cloud VM containing a shell/terminal, a full code editor, and a headless/visual Chrome browser.
  * Devin first inspects the repository, builds an interactive **Confidence Score & Step-by-Step Implementation Plan**, and awaits human sign-off (or proceeds automatically).
  * During execution, Devin writes code, runs unit/integration tests, deploys preview apps, opens the browser to click through the live app, reads stack traces, updates its own **Devin Wiki / Tribal Knowledge base** (persistent cross-session memories about repo quirks), and submits a GitHub Pull Request.
  * When reviewers leave comments on the GitHub PR, Devin wakes up, reads the PR review feedback, pushes new commits, and replies.
* **Capabilities:**
  * **True Asynchronous Parallelism:** A single human engineer can manage a fleet of 5 to 20 concurrent Devin instances working on backlog migrations, test coverage, bug triage, and dependency upgrades via Slack.
  * **Interactive Time-Travel Debugging:** The human supervisor can scrub backward and forward through a video-like timeline of every terminal command, file diff, and browser screenshot Devin saw.
  * **Devin Search & Devin Wiki:** Automatically indexes and documents entire enterprise repositories into interactive architectural diagrams and onboarding guides.
* **Real Limits:**
  * **Struggles with Ambiguous / Greenfield Architecture:** Excels at well-scoped tasks with clear verification criteria (e.g., *"Upgrade React 17 to 18 and fix all broken Jest tests"*, *"Migrate 40 API endpoints from v1 to v2"*), but regularly fails or over-engineers open-ended product design tasks.
  * **Environment Onboarding Friction:** Before Devin can be effective on a complex enterprise monorepo, engineers must spend time configuring Devin's VM snapshot (environment variables, private package registries, database seed scripts, mock services).
  * **Cost Model (ACUs):** Billed via Agent Compute Units (ACUs). A poorly scoped task where Devin gets stuck in a 45-minute test-failure loop can burn significant ACU credits without delivering a usable PR.

---

## 8. Manus (Butterfly Effect / Manus AI)

* **What it actually is:** A cloud-hosted, general-purpose autonomous consumer and knowledge-work agent designed to execute complex, multi-domain tasks from start to finish (research, data analysis, web scraping, spreadsheet creation, dashboard building, and full web deployment).
* **How it works:**
  * Uses a **Multi-Agent Orchestration Architecture** running inside an asynchronous cloud Linux sandbox (Ubuntu container with Python, Node.js, headless Chromium browser, file converters, and deployment CLI tools pre-installed).
  * When given a high-level prompt (e.g., *"Research the top 30 commercial real estate listings in Singapore District 1, analyze yield trends, generate a financial PDF report, and deploy an interactive filtering web app"*), a **Planner Agent** creates a persistent `todo.md` file inside the workspace.
  * Execution Subagents iterate through `todo.md`, writing Python scripts on the fly to scrape data, control the browser, clean CSVs with `pandas`, generate charts with `matplotlib`, compile a React app, and publish it to a live public URL—checking off items in `todo.md` as external state memory to prevent context drift.
* **Capabilities:**
  * **Cloud Asynchronous Execution:** Continues running in the cloud even if the user closes their laptop or browser; sends a notification when finished.
  * **"Manus's Computer" Live Side-Panel:** Users can watch the agent's virtual desktop/browser/terminal in real time and take over the browser session whenever a login wall or CAPTCHA appears.
  * **Deliverable-Oriented:** Unlike chat tools that return text, Manus returns packaged artifacts: `.xlsx` models, `.pptx` decks, `.pdf` reports, zip archives, and live hosted web applications.
* **Real Limits:**
  * **Slow Turnaround:** Because it writes custom scripts, browses dozens of live websites, and verifies its own `todo.md` steps, a single prompt routinely takes 10 to 45 minutes to complete.
  * **Hallucinated Fallback Data:** When a target website blocks Manus's cloud browser IP (403 Forbidden / CAPTCHA), the underlying coding subagent sometimes silently writes a Python script to *generate synthetic/estimated data* to satisfy the `todo.md` step unless the user explicitly inspects the execution logs.
  * **High Credit Consumption:** Multi-agent long-horizon loops consume thousands of tokens per minute; complex tasks quickly exhaust monthly credit tiers.

---

## 9. LangChain & LangGraph

* **What it actually is:**
  * **LangChain:** The massive open-source Python/TypeScript integration library providing standardized wrappers for LLMs, prompt templates, document loaders, vector stores, and tools.
  * **LangGraph:** The low-level, industrial-grade **stateful agent orchestration framework** created by the LangChain team specifically for building controllable, cyclic, production multi-agent systems. *(Trainers must emphasize: For production agents today, engineers build the control flow in **LangGraph**, using LangChain only for standard model/tool interfaces).*
* **How it works (LangGraph):**
  * Models agent workflows as a formal **State Machine / Directed Cyclic Graph**.
  * Every graph consists of three core primitives:
    1. **`State`:** A strictly typed shared data structure (`TypedDict` or `Pydantic` model) that persists across the entire execution.
    2. **`Nodes`:** Python/JS functions (or LLM calls) that read the current `State`, perform work, and return an update to the `State`.
    3. **`Edges` & `Conditional Edges`:** Deterministic or LLM-driven routing functions that decide which `Node` executes next (including loops back to previous nodes).
  * **Checkpointers (Persistence Layer):** Automatically saves the exact graph `State` to Postgres/Redis/SQLite after every single node step ("super-step").
* **Capabilities:**
  * **Durable Execution & Fault Tolerance:** If a server crashes on step 14 of a 20-step agent workflow, LangGraph resumes from step 14 without losing state.
  * **First-Class Human-in-the-Loop (`interrupt()`):** An agent can pause execution indefinitely before a sensitive action, serialize its state to Postgres, wait 3 days for a manager to approve via Slack, and resume execution with human-edited state.
  * **Time-Travel & Forking:** Developers can inspect any historical state checkpoint, modify a variable or tool output, and replay the agent from that exact point.
  * **LangSmith & LangGraph Platform:** Commercial observability (token tracing, evaluation datasets, latency waterfall charts) and managed deployment infrastructure.
* **Real Limits:**
  * **Steep Learning Curve & Boilerplate:** Requires strong software engineering skills. Defining state reducers, graph topologies, and persistence checkpointers is significantly more verbose than spinning up an agent in CrewAI or OpenAI Agents SDK.
  * **Abstraction Overhead (LangChain legacy):** Old `langchain` chains (`AgentExecutor`) suffered from deep, leaky abstractions that were hard to debug; while `LangGraph` solved this by moving to explicit state nodes, legacy tutorials frequently confuse learners by mixing deprecated `AgentExecutor` patterns with modern `LangGraph`.

---

## 10. CrewAI

* **What it actually is:** A high-level, open-source Python multi-agent framework (paired with a commercial enterprise platform, **CrewAI Enterprise**) built around **role-playing organizational metaphors** (`Agents`, `Tasks`, `Crews`) and deterministic event-driven orchestration (`Flows`).
* **How it works:**
  * Standalone Python framework (completely rewritten from scratch, independent of LangChain).
  * Developers define:
    1. **`Agents`:** Assigned a `role` (e.g., *"Senior Financial Analyst"*), a `goal`, a `backstory`, an LLM, and `tools`.
    2. **`Tasks`:** Specific assignments with a `description`, an `expected_output`, and an assigned `agent`.
    3. **`Crew`:** The team container that coordinates execution using either a `Sequential` process (Task 1 -> Task 2 -> Task 3) or a `Hierarchical` process (an auto-generated Manager Agent delegates tasks and reviews outputs).
    4. **`Flows` (`@start`, `@listen`, `@router`):** An event-driven deterministic backbone layer that connects multiple Crews together with standard Python control logic.
* **Capabilities:**
  * **Fastest Prototyping Speed:** A non-expert Python developer can build a working 3-agent collaborative pipeline in under 40 lines of YAML and Python.
  * **Built-in Memory System:** Includes Short-Term Memory (ChromaDB RAG), Long-Term Memory (SQLite task evaluation history), and Entity Memory out of the box.
  * **Built-in Guardrails & Structured Outputs:** Native support for forcing task outputs into Pydantic schemas and programmatic validation callbacks.
* **Real Limits:**
  * **Chattiness & Token Inflation:** Because CrewAI heavily relies on rich `backstory` prompts and inter-agent delegation dialogue (especially in `Hierarchical` mode), agents frequently engage in verbose back-and-forth chatter that burns tokens and adds latency without improving accuracy.
  * **Less Granular Loop Control:** When an individual agent is inside a single `Task` loop, you have less fine-grained step-by-step state-machine control over individual tool-call retries compared to LangGraph.

---

## 11. Microsoft AutoGen & Semantic Kernel (Converging into Microsoft Agent Framework)

* **What it actually is:** Microsoft's two flagship agentic frameworks:
  1. **AutoGen (Microsoft Research):** The pioneer open-source framework for **conversational multi-agent collaboration** and event-driven asynchronous agent meshes (completely redesigned in **AutoGen v0.4**).
  2. **Semantic Kernel (SK):** Microsoft's enterprise-grade, multi-language (**C# / .NET**, **Python**, **Java**) SDK for integrating LLMs, plugins, and Enterprise Process Frameworks into production corporate applications.
  *(Trainer Note: Microsoft is actively unifying AutoGen's multi-agent runtime abstractions with Semantic Kernel's enterprise foundation under the unified **Microsoft Agent Framework / Azure AI Agent Service** umbrella).*
* **How it works:**
  * **AutoGen v0.4 Architecture:** Built on a three-layer architecture:
    * **`Core` (`autogen-core`):** An asynchronous, event-driven Actor Model (supporting distributed runtime across processes and languages).
    * **`AgentChat` (`autogen-agentchat`):** High-level task-driven multi-agent patterns (`RoundRobinGroupChat`, `SelectorGroupChat`, `MagenticOneGroupChat`, `Swarm`), plus `AutoGen Studio` (a low-code GUI builder).
    * **`Extensions` (`autogen-ext`):** Docker command-line code executors, MCP bridges, and OpenAI/Azure model clients.
  * **Semantic Kernel Architecture:** Centers on a `Kernel` object (a dependency injection container) that holds AI service connectors and `Plugins` (native C#/Python/Java methods decorated as tools). Includes the **SK Agent Framework** (supports `ChatCompletionAgent`, `OpenAIAssistantAgent`, and `AzureAIAgent`) and the **SK Process Framework** (deterministic business workflow orchestration).
* **Capabilities:**
  * **Enterprise Language Support (C#/.NET & Java):** Semantic Kernel is the indisputable industry standard for enterprises whose backend stack is C#/.NET or Java rather than Python.
  * **Dockerized Code Execution (AutoGen):** AutoGen has first-class built-in support for agents writing Python/Bash code and executing it inside isolated local or remote Docker containers.
  * **Magentic-One (AutoGen):** A pre-built generalist multi-agent team architecture from Microsoft (Orchestrator + WebSurfer + FileSurfer + Coder + ComputerTerminal) capable of solving complex web and file benchmarks.
* **Real Limits:**
  * **Version Fragmentation (AutoGen):** AutoGen underwent a breaking architectural rewrite from `v0.2` to `v0.4`, alongside a community fork (`AG2`). Trainers must warn developers that `v0.2` code copied from older blogs or LLMs will not run on `v0.4` without migration.
  * **Heavy Enterprise Boilerplate (Semantic Kernel):** SK uses strict enterprise patterns (Dependency Injection, Factory builders, Kernel filters) that feel heavyweight for rapid Python data science prototyping.

---

# 3. COMPARISON

## Master Comparison Matrix

| Platform / Product | Category | Primary Domain | Execution Environment | Single vs. Multi-Agent | License / Open vs. Closed | Pricing & Cost Model |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Claude Code** | CLI Product | Software Engineering & DevOps | Local Terminal (or local Docker / CI) + Cloud API | Single Primary Agent + Spawned Subagents (`Task`) | Proprietary CLI binary; closed Anthropic models | Subscription (Claude Pro/Max: $20–$200/mo) OR Pay-as-you-go API tokens |
| **Claude Agent SDK** | Developer SDK | Coding & Custom Enterprise Agents | Self-hosted Node.js/Python runtime + Cloud API | Single or Programmable Multi-Agent | Proprietary SDK; closed Anthropic models | Pay-as-you-go Anthropic API token consumption |
| **OpenAI Codex (CLI / Cloud)** | CLI + Hosted Product | Software Engineering | CLI: Local sandbox; Cloud: OpenAI Managed Containers | Single Agent per task (Parallel task dispatch in Cloud) | CLI: Open Source (Apache-2.0); Cloud & Models: Closed | Included in ChatGPT Plus/Pro/Team/Enterprise OR OpenAI API tokens |
| **OpenAI Operator (CUA)** | Hosted Product & API | Web Browser & GUI Automation | OpenAI Hosted Cloud Browser VM | Single Agent (with Human Takeover loop) | Closed Source | Included in ChatGPT Pro/Plus tiers OR API (`computer-use-preview` token pricing) |
| **OpenAI Agents SDK** | Developer Framework | General Purpose Multi-Agent Apps | Self-hosted Python/TS runtime + Cloud/Local LLM API | Multi-Agent (via Handoffs & Agent-as-Tool) | Open Source (MIT License) | Free framework; user pays underlying LLM API token costs |
| **Google Antigravity** | Agentic IDE Platform | Full-Stack Software Engineering | Local / Hybrid Workspace + Integrated Browser + Gemini API | Multi-Agent Orchestration ("Mission Control") | Proprietary IDE Platform; Gemini models | Subscription tiers + Google Cloud / Gemini API consumption |
| **Google ADK** | Developer Framework | General Purpose & Enterprise Agents | Self-hosted or Google Vertex AI Agent Engine | Multi-Agent (Hierarchical + A2A Protocol) | Open Source Framework (Apache-2.0) | Free framework; pay for Gemini API / Vertex AI runtime |
| **Hermes (Nous Research)** | Open Model Family + Agent Runtime | General Purpose, Coding, Autonomous Ops | 100% Local GPU / Self-Hosted Server / Docker / Cloud API | Single Agent + Subagent Spawning | Open Weights & Open Source Runtime (Apache-2.0 / MIT) | Free to self-host (pay only GPU compute) OR low-cost inference via OpenRouter/Nous API |
| **Muse (Unity / Microsoft WHAM)** | Domain Product / World Model | 3D/Game Dev & Interactive Environment Sim | Local Editor + Cloud Inference / GPU Cluster | Specialized Domain Agent / Action Model | Closed / Research Weights (WHAM) | Unity Muse: Subscription; Microsoft WHAM: Research / Azure GPU compute |
| **Cursor** | AI-Native IDE Product | Software Engineering | Local IDE (VS Code fork) + Cloud Background VMs | Single Foreground Agent + Parallel Cloud Background Agents | Closed Source Product | SaaS Subscription ($20/mo Pro, $40/mo Business, $200/mo Ultra) + Usage-based overages |
| **Devin** | Hosted Autonomous Agent | End-to-End Software Engineering | 100% Cloud Hosted Linux/Browser/Editor VM | Fleet of Independent Cloud Agent Workers | Closed Source SaaS | Base plan ($20/mo Core pay-as-you-go or $500/mo Team) + **ACU** (Agent Compute Unit) burn |
| **Manus** | Hosted General Agent | Knowledge Work, Research, Data & Web Apps | 100% Cloud Hosted Linux + Headless Browser Sandbox | Multi-Agent (Planner + Specialized Subagents) | Closed Source SaaS | Credit-based SaaS Subscription ($39/mo–$199/mo tiers + top-up credits) |
| **LangGraph** | Developer Framework | Complex Stateful Enterprise Agents | Self-hosted Python/TS OR LangGraph Cloud Platform | Multi-Agent & Arbitrary Cyclic State Graphs | Framework: Open Source (MIT); Platform/LangSmith: Commercial | Free OSS framework; LangSmith/LangGraph Platform charges per node execution & seat |
| **CrewAI** | Developer Framework + Enterprise SaaS | Role-Based Multi-Agent Business Workflows | Self-hosted Python OR CrewAI Enterprise Cloud | Multi-Agent (`Crews` + deterministic `Flows`) | Framework: Open Source (MIT); Enterprise Suite: Commercial | Free OSS framework; CrewAI Enterprise charges SaaS tiers by executed crew runs |
| **AutoGen / Semantic Kernel** | Developer Frameworks | Enterprise Apps (.NET/Python) & Agent Meshes | Self-hosted (.NET/Python/Java) + Docker / Azure AI | Multi-Agent (Actor Mesh / GroupChat / Process) | Open Source (MIT License) | Free OSS frameworks; pay only for Azure OpenAI / LLM tokens & compute |

---

## Five Key Axes of Differentiation

### 1. Coding-Specific vs. General-Purpose
* **Coding-First Platforms (`Claude Code`, `Cursor`, `Devin`, `OpenAI Codex`, `Google Antigravity`):** Built around a deterministic feedback engine—the **compiler, linter, test suite, and Git working tree**. Because code either compiles/passes tests or throws a stack trace, these agents can self-verify with high accuracy.
* **General-Purpose Platforms & Frameworks (`Manus`, `Operator`, `LangGraph`, `CrewAI`, `AutoGen`, `OpenAI Agents SDK`, `Hermes`):** Must operate in domains where "ground truth verification" is noisy or non-existent (e.g., summarizing legal policies, researching competitors, triaging customer support tickets). They rely heavily on structured output validation, LLM-as-a-Judge guardrails, or human approval checkpoints.

### 2. Hosted Cloud Sandbox vs. Local Execution
* **Local Execution (`Claude Code`, `Cursor Foreground`, `Codex CLI`, `Hermes Local`):**
  * *Pros:* Zero onboarding environment setup (already has your local `.env`, VPN access, SSH keys, and cached Docker images); low latency.
  * *Cons:* Ties up your local machine; high blast-radius risk if an agent runs a destructive shell command without containerization.
* **Hosted Cloud Sandbox (`Devin`, `Manus`, `Operator`, `Codex Cloud`, `Cursor Background Agents`):**
  * *Pros:* True asynchronous scaling (fire off 10 tasks and close your laptop); total isolation from your personal hard drive.
  * *Cons:* Cannot reach private corporate databases or intranet tools unless enterprise VPN tunnels / VPC peering are configured; blocked by consumer anti-bot WAFs (Operator/Manus).

### 3. Single-Agent Loop vs. Multi-Agent Orchestration
* **Single-Agent with Subagent Tooling (`Claude Code`, `Codex`, `Cursor`):** A single coherent orchestration loop holds the master task context and only spawns transient, isolated child subagents for bounded read-only reconnaissance. This minimizes communication loss ("telephone game" drift).
* **Explicit Multi-Agent Networks (`CrewAI`, `AutoGen GroupChat`, `LangGraph Multi-Agent`, `OpenAI Agents SDK`):** Divides responsibilities across distinct agent personas with separate system prompts and restricted toolsets. Essential when a single agent would exceed tool **Before Section 3 continues, three corrections to what I wrote in Sections 2–3.** I checked two items I was unsure about, and one was wrong.

**Correction 1: Muse was wrong. Replace the whole "Muse" entry in Section 2.** What I wrote about Unity Muse and Microsoft WHAM is about other products that share the name, and "Origin-Muse / spatial canvas" was made up. The Muse your trainers will be asked about is Meta's:
- **What it is:** Meta's secure, private personal AI agent that proactively helps with people's goals and suggests ideas. Meta launched it on September 8, 2026.
- **How it works:** It runs on Muse Secure VM, a dedicated virtual machine that holds both the agent and the person's data. Its reasoning engine is Muse Spark 1.3. People talk to it through a normal chat window, either in the Muse app or in WhatsApp.
- **What it can do:** It can browse websites, connect to your apps, send emails, make purchases, fill out forms, manage longer-running goals, and keep working after you close the app. You approve the sensitive steps. Muse for Mac (17 September 2026) lets the agent work inside Files, Mail, Messages, Calendar and Notes. There is also Muse Code, Meta's terminal coding agent, and Muse Glimmer, a separate open-weights model.
- **Price (secondary source):** Free with a weekly limit, Power at $20/month, Maximum at $100/month, with the allowance counted weekly in Muse tokens.
- **Limits that matter for Singapore:** It launched for US adults only. I don't know of a Singapore launch date, so check before you teach it as something learners can use. It is also brand new: at launch there were no independent benchmarks.
- **Where it sits:** a hosted, closed, general-purpose consumer agent. It belongs in the same group as Manus and OpenAI's ChatGPT agent, not with the coding tools.

**Correction 2: Hermes Agent is not tied to Hermes models.** It is an open-source autonomous agent that Nous Research released in February 2026. It is free and open source under the MIT license (I wrote "Apache-2.0 / MIT"; it is MIT). It works with any model: Nous Portal, OpenRouter, OpenAI, your own endpoint and others, and you switch with `hermes model` without changing code. You can run it on a $5 VPS, a GPU cluster, or serverless infrastructure, and talk to it from Telegram while it works on a cloud VM. Teach the Hermes *models* and the Hermes *Agent* as two separate things. You can run the agent with Claude or GPT behind it.

**Correction 3: version numbers and prices go out of date quickly.** The model names in Section 2 (Claude 3.7/4, o3, Gemini 2.5) and the prices in the Section 3 table reflect what I knew at training time, not November 2026. Treat every price, model name and default limit (for example Cursor's 25-step cap) as **check before teaching**. The architecture and concepts in Sections 4–10 change much more slowly.

---

# 3. COMPARISON (continued)

### 3. Single-agent vs. multi-agent (continued)
* **Explicit multi-agent networks (CrewAI, AutoGen GroupChat, LangGraph multi-agent, OpenAI Agents SDK handoffs, Google ADK + A2A):** Use separate agents when one agent would need too many tools (tool choice gets worse as the list grows), when tasks need different permissions (the research agent can browse but cannot send email), or when separate context windows let work run in parallel.
* **The cost of multi-agent:** every handoff loses some information, and token use multiplies roughly by the number of agents. Each agent is one more thing that can fail, and failures are harder to trace back.
* **Rule of thumb:** start with one agent. Split only when you can name the specific failure that splitting fixes.

### 4. Open vs. closed
There are three separate layers that can each be open or closed. Learners mix them up.

| Layer | Open examples | Closed examples |
| :--- | :--- | :--- |
| **Model weights** | Hermes models, Llama, Qwen, DeepSeek, Muse Glimmer | Claude, GPT, Gemini, Muse Spark |
| **Harness / runtime code** | Hermes Agent, Codex CLI, Gemini CLI, LangGraph, CrewAI, AutoGen, OpenAI Agents SDK, Google ADK | Cursor, Devin, Manus, Meta Muse app, Antigravity |
| **Hosting / data path** | Self-hosted anything | Any SaaS agent; any closed model API |

* An open-source harness calling a closed model API is **not** "fully open". Your data still leaves your premises.
* Only an open harness, plus open weights, plus self-hosted inference keeps data entirely in-house. This is what matters for strict PDPA or sector rules (MAS TRM for finance, government data classification).

### 5. Pricing and cost models

| Cost model | Who uses it | How the cost behaves | Main risk |
| :--- | :--- | :--- | :--- |
| **Flat subscription with usage caps** | Claude Pro/Max, ChatGPT plans, Cursor, Meta Muse, Manus tiers | Predictable monthly bill; heavy users hit rate or weekly limits | Hitting a limit mid-task; caps change without much notice |
| **Pay per token (API)** | Claude Agent SDK, OpenAI Agents SDK, LangGraph/CrewAI/AutoGen built on paid APIs | Cost scales with context size × number of loop steps | A runaway loop gives a surprise bill |
| **Compute-unit / credit burn** | Devin (ACUs), Manus credits, Nous Portal tiers | Paying for agent working time | A stuck agent burns credits without producing anything |
| **Per-seat enterprise** | Cursor Business, Copilot-class, CrewAI/LangSmith enterprise | Licence per user plus usage | Paying for idle seats |
| **Self-hosted compute** | Hermes Agent + open weights, any OSS framework on local GPUs | Fixed hardware or GPU cost; tokens cost nothing extra | Upfront capex, ops burden, weaker models at small sizes |
| **Free framework plus paid observability** | LangGraph + LangSmith, CrewAI OSS + Enterprise | Framework free; tracing and deployment paid | Hidden platform cost appears at scale |

**Why agent costs explode (teach this):** in a basic loop, the whole conversation so far is re-sent at every step. A 40-step task where the context grows to 100k tokens can therefore process millions of input tokens. Prompt caching cuts this sharply (cached input is billed at a fraction of the normal rate), which is why cache hit rate is a key cost number.

---

# 4. CORE SHARED ARCHITECTURE

Every product in Section 2 is the same machine with different packaging. That machine has the parts below.

## 4.1 The agent loop
```
GOAL → [ model reads context → decides: answer OR call tool(s) ]
         ↓ tool call
       harness executes tool → result appended to context
         ↓
       repeat until: model says "done" | step/budget limit | human interrupt | error cap
```
* **ReAct pattern (Reason + Act):** think, act, observe, repeat. Nearly every agent loop is a version of this.
* **Plan-then-execute:** a planning step writes an explicit plan (`todo.md` in Manus, an implementation plan in Devin or Antigravity, plan mode in Claude Code), then execution works through it. This cuts drift on long tasks.
* **Stop conditions:** the model's own "I'm done", a maximum number of turns, a token or cost budget, a timeout, a human stop. A production agent needs **all** of them, not just the first.
* **Who controls the loop:** in products (Claude Code, Devin) the vendor wrote the loop. In frameworks (LangGraph) you write it. In the Claude Agent SDK and OpenAI Agents SDK, the vendor's loop is handed to you to configure.

## 4.2 Tools and function calling
* **A tool** is a named capability with a description and an input schema (usually JSON Schema).
* **Function calling:** the model does **not** run anything itself. It outputs a structured request (tool name plus JSON arguments). The **harness** checks it, runs it, and feeds the result back in.
* **Parallel tool calls:** one model turn can request several independent tools at once (for example, read 5 files together).
* **Tool description quality decides tool accuracy.** The model chooses tools from their names and descriptions alone. Vague descriptions lead to wrong tool choices.
* **Built-in tool families:** file read/write/edit, shell/bash, search (grep/glob), web search/fetch, browser control (DOM-based or screenshot-based), code interpreter, computer use (mouse/keyboard on screenshots), subagent spawn, memory read/write.

## 4.3 MCP (Model Context Protocol)
* **Roles:** *Host* (the app the user runs: Claude Code, Cursor, ChatGPT, Antigravity) contains a *client*, which connects one-to-one to an *MCP server* that wraps a tool or data source (GitHub, Postgres, Slack, Google Drive).
* **Server primitives:** **Tools** (actions), **Resources** (readable data), **Prompts** (reusable templates). The client side can also offer **sampling** (the server asks the host's model to generate) and **elicitation** (the server asks the user for input).
* **Transports:** `stdio` (local process on your machine) and HTTP (remote; "Streamable HTTP" replaced the older SSE transport). Remote servers use OAuth for authentication.
* **Why it matters:** before MCP, connecting M AI apps to N tools needed M×N custom integrations. With MCP it is M + N.
* **What it is not:** it is not an agent, not a model, and not a security boundary. An MCP server can be malicious (see 5.x tool poisoning).
* **A2A (Agent2Agent):** a different protocol. MCP connects an agent to tools; A2A connects one agent to another agent.

## 4.4 Memory (four kinds; learners blur them)
| Type | What it is | Product examples |
| :--- | :--- | :--- |
| **Working memory (context window)** | Everything the model can "see" right now | All agents |
| **Instruction / project memory** | Standing rules loaded at every session start | `CLAUDE.md`, `AGENTS.md`, `.cursor/rules`, Devin Wiki/Knowledge |
| **Episodic / long-term memory** | Searchable record of past sessions and facts | Hermes Agent cross-session search, CrewAI long-term memory, LangGraph Store, ChatGPT/Claude memory |
| **Procedural memory (skills)** | Saved "how to do X" instructions, scripts or resources loaded only when needed | Claude Agent Skills (`SKILL.md`), Hermes self-written skills |

* **External-state memory:** writing progress to files (`todo.md`, `progress.md`, git commits) so the agent can pick up again after its context is compacted or reset.
* **Compaction:** summarising old context to free space. This loses detail.

## 4.5 Context engineering (the discipline that replaced "prompt engineering" for agents)
* Decide what goes into the window, when, and in what form: just-in-time file reads instead of loading everything up front, subagents for exploration (only their summaries come back), tool-result trimming, and skills that load on demand.
* This ties directly to your own teaching line: **context scales, prompts do not.**

## 4.6 Sandboxing (in order of isolation strength)
1. **None:** the agent runs as you on your laptop. Fastest, and the most dangerous.
2. **OS-level sandbox:** macOS Seatbelt or Linux Landlock/seccomp. Limits which files can be written and blocks the network (Codex CLI, Claude Code sandbox mode).
3. **Container (Docker):** separate filesystem, shares the host kernel (AutoGen executors, devcontainers).
4. **MicroVM (Firecracker, gVisor):** its own kernel. Standard for hosted code execution (E2B, Modal, Daytona).
5. **Dedicated cloud VM:** a full machine per agent (Devin, Manus, Codex Cloud, Meta Muse Secure VM, Cursor Background Agents).
* **Two separate controls:** *filesystem* scope (what it can touch) and *network egress* (where it can send data). Most data leaks happen through the network, not the filesystem.

## 4.7 Approval gates / human-in-the-loop
* **Permission modes:** ask every time, then allowlist specific commands (for example `npm test` is fine, `rm` is not), then auto-approve edits, then full bypass ("YOLO" / `--dangerously-skip-permissions`).
* **Gate types:** pre-action approval (before a tool runs), plan approval (before execution starts), takeover (the human handles login, 2FA or payment directly, as in Operator, Manus and Muse), post-hoc review (PR review), and durable interrupts (LangGraph `interrupt()` pauses for days).
* **Guardrails:** automated checks (input/output validators, policy classifiers) that run without a human, such as tripwires in the OpenAI Agents SDK and hooks in Claude Code.

## 4.8 Observability
* **Traces:** a full record of every model call, tool call, its inputs and outputs, token count, latency and cost (LangSmith, OpenAI Traces, Langfuse, Arize, OpenTelemetry).
* **Evals:** test sets of tasks with known-good outcomes, run on every change to the prompt, tools or model.
* **No traces means no debugging.** This is the single biggest difference between hobby agents and production agents.

---

# 5. FAILURE MODES AND LIMITATIONS

| # | Failure mode | What it looks like in practice | How to detect it | Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Context rot** | Quality drops as context fills: earlier instructions are ignored, rules forgotten, repeated work | Rule violations rise late in a session; compare early vs. late steps in traces | Short sessions, subagents, `/clear`, external progress files |
| 2 | **Compaction loss** | After auto-summary, the agent "forgets" a constraint or exact value | Behaviour changes right after a compaction event in the log | Put critical rules in `CLAUDE.md`/`AGENTS.md` (reloaded every session), not in chat |
| 3 | **Hallucinated tool calls** | Calls a tool that doesn't exist, invents parameters, uses the wrong ID format | Schema validation errors; "tool not found" in traces | Strict schemas, fewer and clearer tools, return helpful error messages |
| 4 | **Hallucinated results / false success** | Says "all tests pass" when they were never run; says "file updated" with no diff | Compare the claim against the actual tool log; independent verification step | Require evidence (test output, diff, screenshot) before marking done |
| 5 | **Fabricated fallback data** | Blocked from a site, it generates "estimated" or synthetic data and presents it as real | Look for `random`, "sample" or "mock" data in scripts; numbers with no source URL | Instruction: "If data is unavailable, stop and report; never synthesise" |
| 6 | **Reward hacking / gaming the check** | Deletes or skips failing tests, hard-codes expected outputs, weakens assertions | Diff review shows test files changed; coverage drops | Protect test files (read-only); review diffs for test edits |
| 7 | **Doom loops** | Repeats the same failing fix 10+ times | The same tool and arguments repeated in the trace; error messages repeating | Step caps, loop detection, "after 3 failed tries, stop and ask" |
| 8 | **Cost blow-up** | Bill or credit use far above plan | Per-run cost dashboards; tokens per task trending up | Budgets and caps per run, prompt caching, cheaper models for subtasks |
| 9 | **Scope creep / over-engineering** | Asked to fix one bug, rewrites 30 files or adds unrequested features | Diff size far larger than the task needs | Narrow task specs; "change only X" constraints; plan approval |
| 10 | **Sandbox limits** | Can't install a package, reach an internal API or database, or a VPN-only site | `network unreachable`, 403, DNS failures in logs | Pre-bake environment images; allowlisted egress; local agent for intranet work |
| 11 | **Environment mismatch** | Works in the agent's VM, fails in prod or on your laptop | CI failure after an agent PR | Same devcontainer for agent, developer and CI |
| 12 | **Anti-bot blocking** | Browser agents stopped by CAPTCHA, WAFs, or logins | Repeated takeover requests; 403s | Use APIs/MCP instead of browsing where possible |
| 13 | **Direct prompt injection** | User input tries to override the system prompt | Red-team test prompts; guardrail tripwires | Input guardrails; least-privilege tools |
| 14 | **Indirect prompt injection** | Hidden instructions in a web page, email, PDF or issue get the agent to act | Unexpected tool calls right after reading external content | Treat all fetched content as untrusted; approval gate on sensitive actions after external reads |
| 15 | **"Lethal trifecta" exfiltration** | Agent with private data + untrusted content + an outbound channel leaks data | Outbound requests to unknown domains; URLs with encoded data | Never combine all three without strict egress allowlisting |
| 16 | **Tool poisoning / malicious MCP server** | A third-party MCP server's tool description contains hidden instructions, or the server changes after approval ("rug pull") | Audit tool descriptions; pin versions; watch for tool definitions changing | Only use vetted servers; pin versions; review descriptions |
| 17 | **Credential leakage** | Agent prints `.env` secrets into logs, commits keys, or pastes them into web forms | Secret scanning (gitleaks, GitHub push protection) | Keep secrets out of the agent's reach; scoped short-lived tokens |
| 18 | **Destructive actions** | `rm -rf`, `DROP TABLE`, force-push, mass emails, real purchases | Audit log of high-risk commands | Deny-lists, approval gates, backups, staging-only credentials |
| 19 | **Approval fatigue** | Humans click "approve" on everything after 20 prompts | High approval rate with near-zero review time | Allowlist safe actions so the remaining prompts mean something |
| 20 | **Multi-agent telephone game** | Detail lost between agents; agents contradict each other or redo work | Compare the handoff message with the original requirement | Fewer agents; structured handoff schemas; shared state |
| 21 | **Parallel edit conflicts** | Two agents edit the same files; merge conflicts | Git conflicts; overwritten changes | Git worktrees or branches per agent; non-overlapping task boundaries |
| 22 | **Non-determinism** | Same prompt gives different results run to run | Run evals several times; measure variance | Evals with pass rates, not single runs; lower temperature where possible |
| 23 | **Framework churn / version drift** | Tutorial code doesn't run (AutoGen 0.2 → 0.4, LangChain `AgentExecutor` → LangGraph, SK/AutoGen → Microsoft Agent Framework) | Import errors, deprecation warnings | Pin versions; check the date on tutorials |
| 24 | **Vendor lock-in** | Prompts, skills, memory formats and tool wiring only work on one vendor | Try switching the model in a test; count vendor-specific APIs | MCP for tools; model-agnostic harness; keep knowledge in portable markdown |
| 25 | **Model deprecation** | Pinned model retired; behaviour changes on upgrade | Vendor deprecation notices; eval regressions | Re-run evals on every model change |
| 26 | **Rate limits / caps** | Agent stalls mid-task when the subscription cap is hit | 429 errors; "limit reached" | Budget-aware scheduling; fallback models |
| 27 | **Data residency / compliance** | Client data processed in a foreign cloud against policy (PDPA, MAS TRM, public-sector classification rules) | Data-flow mapping; vendor DPA review | Regional hosting, enterprise zero-retention terms, or self-hosting |
| 28 | **Over-trust / skill erosion** | Team merges agent output nobody understands | Review time per PR falls; incidents traced to agent code | Require a human owner for every merged change |
| 29 | **Silent partial completion** | Did 7 of 10 subtasks and reports success | Checklist reconciliation against the original task | Explicit acceptance criteria checked item by item |
| 30 | **Latency mismatch** | A 20-minute agent used where a 2-second answer was needed | User drop-off; timeouts | Use chat or a fixed workflow for quick tasks |

---

# 6. TERMINOLOGY GLOSSARY

| Term | Plain-language definition |
| :--- | :--- |
| **LLM** | A model that predicts text; the "brain" inside every agent. |
| **Foundation / frontier model** | A large general-purpose model (Claude, GPT, Gemini, Muse Spark); "frontier" means the current most capable ones. |
| **Open-weights model** | A model whose trained weights you can download and run yourself. |
| **Agent** | An LLM in a loop that chooses and uses tools to reach a goal, deciding its own next steps. |
| **Agentic** | Describes how much a system decides its own steps; it is a spectrum, not yes/no. |
| **Workflow (vs. agent)** | Steps fixed in advance by a human; an agent chooses its steps at runtime. |
| **Agent loop** | The repeated cycle of think, act, observe until done. |
| **ReAct** | The basic agent pattern: reason, then act, then read the result. |
| **Harness / scaffold** | The code around the model that runs the loop, executes tools and manages context. |
| **Agent SDK** | A library that gives developers a ready-made harness to build their own agents (Claude Agent SDK, OpenAI Agents SDK). |
| **Agent framework** | A library for designing agent logic and multi-agent structures in code (LangGraph, CrewAI, AutoGen). |
| **Agent platform** | A packaged product or hosted service that runs agents for you (Devin, Manus, Muse). |
| **Tool** | A defined action the agent may take (read file, search web, send email). |
| **Function calling / tool use** | The model outputting a structured request to run a tool, which the harness executes. |
| **Tool schema** | The formal description of a tool's inputs so the model knows how to call it. |
| **Structured output** | Forcing the model's answer into an exact format (JSON matching a schema). |
| **MCP (Model Context Protocol)** | The open standard plug that connects AI apps to tools and data. |
| **MCP host** | The AI app the user runs (Claude Code, Cursor). |
| **MCP client** | The connector inside the host that talks to one MCP server. |
| **MCP server** | A small program that exposes a tool or data source over MCP; it has no intelligence. |
| **Resource (MCP)** | Read-only data an MCP server offers. |
| **A2A (Agent2Agent)** | An open protocol for agents from different vendors to find and talk to each other. |
| **Agent Card** | An A2A description of what an agent can do and how to reach it. |
| **Subagent** | A child agent spawned for a bounded job, with its own clean context, that reports back a summary. |
| **Handoff** | Passing control of a conversation from one agent to another (OpenAI Agents SDK). |
| **Orchestration** | Coordinating which agent or step runs when, with what information. |
| **Orchestrator / supervisor** | The agent or code that delegates work to other agents. |
| **Multi-agent system** | Several agents with different roles, tools or prompts working on one goal. |
| **Crew** | CrewAI's name for a team of role-based agents. |
| **Graph / state machine** | LangGraph's way of defining agent flow as nodes (steps) and edges (routes). |
| **State** | The shared data an agent system carries between steps. |
| **Checkpoint** | A saved snapshot of the agent's state so it can resume or rewind. |
| **Durable execution** | An agent run that survives crashes and long pauses by resuming from checkpoints. |
| **Skill** | A packaged, reusable instruction set (often `SKILL.md` plus scripts) that an agent loads only when relevant. |
| **Plugin** | A bundle of tools, skills or commands added to an agent product. |
| **Hook** | Code that runs automatically at set points (before a tool call, after an edit) to enforce rules. |
| **Slash command** | A saved prompt shortcut triggered by `/name`. |
| **Context window** | The maximum amount of text (tokens) the model can consider at once; its working desk. |
| **Token** | A chunk of text (about ¾ of an English word) used to measure input, output and cost. |
| **Context engineering** | Deciding what information the agent sees, when, and in what form. |
| **Context rot** | Quality falling as the context window fills up. |
| **Compaction** | Automatically summarising old conversation to free context space. |
| **Prompt caching** | Reusing already-processed prompt sections so repeat input is cheaper and faster. |
| **System prompt** | The standing instructions that define an agent's role and rules. |
| **Project memory file** | A file like `CLAUDE.md` or `AGENTS.md` loaded every session with project rules. |
| **Memory (long-term)** | Information kept across sessions and retrieved when relevant. |
| **RAG** | Retrieval-augmented generation: fetching relevant documents and adding them to context before answering. |
| **Embedding / vector store** | Numeric fingerprints of text and the database that searches them by meaning. |
| **Agentic search** | The agent finding information itself with search tools (grep, file reads) instead of a pre-built index. |
| **Sandbox** | An isolated environment where agent actions can't harm the real system. |
| **MicroVM** | A lightweight, strongly isolated virtual machine for running untrusted agent code. |
| **Network egress control** | Rules on which outside addresses an agent may send data to. |
| **Approval gate** | A checkpoint where a human must approve before the agent continues. |
| **Human-in-the-loop (HITL)** | Any design where humans review, approve or correct agent actions. |
| **Permission mode** | A setting for how much an agent can do without asking. |
| **Allowlist / denylist** | Lists of actions that are always permitted or always blocked. |
| **Guardrail** | An automatic check that blocks unsafe or off-policy inputs or outputs. |
| **Tripwire** | A guardrail that halts the run immediately when triggered. |
| **Takeover mode** | A human temporarily controlling the agent's browser (login, payment, CAPTCHA). |
| **Computer use / CUA** | An agent operating a GUI by looking at screenshots and sending mouse and keyboard actions. |
| **Browser agent** | An agent that navigates websites (Operator/ChatGPT agent, Mariner, Muse). |
| **Background / async agent** | An agent that works in the cloud while you do other things, then reports back. |
| **Headless mode** | Running an agent from scripts or CI with no interactive interface. |
| **Prompt injection** | Malicious instructions hidden in input that hijack the agent. |
| **Indirect prompt injection** | Injection hidden in content the agent reads (web page, email, document). |
| **Lethal trifecta** | Private data + untrusted content + an outbound channel: the combination that enables data theft. |
| **Tool poisoning** | Malicious instructions hidden in a tool's description. |
| **Blast radius** | How much damage a wrong agent action could cause. |
| **Least privilege** | Giving the agent only the access the task needs. |
| **Trace** | The step-by-step record of an agent run. |
| **Observability** | Being able to see and analyse what agents did, cost and got wrong. |
| **Eval** | A repeatable test that scores agent performance on known tasks. |
| **LLM-as-judge** | Using a model to grade another model's output. |
| **Reward hacking** | An agent meeting the letter of a check while defeating its purpose. |
| **Hallucination** | Confidently stated output that is false. |
| **Reasoning / thinking model** | A model that produces internal step-by-step reasoning before answering. |
| **Extended / interleaved thinking** | Reasoning between tool calls so the agent rethinks after each result. |
| **ACU / credits** | Vendor billing units for agent working time (Devin ACUs, Manus credits). |
| **Fine-tuning** | Further training a model on specific data to change its behaviour. |
| **Vendor lock-in** | Being stuck with one provider because your setup only works there. |
| **Worktree** | A separate git working folder so parallel agents don't collide. |
| **Artifact** | A reviewable output an agent produces (plan, diff, screenshot, report). |

---

# 7. COMMON MISCONCEPTIONS

| # | What learners actually say | Correction |
| :--- | :--- | :--- |
| 1 | "ChatGPT is an agent." | Plain chat is not. ChatGPT *with agent mode* is. The difference is whether it takes actions in a loop. |
| 2 | "The AI runs the code itself." | The model only *writes* a tool request. The harness on a computer runs it. |
| 3 | "MCP is an AI." / "I installed MCP so now I have an agent." | MCP is a connector standard. Without an agent (host) to use it, an MCP server does nothing. |
| 4 | "More agents = better results." | Often worse: more cost, more lost information, more failure points. Start with one. |
| 5 | "Agents learn from every conversation automatically." | The model's weights do not change. "Learning" means writing notes or skills to memory, which only some products (Hermes Agent, memory features) do. |
| 6 | "Bigger context window means it remembers everything." | It can *hold* more but pays less attention to more. Context rot is real. |
| 7 | "Open source means free and private." | An open-source harness calling a paid cloud model still costs money and still sends your data out. |
| 8 | "If it says done, it's done." | Agents falsely report success. Check the evidence (tests, diffs, sources). |
| 9 | "Agents replace developers / staff." | They replace *well-specified tasks*. Someone still has to define, verify and take responsibility. |
| 10 | "Zapier with an AI step is an agent." | Only if the AI step chooses actions in a loop. A fixed pipeline with one AI call is an automation. |
| 11 | "Prompt engineering is the main skill." | For agents, context engineering, tool design and verification matter more. Context scales, prompts do not. |
| 12 | "Sandbox means totally safe." | A sandbox limits damage to files. Network access, credentials and prompt injection can still leak data. |
| 13 | "Approving each step keeps me safe." | Only if you actually read each one. Approval fatigue makes it a formality. |
| 14 | "LangChain is the agent framework." | For production agent control flow it's LangGraph. LangChain is mainly the integration library. |
| 15 | "Cursor and Claude Code are the same thing." | Same purpose, different shape: Cursor is an IDE with an agent inside; Claude Code is a terminal agent that plugs into IDEs. They differ in context handling and pricing. |
| 16 | "Devin/Manus work while I sleep, so no supervision is needed." | Async does not mean unsupervised. Output still needs review. Poorly scoped tasks burn credits. |
| 17 | "Coding agents are only for programmers." | The harness (files + shell + tools) suits any knowledge work. The Claude Agent SDK and Hermes Agent are used for non-coding tasks. Non-programmers still need to be able to check outputs. |
| 18 | "Agents are deterministic like software." | Same input, different runs. Measure pass rates, not single demos. |
| 19 | "The model knows my company." | Only what you put in its context or memory. No SSOT means guessing. |
| 20 | "Hermes is a model." | There are Hermes *models* and *Hermes Agent*, a model-agnostic harness. They are different things. |
| 21 | "Muse is Microsoft's game AI." | In late 2026 "Muse" usually means Meta's personal agent (US-only at launch). Check which one the learner means. |
| 22 | "A demo working once proves it's production-ready." | Production needs evals, traces, cost caps, error handling and security review. |
| 23 | "Agents can access anything on the internet." | Cloud agents are blocked by logins, CAPTCHAs, WAFs and VPNs, and can't reach your intranet. |
| 24 | "More tools make the agent more capable." | Past a point, more tools make tool choice worse. Give the minimum set. |
| 25 | "Agents are expensive / cheap." | Both. Cost depends on loop length and context size. The same task can cost cents or tens of dollars. |
| 26 | "Use an agent for everything." | Most business tasks are better as a fixed workflow or a single prompt. Agents are for open-ended, multi-step work. |

---

# 8. CHOOSING GUIDE

## Step 0: Do you need an agent at all?
Ask these questions in order and stop at the first "yes":
1. **Can one good prompt with the right context do it?** Use chat (ChatGPT, Claude, Gemini) with a project or knowledge file.
2. **Are the steps the same every time?** Use a deterministic workflow (Zapier, Make, n8n, Power Automate), optionally with AI steps inside.
3. **Is the task open-ended, multi-step, and does it need to react to what it finds?** Then use an agent.
4. **Is a wrong action costly and hard to reverse (payments, deletions, client emails, regulated data)?** If yes, use an agent only with approval gates, or don't use one.

## Step 1: Who are the users?
| User | Domain | Recommended |
| :--- | :--- | :--- |
| Non-technical individual, personal errands and research | General | ChatGPT agent mode, Manus, Meta Muse (US only at launch); Claude with connectors |
| Knowledge worker, deliverables (reports, decks, spreadsheets) | General | Manus; Claude/ChatGPT agent features; Claude Code or Cowork-style desktop agents for file-based work (check current availability) |
| Developer, pair-programming in an editor | Coding | Cursor, Antigravity, VS Code + Copilot agent mode |
| Developer, terminal-first, large refactors, scripting | Coding | Claude Code, Codex CLI, Gemini CLI |
| Team clearing a backlog of well-scoped tickets asynchronously | Coding | Devin, Codex Cloud, Jules, Cursor Background Agents, Claude Code in GitHub Actions |
| Developer building a custom agent into a product, single vendor fine | Build | Claude Agent SDK or OpenAI Agents SDK; Google ADK on GCP |
| Complex stateful process needing durability, pauses, audit | Build | LangGraph |
| Fast prototype of a role-based team for business tasks | Build | CrewAI |
| .NET/Java enterprise, Azure shop | Build | Microsoft Agent Framework (Semantic Kernel + AutoGen lineage) |
| Data must never leave the premises; or want model freedom | Build/Run | Hermes Agent + open-weights models on local/self-hosted inference |
| Always-on personal assistant on a server, chat-app access | Run | Hermes Agent (Telegram/Discord) |
| 3D/game creation | Domain | Domain tools (Unity AI and equivalents), not general agents |

## Step 2: Tie-breakers
* **Data sensitivity:** self-hosted open weights first, then an enterprise contract with zero data retention and regional hosting, then consumer SaaS.
* **Need to reach an intranet or VPN:** local agent, or a cloud agent with a private network link. Not consumer cloud browsers.
* **Budget predictability:** subscription over pay-per-token. Tokens with hard caps if you must use the API.
* **Team skill:** no engineers means a product, not a framework. Strong engineers can choose a framework.
* **Avoiding lock-in:** a model-agnostic harness (LangGraph, Hermes Agent, CrewAI, OpenAI Agents SDK with other providers) plus MCP tools plus knowledge kept in portable markdown.
* **Verification available?** If outputs can't be checked automatically (tests, schemas), keep a human gate. If they can, more autonomy is safe.

## Step 3: The autonomy dial
Pick the lowest level that does the job: **suggest** (human acts), then **act with approval each step**, then **act within an allowlist**, then **act fully and report**. Move up one level only after a track record at the current level.

---

# 9. BEST PRACTICES / EXPERT WORKFLOW

## Building
1. **Start with the task, not the platform.** Write the definition of done and how it will be checked before choosing a tool.
2. **Simplest thing first:** prompt, then workflow, then single agent, then multi-agent. Each step up must be justified by a failure you actually saw.
3. **Write the context layer first.** A project memory file (`CLAUDE.md`/`AGENTS.md`): purpose, structure, commands, conventions, don'ts. Keep it short; it costs tokens every session.
4. **Design tools for a model, not for a human:** clear names, precise descriptions, few parameters, informative error messages, concise outputs. Merge many tiny tools into fewer meaningful ones.
5. **Least privilege:** scoped tokens, read-only by default, staging credentials, no production secrets in reach.
6. **Build in verification:** tests, linters, schema validation, a screenshot check, or a separate reviewer agent. An agent that can check its own work is many times more reliable.
7. **Add evals before scaling:** 20–50 real tasks with known-good outcomes, run on every change, tracking pass rate, cost and time.
8. **Instrument everything:** traces from day one.
9. **Put caps on everything:** maximum steps, maximum tokens or cost per run, timeouts, retry limits.

## Running (how experienced users operate)
1. **Explore → Plan → Execute → Verify.** Have the agent read and report first, approve its plan, let it execute, then verify independently.
2. **One task per session; reset often.** Clear context between unrelated tasks. Long sessions rot.
3. **Use subagents for exploration** so the main context stays clean.
4. **Write state to files:** plans, progress logs, checklists and commits act as external memory that survives compaction.
5. **Run agents in parallel safely:** a git worktree or branch per agent, with non-overlapping scopes.
6. **Allowlist the boring actions** (tests, linting, reads) so the approvals that remain are taken seriously.
7. **Review diffs, not summaries.** The summary is the agent's claim; the diff is the evidence.
8. **When it loops, interrupt early.** Redirect with a sharper constraint instead of letting it burn steps.
9. **Turn repeated corrections into permanent context:** each time you correct the same thing twice, add it to the memory file or a skill.
10. **Treat external content as hostile:** extra gates on any action after the agent has read web pages, emails or uploaded files.
11. **Keep a human owner** responsible for every merged or sent output.

## What experts do differently from beginners
| Beginner | Expert |
| :--- | :--- |
| Writes longer prompts | Builds better context (files, rules, skills) and fewer, better tools |
| One giant session | Many short, focused sessions |
| Trusts "done" | Checks evidence |
| Adds agents to fix problems | Removes agents and steps to fix problems |
| Approves everything or nothing | Calibrated allowlists by risk |
| Judges by one demo | Judges by eval pass rate over many runs |
| Ignores cost until the bill arrives | Tracks cost per task and cache hit rate |
| Locks knowledge into one vendor's format | Keeps knowledge in portable markdown; tools via MCP |

---

# 10. TEACHING ANGLES

## Core analogies (Singapore-grounded)
| Concept | Analogy |
| :--- | :--- |
| **Chat vs. agent** | Chat is asking the hawker uncle *how* to make char kway teow. An agent is the uncle cooking it, tasting, adjusting and serving the plate. |
| **Agent loop** | A Grab driver: has a destination, checks the map, drives, sees a jam, reroutes, keeps checking until arrival. Not a fixed MRT line. |
| **Workflow vs. agent** | MRT (fixed track, same stops, very reliable) vs. Grab (picks its route live, flexible, occasionally takes a strange detour). Use MRT when the route never changes. |
| **Model vs. harness** | The model is the chef's brain; the harness is the kitchen: stove, knives, order tickets, food-safety rules. A great chef in no kitchen cooks nothing. |
| **Tools / function calling** | The chef *calls out* "fry two eggs"; the kitchen assistant does it and reports back. The model asks; the harness does. |
| **MCP** | A universal travel adapter, or EZ-Link/SimplyGo: one standard that works across many operators. The card doesn't decide where you go. |
| **MCP vs. A2A** | MCP: an agent plugging into appliances. A2A: two companies' staff using the same email standard to coordinate. |
| **Context window** | The table at a kopitiam: only so much fits. Pile on more and things fall off or get buried under the tissue packets. |
| **Context rot** | A 4-hour meeting: by hour 3 nobody remembers what was agreed at 9 am. |
| **Compaction** | Someone writes the minutes of hour 1–3. Useful, but details get lost. |
| **Project memory file (`CLAUDE.md`)** | The SOP binder at a new job, or a shop's handover notes: read at the start of every shift. |
| **Skills** | Recipe cards in a drawer: only pulled out when that dish is ordered, not all spread on the counter. |
| **Long-term memory** | A regular's kopi order the auntie remembers: kept from visit to visit, not re-explained. |
| **Subagent** | The main contractor sending a sub-contractor to measure the kitchen; only the measurements come back, not the whole site visit story. |
| **Multi-agent orchestration** | A BTO project: architect, contractor, electrician, inspector. Coordination makes or breaks it; more trades means more handover errors. |
| **Sandbox** | A showflat or a driving centre circuit: practise and make mistakes without wrecking a real home or road. |
| **Network egress risk** | A sandbox with a phone line out: the circuit is safe, but the learner could still call someone and give away secrets. |
| **Approval gate** | Singpass 2FA or the bank's OTP before a transfer: the system prepares it, you confirm the high-stakes step. |
| **Approval fatigue** | Clicking "accept" on every cookie banner without reading. |
| **Takeover mode** | The driving instructor's dual brake: the learner drives, the instructor steps in at the critical moment. |
| **Prompt injection** | A scam SMS pretending to be from the bank: instructions hidden in content that look legitimate. The agent, like a trusting relative, may follow them. |
| **Hallucinated success** | The renovation contractor who says "all done" before the paint has dried; you inspect before handover payment. |
| **Reward hacking** | A student who scores full marks by finding the answer key rather than learning; checks must measure the real thing. |
| **Cost blow-up** | A taxi meter left running in a jam: the longer the agent wanders, the higher the fare. |
| **Vendor lock-in** | Buying into one phone ecosystem: chargers, apps and photos all tied in; switching is painful. |
| **Open vs. closed / self-hosted** | Cooking at home (control, effort, ingredients stay home) vs. ordering delivery (easy, but someone else's kitchen handles your food). |
| **Coding vs. general agents** | Coding agents are like PSLE maths with an answer sheet: you can check right or wrong. General agents are like composition: harder to mark, so you need a teacher (human gate). |
| **Autonomy dial** | Learner driver progression: L-plate with instructor, then P-plate, then full licence. Agents earn autonomy the same way. |
| **Evals** | The driving test: the same standard route for everyone, repeated, scored. One good drive isn't a licence. |
| **Traces** | The car's dashcam: when something goes wrong, you replay it to find out why. |

## Mental models to anchor the whole course
1. **"Brain + hands + rules + notebook."** Every agent is a model (brain), tools (hands), a harness with gates (rules) and memory (notebook). Every product in Section 2 is just a different packaging of these four.
2. **"Context scales, prompts do not."** Agents fail mostly from missing or rotten context, not bad wording. This ties straight to your SSOT teaching.
3. **"Trust, but check the receipt."** Every claim of "done" needs evidence: diff, test log, source link, screenshot.
4. **"Smallest machine that does the job."** Prompt, then workflow, then agent, then multi-agent. Climb only when forced.
5. **"Blast radius before autonomy."** Ask "what's the worst this could do?" before "how much can it do?"

## Classroom exercises for adult non-engineers
* **Human agent role-play:** one learner is "the model" (can only speak requests), one is "the harness" (only executes and reports exactly what happened), one is "the user". Doing a task like planning a CNY reunion dinner shows the loop, tool calls and hallucinated success.
* **Spot the injection:** give learners an "email" with a hidden instruction and ask what an agent with email access would do.
* **Agent or workflow? sorting game:** 15 real SME tasks (invoice reminders, competitor research, onboarding emails). Learners sort them into chat, workflow or agent.
* **Write a `CLAUDE.md` for your business:** a one-page SOP for an AI colleague. This connects directly to the SSOT/Foundation Library offer.
* **Autonomy dial card:** for each task, pick suggest / approve / allowlist / full, and justify it by blast radius.

## Pacing note (Gagné alignment)
* *Gain attention:* live demo of an agent completing a task, then of it failing confidently.
* *Recall prior learning:* "You already know ChatGPT; now it gets hands."
* *Present content:* the four-part mental model, then the platforms as packages of it.
* *Guided practice:* the role-play.
* *Assess:* the sorting game plus the autonomy dial.
* *Retention:* the `CLAUDE.md` template they take home.

---

**Before you publish, check these:** all prices, model names and default limits; Meta Muse availability outside the US; current names of Microsoft's merged framework and Anthropic's desktop agent products; and whether Google Antigravity's features match what I described. I didn't re-check those in this session, and they change every few months.