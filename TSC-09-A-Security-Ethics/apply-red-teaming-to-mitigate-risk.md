---
id: 09.03.A.A4
tsc: 9
level: Advanced
code: A4
title: Apply red teaming to mitigate risk
---

# Apply red teaming to mitigate risk

> **TSC #9 Generative AI Models — Technical Aspects of Security and Ethics · Advanced · Ability A4**

> **Framework text (verbatim):** "Apply red teaming to identify and mitigate security risks in AI systems."
>
> **TSC #9** Generative AI Models — Technical Aspects of Security and Ethics · **Advanced** · Ability · Bullet 10 of 12

**One-line version:** A red-team finding is not closed when it is written up — it is closed when the fix is in, the fix has been attacked again, and the attack now lives in the permanent test set.

## What it is

This ability is the second half of red teaming. K4 finds weaknesses; A4 converts each finding into a mitigation, verifies it, and makes it permanent. The loop is: reproduce, root-cause, fix at the right layer, retest, add a regression case, record the residual, and tell the owner.

## Deep expansion

### The concept

Red teaming produces findings faster than most teams can fix them, and that asymmetry is where risk accumulates. The classic failure is a report that lists twelve weaknesses, three of which get fixed, and no record of the nine that were accepted by nobody in particular.

Applying red teaming therefore means treating each finding as a work item with a lifecycle:

1. **Reproduce and minimise.** Strip the attack to its shortest working form. The minimal version is what gets fixed and what gets tested; the full version is what gets presented.
2. **Root-cause by layer.** Ask what would have had to be true for the attack to fail. Different answers imply different fixes:
   - *Prompt layer* — the system prompt contains a rule that the model can be talked out of. Real cause: a security rule in prose.
   - *Permission layer* — the tool could do more than the task required. Real cause: over-broad agency.
   - *Identity layer* — the tool took a user identifier from the model's argument rather than the session. Real cause: authentication delegated to the model.
   - *Data layer* — untrusted content entered the context without marking. Real cause: no separation between instruction and data.
   - *Output layer* — model text was rendered or executed. Real cause: trusting generated text.
3. **Fix at the layer that holds.** Deterministic first. If the failure required an unauthorised action, the fix is a permission, a schema or a human gate — not a stronger sentence in the prompt.
4. **Retest the class, not the case.** The attacker's specific string is one member of a family; test variations in language, encoding, framing and length.
5. **Add to the permanent suite.** A regression case with the expected result, in the class taxonomy A1 maintains.
6. **Record the residual and the owner.** If the fix only reduces likelihood, say by how much, and who accepted the remainder.

### The sub-concepts

**Mitigation beats remediation.** Removal of the capability is stronger than blocking an input. If the feature does not need to send email, removing the tool ends the finding permanently; a filter ends it until the next encoding.

**Defence in depth, deliberately placed.** Expect the fix to be bypassed and add a second control at a different layer — the approval gate behind the classifier, the output sanitiser behind the model.

**Severity before effort.** Rate each finding on impact and reachability: who can trigger it, from where, and what it exposes or changes. Ten low-reach findings do not outrank one that leaks other users' records.

**Verification is adversarial.** The person who reported the finding should verify the fix; the person who wrote the fix should not be the only one who believes it works.

**Residual risk needs a signature.** "Mitigated" is a claim about degree. Write the number, the date, and the name.

### How it connects to the rest of the framework

K4 supplies the finding; this bullet closes it. A1 stores the regression case. K3 receives the guardrail refinements. K5 records the residual. A6 decides which findings must block a release and which can ship with a documented acceptance. At Intermediate level, `09.02.I.A1` covers developing mitigation strategies, and `09.02.I.A2` covers implementing defences against prompt attacks.

### What is current as of November 2026

- **Most fixes now land outside the prompt.** Identity binding to the session, narrow single-purpose tools, structured output, and approval gates for state-changing calls are the fixes that survive; prompt hardening is understood as a partial control.
- **Fix verification is a test problem.** Continuous attack suites in the pipeline are what turn "we fixed it" into "we know it still holds on this build".
- **Model upgrades reopen findings.** A finding closed against one model version may reopen against the next, which is why the regression suite is pinned to versions rather than to dates.
- **Disclosure expectations are rising.** Regulators and customers increasingly expect structured incident and vulnerability handling, not a quietly patched endpoint.

### Common misconceptions

- *"Fixed in the prompt."* You changed a preference, not a boundary; treat it as one layer among several.
- *"We documented it, so it is managed."* Documentation without an owner and a date is a note to nobody.
- *"The red team will retest it."* Unless the retest is scheduled and the class is covered, nobody will.
- *"Low severity, so ignore."* Low severity at high reach compounds; rate reachability explicitly.

## How a student should understand it

**Mental model:** an aircraft incident investigation that ends with a modification, a check in the manual, and a note in the training syllabus — not with a report on a shelf.

**Things they can do after this bullet:**
1. Take a finding and name the layer where the real cause sits.
2. Write a fix that a developer could implement, plus the two tests that prove it.
3. State the residual risk and who accepted it.

**Misconceptions to kill:** that a prompt change is a security fix, that documentation equals mitigation, and that a single retest closes a class.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The lift maintenance regime.** A fault is logged, the cause is found, the part is replaced, the lift is load-tested, and the inspection record is updated. Nobody accepts "we told the technician to be more careful" as a repair. Where it breaks: a lift fails in known ways, while an AI system's failure modes are open-ended, so the record is a growing class list rather than a fixed schedule.

**The MOM accident investigation.** The report is not the deliverable; the corrective action with a deadline and an owner is. Inspectors return to check it happened.

### Worked example with a real tool

```
You are the security engineer closing a red-team finding.

Finding: when asked in Malay, the assistant translates its instructions and reveals
the full system prompt, including the internal escalation thresholds.

Produce:
1. The root cause, stated at the correct layer (prompt, permission, identity, data
   or output) — and why the layer you chose is the real one.
2. Two candidate fixes: one deterministic, one probabilistic. Say which you would
   ship first and why.
3. The retest plan — five variations that must all fail to extract the prompt
   (vary language, encoding, framing and turn count).
4. The regression case to add, in one sentence, with its expected result.
5. The residual risk statement and the role that signs it.
```

What to point at afterwards: step two. Learners usually reach for a multilingual classifier; the deterministic fix is to stop putting confidential content in the system prompt at all, because the prompt is readable by anyone who can make the model talk. That reframing — "the secret should not be in the context" — is the transferable lesson, and it applies to keys, thresholds and internal rules alike.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — the same prompt-extraction attack succeeding in three languages.
2. **State the objective** — close one finding end to end, with tests and a residual statement.
3. **Recall prior learning** — how their team handles a production bug: report, fix, verify, prevent.
4. **Present the content** — the seven-step loop and the layer diagnosis.
5. **Guide** — diagnose the layer for the Malay case together.
6. **Elicit performance** — pairs write the deterministic fix and the retest variations.
7. **Give feedback** — check whether the retest attacks the class or only the case.
8. **Transfer** — each learner runs the loop on a finding from their own system.

## What the framework doesn't mention but trainers need to know

- **Fixes have costs, and someone must accept them.** Narrowing a tool may break a legitimate workflow; that trade belongs to the product owner, in writing.
- **Some findings should block a release and some should not.** Agree the rule before the red team reports, or every finding becomes an argument.
- **Reopened findings are normal.** A closed finding that reopens after a model upgrade is evidence the suite works, not evidence the team failed.
- **The register is the memory.** Findings, fixes, retests and residuals in one place is what turns individual diligence into organisational learning.
- **Time matters more than severity alone.** A live exfiltration path in production outranks a theoretical one in a staging build, whatever the impact estimate says.

## Watch out

- **Do not accept "we will monitor it" as a mitigation** for a state-changing action; monitoring detects, it does not prevent.
- **Do not let the fix author verify alone.** Independence is the point of the second look.
- **Do not close a finding without the regression case.** Otherwise the same attack returns with the next release.
- **The stale claim to retire:** "prompt injection is fixed by better prompting." As of November 2026 the fixes that persist are architectural — identity in code, narrow tools, approval gates, constrained output.
