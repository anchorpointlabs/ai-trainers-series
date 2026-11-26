---
id: 02.01.B.K7
tsc: 2
level: Basic
code: K7
title: Concept of prompt design
as_at: 2026-11-26
review_by: 2027-02-25
---

# Concept of prompt design

> **TSC #2 Prompt Design · Basic · Knowledge K7**

> **Framework text (verbatim):** "Concept of prompt design."
>
> **TSC #2** Prompt Design · **Basic** · Knowledge · Bullet 1 of 15

**One-line version:** Prompt design is deciding what you want and what the tool needs to know before you type — there is no phrase that unlocks it.

## What it is

Prompt design is the work of turning an intention into a written brief: the task, the facts the task depends on, who the answer is for, and the limits on the answer. The prompt itself is ordinary language typed into a chat box. The design is in what you put in it, and in what you deliberately leave out.

## Deep expansion

### The concept

A chat tool does not receive your intention. It receives your text and continues it. Everything you did not write is supplied by the model from the patterns of everything it was trained on — an average of the internet, not an average of your office. That one sentence explains most of the frustration a Basic learner brings into the room. The notice came out too formal because nothing said who reads it. The date was wrong because no date was given. The reply ran to two paragraphs because nobody said two sentences.

So the design question is not "which words". It is whether the message carries what a competent colleague would need to do the job without asking you anything.

### The sub-concepts

**Task and background are two different things.** The task is the action — write a notice, summarise this. The background is what the action depends on — the date, the room change, the reason, the reader. Learners collapse both into a topic ("library closure") and are then surprised by a generic result. Naming the two separately is the fastest correction a trainer can make.

**The blanks get filled.** A prompt is not a request the model weighs and then decides to answer. It is a sequence the model continues, one token at a time, each token chosen because it is the most probable continuation of everything above it. So a blank is not neutral; it is an invitation for the most statistically ordinary filler. "Write a notice" reliably produces the notice that appears most often in the world, which is nobody's notice.

**Design ends where engineering begins.** Prompt *design* is the one-off instruction in a chat window, with a human reading the reply and fixing it in the next turn. Prompt *engineering* starts when the same prompt must work across many unseen inputs with nobody editing it between runs. A Basic learner is firmly on the design side of that line, and saying so sets an honest bar: good enough to check, not guaranteed.

**Design is not the neighbouring three.** Not context engineering (choosing what data gets assembled before the model runs), not fine-tuning (changing the weights by training), not retrieval (searching an external store and pasting results in). All four appear in one product; only the first is the learner's job this week.

**The brief test.** If a competent colleague could execute your prompt without asking a question, it is designed. If they would have to ask "which room?", the model will not ask — it will guess.

### How it connects to the rest of the framework

This bullet is the concept; `TSC2-Basic-K2` is the mechanism underneath it (why wording changes the output at all); `TSC2-Basic-K5` is the technique set; `TSC2-Basic-A5` names the parts a prompt is built from. Privacy (`TSC2-Basic-K6`) and guardrails (`TSC2-Basic-K4`) are the two constraints that turn design from a writing habit into a professional one.

### What is current as of November 2026

The chat box has become a workspace. Assistants now carry saved instructions, attached files and per-project memory, so a prompt can contain background the learner never typed today — a standing brief running underneath every request. Two consequences: "what is in the prompt" is no longer fully visible to the person typing, and the skill has shifted slightly from composing a message to maintaining a briefing document.

The frontier models of late 2026 — OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon — differ less in whether they can follow a clear instruction than in how literally they read an ambiguous one, how much they pad, and how much context they hold. That is the argument for teaching design over tool lore: a well-formed brief travels between them; a bag of phrase-tricks does not.

### Common misconceptions

- *"There is a magic phrase — 'act as an expert', 'you are a professional writer'."* A role can shift tone and vocabulary. It cannot supply facts you did not give, and it does not raise accuracy on a factual task.
- *"It already knows what I mean."* It knows what the words most commonly mean. Your meeting, your room and your members are not in the words.
- *"If the prompt is clear, the answer must be right."* A clear prompt improves the odds and removes the excuse. It verifies nothing; the reply still has to be checked against the facts you supplied.

## How a student should understand it

**Mental model:** briefing a very capable relief staff member who starts every morning with total amnesia about your workplace — brilliant, willing, and perfectly happy to invent a room number rather than admit they do not know it.

**Things they can do after this bullet:**
1. Separate the task from the background in any request they write.
2. Name the reader and one limit (length, tone, format) before typing.
3. Check a reply against the facts they supplied, not against how convincing it looks.

**Misconceptions to kill:** the magic phrase, the belief that the tool shares their context, and the equation of a fluent answer with a correct one.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The handover note before leave.** You are away for two weeks and must leave instructions for whoever covers you. You would not write "handle the invoices". You would write which invoices, by when, who signs, and what to do when a supplier queries one. Where it breaks: the relief colleague can phone you; the model cannot, so it answers with confidence instead of asking.

### Worked example with a real tool

Type this into a fresh chat in ChatGPT, Claude or Gemini:

```text
Write a two-sentence notice for members of the fictional Meadow Book Club. Tell them their next meeting is on 18 June at 3 pm in the Blue Room, rather than the Green Room. The change is because the Green Room is being painted. Use only these details and do not add any new ones.
```

What to point at afterwards: the task is one clause; everything else is background — audience, date, time, room, reason — plus a limit that forbids invention. Then run "Write a notice for my book club" in a second chat and put the replies side by side. The second is fluent, plausible and useless. That contrast, not the good output, is the lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "A colleague asks for a club notice and gives no details. What would you need before you could write it?" Collect two answers on the board.
2. **State the objective** — by the end you will write a request that names the task and the background, and check the reply against both.
3. **Recall prior learning** — what they already do when emailing a contractor or briefing a new staff member.
4. **Present the content** — task versus background, the blanks being filled, and why no phrase is required.
5. **Guide** — build the Meadow Book Club prompt together, taking suggestions for what must be included and forbidden.
6. **Elicit performance** — pairs write a prompt for a notice from their own workplace, then run it.
7. **Give feedback** — swap prompts; the receiving pair runs them cold and reports any question they had to ask.
8. **Transfer** — each learner names one recurring request from their job they will now write as a brief.

## What the framework doesn't mention but trainers need to know

- **The reply varies between runs.** The same prompt, run twice, can produce different wording. Teach checking as a routine, not as a response to failure.
- **The cost of a bad prompt is invisible.** People quietly fix a weak output by hand and never register that the prompt was the problem. Ask the room how much editing they do — that is the real quality measure.
- **"Prompt design" sounds technical.** It is closer to briefing. Framing it as professional writing lands better with admin and HR audiences than framing it as AI technique.

## Watch out

- **Do not demo a magic phrase.** Even if a role-play line produces a lovely output, it teaches the wrong lesson and the learner chases phrases for a year.
- **Do not promise repeatability.** Chat tools are not deterministic; a trainer who implies "same prompt, same answer" will be contradicted within ten minutes.
- **Do not let one clean run end the exercise.** Ask for a messier input before anyone relaxes.
- **The stale claim to retire:** "you need the special way of talking to AI." In November 2026 the models follow plain, well-specified English; the skill is specification, not password.
