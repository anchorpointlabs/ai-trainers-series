---
id: 02.01.B.K5
tsc: 2
level: Basic
code: K5
title: Prompt construction techniques and settings
---

# Prompt construction techniques and settings

> **TSC #2 Prompt Design · Basic · Knowledge K5**

> **Framework text (verbatim):** "Techniques in prompt construction (e.g., zero shot prompting, one shot prompting, domain-based prompting techniques, instruction prompting, hyper-parameters such as temperature and sampling parameter)."
>
> **TSC #2** Prompt Design · **Basic** · Knowledge · Bullet 3 of 15

**One-line version:** You build a prompt from four moves — instruct, supply a rule, show an example, and set the dials outside it — and the skill is knowing which move the job needs.

## What it is

Prompt construction is assembling the request: a direct instruction, plus any field-specific rules the tool cannot be expected to know, plus sometimes one worked example of the task done correctly. Separately, generation settings — temperature and the sampling parameters — control how the tool picks its words. Those are not part of the prompt; they sit in the tool's controls or its API, and not every product exposes or honours them.

## Deep expansion

### The concept

Four construction techniques carry almost all the weight at this level, and each answers a different question.

**Instruction prompting** answers "what do you want done?" It is a direct, unambiguous verb: label these, rewrite this, list three. It is the floor of every prompt; when a reply goes wrong, the instruction is the first thing to reread.

**Domain-based prompting** answers "what does this field require?" A library's borrowing rule, a clinic's triage order, the way your company numbers invoices. The model does not know your local rules, and it will invent a plausible one rather than ask. Supplying the rule — and telling it to apply only that rule — is the difference between a generic answer and a usable one.

**Zero-shot and one-shot prompting** answer "how will it know the shape of the answer?" Zero-shot gives the instruction and no example. One-shot gives exactly one worked example — an input and its finished output — before the real input. The example is doing pattern-locking, not teaching: it shows a format and a boundary that words find hard to describe.

None of this is a template to fill in mechanically. The four moves overlap, and the right prompt is the shortest one that leaves no important question open.

### The sub-concepts

**Counting examples, not attempts.** Zero-shot means zero worked examples *in the prompt*. Running the same zero-shot prompt a second time is still zero-shot — that is a retry, not a demonstration. This distinction trips up nearly every class.

**Where one-shots go wrong.** With a single example the model over-generalises: it copies incidental details. If your one example uses the name "Birch", expect "Birch" to reappear. If your one example is a positive case, expect a positive lean. One example buys format; it does not buy balanced judgement.

**Where few-shots go wrong.** More examples bring two biases — majority label bias (four of five labelled WAIT produces a WAIT habit) and recency bias (the last example pulls the answer toward itself). A lopsided set teaches the wrong lesson.

**Settings are outside the prompt.** Temperature controls randomness: low makes the highest-probability choice nearly always win, high flattens the field so less obvious words can appear. Top-p keeps only the most likely candidates whose combined probability reaches a threshold; top-k keeps a fixed number of candidates. Typing the word "temperature" into a prompt changes nothing but the subject of the conversation.

**Determinism is a dial, not a switch.** Even the lowest setting is best-effort; rounding differences can flip a close call between two tokens. "Temperature zero" means "very nearly the same", not "identical".

### How it connects to the rest of the framework

`TSC2-Basic-K7` is the concept these techniques serve; `TSC2-Basic-K2` explains why an example or a rule shifts the output at all; `TSC2-Basic-A1` is the ability to describe these techniques out loud; `TSC2-Basic-K4` covers what to do when construction still fails. Settings reappear at `TSC4-Intermediate-K3` when model parameters become a selection decision.

### What is current as of November 2026

Two shifts. First, the dials have largely disappeared from consumer chat interfaces: temperature and top-p now live mostly in APIs and developer consoles, so a Basic learner is usually adjusting *the prompt*, not the sampling. Teach settings as "a thing that exists and is not in your chat box", and demonstrate them only if your room is technical. Second, the frontier models of late 2026 — OpenAI's GPT-6 generation, Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon — have become markedly better at zero-shot following of a precise instruction, which means one-shot examples are less often needed for format and more often used for house style that cannot be described in words.

### Common misconceptions

- *"One-shot means one attempt."* It means one worked example inside the prompt.
- *"The model knows how our organisation does this."* It knows how the internet does this. Your rule is your job to supply.
- *"I can set the temperature by asking for it politely."* Settings are a control on the tool, not a sentence in the message.
- *"More examples always beat fewer."* Past a handful, cost and latency rise and bias creeps in; a well-described rule often outperforms five lopsided examples.

## How a student should understand it

**Mental model:** the difference between telling a new staff member the procedure, showing them one completed form, and adjusting the printer settings. Three different levers, and only two of them are words on the page.

**Things they can do after this bullet:**
1. Count the worked examples in a prompt and name the technique.
2. Add a field-specific rule so the tool stops inventing one.
3. Say where temperature lives and what it does, without claiming precision.

**Misconceptions to kill:** one-shot as "one try"; that local rules are common knowledge; that a prompt can change a setting.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The kopitiam order.** "Kopi-O siew dai peng, dabao" is a compressed domain language: base, two constraints, one modifier, one output format. Every part is doing a job. Where it breaks: a kopitiam has a fixed menu, so the vocabulary is closed; a prompt's vocabulary is open, which is why the instruction must still be explicit.

### Worked example with a real tool

```text
You are helping a fictional library label book availability.

Use this library rule: if there are no copies available, label the book WAIT; if there is at least one copy available, label it READY.

Example:
Input: Atlas — 0 copies available
Output: Atlas: WAIT

Now label each book below. Reply in the same order, with one line per book in the format "Book: LABEL". Give no explanation.

Birch — 3 copies available
Cedar — 0 copies available
Dune — 1 copy available
```

What to point at afterwards: three techniques in one prompt — instruction ("label each book"), domain rule (the WAIT/READY rule the tool could not know), one-shot example (Atlas). Then delete the example and run it again: that is the same task, zero-shot, and it usually still works because the rule is explicit. That comparison is the lesson — examples are a tool, not a requirement. Finally, ask why the reply might come back with an extra sentence despite "give no explanation", and let them discover that instructions to suppress formatting are among the least reliable.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "How might the tool label books differently if we show it one finished example rather than none?" Take predictions; commit them to the board.
2. **State the objective** — by the end you can name the technique in a prompt, add a rule it lacks, and explain where temperature lives.
3. **Recall prior learning** — the one-word comparison from `TSC2-Basic-K2`; same mechanism, now with examples added.
4. **Present the content** — instruction, domain rule, zero/one-shot, and settings as external dials.
5. **Guide** — build the library prompt on screen, then delete one component at a time and predict the effect before running.
6. **Elicit performance** — pairs label a fresh set of five invented books, then write their own rule for a task in their job.
7. **Give feedback** — compare labels against the rule; discuss any line that broke format or invented a copy count.
8. **Transfer** — each learner names a field rule from their workplace that a prompt would have to be told.

## What the framework doesn't mention but trainers need to know

- **The technique should follow the task, not the fashion.** Simple, well-represented tasks do fine zero-shot. Slightly odd formats want one example. Judgement calls with fuzzy boundaries want a written rule plus two or three contrasting examples.
- **Examples leak.** Whatever is in your example can appear in the answer — names, numbers, even a whole sentence. Use placeholder names (`Book A`) when the content is irrelevant to the pattern.
- **Settings matter more for products than for people.** If your learners only ever use a chat window, teach settings as a fact about the tool and spend the saved time on rules and examples.
- **A rule you cannot state is a rule you cannot check.** If the field rule is "use your judgement like our seniors do", the prompt cannot carry it and the review cannot test it.

## Watch out

- **Do not demo settings you cannot control.** If the room's tool does not expose temperature, say so; showing an API dial to an admin audience wastes the session.
- **Do not claim one-shot is better.** It is sometimes better and sometimes worse; the honest claim is that it shows format.
- **Do not let the example become the answer.** Watch for a reply that reuses "Atlas" for a different book — that is the teaching moment, not a failure to hide.
- **The stale claim to retire:** "turn the temperature down and it becomes accurate." Determinism is not accuracy; a confidently wrong answer at low temperature is still wrong.
