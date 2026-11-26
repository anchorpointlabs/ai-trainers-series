---
id: 03.03.A.A5
tsc: 3
level: Advanced
code: A5
title: Refine outputs and extend capabilities
---

# Refine outputs and extend capabilities

> **TSC #3 Prompt Engineering · Advanced · Ability A5**

> **Framework text (verbatim):** "Apply prompt engineering strategies to refine model outputs and extend capabilities of models."
>
> **TSC #3** Prompt Engineering · **Advanced** · Ability · Bullet 12 of 13

**One-line version:** Refining is making the same task come out better; extending is giving the model something it could not do at all — and confusing the two is why people rewrite good prompts instead of adding the missing capability.

## What it is

Two operations named in one sentence. **Refinement** is an iterative loop on an existing prompt: read the output against the goal, name the single property that is wrong, change the instruction that produces it, run again. **Extension** is adding ability the base model lacks — retrieval for knowledge it never had, a tool call for arithmetic or a live record, a second stage for a task too big for one pass, a schema for an output a system must parse. Refinement edits the instruction; extension edits the architecture around it.

## Deep expansion

### The concept

The distinction matters because the two have different ceilings and different costs. Refinement is cheap, fast, and bounded: three or four well-aimed passes will get a prompt most of the way, and the fifth pass usually makes it worse by adding rules that fight earlier ones. Extension is slower to build and unbounded in what it can reach: no amount of rewording will give a model your refund policy, but one retrieval step will.

The characteristic error is using the first to solve the second. A learner whose output invents a policy will rewrite the prompt five times — adding "do not hallucinate", "be accurate", "only use facts" — and the output will keep inventing, because the model has no facts to use. The instruction was never the problem. The missing capability was.

The second characteristic error is the reverse: a prompt that is merely vague gets extended with three stages and a re-ranker, and now there are four places to be vague.

### The sub-concepts

**The refinement loop has four steps, in order.** Read the output against the goal (not against your hopes). Name the property that is wrong — too long, wrong register, missing a field, hedging. Find the instruction responsible. Change that one. Skipping the naming step is why "refining" turns into random editing.

**Three passes, then stop.** Pass one: audience and purpose. Pass two: the constraint that the output keeps violating. Pass three: the format. If a fourth is needed, the task is under-specified somewhere else — usually the input.

**Revert what did not help.** A change that did not improve the output should be removed, not left in because it sounds sensible. Unhelpful rules cost attention and accumulate.

**Extension has four common forms.** Supply a source (retrieval or a pasted document); add a tool (a calculation, a lookup, a live record); add a stage (extract, then check, then format); enforce a schema. Each adds a capability, and each adds a failure point.

**Reliability multiplies downward.** Three stages at ninety percent each is seventy-three percent end-to-end. Extending buys capability at the cost of compounding failure, which is why every added stage needs its own check.

**Verify at the end, not in the middle.** A verification stage that reads the draft and checks it against the source catches errors the drafting stage cannot see. A verification instruction inside the drafting prompt mostly produces confident reassurance.

**Keep the prompt thin when you extend.** The point of adding retrieval or a tool is that the prompt no longer has to carry the knowledge or the arithmetic. Prompts that grow as capabilities are added are usually duplicating work the system already does.

### How it connects to the rest of the framework

Bullet 3 (`TSC3-Advanced-K3`) is the optimisation loop at prompt level; this bullet is the same loop on a single output plus the architectural step beyond it. Bullet 5 (`K5`) supplies the extension forms, Bullet 13 (`A6`) composes several extensions into a strategy, and Bullet 10 (`A3`) is how you know whether a pass helped. Bullet 8 (`A1`) is the precision work that most refinement passes amount to.

### What is current as of November 2026

- **Extension became configuration.** Attaching a document set, a search index or an internal API to a prompt is now a product feature rather than an integration project, so the balance shifted: more problems are worth extending and fewer are worth another refinement pass.
- **Structured output made stage handoffs cheap.** Where a schema is enforced, one stage's output can be another stage's input without parsing accidents — which is why multi-stage pipelines became ordinary practice with the late-2026 frontier models (GPT-6 generation, Claude 5.5, Gemini 3.1 Pro, Gemini 4 Argon).
- **Cheap parallel calls made selection a refinement technique.** Generating three drafts and choosing is often faster than three sequential refinement passes, and it produces a better audit trail.

### Common misconceptions

- *"Refining means trying again."* A re-roll is not a refinement. Name the defect, change the cause.
- *"Add more instructions until it behaves."* Rules accumulate and fight. Three tested constraints beat fifteen aspirational ones.
- *"A better prompt can add capability."* Wording cannot supply facts, arithmetic or live data. That is what extension is for.
- *"More stages means more reliable."* Stages multiply failure rates unless each is checked.
- *"Extension is a build project."* Usually it is attaching a source or a tool and writing the grounding clause.

## How a student should understand it

**Mental model:** the curry pot. You taste, add salt, taste again — one adjustment at a time. If the pot has no chicken in it, no amount of salt fixes that; you have to go and buy chicken.

**Things they can do after this bullet:**
1. Run a three-pass refinement, naming what each pass changed and reverting what did not help.
2. Decide whether a failure needs refinement or extension, and say why.
3. Add one extension — a source, a tool, a stage or a schema — with a check on the result.

**Misconceptions to kill:** that refinement is re-rolling; that wording adds capability; that added stages are free.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The curry pot.** Taste, adjust one thing, taste again. Add salt, sugar and coconut milk at once and you cannot tell which fixed it — or which ruined it. Where it breaks: a pot of curry is forgiving and cheap to remake; a production prompt is neither, which is why the change is logged.

**The delivery rider with a phone and a map.** The rider was already good at riding. The phone does not make them a better rider; it lets them find addresses they could not have known. That is extension: capability, not skill. Where it breaks: a rider knows when the map is wrong; a model will follow a bad tool output confidently, so the check has to be built.

### Worked example with a real tool

```text
Pass 1: 'Write a complaint reply.'
Pass 2: add audience and tone. 'Reply to a customer complaint, apologetic
but firm, 3 sentences.'
Pass 3: add a constraint. '...and do not promise a refund.'
```

Run each pass and read the output aloud. Pass 1 is a template letter; pass 2 is shorter and has a stance; pass 3 removes the sentence that always causes trouble. Then extend it: paste the actual policy paragraph and add "use only this policy; if it does not cover the case, say a colleague will follow up within two working days". Run the same complaint again — now the reply cites a real remedy instead of a generic apology.

Point at the difference in kind: three passes changed *how* it wrote; the extension changed *what it could know*. Then break it deliberately — remove the policy and keep the instruction "use only this policy" — and watch the model invent one. That is the sentence to leave on the board.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a generic complaint reply and ask how many edits it would take to be sendable.
2. **State the objective** — run three named refinement passes, then add one extension and check it.
3. **Recall prior learning** — editing a colleague's draft: you name one problem at a time, or the draft gets worse.
4. **Present the content** — the four-step loop; three passes; the four extension forms; compounding reliability.
5. **Guide** — run the three passes live, then the policy extension, then the deliberate break.
6. **Elicit performance** — learners refine one weak prompt in three passes and add one extension, logging each change.
7. **Give feedback** — compare logs. Groups that changed several things per pass cannot attribute the result.
8. **Transfer** — each learner identifies one task where refinement has failed twice and names the extension it needs.

## What the framework doesn't mention but trainers need to know

- **The log is the deliverable.** A refinement without a record is a prompt nobody can defend, and the next person will undo the fix.
- **Some outputs cannot be refined into correctness.** If the source is wrong or missing, refinement polishes the error. Check the input before the instruction.
- **Extension changes the failure modes, not just the capability.** Adding retrieval introduces retrieval misses; adding a tool introduces wrong-argument calls. Plan for the new failure, not just the new feature.
- **Verification is an extension in its own right** and usually the highest-value one: a second pass that checks claims against the source catches more than any wording change.
- **Latency is a user-facing cost.** A three-stage pipeline that takes forty seconds will be abandoned by staff even if it is more accurate.

## Watch out

- **Do not call a rewrite a refinement.** Rewriting everything means nothing was learned.
- **Do not extend to compensate for a vague brief.** Fix the audience and the format first; then decide whether capability is missing.
- **Do not add stages without checks.** You are building a chain of assumptions.
- **Do not let the demo stop at "it works".** Show the new failure mode the extension introduced.
- **The stale claim to retire:** "a better prompt can do anything." Capability comes from sources, tools and structure; wording only steers it.
