# Describe prompt techniques

> **TSC #2 Prompt Design · Basic · Ability A1**

**Bullet (verbatim):** Describe fundamental prompt design techniques.

**What it means:** A prompt is what you ask a chat AI to do. Zero-shot prompting gives the task and any needed information but no worked example of the task; one-shot prompting includes one worked example, such as a sample note and its finished notice, before the new task. A second try means running a prompt again; it is not the same as giving an example in a prompt. An example can show the format you want, but it does not guarantee a correct reply.

**The learner must be able to:**
- Describe zero-shot and one-shot prompting by counting the worked examples provided.
- Identify a worked example and the new task in a prompt, and distinguish an example from a second try.
- Choose a technique for a simple task and give a reason for the choice.
- Check a generated notice against its source note and the requested format.

**How to teach it in 20 minutes:**
1. Ask: “We need a two-line room closure notice. How could we show a chat AI the layout we want? Does sending a request twice count as giving an example?” Take two or three guesses. (3 min)
2. Show the two prompts below. In the first, point out that the Cedar note is the task input, not a worked example. In the second, point out the Birch note and finished notice: together they are one worked example. Explain zero-shot and one-shot, then distinguish giving that example from running a prompt a second time. Suggest starting with zero-shot when instructions are clear and no example is needed, or one-shot when a suitable example can show a preferred pattern; neither guarantees a correct result. (7 min)
3. In pairs, run the zero-shot prompt twice in separate fresh chats, then the one-shot prompt in another fresh chat. Check each notice using the criteria below. For each prompt, write down the number of worked examples and explain why the second zero-shot run is still zero-shot. Choose which technique to start with for a clear request with no sample, and which for a team with an agreed sample layout; give one reason for each. (8 min)
4. Debrief: the zero-shot prompt has no worked examples on either run; the one-shot prompt has one, about Birch. Cedar is the new task in both. Ask pairs to report a missing detail or format error if they found one, and explain how the check revealed it. (2 min)

**Exercise (with the exact prompt):**
*Setup: Use a chat AI (an account if required), starting a fresh chat for each run; no files are needed.*

Zero-shot prompt — run twice, each time in a fresh chat:

```text
Turn the following fictional facilities note into exactly two lines for a staff notice. The first line must begin 'Affected:' and include the room, closure day and reason. The second line must begin 'Reopens:' and give the reopening day and time. Do not add anything else.

Now write the notice for this note:
Note: The Cedar meeting room will be closed for floor cleaning on Tuesday and will reopen on Wednesday at 9 am.
```

One-shot prompt — run once in a fresh chat:

```text
Turn the following fictional facilities note into exactly two lines for a staff notice. The first line must begin 'Affected:' and include the room, closure day and reason. The second line must begin 'Reopens:' and give the reopening day and time. Do not add anything else.

Example:
Note: The Birch meeting room will be closed for lighting repairs on Monday and will reopen on Tuesday at 10 am.
Affected: Birch meeting room closed on Monday for lighting repairs.
Reopens: Tuesday at 10 am.

Now write the notice for this note:
Note: The Cedar meeting room will be closed for floor cleaning on Tuesday and will reopen on Wednesday at 9 am.
```

*Expected result:* Each run produces a two-line notice about Cedar meeting room, Tuesday, floor cleaning and reopening on Wednesday at 9 am.  
*What to check:* The lines start with `Affected:` and `Reopens:` in that order, include all those facts on the requested lines and nothing extra; count worked examples in the prompt, not the runs.

**Common mistakes:**
- Counting the new Cedar note as an example — it is the input to process; a worked example also shows the desired answer.
- Calling a second zero-shot run one-shot — count examples provided in the prompt, not attempts.
- Assuming an example makes the reply correct — check the room, day, reason, reopening time and two-line format against the note.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf — accessed 2026-11-15. Page 5 gives the TSC, level and verbatim ability bullet.
- https://proceedings.neurips.cc/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf — accessed 2026-11-15. Brown and colleagues define zero-shot as a task description without examples and one-shot as one task demonstration; they describe examples as input and desired completion pairs.
- https://developers.openai.com/api/docs/guides/prompt-engineering — accessed 2026-11-15. OpenAI describes using input/output examples to guide a response and notes that generated outputs can vary.
- https://dl.acm.org/doi/abs/10.1145/3411763.3451760 — accessed 2026-11-15. Reynolds and McDonell report cases where zero-shot outperformed prompts with several examples, supporting the caution that examples do not guarantee better results.
