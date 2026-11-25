# Tokens and tokenisation

**Framework home** — New GenAI TSC #1 Generative AI Principles and Applications (Basic): *introduction to popular generative AI models and how they work*; and at Intermediate, *model workings, including training data, algorithms and outputs*. Sits underneath TSC #3 Prompt Engineering (Intermediate), K5: *context window limitations and strategies to work within them*.

---

## What it actually is

A language model never sees your sentence. Before anything else happens, text is broken into **tokens** — chunks of characters that the model treats as its atomic units. A token is often a word, sometimes part of a word, sometimes a single space plus a letter. "Unbelievable" might become `un | believ | able`. "Singapore" is often one token; "Toa Payoh" is usually two.

This is not a design choice made for tidiness. It is a consequence of how these models are trained: they learn statistics over token sequences, so the token is the unit of meaning, cost, and memory.

Three consequences follow, and they are the whole reason this topic earns a place in a Basic course:

1. **Character-level work is genuinely hard.** Counting letters, reversing strings, checking spelling character by character — the model never had characters, only chunks. (The classic "how many r's in strawberry" demo is now partly patched by newer models and reasoning modes; that repair is itself worth teaching, because it shows the limitation was real.)
2. **Everything is measured in tokens.** Context windows, pricing, rate limits, latency, truncation. A 20-page report is roughly 8,000–10,000 tokens; a long chat with attachments hits limits faster than people expect.
3. **Efficiency varies by language and content.** English is the most token-efficient major language; Chinese, Tamil and Malay typically need more tokens for the same meaning, and code and numbers tokenise unevenly. A model that "feels smarter in English" may simply be seeing fewer, cleaner chunks.

Tokenisers are model-specific. The same sentence can be 14 tokens on one model and 19 on another — which is why cost comparisons between tools done "by feel" are usually wrong.

## Why it matters at work

Every "the AI forgot what I said", every surprise bill, every truncated summary and every failed letter count traces back here. Knowing tokens turns a mysterious failure into an arithmetic problem you can fix by shortening the input or splitting the task.

## The student lens

**Mental model to install:** the model reads in LEGO bricks, not letters. You can hand it a wall built of bricks; you cannot ask it to count the studs.

**Misconceptions you will hear:**
- *"It reads like I read."* No — it reads chunks, and the chunk map differs per model.
- *"One word equals one token."* Usually 1 word ≈ 1.3 tokens in English; much worse in other languages and in code.
- *"A bigger context window means I can paste anything."* You can paste more, but attention degrades across very long inputs — capacity is not comprehension.

**Five-minute practice:** paste a 300-word email into a tokeniser tool (OpenAI's tokenizer page, or the token count in a playground) and compare with the word count. Then paste the same email in Chinese and compare. Have them write down the two ratios; they will remember their own numbers better than any slide.

## The adult educator lens

**Analogy:** Tokens are like the cuts a butcher makes. You hand over a whole chicken; the model receives parts. Ask it to reassemble the exact original bird and it will do a confident, plausible, slightly wrong job. The cut is fixed before your request arrives — you cannot ask for a different cut mid-sentence.

**Three-minute demo:**
1. Ask the live tool: "How many times does the letter r appear in strawberry?" Let the room see the answer.
2. Open a tokeniser and show the actual split.
3. Now ask it to spell the word with spaces between letters ("s t r a w b e r r y"), then count. It usually succeeds.
4. Close with the point: we didn't make the model smarter, we changed the units it was working with.

**Board sketch:** draw a sentence as a row of whole words, then draw a vertical line through the middle of two words to show the split, then write "= 1 token each" above the pieces. Under it, write the three consequences: characters, cost, language.

**Where it goes wrong in class:** someone will say "then why does it write perfect English?" Answer honestly: it never needed letters to write; it needs letters only to *count* them. Fluent output and exact character operations are different skills, and the second one is where it slips.

**Check for understanding:** "You have a 400-page PDF and a model with a 128k context window. Name two things you must check before pasting." (Answer: does it fit in tokens, not pages; and does the task need exact recall across the whole document.)

## Say this out loud

"The model doesn't read your words. It reads pieces, and it pays for the pieces."

## Content hook

**LinkedIn opener:** "Your AI didn't forget your instructions. You handed it 90,000 tokens and asked it to care about paragraph one."

**Carousel idea:** "The token bill, explained in five slides" — one slide per consequence (characters, cost, language, truncation, the fix), each with a real screenshot.
