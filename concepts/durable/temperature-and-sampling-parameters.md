# Temperature and sampling parameters

**Framework home** — New GenAI TSC #2 Prompt Design (Basic), K5: *techniques in prompt construction, including hyper-parameters such as temperature and sampling parameters*. Basic level: recognise the controls, know your task's regime, know what to do when the tool hides them.

---

## What it actually is

At every step the model gives each candidate next token a probability; sampling chooses one. **Temperature** reshapes that list before the choice — low sharpens it toward the top candidates, high flattens it so unlikely tokens get a real chance. OpenAI-style APIs commonly expose 0 to 2 with a mid-range default; others use 0 to 1 or 0 to 2. The numbers do not travel between tools.

**Top-p** (nucleus) keeps the smallest set of tokens whose probabilities sum to p, then samples inside it — adaptive to confidence. **Top-k** keeps a fixed number of candidates. Change one, not all three.

None of this is a determinism switch. Zero means "usually the most likely token", not "always the same string" — batching, model updates and routing move the text. Most chat apps expose none of it; there the skill is choosing the tool, tightening output shape, re-running.

## Why it matters at work

Pulling figures off invoices is a task where variation is a defect; drafting subject lines is one where it is the product. A team that cannot name its regime gets creative numbers and identical drafts.

## The student lens

**Mental model to install:** temperature is how wide the shortlist is at every single word, not how imaginative the idea is.

**Misconceptions you will hear:**
- *"Zero means repeatable."* Close in behaviour, false in text. Test it before promising it.
- *"Higher means smarter."* Broader: more variety and more error in one motion.
- *"The chat app slider is temperature."* Often a different setting, or absent.

**Five-minute practice:** run one extraction prompt five times at default, counting identical outputs; then add "answer with the number only" and run five again.

## The adult educator lens

**Analogy:** ordering at a hawker stall. At zero, the uncle makes your usual, the same way every time. Turned up high, today's laksa arrives with sambal you didn't ask for: still laksa, not yours. Where it breaks: he has taste; the model is rolling dice over a shortlist.

**Three-minute demo:**
1. Lowest temperature: a name for a Toa Payoh coworking space, twice. Near-identical.
2. Maximum, twice. Wildly different.
3. Then a decision: "Which department approves a $3,200 claim?" Run it repeatedly at high temperature and watch it flip.
4. Rule: variance is a feature for drafting, a defect for decisions.

**Board sketch:** a bar chart for "The meeting is ___", four candidates, sharp and tall at low temperature, flat at high. Under it: "it reshapes the shortlist; it adds no knowledge."

**Where it goes wrong in class:** someone demands a number. No universal value exists, only regimes: extraction, classification and code want the lowest allowed; drafting wants the default, several outputs, a human pick. If the dial is hidden, change the prompt.

**Check for understanding:** "Name one task where you want identical output every time, and one where you want it to differ. What do you change when there is no temperature setting?"

## Say this out loud

"Temperature doesn't make the model smarter. It makes it more willing to pick the second-best word."

## Content hook

**LinkedIn opener:** "Same prompt, same document, different number. The setting nobody touched is the reason."

**Carousel idea:** "One prompt, five temperatures": the same prompt at five settings, a one-line verdict under each.
