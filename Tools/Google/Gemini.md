# Gemini — Google

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** Google’s flagship multimodal conversational AI and workspace reasoning engine for consumers, developers, and enterprise teams.

## The product
Gemini is both a family of foundation models and the front-end assistant interface (`gemini.google.com`, mobile apps, and the Workspace side panel) that replaced Bard and Duet AI. It natively processes and generates text, code, images, audio, and video within a single architecture rather than bolting separate models together. Its defining operational advantage is deep integration with the Google ecosystem—Drive, Docs, Gmail, Search, and Android—combined with massive context windows (1 million to 2 million+ tokens).

## Current line-up (November 2026)
The Gemini ecosystem has transitioned out of the Gemini 1.5 and 2.0 eras into the Gemini 3 and 4 series:
* **Gemini 3 Flash:** The default high-speed, low-latency workhorse powering the free consumer tier and high-volume API routing. Built for quick synthesis, multimodal transcription, and everyday drafting.
* **Gemini 3.1 Pro:** The mid-to-high tier deep-context model available in Gemini Advanced and Vertex AI / Google AI Studio. Built for large-codebase analysis, multi-document synthesis, and sustained reasoning across 2M+ token contexts.
* **Gemini 4 Argon:** The current frontier model in the lineup (the model generating this text). Engineered for complex multi-step reasoning, agentic tool execution, nuanced instruction adherence, and high-stakes analytical workflows.
* **Gems & Deep Research:** Custom system-prompted personas ("Gems") and autonomous multi-step web research agents ("Deep Research") remain core UI features inside the web app.

## What it's best at / not best at
* **Best at:** Long-context multimodal ingestion (dropping an hour-long raw video, a 300-page PDF, or an entire repository into the prompt), real-time web grounding via Google Search, and pulling live personal/corporate context directly from Google Drive and Gmail via `@` extensions.
* **Not best at:** Strict source-locked compliance (unless explicitly constrained, it blends pre-trained weights and live web search with uploaded files), deterministic formatting across massive outputs without programmatic schema enforcement, and running seamless cross-ecosystem workflows if your organization lives strictly in Microsoft 365.
* **The trainer's decision rule:** Use Gemini when the input is huge, multimodal (video/audio), requires current web search, or lives inside Google Drive; switch to a source-locked workspace (like NotebookLM) when zero external hallucination is non-negotiable.

## Pricing (November 2026)
* **Free tier:** Access to the web and mobile app powered primarily by Gemini 3 Flash, with standard rate limits on image generation and file uploads.
* **Google One AI Premium (~US$19.99 / ~S$28.99 per month):** Unlocks Gemini Advanced (access to Gemini 3.1 Pro and Gemini 4 Argon), 2 TB of cloud storage, and Gemini embedded directly in personal Docs, Gmail, Sheets, and Slides.
* **Google Workspace Business / Enterprise:** Since 2025, Google has largely folded standard Gemini Workspace capabilities into core Business and Enterprise licenses while reserving heavy usage limits or specialized security add-ons for higher tiers. *Trainer note: Enterprise bundling and regional currencies shift frequently; verify current local SKUs before quoting exact seat costs to corporate clients.*
* **API (Google AI Studio / Vertex AI):** Pay-as-you-go per 1M input/output tokens, with caching discounts and higher price brackets for prompts exceeding 128k–200k tokens.

## What this actually teaches
**Ecosystem integration vs. raw model intelligence.** Gemini is the ultimate vehicle for teaching learners that an AI tool's real-world utility depends less on leaderboard benchmarks and more on *frictionless access to your existing data* (email, calendar, cloud docs) and native multimodality.

## The student lens
**Mental model:** A bilingual researcher sitting right inside your Google Drive with a live search bar open—brilliant at connecting everything at once, provided you tell them which drawer to open.

**Misconceptions:**
* *"Because it's Google, every answer is pulled live from Google Search."* — **Correction:** Gemini predicts text from its training weights first and only triggers a live search when its grounding router detects a query needing current facts (or when you force it to).
* *"If I ask it about a file in my Google Drive, it automatically knows all my files."* — **Correction:** It does not index and read your entire Drive in one prompt; you must invoke the `@Google Drive` extension or attach the specific files so it pulls them into the active context window.
* *"A 2-million-token context window means it never forgets or misses details."* — **Correction:** Big context means it can *hold* the whole book, not that it pays equal attention to page 142 and page 1. Needle-in-a-haystack retrieval works well, but dense reasoning across hundreds of pages still degrades without structured prompting.

## The adult educator lens
**Analogy:** Like Singpass auto-filling a government form via MyInfo—its superpower isn't that the form is smarter, it's that it already connects to your existing official records (Gmail, Docs, Drive). *Where it breaks:* MyInfo pulls exact deterministic database fields, whereas Gemini summarises and interprets your Drive files probabilistically and can misread a figure.
**Three-minute demo:** Upload a 3-minute unscripted smartphone video of a messy whiteboard walkthrough (or an MP4 recording of a Zoom meeting) straight into the Gemini prompt. Ask it to extract every visual diagram detail, summarize the spoken disagreements with timestamps, and draft a follow-up email. Watching it process raw video + audio natively breaks the "AI is just text chat" paradigm instantly.
**Where it goes wrong in class:** You tell a corporate class to type `@Google Drive` to pull a sample file, and half the room hits a stone wall because their company IT administrator disabled Workspace extensions, or personal users haven't toggled on the Workspace app connectors in their settings.
**Check for understanding:** *"If you paste a 100-page industry PDF into Gemini and ask a question, where does the answer come from—your PDF, Google Search, or the model's training memory?"* (Correct answer: Any mix of the three, unless you explicitly constrain it or verify its citations.)

## Watch out
* **Stale claims to retire:** Stop referring to "Bard", "Duet AI", "PaLM 2", or saying "Gemini can't generate images of people" (an early 2024 pause long since resolved via Imagen 3/4 updates). Retire references to Gemini 1.5 Pro as the current ceiling.
* **What not to overclaim:** Do not claim Gemini in Google Sheets can replace deterministic Python/Excel macros for auditing large financial tables; conversational side-panels still truncate or hallucinate row-level aggregations if not generating explicit formulas.
* **Verify before class:** Check which exact model names appear in the top-left model dropdown on both free and Advanced accounts that morning, and verify whether Workspace Extensions are enabled on your demo tenant.

## Sources
* [Google Gemini Web App & Release Updates](https://gemini.google.com/updates) — ongoing changelog for consumer and Advanced features (accessed November 2026).
* [Google Workspace Admin Help: Gemini for Google Workspace](https://support.google.com/a/answer/13623623) — licensing, data privacy, and extension governance (updated 2025/2026).
* [Google AI for Developers: Gemini Models Documentation](https://ai.google.dev/gemini-api/docs/models/gemini) — official specifications for context windows and API tiers (accessed November 2026).
