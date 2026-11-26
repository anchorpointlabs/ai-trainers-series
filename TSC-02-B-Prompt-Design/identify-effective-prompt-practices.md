---
id: 02.01.B.A6
tsc: 2
level: Basic
code: A6
title: Identify effective prompt practices
---

# Identify effective prompt practices

> **TSC #2 Prompt Design · Basic · Ability A6**

> **Framework text (verbatim):** "Identify best practices for designing effective prompts."
>
> **TSC #2** Prompt Design · **Basic** · Ability · Bullet 11 of 15

**One-line version:** Effective practice is unglamorous — say what you want, give it the facts, set the limit, then read the answer against both.

## What it is

Best practice here means a short list of habits that reliably improve results across tasks: state the task and the reader, supply the facts the task depends on, specify the limits that matter, use plain language, and treat the first answer as a draft to be checked and revised. There is no single fixed template. The habits are the template.

## Deep expansion

### The concept

The reason this bullet exists — and the reason it is an *ability* rather than a knowledge item — is that knowing the habits and applying them are different things. Ask a room "should you specify the audience?" and everyone says yes. Watch the same room write prompts and half of them omit it. So effective practice has to be built as a loop, not memorised as a list.

The loop has three moves:

**Specify.** Task, facts, reader, limits — the elements from `TSC2-Basic-A5`, used sparingly. A prompt that leaves a decision open invites the model to make it, and the model's default is the average of the internet.

**Check.** Compare the answer with the facts you supplied and the requirements you set. Not "does it read well" — does it contain the date I gave it, the sentence count I asked for, the facts and nothing but the facts.

**Revise.** Change the prompt, not the output. If you find yourself editing the reply by hand, that edit is a specification you failed to write; move it into the prompt and run again.

That third move is where most of the value sits, and it is the one learners skip, because editing the output feels faster than improving the brief.

### The sub-concepts

**Specific beats long.** "Write a 120-word notice for parents, mentioning the closure and the collection point, no other facts" outperforms four paragraphs of encouragement. Signal density is what the model responds to; warmth and repetition are cost.

**Facts in, facts out.** Anything the answer must contain should be in the prompt, not in your head. This is not a limitation to be worked around; it is the job.

**One limit that matters beats five that decorate.** Choose the constraint whose absence caused the last failure — length, format, tone, or a ban on invention — and enforce that one properly.

**Plain language, not performance.** Instructions written in clear imperative English work better than ornate requests, and they are easier to hand to a colleague. "Is this understandable to someone with little context?" is a better test than "is this impressive?"

**Check against requirements, not against impression.** Write the acceptance criteria before you generate: what must be present, what must not, what shape. Then the check takes ten seconds and does not depend on mood.

**Vary one thing when revising.** Two changes at once and you cannot tell which helped. This is the same control as `TSC2-Basic-K1`, applied to design rather than to faults.

### How it connects to the rest of the framework

`TSC2-Basic-A5` supplies the elements this ability uses; `TSC2-Basic-K2` explains why the habits work; `TSC2-Basic-A8` is the comparison method that tells you whether a revision helped; `TSC2-Basic-A7` catalogues the misuses these habits prevent. Practitioners who take this further meet the same loop, at scale and with test sets, at `TSC3-Basic-A4`.

### What is current as of November 2026

Two shifts make the habits more valuable, not less. First, the late-2026 models — OpenAI's GPT-6 generation, Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — are good enough that a vague prompt produces a *plausible* answer almost every time, so the failure is quieter than it used to be and the check matters more. Second, saved instructions and project memory mean habits now persist: a learner who writes a sloppy standing brief has institutionalised it. The practical advice for trainers is to spend the time on the specify-and-check loop rather than on phrasing tricks, because the phrasing gap between models has narrowed while the specification gap between people has not.

### Common misconceptions

- *"Best practice means a long prompt with every element."* It means the elements that this task needs, stated clearly.
- *"Politeness improves results."* It does not reliably; explicit criteria do. Pleasantries cost tokens and change nothing you can measure.
- *"If the output is good, the prompt was good."* One good sample may be luck; check a second input before you believe it.
- *"Revising means adding more instructions."* Revising usually means deleting the ones that contradict each other.

## How a student should understand it

**Mental model:** a recipe you are still testing. You do not defend the first version; you cook it, taste it, change one thing, and cook again.

**Things they can do after this bullet:**
1. Spot the missing audience or missing facts in a vague prompt.
2. Write acceptance criteria before generating.
3. Turn their own manual edits back into prompt instructions.

**Misconceptions to kill:** length as quality; politeness as technique; one good output as evidence.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tuition assignment brief.** A parent who says "help my son with maths" gets a general tutor. A parent who says "Sec 2 Express, weak in algebra, one hour a week, please send notes after each session" gets a plan. The difference is not the tone of the request; it is the specification. Where it breaks: a tutor will negotiate the brief; a model will accept it and quietly fill the gaps.

### Worked example with a real tool

```text
The original prompt is: Write a notice.

For this invented task, Pine Street Community Library is holding a book swap on 12 March 2027, from 2 pm to 4 pm, in the library hall. Visitors should bring one book to swap.

1. Rewrite the original prompt in plain language so a chat AI can write a notice for library visitors. Include the relevant facts above, ask for exactly two sentences and instruct it not to add event details that were not supplied. Label this "Revised prompt".
2. Following your revised prompt, write the notice. Label it "Notice".
```

What to point at afterwards: the model produces a revised prompt you can mark against the practice list — does it name the audience, the facts, the length, and the ban on invention? That makes the ability visible and assessable in one screen. Then run the learner's own version and compare. Finally, take any manual edit someone made to the notice and ask where it belongs in the prompt: nine times out of ten it is a missing constraint, and moving it is the habit you are teaching.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "If a colleague just says 'write a notice', what would you need to ask before writing it?" Collect a few, sort them into the element list.
2. **State the objective** — by the end you can revise a vague prompt and check the answer against stated criteria.
3. **Recall prior learning** — elements from `TSC2-Basic-A5`, one-variable testing from `TSC2-Basic-K1`.
4. **Present the content** — the specify/check/revise loop, and the rule that manual edits become prompt edits.
5. **Guide** — revise "Write a notice" as a class, arguing about what to leave out.
6. **Elicit performance** — pairs write their own revised prompt, generate, and mark the output against their criteria.
7. **Give feedback** — swap and mark each other's criteria; identify any criterion the output could not fail.
8. **Transfer** — each learner names the manual edit they make most often and the instruction that would remove it.

## What the framework doesn't mention but trainers need to know

- **Criteria must be falsifiable.** "Professional tone" cannot fail; "two sentences, no invented dates" can. Teach the difference.
- **Habits decay under deadline.** The room will write good prompts in class and vague ones on Friday. Give them a one-page card, not a lecture.
- **Effective practice is boring on purpose.** Learners hoping for cleverness will be disappointed; say so and sell the reliability instead.
- **Checking is a job, not an attitude.** If the workflow has no moment for checking, no amount of good practice survives contact with a busy week.

## Watch out

- **Do not teach practice as a phrasebook.** "Let's think step by step" is not a best practice for a notice; it is a technique for arithmetic.
- **Do not demo only successes.** Show a prompt that failed the check and the revision that fixed it; that is the loop.
- **Do not let the room leave without criteria.** A prompt without acceptance criteria is a hope with punctuation.
- **The stale claim to retire:** "the longer and more detailed the prompt, the better." In November 2026 the models reward structure and specificity, and they are diluted by padding like everything else.
