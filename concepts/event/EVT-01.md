# EVT-01 · Black October: what actually happened in October 2026

**Tier:** Event · **As at:** 9 November 2026 · **Status:** dated case study. Facts are stable; interpretation will keep moving.

**Framework home** — TSC #9 GenAI Models: Technical Aspects of Security and Ethics (Basic to Intermediate): *AI-enabled security risks, vulnerability discovery, incident response*. Also TSC #1 (limitations and responsible use) and TSC #8 (societal impact). This is the entry that makes "AI risk" concrete instead of abstract.

---

## What happened

October 2026 produced an unusual cluster of security events, and the press named it **Black October**. The centre of it was **PHP2Shell** — two critical vulnerabilities in the PHP interpreter, tracked as CVE-2026-109618 and CVE-2026-109619.

**The discovery.** The flaws were found with AI. Security firm Calif reported finding them on 1 August with the help of a large language model; Wiz independently found them using its autonomous vulnerability-research tool alongside Gemini 4 Argon and GPT-5.6 Sol. The bugs were memory-management errors — reuse of freed memory, invalid state persisting between requests — that had sat in the codebase for more than a decade and that Wiz described as extraordinarily hard for a human to exploit manually.

**The patch.** PHP released 8.2.35, 8.3.36, 8.4.27 and 8.5.12 on 21 October. The NSA issued an advisory urging immediate patching.

**The scramble.** Because PHP underpins roughly 70–75% of websites whose language can be identified — including WordPress, Drupal, Joomla and Magento — governments took sites offline *as a precaution, not because they were breached*. The Dutch NCSC, Port of Rotterdam, Overheid.nl, the KNVB, five major political parties and several hospitals went dark; Denmark's Kombit shut services including the national school platform; Finland's Valtori took government services offline; France's Interior Ministry placed its sites into preventive maintenance. Wikipedia and the Internet Archive briefly followed. Censys estimated about 1.5 million of 2.6 million hosts were running an unfixed version.

**The part that should worry trainers.** Amazon's security team detected an exploitation attempt against a honeypot on **17 October — four days before public disclosure**. The embargo did not hold. And AI collapsed the usual window between "patch published" and "exploit weaponised", because reverse-engineering a patch is exactly the kind of reading task these models are good at.

**The rest of the month, briefly.** eMudhra's intermediate CA keys were found to be weakly generated, prompting Chrome and Firefox to revoke them and eMudhra to exit the SSL/TLS certificate business (22 Oct). LiteLLM — an open-source gateway for routing requests across LLM providers — had its release pipeline compromised: a malicious version 1.107.0 reached PyPI and Docker Hub for roughly two hours on 21 October, stealing browser credentials, cloud secrets and API keys. GitLab patched a CVSS 10.0 remote code execution flaw; Brotli and EDK II's network boot driver had critical memory flaws; a Linux kernel RCE landed at CVSS 9.8. One of the firmware flaws was credited to researchers at Anthropic and Google.

## What it actually means

The headline "hackers used AI to hack government sites" is mostly wrong, and the truth is more useful:

1. **AI was the auditor first.** A decade-old bug that humans missed was found by machines reading code at scale. Defensive capability improved in the same month offensive capability did.
2. **AI was the accelerant second.** Once a patch is public, AI makes the diff readable in minutes. The disclosure-to-exploitation window is now measured in hours.
3. **The outage was the defence, not the attack.** Governments went dark on purpose. A room that believes otherwise has learned the wrong lesson.
4. **The AI supply chain is itself a target.** LiteLLM is not an AI model; it is the plumbing that connects applications to models. Compromise the plumbing and you get every key in the building.

## The student lens

**Mental model:** AI is a very fast reader. Point it at code and it finds things humans missed — which is equally true of the person attacking you.

**Misconceptions:**
- *"AI hacked the government."* The sites were taken down by their own operators to patch.
- *"This is a developer problem, not mine."* The LiteLLM attack harvested browser credentials and API keys — the same keys a trainer's demo account uses.
- *"Patching is IT's job."* The single highest-value habit any professional can adopt this year is applying updates within days, not months.

**Five-minute practice:** ask learners to list every AI tool and browser extension they have authorised with a work login. Most will find at least one they have forgotten. That list is their personal exposure surface.

## The adult educator lens

**Analogy:** a building inspection. A new machine can X-ray every wall in the city in a week and find the cracks. That is good news — until you realise the burglars bought the same machine, and the building plans are published the day the repair is announced.

**Three-minute demo:** show the timeline on screen — discovery 1 Aug, honeypot attempt 17 Oct, public disclosure and patch 21 Oct, exploitation the same day. Then ask the room to mark where a "responsible disclosure" window is supposed to protect them. The gap between 17 and 21 October does the teaching.

**Board sketch:** two columns, "AI as defender" and "AI as attacker", same four capabilities in both (reads code fast, finds patterns, writes exploits, scales). The symmetry is the lesson.

**Where it goes wrong in class:** someone will say "so AI is too dangerous". Do not agree or dismiss. Give the honest position: the same month produced the fastest mass patching in living memory *because* AI found the flaw, and the fastest exploitation because AI read the patch. Capability is not a side.

**Check for understanding:** "Name the one thing an ordinary office worker should do differently after October 2026, and the one thing they should stop believing." (Update within days; stop believing that a downed website means a successful hack.)

## Say this out loud

"AI didn't hack the government. It found the hole, and then it made the hole easier to use. Both halves are the lesson."

## Content hook

**LinkedIn opener:** "Everyone shared the headline. Almost nobody noticed that the government sites went down on purpose — and that the exploit attempt happened four days before the world was told."

**Carousel idea:** "Black October in six dates" — 1 Aug, 17 Oct, 20 Oct, 21 Oct, 22 Oct, and today. One line per date, no jargon.
