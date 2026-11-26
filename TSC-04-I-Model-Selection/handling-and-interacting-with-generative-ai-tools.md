---
id: 04.02.I.K4
tsc: 4
level: Intermediate
code: K4
title: Handling and interacting with generative AI tools
as_at: 2026-11-26
review_by: 2027-02-25
---

# Handling and interacting with generative AI tools

> **TSC #4 Generative AI Model Selection · Intermediate · Knowledge K4**

> **Framework text (verbatim):** "Steps in handling and interacting with generative AI tools."
>
> **TSC #4** Generative AI Model Selection · **Intermediate** · Knowledge · Bullet 4 of 11

**One-line version:** Using a tool well is a loop you can write down — state the task, supply context, set the format, run, check, adjust — repeated with the settings recorded, not guessed.

## What it is

"Handling" a generative tool has two halves. The **interaction loop** is how you get good output: brief, run, inspect against the goal, revise. The **handling discipline** is the part nobody teaches — knowing which setting caused the variation, reading an error instead of restarting, and recording what you changed so the result is repeatable.

## Deep expansion

### The concept

Most frustration with these tools comes from changing two things at once and therefore learning nothing. The loop only compounds if each iteration changes one variable: the instruction, the example, the format constraint, or a setting. Record which, and after five iterations you know your task.

That is also why "handling" is a selection skill. Much of what looks like model failure is a settings or input failure, and diagnosing it correctly decides whether you change the tool or change your usage. Teams that never diagnose buy a bigger model for a prompt problem.

### The sub-concepts

**The loop, written down.** State the task in one sentence. Supply the material and the audience. Specify the output contract. Run. Check against the goal, not against your taste. Revise one thing. Repeat.

**Temperature is the main variance dial.** Near zero, the model takes the highest-probability token each step: steady, repetitive, best for extraction, classification and anything you will diff. Above one, the distribution flattens: more variety, more invention, more factual drift. Creative drafting wants it higher; a claims extractor wants it at the floor — and even there, GPU arithmetic can produce small differences, so "identical every time" is an aspiration, not a guarantee.

**Nucleus and top-k sampling are the tail cutters.** They discard the unlikely tail so the model cannot wander into nonsense. In practice you adjust temperature and leave the rest alone unless you have a specific reason.

**Max output length is a budget, not a suggestion.** Setting it too low truncates mid-sentence; setting it too high invites rambling. For structured output, keep it tight.

**Errors are information.** A rate-limit error means concurrency or quota, not a broken model. A context-length error means the input plus the requested output exceeds the window — trim the input or shorten the ask. A schema failure means the model produced prose around the JSON. Reading the error code is faster than regenerating and hoping.

**Structured output should be enforced, not requested.** If the platform supports schema-constrained decoding, the model physically cannot emit invalid syntax. That removes a whole class of failures that prompt wording can only reduce.

### How it connects to the rest of the framework

`TSC4-Intermediate-A5` is the assessment version: vary a setting, compare outputs, log the difference. `TSC4-Intermediate-A4` is the lens you apply when checking the result. `TSC4-Intermediate-K2` covers the prompt side of the loop. `TSC4-Advanced-A4` is what happens when this discipline is applied to twenty systems instead of one.

### What is current as of November 2026

Current frontier tools have changed the handling experience in three ways:

- **Reasoning modes changed the timing.** A thinking mode can pause for many seconds before the first visible token. If you assume the request has hung and resend it, you pay twice and get two answers.
- **Structured output and tool calling are configuration, not prose.** The reliable pattern is a schema, not a paragraph asking nicely for JSON.
- **Caching rewards prompt structure.** Static content at the front of the payload unlocks input discounts; content that changes per request at the front destroys them. That is a handling habit with a price tag.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Temperature zero means deterministic output."* It maximises consistency; it does not guarantee identity. Model updates, floating-point variation and batching can still move a token.
- *"More attempts will fix it."* Re-running the same prompt at the same setting samples the same distribution. Change something or accept the mode.
- *"The tool broke."* Read the error. Rate limits, context limits and schema failures are the overwhelming majority.
- *"Settings are advanced."* They are the difference between a tool that feels random and one that feels reliable.

## How a student should understand it

**Mental model:** a camera. Aperture, shutter and ISO are three dials; changing all three at once and hoping teaches you nothing. Change one, look, change one, look.

**Things they can do after this bullet:**
1. Run the interaction loop and name which single variable they changed each time.
2. Predict the effect of a temperature change before running it.
3. Diagnose a rate-limit, context-length or schema error from its message.

**Misconceptions to kill:** that one run is a result, that settings are someone else's concern, and that an error means the model is unreliable.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The aircon remote.** Temperature, fan speed and mode. Change all three and you cannot tell which one made the room cold. Change one and wait two minutes.

**The kopi order.** "Kopi, less sweet, hot" gets you a specific drink; "coffee" gets you whatever the stall decides. Settings are the "less sweet".

### Worked example with a real tool

Run the same task twice, changing only the dial:

```text
Run: "Summarise this in 3 bullets" at temperature 0.2, then again at 0.9.

Text: "Our Tampines outlet opens 7.30am. The Jurong outlet is closed for
renovation until March. Online orders now ship same-day before 11am."
```

What to point at afterwards: at 0.2 the bullets are near-identical across repeats and the facts are stable. At 0.9 the ordering, emphasis and occasionally the framing shift — and if you run it five times, one version will emphasise the renovation while another buries it. Ask which they would ship to a queue that routes customers by branch, and let the room conclude that variance is a defect for extraction and a feature for drafting.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — run one prompt five times; show five different answers.
2. **State the objective** — by the end you can run the loop, predict a setting's effect and read an error.
3. **Recall prior learning** — sampling and why output varies.
4. **Present the content** — the loop, temperature, length, structured output, error diagnosis.
5. **Guide** — walk the two-temperature demo, narrating the single change.
6. **Elicit performance** — pairs pick a task, run it at two settings, log the difference.
7. **Give feedback** — compare logs; correct those that changed three things.
8. **Transfer** — each learner writes the settings they would standardise for their own task.

## What the framework doesn't mention but trainers need to know

- **Record your settings or you cannot reproduce your own success.** A good output with no settings recorded is an anecdote you cannot repeat next month.
- **Long conversations degrade.** As history grows, cost rises per turn and the model starts losing earlier instructions. Summarise and restart rather than letting a chat run for hours.
- **Streaming changes perceived speed, not actual speed.** Showing tokens as they arrive makes a slow model feel responsive; it does not reduce end-to-end time.
- **Uploaded files are not memory.** Each new conversation may not retain what you attached last time; assume context resets.
- **The prompt you paste into a chat window is not the prompt you would ship.** Shipping means a template, a version and a test.

## Watch out

- **Do not treat the chat interface as the production interface.** It is a workshop, not a deployment.
- **Do not demo settings as a magic trick.** Explain what changed in the distribution, or the room learns superstition.
- **Do not paste client data into a consumer tool to demonstrate something.** Check the retention terms first — the demo becomes an incident otherwise.
- **The stale claim to retire:** "just try again until it works." Iteration without a changed variable is a slot machine.
