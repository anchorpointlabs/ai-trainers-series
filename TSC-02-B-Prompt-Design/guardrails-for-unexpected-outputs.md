---
id: 02.01.B.K4
tsc: 2
level: Basic
code: K4
title: Guardrails for unexpected outputs
---

# Guardrails for unexpected outputs

> **TSC #2 Prompt Design · Basic · Knowledge K4**

**IMDA requirement:** Guardrails to prevent prompts from creating unexpected outputs.

**What it means:** A guardrail is a rule or check that helps keep an AI’s answer within a task. A prompt, the instruction you give an AI, can state the allowed facts, the desired format and what to do when information is missing. The AI may still make mistakes or ignore instructions, so prompt wording alone is neither a guarantee nor a security control, a measure enforced by the system to restrict what it can do. A person should check the answer against the original facts, and permissions for connected tools must be controlled separately.

**The learner must be able to:**
- Identify the task, allowed facts, output format and action for missing information in a prompt.
- Check an AI’s answer against the supplied notes and identify any unsupported detail.
- Explain why a prompt cannot enforce a restriction on a connected tool.
- Choose a separate tool-access control and decide whether to accept or reject an answer after checking it.

**Lesson Plan Ideas:**
1. Show the made-up room notes in the exercise. Ask: “What could go wrong if a notice states a capacity that the notes do not give?”
2. Use the room notice to explain task boundaries: specify the facts to use, the format and the response to missing information. Explain that the AI can still stray from these instructions. A person must compare the answer with the notes before use; separately, the tool owner can disable booking or sending access, or enforce human approval for each specific action in the connected system before it runs.
3. In pairs, identify the task, allowed facts, format and missing-information rule in the prompt. One learner runs it and the other checks the result against the notes and stated checks. Mark it pass or reject; identify a separate control that would stop the AI making an unauthorised booking.
4. Ask for a mismatch, or confirm that none was found. Discuss why an apparently correct answer does not prove the wording is a security control, and what to do if the check fails: reject the answer, correct or rerun it, and recheck it before use.

**Exercise (with the exact prompt):**
Setup: In pairs, use a chat AI with email and booking connections switched off; no files are needed.

```
Create a three-line notice for a made-up room booking using only the notes below.
Do not invent any facts. Do not book the room, send a message, or use any outside tools.
If a required detail is missing, write exactly Not provided for that detail.
Use exactly these labels in this order: Venue:, Time:, Capacity:. Put each on a separate line and add nothing else.

Notes:
Venue: Maple Room
Time: Tuesday at 10:00
The notes do not state the room's capacity.
```

Expected result: Three lines: `Venue: Maple Room`, `Time: Tuesday at 10:00` and `Capacity: Not provided`.
Check: Check for exactly three lines in the stated order; compare every value with the notes and expected result, rejecting any mismatch or extra detail. Name a separate control, such as disabling the AI’s booking access.