# CTX-01 · Context window and context engineering

**Framework home** — New GenAI TSC #1 Generative AI Principles and Applications (Basic): *limitations of AI models* — why a model appears to forget. Carried up to TSC #3 Prompt Engineering (Intermediate), K5: *context window limitations, long-context implications, strategies to work within them*.

---

## What it actually is

The context window is the number of tokens a model holds in view for one request: instructions, conversation, attachments and the answer being written, counted together. Nothing survives between conversations; inside one, the whole history is re-sent every turn.

"Forgetting" is three different failures:

1. **Truncation** — input exceeds the window; the oldest turns are dropped.
2. **Eviction** — the app quietly compresses a long thread to make room.
3. **Attention degradation** — recall of one detail across a long input is uneven; the start and end come back more reliably than the middle.

Context length is capacity, not comprehension. Context engineering is spending it well: instructions at the edges, stated first and repeated last; summarise the middle; retrieve rather than paste; one task per thread. A 200-page PDF paste is usually wrong: it turns a precise question into retrieval.

## Why it matters at work

A tender summary that reads well and misses the risky clause is the expensive failure. Every pasted page is billed on every turn, and a context you cannot reconstruct is an answer you cannot defend.

## The student lens

**Mental model to install:** a desk, not a filing cabinet. What is not on the desk cannot be used, and a crowded desk hides the line.

**Misconceptions you will hear:**
- *"Huge window, so it remembers everything."* It can hold the page and still miss the line.
- *"It got confused."* You truncated, it compressed, or the detail was buried.
- *"Attach the PDF and ask anything."* The file is pasted as text, not indexed.

**Five-minute practice:** ask a question with a whole report attached; then a fresh thread with only the answering paragraph, plus "quote the sentence, then answer". Compare.

## The adult educator lens

**Analogy:** the counter at a hawker stall, not the storeroom. You cook with what is on the counter; the storeroom needs fetching, and that is retrieval. Fill the counter and the dish gets crowded out. Where it breaks: the stallholder decides what to clear; the app does it silently.

**Three-minute demo:**
1. Paste a long tender, ask for a figure and its clause. Fluent, vague.
2. Ask for a middle detail. It guesses.
3. New thread: two paragraphs, plus "quote the sentence; if not stated, write NOT STATED."
4. Run it. Same model, different discipline.

**Board sketch:** a horizontal bar, "window, in tokens": SYSTEM / CONVERSATION / ATTACHMENT / ANSWER. Arrows both ends: "instructions here, and again here". Middle shaded: "summarise or retrieve".

**Where it goes wrong in class:** someone asks whether to buy the biggest window. That raises the ceiling, not the attention, and every token in it is billed. Use the smallest context that holds the answer.

**Check for understanding:** "60-page contract, one question about a payment term. Name the two steps before you ask, and the one line you add." They have it if they locate the section, paste only that, and demand a quote.

## Say this out loud

"The window isn't memory. It's desk space, and you pay rent on every page."

## Content hook

**LinkedIn opener:** "Your AI didn't forget your instructions. You ran out of desk."

**Carousel idea:** "Same document, two threads": the whole-file answer beside the two-paragraph one, then the rules.
