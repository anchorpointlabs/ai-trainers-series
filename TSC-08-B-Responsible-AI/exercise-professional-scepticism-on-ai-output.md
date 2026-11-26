---
id: 08.01.B.A6
tsc: 8
level: Basic
code: A6
title: Exercise professional scepticism on AI output
---

# Exercise professional scepticism on AI output

> **TSC #8 Responsible AI and Generative AI Practices · Basic · Ability A6**

> **Framework text (verbatim):** "Exercise professional scepticism to exercise sound judgement on generative AI output."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Basic** · Ability · Bullet 10 of 10

**One-line version:** Treat every output as a claim from a persuasive stranger: useful, probably right, and unverified until you have opened the source yourself.

## What it is

Professional scepticism is the trained habit of not accepting a claim at face value — questioning it, checking it against independent evidence, and treating generated output as a draft until verified. It is the same discipline auditors apply to a client's numbers, applied to text that arrives in confident prose.

## Deep expansion

### The concept

The phrase is borrowed from audit, and the borrowing is instructive. An auditor does not distrust the client; the auditor *verifies* the client, because the cost of an undetected error is borne by someone who trusted the report. Professional scepticism is not cynicism — it is a duty owed to whoever relies on your work.

Generative AI makes that duty harder in a specific way: the output is engineered to read well. Grammar, structure, confidence and tone are all reliable; the facts are not. Human readers take fluency as a proxy for competence, so the better the model gets at writing, the more the reviewer's guard drops. That is why this bullet exists as an *ability* and not a knowledge point — knowing that models hallucinate does not stop anyone trusting one.

The other half is proportion. Scepticism applied to everything is paralysis. The skill is triage: what will this claim be used for, who is harmed if it is wrong, and what is the cheapest check that would catch the error before it does damage.

### The sub-concepts

**The three-way match.** Borrow the invoice clerk's discipline: a payment needs a purchase order, a delivery order and an invoice that agree. A generated claim needs the same — the claim, an independent source, and your own recomputation or reading. Two of three is a draft; three of three is verified. This single habit accounts for most of the practical benefit of the bullet.

**Verify the source, not the citation.** A model that supplies references can supply references that do not exist, or exist and say something else. The check is: open the link, search the quoted phrase inside the document, confirm the number appears in the context claimed. If the source cannot be reached, the claim is unverified regardless of how plausible the summary reads.

**Recompute anything numeric.** Models are unreliable arithmetic engines when numbers are embedded in prose, and the error is invisible because the sentence still reads correctly. Any figure that will appear in a report, a quotation or a decision gets recomputed — in a spreadsheet, not in the same chat.

**Read the retrieved context, if there is any.** Retrieval-augmented systems reduce hallucination but do not remove it: retrieval can pull the wrong document, the document can be outdated, and the model can stitch two facts into a false synthesis. The check is to read the chunks the answer was built from, not the answer.

**Ask for the counter-case.** Sycophancy means the model will usually agree with your framing. The deliberate counter is to ask what evidence would make the recommendation wrong, or to argue the opposite position. A claim that survives its own best objection is worth more than one that was never tested.

**Use a second, independent path.** A different model, a search engine, a colleague, a textbook — independence is what matters, not sophistication. Asking the same model to check itself is the weakest version of this and the one people do most.

**Recognise automation bias in yourself.** The tell is speed: if you read the output and felt reassured before you had a reason, that is the bias, not the evidence. The distillation's remedy is structural — limit queue speed, show uncertainty, and drop deliberate known-error cases into review queues to see whether anyone catches them.

**Document the check.** A one-line note — what was verified, against what, by whom, when — turns scepticism from a personal virtue into an organisational control. It is also what you produce when someone asks, after the fact, whether anyone checked.

**Know when not to check.** Drafting an agenda, brainstorming names, reformatting a table: the consequence of error is trivial and the check costs more than the mistake. Say so explicitly, so that scepticism is spent where it buys something.

### How it connects to the rest of the framework

`TSC8-Basic-K4` names the failure modes — hallucination, sycophancy, automation bias — and this bullet is the defence. `TSC8-Basic-A1` decides what to do with the output once verified; `TSC8-Basic-A4` encodes the verification duty in the team guideline; `TSC8-Basic-K3` and `TSC8-Basic-A5` cover the inbound side — what may go into the tool in the first place. `TSC1-Basic-K06`, on the limits of the technology, is the underlying explanation for why this habit is permanent rather than a phase.

### What is current as of November 2026

Models have become better at citing and at saying "I'm not certain", which is genuinely useful and slightly dangerous: the citation format is now convincing enough that readers skip the click. Systems built on OpenAI's GPT-6 generation, Anthropic's Claude 5.5, Google's Gemini 3.1 Pro and Gemini 4 Argon increasingly attach sources and reasoning summaries — treat those as *navigation aids*, not as verification. The source still has to be opened.

The other shift is agentic action. When an assistant drafts, the worst case is a wrong paragraph; when it acts, the worst case is a wrong transaction. Scepticism about output becomes scepticism about *actions*: require confirmation before anything irreversible, and read the plan before approving it.

### Common misconceptions

- *"It gave a source, so it's verified."* Citations are text too. A fabricated reference has the same format as a real one.
- *"I asked it to double-check and it said it was right."* Self-review by the same model is the least independent check available.
- *"Scepticism means not using AI."* It means using it and verifying the parts that matter.
- *"Temperature zero makes it factual."* It makes the most probable token certain, not the statement true.
- *"Checking every output is the professional standard."* Proportion is the standard: verify what carries consequence.

## How a student should understand it

**Mental model:** the invoice clerk's three-way match. The claim, an independent source, and your own recomputation have to agree before anything is paid. Two out of three is a query, not a payment.

**Things they can do after this bullet:**
1. Run the three-way match on a generated claim about their own domain in under five minutes.
2. Recompute a number in a spreadsheet rather than accepting the prose version.
3. Say which of their AI uses deserve verification and which do not, and why.

**Misconceptions to kill:** that a citation is evidence; that the model can verify itself; that scepticism is the same as refusal.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The fishmonger's check.** A good fishmonger does not read the label; they look at the gills, press the flesh, smell it. Three cheap independent signals, ten seconds. Verification is a habit of the senses, built by repetition, not a certificate. Where it breaks: spoiled fish announces itself to an experienced handler, while a fluent false claim looks identical to a true one — so the AI version requires deliberate checks rather than trained intuition.

**The invoice clerk's three-way match.** As above. Where it breaks: purchase orders and invoices are structured documents that either match or do not; prose claims require judgement about what "matching" means.

### Worked example with a real tool

Give the room a claim that is checkable and probably wrong:

```
You told me: "Singapore has 500 public libraries." Before I repeat this
in a report, walk me through how I should verify it: what is the
authoritative source, what exact figure would I look for, and what would
make the claim false rather than merely out of date?
```

What to point at afterwards: the model will usually produce a sensible verification route (the National Library Board's published list of libraries), which is the useful part — and it may still restate a number as if it knew. Point at that: the model is good at telling you *how* to check and unreliable at *being* checked. Then have learners actually open the source and correct the claim in the room.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — read a confident paragraph containing one planted falsehood. Ask the room to mark what they would sign their name to.
2. **State the objective** — verify a generated claim using three independent signals and record the check in one line.
3. **Recall prior learning** — the failure modes from `TSC8-Basic-K4`; today you build the defence against them.
4. **Present the content** — three-way match, source verification, recomputation, retrieved context, counter-case, independent second path, automation bias, documentation, proportionality.
5. **Guide** — run the library-claim example together, including actually opening the source.
6. **Elicit performance** — pairs take one claim from their own domain, verify it, and write the one-line record; one pair deliberately gets an unverifiable claim and must report it as such.
7. **Give feedback** — mark for independence: a check against the same model or the same website it cited does not count.
8. **Transfer** — each learner names the one output in their workflow that will now always be verified, and one that will not.

## What the framework doesn't mention but trainers need to know

- **Verification must be cheaper than the error.** If the check takes longer than fixing the mistake, nobody does it. Design checks that cost seconds: one saved source, one spreadsheet column, one colleague's glance.
- **The reviewer's attention is the scarce resource.** Automation bias is a workload problem as much as a character flaw; a team clearing 400 items an hour cannot exercise scepticism no matter how well trained.
- **Self-review is the default failure.** Learners will ask the model to check itself because it is frictionless. Name that as the weakest option in the room.
- **Scepticism needs a place to go.** If a learner finds an error and there is no route to report it, the habit dies after two attempts. Pair this bullet with an escalation line in the guideline.
- **Performance pressure erodes it fastest.** Under deadline, verification is the first step dropped. Teach the triage explicitly so that the drop is a decision rather than a slide.

## Watch out

- **Do not turn the room into cynics.** End on the controls and the triage, not on "you can't trust anything".
- **Do not claim a specific error or hallucination rate.** It varies by model, task and date; say "frequent on specifics, rarer on common knowledge".
- **Do not demo verification you have not done yourself.** If the trainer's example turns out to be right, the lesson collapses.
- **The stale claim to retire:** "newer models don't hallucinate." They hallucinate less often on the questions trainers like to demo, and just as readily on the ones that matter.
