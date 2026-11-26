# Codex — OpenAI

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** OpenAI’s coding-agent product for people working in software projects; it can investigate code and propose or perform development work within the access it is given.

## The product

Codex is aimed at work on an actual codebase: understanding files, modifying code, and checking a change rather than merely answering a programming question in chat. OpenAI introduced a cloud-based Codex coding agent in May 2025; development interfaces and capabilities have evolved since, so a November 2026 class must verify the interface learners will actually use. For an owner who does not code, its relevance is **delegating a bounded software task with review**, not learning to speak in programming jargon.

## Current line-up (November 2026)

**This page does not carry a verified November 2026 Codex model or interface line-up.** “Codex” can refer to the product and its development workflows; it should not be used as if it identified one permanent underlying model. OpenAI’s **May 2025** launch described a coding agent that could work on tasks in an isolated environment. That is a dated baseline, **not** a claim that its launch model, limits, or interface remain current.

The names **GPT-6 Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, and Cyber** cannot responsibly be assigned to Codex roles, tiers, or release dates without current OpenAI documentation. A model label such as GPT-6 Sol, even if accurate, does not tell a trainer what model a learner’s Codex session uses. Record the actual product version, interface, model information *where exposed*, and account entitlements during class preparation.

## What it's best at / not best at

Codex is most useful when the work has a repository, a clear requested change, and a way to test the result. Examples include adding a small feature, fixing a reproducible bug, writing tests, or explaining how a particular part of a codebase works. A good assignment specifies **what may change, what must not change, and how success will be checked**.

It is not a replacement for a maintainer’s judgment, a security review, or knowledge of the business’s actual requirements. Code that runs can still violate a client agreement, expose data, break an untested workflow, or solve the wrong problem. Granting repository access also raises a different question from ordinary chat use: what files, secrets, commands, and external services can this agent reach?

**Trainer’s decision rule:** use Codex for a **bounded codebase task with tests and a reviewer**. Use ChatGPT for an initial explanation or planning discussion when no repository change is required. Do not hand a learner’s production credentials to either one for a classroom demonstration.

## Pricing (November 2026)

**November 2026 Codex pricing and plan inclusion are unverified.** Codex access may depend on the OpenAI product, subscription or organisational plan, interface, and usage limits. A historical launch announcement is not a current price sheet, and ChatGPT’s historical Plus or Pro launch prices do **not** establish today’s Codex entitlement or effective cost.

Before class, verify whether the chosen Codex interface is available to each learner, what usage limits apply, and whether related API or computing charges are billed separately. A “free to try” demonstration must not be represented as unlimited free use.

## What this actually teaches

**Delegation requires a testable definition of done.** Codex is an effective way to show why “make my system better” is a poor assignment, while “change this function, preserve this behaviour, run these tests, and show me the diff” is reviewable. The core lesson is not that an agent writes code quickly. It is that a human must define scope, inspect evidence, and accept responsibility for the change.

## The student lens

**Mental model:** A contractor working in a cordoned-off renovation area: give them the plans and permitted rooms, then inspect the work before opening the building.

**Misconceptions:**
- “If the tests pass, it is safe to deploy.” **Correction:** tests cover only what they check; review security, data handling, and business requirements too.
- “Codex knows what our customers want from the code.” **Correction:** it needs requirements, repository context, and a person who can confirm the result.
- “I asked for one fix, so it could only touch one file.” **Correction:** inspect the diff and enforce technical access boundaries; a request alone is not a permission control.

## The adult educator lens

**Analogy:** A renovation contractor in a Singapore shop unit given access to one room and a punch list. The analogy breaks because a coding agent can change many connected files rapidly, and software failures may be invisible until later.

**Three-minute demo:** Use a disposable repository with a function that miscalculates a fictional invoice total. Ask Codex to reproduce the bug, add a failing test, fix it, run the tests, and show the diff. Inspect the changed files before accepting anything.

**Where it goes wrong in class:** A live demo uses a real business repository, an exposed API key, or a task without a test; learners remember the speed rather than the review.

**Check for understanding:** “Besides passing tests, what must you inspect before accepting this code change?”

## Watch out

Retire the claim that Codex is simply “ChatGPT for coding,” or that it is safe because it operates in a sandbox: **the actual permissions and deployment path matter**. Verify current interfaces, model information, account access, pricing, repository permissions, network access, and approval controls before class. Never infer a November 2026 Codex model catalogue from an assistant’s stated runtime model.

## Sources

- OpenAI, [“Introducing Codex”](https://openai.com/index/introducing-codex/), **16 May 2025** — historical product launch, not a current entitlement list.
- OpenAI, [“Introducing GPT-4.1 in the API”](https://openai.com/index/gpt-4-1/), **14 April 2025** — historical context on OpenAI’s coding-capable models; **not evidence of Codex’s November 2026 underlying model**.
- OpenAI, [“New tools for building agents”](https://openai.com/index/new-tools-for-building-agents/), **11 March 2025** — background on tool-enabled agents; **not a current Codex pricing source**.
