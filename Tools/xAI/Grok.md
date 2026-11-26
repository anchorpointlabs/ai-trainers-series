# Grok — xAI

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** A frontier multimodal AI assistant, coding companion, and cloud agent tightly bundled with live X (formerly Twitter) firehose data and the Cursor IDE, aimed at real-time researchers, power users, and developers.

## The product
Grok is xAI’s flagship assistant (increasingly branded in documentation under SpaceXSI), accessible via [grok.com](https://grok.com), mobile apps, directly inside the X platform, and through the xAI developer API. It combines general reasoning and code generation with dedicated media generation tools (Grok Imagine) and an autonomous cloud-computer agent called Grok Bot. In October 2026, its commercial model shifted from a standalone chatbot to the anchor of "The X Subscription," a unified bundle combining Grok, X Premium social perks, and the Cursor code editor.

## Current line-up (November 2026)
- **Grok 4.7** (released 21 September 2026): The current recommended flagship model for chat, general reasoning, and coding. Carries a May 2026 training knowledge cut-off. On the Responses API, it defaults to returning encrypted reasoning traces (`reasoning.encrypted_content`).
- **Grok 4.6 & Grok 4.3:** Active legacy models. Following the quiet retirement of the original Grok 4 on 15 May 2026, legacy `grok-4` API calls silently redirect to Grok 4.3 (which offers a 1M-token context window).
- **Grok 4.20 (0309 series / Beta):** Available in Reasoning, Non-Reasoning, and Multi-Agent variants via the API. Note that `logprobs` and `top_logprobs` are unsupported and silently ignored on `grok-4.20` and newer.
- **Dedicated Multimodal & Agent Models:** **Image 2.0** (via Grok Imagine), **Video 1.5** (and Video 1.5 Lite, added November 2026), **Grok Voice API**, and **Grok Build 0.1**.

## What it's best at / not best at
- **Best at:** Tracking breaking events, public sentiment, and niche discourse happening right now via native X Search and Web Search; high-volume developer output where its low 3:1 output-to-input API pricing ratio saves significant budget; all-in-one value for developers already paying for Cursor Pro.
- **Not best at:** High-assurance factual verification from social search (X posts carry high noise and misinformation); fine-grained probability calibration or classification workflows that rely on `logprobs`; predictable consumer budgeting, because usage limits are opaque multipliers rather than transparent message counts.
- **Trainer's decision rule:** Use Grok when your task depends on what people are saying *this hour*, or when you want a single bill for your social feed, daily chatbot, and Cursor coding IDE. Use a competitor when you need verifiable citations from peer-reviewed or institutional sources, or strict enterprise governance.

## Pricing (November 2026)
On 12 October 2026, xAI retired the standalone **SuperGrok** plans (Lite, SuperGrok at $30/mo, Plus, and Heavy at $300/mo) for new buyers, replacing them with **The X Subscription** (existing SuperGrok subscribers are grandfathered):
- **Free ($0/mo):** Limited daily Grok chat/agent requests, standard X, starter Cursor allowance.
- **Plus ($8/mo or $80/yr):** Base usage pool; includes Grok Chat, Voice, Imagine images, Grok Build, Cursor integration, and an X checkmark. Does *not* include Grok Bot or video generation.
- **Premium ($30/mo or $300/yr):** 4x the Plus weekly usage pool. The true entry tier for power users—unlocks **Grok Bot** (cloud agent), video generation, and bundles benefits formerly split across SuperGrok, Cursor Pro, and X Premium+.
- **Super ($100/mo or $1,000/yr):** 15x Plus usage, peak priority, 1080p video.
- **Ultra ($200/mo or $2,000/yr):** 50x Plus usage, access to highest-compute chat models.
- **API Pricing (per 1M tokens):** Separate from consumer plans. **Grok 4.7** and **4.6** cost $2.00 input / $6.00 output. **Grok 4.3** and **Grok 4.20** variants cost $1.25 input / $2.50 output. **Grok Build 0.1** costs $1.00 input / $2.00 output. *Crucial billing rule:* API rates double once a prompt reaches 200,000 tokens.
- **What is uncertain:** xAI does not publish exact message, token, or image counts for the consumer weekly usage pool; "1x" and "4x" multipliers fluctuate dynamically with server load and model choice.

## What this actually teaches
**Live social retrieval is not truth—and parametric memory is separate from search.** Because Grok’s documentation explicitly notes that Grok 4.7 knows nothing past May 2026 unless Web Search or X Search is triggered, it is the single clearest classroom vehicle for teaching learners the difference between what a model *was trained on* versus what its *search tools fetch*, and how noisy real-time social data can poison an answer.

## The student lens
**Mental model:** A brilliant research analyst sitting in the middle of a noisy coffee shop (X), reading shouting matches off a live ticker tape.
**Misconceptions:**
- *"Grok automatically knows today's news because it lives inside X."* → **Correction:** Grok 4.7’s base brain stops at May 2026. Unless Web Search or X Search is active (especially critical to toggle in the API), it has zero access to real-time events.
- *"I need to buy the $30 SuperGrok plan to get Grok."* → **Correction:** SuperGrok is retired for new users. You now buy "The X Subscription," where the $30 **Premium** tier replaces SuperGrok and adds Cursor Pro.
- *"The $8 Plus plan gives me the full Grok experience."* → **Correction:** Plus leaves out the Grok Bot autonomous agent and video generation; those only unlock at the $30 Premium tier.

## The adult educator lens
**Analogy:** The X Subscription is like a telco bundle that combines your home fibre broadband, Singtel TV channels, and a mobile data line into one monthly bill—great value if you actually use X, Grok, and Cursor together, wasteful if you just wanted a basic chatbot. Meanwhile, X Search is like asking the aunties and uncles at a hawker centre about a sudden MRT breakdown: you get eyewitness alerts ten minutes before the official CNA report, alongside three completely made-up rumours. *Where it breaks:* Hawker gossip stays local, whereas Grok pulls from millions of global accounts simultaneously, including coordinated bot nets.
**Three-minute demo:** Ask Grok about a breaking local event from this morning (e.g., an East-West Line delay or a viral Singapore topic) with X Search enabled. Then click into the cited X posts to show learners how the model synthesised raw, unverified public tweets into a confident paragraph.
**Where it goes wrong in class:** Learners without paid accounts hit the opaque weekly usage pool ceiling mid-exercise, or $8 Plus users try to follow along with a Grok Bot agent demo and discover it is paywalled behind the $30 tier.
**Check for understanding:** *"If you call the `grok-4.7` API without enabling server-side search tools and ask who won an election held in October 2026, what happens and why?"* (Answer: It fails or hallucinates, because its knowledge cut-off is May 2026 and live data requires search tools enabled.)

## Watch out
- **Retire stale claims:** Stop referencing Grok-2, Grok-3, or the original `grok-4` as current models (`grok-4` died May 2026). Stop quoting "SuperGrok" or "X Premium+" as current storefront plans (retired 12 October 2026). Stop claiming Grok uses FLUX.1 for images (it now runs xAI’s proprietary Image 2.0 / Grok Imagine stack).
- **Do not overclaim:** Do not pitch Grok as "unfiltered truth." It synthesises social posts rapidly, which means it synthesises rumours rapidly.
- **Verify before class:** Check [x.ai/pricing](https://x.ai/pricing) and [grok.com](https://grok.com) the morning of training. xAI changed its pricing architecture three times over the past year, and model aliases shift silently.

## Sources
1. SpaceXSI / xAI Official Documentation, *Grok Models & Pricing* (Grok 4.7 launch and API specs, dated 21 September 2026).
2. SpaceXSI / xAI Announcement & LumiChats / Suprmind Pricing Registries, *Introducing The X Subscription* (Plan consolidation dated 12 October 2026; verified 15–20 November 2026).
3. BenchLM & AI Pricing Guru Registries, *Grok API Pricing (November 2026): Grok 4.7 Token Rates* (Verified 23–24 November 2026).
