# Perplexity — Perplexity

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** A citation-backed answer engine, model router, and multi-step agent workspace for researchers, knowledge workers, and analysts.

## The product
Perplexity began as a conversational search engine that retrieves live web pages and synthesises answers with numbered inline citations. By late 2026, it has evolved into a three-part suite: the core Search/Deep Research answer engine, the Chromium-based **Comet** browser (which reads and compares open tabs alongside the user), and **Perplexity Computer**, a credit-metered agentic workspace that orchestrates multiple models to execute scheduled or multi-step tasks. Rather than relying solely on its own models, Perplexity acts as an orchestration layer over its in-house `Sonar` family and third-party frontier models.

## Current line-up (November 2026)
- **Modes & Workflows:** Standard **Search** (with **Effort Mode** launched Sept 21, 2026: Light, Standard, High, Ultra), **Deep Research** (multi-step cited reports), **Model Council** (runs 2–8 models in parallel to compare consensus and disagreement), and **Learn Mode**.
- **Perplexity Computer (launched early 2026, updated Oct 5, 2026):** Agent orchestrator coordinating ~19 models with **Automations** (scheduled/event-driven tasks), inline 3D visuals/charts, and **Portable Computer** (local Windows/Linux execution, Sept 2026).
- **Comet Browser (free since Oct 2025; agent upgraded Feb 2026):** Desktop browser with side-panel page synthesis and browser-agent actions.
- **Model Picker (as of Nov 19, 2026):** In-house `Sonar` models plus frontier third-party options for paid tiers (including OpenAI's `GPT-6.2 Sol` and `GPT-6.2 Astra`, and Anthropic's `Claude Opus 4.6` / `Sonnet 4.5`).
- **Developer Platform (`pplx-api`):** `Sonar` search-augmented endpoints and the Apache 2.0 open-weight routing model `pplx-decider-v1.1-27B` (Oct 6, 2026).

## What it's best at / not best at
**Best at:** Fast desk research requiring verifiable links, cross-checking claims across multiple frontier models via Model Council, and synthesising live public web data with uploaded PDFs inside Spaces.
**Not best at:** Deep creative writing, long-form stylistic editing, or working over massive private spreadsheets where deterministic database queries (SQL/Python locally) are required instead of search retrieval.
**Trainer decision rule:** Use Perplexity when your output must be anchored to verifiable external facts or live web sources; switch to a dedicated workspace LLM (like Claude or ChatGPT) when you are drafting, coding, or transforming text you already possess.

## Pricing (November 2026)
- **Free ($0/mo):** Unlimited basic searches (auto-routed `Sonar`), very limited advanced/Pro queries, and access to the Comet browser.
- **Perplexity Pro ($20/mo billed monthly, or ~$16.67/mo at $200/yr; $10/mo Education Pro):** High daily Pro search caps (~400–600/day), manual frontier model selection, Deep Research, Spaces, access to premium data sources (e.g., Statista/PitchBook summaries), and a starter allowance of Computer credits.
- **Perplexity Max ($200/mo):** Unlimited Pro searches, full **Model Council** on web/iOS, priority frontier models, and **Perplexity Computer** with 10,000 monthly agent credits.
- **Enterprise:** **Enterprise Pro** at $40/seat/mo; **Enterprise Max** at $325/seat/mo (adds admin governance, SOC2 controls, and Comet permission management).
- **API (`pplx-api`):** Separate pay-as-you-go billing. Charges $5 per 1,000 requests *plus* token costs (ranging from $0.20/$0.20 per 1M tokens on `Sonar Small Fast` up to $3.00/$15.00 on `Sonar Pro`).
- **Uncertain:** Perplexity frequently A/B tests its pricing pages (some Oct 2026 pages hid the $20 monthly figure in favour of $17/mo annual display) and dynamically adjusts how many Computer credits complex agent runs burn.

## What this actually teaches
**Retrieval-Augmented Generation (RAG) and source verification:** Perplexity is the best vehicle for teaching learners the difference between parametric memory (what a model "remembers" from training) and grounded synthesis (fetching live documents first and generating an answer constrained by citations).

## The student lens
**Mental model:** A fast research intern who reads ten tabs in five seconds and hands you a one-page brief with footnotes—though you still have to click the footnotes to make sure they didn't misread paragraph three.
**Misconceptions:**
- *"If a sentence has a blue citation badge, the fact is 100% true."* → Correction: A citation only proves Perplexity found that webpage; the webpage itself might be unreliable, or the model may have misquoted it.
- *"Choosing the most expensive model in the picker guarantees the best research report."* → Correction: In Perplexity, the *mode* (Search vs. Deep Research vs. Computer) dictates how much evidence is gathered; the *model* mostly changes how the synthesis is written.
- *"My $20 Pro plan gives me unlimited Perplexity Computer automation."* → Correction: Computer runs on metered credits, and heavy browser-agent loops can exhaust a Pro credit allowance quickly.

## The adult educator lens
**Analogy:** Asking a seasoned NLB (National Library Board) reference librarian versus asking a talkative uncle at a kopitiam. The kopitiam uncle (a raw ungrounded chatbot) gives a confident story from memory; the NLB librarian (Perplexity) pulls three current Straits Times clippings and a MAS circular, summarises them, and points to the exact page. *Where it breaks:* A human NLB librarian evaluates the legal authority of a source instinctively, whereas Perplexity will happily cite an outdated SEO blog next to an official `.gov.sg` page if both match the keywords.
**Three-minute demo:** Ask a specific local regulatory question (e.g., *"What are the latest MOM COMPASS point thresholds and exemptions in Singapore as of late 2026?"*). Run it in standard Search, hover over two citations to show one official `mom.gov.sg` source and one third-party consultancy blog, then toggle **Source Filters** or **Model Council** to show how restricting sources changes the reliability of the answer.
**Where it goes wrong in class:** Learners on Free accounts try to follow along with a trainer demonstrating Pro/Max features (like Model Council, Deep Research, or Computer) and immediately hit paywall modals, stalling the workshop.
**Check for understanding:** "You need a two-page competitor brief with verified 2026 pricing links. Which matters more to configure first in Perplexity: switching the model dropdown to `GPT-6.2`, or switching the mode from Search to Deep Research? Why?"

## Watch out
- **Retire stale claims:** Stop calling Perplexity "just a wrapper around GPT-4"—it runs its own `Sonar` and `pplx-decider` models alongside multi-model agent orchestration. Also retire claims that the Comet browser is invite-only or paid (it has been free since late 2025).
- **Do not overclaim:** Never teach that RAG eliminates hallucinations; teach "citation verification" (checking that the cited link actually supports the sentence).
- **Verify before class:** Open the model dropdown 30 minutes before class—Perplexity swaps model version numbers (e.g., `GPT-6.1` to `GPT-6.2`, `Claude 4.5` to `4.6`) every few weeks without warning.

## Sources
1. [Perplexity Help Center — *What advanced AI models are included in my subscription?*](https://www.perplexity.ai/help-center) (Updated 19 November 2026).
2. [The Oxford AI School — *What Are the New Features of Perplexity? (October 2026)*](https://theoxfordaischool.com/) (10 October 2026).
3. [Mem0 — *Perplexity Pricing 2026: Pro, Max, Computer & API Costs*](https://mem0.ai/) (Checked 8 October 2026).
