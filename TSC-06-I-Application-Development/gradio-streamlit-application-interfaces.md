---
id: 06.02.I.A3
tsc: 6
level: Intermediate
code: A3
title: From notebook to interface: shipping a model behind Gradio or Streamlit
---

# From notebook to interface: shipping a model behind Gradio or Streamlit

> **TSC #6 Generative AI Application Development and Deployment · Intermediate · Ability A3**


> **Framework text (verbatim):** "Develop applications that integrate generative AI models via developer tools and cloud service offerings (e.g. Gradio and Stramlit interfaces)."
>
> **TSC #6** Generative AI Application Development and Deployment · **Intermediate** · Ability · Bullet 10 of 12

**One-line version:** Gradio and Streamlit turn a Python script into something a colleague can use — and the difference between a demo and an application is everything built around the model call.

## What it is

This is the ability to put a working interface in front of a model: pick a framework, wire an input control to a model call, handle the failure paths, keep the key out of the browser, and deploy it somewhere a named user can reach. The deliverable is a URL someone else can open and use without you present.

## Deep expansion

### The concept

Both tools do the same trick: they read a Python script and render a web app, so a data person can build an interface without a frontend engineer. The difference is what each is shaped for.

**Gradio** is built around a function: inputs in, outputs out, widgets generated from the type signatures. Chat interfaces, file uploads, image and audio I/O and shareable links are one decorator away — the fastest path to "let people try my model".

**Streamlit** is built around a script that reruns top to bottom on every interaction, with session state carrying what must persist. Layout, tables, charts, multi-page navigation and sidebar controls are stronger — the fastest path to "let people use this data tool that happens to call a model".

The choice follows the shape of the interaction, not capability: a single prompt-and-response demo is Gradio; a multi-step workflow with sidebars, filters and history is Streamlit.

The ability, though, is not the framework. It is knowing what a demo lacks: **secrets** (in `st.secrets` or the environment, never the repo), **error surfaces** (a timeout must appear as a sentence, not a stack trace), **cost and rate limits** (one user clicking forty times is a real bill), **persistence** (history that vanishes on refresh), **access control** (a public link is public), and **concurrency** (blocking model calls under load).

### The sub-concepts

**The function boundary.** In Gradio the handler function is the contract: parameters become inputs, return becomes output, and everything testable lives there — you can unit-test it without the UI.

**Session state.** In Streamlit, `st.session_state` is the only memory between reruns. Forgetting it produces the classic bug where chat history resets on every message.

**Streaming.** Both support token-by-token output, and it transforms perceived latency. It also complicates errors: the failure may arrive after half the answer is on screen.

**Deployment target.** Hugging Face Spaces and Streamlit Community Cloud are fine for internal demos; a container on your cloud is what you use when the app touches real data. The target determines the authentication story.

**Caching.** `st.cache_data` for expensive retrieval, so a rerun does not re-embed the same document.

**Environment parity.** The app runs where you deployed it. Pin versions — a floating framework or SDK version is the most common "it worked yesterday" failure.

### How it connects to the rest of the framework

`TSC6-Intermediate-K1` is the contract behind the call, `TSC6-Intermediate-K3` is where the app lands, and `TSC6-Intermediate-K7` must be inside the handler, not the UI. `TSC6-Basic-A1` supplies the prompt; `TSC6-Intermediate-A5` is what happens when the framework version conflicts with the environment. `TSC6-Basic-K2` (low-code) is the neighbouring skill — this is the code-first version.

### What is current as of November 2026

Both frameworks have become the default last mile for AI prototypes, and expectations have risen with them. Streaming, chat history and file upload are table stakes — a form with a submit button reads as dated. Deployment is one command, so a prototype can be live in minutes, which raises the bar for what should be live: "it was only a demo" no longer excuses an open endpoint. And the honest gap has moved to auth and data — the framework renders your interface, but it will not give you single sign-on, row-level permissions or an audit log.

### Common misconceptions

- *"If it runs locally, it's an app."* Local means one user, no auth, no concurrency, no monitoring.
- *"The framework handles security."* It handles rendering. Secrets, auth, rate limits and logging are yours.
- *"The share link is fine for now."* A public link to an endpoint with your key behind it is an open wallet.

## How a student should understand it

**Mental model:** the showflat versus a TOP unit. The showflat looks finished — the tap is there, the lights work, the view is real. There is no water in the pipe, no wiring certificate, no key handover.

**Three things they can do after this bullet:**
1. Build and run a two-control app that calls a model with the key read from secrets.
2. Handle three failures visibly: missing key, provider error, empty response.
3. Deploy it to a URL and state plainly what is still missing before real users.

**Misconceptions to kill:** local equals deployed, the framework handles security, and the share link is harmless.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**Showflat versus TOP.** A showflat is furnished, lit and convincing; a TOP unit has water, power, a fire certificate and a key. The gap is invisible in photographs and total in practice. Where it breaks: a showflat is built to deceive, while a prototype is honestly incomplete — the risk is that the audience forgets which one it is looking at.

**A pasar malam stall versus a shopfront.** The stall goes up in an afternoon, needs no lease, serves for a week, and everyone understands it is temporary. Put the same stall in a mall unit and it looks unfinished.

### Worked example with a real tool

Ask for the app, then run it. In Claude:

```
Write a Streamlit app for a tuition centre's FAQ assistant.

- A text area for the parent's question and a submit button.
- Call an OpenAI-compatible chat endpoint using base_url, api_key and
  model from st.secrets, with stream=True and st.write_stream.
- Keep the conversation in st.session_state so it survives a rerun.
- Wrap the call in try/except and show the provider's error in
  st.error, with a plain-English hint for 401, 429 and timeout.
- Show a token counter in the sidebar.
```

The shape of what comes back:

```python
import streamlit as st
from openai import OpenAI

st.title("Bright Minds — FAQ assistant")
client = OpenAI(api_key=st.secrets["api_key"], base_url=st.secrets["base_url"])
MODEL = st.secrets["model"]

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system",
         "content": "Answer only questions about courses, fees and schedules."}
    ]

for m in st.session_state.messages[1:]:
    st.chat_message(m["role"]).write(m["content"])

if q := st.chat_input("Ask about a course, fee or schedule"):
    st.session_state.messages.append({"role": "user", "content": q})
    st.chat_message("user").write(q)
    try:
        stream = client.chat.completions.create(
            model=MODEL, messages=st.session_state.messages, stream=True
        )
        answer = st.chat_message("assistant").write_stream(stream)
    except Exception as e:
        st.error(f"Could not reach the model: {e}")
        answer = None
    if answer:
        st.session_state.messages.append({"role": "assistant", "content": answer})
```

What to point at afterwards: run it, then delete the key from `secrets.toml` and run it again — the `st.error` branch is the difference between an app and a demo. Then look for what is still absent: no auth, anyone with the URL can spend your quota, and nothing logs who asked what. That list is the honest gap to production.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — two live URLs: one that handles an error gracefully, one that shows a stack trace.
2. **State the objective** — you will deploy a working interface with secrets handled and three failures surfaced.
3. **Recall prior learning** — they have a prompt and a model call working in a notebook.
4. **Present the content** — Gradio versus Streamlit, the function boundary, secrets, session state, deployment targets.
5. **Guide** — build the FAQ assistant together from the prompt above.
6. **Elicit performance** — each learner wraps their own use case in one interface and deploys it.
7. **Give feedback** — the common miss is the key in the code; the second is no session state, so history resets.
8. **Transfer** — they write the "what's missing before real users" list for their own app.

## What the framework doesn't mention but trainers need to know

- **The notebook is not the app.** Most learners arrive with a Colab cell full of hard-coded strings. The refactor into a handler with configuration is the actual work.
- **Auth is the production gate, not the model.** Prototypes die at the security review, not the quality review. Teach the list once: identity, permissions, logging, rate limit, retention.
- **Free tiers sleep.** A space that idles and takes forty seconds to wake is a bad first impression. Know the hosting behaviour before demoing to a client.
- **The `base_url` habit pays off.** Writing against an OpenAI-compatible base URL makes switching provider, or moving to an in-house endpoint, a config change.

## Watch out

- **Do not demo with a hard-coded key**, even a throwaway one. The room copies what it sees.
- **Do not present a share link as a deployment.** Say the word "public" out loud.
- **Do not let the framework become the lesson.** Ten minutes on widgets, the rest on secrets, errors, state and the production gap.
- **The stale claim to retire:** "you need a frontend developer to build an AI interface." In November 2026 you need a Python file and a deployment target — and a frontend developer for everything after the prototype.
