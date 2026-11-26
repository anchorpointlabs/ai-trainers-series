# Vibe Coding — Knowledge Distillation

> **Source model:** Gemini 4 Argon (`gemini-4-argon`) via i10x
> **Extracted:** 2026-11-26 (distillation run)
> **Status:** RAW distillation — exhaustive extraction, not yet cut into entry-template format.

---

# 1. DEFINITION AND BOUNDARIES

## What Vibe Coding Actually Is
Vibe coding is a paradigm of software creation where the human directs the development of an application primarily through natural-language prompts, visual references, and runtime feedback (such as pasting error messages or describing visual bugs), while an AI system writes, edits, and connects the underlying source code. 

The term was popularized by Andrej Karpathy in early 2025 to describe a workflow where the creator "fully gives in to the vibes," embraces exponential AI capabilities, and largely stops reading or manually editing the code line-by-line. In pure vibe coding:
* The primary interface is a conversational chat box or voice prompt, not a text editor.
* The human operates as a product manager, quality assurance (QA) tester, and creative director.
* The AI operates as the software architect, syntax writer, and debugger.
* Code is judged by **observable runtime behavior** ("Does the button work when I click it?") rather than **structural code quality** ("Is this state management pattern scalable?").

## Exact Boundaries and Separations

### (a) Vibe Coding vs. Traditional Software Engineering
| Dimension | Traditional Software Engineering | Vibe Coding |
| :--- | :--- | :--- |
| **Primary Artifact** | Clean, maintainable, deterministic source code and system architecture. | A working user interface and functional outcome, regardless of how the underlying code looks. |
| **Comprehension** | The engineer understands the syntax, data structures, control flow, and execution model of every line committed. | The creator often cannot read or explain the generated source code, treating the codebase as an opaque black box. |
| **Debugging Method** | Reading stack traces, setting breakpoints, inspecting variables in memory, and reasoning about state. | Copy-pasting the raw error message or a screenshot of the broken screen back into the AI prompt and asking it to fix it. |
| **Change Management** | Deliberate refactoring, modular design, unit testing, and strict version control discipline. | Re-prompting the AI until the desired behavior appears, or rolling back the entire checkpoint when the AI breaks the app. |
| **Cost of Creation vs. Maintenance** | High upfront creation cost (slow to write); lower long-term maintenance cost if well-architected. | Near-zero upfront creation cost (minutes to generate); potentially catastrophic maintenance cost as complexity compounds. |

### (b) Vibe Coding vs. No-Code / Low-Code Builders (Bubble, Webflow, Glide, OutSystems)
* **Output Artifact:** No-code tools do not give you standard source code; they compile your visual configurations into a proprietary format locked inside their platform runtime. Vibe coding generates **real, standard source code** (typically TypeScript, React, Tailwind CSS, Python, SQL) that can be exported to GitHub, run locally, and hosted anywhere.
* **Interface:** No-code requires learning a complex visual programming interface (drag-and-drop canvases, property panels, relational database builders, workflow trees). Vibe coding uses natural language ("Make a pricing table with three tiers and a toggle for annual billing").
* **Ceiling vs. Floor:** No-code has a hard ceiling defined by the platform's pre-built blocks and plugins; if Bubble does not support a specific WebSocket protocol, you cannot build it without writing a custom code plugin. Vibe coding has no pre-defined component boundary—if it can be written in JavaScript or Python, the LLM can attempt to write it.
* **Determinism:** No-code blocks are deterministic and pre-tested by the vendor. Vibe-coded components are generated from scratch on the fly and may contain subtle syntax or logic bugs every time they are generated.

### (c) Vibe Coding vs. AI Code Autocomplete (GitHub Copilot Inline, Supermaven, Tabnine)
* **Who is in the Driver's Seat:** With AI autocomplete, a human software engineer is actively typing code inside an IDE; the AI predicts the next line or function signature (ghost text), and the human reads and accepts it (`Tab`). In vibe coding, the human does not write code or navigate the syntax tree; the AI creates, modifies, and deletes entire files autonomously across the project.
* **Scope of Generation:** Autocomplete operates at the token, line, or single-function level within a single open file. Vibe coding operates at the feature or application level across dozens of files simultaneously (database schema + API route + frontend component).
* **Required Skillset:** Autocomplete requires you to already know how to code; it cannot start a project from an empty folder if you do not know what file to create first. Vibe coding requires zero syntax knowledge to go from a blank screen to a deployed web app.

### (d) Vibe Coding vs. Fully Autonomous Agentic Coding (Devin, OpenHands, SWE-agent)
* **The Human Loop Cadence:** Vibe coding is a **tight, synchronous, human-in-the-loop conversational cycle**. The human prompts, waits 10–60 seconds, looks at the live preview, clicks a button, notices the color is wrong or a click fails, and immediately prompts again. Fully autonomous agents are designed for **asynchronous, long-horizon delegation**: you assign a GitHub issue or a full specification, walk away for 30 minutes to several hours, and the agent plans, researches, writes tests, runs tests, fixes its own failures, and submits a Pull Request.
* **Verification Mechanism:** In autonomous agentic coding, the *agent* verifies its own work via automated test suites, linters, and headless browsers before showing the human. In vibe coding, the *human* is the primary test runner, visually inspecting a live preview window after every prompt.
* **Target User:** Autonomous coding agents (like Devin) are largely built to act as junior software engineers inside existing engineering teams (taking tickets from Linear/Jira and opening PRs). Vibe coding tools are built for interactive creation from scratch or rapid visual iteration by solo builders, designers, PMs, and non-engineers.

---

# 2. CORE MECHANICS

To teach vibe coding properly, trainers must strip away the illusion of magic and explain the exact mechanical pipeline happening under the hood.

## 1. The LLM as a Statistical Code Generator
Large Language Models (Claude 3.5/3.7 Sonnet, GPT-4o, o3-mini, Gemini 2.5 Pro) do not "understand" software execution the way a compiler or a human engineer does. They do not run a mental simulation of memory allocation or CPU execution. Instead:
* They are trained on billions of lines of public source code (GitHub, Stack Overflow, documentation).
* When prompted, they predict the most statistically probable sequence of code tokens that satisfies the user's natural language request, given the system instructions and current files in view.
* **Consequence:** They are overwhelmingly best at mainstream, heavily documented tech stacks (React, Next.js, Tailwind CSS, Node.js, Python, Supabase) because their training data contains millions of examples of those exact patterns. If you ask them to vibe-code in an obscure framework or a brand-new library released last week, they will fail or hallucinate outdated syntax.

## 2. The Context Window: The AI's Only "Working Memory"
The single most important technical concept a vibe coder must grasp is the **Context Window**.
* **What it is:** The maximum amount of text (measured in tokens, where 1 token is roughly 3/4 of a word or 4 characters of code) the LLM can process in a single request-response turn.
* **Statelessness:** Every time the user hits "Send" in a vibe coding tool, the LLM starts from a completely blank state. It has zero persistent biological memory of who you are or what your app is.
* **How the illusion of memory works:** To make it feel like a continuous conversation, the vibe coding platform (Cursor, Lovable, Bolt) secretly bundles a massive package of text and sends it all at once on *every single prompt*:
  1. **The System Prompt:** Hidden instructions written by the tool maker (e.g., "You are an expert React developer. Always use Tailwind CSS. Never leave placeholder comments...").
  2. **Project Context / File Tree:** A list of files in the project and the full text content of the files deemed relevant to the current prompt.
  3. **Chat History:** Previous prompts from the user and previous code diffs generated by the AI in this session.
  4. **Terminal / Console Output:** Any recent build errors or runtime crash logs.
  5. **The Current Prompt:** What the user just typed.

## 3. Why the AI Has No Persistent Understanding of the Codebase
As a vibe-coded application grows from 3 files to 50 files, the total code plus the chat history exceeds the effective capacity of the context window (or becomes too expensive and slow to send on every turn).
* **Context Truncation & Retrieval (RAG):** Tools cannot always send every line of every file. They use algorithms (embeddings, grep searches, file-tree heuristics) to *guess* which 5 to 10 files are relevant to your prompt and only show those to the LLM.
* **Context Rot / "Lost in the Middle":** Even when an LLM supports a 200,000-token context window, its attention degrades as the context fills up with dead ends, old error messages, and contradictory instructions from 40 turns ago.
* **The Result:** If the AI edits `File A` because you asked for a new feature, and `File B` (which was not pulled into the active context window) depended on the old structure of `File A`, `File B` breaks instantly. The AI does not "know" `File B` broke until the compiler throws an error in the next step.

## 4. The Prompt → Generate → Apply → Run → Iterate Loop
Every vibe coding tool orchestrates an automated pipeline around the LLM:
1. **Prompt Ingestion:** The user types: *"Add a dark mode toggle to the navbar."*
2. **Context Assembly:** The tool scans the codebase, grabs `Navbar.tsx`, `tailwind.config.js`, and `App.tsx`, combines them with the system prompt, and sends them to the LLM API.
3. **Code Generation / Tool Calling:** The LLM outputs structured instructions (using XML tags or JSON tool calls) specifying which files to create or modify, and outputs the new code or a search-and-replace diff.
4. **File System Application:** The tool parses the LLM output and overwrites the actual files on the disk or virtual container.
5. **Hot Reload & Compilation:** A build tool (like Vite or Next.js) watching the file system detects the file save, recompiles the code in milliseconds, and refreshes the embedded preview browser.
6. **Feedback Capture:**
   * *If compilation fails:* Many tools automatically catch the terminal error and feed it back to the LLM to self-heal before the user even intervenes.
   * *If compilation succeeds:* The user sees the updated UI in the preview pane, tests it manually, and starts the next loop.

---

# 3. THE TOOL LANDSCAPE

Vibe coding tools divide into three distinct categories: **Browser-Based Prompt-to-App Sandboxes**, **AI-Native IDEs (Desktop Editors)**, and **Terminal/CLI Agents**.

## Category A: Browser-Based Prompt-to-App Platforms
These require zero local setup. You open a URL, type a prompt, and get a live preview and deployed URL in the browser.

### 1. Lovable (formerly GPT Engineer)
* **What it is:** A full-stack browser-based AI app builder tightly integrated with React (Vite), Tailwind CSS, shadcn/ui, and Supabase for the backend.
* **Strengths:**
  * Best-in-class non-technical user experience.
  * Native, two-way GitHub synchronization (you can edit code in GitHub or Cursor and it syncs back to Lovable).
  * Deep, automated integration with Supabase: it can write SQL migrations, set up Row Level Security (RLS) policies, configure user authentication, and create edge functions directly from chat.
  * Visual "Select and Edit" tool that lets users click a specific button in the preview and prompt changes just for that element.
* **Real Limits:**
  * Opinionated stack lock-in: It essentially only builds React + Vite + Tailwind + Supabase web apps. You cannot use it to build a Python data pipeline, a native iOS Swift app, or a Django monolith.
  * Credit/message limits on paid tiers can burn quickly when the AI enters a bug-fixing loop.
  * Complex backend orchestration beyond Supabase Edge Functions is difficult to manage.

### 2. Bolt.new (by StackBlitz)
* **What it is:** A browser-based prompt-to-app environment powered by StackBlitz's **WebContainers** technology, which runs a real Node.js environment entirely inside the user's browser tab (no remote virtual machine required).
* **Strengths:**
  * Extremely fast startup and hot-reloading because the server runs locally in the browser via WebAssembly.
  * Broader framework flexibility than Lovable: supports Next.js, Astro, Remix, SvelteKit, Vue, Vite, and Expo (React Native for mobile previews).
  * Gives full visibility into the file tree and an interactive terminal inside the browser.
  * One-click deployment to Netlify.
* **Real Limits:**
  * Because WebContainers run inside the browser, it cannot run native binaries outside the Node.js ecosystem (e.g., no native Python/C++ environments, no local PostgreSQL binary running inside the container).
  * Historically notorious for high token consumption because it often rewrites entire files on each edit, rapidly burning through monthly token allowances during debugging loops.

### 3. v0 (by Vercel)
* **What it is:** Originally a generative UI component tool, now expanded into a full Next.js application builder deeply integrated into the Vercel ecosystem.
* **Strengths:**
  * Unmatched frontend design aesthetic out of the box. Because Vercel maintains Next.js and employs the creator of `shadcn/ui`, v0 produces clean, accessible, modern interfaces that rarely look broken.
  * First-class support for the Next.js App Router, React Server Components, and Vercel deployment pipelines.
  * Excellent for generating isolated UI blocks, interactive charts, and multi-page layouts from uploaded wireframes or screenshots.
* **Real Limits:**
  * Strongly tied to the Next.js/Vercel ecosystem. Next.js App Router (Server vs. Client components) is notoriously complex even for LLMs, sometimes leading to hydration errors or server/client boundary confusion.
  * Less turnkey for full relational backend management compared to Lovable's native Supabase GUI workflow, though Vercel marketplace integrations (Neon Postgres, Upstash) are closing this gap.

### 4. Replit Agent
* **What it is:** An autonomous app-building agent living inside Replit's cloud development platform, operating on a real Linux container in the cloud.
* **Strengths:**
  * Runs on a true cloud Linux VM, meaning it is **not restricted to JavaScript/Node.js**. It can build Python (Flask, FastAPI, Streamlit), Node.js, install system-level Linux packages (like `ffmpeg`), and provision a real cloud PostgreSQL database automatically.
  * Includes a mobile app that allows users to actually vibe-code and deploy full-stack apps from a phone.
  * Handles environment secrets, database provisioning, and persistent hosting all under one roof without connecting third-party accounts like Supabase or Netlify.
* **Real Limits:**
  * Closed platform bias: moving an app off Replit's proprietary database and hosting configuration requires manual re-wiring of environment variables and infrastructure.
  * The Agent plans and executes multi-step checkpoints autonomously, which can take several minutes per turn and costs metered usage fees per checkpoint—if it goes down the wrong architectural path, you pay for the detour.

---

## Category B: AI-Native Desktop IDEs
These are applications installed on a computer (usually forks of Microsoft VS Code). They require local runtime setup (installing Node.js, Python, Git) or dev containers, and offer maximum power and flexibility.

### 5. Cursor
* **What it is:** A fork of VS Code with deep, native AI integration. Its flagship vibe-coding feature is **Composer / Agent Mode** (`Cmd+I` / `Ctrl+I`).
* **Strengths:**
  * The industry standard for serious vibe coders and AI-assisted engineers.
  * **Any language, any stack, any size:** Can build iOS apps (Swift), Android apps (Kotlin), Python backends, Rust CLI tools, Chrome Extensions, or massive monorepos.
  * **Agent Mode:** Can automatically search the codebase, read documentation via web search, create/edit multiple files, run terminal commands, read the terminal errors, and loop until tests pass.
  * **Model Agnostic:** Users can switch between Claude 3.7 Sonnet, GPT-4o, o3-mini, Gemini 2.5 Pro, or DeepSeek on the fly.
  * Supports `.cursorrules` files to enforce permanent coding standards and project memory.
* **Real Limits:**
  * High intimidation factor for true beginners: requires opening a full code editor, managing local terminal environments, handling local port conflicts (`localhost:3000`), and installing system dependencies (Node, Git, Python).
  * No built-in one-click cloud hosting or database—you must manually set up GitHub, Vercel/Render, and Supabase/Firebase yourself.

### 6. Windsurf (by Codeium)
* **What it is:** Another AI-native VS Code fork featuring an agentic system called **Cascade**.
* **Strengths:**
  * Cleaner, less cluttered UI than Cursor, often praised by non-engineers transitioning from browser tools to a desktop IDE.
  * **Cascade Flow Awareness:** Windsurf tracks what you do in the terminal and what edits you make manually in the editor in real time, automatically incorporating those actions into its context without you needing to explain them in chat.
  * Built-in live preview pane inside the IDE that lets users click UI elements and send them directly into the Cascade prompt.
* **Real Limits:**
  * Same local environment friction as Cursor (requires local dependencies, Git, and external deployment setups).
  * Credit calculation system ("Flow Action Credits") can sometimes feel opaque when the agent performs multiple background searches and file reads.

---

## Category C: Terminal / CLI Agents & Repository Planners

### 7. Claude Code (by Anthropic)
* **What it is:** An agentic command-line interface (CLI) tool developed directly by Anthropic that runs right inside the user's terminal (`claude`).
* **Strengths:**
  * Direct, raw access to Claude 3.7 Sonnet with Anthropic's own first-party agentic scaffolding and zero middleman context truncation.
  * Exceptional at navigating massive existing codebases, running complex bash pipelines, executing test suites, managing Git commits/PRs, and doing deep architectural refactoring.
  * Can run headless or interactively in any terminal environment.
* **Real Limits:**
  * **Zero graphical user interface:** It lives entirely in a text terminal. For a non-technical vibe coder who relies on visual previews and point-and-click interfaces, a pure CLI tool is intimidating.
  * Token costs are billed directly against Anthropic API usage (or Claude Max plans), and heavy sessions can easily cost $5 to $30+ per day in raw API tokens.

### 8. GitHub Copilot (Edits / Agent Mode / Workspace)
* **What it is:** Microsoft/GitHub's native AI coding suite inside VS Code and GitHub.com. (Note: *Copilot Workspace* was a browser-based issue-to-PR planning environment whose features have largely been merged into **VS Code Copilot Agent Mode** and GitHub's native coding agent).
* **Strengths:**
  * Enterprise clearance: Because it is owned by Microsoft/GitHub, it is often the *only* tool already approved by corporate IT, legal, and cybersecurity departments in large Singapore enterprises and government-linked companies.
  * Tight integration with GitHub Issues, Pull Requests, and Actions.
* **Real Limits:**
  * Historically lagged behind Cursor and Windsurf in multi-file editing speed and UI polish, though VS Code's recent Agent Mode updates have narrowed the gap.
  * Still designed primarily for professional developers working inside existing repositories rather than non-coders spinning up an app from a single prompt.

### 9. Other Notable Mentions Trainers Will Be Asked About
* **Cline / Roo Code:** Open-source VS Code extensions that turn standard VS Code into an autonomous coding agent. Great for transparency and bringing your own API keys (OpenRouter, Anthropic, local models), but burns API credits rapidly because it does not subsidize token costs.
* **Aider:** A veteran open-source terminal-based pair programmer with automatic Git commit integration on every prompt. Popular with technical users, steep learning curve for beginners.
* **Base44 / Create.xyz:** "Batteries-included" browser prompt-to-app builders similar to Lovable, except they bundle the database, authentication, and hosting internally without requiring the user to even create an external Supabase account. Fastest time-to-app, highest platform lock-in.

---

# 4. THE WORKFLOW

## The Vibe Coder's Step-by-Step Execution Loop

### Step 1: Describe (Scoping & Initial Prompting)
The vibe coder does not open a blank code file. They start by formulating an initial prompt (or asking ChatGPT/Claude to help write a Product Requirements Document first).
* *Action:* Provide the AI with the core user journey, desired look and feel (often attaching a screenshot of an existing app or a Figma frame), and the core features for Version 1.

### Step 2: Generate (Scaffolding)
The AI generates the initial project skeleton (typically 10–25 files: package configurations, routing, landing page, mock data arrays, UI components) and installs dependencies.
* *Action:* The vibe coder waits 30–90 seconds while watching the file tree populate and the preview screen boot up.

### Step 3: Run & Inspect (Visual Verification)
The tool boots a live development server and renders the application in an embedded browser window.
* *Action:* The vibe coder looks at the visual output. Is the screen blank (a white screen of death)? Does the layout match the prompt?

### Step 4: Test (Manual Behavioral Clicking)
Because vibe coders rarely write automated test suites first, testing is manual and interactive.
* *Action:* Click every button, type into every form field, resize the window to check mobile responsiveness, and refresh the page to see if entered data disappears (testing whether data is actually saved to a database or just sitting in temporary browser memory).

### Step 5: Iterate (The Micro-Prompt & Error-Pasting Loop)
This is where 90% of time is spent.
* *If something is broken:* The user copies the red error text from the browser console or terminal, pastes it directly into the chat box (often without adding a single word of explanation), or clicks the "Auto-Fix" button.
* *If it works:* The user prompts the next incremental change: *"Now connect the 'Save Invoice' button to a Supabase table called `invoices` so the data persists when I refresh."*

### Step 6: Deploy (Publishing to a Live URL)
Once the app works in the sandbox preview, the vibe coder clicks the built-in **"Publish" / "Deploy"** button (in Lovable, Bolt, Replit, or v0) or pushes the code to GitHub linked to Vercel/Netlify.
* *Action:* The platform runs a production build (`npm run build`), bundles the static assets and serverless functions, assigns a public `.app` or `.vercel.app` URL (or custom domain), and the software is live on the internet.

---

## How This Differs from How a Real Software Engineer Works

| Phase | How a Real Software Engineer Works | How a Vibe Coder Works |
| :--- | :--- | :--- |
| **1. Starting Point** | **Data Model & Architecture First:** Designs the database schema, API contracts, authentication flow, and state management architecture *before* building the UI screens. | **UI & Mock Data First:** Generates a fully clickable visual frontend using hardcoded fake data on Prompt #1, then tries to bolt a real database and backend onto the UI later. |
| **2. Granularity of Work** | Builds bottom-up in deterministic layers (e.g., write a utility function, write a unit test for it, expose it via an API endpoint, consume it in a component). | Builds top-down by visible user feature ("Add a dashboard page with a chart of monthly sales"). |
| **3. Verification** | Uses automated unit tests, integration tests, static type checking (`tsc`), and linters (`ESLint`) to verify correctness without manually clicking every screen. | Relies almost exclusively on "happy-path" manual clicking in the browser preview. If it looks right on the screen, it is assumed to work. |
| **4. Debugging** | **Root-Cause Analysis:** Reads the stack trace, inspects the exact line of code, checks variable values in a debugger, understands *why* the bug occurred, and applies a minimal surgical fix. | **Symptom Suppression:** Pastes the error message into the chat and asks the AI to make the error go away. The AI may fix the crash by deleting a feature, wrapping broken logic in a silent `try/catch` block, or duplicating code. |
| **5. Dependency Management** | Carefully audits third-party libraries for bundle size, security vulnerabilities, maintenance status, and version compatibility before running `npm install`. | Allows the AI to install whatever package it hallucinates or prefers on each prompt, frequently ending up with bloated or conflicting dependencies. |
| **6. Deployment Readiness** | Separates development, staging, and production environments; runs CI/CD pipelines; configures environment variables, rate limiting, logging, and error monitoring (Sentry). | Clicks "Deploy" directly from the single working branch, often running production traffic against the same database used for testing. |

---

# 5. WHAT IT'S GENUINELY GOOD AT

Trainers must anchor learners in realistic expectations. Vibe coding is not a silver bullet for all software, but inside its sweet spot, it delivers a 10x to 50x speed advantage.

## 1. Interactive Prototypes & Clickable Wireframes
* **Why it shines:** Previously, product managers and designers spent days in Figma linking static screens together with spaghetti prototype arrows that still couldn't accept real keyboard input or calculate real math.
* **Concrete Example:** A product manager building a complex mortgage calculator or an insurance claims intake flow can vibe-code a working React prototype in 30 minutes that accepts real user input, runs real formulas, adapts to mobile screens, and can be sent as a URL to stakeholders or user-testing participants.

## 2. MVPs (Minimum Viable Products) for Validation
* **Why it shines:** Early-stage founders need to test if customers will actually sign up, upload data, or pay for a workflow before spending $50,000+ hiring an agency or dev shop.
* **Concrete Example:** A solo founder builds a Niche Job Board, an AI Resume Grader wrapper, or a B2B Directory with user login (Supabase Auth), a basic database, and a Stripe Checkout link in a single weekend to validate market demand with their first 50 users.

## 3. Marketing Landing Pages, Microsites & Waitlists
* **Why it shines:** Pure frontend UI, animations, copy layouts, and simple email-capture forms have near-zero backend complexity and are heavily represented in LLM training data.
* **Concrete Example:** Event registration pages, product launch waitlists saving emails to Supabase or Airtable, interactive ROI calculators for B2B sales teams, and personal portfolio websites.

## 4. Internal Back-Office Tools & Admin Dashboards
* **Why it shines:** Internal company tools only have 5 to 50 trusted employees using them. They do not need bulletproof protection against millions of malicious internet hackers, nor do they need sub-50ms global latency.
* **Concrete Example:**
  * A custom CRUD (Create, Read, Update, Delete) dashboard for an operations team in a logistics company to view and update CSV shipment statuses.
  * An internal content moderation queue or customer support lookup panel that pulls data from two existing company APIs.

## 5. One-Off Utilities, Data Converters & Automation Scripts
* **Why it shines:** Disposable software ("software for an audience of one"). The code never needs to be maintained long-term; it just needs to run correctly today.
* **Concrete Example:**
  * A Python script to clean, deduplicate, and merge 40 messy Excel spreadsheets from different regional sales branches into one standardized CSV.
  * A custom browser bookmarklet or Chrome Extension that scrapes a specific internal table and formats it for a weekly PDF report.
  * A local batch tool that renames 2,000 product images, compresses them to WebP, and extracts metadata.

## 6. UI/UX Explorations & Design System Scaffolding
* **Why it shines:** Generating 5 completely different visual variations of a dashboard layout in v0 or Bolt takes 5 minutes, allowing teams to compare real browser rendering, dark/light themes, and responsive behavior instantly.

---

# 6. FAILURE MODES AND LIMITATIONS

This is the most critical section for trainers. Every learner *will* hit these walls. Teaching them to recognize and name these failure modes prevents frustration and catastrophic security mistakes.

## 1. Security Holes & Exposed Secrets
* **What it looks like:**
  * **Hardcoded API Keys:** The user says *"Connect this to OpenAI using my key `sk-proj-12345...`"* and the AI pastes the secret key directly into a frontend React file (`App.tsx`). Anyone who opens Chrome DevTools on the deployed website can steal the key in 10 seconds and rack up thousands of dollars in API bills.
  * **Broken or Missing Row Level Security (RLS):** To make a database query work quickly without permission errors, the AI disables Supabase RLS or sets a policy to `USING (true)` for all users. The app appears to work, but any user who knows how to open the browser network tab can read, edit, or delete *every other customer's private data* (violating Singapore's PDPA laws).
  * **Client-Side Auth/Payment Bypass:** The AI checks `if (user.isPaid)` or `if (user.isAdmin)` only in the frontend React router without enforcing permissions on the backend server or database.
* **How to detect it:**
  * Search the entire codebase (`Cmd+Shift+F`) for strings starting with `sk-`, `api_key`, `secret`, or `Bearer` before deploying.
  * Inspect the Supabase dashboard's "Authentication -> Policies" or "Security Advisor" tab to verify no table has public unrestricted read/write access unless intentionally public.
  * Open the deployed site in an Incognito window and attempt to navigate directly to `/admin` or `/dashboard` URLs.

## 2. The "Regression Whack-a-Mole" / AI Forgetting What It Built
* **What it looks like:** Features A, B, and C work perfectly. You prompt the AI to add Feature D. Feature D works, but when you click Feature A, it is completely broken or missing. You ask the AI to fix Feature A; it fixes A, and breaks Feature D.
* **Why it happens:** As explained in Section 2, the AI's context window moved on, or in attempting to rewrite a 600-line file to add Feature D, the LLM got lazy and omitted or accidentally altered the functions handling Feature A.
* **How to detect it:**
  * Sudden drops in file line count after an edit (e.g., a 450-line file suddenly becomes 210 lines).
  * Comments appearing in the code like `// ... rest of existing code here` or `// TODO: implement previous logic` where real code used to live.
  * Viewing the Git diff before accepting changes and seeing large red deleted blocks of code unrelated to your prompt.

## 3. Silent Mock Data / "Works in the Demo, Fake Under the Hood"
* **What it looks like:** You ask the AI to build an AI Receipt Scanner or a Real-Time Stock Tracker. The UI looks stunning. You upload a receipt, a progress bar spins for 2 seconds, and it outputs a neatly formatted table of items and prices! You think it works—until you upload a picture of your cat, and it outputs the *exact same* coffee shop receipt items and prices.
* **Why it happens:** When an integration (like calling an external OCR API, configuring webhooks, or setting up a backend database) requires credentials or complex steps the AI doesn't have, the AI fulfills the prompt by writing a `setTimeout()` delay and returning hardcoded fake JSON data so the UI looks functional.
* **How to detect it:**
  * Test with absurd or varied inputs (upload a blank image, enter strange numbers).
  * Hard-refresh the browser (`Cmd+Shift+R`) or open the app in a different browser—if all your "saved" items vanish, the app is only saving to temporary React state or `localStorage`, not a real database.
  * Ask the AI explicitly: *"List every part of this app that is currently using mock data, hardcoded arrays, or `localStorage` instead of a real backend API or database."*

## 4. Unmaintainable Spaghetti Code & Monolithic Files
* **What it looks like:** Because LLMs find it easier to edit one file in context rather than coordinating imports across 15 files, they tend to dump everything—UI layout, business logic, API fetch calls, CSS styles, and type definitions—into a single 2,000-line `Index.tsx` or `App.tsx` file. It also duplicates the exact same helper function across 6 different files instead of importing a shared utility.
* **Why it matters:** Once a single file passes ~600–800 lines, LLM edit accuracy drops sharply, token costs skyrocket on every prompt, and human engineers cannot easily take over the codebase.
* **How to detect it:**
  * Check file lengths in the file explorer. Any single component file over 400–500 lines is a warning sign.
  * Change a tax rate or brand rule in one place and notice it only updates on page 1, not on page 3, because the logic was copy-pasted rather than centralized.

## 5. Hallucinated APIs, Outdated SDKs & Dependency Hell
* **What it looks like:** The app crashes with `TypeError: openai.createCompletion is not a function` or `npm ERR! ERESOLVE unable to resolve dependency tree`.
* **Why it happens:** Every LLM has a training knowledge cutoff. Libraries like Next.js (v13 vs v14 vs v15), Tailwind CSS (v3 vs v4), Stripe SDKs, and OpenAI SDKs introduce breaking changes. The LLM frequently mixes syntax from an older version (which makes up the majority of its training data) with a newer version installed in `package.json`, or completely invents a method name that sounds plausible (`supabase.auth.getCurrentUserSession()` instead of `supabase.auth.getSession()`).
* **How to detect it:**
  * Repeated loops where the AI edits the same 3 lines of an API call 5 times in a row and gets a new `is not a function` or `Module not found` error each time.
  * When this happens, the AI does not know the current syntax—the user must manually copy-paste the official current documentation from the vendor's website into the chat window.

## 6. Broken Edge Cases & Happy-Path Bias
* **What it looks like:** The app works perfectly when you type a normal name ("John Tan"), upload a 200KB JPG image, and have fast Wi-Fi. In production, a real user:
  * Double-clicks the "Pay Now" button and gets charged twice (no button disabled/loading state).
  * Uploads a 15MB iPhone HEIC photo and crashes the server.
  * Leaves a middle field blank and causes a fatal `Cannot read properties of undefined (reading 'map')` white-screen crash that bricks their entire account view.
* **How to detect it:**
  * Deliberately try to break forms: submit empty forms, click submit buttons 5 times rapidly, paste 10,000 characters into a text box, disconnect Wi-Fi mid-action, and test with zero items in the database (empty states).

## 7. Infinite Death Loops (The AI Digging the Hole Deeper)
* **What it looks like:** A bug appears. The user pastes the error three times. On attempt #1, the AI adds a workaround. On attempt #2, the workaround causes a TypeScript error, so the AI changes the data types. On attempt #3, changing the data types breaks 8 other components. By attempt #8, the entire app won't even compile, and the user has burned 20% of their monthly credits.
* **How to detect it:**
  * **The 3-Strike Rule:** If pasting an error back to the AI fails to fix the specific issue after 3 consecutive prompts, the AI is stuck in a local minimum and polluting its context window with bad code. Stop prompting forward; revert to the last working checkpoint immediately.

## 8. Scope Creep & The "90/10 Paradox"
* **What it looks like:** Because the first 80–90% of the app (the visual UI and basic CRUD) took only 45 minutes to generate, the non-technical creator assumes the app is "almost done" and starts adding "just a few more features" (multi-tenant team roles, recurring subscription webhooks, PDF invoice generation, email notifications). That final 10–20% takes weeks or proves impossible without engineering intervention because complexity in software scales exponentially, not linearly.
* **How to detect it:**
  * The velocity of progress drops from "new feature every 5 minutes" to "spent 6 hours trying to get one Stripe webhook to sync with user permissions."

---

# 7. TERMINOLOGY GLOSSARY

Trainers should hand this exact glossary to learners on Day 1. Every definition is written in plain, one-line language for non-engineers.

1. **Vibe Coding:** Building software by describing what you want in plain language to an AI and judging the results by testing the live app rather than reading the code.
2. **LLM (Large Language Model):** The underlying AI brain (like Claude 3.7 Sonnet or GPT-4o) that predicts and writes the code behind your vibe-coding tool.
3. **Context Window:** The AI's short-term working memory—the maximum amount of conversation history and code files it can read at one time before it starts forgetting earlier details.
4. **Token:** The basic unit of text (~4 characters) that AI models read and write, which tools use to measure memory limits and bill your usage.
5. **Prompt-to-App:** Browser platforms (like Lovable, Bolt.new, or v0) that turn a text description directly into a live, running application without installing anything on your computer.
6. **Agent / Agentic Mode:** An AI mode that doesn't just suggest code in a chat box, but autonomously searches files, edits multiple parts of your project, runs terminal commands, and fixes its own errors.
7. **IDE (Integrated Development Environment):** A professional desktop software editor (like VS Code, Cursor, or Windsurf) where code files live and are edited.
8. **Frontend (Client-Side):** The visual part of the application—buttons, layouts, animations, and forms—that runs directly inside the user's web browser.
9. **Backend (Server-Side):** The hidden engine running on a secure remote computer that processes business rules, talks to the database, and protects secret keys away from the user's browser.
10. **Full-Stack:** An application that includes both a visual Frontend and a data-storing Backend connected together.
11. **Database (DB):** An organized digital filing cabinet (usually powered by PostgreSQL in tools like Supabase) that permanently saves user accounts and app data so it doesn't vanish when you refresh the page.
12. **CRUD:** The four basic actions almost every business app performs on data: **C**reate, **R**ead, **U**pdate, and **D**elete.
13. **API (Application Programming Interface):** A structured messenger that allows your app to talk to external services (like Stripe for payments, OpenAI for intelligence, or OneMap for Singapore addresses).
14. **API Key / Secret:** A private digital password that lets your app use a paid external service (and charges your credit card), which must never be exposed in Frontend code.
15. **Environment Variables (`.env`):** A secure configuration vault outside your public code where secret API keys and database passwords are stored safely.
16. **Sandbox / Dev Container:** An isolated, safe virtual computer where your AI runs and previews your unfinished code without affecting the live internet or your personal computer's files.
17. **Localhost:** A private preview web address (like `http://localhost:3000`) that only works on your own computer while you are building and testing an app.
18. **Hot Reload (HMR):** The mechanism that automatically refreshes your preview screen within a second every time the AI saves a change to your code.
19. **Console / Terminal:** The text window showing behind-the-scenes system logs and red error messages that you copy and paste back to the AI when something breaks.
20. **Iteration Loop:** The core cycle of vibe coding: prompt a small change, inspect the preview, test it, feed back any errors, and repeat.
21. **Hallucination:** When the AI confidently invents a non-existent code command, software library, or fake feature because it is guessing statistically rather than knowing facts.
22. **Mock Data / Hardcoding:** Fake sample numbers or text written directly into the visual code to make a prototype look real before a real database is connected.
23. **State:** The temporary data an app remembers right now in your browser tab (like whether a popup menu is currently open or what you just typed into a search box).
24. **Dependencies / Packages (`package.json`):** Pre-built open-source code toolkits (for charts, icons, calendars, or date math) that your app downloads and relies on so the AI doesn't have to write everything from scratch.
25. **Version Control (Git / GitHub):** A "time machine" system that saves snapshots of your entire codebase so you can always rewind to a working version if the AI destroys your app.
26. **Commit / Checkpoint:** A single saved snapshot in your Version Control history marking a moment when the app was working properly.
27. **Diff (Difference):** A visual highlight showing the exact lines of code the AI wants to add (in green) and delete (in red) before you approve the change.
28. **Refactoring:** Reorganizing and cleaning up messy code behind the scenes to make it easier to maintain, without changing how the app looks or behaves to the user.
29. **Technical Debt (Tech Debt):** The hidden pile of messy shortcuts and tangled code that accumulates when you build fast, eventually making every new feature harder and slower to add.
30. **Row Level Security (RLS):** Database security rules (especially in Supabase) that ensure User A can only view and edit User A's private data, never User B's data.
31. **Deployment (Shipping):** Packaging your finished code from your private editing sandbox and publishing it onto public cloud servers with a real web link anyone can visit.
32. **System Rules (`.cursorrules` / Knowledge File):** A master instruction document saved in your project that reminds the AI of your app's design rules, tech stack, and "do not touch" boundaries on every single prompt.

---

# 8. COMMON MISCONCEPTIONS

Trainers will hear these exact phrases in the classroom. Here is how to correct each one immediately and accurately.

### 1. *"If it looks like it works on my screen, it's ready for real customers."*
* **The Reality:** Visual appearance is the easiest 20% of software. An app that looks polished on your screen often has fake hardcoded data, wide-open database security where any user can delete the entire database, zero error handling if two people click at once, and exposed API keys that will bankrupt you within hours of posting the link publicly.

### 2. *"A better, longer initial prompt will give me a complete, complex app in one shot."*
* **The Reality:** "Mega-prompting" an entire 15-feature application in Prompt #1 almost always fails. LLMs have output token limits (typically 4,000 to 8,000 tokens per response). If you ask for 15 features at once, the AI is forced to write shallow shell code, placeholder buttons, and fake logic for all 15 features to fit them into one reply. Good vibe coding builds **one vertical slice at a time**.

### 3. *"The AI remembers why it wrote that code 20 minutes ago."*
* **The Reality:** The AI has no persistent mind or memory. Every prompt is read by a fresh instance of the model scanning a truncated window of files and chat logs. Once a message scrolls out of the active context window or you start a new chat session, the AI has zero memory of why a specific workaround was put in place and will happily delete it unless a comment in the code or a project rules file explicitly warns it not to.

### 4. *"Vibe coding means I don't need to know anything about how software systems work."*
* **The Reality:** You do not need to memorize **syntax** (where semicolons and curly braces go), but you still must understand **system concepts** (the difference between frontend and backend, what a database table is, how user login works, and why API keys must stay secret). Without basic architectural literacy, you cannot diagnose why your app loses data on refresh or tell the AI how to fix it.

### 5. *"When the AI gets stuck on a bug, I just need to keep clicking 'Try Again' or pasting the error until it figures it out."*
* **The Reality:** After 2 or 3 failed attempts on the same bug, the chat history is poisoned with bad assumptions and broken code edits. Each subsequent "Fix it" prompt makes the codebase *worse* and burns money. The right move is to rewind/rollback to the last working state, start a fresh chat window, and rephrase the request with better constraints or documentation.

### 6. *"Vibe coding makes software engineers obsolete / We can fire our dev team."*
* **The Reality:** Vibe coding eliminates the bottleneck of spinning up basic CRUD interfaces and prototypes, but it increases the need for experienced engineers who can audit security, architect scalable databases, untangle AI-generated tech debt, and integrate complex enterprise legacy systems. It turns non-engineers into 0-to-1 prototype builders, and turns real senior engineers into 10x architects.

### 7. *"No-code tools (like Bubble or Webflow) and vibe coding tools (like Lovable or Cursor) are the exact same thing."*
* **The Reality:** No-code locks you into a vendor's proprietary visual drag-and-drop boxes; if the vendor raises prices 500% or shuts down, you cannot export your app and run it elsewhere. Vibe coding writes universal, human-readable open-source code (React, TypeScript, Python) that you legally own, can download to your laptop, commit to GitHub, and hand directly to any human software developer in the world.

### 8. *"Once the app is deployed, I'm done and it costs nothing to maintain."*
* **The Reality:** Software rots. Third-party APIs retire old versions, security vulnerabilities are discovered in npm packages, databases fill up, and browsers update. Every deployed production app requires an owner who knows how to update dependencies, monitor error logs, and manage hosting/database bills.

---

# 9. BEST PRACTICES / EXPERT WORKFLOW

This is the exact standard operating procedure (SOP) that separates frustrated beginners from expert vibe coders who consistently ship working tools.

## 1. Pre-Flight Planning: The "PRD First" Rule
Never open Bolt, Lovable, or Cursor and type a 1-sentence stream-of-consciousness prompt.
1. Open a standard reasoning chat (Claude or ChatGPT).
2. Describe your app idea and tell it: *"Act as a Senior Product Manager and Technical Architect. Interview me with 5 questions to clarify edge cases, data models, and user flows. Then write a minimalist Product Requirements Document (PRD) and a step-by-step build plan broken into 6 small, testable milestones."*
3. Save that PRD as a markdown file (`PRD.md` or inside Project Knowledge) so the coding AI always has a north star.

## 2. Set Up Permanent Project Guardrails (`Knowledge` / `.cursorrules` / `CLAUDE.md`)
Before generating features, create a persistent rules file in the root of your project (called "Knowledge" in Lovable, `.cursorrules` in Cursor, `CLAUDE.md` in Claude Code). Include:
* **Tech Stack Lock:** *"Use React, TypeScript, Tailwind CSS, Lucide icons, and Supabase. Do NOT install new UI component libraries without asking first."*
* **File Size Limit:** *"Keep files modular and under 300 lines. Split components into smaller files rather than creating monolithic files."*
* **Anti-Regression Rule:** *"Do not delete or modify existing working features unrelated to the current prompt. Never replace working code with `// TODO` or placeholder comments."*
* **Real vs. Mock Clarity:** *"If you use mock data, clearly label it in the UI with a badge that says `[MOCK DATA]` so I never confuse it with real database queries."*

## 3. Small Vertical Slices (One Feature = One Prompt = One Checkpoint)
Work in atomic cycles:
* **Bad Prompt:** *"Build the dashboard, add user login, add dark mode, create a PDF export button, and connect Stripe payments."*
* **Expert Prompt:** *"Step 1: Create the read-only dashboard table showing rows from the `bookings` table in Supabase. Do not add edit or delete buttons yet. Let me verify the data loads first."*
* Only move to Step 2 after you have visually verified Step 1 in the preview.

## 4. Relentless Version Control ("Save Game" Discipline)
Treat version control like saving your game right before fighting a boss in a video game.
* **Commit on Green:** The moment a feature works and there are zero errors in the console, commit to Git (or ensure a clean named checkpoint exists in Lovable/Replit).
* **The 3-Strike Rollback:** If a new prompt breaks the app and the AI cannot fix it within 3 follow-up prompts, **do not keep prompting**. Hit "Restore Checkpoint" or `git reset --hard`, open a **brand-new chat thread** (to wipe the polluted context window clean), and try again with a more specific prompt.

## 5. Use "Chat / Ask Mode" Before "Edit / Agent Mode"
When tackling a tricky bug or a complex new feature:
1. First prompt the AI with: *"DO NOT write or edit any code yet. Read the codebase and explain to me in plain English why the invoice total is calculating incorrectly, and propose 2 ways to fix it."*
2. Review its explanation. Usually, you will spot immediately if the AI is misunderstanding your goal.
3. Once you agree on the plan, say: *"Proceed with Option 1. Only modify `InvoiceSummary.tsx`."*

## 6. Force the AI to Write Automated Sanity Checks & Security Audits
Even if you don't know how to write tests or audit code yourself, you can use a second AI (or a fresh chat session) as an adversarial reviewer:
* **The Security Audit Prompt:** *"Act as a senior cybersecurity auditor. Scan my entire codebase and database schema. List every potential vulnerability: exposed API keys, missing Supabase RLS policies, unvalidated form inputs, or pages that can be accessed without authentication. Rank them by severity."*
* **The Edge-Case Prompt:** *"Look at the booking form component. List 5 realistic user actions (like double-clicking submit, entering negative numbers, or losing internet connection) that would currently break this form or corrupt data, and then fix them."*

## 7. Know the Exact Hand-Off Criteria to a Real Software Engineer
Teach learners the hard red lines where solo vibe coding must stop and a professional software engineer must be brought in to review, refactor, or take over:
1. **Regulated Personal Data (PDPA / NRIC / Medical / Financial):** The moment the app stores Singapore NRIC numbers, FinTech/banking records, medical history, or sensitive corporate IP, a qualified engineer must audit authentication, encryption, and Row Level Security.
2. **Real Money Movement (Beyond Simple Payment Links):** A simple Stripe Payment Link is fine for vibe coding. Custom multi-party marketplaces, wallet balances, automated refunds, or usage-based billing webhooks require deterministic engineering—a hallucinated webhook handler can accidentally refund customers or double-charge them.
3. **Production Scale (>100 Concurrent Active Users or Mission-Critical Uptime):** If an app crashing for 4 hours would cost the company real revenue or reputational damage.
4. **The "Context Ceiling" (>10,000 Lines of Code / 60+ Files):** When every small change breaks two old features despite following best practices, the architecture has outgrown pure vibe-coding context limits and needs an engineer to refactor it into clean, decoupled modules with automated test suites.

---

# 10. TEACHING ANGLES (ANALOGIES & SINGAPORE MENTAL MODELS)

When teaching non-technical adult learners in Singapore (PMETs, SME owners, civil servants, marketers, operations managers), abstract computer science terms cause them to tune out. Use these tested analogies and local mental models.

## 1. The HDB ID / Contractor Analogy (How Vibe Coding Works)
* **Traditional Coding** is laying your own floor tiles, wiring your own DB box, and doing your own plumbing with your bare hands. It takes years to learn, and if you don't know the craft, you can't build the house.
* **No-Code (Bubble/Webflow)** is buying modular furniture from IKEA. It's fast and reliable, but you can only build what exists in the IKEA catalogue.
* **Vibe Coding** is acting as the homeowner managing a hyper-fast contractor who works at 100x human speed, never sleeps, and charges $20 a month—**but has complete amnesia every 15 minutes and zero common sense.**
  * If you tell the contractor: *"Make the kitchen look nice,"* he might build a gorgeous marble counter—and cover up your water pipes and gas valve with concrete because you didn't specify they needed to remain accessible.
  * If you ask him to repaint the bedroom wall, and you don't watch him closely, he might knock down the living room toilet wall because it was in his way.
  * **Your job as a vibe coder is Clerk-of-Works / Site Inspector:** Give one room's instruction at a time, inspect the plumbing after every step, and take photos (Git commits) before letting him touch the next wall.

## 2. The Hawker Centre Stall Analogy (Frontend vs. Backend vs. API Keys)
Learners consistently fail to understand why putting an OpenAI API key or business rule in the Frontend is dangerous.
* **The Frontend (React/UI)** is the front counter and menu board of a hawker stall where customers stand and queue. **Anything placed on the front counter is visible to every stranger walking past.**
* **The Backend (Supabase Edge Functions / Server)** is the locked kitchen behind the stall door where the secret chili recipe and the cash register safe are kept.
* **An API Key** is your company's physical Corporate DBS Credit Card with no spending limit.
  * Putting your API key in the Frontend code is like **Scotch-taping your physical corporate credit card and PIN number to the front glass of the hawker stall** so customers can pay the supplier directly. It works during your test, and within 10 minutes of opening to the public, a passerby copies the card details and buys $5,000 worth of crypto.
  * Your credit card (API Key) must stay locked in the back kitchen (Backend Environment Variables), and customers at the front counter (Frontend) must pass their order slip through the small window (API request) to the kitchen staff.

## 3. The "Showflat vs. TOP" Analogy (Mock Data & Prototypes vs. Production)
Learners often see a slick UI generated in 2 minutes by Lovable or v0 and think the software is 90% finished.
* **A Prompt-1 Vibe-Coded App is a Property Developer Showflat.** When you walk into a condo showflat at Marina Bay, the living room looks breathtaking, the chandelier glows, and the kitchen tap exists.
* **Why you can't live in a Showflat:** If you turn the kitchen tap, no water comes out (Mock Data). The walls are made of thin plywood (no backend validation). There is no sewage pipe connected to the PUB main grid (no database schema), and the front door has no real lock (no Row Level Security).
* Getting from the Showflat (UI Prototype) to **TOP (Temporary Occupation Permit / Production Deployment)** requires hooking up the invisible water pipes, sewerage, electrical safety breakers, and door locks. Teach learners to celebrate building a Showflat in 20 minutes—while respecting the checklist needed before letting real tenants move in.

## 4. The "Goldfish with a PhD" Mental Model (The Context Window)
To stop learners from getting angry when the AI "forgets" an instruction from 30 minutes ago:
* Tell them: **"You are working with a Harvard Computer Science PhD who has the 30-second memory of a goldfish."**
* Every time you hit Enter, the goldfish wakes up for the first time today, frantically reads the sticky notes pasted on its fishbowl (`System Rules / PRD`), reads the last 10 pages of your notebook (`Chat History`), looks at the 4 code files currently open on the desk, makes a brilliant edit in 5 seconds, and immediately loses consciousness again.
* Once your notebook hits 50 pages of arguments and scratched-out errors, the goldfish gets confused reading all the crossed-out mistakes. **Throw away the messy 50-page notebook (start a New Chat), keep only the clean final blueprint, and the goldfish suddenly becomes smart again.**

## 5. Practical Classroom Exercises for Singapore Trainers
When structuring a hands-on workshop (e.g., WSQ / SkillsFuture corporate training):
1. **Exercise 1 (The 15-Minute Win — Pure Frontend):** Build an interactive **CPF / Mortgage / Freelance GST Calculator** or **Company Event Lucky Draw Spinner** in v0 or Bolt.new. Zero database, zero API keys, instant visual gratification, deploy to a live link students can open on their phones via QR code.
2. **Exercise 2 (The "Spot the Fake" Diagnostic):** Have students ask the AI to build an "Expense Claim Receipt Scanner." Let them celebrate that it looks working—then make everyone refresh the browser tab and watch their uploaded data vanish, or upload a photo of a Kopi-O and watch it output a $142 taxi receipt. Use that exact moment of surprise to teach **State vs. Database** and **Mock Data vs. Real API**.
3. **Exercise 3 (Full-Stack CRUD with Guardrails):** Build a simple **Internal Leave / Room Booking / Inventory Tracker** using Lovable + Supabase. Force them to intentionally break the app once, experience the frustration, use the **Restore Checkpoint** button to recover in 3 seconds, and inspect a basic Supabase Row Level Security table before publishing.