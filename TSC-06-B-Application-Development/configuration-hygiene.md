---
id: 06.01.B.A5
tsc: 6
level: Basic
code: A5
title: "Configuration hygiene: the settings that quietly decide whether your app works"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Configuration hygiene: the settings that quietly decide whether your app works

> **TSC #6 Generative AI Application Development and Deployment · Basic · Ability A5**


> **Framework text (verbatim):** "Maintain proper software configurations and settings."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Ability · Bullet 11 of 11

**One-line version:** Configuration is the part of the system nobody owns until it breaks, and it breaks on a Tuesday morning.

## What it is

Maintaining configurations means keeping the settings an application depends on — keys, model versions, parameters, endpoints, quotas, guardrail thresholds — in a known, documented, reviewable state, separated by environment, with secrets held securely and every change recorded. It is the least glamorous ability in this level and the one that decides whether last month's working demo still works.

## Deep expansion

### The concept

An AI application has two kinds of content: code you write and settings you choose. The code is visible, reviewed and versioned. The settings are scattered — an environment variable here, a text box in a console there, a model name hard-coded in a script, a threshold adjusted by someone who has since left.

Configuration is where behaviour actually lives. The same code with a different temperature, model snapshot, top-k or guardrail threshold is a different product. When an AI app misbehaves and the code has not changed, the answer is almost always in the settings.

The habit is to treat configuration as an artefact with an owner, a record and a review — not a page someone visits when something feels off. That is achievable at Basic level with a table and a text file.

### The sub-concepts

**Secrets are not configuration.** An API key is a credential: a secret store or an environment variable, never code, a notebook, a screenshot or a chat message. It needs a named owner, a rotation date and a revocation plan. A key pasted into a shared document is already compromised; the only question is whether anyone noticed.

**Environments are separate for a reason.** Development, testing and production should not share keys, data or model versions. The separation is not bureaucracy — it is blast radius.

**Pin what you depend on.** Model snapshot, package versions, retrieval parameters and the prompt itself. Pinning is how you make yesterday reproducible; without it, "it worked last week" is unfalsifiable.

**Document the defaults with a reason.** A table of setting, value, why, owner, last reviewed. The "why" column is the one people skip and the one that stops a future engineer "fixing" a deliberate choice.

**Drift is the default state.** The configuration of record and the configuration actually running diverge the moment two people can edit it. Keep settings in version control, or export and compare on a schedule.

**Least privilege.** The application's key should do what the application does and nothing else. An admin key in a small app is a large incident waiting for a small bug.

### How it connects to the rest of the framework

`TSC6-Basic-K6` is the environment this configuration must fit; `TSC6-Basic-A1` is where the model parameters are chosen; `TSC6-Basic-A4` is the performance conversation that often triggers a change. `TSC6-Intermediate-K6` and `TSC9` turn these habits into organisational controls.

### What is current as of November 2026

- **Secret scanning is a gate, not a courtesy.** Hosting platforms block pushes containing recognised credentials, and providers auto-revoke keys that appear publicly. The safety net exists; relying on it is still a bad habit.
- **Model snapshots retire on a published schedule.** Pinning a model is a configuration decision with a calendar attached: someone must own the deprecation notice and the migration.
- **Admin consoles centralised settings** and added audit logs, making "who changed this" answerable for the first time.

### Common misconceptions

- *"It's just a settings page."* It is the behaviour of the product. Someone changed a threshold and the product changed with it.
- *"We'll document it later."* Later is after the person who understood it has moved teams.
- *"One key for everything is simpler."* Simpler until it leaks, when everything must be rotated at once, including things you forgot existed.

## How a student should understand it

**Mental model:** the recipe card and the supplier list taped to the stall's wall. The cook can leave; the stall still opens, because what made it work was written where the next person can find it.

**Three things they can do after this bullet:**
1. Produce a settings table for their own app — setting, value, why, owner, last reviewed.
2. Move every credential out of code into a secret store, and name a rotation owner.
3. Explain what breaks when a pinned model version is retired, and who receives the notice.

**Misconceptions to kill:** that configuration is clerical, that secrets in a private document are safe, and that a working system needs no record.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The household utility accounts.** Gas, water, electricity, town council, broadband — one folder with the account numbers and passwords lets a family recover in an afternoon; one person's phone loses them a week. Configuration is that folder. Where it breaks: utilities are stable for years, while a model endpoint can retire in a quarter, so the folder needs a review date, not just a location.

**The stall's recipe card.** The founder's version lives in the founder's hands. The surviving stall has the recipe, the portions and the supplier's number on the wall — which is also why the franchise tastes the same in Jurong and in Tampines.

### Worked example with a real tool

Take a working app's scattered settings and turn them into something maintainable:

```
Here are the settings spread across my script and the platform console.
Produce (a) a .env.example with placeholder values and a comment per variable,
(b) a markdown table: Setting | Value | Why | Owner | Last reviewed, and
(c) a list of which values must never be committed, with the reason.

Settings: OPENAI_API_KEY=sk-...(real), MODEL=gpt-4o-mini, TEMP=0.2, TOP_K=8,
CHUNK=1000, MAX_TOKENS=800, guardrail_threshold=0.7, and one admin_api_key
used for both the app and the admin console.
```

What to point at afterwards: the first line of the output — the model has copied the real key into `.env.example`. That is not a bug; it is exactly what you asked for, and precisely the mistake the exercise prevents. Delete it, insert a placeholder, then look at the last setting: one key for both app and admin. The table makes the privilege problem visible in a way reading the script never did.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two printouts: a script with a key on line 3, and a screenshot of the same key in a chat. Ask which is in someone's phone right now.
2. **State the objective** — by the end you can produce a settings table, separate secrets from configuration, and pin what the app depends on.
3. **Recall prior learning** — the environment sheet from K6, the parameters from A1, the cost discussion from A4.
4. **Present the content** — secrets, environments, pinning, the five-column table, drift, least privilege.
5. **Guide** — build the table for a small app, arguing the "why" column for each row.
6. **Elicit performance** — each learner writes the table and `.env.example` for their project; a partner reviews it for a leaked credential.
7. **Give feedback** — the review findings are the feedback. Expect at least one real key in the room.
8. **Transfer** — each learner names the owner of each pinned version, the review date, and puts it in a calendar invite.

## What the framework doesn't mention but trainers need to know

- **The prompt is configuration.** It lives in a text box, gets edited quietly and changes behaviour more than any parameter. Version it with the code.
- **Rotation needs a rehearsal.** A key rotation never tested is a plan, not a capability. Know how to revoke before you need to.
- **Guardrail thresholds drift.** Someone lowers a threshold to stop false refusals and never raises it back. Review dates catch this; memory does not.

## Watch out

- **Do not demo with a real key on screen.** Ever. Even for three seconds, even privately.
- **Do not let the table become a document nobody opens.** Attach it to the README and the go-live checklist.
- **The stale claim to retire:** "configuration is an IT matter." The model version, retrieval parameters and guardrail threshold are product decisions now.
