# PRM-01 · Anatomy of a prompt: role, task, context, format, constraints

**Framework home** — New GenAI TSC #2 Prompt Design (Basic): A5 *define the fundamental elements of a prompt*; K7 *concept of prompt design*; A6 *identify best practices for designing effective prompts*. This is the entry-level spine of the whole course.

---

## What it actually is

A prompt is not a sentence. It is a **specification** — a short document that removes ambiguity from a request. The five elements that do the work:

1. **Role** — who the model should answer as. Useful because it narrows vocabulary and standards ("as a payroll officer" vs "as a HR director" produce different levels of detail). Weak when it is ornamental: "you are a world-class genius" changes tone, not accuracy.
2. **Task** — the verb and the object. "Summarise" is not a task; "summarise for a manager who has 30 seconds and must decide whether to approve" is.
3. **Context** — the facts the model cannot know: audience, prior decisions, constraints, the document itself, what "good" looks like here.
4. **Format** — the shape of the answer: table, five bullets, 120 words, JSON with three keys, email with subject line.
5. **Constraints** — what must not happen: no invented figures, no recommendations, quote only from the text, flag anything uncertain, British spelling, no jargon.

The order is not sacred, but the completeness is. Most "bad prompts" are missing elements 3 and 5, not elements 1 and 2 — people tell the model *what to do* and forget to tell it *what world it is doing it in*.

A useful discipline: write the five labels out literally in the prompt the first few times. Once learners see the labels working, they can drop them.

## Why it matters at work

The difference between a usable draft and a rewrite is usually 20 extra words of specification. Teams that learn this stop treating AI output as a lottery and start treating it as a brief — which is a skill they already have from managing vendors, interns and agencies.

## The student lens

**Mental model to install:** you are not chatting, you are briefing. If a competent new colleague could not act on your message without asking two questions, the prompt is incomplete.

**Misconceptions you will hear:**
- *"Longer is better."* No — *specified* is better. Padding with politeness adds tokens, not clarity.
- *"The magic words matter."* "Please", "kindly", "you are an expert" are tone, not specification.
- *"I don't know what context to give."* Then answer three questions: who reads this, what do they already know, what decision follows.

**Five-minute practice:** take a real email they wrote this week, strip it to one sentence, then rebuild it with all five labels. Run both versions. Compare. The gap is the lesson.

## The adult educator lens

**Analogy:** a prompt is a **work order**, not a request. A work order for a contractor says what, where, to what standard, in what finish, by when. "Please build something nice" is not a work order; you would not accept the result, and neither should you accept the output.

**Three-minute demo:**
1. Type: "Write an email about the retrenchment." Watch the room wince at the generic, tone-deaf result.
2. Rebuild it live with the five labels: role (HR business partner), task (notify a team of a role redundancy, with dignity), context (12-person team, one affected, union-covered), format (180 words, three short paragraphs, no subject line), constraints (no legal admissions, no timelines, offer a private meeting).
3. Run it. Let the silence do the teaching.

**Board sketch:** five boxes in a row labelled ROLE / TASK / CONTEXT / FORMAT / CONSTRAINTS. Under CONTEXT write "who reads it, what they know, what happens next". Under CONSTRAINTS write "what must not appear". Keep this on the whiteboard for the rest of the day; point at it every time a learner's prompt fails.

**Where it goes wrong in class:** the sceptic says "real work is too messy for a template". Agree, then show the messy version *with* the labels still visible — the labels survive complexity; they are not a form to fill.

**Check for understanding:** give them a prompt that produces a bad answer and ask which of the five elements is missing. If they can name it, they have the model.

## Say this out loud

"A prompt is a work order. If a new colleague couldn't act on it, neither can the model."

## Content hook

**LinkedIn opener:** "Everyone is collecting prompt 'formulas'. Almost nobody is writing a complete brief. Five labels fix 80% of bad output."

**Carousel idea:** "Same ask, five versions" — one slide per version, each adding one element, with the output alongside. The visual improvement curve does the persuading.
