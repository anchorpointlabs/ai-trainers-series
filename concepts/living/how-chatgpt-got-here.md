# How ChatGPT got here: 2022 to 2026

**Tier:** Living · **As at:** 9 November 2026 · **Expires:** the era framework holds for years; the version list holds for roughly one quarter.

**Framework home** — TSC #1 Generative AI Principles and Applications (Basic): *introduction to popular generative AI models, how they work, and industry trends*. This is the entry that makes "trends" teachable instead of a list of names.

![How ChatGPT got here, 2022 to 2026](/home/ubuntu/deliverables/ai-trainer-library/assets/chatgpt-timeline.png)

---

## What actually happened

**30 Nov 2022 — ChatGPT launches** as a free research preview on the GPT-3.5 series. The model was not new; the interface was. A text box that answered in sentences turned a research API into a household product in about a week.

**14 Mar 2023 — GPT-4.** Multimodal input (text and images), 8K and 32K context variants. The first time "attach a diagram" was a reasonable request.

**6 Nov 2023 — GPT-4 Turbo, 128K context, JSON mode, GPTs, Assistants API.** Two things became permanent: context became a budget you manage, and structured output became a product feature rather than a prompting trick.

**13 May 2024 — GPT-4o.** One model handling text, audio and image in and out, 128K context. Voice stopped feeling like a walkie-talkie.

**12 Sep 2024 — o1-preview.** The first reasoning model: it deliberates before answering. This is the moment Chain-of-Thought stopped being only a prompt technique and became an architecture. Everything trainers taught about "think step by step" had to be re-taught as "the model now does this whether you ask or not".

**5 Dec 2024 — o1 full and ChatGPT Pro.** 9 Dec 2024 — Sora goes public. **23 Jan 2025 — Operator**, an agent that uses a browser on your behalf.

**2025 — the GPT-5 generation.** The o-series and the GPT line converge: one system that routes between a fast answer and a slower, thinking one. The visible consequence for users is that "which model am I talking to" becomes invisible, and the invisible consequence is that model choice becomes a routing decision rather than a brand loyalty.

**2026 — the GPT-6 generation, in five releases.** GPT-6 Astra (3 Sep), GPT-6 Sol and Luna as faster and cheaper tiers (22 Sep), GPT-6.1 Sol (29 Sep), GPT-6.1 Terra (26 Oct), and GPT-6 Cyber (5 Nov), a variant built for vulnerability investigation and fix verification. Alongside it: GPT Image 2.6 (4 Nov) and full-duplex voice models that listen and speak at once.

**The other two lines, for contrast.** Anthropic's current lineup is Claude Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5 — 1M-token context across the board, adaptive thinking switched on by default on the top two, knowledge cutoff June 2026, and published retirement commitments into late 2027. Google went Gemini 3 Flash (Dec 2025), Gemini 3.1 Pro (Feb 2026), and by October 2026 Wiz was crediting "Gemini 4 Argon" in its vulnerability research.

## What this actually teaches

Four eras, not twenty version numbers:

1. **Chat (2022–23).** Language as an interface. The skill was asking.
2. **Multimodal and context (2023–24).** Documents, images, audio; windows big enough to paste a report. The skill was supplying.
3. **Reasoning (2024–25).** Deliberation inside the model. The skill was specifying and auditing, not coaxing.
4. **Agents and specialisation (2025–26).** Tools, browsers, security-tuned variants. The skill was scoping and governing.

Teach the eras and you can teach the same lesson in 2027 with different names in the boxes. Teach the version numbers and your slide is wrong by February.

## Why it matters at work

Two practical consequences. **Deprecation is a curriculum problem:** GPT-4o and GPT-4.1 API snapshots shut down on 14 January 2027, o1/o3-mini/o4-mini went on 23 October 2026, and GPT-5.5 was retired from ChatGPT on 14 October 2026. If your exercise depends on a specific model's quirks, it has a shelf life. **And "which model" is now a real decision:** a fast tier, a thinking tier and a security-specialised tier exist side by side, and choosing wrong is a cost or quality problem, not a taste problem.

## The student lens

**Mental model:** the industry is not releasing better chatbots; it is releasing different *kinds of worker* — a fast one, a careful one, a specialist. Version numbers are job titles changing.

**Misconceptions:**
- *"Newer is always better for my task."* Newer is usually more capable and often slower and dearer. Extraction at scale still belongs on a small fast model.
- *"The model I learned on still exists."* Check the deprecation page before you promise a demo.
- *"ChatGPT is one thing."* It is a product wrapping a routing system, plus image, voice, video and agent surfaces that ship on different clocks.

**Five-minute practice:** ask learners to name the last three AI releases they heard about, then place each one in an era. Most will discover they have been tracking brand news, not capability shifts.

## The adult educator lens

**Analogy:** phone generations. Nobody teaches "the iPhone 12"; they teach what changed — camera, battery, screen. Same here: the useful unit is the shift, not the SKU.

**Three-minute demo:** open the deprecation page for one major provider on screen. Let the room read the shutdown dates. Then ask: "what in your workflow depends on a model that has a date on it?" That single page does more for AI literacy than any capability slide.

**Board sketch:** one horizontal line, four bands — CHAT / MULTIMODAL / REASONING / AGENTS — with two or three dots per band and no version numbers at all. Under it: "the dots change; the bands don't."

**Where it goes wrong in class:** someone asks "so which one should I use?" The honest answer is a decision rule, not a brand: smallest model that clears your quality bar, thinking tier only for multi-step judgement, specialised tier only when the risk justifies it.

**Check for understanding:** "Name one thing that changed permanently between 2022 and 2026, and one thing that was true in 2022 and is still true today." (Answer: the interface and the reasoning changed; the model still predicts tokens and still cannot verify itself.)

## Say this out loud

"Four eras, not forty versions. If your slide is a list of model names, it expires faster than your learners' attention."

## Content hook

**LinkedIn opener:** "Everyone can name GPT-6. Almost nobody can say what changed in 2024 that made prompting a different skill."

**Carousel idea:** "Four eras of ChatGPT" — one band per slide, one screenshot per era, no version numbers until the final slide.
