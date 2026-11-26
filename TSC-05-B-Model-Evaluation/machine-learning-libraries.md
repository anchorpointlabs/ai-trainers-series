---
id: 05.01.B.K1
tsc: 5
level: Basic
code: K1
title: Machine learning libraries: the toolbox evaluation runs on
as_at: 2026-11-26
review_by: 2027-02-25
---

# Machine learning libraries: the toolbox evaluation runs on

> **TSC #5 Generative AI Model Evaluation · Basic · Knowledge K1**


> **Framework text (verbatim):** "Machine learning libraries (e.g., TensorFlow, PyTorch, Keras)."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Knowledge · Bullet 1 of 11

**One-line version:** You do not have to write the evaluation code yourself — but you do have to recognise the three library names, because every evaluation report, tutorial and job listing assumes you can tell them apart.

## What it is

Machine learning libraries are ready-made toolkits of code that people use to build, train and test AI models. TensorFlow, PyTorch and Keras are the three names that appear most often. At Basic level the point is not to code in them. It is to recognise what they are, what each one is for, and what it means when a report says a model was evaluated "in PyTorch".

## Deep expansion

### The concept

A library is a collection of pre-written building blocks — the maths, the training loops, the evaluation functions — that someone else wrote so you do not start from a blank page. Think of it as the difference between a chef who forges her own knives and one who buys them. The chef's skill is in the cooking, not the metallurgy; the evaluator's skill is in judging the output, not re-implementing the neural network.

The framework puts this bullet first because it is scaffolding: almost everything else in TSC #5 is *described* in the language of these tools, even when the learner never opens one. A learner who freezes at "TensorFlow" will miss the actual point of every evaluation metric that follows.

### The sub-concepts

**TensorFlow.** A Google-built library that is strong for *production* — training a model, then serving it at scale inside a product. Older tutorials and many enterprise systems use it.

**PyTorch.** A Meta-built library that became the default for *research*. Most frontier model labs release their model *weights* in a format that loads in PyTorch. When a paper says "we evaluated in PyTorch", that is usually what it means.

**Keras.** A friendlier layer that sits on top of a heavier library (historically TensorFlow). It is designed so a person can describe a model in a few readable lines. Good to know as "the approachable one".

**A library is not a model.** This is the distinction that matters most. TensorFlow and PyTorch are toolkits; GPT-6, Claude 5.5 and Gemini 4 are models. A library contains no knowledge on its own — it is the scaffolding the model's weights run on. Learners routinely conflate the two.

### How it connects to the rest of the framework

This bullet is the plumbing. `TSC5-Basic-K2` (the evaluation criteria) is *what* you measure; `TSC4-Intermediate-K1` (how models work inside) is *why* the toolkits exist; `TSC7-Basic-K1` (model development) is where you would actually train a model and therefore genuinely need these libraries. For a Basic evaluator, the libraries matter mostly as vocabulary — you read them, you do not operate them.

### What is current as of November 2026

The most useful shift is this: **most commercial model evaluation no longer touches a library at all.** When you evaluate GPT-6 Terra or Claude 5.5, you send text to an API and receive text back — no PyTorch, no TensorFlow. The libraries matter for people who *host* open-weight models themselves (loading Llama, Qwen, or Singapore's SEA-LION weights locally). So the honest framing for a Basic class is: "you will meet these names in writing; you will only use them if you later move to self-hosting."

### Common misconceptions

- *"TensorFlow and PyTorch are competing AI models."* They are toolkits, not models. Two teams can evaluate the *same* model using either one.
- *"I have to learn these before I can evaluate anything."* Only if you are training or self-hosting. Evaluating a commercial model through an API needs none of them.
- *"A library is what makes the model smart."* The library holds the machinery; the intelligence is in the trained weights.

## How a student should understand it

**Mental model:** a garage full of professional tools. You can judge whether a car drives well without being the mechanic — but you should know a spanner from a socket, because the mechanic's report is written in those names.

**Three things they can do after this bullet:**
1. Read a model card or evaluation report and say whether "evaluated in PyTorch" means "trained in a research toolkit" or "run through an API" (usually the former).
2. Name the three libraries and one word each: TensorFlow (production), PyTorch (research), Keras (approachable).
3. Correct someone who calls a library a model — in one sentence, without jargon.

**Misconceptions to kill:** that the libraries are the AI, that learning them is a prerequisite, and that evaluating a commercial model requires coding.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker's kitchen.** The wok, the cleaver and the gas stove are tools; the dish is the model's output. A food critic does not need to season the wok to judge the char kway teow. But the critic who knows "this was fried in a cast-iron wok on high heat" reads the review with more authority than one who does not. The libraries are the wok — worth naming, not worth operating, for the critic's job.

**The engine and the car.** PyTorch and TensorFlow are engine-building kits; a GPT or Claude model is the finished car. You can drive the car without opening the bonnet. The analogy breaks only in one place: for self-hosted open-weight models you *are* the mechanic, so the toolkit becomes your daily job.

### Worked example with a real tool

Open the Hugging Face page for an open model (for example, a Llama or Qwen variant). Point at the line that names the library — "PyTorch" — and the file type — "safetensors". That is the entire demonstration:

```
Where it says:  "Library: PyTorch"  →  the toolkit the weights load in
Where it says:  "Model type: LlamaForCausalLM"  →  the model itself
```

What to point at afterwards: the library and the model are two separate lines, because they are two separate things. That one screenshot does more than twenty minutes of explanation.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — hold up a phone and ask: "which part of this is a library and which part is a model?" Let them guess wildly.
2. **State the objective** — by the end, you will read a model card and not be confused by the three library names.
3. **Recall prior learning** — they already use ChatGPT/Claude/Gemini; ask what they think "runs" it.
4. **Present the content** — the three names, one word each, plus "library ≠ model".
5. **Guide** — open one real model card together and name each line.
6. **Elicit performance** — in pairs, each pair opens a different model card and reports "library" vs "model type".
7. **Give feedback** — correct the pairs who swapped the two; praise the ones who caught the safetensors detail.
8. **Transfer** — ask each learner to find one place in their own work where they saw a library name and now understand it.

## What the framework doesn't mention but trainers need to know

- **Hugging Face is the de facto hub.** The framework names three libraries but not the platform where most weights live. A Basic learner benefits more from knowing "go to Hugging Face to see a model card" than from any library's API.
- **The library-versus-framework distinction.** TensorFlow is often called a framework and Keras a library. Do not let the vocabulary battle eat class time; the actionable difference is production-versus-research-versus-approachable.
- **API users are the majority of your classroom.** Most learners will never install a library. Teach the names as reading vocabulary, not as a coding task — otherwise you lose the room in the first ten minutes.

## Watch out

- **Do not turn this into a coding lesson.** The moment you open a code editor you have left Basic evaluation and entered TSC #7 territory. One screenshot, then move on.
- **Do not overclaim "you will never need this".** The learner who later self-hosts SEA-LION for data-residency reasons will need exactly this. Say "you will not need it *for evaluation of commercial models*".
- **The stale claim to retire:** "you must learn Python and PyTorch to work with AI." In November 2026 most people's entire working relationship with AI is a chat box and an API key — the libraries are optional equipment, not the front door.
