# DeepSeek — DeepSeek

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** An open-weight reasoning and coding model suite with a free consumer chatbot and low-cost API, built for developers, technical analysts, and cost-sensitive AI builders.

## The product
DeepSeek provides both a free consumer chat application (web and mobile) and an API/open-weight ecosystem of Mixture-of-Experts (MoE) language models. After disrupting the market in early 2025 with its `DeepSeek-R1` reasoning model, the company consolidated its stack in 2026 into the multimodal V4 architecture, combining native visual understanding, switchable reasoning ("thinking mode"), and aggressive KV-cache compression. Users either access it at zero cost through the hosted interface or integrate it via API and self-hosted MIT-licensed weights.

## Current line-up (November 2026)
- **`DeepSeek-V4.1-Flash` (checkpoint `1017`, Oct 2026):** The default flagship powering the consumer app and the `deepseek-flash` API alias. It is a 552B-parameter asymmetric MoE (8B active input parameters, 16B active output parameters) with a 1M token context window, native vision, and toggleable thinking mode. Released September 9, 2026; updated October 17, 2026.
- **`DeepSeek-V4-Pro` (checkpoint `0813`, Apr/Aug 2026):** Launched April 24, 2026. Being phased out in favour of `V4.1-Flash` (which outperforms it on speed and benchmarks) while awaiting `V4.1-Pro`. Some API accounts still access `V4-Pro-0813`, though default `deepseek-v4-pro` calls began routing to `V4.1-Flash` in September 2026.
- **Application APIs (Nov 13, 2026):** Hosted server-side tools including `deepseek_web_search`, `deepseek_read_url`, file parsing, and `DeepSeek-OCR 2`.
- **Legacy / Missing:** `DeepSeek-V3.2` (Dec 2025) and `DeepSeek-R1` (Jan 2025) remain on Hugging Face for local deployment. The widely rumoured `DeepSeek-R2` has not been released as of November 2026.

## What it's best at / not best at
**Best at:** Transparent step-by-step reasoning, code generation, structured math/logic problems, and high-volume API agent loops where KV-cache hits make long-context processing remarkably cheap. 
**Not best at:** Unfiltered geopolitical or China-sensitive queries (which trigger strict server-side censorship), low-governance enterprise deployments with strict data residency rules (data on the hosted app/API routes to China), and polished multimodal workspace collaboration.
**Trainer decision rule:** Use DeepSeek when you want to inspect the raw chain-of-thought on hard logic or coding tasks—or when building high-volume API workflows on a tight budget—provided the data is completely non-sensitive or running on locally hosted weights.

## Pricing (November 2026)
- **Consumer App (`chat.deepseek.com` & mobile):** Free ($0). No paid consumer subscription tier exists.
- **API (`deepseek-flash` / `V4.1-Flash-1017`):** Uses peak vs. off-peak pricing. Peak hours are Mon–Fri, 01:00–04:00 and 06:00–10:00 UTC (09:00–12:00 and 14:00–18:00 SGT).
  - *Off-peak per 1M tokens:* $0.15 input (cache miss) / $0.003 input (cache hit) / $0.60 output.
  - *Peak per 1M tokens:* $0.30 input (cache miss) / $0.006 input (cache hit) / $1.20 output.
- **API (`V4-Pro-0813`, where unrouted):** Off-peak $0.66 miss / $0.022 hit / $1.98 output per 1M tokens (doubles at peak).
- **Add-on APIs:** Standalone Search and Fetch APIs cost $0.75 per 1,000 requests (though as of Nov 18, 2026, server-side search triggered inside model calls is billed solely as context tokens). OCR API is $0.225 per 1,000 pages.
- **Uncertain:** Exact third-party host rates (e.g., Together, Fireworks, AWS) vary significantly and do not follow DeepSeek's peak/off-peak schedule.

## What this actually teaches
**Visible reasoning and architectural efficiency:** DeepSeek is the clearest vehicle for teaching learners that "thinking" is a distinct compute phase (trading latency and output tokens for verification) and that open-weight model efficiency is driven by sparse architectures and caching rather than sheer parameter size.

## The student lens
**Mental model:** A glass-walled kitchen where you watch the chef test, burn, and redo a sauce before plating the final dish.
**Misconceptions:**
- *"The thinking trace is reading the AI's true subconscious mind."* → Correction: It is simply extra token generation trained via reinforcement learning to break down steps before producing the user-facing response.
- *"Because it's open-source, the website is safe for company data."* → Correction: Open-weight means the model files are downloadable under an MIT license; the free website (`chat.deepseek.com`) is still a proprietary cloud service hosted in China that logs your inputs.
- *"I should look for DeepSeek R2 for reasoning tasks."* → Correction: `R2` has not launched; reasoning is now a built-in toggle ("thinking mode") inside the `V4.1-Flash` model.

## The adult educator lens
**Analogy:** ERP (Electronic Road Pricing) on the CTE combined with a hawker centre open kitchen. You see every move the cook makes for cheap, and if you travel outside peak hours, the toll drops by half. *Where it breaks:* ERP regulates physical congestion without recording what is inside your car, whereas DeepSeek's direct cloud reads and retains every prompt you send.
**Three-minute demo:** Paste a flawed 30-line Python script or a tricky logic puzzle into `chat.deepseek.com` with Thinking and Web Search enabled. Expand the grey thought block live so learners see the model propose an approach, catch its own error mid-stream, and pivot before writing the final answer.
**Where it goes wrong in class:** Peak-hour server throttling during Singapore afternoon workshops (14:00–18:00 SGT overlaps with DeepSeek's 06:00–10:00 UTC peak window), or corporate firewall blocks preventing learners from reaching `.cn` / DeepSeek endpoints.
**Check for understanding:** "If your developer team runs a batch document-extraction script at 3:00 PM Singapore time using the free web chat vs. the API, what are the two biggest differences in cost and data privacy?"

## Watch out
- **Retire stale claims:** Stop teaching that DeepSeek splits its product into "V3 for chat and R1 for reasoning"—`V4.1-Flash` handles both via a mode switch. Also retire claims that `DeepSeek-R2` is out; any site hosting "R2" in November 2026 is a fake wrapper.
- **Do not overclaim:** Do not pitch the direct API as enterprise-ready for regulated sectors without third-party Western/local hosting.
- **Verify before class:** Test whether `chat.deepseek.com` requires SMS/email verification on the venue IP, and check if `V4.1-Pro` has officially replaced the `V4-Pro` fallback route.

## Sources
1. [DeepSeek Official Release Notes — *Introducing DeepSeek-V4.1-Flash*](https://api-docs.deepseek.com/) (9 September 2026).
2. [DeepSeek API Documentation — *Models & Pricing / Change Log*](https://api-docs.deepseek.com/) (Updated 18 November 2026).
3. [Layer3Labs — *DeepSeek New Model Release 2026: R2 Not Out, V4 Is*](https://layer3labs.io/) (8 October 2026).
