---
id: 01.01.B.K4
tsc: 1
level: Basic
code: K4
title: Where generative AI helps and where it does not
as_at: 2026-11-26
review_by: 2027-02-25
---

# Where generative AI helps and where it does not

> **TSC #1 Generative AI Principles and Applications · Basic · Knowledge K4**

> **Framework text (verbatim):** "Transformative potential of generative AI in various industries, including domains where generative AI could be used, and where it may not work."
>
> **TSC #1** Generative AI Principles and Applications · **Basic** · Knowledge · Bullet 4 of 13

**One-line version:** Generative AI is a multiplier on work that is language-shaped, draftable and checkable — and a liability on work that must be exact, accountable, fresh or irreversible.

## What it is

Every industry has the same four task types: produce text-shaped artefacts, reduce text-shaped artefacts, decide, and act. Generative AI transforms the first two almost everywhere and touches the third only in an advisory way. Knowing where it does not work is a professional skill, not a disclaimer. This bullet asks the learner to hold both halves at once: the transformation is real, and the boundary is specific.

## Deep expansion

### The concept

The framework asks for "transformative potential … and where it may not work". Trainers tend to teach the first half with enthusiasm and the second as a warning slide. They are the same skill: **matching task to tool**. The useful question is not "can it do this?" — it usually produces something — but "what does it cost me if the output is wrong, and how would I know?"

Five tests, in order. Run them and the answer is usually obvious in a minute:

1. **Is the task language-shaped?** Drafting, summarising, restructuring, translating, explaining, classifying by meaning. If the work is about words, images or code as artefacts, it is in scope.
2. **Is a good-enough draft useful?** The output is a draft by construction. Work where a competent human will read and revise gains enormously; work where the output is used unreviewed does not.
3. **Can a wrong answer be caught?** If verification is cheap — compare the source, check the figure, run the test — the risk is manageable. If the output is plausible and unverifiable, the tool is dangerous however good it looks.
4. **Does it require exactness or freshness?** Arithmetic, today's regulation, a contract clause, a dosage. The model's strengths are fluency and pattern, not precision and recency.
5. **May the data leave?** Personal data, client confidences, unpublished financials. If the answer is no, fit is settled before quality is discussed.

### The sub-concepts

**Where it helps, by the task not the industry.** Healthcare: drafting patient-education material, restructuring a protocol into a checklist. Legal: first-draft clause comparison, summarising discovery. Logistics: exception notices, translation of a customs query, carrier correspondence. Education: differentiating a worksheet for three ability levels, generating practice questions. Finance and HR: policy summaries, job descriptions, first-draft replies to routine enquiries. Public sector: plain-language rewrites of notices, Q&A preparation. In every case the transformation is **compression, restatement or variation** — never judgement.

**Where it does not work.** Four families, and learners should name one example from their own job for each. **Exact computation** — summing a column, reconciling a ledger, computing GST: use a formula or a script. **Fresh or authoritative facts** — today's COE prices, whether a clause is compliant with an Act as amended: the model has a cutoff and no obligation to be current. **Accountability-bearing decisions** — hiring, credit, medical, disciplinary: the model may inform, a named human decides and explains. **Deterministic process** — if the rule is "when a form is submitted, copy row three and send template B", an LLM is slower, costlier and can invent; code the rule.

**The 80/20 split.** Give it the boring 80% — first draft, summary, variation, table — and keep the judgement 20%: the decision, the tone call, the final check, the signature. Not a law, a habit that prevents both over-trust and refusal.

**The escalation ladder.** Where a task sits on this boundary is often a design choice. Deterministic code first; a single model call second; a fixed pipeline of calls third; an agent with tools only when the path is genuinely unknown. Most SME "AI projects" that fail started at the top of the ladder.

### How it connects to the rest of the framework

`TSC1-Basic-K1` gives the five purposes this bullet distributes across industries. `TSC1-Basic-K6` explains mechanically why the "does not work" column exists. `TSC1-Basic-K8` and `TSC1-Basic-A03` decide whether the data may be used at all. `TSC1-Basic-A05` is the governance check when a use case passes the fit test but affects people.

### What is current as of November 2026

- **The "cannot" column has shrunk unevenly.** Coding, structured extraction and document comparison improved sharply. Exact arithmetic in text, freshness and accountability did not. Trainers who retire the whole caveat because a demo impressed them over-promise; trainers who keep all of it under-serve.
- **Agentic use moved the boundary rather than removing it.** With tool access a model can search, read, fill and send. That extends scope into workflow and sharpens the limits — an action is harder to reverse than a sentence. The question changes from "is the draft good?" to "what may it do without asking?"
- **The biggest workplace use is transformation, not creation.** In most Singapore offices the value is summarising, restructuring and translating documents that already exist. A course that demonstrates only creative writing misrepresents where the hours are saved.
- **Regulated sectors now assume a human owner.** MAS guidance on credit decisions and the Model AI Governance Framework for Agentic AI both treat "the AI decided" as no answer at all.

### Common misconceptions

- *"It's clever, so it works for everything."* Cleverness in language is not competence in arithmetic, law or medicine. The failures are specific, which is good news: they can be taught.
- *"It's unreliable, so it's useless for serious work."* Serious work is mostly drafting, summarising and reviewing — exactly what it does well, with a human sign-off.
- *"A human check at the end makes any use case safe."* A check nobody has time, information or authority to perform is decoration. It has to be designed, not appended.
- *"Automating the whole task is the goal."* Automating the 80% and keeping the judgement is usually the better outcome, and the one that survives an audit.

## How a student should understand it

**Mental model:** the brilliant tutor who can explain anything, write anything, and never tires — but cannot sit the exam for you, cannot sign the certificate, and does not know what changed in the syllabus last week.

**Things they can do after this bullet:**
1. Run the five tests on a task from their job and give a verdict with a reason.
2. Name three tasks in their industry where it helps and three where it does not, naming the task rather than the industry.
3. Say what a workable human check looks like for a use case they would approve.

**Misconceptions to kill:** that it works everywhere, that it is useless for serious work, and that a human "in the loop" makes any use case safe.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The relief teacher who is excellent at explaining.** Give this teacher any topic and you get a clear, patient, well-structured explanation. Ask them to mark the PSLE paper and submit the results and they cannot — not because they are weak at the subject, but because the task needs a signature, a standard and an audit trail. Where it breaks: the relief teacher would at least say "I'm not qualified to mark this"; the model will happily produce a mark.

**The zi char stall with one wok.** One stall, one wok, a hundred dishes, fast and cheap. It will not do your accounts, and it will not tell you the dish is wrong for the customer. Order what the wok is good at, and taste before serving.

### Worked example with a real tool

One prompt that makes the boundary visible on one screen:

```text
Here are six tasks. For each, answer in this format:
TASK: <name> | VERDICT: good fit / bad fit | WHY: <10 words> | CHECK: <how a human verifies>

1. Draft a thank-you letter to a donor who gave $5,000.
2. Diagnose why a patient has been dizzy for three days.
3. Add up the 47 line items in this invoice.
4. Turn a 12-page annual report into a one-page staff briefing.
5. Tell me the current CPF contribution rate for a 62-year-old.
6. Write the first draft of a tender response against this specification.
```

What to point at afterwards: the model sorts 1, 4 and 6 correctly and reasons well about 2 and 3. Watch 5 — it will state a rate with total confidence. That is the demonstration: the model can explain its own limits beautifully and still walk straight through one. The lesson is not "the list is wrong"; it is that the learner's judgement is the control, not the model's self-report.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — Two headlines: "Our firm now uses AI to draft client emails" and "Firm fined over AI-generated advice". Which do they believe, and why?
2. **State the objective** — "You will look at any task in your job and say, with a reason, whether this tool helps and what check you would attach."
3. **Recall prior learning** — From K1: sort today's tasks into create / transform / analyse / converse / act.
4. **Present the content** — The five tests on one slide, then the 80/20 split.
5. **Guide** — Run the six-task prompt and debrief the CPF answer honestly.
6. **Elicit performance** — Each table lists four tasks from one member's job and runs the five tests.
7. **Give feedback** — Take the hardest cases. They are always "the draft goes to a client" or "the number goes into a report" — name the pattern.
8. **Transfer** — Each learner writes: "In my job I will use it for ___ and not for ___, because ___."

## What the framework doesn't mention but trainers need to know

- **The cost of a wrong answer is consequence × visibility × reversibility.** A wrong internal draft is cheap; a wrong letter to 4,000 policyholders is not, and the difference is not about model quality.
- **Verification cost is the real constraint.** If checking takes longer than doing it manually, the productivity gain is imaginary.
- **SMEs have no legal team and no policy.** Your learners may be the entire governance function. Give them a one-page rule they can apply alone.
- **The best first use case is boring.** Internal, reversible, text-heavy, with an obvious checker. The flashiest demo creates the worst first project.

## Watch out

- **Do not run an industry-tourism slide deck.** "AI in healthcare, AI in logistics" teaches nothing. One task, five tests, their own work.
- **Do not let the demo pick the use case.** The model is impressive on whatever you chose; the learner's job is different.
- **Do not present the "does not work" list as permanent.** It shrinks. Date it, and say which parts have moved.
- **The stale claim to retire:** "AI cannot do anything that requires accuracy." It does plenty that requires accuracy, with a check. The accurate claim is narrower: it cannot be *trusted* without one.
