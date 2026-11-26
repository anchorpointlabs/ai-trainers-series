---
id: 02.01.B.A6
tsc: 2
level: Basic
code: A6
title: Identify effective prompt practices
---

# Identify effective prompt practices

> **TSC #2 Prompt Design · Basic · Ability A6**

**IMDA requirement:** Identify best practices for designing effective prompts.

**What it means:** A prompt is the instruction you give an artificial intelligence (AI) tool, such as a chat tool that can produce text. Useful habits include stating the task and audience clearly, supplying the facts needed and specifying important limits on the answer, such as its length. Use plain language, check the answer against the requirements and revise the instruction if needed; there is no single fixed template for every task.

**The learner must be able to:**
- Identify useful details missing from a vague prompt, such as the audience and event facts.
- Revise a prompt in plain language using the relevant supplied facts and the required answer length.
- Check an answer against those facts and requirements, then suggest a prompt change if something is missing.

**Lesson Plan Ideas:**
1. Ask: “If a colleague simply says ‘Write a notice’, what would you need to ask before writing it?” Collect a few suggestions. 
2. Explain the central habit: give the details needed for the job. Using the notice task below, point out the audience, event facts and two-sentence limit; ask learners which details would also matter in a notice from their own workplace. Stress that clear words and relevant information matter more than a fixed formula. 
3. In pairs, read the original prompt, invented facts and task requirements in the exercise. Identify two things missing from the original and write your own improved prompt before generating the AI example . Paste the exact block into a new chat, independently check its revised prompt and notice using the check below, and amend your own prompt if needed . Run your own revised prompt in another new chat and check the notice against the same facts and length . 
4. Ask pairs which detail they added and why. If a notice missed a requirement, ask how they would make that requirement clearer in their prompt; if none did, ask what they would change if the date were missing. 

**Exercise (with the exact prompt):**
*Setup: Work in pairs with a chat AI, using a new conversation for each run; no files are needed and all event details are invented.*

```text
The original prompt is: Write a notice.

For this invented task, Pine Street Community Library is holding a book swap on 12 March 2027, from 2 pm to 4 pm, in the library hall. Visitors should bring one book to swap.

1. Rewrite the original prompt in plain language so a chat AI can write a notice for library visitors. Include the relevant facts above, ask for exactly two sentences and instruct it not to add event details that were not supplied. Label this "Revised prompt".
2. Following your revised prompt, write the notice. Label it "Notice".
```

Expected result: A revised prompt for library visitors, followed by a two-sentence notice about the book swap.
Check: Both your revised prompt and the AI's should specify the library, book swap, 12 March 2027, 2 pm to 4 pm, library hall, one book per visitor, two sentences and no added event details; the notice should include the facts, contain exactly two sentences and add no unsupported event details.

**Common mistakes:**
- Asking only “Write a notice” — say what the notice is about and who will read it.
- Leaving out a known event detail or adding irrelevant material — include the facts needed for this task, such as the date and place.
- Treating a fluent answer as proof it met the request — check the facts and sentence count, then clarify the prompt if needed.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf — accessed 2026-11-15; page 5 states the TSC, level and ability bullet.
- https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api — accessed 2026-11-15; recommends clear, specific instructions on context, outcome, length and format, and acknowledges that different formats may fit different tasks.
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices — accessed 2026-11-15; recommends clear instructions, useful context and explicit output requirements, and suggests checking whether a person with little context can follow the prompt.
- https://developers.openai.com/api/docs/guides/prompt-engineering — accessed 2026-11-15; discusses relevant context, variation in AI outputs and testing against requirements while revising prompts.
