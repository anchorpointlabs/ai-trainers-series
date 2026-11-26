---
id: 07.01.B.K5
tsc: 7
level: Basic
code: K5
title: "Embeddings and tokenisation: how text becomes numbers a model can learn from"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Embeddings and tokenisation: how text becomes numbers a model can learn from

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K5**


> **Framework text (verbatim):** "Embeddings and tokenisation."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 5 of 15

**One-line version:** Tokenisation decides what the model can see; embeddings decide what it can compare — and both are frozen choices you inherit when you fine-tune.

## What it is

Tokenisation is the step that cuts text into the units a model actually processes — words, word-fragments, characters, pixels or audio frames — and maps each unit to an integer. Embeddings turn those integers into vectors, lists of numbers positioned so that things used in similar ways sit close together. Together they are the model's entire interface with the world: nothing goes in and nothing comes out that has not passed through them.

## Deep expansion

### The concept

A neural network cannot multiply a word. It can only multiply numbers. So every generative system begins with a **vocabulary**: a fixed list of units, each with an index. Text is split into those units, the units are replaced by their indices, and those indices look up rows in a large table. Each row is an embedding — a vector, typically hundreds or thousands of numbers long.

The magic is in the geometry. Training moves those vectors so that "refund" ends up near "return", "Makan" near "eat", and "not good" pointing in a direction that is consistently opposite to "good". Once meaning is a position, arithmetic on meaning becomes possible: similarity is a distance, retrieval is a nearest-neighbour search, and the attention mechanism inside a transformer is a learned weighting over those positions.

Tokenisation is where the compromises live. Too fine (characters) and sequences become enormous and training is slow. Too coarse (whole words) and the vocabulary explodes, and any misspelling becomes an unknown token. The near-universal answer is **byte-pair encoding** or a close relative: start from characters, repeatedly merge the most frequent adjacent pair, and stop at a chosen vocabulary size. The result is chunks like `gener` + `ation`, which is why models handle new words gracefully and why they miscount letters.

### The sub-concepts

**Vocabulary size.** Typically tens of thousands to a couple of hundred thousand entries. Bigger compresses text better but costs memory in the output layer.

**Subword splitting.** Common words get one token; rare words get several. This is why "tokenise" and "tokenize" may split differently, and why a Singapore address can cost more tokens than a plain English sentence.

**The context window is counted in tokens, not words.** A rough English rule of thumb is three-quarters of a word per token, but code, Chinese, Malay and emoji all break that rule.

**Embeddings as a table.** The embedding layer is a lookup table learned during training. When people say "the model's embeddings", they mean the rows of that table.

**Standalone embedding models.** Separate models (the `sentence-transformers` family, and the embedding endpoints offered by the major providers) exist purely to turn text into vectors for search. They are trained differently from generative models and are usually smaller and cheaper.

**Multi-modal embeddings.** Images and audio get projected into the same space as text, which is what makes "search my photos by description" possible. The Intermediate level treats this properly.

### How it connects to the rest of the framework

`TSC7-Basic-K4` decides what text reaches the tokeniser; this bullet decides how it is represented. `TSC7-Basic-K6` (loss) is computed over token probabilities, so tokenisation shapes the number. `TSC6-Basic-K1` (retrieval-augmented generation) is embeddings used at query time rather than training time. `TSC7-Intermediate-K3` (multi-modal embeddings) is the next step up. Roughly half of TSC #6 is quietly this bullet applied.

### What is current as of November 2026

Two things have changed in practice. First, **tokenisation has become a cost and quality issue at the product level**: providers price per token, context windows are quoted in tokens, and multilingual gaps are largely tokenisation gaps — a sentence in Malay or Chinese often consumes noticeably more tokens than the same meaning in English, which is a fairness question as well as a billing one. Second, **embedding models are now a distinct product category**, with dedicated endpoints from the same vendors who sell current frontier models, plus strong open-weight options.

For a Basic class the useful framing is: you will almost never design a tokeniser. You will inherit one, and you need to know its consequences — context limits, cost, multilingual behaviour, and the fact that a model cannot see a character it never tokenised as a character.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"A token is a word."* It is a fragment. "Unbelievable" is often three tokens.
- *"Embeddings are a kind of search index."* They are vectors; a search index is one thing you can build on top of them.
- *"The model reads letters."* It reads token IDs. That is why character-level tasks (counting the r's in "strawberry") are unreliable.
- *"All embedding models are interchangeable."* Different models produce different geometries; vectors from one are meaningless to another.
- *"Tokenising is preprocessing I can skip."* It is the model's input format. Getting it wrong means the model was never trained on what you think.

## How a student should understand it

**Mental model:** a postal system. Tokenisation is the postcode — a fixed set of codes that determines how finely an address can be routed. Embeddings are the map: every address has coordinates, and nearness on the map means similarity in practice.

**Three things they can do after this bullet:**
1. Tokenise a sentence with a real tokeniser and count the tokens, then compare with the word count.
2. Explain why a context window "of 200,000 tokens" is not "200,000 words".
3. Build a five-line semantic similarity check between two sentences and interpret the score.

**Misconceptions to kill:** that tokens are words, that the model sees characters, and that embeddings from different models can be mixed.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The postal code.** Singapore addresses are fine-grained; a six-digit postcode routes mail precisely. A model's tokeniser is the postcode system: it decides the finest granularity available. If a word has no postcode, it gets delivered in pieces.

**The HDB estate map.** Every block has coordinates. Blocks built around the same MRT station sit close together on the map even if they look different. Embeddings are that map for meaning — and like any map, it reflects the surveyor's choices: which estates were mapped well, and which were left as blank space.

### Worked example with a real tool

Two cells. First, look at what the model actually sees:

```python
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("gpt2")
text = "Makan already? Let's go to Jurong East."
print(tok.tokenize(text))
print(len(tok.tokenize(text)), "tokens for", len(text.split()), "words")
```

Then compare meaning with vectors:

```python
from sentence_transformers import SentenceTransformer, util
m = SentenceTransformer("all-MiniLM-L6-v2")
a = m.encode("My order has not arrived")
b = m.encode("Where is my parcel?")
c = m.encode("The weather is hot today")
print(util.cos_sim(a, b).item(), util.cos_sim(a, c).item())
```

What to point at afterwards: the token list shows fragments, not words; the two similarity scores show that "not arrived" and "where is my parcel" land close together while "weather" does not. That is meaning as distance, in two numbers.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — ask the room to count the letter "r" in a word, then show a model getting it wrong. Ask why.
2. **State the objective** — by the end you can explain tokens, context limits and semantic similarity without hand-waving.
3. **Recall prior learning** — from TSC #6 they know RAG uses a vector database; now they see what is in it.
4. **Present the content** — vocabulary, BPE, embedding table, cosine similarity, token cost.
5. **Guide** — run both cells together and predict the token count before printing it.
6. **Elicit performance** — pairs tokenise one English and one Malay sentence and compare counts.
7. **Give feedback** — correct "tokens are words"; use the printed list as evidence.
8. **Transfer** — each learner estimates the token cost of a document they handle weekly.

## What the framework doesn't mention but trainers need to know

- **Tokenisation is a fairness surface.** Languages and dialects that tokenise inefficiently get less context, higher cost and worse performance for the same money. This is now a documented concern in multilingual deployment, and Singapore classrooms are multilingual.
- **You inherit, you do not choose.** For fine-tuning, the tokeniser is fixed by the base model. Changing it means retraining the embedding table.
- **Embedding dimension is not quality.** A 384-dimension model can outperform a 3,072-dimension one on your task; benchmark on your own data.
- **Cost arithmetic is a teachable skill.** Price per million tokens multiplied by average tokens per request is the whole back-of-envelope, and most learners have never done it.

## Watch out

- **Do not open with the maths of cosine similarity.** Show two scores first, formula later if at all.
- **Do not say "the model understands this sentence's meaning".** It has a position for it. That distinction is the whole bullet.
- **Do not mix embedding models in a demo.** Vectors from different models are not comparable, and a demo that does it teaches a broken habit.
- **The stale claim to retire:** "one token is roughly one word." In November 2026, with multilingual and code-heavy workloads, that estimate is wrong often enough to misprice a project.
