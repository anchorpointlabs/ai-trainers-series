# COT-01 · Chain-of-Thought (and when it makes things worse)

**Framework home** — New GenAI TSC #3 Prompt Engineering, **Advanced**: K *advanced prompt techniques (e.g. Chain-of-Thought, Tree of Thought prompting)*; A *devise innovative prompt strategies*. Deliberately not a Basic Prompt Design item — placing it correctly is half the teaching.

---

## What it actually is

Chain-of-Thought (CoT) is the practice of asking a model to **externalise intermediate steps** before committing to an answer: "work through this step by step, show your reasoning, then state the conclusion."

Why it helps: a model producing an answer in one pass has to compress every intermediate calculation into a single forward jump. Generating intermediate tokens gives the model more computation to spend on the problem — and gives *you* something to audit. That second benefit is the one trainers under-sell. CoT is as much a **debugging and trust device** as an accuracy device.

Three important nuances for 2026:

1. **Reasoning models changed the default.** Models with built-in reasoning modes already generate internal deliberation. Adding "think step by step" to those can be redundant, and occasionally counter-productive — you are instructing a system that already does it, and you may flatten its internal strategy.
2. **CoT is not proof.** A well-written chain can be a fluent rationalisation of a wrong answer. The steps are generated text, not an audit trail of hidden computation. Never present CoT as verification.
3. **It costs tokens and time.** For classification, extraction, formatting and rewriting, CoT usually adds cost without adding accuracy. It earns its keep on multi-step arithmetic, policy application, causal judgement and anything with a decision tree.

There is also a known tension: forcing visible reasoning can hurt on tasks where the model's implicit judgement is better than its articulated reasoning (some safety and fairness judgements are the standard example). Worth one slide, not ten.

## Why it matters at work

Analysts, auditors and case officers are frequently asked to trust an AI conclusion. CoT gives them something to read, critique and challenge — and gives the trainer a legitimate way to say "check the steps, not just the answer".

## The student lens

**Mental model to install:** show your working, like a maths exam — but remember that a neat page of working has never guaranteed a right answer.

**Misconceptions you will hear:**
- *"If I ask it to think step by step, the answer is correct."* No; it is *checkable*, which is different.
- *"CoT always improves output."* Only on tasks with genuine intermediate steps.
- *"The model is hiding its real reasoning when it doesn't show steps."* It is not hiding a transcript; it is generating one when asked.

**Five-minute practice:** give the model a two-step policy question (e.g. leave eligibility with two overlapping rules) three ways — no instruction, "think step by step", and "list the rules, apply each, then conclude". Compare the three answers and, crucially, mark which steps were wrong.

## The adult educator lens

**Analogy:** asking a colleague for a decision versus asking for the **case file**. The case file lets you disagree at paragraph three instead of rejecting the whole answer. CoT turns an opinion into a case file — sometimes a well-argued wrong one.

**Three-minute demo:**
1. Ask a genuinely multi-step question with no CoT instruction. Get the answer.
2. Ask again with "show your working, number each step."
3. Then break it: change one premise and re-run, so the room watches the reasoning adapt — and watches it confidently produce a different conclusion from the same faulty premise.
4. Land the point: the value is auditability, not truth.

**Board sketch:** two columns — "tasks that need steps" (multi-rule eligibility, cost breakdowns, pros/cons with constraints, root-cause) and "tasks that don't" (rewrite this email, extract these fields, classify this ticket, translate this). Ask the room to sort five of their own tasks into the columns.

**Where it goes wrong in class:** someone says "so reasoning models make prompting obsolete". Answer: no — it moves the trainer's job from *eliciting* reasoning to *specifying* the task and *auditing* the reasoning. That is a harder, more valuable job.

**Check for understanding:** "Name a task in your job where showing the steps would make a wrong answer easier to catch, and one where it would just cost more tokens."

## Say this out loud

"Chain-of-Thought doesn't make the model right. It makes it arguable — and arguable is what you actually need."

## Content hook

**LinkedIn opener:** "'Think step by step' is the most repeated prompt advice on the internet, and half the people repeating it are using it on tasks that don't have steps."

**Reel idea:** screen recording of a correct-looking CoT answer that collapses when one premise is changed — 45 seconds, no voiceover, captions only. Title: "Confident is not correct."
