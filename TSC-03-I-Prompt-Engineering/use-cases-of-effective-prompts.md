---
id: 03.02.I.K5
tsc: 3
level: Intermediate
code: K5
title: Use cases of effective prompts
---

# Use cases of effective prompts

> **TSC #3 Prompt Engineering · Intermediate · Knowledge K5**

> **Framework text (verbatim):** "Use cases of effective prompts."
>
> **TSC #3** Prompt Engineering · **Intermediate** · Knowledge · Bullet 5 of 13

**One-line version:** Naming the use case is the design step — every recurring task has a prompt shape that fits it, and a failure it invites.

## What it is

Use cases of effective prompts are the recurring task shapes of real work: summarising, extracting, classifying, drafting, transforming, brainstorming, translating, comparing, planning and answering over documents. Each has a shape — the two or three sentences that change the output — and a characteristic failure. Knowing the catalogue is what stops a learner from writing one generic prompt and blaming the model.

## Deep expansion

### The concept

"Use case" is not "industry". A use case is a repeatable operation on a document or a decision: the same verb, the same kind of input, the same kind of output, done again next week. That repetition is what makes it teachable, because the standard of quality is set by the task rather than by taste. A summary is good if the reader can act on it. An extraction is good if every field is right and traceable to the source. A classification is good if two people, or two runs, put the same borderline case in the same bucket.

Ten shapes cover most office work. Teach the shape and the failure together; a shape without its failure is a template, and templates get used where they do not belong.

1. **Summarise.** Shape: length, reader, what must survive, what may be dropped. Failure: a confident compression that loses the exception, the qualifier or the number.
2. **Extract.** Shape: named fields, types, verbatim versus normalised, and a line for what to do when a field is absent. Failure: an invented value in an empty field.
3. **Classify.** Shape: the label set with a definition per label, one label per item, a borderline rule, examples at the boundary. Failure: label drift between runs and bias toward whichever label appears most in the examples.
4. **Draft.** Shape: audience, purpose, the facts allowed, a house-style sample, length. Failure: generic corporate register plus invented specifics.
5. **Transform or rewrite.** Shape: source, target register and medium, the facts that must survive verbatim. Failure: silent mutation of a name, a figure or a date.
6. **Brainstorm.** Shape: quantity, an explicit demand for difference, constraints, banned clichés. Failure: ten versions of one idea in ten costumes.
7. **Translate or localise.** Shape: target language and variety, glossary of terms that must not change, names retained. Failure: terminology drift and mistranslated numbers.
8. **Compare or recommend.** Shape: criteria, evidence required, output as a table, the rule for the recommendation. Failure: a confident ranking with no stated criteria.
9. **Plan or checklist.** Shape: steps, owners, dependencies, what could go wrong. Failure: a generic project plan that fits any project.
10. **Answer over documents.** Shape: sources delimited, citations required, an abstention line. Failure: blending two documents, or answering from the model's own memory instead of the source.

### The sub-concepts

**Shape means the few sentences that change behaviour.** In practice most failures trace to one of four missing items: the reader, the length, the field list, or the line that says what to do when the input does not support the task. Add those four and a mediocre prompt becomes usable.

**Volume changes the artefact.** A one-off chat prompt and a template with variables run across two hundred invoices are different things: the second needs a fixed schema, a failure branch, a version number and a sample of test inputs. Intermediate learners should know which one they are building before they start typing.

**Each use case has its own done-check.** Summaries: can the reader decide? Extractions: does every field trace to a quote? Classifications: would a second reviewer agree? Drafts: would you send it after one edit? Writing the done-check is a two-minute habit that converts taste into a test.

**Use cases recombine into chains.** Extract the clauses, classify each against a policy, draft the exception memo, format the table. The chain is more reliable than a mega-prompt because each link can be checked.

**The use case sets the model tier.** Extraction and classification want consistency, low temperature and the fast tier. Open-ended drafting and brainstorming want the stronger model. Paying for deliberation on a field-extraction job is a common and expensive mistake.

### How it connects to the rest of the framework

`TSC1-Intermediate-A2` gives the five fundamental uses — summarise, infer, reason, transform, augment — and this bullet is their workplace catalogue. `TSC3-Intermediate-A3` is the technique choice inside each shape, `TSC3-Intermediate-A4` is the matching decision, and `TSC3-Intermediate-K6` explains why brainstorming and extraction need opposite settings. `TSC2-Basic-K3` holds the modes — text, image, video, code — that the same shapes recur in.

### What is current as of November 2026

Two use cases dominate measured workplace value: summarisation of documents that already exist, and structured extraction from them. That is where the hours were, and the GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon have all been tuned toward it — long inputs, reliable schemas, citations.

Three shifts worth teaching:

- **Extraction became an engineering task, not a prompting trick.** Native structured-output modes enforce a schema at generation time, which removes the old fight with Markdown fences. The remaining work is field design and the absent-value branch.
- **The "act" use case arrived.** With tool access, the prompt can end in an action — file it, send it, update the record. That extends the catalogue beyond text and raises the question of what the model may do, not just say.
- **Brainstorming got worse on reasoning models.** A deliberating model converges on the single best answer, which is excellent for analysis and poor for ideation. For divergence, use the fast chat tier and ask for volume explicitly.

### Common misconceptions

- *"One good prompt works for every task."* The shape is task-specific. A summarisation prompt applied to extraction produces prose where fields were needed.
- *"Summarise means shorten."* Shortening keeps the words; summarising chooses what the reader needs and drops the rest. Different instruction, different output.
- *"Classification just needs the labels."* Without a definition per label and a borderline rule, the model invents its own boundaries — consistently wrong, and impossible to appeal.
- *"Brainstorming is asking for ideas."* It is asking for difference, and difference has to be specified or you get synonyms.

## How a student should understand it

**Mental model:** the stack of different forms at a polyclinic reception. Registration, referral, X-ray request, medical certificate — same patient, different pad, because each desk needs different fields. Using the wrong pad is not a clerical slip; it produces an unusable record.

**Things they can do after this bullet:**
1. Name the use case before writing the prompt, and say what shape it needs.
2. Write the shape — reader, length or fields, and the failure line — for their three most common tasks.
3. Take a task solved with the wrong shape and re-shape it, then compare outputs.

**Misconceptions to kill:** that one prompt fits all tasks; that summarising is shortening; that a taxonomy is enough for classification.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic forms.** Different pads for different services, each with the fields that service actually needs. Where it breaks: a form cannot be filled wrongly in an interesting way; a prompt can produce a beautifully formatted answer to the wrong question.

**The referral letter and the discharge summary.** Same patient, same facts, different reader and different job — one asks another doctor to act, the other tells the patient what happened. Ask the room to write both in one prompt and watch the output split the difference and serve neither.

### Worked example with a real tool

Extraction, the highest-value shape, on a messy input:

```text
Extract from the invoice below into a table with exactly these columns:
Vendor | Invoice number | Date (YYYY-MM-DD) | Amount (SGD, numerals only) | PO reference

Rules:
- Quote values exactly as printed. Do not convert currency or reformat dates you cannot parse.
- If a field is not present, write MISSING. Never infer it from context.
- If the invoice is in a currency other than SGD, write the currency code in the Amount column
  instead of converting.

<invoice>
{{INVOICE_TEXT}}
</invoice>
```

Then the borderline classification version, and point at the difference: the extraction prompt spends its words on fields and on what to do when a field is absent; the classification prompt spends its words on definitions and a borderline rule. Neither spends words on "be accurate". Run the extraction on an invoice missing a PO number — the MISSING cell is the entire lesson.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a fluent, wrong summary that dropped the exception clause.
2. **State the objective** — by the end you can name a use case and write its shape, including the failure line.
3. **Recall prior learning** — what are the five fundamental uses of generative AI they already know?
4. **Present the content** — the ten shapes with their failures, then shape-as-four-missing-items.
5. **Guide** — build the invoice extraction prompt together, arguing about the absent-value rule.
6. **Elicit performance** — pairs pick their most common task and write the shape for it.
7. **Give feedback** — swap prompts, run each on one hard input, and mark whether the four items are present.
8. **Transfer** — each learner writes their done-check for their top use case and pins it next to the prompt.

## What the framework doesn't mention but trainers need to know

- **The catalogue is the trainer's own IP.** The framework says "use cases", not which ones. Choose the five that appear in the room's work and let the rest be homework.
- **Chains beat mega-prompts, and chains are what production looks like.** Show one two-step chain even at Intermediate level: extract, then draft.
- **The reviewer's standard is the real specification.** Ask "who checks this, and what will they look for?" — the answer usually rewrites the shape.
- **Some use cases should not be prompted at all.** Counting, totals and exhaustive lists belong to a spreadsheet, SQL or a tool call. Saying so early saves a term of frustration.
- **Volume changes governance, not just engineering.** A template run over customer documents needs a data-handling decision before it needs a better prompt.

## Watch out

- **Do not teach twenty use cases.** Five, done properly with failures, transfers; twenty becomes a slide nobody reads.
- **Do not demo extraction on a clean, well-formatted PDF.** Use a real invoice with a stamp across the total, or the class learns a false confidence.
- **Do not let brainstorming stand in for judgement.** Ideas are cheap; the converge step is the work.
- **The stale claim to retire:** "prompting is for writing." In 2026 the biggest uses are reading, extracting and classifying — the writing is the smallest part of the value.
