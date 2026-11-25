# REA-01 · ReAct: reason plus act

**Framework home** — New GenAI TSC #3 Prompt Engineering, **Advanced**: K *techniques that extend capabilities of generative AI models (e.g. Retrieval-Augmented Generation, external tools and libraries)*; A *apply prompt engineering strategies to extend model capabilities*. Also the conceptual ancestor of TSC #6 (application development and deployment) and of the IMDA Model AI Governance Framework for Agentic AI (Jan 2026).

---

## What it actually is

ReAct is a loop, not a prompt trick. The model alternates:

**Thought** (what do I need?) → **Action** (call a tool: search, calculator, database, API) → **Observation** (what came back) → **Thought** (does that answer it, or what next?) → repeat → **Answer**.

The insight is that a language model's two weaknesses are complementary: it reasons reasonably but knows nothing current and cannot compute reliably; tools compute and retrieve perfectly but reason not at all. Interleaving them fixes both — provided something stops the loop.

That "something" is the whole engineering story. In production, ReAct needs: a defined tool inventory, a stopping condition, an error path for when a tool fails, a permission boundary, and a log. Without those, you have a system that can confidently query the wrong database five times in a row.

This is the pattern behind what the industry now calls **agents** — and the reason IMDA published a dedicated governance framework for agentic AI in January 2026, covering human oversight, action boundaries and accountability. If you teach ReAct, you are teaching the first chapter of that framework whether you say so or not.

## Why it matters at work

Every "AI that books the meeting / files the claim / checks the inventory" is ReAct underneath. Understanding the loop lets a non-developer ask the right procurement questions: what tools can it call, what can it not do, who approves an action, and what is logged.

## The student lens

**Mental model to install:** a new intern with a phone, a login and no memory of yesterday. Capable, fast, needs a checklist and a supervisor.

**Misconceptions you will hear:**
- *"ReAct is a better prompt."* It is an architecture: model + tools + control loop.
- *"If it can search, it won't hallucinate."* It can retrieve the wrong thing, misread the right thing, or act on stale data. Retrieval moves the failure, it doesn't delete it.
- *"Agents are just chatbots with plugins."* The difference is *autonomy over actions*, which is exactly where governance starts.

**Five-minute practice:** give learners a task ("find the current GST rate and compute the GST on $4,820") and have them write the Thought/Action/Observation sequence by hand, including what they would do if the search returned 2023 data. The handwritten loop teaches more than any demo.

## The adult educator lens

**Analogy:** a delivery rider with a phone. "Thought" is reading the address; "Action" is checking the map; "Observation" is the traffic report; then re-plan. The rider is useful because they can *act*, and risky for the same reason. Nobody would let a rider deliver to any address they liked without a record — same principle.

**Three-minute demo:** run a tool-enabled assistant on a live question with a calculation in it. Narrate the loop out loud as it happens: "it decided to search… it read that page… now it's calculating… now it's checking." Then deliberately ask something the tools cannot answer and show how the loop terminates — or fails to.

**Board sketch:** a circular arrow with four stations (Thought, Action, Observation, Thought), and a straight arrow exiting the circle labelled "Answer". Around the circle, write the five controls: tool list, stop condition, error path, permissions, log.

**Where it goes wrong in class:** someone asks "so can it do my job?" Redirect to the precise answer: it can execute a defined loop inside defined permissions. The judgement about *which* loops to allow, and what counts as acceptable error, remains the job — which is why the governance framework exists.

**Check for understanding:** "Your agent has search and email access. Name two things you would restrict before letting it run unattended, and where you would look afterwards to see what it did."

## Say this out loud

"ReAct is a loop with tools. The loop is the easy part; the brakes are the product."

## Content hook

**LinkedIn opener:** "Everyone is building 'agents'. Almost nobody has written down what the agent is not allowed to do. That document is the actual deliverable."

**Carousel idea:** "Anatomy of an agent, in five controls" — tool list, stop condition, error path, permissions, log. One slide each, with the failure it prevents.
