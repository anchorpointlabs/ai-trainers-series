---
id: 04.03.A.A1
tsc: 4
level: Advanced
code: A1
title: Deploy models for specialised tasks
as_at: 2026-11-26
review_by: 2027-02-25
---

# Deploy models for specialised tasks

> **TSC #4 Generative AI Model Selection · Advanced · Ability A1**

> **Framework text (verbatim):** "Deploy existing models for a variety of specialised tasks or creative applications (including using techniques such as pre-training or fine-tuning)."
>
> **TSC #4** Generative AI Model Selection · **Advanced** · Ability · Bullet 5 of 8

**One-line version:** Specialisation is a ladder — prompt, then retrieve, then tune — and you climb only when the rung below has been proven insufficient.

## What it is

A specialised task (drafting Singapore legal correspondence, triaging insurance claims, generating on-brand product copy) is served by taking an existing general model and adapting it, then running it as a stable monitored service. There are four adaptation routes and two hosting patterns, and the deployable skill is choosing the cheapest adequate combination and shipping it with a version pin and a monitoring loop.

## Deep expansion

### The concept

The ladder has four rungs, in ascending order of cost and commitment:

1. **Prompting** — describe the task, give two or three examples, specify the output format. Hours of work, no assets to maintain.
2. **Retrieval** — keep the prompt but inject relevant private or fast-changing content at query time. Days to weeks, and it buys freshness and citations.
3. **Fine-tuning** — train an adapter to teach a *behaviour*: a house style, a strict schema, an internal shorthand. Weeks, and it creates a maintenance obligation.
4. **Continued pre-training** — train on billions of unlabelled domain tokens. Months and serious money, justified only when the language or modality is essentially absent from existing models.

The rule that separates competent practitioners from enthusiasts: **climb only when the rung below has been measured and found insufficient.** Most failed enterprise projects are a rung-three solution to a rung-one problem.

### The sub-concepts

**What each rung is actually good for.** Prompting handles general tasks, tone control, formatting and short-context reasoning. Retrieval handles facts that change or that the model never saw. Fine-tuning handles form — schema obedience, jargon, a brand voice — and also compression, by distilling a huge prompt into a small model. Continued pre-training handles missing language or modality, and nothing else.

**What each rung cannot do.** Retrieval cannot teach a model a new writing style or a reasoning pattern it lacks. Fine-tuning cannot teach facts: it has no citations, cannot forget a deleted record on request, and blends new facts with old weights. Prompting cannot compensate for a model that simply cannot do the task at all.

**They compose.** The mature pattern is all three at once: a fine-tuned small model that reliably emits a strict schema, inside a retrieval pipeline that supplies current facts, steered by a structured system prompt. The rungs are not exclusive; they are layers.

**Hosting follows adaptation.** A vendor API is quickest and shifts operations to the provider; a managed cloud endpoint gives control without hardware; self-hosted open weights give residency and unit-cost control at the price of an engineering team. Pick the hosting pattern after the adaptation route, because an open-weight-only adaptation forces the hosting question.

**Deployment is not done until it is pinned and watched.** Six artefacts determine behaviour: model snapshot, prompt template, sampling settings, tool schemas, retrieval configuration, guardrails. All six get versions, and the service gets an evaluation gate.

### How it connects to the rest of the framework

`TSC4-Advanced-K2` is the theory of these rungs; this bullet is their application. `TSC4-Advanced-K3` is the deployment half in detail. `TSC4-Advanced-K4` prices the commitment each rung creates. `TSC4-Intermediate-A2` is the sibling skill on the same ladder — steering a model to a domain or style with prompts and examples — and `TSC4-Intermediate-A1` supplies the cost comparison that usually decides between rungs two and three.

### What is current as of November 2026

With current frontier models, the practical change is that the lower rungs got much stronger:

- **Long context weakened the case for retrieval in small corpora.** A few hundred pages can now be passed directly. The case for retrieval returns as soon as the corpus is large, changes often, or needs per-user access control.
- **Native tool use and strict structured outputs removed a whole class of glue code.** "It must return valid JSON" is now a configuration flag, not a fine-tuning project.
- **Adapter hosting is a platform feature.** You can fine-tune and serve without owning GPUs, so the barrier to rung three is now judgement rather than infrastructure.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Our task is specialised, so it needs a custom model."* Specialised vocabulary is usually a prompt problem. Specialised *form* is a fine-tuning problem. Specialised *facts* are a retrieval problem.
- *"Fine-tuning is how you make the model an expert in our industry."* Fine-tuning changes how it writes, not what it knows.
- *"A prototype that works is a deployment."* A deployment has a version, a gate and a monitor.
- *"We will pick the hosting later."* The adaptation route often forecloses it, so the order matters.

## How a student should understand it

**Mental model:** a four-speed gearbox. First gear is a good prompt and gets you up most hills. You shift up only when the engine is straining — and you do not start a journey in fourth.

**Things they can do after this bullet:**
1. Choose an adaptation route for a stated task and justify it against the rung below.
2. Sketch the deployment: what is pinned, what is monitored, what triggers rollback.
3. Recognise the three failure signatures — wrong rung, missing citation, unmonitored drift.

**Misconceptions to kill:** that specialisation implies fine-tuning, that a prototype equals a deployment, and that hosting is a separate later decision.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tailoring ladder.** Off-the-rack with a good belt (prompt). Off-the-rack, altered (fine-tune). Bespoke from a tailor who keeps your measurements on file (fine-tune plus maintenance). Made from hand-woven cloth because nobody weaves that pattern (continued pre-training). The last one is justified about once a decade, and the shop that sells it to everyone is selling vanity.

**The open-book exam.** Retrieval is being allowed to bring the textbook. It turns a memory problem into a lookup problem, which is exactly right for policy that changes — and useless if the exam is about writing in your company's voice, which no textbook contains.

### Worked example with a real tool

Run the same task three ways in ten minutes, in one chat window:

```text
You are replying to a customer about a delayed parcel. Policy: refunds
are issued after 10 working days. Our tone: warm, brief, no emoji,
never promise a date we cannot keep.
Write the reply in under 90 words.
```

Then repeat with two example replies pasted in as style anchors, then once more with a three-line extract of the actual policy inserted and a request to cite the clause. What to point at afterwards: the first output is already acceptable; the second matches the house voice; the third can be audited. Each rung bought something different, and none of them needed a training run. That is the lesson — price the rung against the value it adds.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a generic reply and a house-voice reply side by side; ask which one would survive a customer complaint.
2. **State the objective** — by the end you can pick a route and defend why the cheaper one is not enough.
3. **Recall prior learning** — the pre-train/fine-tune distinction, and what RAG does.
4. **Present the content** — the four rungs, what each buys, what each costs to maintain.
5. **Guide** — walk the three-way demo live, naming the value added at each step.
6. **Elicit performance** — pairs get a task card and must justify a route in two sentences.
7. **Give feedback** — debrief, challenging every "we would fine-tune it".
8. **Transfer** — each learner writes the route and the deployment gate for one real task.

## What the framework doesn't mention but trainers need to know

- **The ladder is a budget argument, not a purity argument.** If a fine-tune is genuinely needed, do it — but arrive with the comparison that shows the prompt route failed.
- **Retrieval adds its own failure surface.** If the retriever returns the wrong page, a perfect generator produces a confident wrong answer. Evaluate retrieval and generation separately.
- **Access control decides between retrieval and everything else.** Row-level permissions cannot be baked into weights. If different staff must see different content, retrieval is not optional.
- **Some "specialised tasks" are classification tasks in disguise.** If the output is one of five labels, an encoder model is the right tool and the whole generative ladder is overkill.
- **Deployment gates are political as well as technical.** Get the data protection officer and InfoSec into the design conversation before the demo, not after.

## Watch out

- **Do not demo fine-tuning as the punchline.** The impressive demo is the prompt that works, because it is the one the room can repeat on Monday.
- **Do not claim a custom model is more accurate without a test set.** "It feels more ours" is not evidence.
- **Do not present the ladder as a maturity model.** Fine-tuning is not "more advanced"; it is more expensive and more committed.
- **The stale claim to retire:** "you need a bespoke model to handle a specialised domain." In November 2026, prompt plus retrieval handles most of what enterprises call specialised.
