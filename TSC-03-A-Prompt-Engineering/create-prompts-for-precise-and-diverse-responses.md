---
id: 03.03.A.A1
tsc: 3
level: Advanced
code: A1
title: Create prompts for precise and diverse responses
as_at: 2026-11-26
review_by: 2027-02-25
---

# Create prompts for precise and diverse responses

> **TSC #3 Prompt Engineering · Advanced · Ability A1**

> **Framework text (verbatim):** "Create prompts to elicit precise and diverse responses from AI models."
>
> **TSC #3** Prompt Engineering · **Advanced** · Ability · Bullet 8 of 13

**One-line version:** Precision is narrowing the model's options until only one shape fits; diversity is widening them along named axes until the options genuinely differ — and you cannot do both in one call.

## What it is

Two goals that pull in opposite directions. A **precise** response matches the exact shape you specified: fields, labels, length, order, no commentary. A **diverse** response explores genuinely different options rather than ten paraphrases of one idea. Precision is produced by constraint; diversity by directed variation. This ability is the craft of building each on purpose, and of sequencing them when a task needs both.

## Deep expansion

### The concept

Every prompt defines a distribution over possible responses. Precision work narrows it: an enum, a schema, a table with named columns, a length range, an explicit "no other text", and a low temperature all push probability mass onto one acceptable shape. Diversity work widens it — but widening alone produces noise, not range: ten outputs that differ in wording and agree in substance. Real diversity comes from naming the axes along which you want difference: audience, register, risk appetite, length, channel, angle, price position.

The two conflict because they are the same dial turned in opposite directions. A prompt that demands a strict table *and* creative freedom produces either a table with bland content or creative content that ignores the table — and the model chooses which constraint to drop silently. The professional pattern is sequential: **diverge, then converge.** Generate wide against explicit axes, select against explicit criteria, then reformat the winner precisely.

### The sub-concepts

**Count the degrees of freedom.** Audience, length, format, tone, scope, certainty. Any you leave unnamed, the model fills with the most common convention in its training data — which is why unexplained prompts produce the same competent, forgettable answer every time.

**Precision needs a checkable output.** A defined schema, a fixed set of allowed labels, a table with named columns, a word range. If you cannot write a rule that decides pass or fail, you have described a preference rather than specified a shape.

**Diversity needs axes, not adjectives.** "Be creative" is not an instruction; it is a mood. "Ten taglines: three warm, three blunt, two self-deprecating, two competitive" produces range, because the axes are explicit and can be checked.

**Sampling settings widen the tail; prompts widen the range.** Higher temperature and nucleus sampling make individual word choices less predictable, which is a weak form of diversity. Explicit axes plus multiple calls give controlled variation you can reproduce and evaluate.

**Quantity then selection is a legitimate method.** Ask for ten, filter against criteria, keep two. That is often cheaper than trying to write one prompt that lands the perfect option first time — and it makes the criteria visible.

**The same task can need both, in order.** A brand exercise may want thirty directions and one finished layout. Recognising the two phases is the skill; conflating them is the common failure.

### How it connects to the rest of the framework

Bullet 3 (`TSC3-Advanced-K3`) is the sequencing that makes diverge-then-converge work; Bullet 9 (`A2`) is the analysis that tells you which lever produced which shift; Bullet 10 (`A3`) is how you prove the precise prompt actually is precise across cases. Bullet 13 (`A6`) composes both into pipelines, and Bullet 6 (`K6`) is where repeated precision becomes a template with a schema.

### What is current as of November 2026

- **Precision became a platform feature.** Where a structured output schema can be supplied, the format is enforced at generation rather than requested in prose. The prompt's job shrank to saying which schema and what belongs in each field.
- **Reasoning-shaped models collapse diversity by default.** The late-2026 frontier models (GPT-6 generation, Claude 5.5, Gemini 3.1 Pro, Gemini 4 Argon) are tuned to converge on the best answer, which makes them excellent for precision and reluctant for range. Diversity work moved to explicit axes, multiple parallel calls, and sometimes an older or cheaper model.
- **Batch generation made the quantity-then-select pattern cheap.** Generating ten candidates in one request and choosing among them is now normal practice rather than a luxury.

### Common misconceptions

- *"Be creative produces diversity."* It produces the model's default idea with more adjectives. Name the axes.
- *"Precise means short."* Precision is about the shape of the answer, not its length; a precise answer can be long.
- *"Temperature is the diversity lever."* It is the weakest one. Axes and multiple calls do more, and more reproducibly.
- *"I can ask for a strict format and open exploration."* You can ask; you will get one of them, chosen by the model, without being told which.
- *"Ten options means ten ideas."* Usually it means three ideas and seven restatements; check before presenting.

## How a student should understand it

**Mental model:** the tailor. Measurements are precision — chest, waist, length, no negotiation. Three fabric-and-cut sketches are diversity. You choose the sketch, then the measurements are taken; nobody takes measurements on three garments at once.

**Things they can do after this bullet:**
1. Write one prompt optimised for a checkable shape and one optimised for range, for the same task.
2. Name which levers serve which goal, and which conflict.
3. Sequence the two: generate wide, select, then reformat precisely.

**Misconceptions to kill:** that creativity is a setting; that constraints and range can coexist in one instruction; that ten outputs are ten ideas.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tailor at People's Park.** You do not say "make something nice". You give measurements, and separately you look at three cuttings and choose one. Where it breaks: a tailor asks questions when a measurement is missing; a model invents the missing number, so an unnamed degree of freedom becomes a silent assumption.

**The zi char order versus the chef's recommendation.** "Kopi-O siew dai, peng, dabao" is precision — five parameters, no ambiguity, same drink every time. "Chef, recommend something" is diversity — and you get a range only if you add "one soupy, one fried, one vegetable". Where it breaks: a stall's menu bounds the range; a model's range is bounded only by what you name.

### Worked example with a real tool

```text
Precision: List the 5 risks of this plan as a table with columns Risk,
Likelihood (High/Med/Low), Owner. No other text.
```

```text
Diversity: Give 10 taglines for a pickleball club, each in a different
emotional register.
```

Run both. The first should return exactly five rows and three columns, and a single stray sentence is the diagnostic: the format instruction was not strong enough, or the schema should be enforced instead. The second returns ten lines — now sort them in the room. Typically three are the same joke, four share a word, and only two or three are genuinely distinct. Then rewrite the diversity prompt with named registers (competitive, self-deprecating, community-minded, nostalgic, aggressive) and run again. The comparison is the lesson: range comes from the axes, not from the word "different".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a "ten ideas" output and ask the room how many distinct ideas it contains. They will say four.
2. **State the objective** — build a precision prompt with a checkable shape and a diversity prompt with named axes, and know which is which.
3. **Recall prior learning** — the difference between a brief that says "something nice" and one that says "A4, two colours, logo bottom right".
4. **Present the content** — degrees of freedom; precision levers; diversity axes; the diverge-then-converge sequence.
5. **Guide** — run the table prompt, then the tagline prompt, then the tagged version.
6. **Elicit performance** — learners write both versions for one task from their work, plus the pass/fail check for the precise one.
7. **Give feedback** — score the precise outputs against the checks the learners wrote; count distinct ideas in the diverse set.
8. **Transfer** — each learner picks one recurring task and writes the divergence prompt they will keep.

## What the framework doesn't mention but trainers need to know

- **Diversity without a selection criterion is a party trick.** Ten options and no way to choose is not a decision aid. Always pair range with the criteria for picking.
- **Precision often belongs in a schema, not a sentence.** Where the platform supports structured output, describe the fields and let enforcement do the work; prose formatting instructions are the fallback.
- **Repetition is the tell for laziness.** If two options share the same joke or the same noun, the model is not exploring; it is padding. Teach learners to say "these three are the same idea — replace them".
- **Constraints fight.** Word limits plus mandatory inclusions produce compression that drops the least-repeated item. Predict it rather than being surprised.
- **Cost scales with candidates.** Ten candidates times a thousand runs is ten thousand generations; range has a budget, and the budget belongs in the design conversation.

## Watch out

- **Do not let "creative" stand in for specification.** It is the word that produces the most generic output in the room.
- **Do not demo diversity with five options that are the same idea.** Sort them in front of the class; the embarrassment is the teaching.
- **Do not teach precision as "add more rules".** Three tested constraints beat fifteen untested ones.
- **Do not skip the convergence step.** The deliverable is usually one artefact, not a menu.
- **The stale claim to retire:** "turn the temperature up for creativity." In November 2026 range comes from named axes and multiple calls; temperature mostly adds wobble.
