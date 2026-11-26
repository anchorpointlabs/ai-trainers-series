---
id: 07.03.A.K5
tsc: 7
level: Advanced
code: K5
title: Generative models beyond text: proteins, 3D scenes and world models
as_at: 2026-11-26
review_by: 2027-02-25
---

# Generative models beyond text: proteins, 3D scenes and world models

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K5**


> **Framework text (verbatim):** "Specialised uses of generative AI (e.g., protein generation, 3D model generation, world models)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 5 of 20

**One-line version:** Outside text the grammar changes — a protein must fold, a mesh must close, a world model must stay consistent for a thousand frames — and each domain brings its own verifier, which is what makes it tractable.

## What it is

Specialised generative applications adapt the same statistical machinery to domains with hard structural constraints: protein and molecule design, 3D assets and scenes, and learned simulators ("world models") that predict how an environment evolves. The models differ less in principle than in representation, constraint enforcement and the availability of a cheap test of correctness.

## Deep expansion

### The concept

Text generation has a soft constraint: it must read plausibly. These domains have hard constraints. A protein that does not fold is not a protein. A mesh with inverted normals cannot be rendered or printed. A world model that invents a door in frame 400 and loses it in frame 401 has failed regardless of how good frame 400 looked.

So the pattern in every specialised domain is the same three-part structure:

1. **A representation that makes constraint-satisfaction cheap** — backbone torsion angles, signed distance fields, Gaussians, latent physical state.
2. **A generator conditioned on the requirement** — bind to this receptor, fit this footprint, obey this control input.
3. **A verifier that is cheaper than reality** — a folding model, a physics engine, a mesh validator, a lab assay.

The third part is what separates a working application from a demo. Where the verifier is cheap and objective, generative design compounds: you propose a thousand candidates overnight and test the best twenty.

### The sub-concepts

**Protein and molecule generation.** Structure prediction tells you what a sequence folds into; generative design runs the other way, proposing sequences or structures that meet a binding or stability requirement. Diffusion over backbone geometry and autoregressive sequence models are both in use, and candidates are filtered by predicted structure, then synthesised and assayed in a wet lab. The loop is slow and expensive at the end, which shapes every design decision.

**3D asset and scene generation.** Text or image to mesh, Gaussian splats or radiance fields, plus scene layout that respects scale and collision. Production constraints are unforgiving: polygon budgets, UVs, materials, engine compatibility. A beautiful asset that needs three days of retopology has saved nobody time.

**World models.** A learned simulator that predicts next state from current state and action, trained on video or telemetry. Used to train robot policies and to fill simulation gaps. Their failure mode is compounding error: small inconsistencies accumulate over long rollouts, so short-horizon quality can hide long-horizon collapse.

**Evaluation is domain-specific.** Perceptual scores for images, validity and uniqueness for molecules, task success for policies, physical plausibility for scenes. No single metric travels between domains, which is why the framework's "specialised" framing is accurate rather than decorative.

### How it connects to the rest of the framework

`TSC7-Advanced-K4` is the research frontier these applications draw from; `TSC7-Advanced-K7` (synthetic data) is how many of them generate training material; `TSC5-Intermediate-K2` covers the metric families that must be replaced for each domain. `TSC7-Advanced-A1` is where a learner designs a method for one of these.

### What is current as of November 2026

Scientific design has become an industrial workflow rather than a demonstration: generative structure models feed automated assay pipelines in pharmaceutical and research settings, and materials discovery groups use them as candidate generators with simulation in the loop. On the 3D side, Gaussian-splat representations and diffusion-based asset generation have moved into production pipelines for games and heritage visualisation, usually with a human artist finishing the work. World models remain the most speculative of the three: impressive in short rollouts, still unreliable for long-horizon planning, which is exactly where robotics needs them.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Protein generation means we can skip the lab."* Predicted structures still need experimental confirmation; the model narrows the search, it does not close the loop.
- *"Text-to-3D replaces a 3D artist."* It replaces the blockout. Everything downstream — topology, UVs, rig, materials — remains skilled work.
- *"A world model is a simulator."* It is a learned approximation that fails where the training distribution ends, and it degrades over long horizons.

## How a student should understand it

**Mental model:** a very fast sketch artist who has seen a million examples and has never touched the material. Brilliant for options, useless as a final answer without a test bench.

**Three things they can do after this bullet:**
1. For a domain, name the representation, the constraint and the verifier.
2. Judge whether a generative approach is worth it by the cost of verification.
3. Spot compounding-error failure in a rollout rather than a single frame.

**Misconceptions to kill:** that generation removes the lab or the artist, and that a good single output implies a good model.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The tuition teacher who has never sat the paper.** They can produce a hundred plausible answers and have no idea which will pass marking. The verifier — the marker — is what makes the hundred answers useful. Where it breaks: in science the "marker" costs real money and weeks.

**The HDB renovation render.** A beautiful 3D render sells the flat; the contractor still needs measurements, load-bearing walls and a permit. Generation sells the idea, engineering delivers it.

### Worked example with a real tool

Have learners design a proposal-and-verification loop rather than ask for content:

```
We want to design peptides that bind a specific target protein.
We have: a structure prediction tool, a molecular dynamics
simulator, and budget to synthesise and assay 40 candidates.

Design the pipeline:
1. What the generative model proposes, and at what representation.
2. The three filters before synthesis, cheapest first, with the
   approximate cost of each (in relative terms, not dollars).
3. How many candidates to generate for 40 to survive.
4. The one failure mode that would waste the whole batch.
```

What to point at afterwards: most answers generate a hundred candidates and filter on the predictor alone. The teachable correction is *decorrelation* — filtering only on the same model that generated the candidates selects for the model's blind spots, so at least one filter must be independent.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a generated protein structure beside an assay result that contradicted it.
2. **State the objective** — specify representation, constraint and verifier for one domain.
3. **Recall prior learning** — manifold hypothesis from `TSC7-Advanced-K1`.
4. **Present the content** — the three-part pattern and domain-specific evaluation.
5. **Guide** — design the peptide loop together.
6. **Elicit performance** — groups do the same for 3D assets or a world model.
7. **Give feedback** — critique verifier independence and cost ordering.
8. **Transfer** — each learner names a domain in their own industry with a cheap verifier.

## What the framework doesn't mention but trainers need to know

- **Verification cost sets the ceiling.** If the test is expensive, generative design helps less than the papers suggest.
- **Domain data is the moat, not the model.** Structural biology, CAD libraries and sensor logs are where advantage lives.
- **Long-horizon consistency is the unsolved part.** Teach learners to test rollouts, not snapshots.
- **Regulatory and IP questions arrive early.** Generated molecules and assets raise ownership questions that predate deployment.

## Watch out

- **Do not present a single beautiful output as evidence.** Cherry-picked samples are the oldest trick in generative work.
- **Do not claim a domain is "solved".** Structure prediction improved enormously and still fails on the interesting cases.
- **Do not let the class leave thinking this is only for PhDs.** The pipeline design is an engineering skill they can practise today.
- **The stale claim to retire:** "generative AI is a text technology with side quests." In 2026 the highest-value applications are often the non-text ones.
