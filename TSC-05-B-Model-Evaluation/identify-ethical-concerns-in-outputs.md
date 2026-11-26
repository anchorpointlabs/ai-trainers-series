---
id: 05.01.B.A5
tsc: 5
level: Basic
code: A5
title: Identify ethical concerns in generated outputs
as_at: 2026-11-26
review_by: 2027-02-25
---

# Identify ethical concerns in generated outputs

> **TSC #5 Generative AI Model Evaluation · Basic · Ability A5**


> **Framework text (verbatim):** "Identify ethical concerns in generated outputs."
>
> **TSC #5** Generative AI Model Evaluation · **Basic** · Ability · Bullet 11 of 11

**One-line version:** The ethics check is a scan you run on the output itself — looking for privacy leaks, bias, deception and harm — because an output can be accurate and still be wrong to send.

## What it is

This is the ability to read a generated output and flag the ethical problems in it: personal data that should not be there, bias or stereotyping, content that could deceive or be mistaken for human, and material that could cause harm. It is the applied, per-output version of knowing that ethics matters — a checklist run on real text, with a specific finding as the result.

## Deep expansion

### The concept

Ethical concerns live *inside* the output, not in the abstract. A paragraph can be factually perfect and still leak a customer's NRIC, stereotype a group, or read like a genuine human wrote it when it did not. The ability is a deliberate scan of each output for a fixed set of concerns — the same way a proofreader scans for spelling, an ethical evaluator scans for harm. The discipline is treating this scan as part of "done", not as an optional extra that happens when someone remembers.

### The sub-concepts

**Privacy.** Did the output include personal data it should not — a name, NRIC, phone number, medical detail — either reproduced from the prompt or invented? In Singapore this is a PDPA concern as much as an ethical one, so a privacy leak is a *finding*, full stop.

**Bias and stereotyping.** Does the output assume or reinforce a group trait — a gender, race, age, religion — where it should not? This is the output-level version of the bias detection in `TSC5-Basic-A4`, run with an ethics lens.

**Deception.** Could the output be mistaken for something it is not — a human-written testimonial, a real photo, a genuine endorsement? Undisclosed synthetic content is a deception risk even when the content itself is benign.

**Harm.** Does the output enable harm if taken seriously — unsafe advice, defamation, incitement, or content a vulnerable reader could act on to their detriment? The test is not "is it wrong" but "what happens if someone believes it."

### How it connects to the rest of the framework

This is the ability that operationalises `TSC5-Basic-K6` (ethical considerations) — K6 is *knowing* the concerns, A5 is *finding* them in a live output. It sits beside `TSC5-Basic-A4` (identify limitations and biases), sharing the same scanning habit with a narrower, ethics-only target. It is the seed of `TSC8` (Responsible AI), where this single-bullet ability becomes a full skill with frameworks and governance.

### What is current as of November 2026

The headline shift is **deception has become the dominant concern.** Late-2026 models generate voice, image and text that are effectively indistinguishable from human work, so "is this real" is now the most common ethics question a Singapore office asks — synthetic endorsements, deepfake clips, AI-written reviews. Privacy is the second: as models get better at memorising and reproducing, the risk of a personal detail surfacing in an output grows, and PDPA turns "it leaked" from an embarrassment into a compliance incident. The scan has moved from a nice-to-have to a pre-send step.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"If it's accurate, it's ethical."* An accurate output can leak data, stereotype a group, or deceive its reader. Accuracy and ethics are different scans.
- *"The model will catch its own ethics problems."* The model produces the output; it does not reliably flag its own harms. The scan is the human's job.
- *"Ethics only matters for sensitive industries."* A deceptive product review in retail, a biased hiring note in HR, a leaked phone number in support — every industry has a version of the same four concerns.

## How a student should understand it

**Mental model:** the pre-flight checklist. A pilot does not ask "does anything look wrong?" — she runs the checklist, every time, in order. The ethics scan is the pre-send checklist for any AI output that leaves your hands: privacy, bias, deception, harm.

**Three things they can do after this bullet:**
1. Run the four-part scan on one output and flag any concern with a specific quote and why it fails.
2. Name the one concern most likely to bite in *their* industry, with a concrete example.
3. Decide — and say — whether a given output should be held back, edited, or sent.

**Misconceptions to kill:** accurate = ethical, "the model catches its own", and ethics = sensitive industries only.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The pre-flight checklist.** Pilots run the same list before every flight, not because they expect a problem but because a missed item is catastrophic. The ethics scan is the same: four items, every output, in order — privacy, bias, deception, harm. It is not suspicion; it is routine.

**The "would you sign it" test.** Before you send an output, ask: would you put your own name on it, and could it come back to you in a complaint? If the answer is "no" for any of the four concerns, it does not go. This folds the whole scan into one question the room already knows how to ask.

### Worked example with a real tool

Generate an output that is *plausible but ethically wrong*, then scan it live:

```
Write a short customer testimonial for our new financial advisory
service, in the voice of a satisfied retiree.
```

What to point at afterwards: the output is likely well-written and positive — and it is a fabricated testimonial, which is *deception* (a fake customer voice) and possibly *harm* (misleading prospective clients about a financial product). Run the four scans: privacy (does it invent a fake name or details — yes), bias (maybe), deception (yes, clearly), harm (yes, if it misleads buyers). The lesson: nothing in the prompt said "do something unethical", and the model happily did it anyway — which is exactly why the scan has to be on the human side.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show the fabricated testimonial and ask how many would have posted it without a second thought.
2. **State the objective** — you will scan any output for the four ethical concerns before it is sent.
3. **Recall prior learning** — they know the ethical considerations (K6) and bias detection (A4); this is the output-level scan.
4. **Present the content** — privacy, bias, deception, harm; one concrete example of each.
5. **Guide** — run the four scans on the testimonial together.
6. **Elicit performance** — each learner takes one output from their own work and runs the scan, flagging anything.
7. **Give feedback** — confirm real findings and correct the false flags (not every AI-written line is deception).
8. **Transfer** — they add the four-item scan to their own "before I send" routine.

## What the framework doesn't mention but trainers need to know

- **Deception is the modern headline, and it is not just deepfakes.** A fabricated testimonial, an AI-written review, a "personal" email that was auto-generated — these are the everyday deception risks in a normal office, and they need no technical skill to spot once you are looking.
- **The scan is only useful if it changes a decision.** Flagging a concern and sending the output anyway is not evaluation, it is paperwork. Teach the "hold, edit, or send" decision as the final step.
- **Singapore anchors the privacy item.** PDPA makes a data leak a compliance matter with consequences, so the privacy scan is not abstract virtue — it is legal hygiene. Learners should feel the weight of that one item specifically.

## Watch out

- **Do not turn the scan into paralysis.** Four checks, then a decision. A learner who flags everything and sends nothing has traded one failure for another — the point is to *catch real harms*, not to treat every output as radioactive.
- **Do not accept "the model said it, so it's fine" as a defence.** The human who sends the output owns its ethics. This is the accountability lesson, and it has to be stated plainly or learners will treat the model as the responsible party.
- **The stale claim to retire:** "we don't need an ethics check, our outputs are always benign." Every output is benign until it is not — a fabricated testimonial, a leaked NRIC, a biased hiring note are all produced by the same "benign" model in a normal afternoon.
