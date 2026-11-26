# Copilot — Microsoft

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** Microsoft’s umbrella brand for AI assistants and agents embedded across Windows, the web, and the Microsoft 365 productivity suite for consumers and enterprise workers.

## The product
Copilot is not a single tool; it is an AI orchestration layer that connects frontier models to user interfaces and data. At the consumer and basic business level, it provides a web-grounded chat interface (`Copilot Chat`). At the paid enterprise level (`Microsoft 365 Copilot`), it acts as an operating system for work—combining chat, cross-departmental collaboration (`Cowork`), autonomous background agents (`Autopilot`), and in-app generation inside Word, Excel, PowerPoint, Outlook, and Teams, all grounded in the organisation’s internal data (`Work IQ` / Microsoft Graph).

## Current line-up (November 2026)
- **Consumer plans:** Free `Copilot` app (web/mobile/Windows). `Microsoft 365 Personal` and `Family` include a capped allowance of 60 Copilot AI credits per month inside Office desktop apps. `Microsoft 365 Premium` (which replaced the retired `Copilot Pro` plan in October 2025; legacy `Copilot Pro` support fully ended 1 August 2026) unlocks uncapped Copilot in consumer desktop apps. A top-tier `Microsoft 365 Pro` consumer plan also exists.
- **Commercial plans:** `Copilot Chat` (formerly Bing Chat Enterprise) is included free with eligible Microsoft 365 business licences for web-only chat. `Microsoft 365 Copilot Business` (launched December 2025 for organisations up to 300 seats) and `Microsoft 365 Copilot` (Enterprise, 300+ seats) provide full Graph-grounded integration across Office apps, `Cowork`, and `Autopilot`.
- **Builder & developer tiers:** `Copilot Studio` for building custom enterprise agents, and `GitHub Copilot` for software engineering.
- **Underlying models:** Copilot uses dynamic model routing (`Microsoft Decision 1.1`) rather than a single static model. OpenAI’s `GPT-5` rolled out to M365 Copilot in August 2025, followed by `GPT-5.6` as the preferred default in July 2026. At Ignite (17 November 2026), Microsoft introduced its in-house `MAI` model family (`MAI Code 2`, `MAI Image 2.7`, `MAI Realtime 1`, `MAI Transcribe 2`) into the routing harness alongside OpenAI’s `GPT-6` series. As of 24 November 2026, consumer interfaces frequently hide specific `GPT` model pickers behind simplified task modes (`Auto`, `Quick Response`, `Think Deeper`).

## What it's best at / not best at
**Decision rule:** Use paid M365 Copilot when the output must synthesise internal company emails, Teams transcripts, and SharePoint files inside Office formats; use a standalone frontier chatbot when doing deep, zero-shot reasoning from scratch on clean text.
- **Best at:** Catching up on missed Teams meetings with action items; turning an existing Word specification into a starter PowerPoint deck; querying across scattered company SharePoint documents (`Work IQ`) while respecting existing enterprise security permissions.
- **Not best at:** Complex multi-step financial modelling in Excel on dirty, unstructured spreadsheets; maintaining long-context coherence when users have poor SharePoint file hygiene; transparent model selection (the routing harness frequently swaps underlying models without notifying the user).

## Pricing (November 2026)
*All figures in USD list prices (verified November 2026); regional and enterprise agreement discounts vary.*
- **Free:** $0 for consumer web/mobile `Copilot`, and $0 add-on for commercial web-grounded `Copilot Chat` (requires base M365 licence).
- **Consumer:** `M365 Personal` ($9.99/month) and `Family` ($12.99/month) include 60 AI credits/month. `M365 Premium` ($19.99/month or $199.99/year) removes credit caps and includes 6 TB storage. `M365 Pro` is $99.99/month.
- **Business (<300 users):** `M365 Copilot Business` add-on is $21/user/month billed annually (an $18/user/month promotional rate runs through 31 December 2026). A bundled `Business Standard with Copilot` SKU runs $23.50/user/month.
- **Enterprise (300+ users):** `M365 Copilot` is $30/user/month billed annually, on top of a required base M365 E3/E5 licence.
- **Uncertain:** Pay-as-you-go `Copilot Studio` credit consumption rates and `Autopilot` agent run costs shift rapidly and depend heavily on tenant agreements—verify live calculation tables before quoting to IT buyers.

## What this actually teaches
**Context architecture beats raw model intelligence.** Copilot is the definitive vehicle for teaching learners that an AI assistant’s usefulness in an organisation depends almost entirely on what data it is permitted to read (`Work IQ` / Graph grounding) and how well that data is governed, rather than which frontier model sits under the hood.

## The student lens
**Mental model:** A newly hired executive assistant who has already read every email, calendar invite, and shared folder your security badge allows you to open—eager to draft, but only as accurate as your filing cabinet.
**Misconceptions:**
- *"I bought Copilot on my home laptop, so I can use it to search my company’s SharePoint."* → **Correction:** Consumer `M365 Premium` cannot connect to corporate work data; only a commercial `M365 Copilot` licence assigned by your IT admin can read your company Graph.
- *"Copilot is just ChatGPT with a Microsoft logo."* → **Correction:** While it uses OpenAI models (`GPT-5.6`), Copilot wraps them in Microsoft’s routing harness, pairs them with in-house `MAI` models, and grounds them in your live Office files.
- *"If I deploy Copilot, everyone in the company can see my private documents."* → **Correction:** Copilot inherits your existing M365 permissions; it can only surface files a user already has permission to view (though it will expose poorly configured oversharing).

## The adult educator lens
**Analogy:** Using free `Copilot Chat` vs paid `M365 Copilot` is like asking a taxi driver at Changi Airport for directions versus logging into your personal Singpass. The taxi driver (`Copilot Chat`) knows the public roads of Singapore (the public web), while Singpass (`M365 Copilot`) pulls your exact CPF balances, HDB records, and tax filings across agencies (`Work IQ`). *Where it breaks:* Singpass fetches deterministic database records with 100% precision, whereas Copilot probabilistically summarises your files and can still hallucinate details.
**Three-minute demo:** Open Word with a blank page, type `/`, reference an existing messy 5-page meeting transcript `.docx` in OneDrive, and generate a formatted client proposal in 20 seconds—then click the citation footnotes to prove it pulled only from that file.
**Where it goes wrong in class:** Half the room logs in with personal `@outlook.com` accounts, half with corporate Entra IDs that only have free `Copilot Chat`, and two people have full `$30` licences—causing total confusion when the Copilot button is missing inside their desktop Word app.
**Check for understanding:** "If a staff member uses Copilot to summarise 'the latest HR leave policy' and gets a 2021 draft instead of the 2026 policy, is that a model failure or a SharePoint data hygiene failure—and why?"

## Watch out
- **Retire stale claims:** Stop calling the consumer tier `Copilot Pro`; it was retired in late 2025 and replaced by `Microsoft 365 Premium`. Stop saying Copilot runs on `GPT-4`; it moved to `GPT-5` in August 2025 and `GPT-5.6` / `MAI` routing in 2026.
- **Do not overclaim:** Do not promise learners that Copilot in Excel can replace data analysts; its Python/formula generation still struggles with unformatted multi-tab sheets.
- **Verify before class:** Check the tenant licence state of your training accounts 24 hours prior. Since April 2026, Microsoft restricted in-app Copilot Chat sidebars in Word/Excel/PowerPoint for unlicensed users in large enterprises (2,000+ seats), and UI model toggles (`Auto` vs explicit model names) change without notice.

## Sources
- [Ignite 2026: Building the frontier ecosystem — Official Microsoft Blog](https://blogs.microsoft.com/blog/2026/11/17/ignite-2026-building-the-frontier-ecosystem/) (17 November 2026)
- [Seven new world-class models at scalable price-performance — Microsoft AI](https://microsoft.ai/news/) (17 November 2026)
- [Microsoft Copilot Plans and Pricing — Microsoft 365](https://www.microsoft.com/en-us/microsoft-365/copilot/pricing) (Accessed November 2026)
