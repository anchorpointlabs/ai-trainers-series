---
id: 07.03.A.A6
tsc: 7
level: Advanced
code: A6
title: Neuro-symbolic systems: pairing a model with a solver that cannot guess
as_at: 2026-11-26
review_by: 2027-02-25
---

# Neuro-symbolic systems: pairing a model with a solver that cannot guess

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A6**


> **Framework text (verbatim):** "Design neuro-symbolic AI systems (e.g. incorporation of SAT/SMT solvers)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 17 of 20

**One-line version:** A generative model is excellent at turning messy language into structure and hopeless at guaranteeing anything — so hand the guarantee to a solver and let the model do the translation.

## What it is

A neuro-symbolic system combines a learned component with a symbolic one: a language model reads a policy document and emits constraints; a SAT, SMT or constraint-programming solver finds a solution that satisfies them, or proves that none exists. The neural half handles ambiguity and language; the symbolic half handles correctness and explanation.

## Deep expansion

### The concept

The division of labour is the design. There are only three sensible arrangements:

1. **Model proposes, solver checks.** The model generates a candidate — a schedule, a configuration, a set of rule applications — and the solver verifies it against formal constraints. Rejection is cheap and unambiguous.
2. **Model translates, solver solves.** The model converts natural-language requirements into a formal specification; the solver does the search. This is where the leverage is, and where the risk is: a wrong translation produces a confidently wrong answer with a proof attached.
3. **Solver searches, model explains.** The solver produces a solution or an infeasibility proof; the model renders it in language a human can act on. Explaining *why* a roster is impossible is often worth more than the roster.

The reason to bother is that a solver gives something a model cannot: a certificate. When a constraint set is unsatisfiable, an SMT solver returns an unsatisfiable core — the minimal set of constraints that conflict — which tells an operations manager that the problem is the policy, not the software.

### The sub-concepts

**What each solver class is for.** SAT handles pure boolean feasibility; SMT adds arithmetic and theories (integers, arrays, bit-vectors); constraint programming (CP-SAT and friends) handles scheduling and assignment with optimisation objectives; linear and mixed-integer programming handles continuous resource allocation. Choosing wrongly turns a five-second problem into a five-hour one.

**Specification is the bottleneck.** Translating "nurses should not work more than two consecutive nights except in emergencies" into constraints requires deciding what an emergency is, whether the rule is hard or soft, and who arbitrates. Most project time goes here, and it is not a modelling problem.

**Soft constraints and objectives.** Real rosters are not satisfiable under all hard rules, so the useful design expresses preferences as weighted objectives and reports the trade-off rather than failing.

**Grammar-constrained generation.** A cheaper cousin: restrict the model's output to a formal grammar or JSON schema so the result is parseable by construction. It removes syntax errors, not semantic ones.

**Auditability.** The symbolic layer provides a trail — which rule, which constraint, which input — that satisfies a regulator in a way a model's reasoning trace never will.

### How it connects to the rest of the framework

`TSC7-Advanced-K1` explains why a model cannot guarantee anything; this bullet is the architecture that compensates. `TSC7-Advanced-A1` supplies the generate-and-verify pattern this specialises. `TSC9-Intermediate-K2` covers the security and correctness properties being protected, and `TSC8-Intermediate-K3` covers the accountability obligations an audit trail satisfies.

### What is current as of November 2026

Two developments made this practical. First, current frontier models are reliable enough at structured extraction and at emitting syntactically valid solver code that the translation step is no longer the fragile part; the fragile part is now the requirement itself. Second, solver tooling has become easy to embed (Python bindings, cloud solvers), so neuro-symbolic designs appear in rostering, compliance checking and configuration management rather than only in research labs.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"The model can do constraint satisfaction if prompted carefully."* It can produce something plausible; it cannot certify feasibility, and it silently violates constraints under load.
- *"Neuro-symbolic means old-fashioned rules with an LLM bolted on."* The interesting designs put the model where language lives and the solver where guarantees live.
- *"A solver either finds a solution or the problem is impossible."* Without a time limit, "no answer yet" is not "no answer".
- *"Formal specification removes ambiguity."* It relocates it — to whoever writes the constraints.

## How a student should understand it

**Mental model:** an interpreter and a judge. The interpreter turns what was said into a precise claim; the judge rules on it. Neither is useful alone.

**Three things they can do after this bullet:**
1. Decide which half of a problem belongs to the model and which to the solver.
2. Write constraints as hard or soft with explicit weights.
3. Read an unsatisfiable core and explain it to a business owner.

**Misconceptions to kill:** that prompting can replace solving, that solvers remove ambiguity, and that symbolic systems are legacy technology.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The customs declaration.** An officer reads what you wrote (language), the system checks it against the tariff and the rules (symbolic). The officer's judgement is not accepted as proof of duty paid.

**The HDB eligibility check.** "Your household qualifies" is a rule application, not an opinion — and if it says no, it can tell you which criterion failed. A model that says "probably eligible" is worse than useless here.

### Worked example with a real tool

Have learners write the extraction prompt and the constraints:

```
Here is our clinic's rostering policy [paste 1 page].

1. Extract every rule as a constraint. Mark each HARD or SOFT,
   and for SOFT ones propose a weight and say who owns it.
2. Write the CP-SAT model skeleton in Python (OR-Tools): variables,
   hard constraints, objective. Do not solve yet.
3. The model must handle "except in emergencies" - how do you
   represent that without making every rule soft?
4. If the solver proves infeasible, what do you show the clinic
   manager?
```

What to point at afterwards: question 3 exposes the real design work — an exception is either a variable with a penalty or a human decision, and the prompt has to make that choice explicit. Question 4 is where the value becomes obvious: an unsatisfiable core names the two rules that conflict, and the manager changes policy instead of blaming the software.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a model-generated roster with one nurse on two shifts at once.
2. **State the objective** — split a problem into translation and solving, and write the constraints.
3. **Recall prior learning** — why a model cannot guarantee anything, from `TSC7-Advanced-K1`.
4. **Present the content** — the three arrangements, solver classes, soft constraints, auditability.
5. **Guide** — build the roster skeleton together and solve a small instance.
6. **Elicit performance** — teams encode a policy from their own organisation.
7. **Give feedback** — run each model, then read the infeasible cases.
8. **Transfer** — each learner names one decision in their work that should be a rule, not a judgement.

## What the framework doesn't mention but trainers need to know

- **The hard part is eliciting requirements, not writing code.** Budget for arguments about exceptions.
- **Solvers need time limits and fallbacks.** An operations system that hangs is worse than one that says "no solution found in 30 seconds".
- **Keep the model out of the solve.** Use it for extraction and explanation; never for the search itself.
- **Version the constraint set.** Policy changes must be traceable to roster outcomes.

## Watch out

- **Do not demo an LLM "solving" a scheduling problem.** It will look fine on eight items and fail on eighty.
- **Do not present a solver as infallible.** It is exact with respect to the model, and the model may be wrong.
- **Do not skip the soft-constraint discussion.** Binary thinking about rules is why real projects fail.
- **The stale claim to retire:** "symbolic AI is obsolete." In 2026 the guarantees are the scarce resource, and they come from solvers.
