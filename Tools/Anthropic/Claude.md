# Claude — Anthropic

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** A family of general-purpose AI models and apps (chat, API, coding agent) for people who need careful reading, long documents, and reliable instruction-following — built for professionals, not hobbyists.

## The product
Claude is Anthropic's assistant, available as a web/desktop/mobile app, as an API for builders, and as Claude Code for agentic work in a terminal or IDE. The pitch is steadiness: long context, instruction-following, and a safety posture (refusals, honesty about uncertainty) that enterprise and regulated buyers care about. It is a model you give *context* to, which is why it suits a Company-OS-style way of working.

## Current line-up (November 2026)
Unverified: the names below were in use when this page was written (26 November 2026) but have not been checked against Anthropic's own pages. **Verify every name and date on Anthropic's model page before class.**

- **Claude Fable 5.1** — positioned as the general workhorse.
- **Claude Opus 5.5** — top-end reasoning/agentic model.
- **Claude Sonnet 5.5** — mid-tier balance of speed and capability.
- **Claude Haiku 5.5** — fastest/cheapest tier for high-volume, simple tasks.
- **1M-token context** — advertised on current models; unconfirmed which tiers, and whether it is default or opt-in/beta.
- **Adaptive thinking** — the model decides how much to reason per request (the successor to manual "extended thinking" budgets). Exact controls per model: verify.
- **Knowledge cutoff:** June 2026 for the current generation (unverified).

Release dates for the 5.5 models: not confirmed. Do not state them in class unless read off the official page that day.

## What it's best at / not best at
**Best at:** long documents (contracts, SOP libraries, transcripts); following structured instructions and precedence rules; writing in a specified voice; coding and multi-step agent tasks via Claude Code; saying "I don't know."
**Not best at:** real-time facts (needs web search or supplied documents); image generation (it does not make images); arithmetic at scale without tools; anything after its cutoff.
**Decision rule for learners:** *If the job is "read a lot, reason carefully, follow my rules," use Claude. If the job is "what happened today" or "make me a picture," use something else or give Claude the material.*

## Pricing (November 2026)
Structure is stable; numbers rot. Based on the long-standing structure — **confirm on anthropic.com/pricing**:
- **Free** — app access with usage caps, usually to a lower-tier model at peak.
- **Pro** — individual paid plan, historically about US$20/month (SGD billed with GST; expect ~S$30). Higher limits, Claude Code access, projects.
- **Max** — higher-usage individual tiers, historically US$100 and US$200/month. Verify current levels.
- **Team / Enterprise** — per-seat with admin controls, SSO, data-retention commitments; price on request for Enterprise.
- **API** — per million tokens, input cheaper than output; Haiku cheapest, Opus most expensive; cached-input and batch discounts exist. Per-token figures for the 5.5 models are not quoted here because they are unverified.

Uncertain: whether 1M context carries a surcharge on any tier; current Max limits; whether Singapore pricing is USD-billed.

## What this actually teaches
The one lesson Claude is the best vehicle for: **context beats prompts.** Students who paste a one-line prompt get generic output; students who load the facts, rules, and voice first get work that sounds like their business. Claude's long window and instruction discipline make this visible in minutes, which is why it is the right tool to teach "build the knowledge layer, then ask."

## The student lens
**Mental model:** A very well-read new hire on their first day — brilliant, fast, polite, and knows nothing about *your* company until you hand them the staff handbook.
**Misconceptions:**
- *"It knows about my business."* It knows nothing about you until you supply it. Every session starts from zero unless you use projects/memory features.
- *"Bigger context means I should paste everything."* Relevance still matters; the middle of a huge paste is read least carefully. Give the right files, not all files.
- *"It said it, so it's checked."* Claude will flag uncertainty when asked, but it does not verify facts against the world. Verification is your job.

## The adult educator lens
**Analogy:** A locum relief teacher at an MOE school: competent anywhere, but only as good as the lesson plan and class notes you leave on the desk. **Where it breaks:** the relief teacher remembers you next term; Claude does not, unless you build memory in.
**Three-minute demo:** Ask Claude to write a client email with no context. Then paste a three-table "facts + voice + rules" file and ask again. Put the two outputs side by side. That gap is the whole course.
**Where it goes wrong in class:** Learners hit free-tier usage caps mid-exercise, or the class is split across Free/Pro and gets different models. Standardise accounts before the session.
**Check for understanding:** "What three things would you have to give Claude before it could draft your proposals without embarrassing you?"

## Watch out
- Retire any slide naming Claude 3.x, 4.x, or "200K context" as current.
- Do not overclaim 1M context as "it reads everything perfectly" — attention degrades across very long inputs; test with the learner's own documents.
- Do not promise "no hallucinations." Promise "flags uncertainty when asked, and refuses less often than you think."
- Verify before class: current model names, which tier is on Free, Pro/Max prices in SGD, Claude Code availability on the plan, and data-retention terms (relevant to PDPA conversations).

## Sources
- Anthropic model overview — docs.anthropic.com (check the "last updated" date on the page the morning of class).
- Anthropic pricing page — anthropic.com/pricing (undated; capture a screenshot with date for your records).
- Anthropic release notes / announcements — anthropic.com/news (confirm 5.5-series release dates; they are unverified here).
