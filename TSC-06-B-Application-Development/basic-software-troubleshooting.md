---
id: 06.01.B.K5
tsc: 6
level: Basic
code: K5
title: "Troubleshooting by procedure: read the error, find the doc, change one thing"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Troubleshooting by procedure: read the error, find the doc, change one thing

> **TSC #6 Generative AI Application Development and Deployment · Basic · Knowledge K5**


> **Framework text (verbatim):** "Basic software troubleshooting steps (e.g., interpret help resources and documentation)."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Knowledge · Bullet 5 of 11

**One-line version:** Troubleshooting is not intuition — it is a short, boring procedure that most people skip at step two.

## What it is

Basic troubleshooting is a fixed sequence: reproduce the problem, read the whole message, isolate the cause by changing one thing at a time, check the official documentation for the exact term, and record what you did. "Interpreting help resources" means reading a documentation page the way its author intended — including the version selector and the deprecation banner most readers miss.

## Deep expansion

### The concept

The instinct under pressure is to change several things at once and hope. It works often enough to be reinforcing, which is why it survives. It also destroys the information you need: if it starts working after four changes, you do not know which one fixed it, so you cannot prevent the next occurrence or explain the fix to anyone.

The procedure exists to protect causality. One variable per attempt, and a written record of what you tried. It is slower for the first ten minutes and dramatically faster for the next hour — the trade a trainer has to sell, because the room has been rewarded for the other behaviour for years.

A second skill sits inside this bullet: reading documentation. Vendor docs are structured predictably — parameters, examples, error tables, changelog, deprecation notices, and a version switcher in the corner. Learners who learn that structure stop searching for answers and start navigating to them.

### The sub-concepts

**Reproduce before you fix.** If you cannot make it happen on demand, you cannot know you have fixed it. Note the input, the sequence and the environment.

**Read the whole message.** Not the first line. The stack trace names the file, the line and the call; the clause after the colon often names the cause; the part after "however" names the limit you crossed.

**The error string is the search key.** Strip your own paths, IDs and variable values, keep the library and the exact wording. Searching a paragraph gets you an unrelated thread from 2019.

**One change at a time.** Change the key, rerun. Change the model name, rerun. Write down each attempt and its result. Keep a known-good baseline so the difference is the search space.

**Version first.** The most common cause of "the documentation is wrong" is that it documents a different version than the one installed. Check the selector, the changelog, `--version`.

**The documentation hierarchy.** Official reference (authoritative) → changelog (what moved) → examples (the working shape) → status page (is it them?) → community answers (fast, often stale) → the support ticket (last, and only with evidence).

### How it connects to the rest of the framework

`TSC6-Basic-K3` supplies the failure catalogue this works through; `TSC6-Basic-A3` is what to do when the procedure runs out of road; `TSC6-Basic-A4` is the specialised version for speed and cost. `TSC6-Basic-A5` is where most of these faults are introduced.

### What is current as of November 2026

- **The assistant is now step one.** Pasting a traceback with context into Claude, ChatGPT or Gemini resolves much of the routine case faster than documentation browsing — and regularly invents parameter names, error codes and documentation pages. Treat the answer as a hypothesis, never a citation.
- **Documentation search moved into the editor.** Copilot, Cursor and Claude Code read the installed library's own source and docstrings, which is often more accurate than the vendor site for the version you actually have.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Restart it and hope."* Restarting clears state; it does not tell you what broke. A data point, not a strategy.
- *"If the documentation says it, it is true for me."* Version, plan and region all change what is true.
- *"The model is at fault."* More often than not the request never reached the model, or reached it malformed.

## How a student should understand it

**Mental model:** an electrician tracing a tripped circuit. You do not replace the fuse box. You isolate, one breaker at a time, until the faulty circuit identifies itself.

**Three things they can do after this bullet:**
1. Reproduce a fault, capture the exact message, and reduce it to a searchable fragment.
2. Read a documentation page and find the parameter, the version and any deprecation notice.
3. Run a one-change-at-a-time sequence and keep a record someone else could follow.

**Misconceptions to kill:** that speed comes from changing more at once, that documentation is for other people's versions, and that an assistant's fix is a verified fix.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The aircon technician's first three questions.** Is the remote on the right mode, is the filter clean, is the unit receiving power. Every technician asks them before opening anything; every customer finds it faintly insulting. The obvious checks catch most faults, which is why professionals do them first and amateurs skip them.

**The HDB breaker board.** One switch per circuit, labelled if you are lucky. You flip one, observe, flip it back. A householder who flips all of them at once gets the lights on and learns nothing.

### Worked example with a real tool

A Streamlit app that suddenly stops answering. Paste the traceback and the last change into an assistant:

```
Here is the full traceback and the last change I made. Give me:
(a) the three most likely causes, ranked, with reasoning;
(b) for each, the single check that would confirm or eliminate it;
(c) the exact documentation page and parameter name to look for.

Rules: do not suggest reinstalling anything before (b); do not invent URLs —
if unsure, give me the search terms and say you are unsure.

Traceback:
  File "app.py", line 24, in <module>
    client = OpenAI()
  openai.OpenAIError: The api_key client option must be set either by passing
  api_key to the client or by setting the OPENAI_API_KEY environment variable
```

What to point at afterwards: the diagnosis is right and fast, and the third suggestion is a plausible fix involving an environment variable that does not exist. The learner's procedure — confirm, one change, rerun — catches that in thirty seconds. The assistant is not the problem; the missing procedure is.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — break something live. Delete the key, rerun, let the room watch the traceback appear.
2. **State the objective** — by the end you can run the procedure and read a documentation page without guessing.
3. **Recall prior learning** — the triage from K3: model, configuration, provider.
4. **Present the content** — the procedure, the search-fragment technique, the documentation hierarchy, the version trap.
5. **Guide** — work the same broken app together, narrating each check and each dead end honestly.
6. **Elicit performance** — pairs get a fault each (wrong model name, missing key, oversized file, expired key) and write a five-line record.
7. **Give feedback** — read two records aloud. Ask which one a colleague could follow at 9am tomorrow.
8. **Transfer** — each learner writes the procedure into their team's runbook, with who to ask when it fails.

## What the framework doesn't mention but trainers need to know

- **The record is the real output.** The fix helps once; the record helps every time. Make learners write it even when the fix was obvious.
- **Environment drift beats code bugs.** "Works on my machine" means a different package version, key or region. Ask for versions before asking for code.
- **Assistants fabricate API surface confidently.** It will invent `client.set_key()` because the name is plausible. Verify against the installed package.

## Watch out

- **Do not fix it for them during the exercise.** A rescued learner learns that waiting works.
- **Do not demo only faults you planted.** Real faults are messier, and the room can tell.
- **Do not let "ask the AI" become the whole procedure.** It is a fast first hypothesis and a poor final authority.
- **The stale claim to retire:** "search Stack Overflow for the error." For current SDK versions, reading the source beats it.
