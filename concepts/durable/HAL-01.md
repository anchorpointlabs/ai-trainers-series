# HAL-01 · Hallucination: why models invent things, and what actually reduces it

**Framework home** — New GenAI TSC #1 Generative AI Principles and Applications (Basic): *limitations of AI models in generating relevant outputs*, at the level where a learner must be able to explain a wrong answer without mystifying it. TSC #2 Prompt Design (Basic), K1 *techniques in troubleshooting AI tools* and K4 *guardrails to prevent prompts from creating unexpected outputs*. TSC #9, where verification of model output becomes a control rather than a habit.

---

## What it actually is

At each step the model does one thing: produce a plausible continuation of what it has read so far. When the pattern strongly implies a fact and the model holds that fact, plausibility and truth line up. When the fact is missing, ambiguous, or rare, the nearest plausible continuation is a fabricated one — a clause number, a rate, a name, a citation — produced by exactly the same machinery that produces correct answers. There is no separate check and no internal flag that distinguishes "I know this" from "I am filling the shape".

That is why fluency and factuality are independent. Grammar, register and confident structure are cheap and always available; being right depends on the specific fact being present. Confidence is a property of the prose, not evidence about the claim. "It said it confidently" tells you the sentence was well-formed.

The failure modes worth naming in a classroom: invented citations and case references; numbers that are the right shape and the wrong value; a quote attributed to the wrong person; an answer about a document it was never given; and facts that were true when the training data was collected, delivered in the present tense.

The mitigations form a ladder, most reliable first. **Ground it** — supply the text and require the answer to come only from the text. **Require quotes or references, then check them** — an unverified citation is decoration, and fabricated references are the most common hallucination in professional work. **Constrain the task** — narrow question, fixed output shape, and an explicit escape: "if it is not stated, write NOT STATED". **Lower randomness**, and use tools with retrieval for current facts. **Verify independently** — the source of truth, a second tool, a colleague. On anything entering a tender, a payslip, a report book or a board paper, the human signature is the last control and the only one that carries accountability.

The honest limit: you cannot prompt your way to guaranteed truth. "Do not hallucinate" is a wish. "Quote the sentence or write NOT STATED" is a control — and it still needs a human to read the quote.

## Why it matters at work

A fabricated clause in a tender response or a wrong CPF figure in an HR memo is not an inconvenience; it is a liability with a name at the bottom. The real cost is not the single wrong answer but what happens next — either the team stops trusting the tool entirely, or it stops checking.

## The student lens

**Mental model to install:** a well-read colleague who would rather give you a confident answer than admit a gap, and who is never embarrassed afterwards.

**Misconceptions you will hear:**
- *"It only makes things up on obscure topics."* It is worst where a specific detail is expected and missing — a clause number, a date, a name.
- *"Newer models don't do this."* The rate falls; the mechanism stays. A better model makes the remaining errors harder to spot.
- *"I told it to be accurate."* Accuracy is not a setting. It is a property of what you supplied and what you checked.

**Five-minute practice:** give it a document they know well and ask a question the document does not answer. Then ask one it does answer, with "quote the sentence you used." Check both. The first one is the lesson.

## The adult educator lens

**Analogy:** the colleague who never says "I don't know". In the meeting they give you the figure, the date and the regulation number, smoothly, in a tone that closes the discussion. You find out at the client meeting. Where it breaks: that colleague can be trained and will eventually feel the embarrassment. The model's confidence does not update, because it was never a signal.

**Three-minute demo:**
1. Ask for a current statutory figure — a CPF rate, a levy band — and let it answer in full, confident, structured prose.
2. Ask where that came from, and open the link. Plausible title, wrong page.
3. Paste the actual source text and rerun with "quote the sentence you used; if the text does not state it, write NOT STATED."
4. Compare the two answers side by side. Same model, minutes apart.

**Board sketch:** two overlapping circles labelled "sounds right" and "is right". Mark the overlap and write "manufacture this, don't assume it". Below, the ladder as five rungs, top rung "ground in supplied text", bottom rung "human sign-off".

**Where it goes wrong in class:** someone asks how to know when to trust it. Answer: you do not trust the model, you trust the check — and the check scales with the cost of being wrong. A brainstorm list needs a glance; a figure in a submission needs a source and a reader.

**Check for understanding:** "Name a sentence in your work that must never be wrong, and the exact check you would run before it leaves your desk." If the answer is "ask the AI to double-check", they have not got it — that is the same generator marking its own homework.

## Say this out loud

"It doesn't know when it's guessing. So the checking is the skill, not the prompting."

## Content hook

**LinkedIn opener:** "It gave me a clause number, a date and a source. Two of the three were invented, and all three arrived in the same confident tone."

**Carousel idea:** "Five rungs on the trust ladder" — one mitigation per slide with the failure it prevents, ending on a screenshot of a fabricated citation and the real page.
