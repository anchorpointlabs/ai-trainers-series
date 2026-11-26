---
id: 06.01.B.A1
tsc: 6
level: Basic
code: A1
title: "Wiring a model into an application: the prompt, the parameters and the contract"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Wiring a model into an application: the prompt, the parameters and the contract

> **TSC #6 Generative AI Application Development and Deployment · Basic · Ability A1**


> **Framework text (verbatim):** "Apply effective prompt engineering and model configuration to integrate foundational models into applications."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Ability · Bullet 7 of 11

**One-line version:** In an application, the prompt is not a message — it is the specification, and the parameters are how much freedom you grant while it is followed.

## What it is

Integrating a foundation model means treating it as a component with an interface: a system instruction that defines the job, a user input carrying the data, parameters that set how the model samples, an output contract the code can rely on, and error handling around all of it. Prompt engineering in an application is prompt engineering with a contract attached.

## Deep expansion

### The concept

In a chat window, a prompt is a request and a human reads the answer. In an application, code reads the answer. That single change reshapes every decision. Ambiguity a human would resolve charitably becomes a parsing error; variation a human would find creative becomes an intermittent bug.

So the work splits into three parts learners must keep distinct. The **instruction** says what the model must do, in what role, with what rules and what it must refuse. The **configuration** — model choice, temperature, output length, format, timeout, retry — changes behaviour as much as wording does. The **contract** is the shape of output your code accepts, and what happens when it is not produced.

The third part separates a demo from an integration. A model is an unreliable function: it usually returns what you asked for. The application must be built for the times it does not.

### The sub-concepts

**The system prompt is the constitution.** Set once, applied to every call: role, rules, output format, refusals. Short enough to obey, specific enough to test. A long system prompt is not more thorough; it is more places to be contradicted.

**Temperature and top-p.** Both control randomness. Temperature 0 does not guarantee identical output — it makes repetition most likely. Low for extraction and classification; higher for drafting. Set one, not both, unless you can explain why.

**The output contract.** Ask for a named structure, then validate it in code. A schema the model is told about is a strong hint; a schema the API enforces is a guarantee, and current APIs support the enforced kind.

**Statelessness.** The model remembers nothing between calls. This is the goldfish with a PhD: brilliant for thirty seconds, then it forgets. Re-paste the clean blueprint rather than trusting a long, drifting conversation.

**The model is a setting, not a commitment.** Model name in configuration, pinned version, one interface that can point elsewhere. Model names change; your integration should not have to.

### How it connects to the rest of the framework

`TSC2-Basic` and `TSC3-Basic` are the prompt craft underneath this; this bullet is that craft under a contract. `TSC6-Basic-K1` supplies the context, `TSC6-Basic-A2` builds the retrieval that fills it, and `TSC6-Basic-A5` is where the parameters live and are maintained.

### What is current as of November 2026

- **Structured output is first-class.** Current APIs — the GPT-6 family, Claude 5.5, Gemini 3.1 Pro — accept a schema and constrain generation to it. Teach that, not the old routine of begging for JSON and regexing it out.
- **Reasoning modes changed the advice.** The flagships now think before answering, so "think step by step" is redundant or counterproductive; specify outcome, constraints and audience instead. Some reasoning modes no longer expose temperature at all, which breaks older tutorial code.
- **Prompt caching made long system prompts affordable**, provided the instruction block never changes — which shifts the trade-off in favour of a fuller constitution.

### Common misconceptions

- *"Temperature 0 means the same answer every time."* Most likely, not identical. Do not build a test suite that assumes determinism.
- *"The model remembers my last call."* It does not. Your app remembers; the model sees only what you send.
- *"If it returns JSON, it is valid JSON."* Not unless the schema was enforced. Parse, catch, retry once, then fail loudly.

## How a student should understand it

**Mental model:** a job description plus a discretion clause. The instruction says what the job is, the parameters say how much latitude the holder has, the contract says what must be on the desk at the end of the day.

**Three things they can do after this bullet:**
1. Write a system prompt with a role, rules, output format and explicit refusal behaviour.
2. Choose parameters that match the task, and say why.
3. Wrap a model call in validation, a retry and a clear failure, so the app never silently accepts garbage.

**Misconceptions to kill:** that prompting ends at wording, that temperature is a quality dial, and that a working call is an integrated call.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The hawker stall's standing order.** "Kopi, no sugar, less milk" is the system prompt — fixed, repeated to every new cook, never renegotiated. The parameters are strength and cup size: same order, different pour. Where it breaks: a cook having a bad day still makes drinkable kopi; the model on a bad day makes confident nonsense, which is why the contract must catch it.

**The goldfish with a PhD.** Brilliant, fast, knows the field, forgets you the moment you turn away. You would not brief this colleague once and assume it stuck.

### Worked example with a real tool

A tuition centre wants enquiries classified so admin can route them. Type this into an API playground, notebook or an app builder's AI step:

```
System:
You classify enquiries for a tuition centre. Return exactly one object:
{"subject": one of ["FEES","SCHEDULE","TEACHER","ENROLMENT","OTHER"],
 "urgency": one of ["LOW","MEDIUM","HIGH"],
 "parent_name": string or null,
 "summary": one sentence, maximum 20 words}

Rules: HIGH urgency means the parent mentions withdrawing, a refund, or a
complaint about safety. If the message is not about the centre, use OTHER.
Never invent a parent name that is not stated.

User: {{enquiry_text}}
```

Set alongside it: low temperature, output constrained to the schema, a timeout, one retry with backoff.

What to point at afterwards: run the same enquiry three times and show the output is stable but not byte-identical. Raise the temperature and watch a field drift outside the allowed values — proof the schema must be enforced, not requested. Remove the parent-name rule and watch a fabricated name appear. Three settings, three behaviours, one paragraph of instruction.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — paste a customer email and ask the room to write the instructions a new admin would need to sort it identically. Their list is a system prompt, and longer than they expected.
2. **State the objective** — by the end you can write an application-grade system prompt, set parameters for a task, and enforce an output contract.
3. **Recall prior learning** — prompt structure from TSC #2 and #3; the stateless API and context window from K1.
4. **Present the content** — instruction, configuration, contract; what each parameter changes.
5. **Guide** — build the classifier prompt together, then break it deliberately: no format, no refusal rule, high temperature.
6. **Elicit performance** — pairs write a system prompt for their own task with a defined schema, then run five real inputs.
7. **Give feedback** — project two prompts and ask which failure was the instruction's fault and which the configuration's.
8. **Transfer** — each learner writes the parameters they would set for their own use case, one reason per line.

## What the framework doesn't mention but trainers need to know

- **The prompt is source code.** It belongs in version control with a changelog, not in a text box edited last quarter. When outputs shift, the prompt diff is the first thing to read.
- **Log input, output, model version and parameters.** Without all four, no output is reproducible and no regression is diagnosable.
- **Refusals need designing, not discovering.** An app never told what to refuse will refuse arbitrarily, or comply.

## Watch out

- **Do not let conversational folklore into an application.** Tricks that impress in chat often destabilise machine-parsed output.
- **Do not demo only the happy path.** The retry, the validation failure and the refusal are the integration.
- **The stale claim to retire:** "add 'think step by step' to every prompt." On reasoning models in 2026 it is redundant; on others it is a weak substitute for specifying the task.
