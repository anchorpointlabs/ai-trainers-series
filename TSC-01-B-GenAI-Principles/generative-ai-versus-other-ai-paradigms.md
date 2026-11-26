---
id: 01.01.B.K5
tsc: 1
level: Basic
code: K5
title: Generative AI versus other AI paradigms
---

# Generative AI versus other AI paradigms

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K5**

> **Framework text (verbatim):** "Difference between generative AI and other AI paradigms."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 5 of 13

**One-line version:** Most AI in a bank decides; generative AI produces. One outputs a label or a number, the other outputs content — and confusing the two is how organisations buy the wrong system.

## What it is

"AI" is an umbrella, not a product. Under it sit rule-based systems, classical machine learning that classifies or forecasts, optimisation engines, robotic control, and generative models. Generative AI is the branch that produces new content rather than a decision, a score or a label. The distinction that survives contact with a workplace is **decision versus creation**, and it holds even as the technologies blur at the edges.

## Deep expansion

### The concept

Draw the room a line with two ends. At one end, a system takes an input and returns **a judgement about it**: spam or not spam, churn or not churn, $4,200 next month, segment B. At the other, a system takes an input and returns **a new artefact**: a reply, a poster, a function.

The first is **discriminative** — it learns the boundary between categories, and its output is small. A spam filter's entire answer is one bit. The second is **generative** — it learns the shape of the data itself and can produce more of it, and its output is large. A drafted reply is two hundred words of judgement calls.

Three consequences follow, and each is a business consequence rather than a technical one:

- **Evaluation differs.** A classifier is judged by accuracy, precision and recall on a labelled test set. A generative output is judged by a human reading it against a brief. You cannot compute the accuracy of a job posting.
- **Failure looks different.** A classifier fails by mislabelling, and the error is countable. A generative model fails by producing something fluent and wrong, visible only to someone who checks.
- **Governance differs.** A credit-scoring model is a regulated decision system with explainability obligations. A drafting assistant is a tool used by a human who remains the author. "We use AI" describes two entirely different risk profiles.

### The sub-concepts

**Discriminative and predictive models.** Trained on labelled examples to output a category or a number: fraud detection, churn prediction, demand forecasting, credit scoring, defect detection, document classification. Most AI already deployed in Singapore banks, insurers, logistics firms and agencies is this. It is usually smaller, cheaper, faster and more auditable than a generative model, and often invisible to staff because it sits inside an existing system.

**Generative models.** Trained to model the distribution of content — text, image, audio, video, code, structured data. Output is a draft artefact. Everything in this TSC sits here.

**Rule-based and expert systems.** The oldest paradigm and still the most common in operations: explicit if-then logic, workflow engines, form validation. Not learning at all, and often the correct answer. A trainer who lets a learner believe "AI" means "learning" will be asked why the leave-application system is called AI.

**Optimisation and recommendation.** Given constraints, find the best assignment: routing, rostering, pricing, "customers also bought". Distinct from both prediction and generation, and frequently mislabelled in vendor decks.

**Agentic systems.** Not a separate paradigm — an application of generative models with tools and a loop. Worth naming because learners will ask, and because the boundary that matters is not "does it generate" but "may it act". That is `TSC1-Basic-A05`, not this bullet.

**Where the line blurs, honestly.** An LLM can be used as a classifier ("label these 400 complaints"), and a modern classifier can generate explanations. Translation and summarisation were sequence-to-sequence prediction before anyone called them generative AI. The distinction is about **what the output is for**, not which architecture is inside. Teach the purpose test, not the architecture test.

### How it connects to the rest of the framework

`TSC1-Basic-K2` is the mechanism both paradigms share — learning from examples. `TSC1-Basic-K3` covers the generative family specifically. `TSC1-Basic-K4` turns this distinction into a fit test. `TSC1-Basic-K6` is the failure list for the generative side. At Intermediate, the discriminative side returns whenever a learner proposes a language model for something a trained classifier would do better and cheaper.

### What is current as of November 2026

- **The generative side consolidated into chat products; the discriminative side did not.** A learner's whole experience of "AI" is now a chat window on a frontier model from OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line, or Google's Gemini 3.1 Pro / Gemini 4 Argon. The fraud model in the back office has not changed shape, and it is still doing most of the measurable work.
- **Language models are being used as classifiers, with mixed results.** For messy unlabelled text — complaint triage, contract type detection — a prompted model with a schema is often the fastest route to a first working system. For high-volume, stable, labelled tasks, a trained classifier is cheaper per call and far easier to defend in an audit.
- **Multimodality widened the generative side.** Image, video and voice are separate model families with separate interfaces — the same category as text generation, not modes of the chatbot. Their failure patterns are visual rather than factual.
- **Agentic products made "act" a third category.** Decide, create, act. Learners meet all three in one interface, which is exactly why the distinction has to be taught rather than assumed.

### Common misconceptions

- *"AI and GenAI are the same word."* They nest. Most deployed AI in a serious organisation is not generative, and most generative deployments are not decisions.
- *"All AI generates content."* A churn model generates a probability. That is the entire output.
- *"'Generative' means smarter."* It means "creates". A generator can be worse than a small, well-tuned classifier at a narrow task — frequently is.
- *"If a model writes the label, it is generative AI."* If the deliverable is a label, it is a classification task being done with a generative tool. Governance follows the deliverable.

## How a student should understand it

**Mental model:** the security guard at the lobby versus the MC at the dinner. One decides who comes in; the other writes and performs the script. Both are useful, both are staff, and no event planner would swap them.

**Things they can do after this bullet:**
1. Classify any system they meet as generative, discriminative or rule-based, and say what its output is.
2. Explain the difference to a colleague in one sentence, without jargon.
3. Give one example of each from their own organisation — including one they never thought of as AI.

**Misconceptions to kill:** that AI means GenAI, that all AI creates content, and that generative is automatically the more advanced choice.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The librarian versus the novelist.** Ask a librarian which of these 400 books are about WWII and you get a list — accurate, fast, finished. Ask a novelist for a chapter set in 1943 and you get prose that reads like the period, with details that may be invented. Both are excellent at their job. Sending the novelist to do the cataloguing wastes money; sending the librarian to write the chapter produces a bibliography. Where it breaks: the librarian never gets it wrong, and the novelist would at least know they were making things up.

**The clinic.** A triage system reads your symptoms and assigns a priority band — a decision, and the output is one word. A generative assistant drafts the letter telling you your appointment is in three weeks — content, and the output is a paragraph you must read before it goes out. Same clinic, two systems, two failure modes.

### Worked example with a real tool

Make the model do the classifying, because the point of the bullet is the sort:

```text
For each system below, answer in one line:
SYSTEM: <name> | TYPE: discriminative / generative / rule-based | OUTPUT: <one word> | WHY: <12 words>

1. Flags a transaction as likely fraud.
2. Writes a product description from a spec sheet.
3. Predicts next month's sales for each outlet.
4. Translates a customer email from English to Malay.
5. Routes a leave application to the right approver based on department and grade.
6. Summarises a 40-page tender into one page.
7. Scores a job applicant from 1 to 100.
8. Draws a poster for a fire drill.
```

What to point at afterwards: rows 1, 3 and 7 all produce **a number or a label** — decisions, whatever engine is inside. Rows 2, 4, 6 and 8 produce **an artefact**. Row 5 is a rule, and it is the one most people call AI because it is automated. Then ask the useful question: which of these eight would you let run without a human reading the output? The answers split along exactly this line, which is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — A spam filter's verdict ("SPAM") next to a drafted customer reply. What is the difference, in one word?
2. **State the objective** — "You will sort any system into decide / create / rule, and say why the difference changes how you check it."
3. **Recall prior learning** — From K2: the model predicts. Now ask: predict *what*, a label or content?
4. **Present the content** — Two columns on the board. Fill the left with systems the room already uses.
5. **Guide** — Run the eight-system prompt, then correct row 5 together.
6. **Elicit performance** — Each pair adds three systems from their own organisation and classifies them.
7. **Give feedback** — Debrief the two hardest: a recommendation engine, and an LLM used as a classifier.
8. **Transfer** — Which of their three would they want explained to an auditor, and in what terms?

## What the framework doesn't mention but trainers need to know

- **The budget follows the paradigm.** A discriminative model on a labelled dataset is usually a data-science project; a generative deployment is usually a change-management project. Different costs, timelines and failure modes.
- **"We already use AI" is often true and often irrelevant.** Existing fraud or routing systems tell you nothing about whether the organisation can govern a drafting assistant.
- **Explainability obligations attach to decisions.** If the output affects someone's eligibility, credit or employment, the paradigm question becomes a regulatory one.
- **Language models as classifiers need a schema and an eval set.** Without a fixed output schema and a hundred hand-labelled examples you cannot tell whether the classifier works — and most pilots skip it.

## Watch out

- **Do not let "AI" do the work of a definition.** Say "predictive model" or "generative model" every time. The vocabulary discipline is the lesson.
- **Do not demo only generative tools.** A room that leaves thinking AI equals chat will buy a language model for a forecasting job.
- **Do not use "traditional AI" as a put-down.** It is the AI that is currently running the business.
- **The stale claim to retire:** "AI means machines that think like humans." Nobody in the deployed-systems business uses that definition, and it makes every later conversation harder.
