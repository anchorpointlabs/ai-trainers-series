---
id: 05.03.A.A2
tsc: 5
level: Advanced
code: A2
title: "One framework, many inputs: integrating text, image, audio and structured evidence"
as_at: 2026-11-26
review_by: 2027-02-25
---

# One framework, many inputs: integrating text, image, audio and structured evidence

> **TSC #5 Generative AI Model Evaluation · Advanced · Ability A2**


> **Framework text (verbatim):** "Integrate diverse data sources and modalities into evaluation frameworks."
>
> **TSC #5** Generative AI Model Evaluation · **Advanced** · Ability · Bullet 8 of 13

**One-line version:** A multimodal system fails at the joins, so the evaluation must be built where the modalities meet, not once per modality and added up.

## What it is

This ability is the engineering of one framework that holds items from different sources — documents, transcripts, images, transaction tables, tool logs — scores them with methods appropriate to each, and reports them together without pretending the numbers are commensurable. The output is one schema, one provenance trail, one report, and a defensible rule for how a score in one modality relates to another.

## Deep expansion

### The concept

Most multimodal evaluations are several evaluations stapled together: an image score, a transcript score, a table accuracy figure, and a summary slide that adds them. The stapling is where the errors live.

**Incommensurable scales.** A similarity score, a word error rate, a rubric score out of five and a currency error in cents cannot be averaged. Keep raw measures separate and define the decision rule at the level of *outcomes*.

**Different sampling logics.** Text items are cheap and plentiful; recordings are expensive and biased toward whoever agreed to be recorded; images may be synthetic. Combining them means stating what population each sample represents, and not letting the cheap modality win by count.

**Alignment and provenance.** An image, its caption, the transcript of the call and the CRM record describe one case. Without a case identifier, an item-level join and a record of which asset version was used, the evaluation cannot be reproduced or audited.

**Missing modalities.** In production one input is often absent — no photo, no transcript, a corrupt file. How the system behaves then is a first-class evaluation question, invisible if the test set contains only complete cases.

### The sub-concepts

**The evaluation record.** One row per item: case id, modality set, input references, system version, output, per-modality scores, judge identity and version, human scores where available, free-text diagnosis. Everything else is a view of this table.

**Modality-specific metrics, kept separate.** Character error rate for transcripts, embedding or perceptual distance for images, exact or numeric match for structured fields, rubric scores for open text — each with its own denominator.

**Normalisation only where legitimate.** Percentile ranks or pass/fail thresholds make scores comparable for triage; they do not make them additive. Say which you are doing.

**Stratified sampling across modalities.** Deliberately over-sample rare combinations — photo plus complaint, call plus follow-up email — because cross-modal failure lives there.

**Cross-modal consistency checks.** Does the description match the image? Does the summary contradict the transcript? Does the extracted figure match the invoice? Cheap, high-yield, and impossible in a single-modality evaluation.

**Privacy tiers per modality.** Audio and images carry more identifiability than text. Build the report from the lowest tier that supports the claim.

### How it connects to the rest of the framework

`05.03.A.A1` is the human and live-test layer on top of this framework; `05.03.A.K4` supplies the judges. `05.02.I.A2` is the analytical skill the schema serves and `05.02.I.K3` (visualisation) is how the integrated result is read. `05.03.A.K5` sets privacy constraints per modality, and `TSC7-I` supplies the multimodal model knowledge that tells you which failures to expect.

### What is current as of November 2026

Natively multimodal models collapsed the pipeline — one call takes a PDF, a photo and a recording — which removed plumbing and created an attribution problem: you can no longer blame the transcription step, because there is not one you control. The compensating practice is to evaluate on the *join*: given this photo and this complaint, is the answer right, and can you tell which input it ignored. Long context has made whole-document and whole-call evaluation practical, which raises the bar — a system that reads the whole file has no excuse for missing page nine.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"We evaluate each modality separately and combine."* Combining is the part that fails. The interesting failures are cross-modal.
- *"A multimodal model means a modality-agnostic evaluation."* The model is; your sampling, raters and privacy tiers are not.
- *"More items is better."* A thousand scraped captions will outvote eighty carefully collected recordings and tell you about the captions.

## How a student should understand it

**Mental model:** a polyclinic consultation record — vitals, a photo of the rash, a voice note, the doctor's note. The diagnosis is only as good as the join, and the join is the patient in the chair.

**Three things they can do after this bullet:**
1. Design an evaluation record that holds every modality with provenance and version.
2. Write cross-modal consistency checks for a real product.
3. Say which modality is doing most of the work in a given report, and whether that is appropriate.

**Misconceptions to kill:** that combining scores is addition, that separate evaluations compose, and that a multimodal model needs only multimodal test items.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The wet market fish stall.** The fish is judged by look, smell, touch and the seller's word. Any one can be faked; the buyer integrates them and notices when they disagree — bright eyes but a smell. It breaks because a buyer weights by experience and an evaluation has to write its weights down.

**The HDB renovation quote.** You have a drawing, a photo of the existing kitchen and a written quotation. The question is not "is the drawing nice" but "does the quotation match the drawing and the photo". Most disputes come from a mismatch nobody checked.

### Worked example with a real tool

An assistant answers product questions from a photo, a spec sheet and the customer's message. Build the cross-modal check. Paste this into Claude with one real case:

```
Here is one case: a customer message, a product photo, and the spec sheet text. The
assistant's answer follows.

Build a consistency audit: (1) extract every factual claim in the answer; (2) tag each
claim's source as PHOTO, SPEC, MESSAGE or NONE; (3) flag every NONE as unsupported;
(4) flag any claim where PHOTO and SPEC disagree and say which the answer followed;
(5) flag anything in the MESSAGE the answer ignored that should have changed it.

Output a table: claim, tag, supporting span (quoted), verdict. Then one sentence:
which single input, if removed, would most change the answer.
```

What to point at afterwards: the NONE column. Most rooms surface two or three confident claims with no source — exactly the failure a per-modality evaluation scored as fine, because the image was described accurately and the spec quoted correctly. Then the last sentence tells you which input to sample hardest.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show an answer that is right about the photo and the spec, and wrong about the customer's question.
2. **State the objective** — each team has a schema and three cross-modal checks for their own system.
3. **Recall prior learning** — rubrics are per-task, and here the task spans three inputs.
4. **Present the content** — the record, incommensurable scales, sampling logic, missing-modality testing, privacy tiers.
5. **Guide** — run the consistency audit together and mark the NONE claims.
6. **Elicit performance** — teams design their record schema and one cross-modal check.
7. **Give feedback** — review schemas for missing provenance fields; that kills reproducibility.
8. **Transfer** — each learner lists the modalities their current evaluation ignores entirely.

## What the framework doesn't mention but trainers need to know

- **Binary assets are the hard part of versioning.** Hash them and store a manifest; a re-encoded JPEG is a different item.
- **Consent differs by modality.** People consent to text far more readily than to a recording of their voice. The audio subset needs its own conversation.
- **Synthetic items are useful for coverage and dangerous for conclusions.** Label them, and never let a synthetic majority outvote real items on a claim about real users.
- **Cost scales with modality.** Transcription and image judging cost materially more per item; the sampling design has to respect the budget.

## Watch out

- **Do not average across modalities.** It produces a number nobody can defend under questioning.
- **Do not let the cheap modality set the sample.** Stratify deliberately and report denominators.
- **Do not test only complete cases.** Production is full of half-populated records, and the failures cluster there.
- **Do not build the framework without the join key.** If you cannot link a photo to a ticket, you cannot evaluate the answer about the ticket.
- **The stale claim to retire:** "we will add images to the eval later." A new modality means a new schema, sampling and privacy tier — a new evaluation, not an extension.
