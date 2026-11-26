---
id: 02.01.B.K3
tsc: 2
level: Basic
code: K3
title: Different output modes
---

# Different output modes

> **TSC #2 Prompt Design · Basic · Knowledge K3**

**Bullet (verbatim):** Impact of prompts on different modes of AI output.

**What it means:** A prompt is the instruction you give an AI; it can ask for different forms of result. For an update to a colleague, specify the reader, length and facts; for code, specify the programming language, data and what the program should do. Code is text containing instructions for a computer, so check it by running it as well as reading it. A prompt does not guarantee a correct result, and actual replies can vary.

**The learner must be able to:**
- Identify the different requirements in a prompt for a written update and one for code.
- Compare the two replies against the requested form and the same supplied facts.
- Run the generated code against the expected result and check what happens when one value changes.
- Explain why an apparently correct written reply does not show that a program will work.

**How to teach it in 20 minutes:**
1. Ask: “If I need a room update for a colleague and a program to calculate the same figures, should I ask for exactly the same thing?” Collect two ideas. (3 min)
2. Using the invented room figures below, contrast a text prompt's reader and two-sentence limit with a code prompt's language, data, calculation and exact printed lines. Python 3 is a programming language; variables are named places to store values, and external libraries are extra packages of pre-written code. Both replies arrive as text in the chat, but the second is intended to be run. (7 min)
3. In pairs, run the two prompts in separate new chats. Check the update, inspect the code for unwanted operations, and run the code in the Python 3 runner. Change the booked value as directed below and run it again. (8 min)
4. Debrief: Which prompt details shaped each form? What went wrong, or might go wrong, if a readable answer is treated as a working program? Compare the checks used for each. (2 min)

**Exercise (with the exact prompt):**
*Setup: a chat AI and a Python 3 runner (a tool for running Python programs); use a separate new chat for each prompt and only the invented data provided.*

Text prompt:
```text
Use these invented figures: Cedar has 3 seats, of which 2 are booked; Ash has 5 seats, of which 1 is booked. Available seats are total seats minus booked seats.
Write a short update for a colleague in exactly two sentences, one per room. Each sentence must state the room name, how many seats are booked and how many are available. Use British English. Return only the update.
```

Code prompt (Markdown fences are lines of three backtick characters used to mark a code block):
```text
Use these invented figures: Cedar has 3 seats, of which 2 are booked; Ash has 5 seats, of which 1 is booked. Available seats are total seats minus booked seats.
Write a complete Python 3 program that stores the four given numbers in variables named cedar_seats, cedar_booked, ash_seats and ash_booked. Calculate each room's available seats by subtraction. Print the room names, booked values and calculated available values as exactly these two lines:
Cedar: 2 booked, 1 available
Ash: 1 booked, 4 available
Use no input, files or external libraries. Return only the code, without an explanation or Markdown fences.
```

Expected result: The update has two sentences with Cedar 2 booked/1 available and Ash 1 booked/4 available; the program prints `Cedar: 2 booked, 1 available` and `Ash: 1 booked, 4 available` on separate lines.

What to check: Count the sentences and check their facts; inspect the code and do not run it if it does anything beyond storing values, calculating and printing. Otherwise run it, change `cedar_booked` from 2 to 1, and run again: Cedar should show `1 booked, 2 available`, while Ash remains unchanged.