---
id: 06.01.B.K2
tsc: 6
level: Basic
code: K2
title: "Low-code and no-code: building an AI app without building the pipes"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Low-code and no-code: building an AI app without building the pipes

> **TSC #6 Generative AI Application Development and Deployment · Basic · Knowledge K2**


> **Framework text (verbatim):** "Low-code, no-code application development."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Knowledge · Bullet 2 of 11

**One-line version:** Low-code gets you a working app in an afternoon; the skill is knowing which apps are allowed to be that cheap.

## What it is

Low-code and no-code platforms let someone assemble a working application — a form, a table, a workflow, a model call, a screen — by configuring components instead of writing a program. No-code means everything through the interface; low-code means the interface plus small amounts of script when it runs out.

## Deep expansion

### The concept

Every application has three layers: somewhere to keep the data, logic that acts on it, and a surface a human touches. Traditional development writes all three. Low-code ships all three as configurable parts, so the builder's job becomes assembly: pick the table, draw the flow, drop in the form, connect the model.

For generative AI this matters because the model call is now one more component. A learner who can drag a workflow together can put an instruction in front of a model, take the response and write it back to a row — which is what most internal AI tools actually are.

The framework lists this as knowledge, not ability, and that is right. A Basic learner needs to know what these platforms can and cannot carry, and where the boundary with a real engineering team sits.

### The sub-concepts

**The three layers.** Data, logic, interface. Every platform arranges them differently, and every failure can be located in one of them.

**No-code versus low-code versus pro-code.** Not a quality ladder — a control ladder. No-code maximises who can build; pro-code maximises what can be built. Choose by consequence of failure, not by ambition.

**The glue platform.** A category that connects existing systems: trigger on an event, transform the payload, call the model, write back. For AI this is often the entire product.

**Citizen developer and shadow IT.** When the business can build without IT, it will. The governance question — who approves, who owns, who can see the data — arrives later than the app does.

**Vendor lock-in.** The app lives in someone's platform. Export is partial, and terms can change under you.

### How it connects to the rest of the framework

`TSC6-Basic-K4` covers the developer tools one level down; `TSC6-Basic-K6` covers the requirements that decide whether a platform can host the thing; `TSC6-Basic-A5` is the configuration discipline that keeps it working. `TSC6-Intermediate-K3` and `TSC6-Advanced-A2` are where you go when the platform stops carrying the load.

### What is current as of November 2026

The category has split in two, and trainers should say so.

- **Classic low-code** — Power Platform, AppSheet, Airtable, Retool, Zapier, Make, n8n — added model calls as a standard step. The workflow builder is now the most common place a Singapore SME actually deploys generative AI.
- **Prompt-to-app builders** — Lovable, Bolt, v0, Replit and the app-generation features inside the major assistants — moved from producing snippets to producing a working front end from a paragraph. That is the "vibe coding" wave: the demo became trivial and the production question got harder.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"No-code means no engineering."* It means the platform vendor did the engineering, invisibly. The limits are real and not yours to fix.
- *"The demo is the product."* A demo survives one happy path. A product survives an empty field, a duplicate record, a 429 and a colleague who clicks twice.
- *"It will scale with us."* It scales until it does not, usually during a busy period.

## How a student should understand it

**Mental model:** IKEA versus built-in carpentry. Flat-pack gets you a solid shelf this afternoon. It is not a failure — it is the right choice for a shelf. It becomes a failure the day you ask it to hold the television.

**Three things they can do after this bullet:**
1. Name the three layers of any app and say which one a platform is weakest at.
2. Choose no-code, low-code or pro-code for a use case, and defend the choice.
3. List the four questions to ask before a business-built AI app goes live.

**Misconceptions to kill:** that no-code is unprofessional, that a working demo is a finished product, and that scale is a later problem.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The showflat versus TOP.** A prompt-built interface is a condo showflat: the taps are real, the kitchen looks finished, the light falls beautifully. Nothing flows, because the pipes were never laid. Temporary Occupation Permit is the unglamorous part — plumbing, wiring, fire safety, the certificate that says a human may live here. Where it breaks: a showflat is deliberately deceptive, whereas the builder usually believes they have finished. Say that out loud; it changes how the room hears it.

**The hawker stall's first month.** Anyone can rent a stall and sell one dish well. The one that survives has a supplier, a licence, a queue plan and someone who covers when the cook is on MC. The app is the dish; the rest is what makes it a business.

### Worked example with a real tool

In Airtable, a Google Sheet with an AI field, or n8n, take a real complaint log. The instruction typed into the AI step:

```
You are classifying customer complaints for a tuition centre.
Read the complaint text and return exactly one category from:
FEES, SCHEDULE, TEACHER, FACILITIES, REFUND, OTHER.
Then return a severity of LOW, MEDIUM or HIGH, where HIGH means the
customer has asked for money back or threatened to leave.
Return only: {"category": "...", "severity": "...", "reason": "one short sentence"}
```

What to point at afterwards: the automation is eight clicks and one paragraph, and it is genuinely useful. Then break it in front of them — a row with the complaint empty, a row in Malay, a row asking for a refund *and* complaining about a teacher. The output is still valid JSON and is now wrong. That gap between "runs" and "correct" is the entire bullet.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a 30-second screen recording of the classifier being built from an empty base. Nothing but clicks.
2. **State the objective** — by the end you can place low-code on the build ladder, pick the rung for a use case, and name what must be true before go-live.
3. **Recall prior learning** — the three layers of an application; the model as an unreliable function.
4. **Present the content** — the ladder, the layers, showflat versus TOP, and four go-live questions: whose data, who can see it, who owns it when I leave, what happens when the vendor changes terms.
5. **Guide** — build the classifier together, one row at a time, narrating each choice.
6. **Elicit performance** — pairs sketch one internal tool on paper: table, trigger, prompt, output field.
7. **Give feedback** — two pairs present. The room names the layer most likely to fail and the question nobody asked.
8. **Transfer** — each learner writes the four go-live questions into their notes, with real names against each.

## What the framework doesn't mention but trainers need to know

- **The build is not the deliverable; the ownership is.** An app built by one enthusiastic officer and undocumented is a resignation letter waiting to happen.
- **Data protection is the quiet risk.** Pasting customer records into a third-party platform can be a PDPA problem before it is a technical one. Read the data-processing terms.
- **Cost is per-operation, not per-seat.** Automation platforms bill by run; a loop firing on every row edit multiplies quietly.

## Watch out

- **Do not let the room leave believing they can now ship software.** Confidence built on a happy-path demo is a liability you personally created.
- **Do not demo a build you have not rehearsed on this platform version.** A live fumble undoes the point about reliability.
- **The stale claim to retire:** "low-code is for small tools only." In November 2026 business-critical workflows run on these platforms — which makes governance, not ambition, the limiting factor.
