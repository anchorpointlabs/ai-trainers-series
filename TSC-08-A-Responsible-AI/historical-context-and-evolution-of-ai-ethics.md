---
id: 08.03.A.K2
tsc: 8
level: Advanced
code: K2
title: Historical context and evolution of AI ethics
as_at: 2026-11-26
review_by: 2027-02-25
---

# Historical context and evolution of AI ethics

> **TSC #8 Responsible AI and Generative AI Practices · Advanced · Knowledge K2**

> **Framework text (verbatim):** "Historical context and evolution of AI ethics."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Advanced** · Knowledge · Bullet 2 of 14

**One-line version:** The questions are seventy years old; only the fluency is new.

## What it is

AI ethics began as a question about machines that make decisions people used to make, and it has run through three eras: the philosophical era, when the worry was whether a machine could be trusted with judgement at all; the algorithmic-accountability era, when scoring systems in credit, hiring and policing were shown to encode human prejudice at scale; and the generative era, where the system produces language, images and actions rather than a number. The concerns rhyme, and knowing the rhymes stops a class treating today's problem as unprecedented.

## Deep expansion

### The concept

The first era is philosophy with a lab attached. Turing's 1950 paper asked whether a machine could imitate a conversation; Wiener's *The Human Use of Human Beings* worried about automation and purpose a year earlier; Weizenbaum built ELIZA in 1966, watched people confide in a script of pattern-matching, and spent the rest of his career warning against exactly the trust his own program attracted. The lesson from that era is already modern: people attribute understanding to systems that have none, and that attribution is a design problem, not a user error.

The second era is measurement. Expert systems in the 1980s put rules into medicine and finance and failed on the edges of their own rulebooks. By the 2010s, statistical scoring had spread into bail, hiring and lending, and investigative journalism in 2016 did to a US risk-assessment tool what auditors now do routinely: it compared error rates across racial groups and found they diverged. That single analysis moved fairness from a philosophical term to a metric with a definition, and the definitions have multiplied ever since. Regulation followed the same path: the GDPR in 2018 made data protection a design constraint, the OECD AI Principles in 2019 gave governments shared vocabulary, UNESCO's Recommendation in 2021 gave it a normative text, and Singapore's IMDA framework gave the region an operational one.

The third era is scale and agency. From late 2022 systems stopped classifying and started composing — fluently, at a length nobody could check by eye. The 2024 IMDA framework for generative AI, the EU AI Act's entry into force the same year, and the *Moffatt v. Air Canada* tribunal ruling — where a company was held to its chatbot's invented bereavement policy — mark the moment governance shifted from "is the model fair" to "who owns what the model says and does". By 2026 the live question is autonomy: what may a system do on your behalf before a human is required to approve.

### The sub-concepts

**Four questions recur.** Is it fair? Can we see inside it? Who answers for it? What does it do to the people whose work it changes? Every era asks all four; each era changes which one is urgent.

**Each era adds a mechanism, not a moral.** Statistics added scale — prejudice encoded once, applied a million times. Generative models add fluency — wrong answers that read like right ones. Agents add action — a wrong answer that has already sent the email.

**Settled questions should stay settled.** That removing race and gender columns makes a model fair was disproven by practice years ago; proxy variables reconstruct protected attributes from postal code, school and language. A class that re-opens this loses an hour and gains nothing.

**Singapore's arc is its own.** The Model AI Governance Framework, the AI Verify testing toolkit, Project Moonshot for LLMs, and the PDPC's advisory guidelines on AI recommendation and decision systems form a local lineage worth teaching by name, because learners will be asked about these in interviews.

### How it connects to the rest of the framework

`TSC8-Advanced-K1` is the current map of standards this history produced; `TSC8-Advanced-K3` is the cross-border problem the history created; `TSC8-Advanced-A5` is the dilemmas each era handed forward; `TSC8-Advanced-A9` is the next chapter, written for domains no framework yet covers. `TSC8-Advanced-A3` inherits its method directly: adversarial testing is the professionalised version of the 2016 error-rate comparison.

### What is current as of November 2026

The history has a live edge. The EU AI Act's prohibitions took effect in February 2025 and its high-risk and general-purpose obligations are phasing in, so the second era's "voluntary principles" period is closing. The genuinely new item on the timeline is agentic deployment, which has no settled governance anywhere, and synthetic media at election scale, which Singapore addressed through the Elections (Integrity of Online Advertising) Amendment rather than through AI-specific statute.

### Common misconceptions

- *"AI ethics started with ChatGPT."* It started with automation and judgement, and the fairness metrics used in audits today predate large language models by a decade.
- *"Bias is a new problem caused by big models."* Bias is older than the models; scale makes it cheaper to deploy, not newly invented.
- *"The old debates were resolved."* They were operationalised, unevenly. Fairness metrics still conflict mathematically; the argument moved from "is fairness possible" to "which fairness".
- *"History is exam material."* It is argument material: the fastest way to kill a bad proposal is to name the decade in which it already failed.

## How a student should understand it

**Mental model:** the same family argument held in three generations — grandfather argues about whether machines should decide anything, father argues about whether the scoring was fair, and the grandchild argues about what the chatbot promised the customer. Same table, new complaint.

**Things they can do after this bullet:**
1. Name one pre-LLM milestone and say what it established.
2. Explain what each era added — scale, fluency, agency — rather than what it replaced.
3. Take a current concern and trace its older root.

**Misconceptions to kill:** that this began in 2022, and that bias arrived with generative models.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The same exam paper, reset every decade.** The questions — fairness, opacity, accountability, effect on work — are printed identically. What changes is the case study at the top of the page: a 1980s credit rule, a 2016 risk score, a 2026 agent that books travel.

### Worked example with a real tool

```
Trace one current concern — AI-generated video of a public figure saying
something they never said — back through AI ethics history.
Give me: (1) the oldest comparable concern, (2) what is genuinely new in
2026, (3) which older regulatory response is the closest precedent and why
it does or does not fit.
```

What to point at: models will reach for photography manipulation, propaganda and counterfeit goods as precedents — all defensible. The teaching point is the third column: the closest institutional precedent is provenance and labelling (C2PA-style signed metadata, watermarking), which descends from transparency arguments, not from content law. That is how history becomes a design tool rather than trivia.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — play a two-line ELIZA-style exchange, then a modern chatbot reply to the same input. Ask what changed.
2. **State the objective** — place any current AI concern into its historical lineage and name what is new.
3. **Recall prior learning** — earlier bullets on bias and privacy: these are the second era's legacies.
4. **Present the content** — three eras, one mechanism added each, four recurring questions.
5. **Guide** — do the deepfake trace together on the board.
6. **Elicit performance** — pairs pick a concern from their own sector and date its root.
7. **Give feedback** — correct the "everything is new" answers and the false precedents.
8. **Transfer** — each learner notes for their manager what is old, what is new, what to do.

## What the framework doesn't mention but trainers need to know

- **Regulation follows scandal, not foresight.** The GDPR followed data-breach headlines; the EU AI Act followed years of bias reporting. Expect the next wave after the first serious agentic incident.
- **The "AI winter" lesson is about overpromising.** Two collapses in funding followed claims that outran capability. The same dynamic now appears as vendor claims about autonomy.
- **Singapore's contribution is procedural, not philosophical.** Teach AI Verify and Project Moonshot as the local answer to a global argument about evidence.

## Watch out

- **Do not deliver a timeline recital.** Dates without consequences are forgettable; each milestone must land as a change in what was expected of builders.
- **Do not claim firsts you cannot source.** "First regulation" claims invite correction and cost credibility.
- **The stale claim to retire:** "AI ethics is a new field." It is an old field with a new instrument, and the instrument is what changed.
