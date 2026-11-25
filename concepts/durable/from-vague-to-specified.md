# From vague to specified: making intent explicit

**Framework home** — New GenAI TSC #2 Prompt Design (Basic): A6 *identify best practices for designing effective prompts*; A7 *identify common prompt misuses (e.g. lack of context, vague instructions) and risks*; K2 *principles of how prompts shape AI-generated content*.

---

## What it actually is

Almost every "bad prompt" is a **specification failure**, not a language failure. The person knew what they wanted. They wrote something a colleague would have interpreted correctly, because the colleague shares their context, their history and their standards. The model shares none of it.

People under-specify for four reliable reasons:

1. **They are thinking aloud.** The first sentence of a request is usually the *trigger*, not the brief. "Can you look at this contract" is a gesture toward a task, not a task.
2. **They assume shared context.** The audience, the prior decision, the reason this matters — all held in the writer's head and never typed.
3. **They are polite instead of precise.** "If you don't mind, could you maybe summarise this a bit?" contains no information about length, audience or purpose.
4. **They do not know what "good" looks like.** If the writer cannot describe an acceptable output, the model cannot produce one — and will produce a plausible average instead.

The fix is not longer prompts. It is **four questions asked before writing**:

- **Who reads this?** (audience, seniority, prior knowledge)
- **What do they already know?** (what can be assumed, what must be spelled out)
- **What decision or action follows?** (the output exists to enable something)
- **What would make this unusable?** (the constraint that matters more than tone)

Answer those four in a sentence each, and a mediocre prompt becomes a specification. Skip them, and no amount of prompt-framework jargon will save it.

## Why it matters at work

Most office communication already suffers from under-specification — this is the same disease, with a faster feedback loop. A learner who cannot answer the four questions for an AI has usually been writing vague briefs to humans too, and getting away with it because the humans filled the gaps. The model will not.

## The student lens

**Mental model to install:** the model is a competent new colleague on day one — smart, fast, no context, and too polite to ask twice.

**Misconceptions you will hear:**
- *"It should know what I mean."* It knows what the words mean, not what your Tuesday looks like.
- *"If I add more detail, it gets confused."* Confusion usually comes from *conflicting* or *unranked* detail, not from detail itself. Rank it: "most important is X, secondary is Y".
- *"Specification is a template."* Templates are training wheels. The four questions survive after the template is gone.

**Five-minute practice:** take a real request they sent this week (email, chat, instructions to a junior). Rewrite it answering the four questions. Then decide which version they would rather receive as a new joiner — and notice that the specified version is usually shorter, not longer.

## The adult educator lens

**Analogy:** ordering at a *cai fan* stall. "Rice, two veg, one meat, less oil, no chilli" gets you lunch. "Something nice, not too heavy" gets you whatever the server decides — and you eat it, because you were hungry, not because it was right. Most people prompt like the second customer, then blame the stall.

**Three-minute demo:**
1. Type: "Write a summary of this report." Show the generic result, three paragraphs of nothing.
2. On the same screen, add the four answers: reader is a regional director who has 30 seconds, decision is whether to approve a budget line, must not exceed 120 words, must lead with the number.
3. Re-run. The room sees the difference is specification, not vocabulary.
4. Then remove only the audience line and re-run — the output drifts back. That single deletion is the most memorable slide of the day.

**Board sketch:** four boxes in a diamond — WHO READS / WHAT THEY KNOW / WHAT DECISION / WHAT RUINS IT — with an arrow into a single output box. Leave it up all day; when a learner's prompt fails, point at the empty box rather than editing their words for them.

**Where it goes wrong in class:** a learner says "my work is too complex for four questions". Agree — then run a genuinely complex example (a tender clarification, a performance improvement plan) through the four questions and let them see that complexity changes the *answers*, not the *questions*.

**Check for understanding:** give them a one-line prompt and ask which of the four questions is unanswered, and what the model will silently invent to fill the gap. Naming the invention is the proof they understand.

## Say this out loud

"You didn't write a bad prompt. You wrote a brief with holes — and the model filled them without asking."

## Content hook

**LinkedIn opener:** "Prompting is not a magic phrase skill. It's a specification skill, and most professionals were never taught it — they were promoted past it."

**Carousel idea:** "Before and after, one line at a time" — start with a vague request, add one specification per slide, show the output changing. Seven slides, no theory until the end.
