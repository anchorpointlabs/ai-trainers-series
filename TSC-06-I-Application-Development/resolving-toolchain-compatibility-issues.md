---
id: 06.02.I.A5
tsc: 6
level: Intermediate
code: A5
title: When it breaks outside the model: resolving toolchain compatibility issues
as_at: 2026-11-26
review_by: 2027-02-25
---

# When it breaks outside the model: resolving toolchain compatibility issues

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Ability A5**


> **Framework text (verbatim):** "Resolve compatibility issues with other software or systems (e.g., GitHub Copilot, CircleCI)."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Ability · Bullet 12 of 12

**One-line version:** The model is usually fine — it is the editor extension, the CI runner, the proxy or the SDK major version that is not, and the fix starts with "where exactly does it fail".

## What it is

This is the ability to diagnose and fix the failures that happen where generative AI tooling meets the rest of your stack: an IDE assistant that will not authenticate, a pipeline that cannot reach a provider, an SDK whose major version changed under a pinned dependency, an enterprise proxy intercepting TLS. The deliverable is a working configuration plus a written note of what the constraint was.

## Deep expansion

### The concept

Compatibility failures share a signature: **the same code works in one environment and not another**. That is the diagnostic lever. Instead of reading the code, you map the difference between the two environments — operating system, runtime version, network path, credentials, package versions, policy.

The surfaces a GenAI developer actually meets:

- **Credentials and scopes.** A GitHub token that works in the web UI but not for Copilot; a provider key valid for one project but not another; an OAuth scope granted for repository read but not for the workflow API.
- **Network path.** Corporate proxy, TLS interception, allowlist, VPN-only egress, region blocking. The single most common cause of "it works at home".
- **Runtime and package versions.** Python 3.9 versus 3.12, Node 18 versus 22, an SDK that jumped a major version and renamed a class, a pin that resolved differently in CI.
- **Editor and extension state.** An assistant extension that updated, lost its session, or conflicts with another extension's keybindings or language server.
- **CI runner environment.** No GPU, no outbound network by default, an image without the native library, secrets not exposed to forked pull requests, CRLF versus LF line endings.
- **Plan and quota limits.** A workspace plan that does not include the feature the code calls; a CI plan with a concurrency cap.

### The sub-concepts

**Isolate by environment.** Run the failing step in three places — your machine, a clean container, and CI. The pair that differs tells you which surface is involved.

**Read the real error.** Not the summary the extension shows, but the log file, the `--verbose` output, the CI step's raw stderr. Extension UIs routinely replace a specific error with "something went wrong".

**Pin and lock.** `==` in requirements, a committed lockfile, an explicit runtime version in CI config. Floating versions cause most "it worked yesterday" incidents.

**Check the deprecation calendar.** SDKs and model versions retire on published schedules. A 404 on a model name is usually a retirement, not a typo.

**Minimal reproduction.** Cut the pipeline to the one step that fails. A failing step with three environment variables and no cache is a bug report someone can act on; a failing forty-minute pipeline is a conversation.

**Least-privilege troubleshooting.** Add permissions one at a time so you learn which was needed. Granting everything works, teaches nothing, and fails the security review later.

**Windows-specific traps.** Path separators, CRLF, long path limits, and case sensitivity differences between a Windows laptop and a Linux runner. Training rooms here are full of Windows laptops deploying to Linux containers.

### How it connects to the rest of the framework

`TSC6-Intermediate-K1` explains why the seam fails, `TSC6-Intermediate-K3` is where most of these issues surface, and `TSC6-Intermediate-A1` is the sibling skill for model-side failures. `TSC6-Basic-K5` and `A4` are the Basic troubleshooting pair this grows from. At Advanced level, `TSC6-Advanced-K4` and `A6` automate the diagnosis with scripts.

### What is current as of November 2026

Toolchain compatibility has become a bigger share of the work, not a smaller one. Assistant tooling is embedded everywhere — editors, CI platforms, issue trackers and cloud consoles — each with its own auth model and its own way of failing quietly, so the number of integration points per developer has gone up. Protocols reduced one class of problem: MCP-standardised tool connections mean "this assistant cannot see that system" now has a common shape and a common fix. Version churn remains the top cause, because the major SDKs still ship breaking changes on a cadence shorter than most organisations' upgrade cycles.

### Common misconceptions

- *"It's a bug in the AI tool."* Usually it is a credential scope, a network path, or a version. The tool is the visible symptom.
- *"Reinstall and try again."* Reinstalling resolves extension state, one of six surfaces. When it does not work, people conclude the tool is broken.
- *"It works locally, so the code is fine."* Locally means your credentials, your proxy exceptions, your cached packages.

## How a student should understand it

**Mental model:** the three-pin plug. The appliance is fine; the socket standard differs. You need an adapter — and the adapter must be rated for the load, not just fit the hole.

**Three things they can do after this bullet:**
1. Take a failing tool and say which surface is implicated, from the evidence.
2. Produce a minimal reproduction that someone else can run.
3. Fix it with the narrowest credential or configuration change, and write down why.

**Misconceptions to kill:** it is the AI's fault, reinstall fixes everything, and admin rights are a solution.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The three-pin plug.** Correct appliance, wrong socket, and the adaptor must match the load. Where it breaks: a plug either fits or it does not, while a token can *partially* work — read access fine, write access denied — which is why scope problems take longer to spot than physical ones.

**Corppass versus SingPass.** Same person, different authorisation. You log in perfectly and still cannot perform the action, because the entity you are acting for has not granted the scope. That is exactly the GitHub token that reads code but cannot trigger a workflow.

### Worked example with a real tool

Give the model the raw error *and the environment*, and make it produce a diagnostic order rather than a guess. In Claude:

```
A GitHub Actions job fails only in CI, never locally.

npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
npm ERR! While resolving: app@1.0.0
npm ERR! Found: openai@5.2.1
npm ERR! Could not resolve dependency:
npm ERR! peer openai@"^6.0.0" from @myorg/ai-helpers@2.3.0

Local: Node 22, npm 10, lockfile committed. CI: Node 18, npm 9,
npm ci in a node:18 image.

Give me: the two most likely causes, one command to confirm each,
and the smallest fix.
```

What to point at afterwards: the error names the conflict — a peer dependency demanding major version 6 while 5.2.1 is installed — and the second half of the prompt is where learners usually fail, because they omit the environment. With it included the diagnosis is immediate; without it the model produces three plausible guesses. **The quality of the answer is the quality of the environment description**, and that is a habit worth teaching explicitly.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — "works on my machine, fails in CI", and how many have lost a day to it.
2. **State the objective** — you will locate a compatibility failure to one surface and fix it narrowly.
3. **Recall prior learning** — they know the four error families (A1) and deployment targets (K3).
4. **Present the content** — the six surfaces, isolate-by-environment, pin and lock, minimal reproduction.
5. **Guide** — work the CI failure together from the prompt above, then verify against the runner image.
6. **Elicit performance** — each learner brings a real failure and writes the surface plus the reproduction.
7. **Give feedback** — the common gap is a vague reproduction; push until it is one command.
8. **Transfer** — they add a "known constraints" note to their project README.

## What the framework doesn't mention but trainers need to know

- **Enterprise laptops are the real test environment.** Proxy, certificate interception, endpoint detection, restricted installs. A demo on a personal laptop teaches a workflow half the room cannot reproduce on Monday.
- **This is where most elapsed time goes, and it is invisible in plans.** Nobody estimates "three hours fighting the token scope". Say the number out loud so learners budget for it.
- **Write the fix down.** Every compatibility fix is a future five-minute answer if it is in the README, and a future lost afternoon if it is in someone's chat history.
- **CI has no memory.** Anything the pipeline depends on — a cached model file, a local config, an environment variable — must be declared. Works-locally failures are almost always undeclared dependencies.

## Watch out

- **Do not let the session become an install-fest.** Debugging one learner's machine for forty minutes teaches nothing to the other nineteen. Diagnose the pattern, hand out the fix.
- **Do not blame the vendor by default.** It is sometimes the vendor, and usually not. "The tool is broken" stops the diagnostic process.
- **Do not demo in an admin shell.** The room will try it at home and hit the permission wall.
- **The stale claim to retire:** "just reinstall it." In November 2026 the assistant is one component in a stack of credentials, proxies, runtimes and runners, and reinstalling touches one of six.
