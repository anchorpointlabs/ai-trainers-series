---
id: 08.03.A.A7
tsc: 8
level: Advanced
code: A7
title: Assess AI ethics across disciplines
as_at: 2026-11-26
review_by: 2027-02-25
---

# Assess AI ethics across disciplines

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Ability A7**

> **Framework text (verbatim):** "Assess the interplay of AI ethics with legal, cultural, socio-political and environmental aspects."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Ability · Bullet 11 of 14

**One-line version:** The assessment is not four findings in four columns — it is one decision seen from four sides, including the side that pays.

## What it is

Assessing the interplay means taking a single decision and asking how the legal, cultural, socio-political and environmental dimensions act on each other. Sometimes they reinforce: a system that is lawful, welcomed and cheap to run is unusual but real. More often one buys what another pays for, and the assessment's job is to name which, for whom, and with what evidence. The output is a judgement about a decision, not a survey of four topics.

## Deep expansion

### The concept

The method is a matrix. Rows are the decision's concrete choices — what data is collected, who is enrolled, what the model optimises, how long outputs are retained, who can appeal. Columns are the four dimensions. In each cell, mark whether the dimension supports the choice, conflicts with it, or is neutral, and write the specific reason.

Four patterns recur, and trainers should teach them by name.

**Legal but unethical.** Lawful processing of publicly available data can still be a cultural violation — scraping a community's photographs to train a model that will never serve them. The legal column says yes; the cultural and socio-political columns say this is extraction.

**Accepted but unlawful.** A tool everyone wants may breach a statute — a workplace camera that monitors "engagement" may be popular with managers and still sit outside what the PDPA and employment norms permit.

**Efficient but costly elsewhere.** A model that routes every trivial request through a frontier system is cheap per decision and expensive in aggregate: electricity, water for cooling, and hardware churn that appears on nobody's project budget.

**Benefits one group, costs another.** The most common pattern. The employer gains surveillance capability; the worker loses bargaining power. The platform gains moderation capacity; the moderator absorbs the harm.

### The sub-concepts

**Specificity beats labels.** "Environmental impact" is not an assessment; "1.2 million inference calls a month on a model with no distillation attempt" is. Push every cell down to a measurable choice.

**Power mapping.** For each conflict, ask who can refuse, who can appeal, and who can leave. Those with none of the three carry the cost.

**Evidence per dimension.** Legal: statute, guidance, precedent. Cultural: language coverage, representation in outputs, community consultation. Socio-political: who is monitored, who holds the logs, who can switch it off. Environmental: model size, call volume, hosting region, refresh cycle.

**Reinforcement, not only conflict.** Name the cases where two dimensions agree, because those are the cheapest wins and they are usually overlooked.

**The irreducible conflict.** Some decisions cannot satisfy all four. Record which cost was accepted, by whom, and when it will be revisited.

### How it connects to the rest of the framework

`TSC8-Advanced-K4` supplies the four lenses; this bullet is their interaction. `TSC8-Advanced-A5` is the dilemma analysis when two dimensions are irreconcilable; `TSC8-Advanced-A8` is the team you convene to do the assessment properly; `TSC8-Advanced-K3` is why the legal column changes at a border; `TSC8-Advanced-A1` is where the assessment becomes a gate document.

### What is current as of November 2026

Two dimensions have become harder to keep separate. The environmental one is now a procurement and reporting question in Singapore, where data-centre efficiency standards and tropical cooling constraints make compute visible to facilities and finance. The socio-political one changed shape with agency: an assistant that acts — as the tool layers in OpenAI's GPT-6 generation, Anthropic's Claude 5.5 and Google's Gemini 3.1 Pro and 4 Argon now do — redistributes authority rather than attention, and consent obtained for "a chatbot that answers" does not cover "an agent that transacts". Culturally, the measurable items are dialect coverage and representation in outputs, which is why localised evaluation sets have become the practical instrument for a dimension that used to be discussed only in prose.

### Common misconceptions

- *"Assessment means covering each topic in turn."* Coverage is not interplay; the finding lives at the intersections.
- *"Legal review covers it."* Legal is one column and it is the floor.
- *"Environmental cost is an infrastructure matter."* Model selection and call volume are product decisions.
- *"Culture means translation."* It means register, imagery, representation and who was consulted.

## How a student should understand it

**Mental model:** the durian. Perfectly legal to sell, banned on the MRT and in many buildings, environmentally expensive to ship chilled, and socially loaded in a way no other fruit is. Four dimensions, one object, and every rule about it is a compromise.

**Things they can do after this bullet:**
1. Fill a decision-by-dimension matrix with specific choices, not labels.
2. Name one conflict and who bears its cost.
3. Recommend an option and state the cost it accepts.

**Misconceptions to kill:** four columns equal an assessment, legal equals adequate, and environment is somebody else's department.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The durian.** Legal to sell; banned in lifts, trains and many buildings; chilled air-freight has a real footprint; and it carries social meaning that shapes who eats it where. Nobody assesses a durian policy with one lens. Where it breaks: durian rules are local, visible and enforced by signage, while AI costs are diffuse.

**The used-car inspection.** Four checks — legal (transferable, no outstanding loan), cultural (would your family accept it), socio-political (does the dealer hold the logbook), environmental (fuel and emissions). A car that passes one check and fails another is still a bad purchase. Where it breaks: a car's costs land on the buyer; an AI system's costs often land on third parties.

### Worked example with a real tool

```
A model is lawful, culturally accepted, and environmentally costly.
Find the tension and resolve it.
Give me: (1) the specific environmental cost in measurable terms, (2) who
benefits and who bears it, (3) three options that reduce the cost, (4) which
option you recommend and what it costs in accuracy or convenience.
```

What to point at: the third column is where models are weakest — they propose "use a smaller model" without saying which task degrades. Ask the class to name the task that must not degrade. That single question converts an environmental slogan into an engineering decision, and it is the skill this bullet is for.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — one product decision, four one-line reactions from four colleagues. All defensible, mutually incompatible.
2. **State the objective** — fill the matrix and defend one recommendation.
3. **Recall prior learning** — the four lenses and one conflict from `TSC8-Advanced-K4`.
4. **Present the content** — the four patterns and the specificity rule.
5. **Guide** — build the matrix for the compute-heavy model together.
6. **Elicit performance** — groups assess a live decision from their organisation.
7. **Give feedback** — reject cells that contain labels instead of choices.
8. **Transfer** — each learner adds one dimension to an existing impact assessment that omits it.

## What the framework doesn't mention but trainers need to know

- **Environmental assessment has no audit standard yet.** That makes it the easiest column to leave blank and the easiest to be challenged on later.
- **Cultural harm is measurable.** Dialect failure rates and representation counts turn opinion into evidence.
- **The socio-political column needs names.** "Stakeholders" is not an answer; "the 40 riders on this route" is.
- **Interplay findings belong in the decision record.** Otherwise the matrix is a workshop artefact that nobody reads again.

## Watch out

- **Do not let the class produce four separate essays.** One decision, four readings, one recommendation.
- **Do not treat conflict as failure.** Conflict is the finding; a matrix with no conflict means the analysis was shallow.
- **Do not skip the cost-bearer.** Ask who pays, every time, until it is automatic.
- **The stale claim to retire:** "We did a legal and ethical review." Two columns is not an assessment.
