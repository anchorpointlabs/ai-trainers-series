---
id: 07.03.A.A5
tsc: 7
level: Advanced
code: A5
title: Designing agentic systems: loop, tools, memory and the leash
as_at: 2026-11-26
review_by: 2027-02-25
---

# Designing agentic systems: loop, tools, memory and the leash

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Ability A5**


> **Framework text (verbatim):** "Design agentic AI systems."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Ability · Bullet 16 of 20

**One-line version:** An agent is a model in a loop with tools and a budget — and almost every design decision is about the budget, the tools and what the loop is allowed to touch.

## What it is

Designing an agentic system means specifying the loop (plan, act, observe, revise), the tools it may call, the memory it carries, and the leash: permissions, limits, approval points and logging. The model is one component; the system around it determines whether the result is useful or a liability.

## Deep expansion

### The concept

Four elements, in the order that determines success:

**The loop and its termination.** Every iteration must move toward a checkable goal, and the system must know when to stop: goal met, budget exhausted, or no progress detected. Agents that loop without a termination condition burn money and produce nothing; agents that stop on the first plausible answer do not need a loop.

**The tools.** Few, well described, idempotent where possible, and shaped so that a mistake is recoverable. A tool that deletes, sends or pays needs a dry-run mode and an approval. Tool descriptions are prompt engineering — vague schemas produce wrong calls.

**The memory.** Working memory is the context window; episodic memory is the run log; semantic memory is retrieval over a store. Confusing these produces the classic failure where the agent "forgets" a decision it made ten steps ago because the transcript got truncated.

**The leash.** Permissions scoped to the task (least privilege), hard budgets on steps, tokens, wall time and money, sandboxed execution for generated code, human approval at irreversible steps, and an audit log of every action. This is not bureaucracy; it is what makes the system deployable at all.

### The sub-concepts

**Compounding error.** Each step is right 95% of the time; ten steps is under 60% end to end. Design for short trajectories, checkpoints and verification between steps, not for longer chains.

**Prompt injection through tool output.** Anything the agent reads — a web page, a PDF, an email, a ticket — can contain instructions. The lethal combination is untrusted content, access to private data, and an ability to send externally; break at least one of the three in every design.

**Trajectory evaluation.** You cannot evaluate an agent on its final answer alone. Score task success, number of steps, cost, and whether any unauthorised action was attempted. Replay logs are the dataset.

**Human-in-the-loop placement.** Put the gate where an error becomes irreversible, not where it is convenient. Approving a plan is cheap and useless; approving the final send is where value is protected.

**Multi-agent arrangements.** Specialists with a coordinator can work, but only when each agent has a narrow, verifiable job. Debate and self-critique without an external check mostly add cost.

### How it connects to the rest of the framework

`TSC7-Advanced-K2` covers the integration contexts an agent operates in; `TSC7-Advanced-A1` supplies the method primitives the loop uses. `TSC6-Intermediate-K7` and `TSC6-Intermediate-A4` cover guardrails and moderation that sit beside the leash. `TSC9-Intermediate-K4` covers the security failure modes; `TSC8-Intermediate-A3` covers the governance approvals.

### What is current as of November 2026

Agents moved from demos to supervised production during 2025–26, and the design vocabulary hardened around tool protocols, sandboxed execution and approval gates. Current frontier models are notably better at holding a long task plan, which raises the temptation to remove human checkpoints. Resist it: the model's reliability improved, and the consequence of a wrong irreversible action did not. Expect procurement to ask for the audit log before the capability demo.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"An agent is a chatbot with tools."* A chatbot with tools and no termination condition is a cost incident.
- *"Better models make guardrails unnecessary."* Better models make guardrails more effective, not less necessary.
- *"More autonomy means more value."* Value comes from completed tasks per dollar, and autonomy usually raises cost before it raises completion.
- *"If it works in the demo, the design is sound."* Demos run on curated inputs and short trajectories.

## How a student should understand it

**Mental model:** a new hire with a company card, a laptop and no memory of yesterday. You would not hand over the card without a limit and a receipt policy.

**Three things they can do after this bullet:**
1. Write the loop's termination conditions and budgets before the prompt.
2. Design a tool set with one approval gate at an irreversible step.
3. Evaluate an agent on trajectory metrics, not final answers alone.

**Misconceptions to kill:** that agents are chatbots with tools, that autonomy is the goal, and that models replace guardrails.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The intern with a company card.** Capability is high, judgement is unproven, and the limit is what makes them safe to deploy. Receipts are the audit log. Where it breaks: an intern learns from being told off; an agent's policy is fixed until you change the code.

**The MRT driver and the signalling system.** The driver acts, the system enforces the safe envelope. Remove the signalling and the driver's skill becomes a liability.

### Worked example with a real tool

Design the leash before the prompt:

```
Build an agent that answers procurement policy questions and,
when authorised, raises a purchase request in our ERP.

1. List the tools it needs, with the exact permission scope for
   each, and which ones are irreversible.
2. The loop's termination conditions (three of them).
3. Where the human approval sits, and what the approver sees.
4. Three prompt-injection paths into this agent, and which leg of
   the trifecta each design change breaks.
5. The five metrics you would log per run.
```

What to point at afterwards: learners almost always forget that the policy documents themselves are untrusted input — a supplier-submitted PDF in the knowledge base can carry instructions. The correction is architectural: retrieval content is data, never instructions, and the write tool requires an approval that displays the exact amount and vendor.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — a run log where an agent retried a failed payment four times.
2. **State the objective** — specify loop, tools, memory and leash for one workflow.
3. **Recall prior learning** — tool contracts from `TSC6-Basic-K1`.
4. **Present the content** — the four elements, compounding error, injection, trajectory evaluation.
5. **Guide** — design the procurement agent together.
6. **Elicit performance** — teams specify an agent for their own process.
7. **Give feedback** — red-team each design for injection and irreversible actions.
8. **Transfer** — each learner runs a two-step agent locally and logs the trajectory.

## What the framework doesn't mention but trainers need to know

- **Cost per completed task is the metric.** Agents fail by spending, not only by erring.
- **Idempotency is the difference between a retry and a duplicate payment.** Every write tool needs a request key.
- **Logs are the product.** Without trajectories you cannot debug, evaluate or audit.
- **Start with one tool and one checkpoint.** Systems that work grow from that; systems that start broad rarely ship.

## Watch out

- **Do not demo an agent with live credentials.** It is the fastest way to create an incident in a training room.
- **Do not present autonomy as the objective.** The objective is completed work at acceptable cost and risk.
- **Do not skip the injection discussion.** It is the security lesson that matters most here.
- **The stale claim to retire:** "agents will replace workflows." In 2026 agents execute bounded tasks inside workflows that humans still own.
