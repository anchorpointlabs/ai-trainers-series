# Meta AI — Meta

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** Meta’s dual-track AI ecosystem comprising the free social-app assistant ([meta.ai](https://meta.ai), WhatsApp, Instagram, Facebook), the standalone **Meta Muse** personal cloud agent, and the underlying **Muse** (mostly closed) and **Llama 4** (open-weight) model families.

## The product
For two years, "Meta AI" simply meant a free chatbot powered by open-weight Llama models tucked inside WhatsApp and Instagram search bars. In 2026, Meta executed a major strategic pivot: Meta Superintelligence Labs launched the **Muse** model family in April 2026, moving its frontier work toward proprietary, hosted agentic systems while keeping a select open-weight track. Today, users encounter Meta AI either as the free everyday social assistant (running on Muse Spark 1.1+) or as **Meta Muse** ([muse.ai](https://muse.ai), iOS/Android, and a macOS desktop app), a paid personal agent that runs inside a cloud virtual machine ("Muse Secure VM") to automate shopping, travel, calendar, and local Mac file tasks.

## Current line-up (November 2026)
Meta’s line-up is split between the new proprietary **Muse** frontier line and the open-weight **Muse Open / Llama 4** herd:
- **Muse Spark 1.3** (released 2 September 2026): Flagship closed-weight multimodal model (text, image, audio, video, PDF) with a 1M-token context window (131K max output), built for long-horizon agentic coding and multi-step execution via the **Muse Code** harness. Succeeds Muse Spark 1.0 (April 2026) and 1.1 (which took over [meta.ai](https://meta.ai) in July 2026).
- **Muse Wonder** (released October 2026) & **Muse Ember** (released 9 November 2026): Closed hosted models; Wonder sits at the top capability tier, while Ember is Meta's smallest, lowest-cost efficiency model.
- **Muse Image & Muse Video** (launched 7 July 2026): Dedicated media generation inside Meta AI.
- **Muse Spark Open** (15 October 2026) & **Muse Glimmer** (August 2026): Meta’s new open-weight releases. Spark Open is an 816B total / ~42B active Mixture-of-Experts (MoE) model with a 1M context window; Glimmer is a 30B model licensed under Apache 2.0 that fits on a single consumer GPU.
- **Llama 4 Scout & Llama 4 Maverick** (released 5 April 2025; no new Llama-branded models have shipped since): Open-weight MoE models (both 17B active parameters; Scout is 109B total with a 10M-token context window; Maverick is 400B total with a 1M context window). *Note:* The ~2T parameter **Llama 4 Behemoth** was announced as a distillation teacher in April 2025 but never publicly released.

## What it's best at / not best at
- **Best at:** Zero-friction availability inside apps 4 billion people already open daily (WhatsApp, Instagram); background consumer life-admin and shopping via the Meta Muse agent (and shared "Muse Spaces", launched 6 November 2026); massive-context local or self-hosted deployments using Llama 4 Scout (10M tokens) or Muse Spark Open.
- **Not best at:** Default data privacy. Both the consumer Muse app and the developer API carry aggressive default training-on-user-data traps that must be manually avoided. Also erratic on complex multi-site travel booking in the consumer agent.
- **Trainer's decision rule:** Use Meta AI in WhatsApp for quick, casual group-chat assistance; use open-weight Llama 4 Scout or Muse Spark Open on your own servers when you need 1M–10M context windows without sending data to a frontier lab; use the Muse Spark 1.3 API for long-horizon coding agents *only* after auditing your API model ID string for privacy compliance.

## Pricing (November 2026)
- **Meta AI Social Assistant ([meta.ai](https://meta.ai), WhatsApp, IG, FB):** Free ($0).
- **Meta Muse Consumer Agent ([muse.ai](https://muse.ai) & apps):** Billed by weekly token allowances rather than message counts:
  - **Free ($0/mo):** Weekly usage cap (pauses when hit; a single heavy ticket-shopping or report task can consume 10%+ of the weekly pool).
  - **Muse Power ($20/mo):** 500 million Muse tokens per week.
  - **Muse Maximum ($100/mo):** 3 billion Muse tokens per week.
- **Hosted Muse API Pricing (per 1M tokens):**
  - **Muse Spark 1.3 (`muse-spark-1.3`):** $1.25 input ($0.15 cached input) / $4.25 output. Also offered as a discounted **`muse-spark-1.3-contributor`** SKU that trains on your prompts and completions.
  - **Muse Ember:** $0.30 input ($0.012 cached input) / $1.50 output.
- **Open-Weight Models (Llama 4 / Muse Spark Open / Glimmer):** Free to download and self-host (Llama 4 carries the 700M-monthly-active-user commercial threshold; Muse Glimmer is Apache 2.0). Via third-party hosts like OpenRouter (as of November 2026): Llama 4 Scout is ~$0.10/$0.30, Maverick is ~$0.19/$0.65, and Muse Spark Open is ~$1.25/$4.25 per 1M tokens.
- **What is uncertain:** Meta does not disclose the exact weekly token ceiling on the Muse Free tier, and regional rollout of the standalone Muse agent outside North America (with reports of Singapore and Japan access) remains fluid.

## What this actually teaches
**"Open weights" vs. "Hosted service"—and how data-training defaults hide in the fine print.** Meta’s 2026 split between open weights (Llama 4 / Muse Open) and closed agent services (Muse Spark 1.3) is the richest real-world case study for teaching learners that *who runs the model* and *which exact SKU string an app calls* determines whether your confidential data stays private or becomes training fuel.

## The student lens
**Mental model:** Meta used to only give away free recipe books (Llama open weights) so anyone could cook at home; in 2026, they opened a high-end automated catering service (Muse) where the chefs cook for you in their kitchen—and memorise your family recipes unless you explicitly tell them not to.
**Misconceptions:**
- *"Meta's AI is 100% open-source and free."* → **Correction:** That ended in April 2026. While Llama 4 and Muse Glimmer/Spark Open are open-weight, Meta's main models powering its assistant and API (`Muse Spark 1.3`, `Muse Wonder`, `Muse Ember`) are closed, proprietary, and paid up to $100/month.
- *"Meta AI is still running on Llama 3 or Llama 4."* → **Correction:** No new Llama model has shipped since April 2025. Meta replaced Llama inside its consumer chatbots with **Muse Spark** between April and July 2026.
- *"If I use the Muse API or connect Muse to my Mac, my work data is automatically private."* → **Correction:** In the Muse consumer app, connected services train Meta's models by default unless switched off in Data Controls. In the API, calling `muse-spark-1.3-contributor` explicitly trades your prompt data for a lower token price.

## The adult educator lens
**Analogy:** Using open-weight Llama 4 Scout or Muse Glimmer on your own server is like buying an appliance from Harvey Norman and plugging it into your own HDB flat—nobody outside your flat sees what you cook. Using Meta AI in WhatsApp or the Meta Muse cloud agent is like eating at a food court where you pay with a loyalty app that tracks every dish you order to optimise the stall's menu—and in the API, the `-contributor` SKU is like accepting a 20% discount voucher in exchange for letting the stall film your table. *Where it breaks:* A food court cannot copy your work documents, whereas the macOS Muse agent can read local files if granted folder permissions without turning off Data Controls.
**Three-minute demo:** Open two tabs side-by-side: show the Muse API pricing table highlighting `muse-spark-1.3` vs. `muse-spark-1.3-contributor` (and the Muse app's Data Controls toggle), then contrast it with a self-hosted or zero-retention OpenRouter call to `Llama 4 Scout` processing a 500-page PDF inside its 10M-token window.
**Where it goes wrong in class:** Learners outside supported regions hit geo-blocks when trying to install the standalone Meta Muse agent, or learners blow through their entire weekly Muse Free token quota in a single multi-step shopping prompt during the first ten minutes of a lab.
**Check for understanding:** *"A developer in your company says, 'We're using Meta's latest AI model, so it's open-source and our data stays private.' What two questions must you ask them immediately?"* (Answer: 1. Are we self-hosting open weights like Llama 4 Scout / Muse Spark Open, or calling the closed Muse Spark 1.3 cloud API? 2. If calling the API or app, did we avoid the `-contributor` SKU and disable training in Data Controls?)

## Watch out
- **Retire stale claims:** Stop teaching that Meta is a pure open-weight company or that Llama is Meta’s frontier brand—**Muse** has been the frontier brand since April 2026. Stop telling learners "Llama 4 Behemoth is coming soon" (announced April 2025, never released).
- **Do not overclaim:** Do not present Llama's license as "open source" under the OSI definition; Llama 4 still uses the custom Llama Community License with the 700M MAU restriction (only the 30B **Muse Glimmer** model uses true Apache 2.0).
- **Verify before class:** Confirm whether standalone [muse.ai](https://muse.ai) consumer accounts are open to Singapore IP addresses and local phone numbers without a waitlist on the day of your session, and verify current `-contributor` API discount rates.

## Sources
1. Meta Superintelligence Labs Official Releases & Product Announcements, *Introducing the Muse Family (Muse Spark 1.0–1.3, Muse Wonder, Muse Ember, and Meta Muse Agent)* (April – 9 November 2026).
2. Meta AI Open-Weight Repository & Release Notes, *Llama 4 Scout & Maverick* (5 April 2025) and *Muse Glimmer (Apache 2.0) & Muse Spark Open (816B MoE)* (August & 15 October 2026).
3. Meta Muse Pricing & Data Controls Documentation / OpenRouter Model Registry, *Muse Power & Maximum Tiers, `muse-spark-1.3-contributor` API SKU, and Third-Party Hosting Rates* (Verified November 2026).
