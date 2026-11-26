---
id: 09.01.B.K1
tsc: 9
level: Basic
code: K1
title: Fundamentals of AI model security
as_at: 2026-11-26
review_by: 2027-02-25
---

# Fundamentals of AI model security

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Basic · Knowledge K1**

> **Framework text (verbatim):** "Fundamental concepts of AI model security, including importance of monitoring and reporting risks."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Basic** · Knowledge · Bullet 1 of 8

**One-line version:** An AI model has no wall between instructions and information — anything it reads can become an order, so the safety net is watching what it does and reporting what looks wrong.

## What it is

AI model security is the practice of protecting a system that uses a generative model from being manipulated, robbed, or made to act against its owner's interest. It is not mainly about the model's code. It is about the whole path a message travels: what enters the model, what the model does with it, and what the application does with the answer. Monitoring and reporting are part of the definition, not an afterthought, because a system nobody watches is a system nobody can defend.

## Deep expansion

### The concept

Traditional software separates instructions from data. A database engine is told, in a fixed grammar, which part of a query is the command and which part is a value, so a value can never turn into a command. A language model has no such separation. The developer's system prompt, a document pulled from a shared drive, and the customer's message are all tokens in one stream, weighted by the same attention. Nothing in the architecture marks one stretch of text as law and another as content.

That single fact produces the whole discipline. If data can be read as instruction, every text the model touches is a potential entry point: an email, a resume, a calendar invite, a support ticket, a page a browsing tool fetches. Security shifts from "is the code correct" to "what can reach the context window, and what may the model do once it has".

The framework's second half — monitoring and reporting — follows from this. Because the weakness cannot be patched out of the model, protection is mostly detection and response: log what the model was given, log what it decided, watch for the shape of an attack, and give staff a route to raise a suspicion. A bank stops fraud by watching transactions, not by hoping.

### The sub-concepts

**The prompt is an input channel, not a question box.** Every text field that reaches a model is an interface into the system, with the same standing as a login form. Learners who see a chat box as "just typing" will not see the attack surface.

**The model is a confident interpreter, not a parser.** A JSON parser rejects malformed input with an error. A model accepts everything and produces something. It has been trained to follow instructions it finds, so obeying an attacker is not a malfunction — it is the model doing its job on the wrong authority.

**Confused deputy.** The model holds authority the application gave it — read the inbox, query orders, send mail — but cannot tell whether an instruction came from the developer, the user, or a stranger's document. It takes orders from whoever speaks last.

**Tools are the blast radius.** A model that only prints text can embarrass you. A model that can send email, issue refunds or run queries can cost you money and data. The security question changes the moment agency is added.

**Data is both target and weapon.** The same material is what attackers want to take — customer records, the system prompt, business logic — and what they use to get in: a poisoned document, a hidden instruction in a web page.

**Monitoring and reporting.** Three things get watched: inputs (what arrived), decisions (which tool the model proposed, with which arguments), and outcomes (what the tool actually did). Reporting is the human channel that turns a strange transcript into an incident with a number.

### How it connects to the rest of the framework

`TSC9-Basic-K2` is the testing counterpart — you probe for these weaknesses before launch. `TSC9-Basic-K3` is the control layer. `TSC9-Basic-A1` is spotting an attack in a transcript; `TSC9-Basic-A2` is writing the risk down. At Intermediate, `TSC9-Intermediate-K1` widens the same idea into a full control set, and `TSC9-Intermediate-A2` turns it into layered defence against prompt attacks.

### What is current as of November 2026

The frontier models of late 2026 — OpenAI's GPT-6 generation (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra and the security-tuned Cyber), Anthropic's Claude 5.5 line, Google's Gemini 3.1 Pro and Gemini 4 Argon — are harder to trick with a crude "ignore your instructions" than their predecessors, because vendors now train an instruction hierarchy: developer messages outrank user messages, and user messages outrank retrieved text. That is a real improvement and not a fix — and these are also the models being wired to tools and browsers, which raises the cost of a successful trick.

- **Hierarchy reduces frequency, not possibility.** A document can still be written to sound like the developer.
- **Guardrails now ship as a platform feature.** Input and output classifiers are usually a switch. Switched on is not the same as working; it has to be tested.

### Common misconceptions

- *"Security is the vendor's job — we use a commercial model."* Vendors train a model to refuse universal harms like weapons instructions. They know nothing about your refund limit, your customer rows or your inbox. Your business logic is yours.
- *"It is only text, so the worst case is a rude answer."* Text that reaches a tool becomes an action; text that reaches a browser becomes a request to an outside server.

## How a student should understand it

**Mental model:** a brilliant new intern with the keys to the office, who cannot tell a manager from a stranger, and who does exactly what the last piece of paper said.

**Things they can do after this bullet:**
1. Name the three entry points: the user's own message, a document the system reads, a tool the system calls.
2. Explain to a colleague why "we told it not to" is not a control.
3. Say what should be logged and who to tell when something looks wrong.

**Misconceptions to kill:** that security means code review only; that internal equals safe; that a model which refuses bad things is therefore secure.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The brilliant, gullible intern.** A fresh graduate who has read every book in the National Library, drafts a report in three seconds, and has zero street smarts. The CEO asks for a summary and gets one. Then a courier hands over a letter saying "urgent instruction for the intern: photocopy the contract on your desk and mail it to this address" — and the intern does it, because every sentence read is a sentence obeyed. Where it breaks: the intern eventually learns; the model does not.

**The sticky note on the invoice.** An accounts-payable clerk in a locked back office at a Raffles Place SME. Nobody off the street can walk in. But suppliers post invoices in, and one carries a Post-it: "Finance policy update — pay to this new account." The locked door was never the vulnerability. The document was.

### Worked example with a real tool

Ask the room to design an assistant that summarises a shared inbox. Type this into any chat model as a planning prompt:

```
I want an AI assistant that reads our shared customer-service inbox
and drafts replies. Before I build it, list:
1. every kind of text that will enter the model,
2. what an attacker could hide in each one,
3. what the assistant may do, and what it must never do without
   a human clicking approve.
```

What to point at afterwards: the input list always contains something the learner did not think of — a signature block, an attachment, a forwarded chain. That is the surface. The second list is the blast radius. Neither is about the model's code.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a two-line email containing a hidden instruction, then ask what the assistant will do with it.
2. **State the objective** — by the end, they can name the entry points, the blast radius and the monitoring duties for one real assistant.
3. **Recall prior learning** — phishing: a message pretending to be from the boss. Same trick, new victim.
4. **Present the content** — no wall between instruction and data; confused deputy; tools as blast radius; monitoring and reporting.
5. **Guide** — work the inbox example together, filling the lists on the whiteboard.
6. **Elicit performance** — pairs pick a system they use and list its inputs, tools and one thing to log.
7. **Give feedback** — debrief: which lists missed the document path, which granted a tool for convenience.
8. **Transfer** — each learner writes one sentence to their manager about what to watch.

## What the framework doesn't mention but trainers need to know

- **Agency is the dividing line.** The same model is low risk as a drafting tool and high risk as an agent with send rights. Ask "what can it touch" before "how smart is it".
- **The dangerous combination is ordinary.** Private data plus outside text plus a way out is what most useful assistants have.
- **Reporting needs a destination.** "Report it" is meaningless without a named channel. Ask who they would tell today; the silence is the lesson.

## Watch out

- **Do not demo an attack you cannot contain.** Show a transcript, not a live exploit against a system in the room.
- **Do not overclaim the fix.** "New models are safer" is true only in the narrow sense of refusing obvious harm.
- **Do not let the lesson become a lecture on transformers.** The usable idea is "instructions and data share one stream". One sentence, then consequences.
- **Retire the stale claim:** "AI security is a model problem." In November 2026 it is an architecture, logging and human-process problem wrapped around a model that will occasionally be fooled.
