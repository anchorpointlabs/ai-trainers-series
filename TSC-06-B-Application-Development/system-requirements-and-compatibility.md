---
id: 06.01.B.K6
tsc: 6
level: Basic
code: K6
title: "System requirements: the unglamorous checklist that decides whether it runs"
---

# System requirements: the unglamorous checklist that decides whether it runs

> **TSC #6 Generative AI Application Development and Deployment · Basic · Knowledge K6**


> **Framework text (verbatim):** "Fundamentals of system requirements and compatibility."
>
> **TSC #6** Generative AI Application Development and Deployment · **Basic** · Knowledge · Bullet 6 of 11

**One-line version:** Nothing in this bullet is interesting, and everything downstream depends on it.

## What it is

System requirements are the conditions a machine must meet for software to run: operating system and architecture, runtime version, memory, disk, graphics hardware, network access and permissions. Compatibility is whether the specific combination you have chosen — library version, model, operating system, region — works together. Both are checked before the build, not after it fails in front of a client.

## Deep expansion

### The concept

Every generative AI application is two systems pretending to be one: the code you write, and the machine that runs it. The code has requirements; the machine has a supply; compatibility is the overlap.

Learners skip this because tutorials assume it and demos hide it. The tutorial runs in the author's environment, the demo on the trainer's laptop, the pilot on a locked-down corporate image behind a proxy with no admin rights and a Python version two releases behind. The gap between those three is where projects die, and it is entirely predictable.

The professional habit is to write the target environment down before writing code, and to treat any requirement you cannot verify as a risk rather than an assumption.

### The sub-concepts

**The target environment, written down.** Operating system and version, architecture (x86 or ARM), runtime version — Python 3.11 versus 3.13 is not cosmetic — memory, free disk, GPU present or not, browser, network restrictions, and whether the user has administrator rights.

**Dependencies and the version graph.** Every library depends on others within version ranges. Two packages can each be satisfied and still be incompatible with each other. A lockfile records the exact resolved set so tomorrow's machine matches today's.

**Hardware for local models.** Running a model locally trades API cost for memory: enough to hold the weights plus the working context. Quantisation is the lever that moves a model from "needs a workstation" to "runs on a laptop", at some cost in quality.

**The corporate perimeter.** Outbound access to the model provider, proxy configuration, TLS inspection that breaks certificate validation, blocked ports and egress rules. In large Singapore enterprises this is where most pilots stall.

**Region and data residency.** Model availability, feature availability and where data is processed all vary by region. A solution demonstrated on a US tenant may not be procurable here.

### How it connects to the rest of the framework

`TSC6-Basic-K4` is the tool layer that generates these requirements; `TSC6-Basic-A5` records and maintains the configuration once it exists; `TSC6-Basic-K3` includes the errors that appear when these checks were skipped. `TSC6-Intermediate-K3` (cloud deployment) and `TSC6-Advanced-K1` (compute efficiency) are this bullet at professional depth.

### What is current as of November 2026

- **Local inference became ordinary.** Quantised open models now run acceptably on consumer laptops, so "we must call an API" is no longer true for every use case — especially where data cannot leave the building.
- **Most teams still never run a model.** They call a hosted API, which moves the compatibility question from graphics memory to SDK version, region and quota. Teach both, and say which one your learners will meet.
- **Containers became the default answer to "works on my machine".** Packaging the app with its runtime removes most of this bullet's pain and is now table stakes in any deployment conversation.

### Common misconceptions

- *"If it runs on my laptop, it will run on the server."* Your laptop has your versions, proxy settings and admin rights. The server has none of them.
- *"Latest version is best."* Best for security patches, worst for a working demo on Monday. Pin, then upgrade deliberately.
- *"More RAM fixes it."* RAM fixes memory faults, not a missing GPU, a blocked port or a Python mismatch.

## How a student should understand it

**Mental model:** an air-conditioner site survey. The installer measures the ledge, checks the bracket, finds the power point and asks about the lease before quoting. Skip the survey and you buy a unit that does not fit — expensively.

**Three things they can do after this bullet:**
1. Write a one-page target-environment sheet for their own project before building.
2. Read a library's requirements and identify which ones their environment does not meet.
3. Explain why a demo that worked on the trainer's laptop failed on the corporate image.

**Misconceptions to kill:** that environment differences are bad luck, that "latest" is a strategy, and that a cloud deployment has no requirements to write down.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The aircon site survey.** Nobody enjoys it, everybody who skips it pays. The bracket, the power point, the drainage slope and the lease permission are four boring checks that decide whether the installation happens at all.

**The approved calculator list.** For national examinations only listed models are permitted, and the list is published. Software versions work the same way: the target environment publishes what it supports, and an unlisted combination is a risk you take knowingly rather than a mystery you discover later. Where it breaks: unlike an exam, you can sometimes change the environment — but before the build, not during.

### Worked example with a real tool

Give the room a target machine and a requirements file, and ask an assistant to do the survey:

```
Target machine: Windows 11 laptop, 16 GB RAM, no dedicated GPU, Python 3.12,
corporate proxy with TLS inspection, no administrator rights, HTTPS only.

requirements.txt:
openai==0.28.1
langchain==0.1.0
torch==2.0.1
streamlit

Tell me, in order of certainty, which of these will fail on this machine and why.
Then give the smallest set of versions that work together on Python 3.12.
Mark anything uncertain as "verify with pip".
```

What to point at afterwards: the first two diagnoses are solid — the legacy SDK and the pinned old framework are real mismatches — and the version recommendations are partly invented. The lesson is the method: form hypotheses from the requirements, then verify on the machine itself with `pip install --dry-run`, `python --version` and the vendor's compatibility page.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — hold up two laptops. One runs the demo, one does not. Ask what is different. Nobody knows, which is the point.
2. **State the objective** — by the end you can write the environment sheet, read a requirements list, and predict the likely compatibility failures for a target.
3. **Recall prior learning** — the error catalogue from K3; the layer map from K4.
4. **Present the content** — the environment sheet, the version graph, the network perimeter, minimum versus recommended.
5. **Guide** — complete an environment sheet for the training room's own machines, together.
6. **Elicit performance** — groups get a different target (locked-down office PC, cloud VM, phone) and a different stack, and produce the sheet plus a ranked risk list.
7. **Give feedback** — compare sheets. The recurring miss is the network; make that visible.
8. **Transfer** — each learner writes the sheet for their next real project and sends it to whoever owns the machines.

## What the framework doesn't mention but trainers need to know

- **Ask about admin rights first.** It determines whether they can install anything at all, and it is the most common blocker in Singapore training rooms.
- **TLS inspection breaks more AI pilots than model quality does.** A re-signing proxy makes calls fail with a certificate error that looks like an outage.
- **Disk is the forgotten constraint.** Model weights and container images are large; tens of gigabytes of free space is not unusual for local work.

## Watch out

- **Do not treat this bullet as the boring one and rush it.** It decides whether the rest of the course survives contact with the learner's office.
- **Do not quote hardware figures from memory.** Requirements change per model and per quantisation; read the model card.
- **The stale claim to retire:** "you need a GPU to run a language model." In November 2026 a quantised small model runs on a laptop, and a hosted API needs no local hardware at all.
