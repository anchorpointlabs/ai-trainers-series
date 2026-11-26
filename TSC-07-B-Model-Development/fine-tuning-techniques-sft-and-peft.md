---
id: 07.01.B.K8
tsc: 7
level: Basic
code: K8
title: "Fine-tuning: turning a general model into one that fits your job"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Fine-tuning: turning a general model into one that fits your job

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K8**


> **Framework text (verbatim):** "Fine-tuning techniques (e.g., supervised fine-tuning, parameter-efficient fine-tuning, perform inference)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 8 of 15

**One-line version:** Fine-tuning does not teach a model new facts so much as narrow its behaviour — and parameter-efficient methods let you do that on one GPU for the price of a lunch.

## What it is

Fine-tuning takes a model that has already been trained on a very large corpus and continues training it on a smaller, targeted dataset. Supervised fine-tuning (SFT) uses pairs of input and desired output. Parameter-efficient fine-tuning (PEFT) freezes most of the model and trains a small number of added parameters instead — LoRA being the dominant method. The bullet ends with "perform inference" for a reason: a fine-tune that cannot be run cheaply is not finished.

## Deep expansion

### The concept

A base model has learned the shape of language, not your procedures. Fine-tuning shifts its behaviour: the tone it writes in, the structure it returns, the house style of your replies, the pattern of your ticket classifications. The shift is real but narrow. It is a nudge to a distribution, not a database insert.

**Full fine-tuning** updates every weight. It is the most capable option and the most expensive: you need memory for the weights, the gradients, the optimiser state and the activations, and you end up with a complete copy of the model per task. For a model of any real size this is out of reach of a normal team.

**PEFT** freezes the original weights and inserts small trainable ones. LoRA adds low-rank matrices to selected layers, so the number of trained parameters can be a fraction of a percent of the total. The base model stays on disk, unchanged; you save a small adapter file. Swap the adapter and you have swapped the behaviour.

**SFT data format** is the practical crux. Most tooling expects a conversation or an instruction-response pair, and the *loss is computed only on the response tokens* — you are teaching it what to say, not what to read. Getting the masking wrong is the most common silent failure in the whole workflow: the model trains happily and learns to reproduce the prompt.

### The sub-concepts

**Instruction tuning.** SFT on a broad mixture of instructions and answers, which is how a raw next-token model becomes something that follows requests.

**LoRA and QLoRA.** LoRA adds trainable low-rank matrices; QLoRA additionally loads the frozen base in 4-bit precision so a large model fits on a single GPU. Rank and alpha are the two settings you will actually touch.

**Learning rate and epochs.** PEFT tolerates a higher learning rate than full fine-tuning, and needs few epochs. Three epochs on a small set is a common starting point; more often memorises.

**Catastrophic forgetting.** Train narrowly for too long and the model loses general ability — it becomes excellent at your task and worse at everything else. Mixing in a little general data is the usual mitigation.

**Inference.** Running the fine-tuned model. With PEFT this means loading the base model plus the adapter; with a hosted service it means calling your tuned endpoint. Quantised inference is normal here.

**When not to fine-tune.** If the task is knowledge, use retrieval. If the task is format and tone, fine-tune. If you cannot describe the desired output consistently, you cannot build a dataset for it.

### How it connects to the rest of the framework

`TSC7-Basic-K4` produces the data; `TSC7-Basic-K9` says what format it should be in. `TSC7-Basic-K7` (optimisation) sets the learning rate and schedule. `TSC6-Basic-K1` (RAG) is the alternative you should rule out first. `TSC7-Intermediate-K10` covers continuous pre-training, which is the heavier sibling. `TSC7-Basic-A2` (implementing an existing architecture) is the step before this one.

### What is current as of November 2026

PEFT is now the default, not the budget option. Almost every serious open-weight adaptation — a Llama, Qwen, Mistral or SEA-LION variant tuned on domain data — is a LoRA adapter on a frozen base, because it is cheap, reversible and easy to serve several adapters from one loaded model. Hosted fine-tuning endpoints from the major providers have made the fully-managed version routine, and most now expose a supervised fine-tuning job with a JSONL upload and a trained model ID.

The honest shift for a Basic class: **fine-tuning is no longer the hard part; dataset construction is.** Tooling has absorbed the engineering. What remains scarce is a few hundred genuinely well-written examples that consistently demonstrate the behaviour you want, with the failures documented.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"Fine-tuning teaches the model my documents."* It nudges behaviour. For facts, retrieve them at query time.
- *"More epochs means better."* Past a point, more epochs means memorisation and forgetting.
- *"LoRA is a cheap approximation, full fine-tuning is the real thing."* For most adaptation tasks LoRA matches full fine-tuning, at a fraction of the cost.
- *"A low training loss means the model is good."* It means the model reproduces your dataset. If the dataset is thin, so is the model.
- *"Fine-tuning fixes hallucination."* It can reduce it in a narrow domain and increase confidence everywhere else.

## How a student should understand it

**Mental model:** sending an experienced driver on a two-day course for your specific delivery route. They already know how to drive. You are not teaching driving; you are teaching your route, your gates and your regular customers.

**Three things they can do after this bullet:**
1. Decide between prompting, retrieval and fine-tuning for a stated task, with a reason.
2. Write a twenty-row SFT dataset in the expected format and explain which tokens the loss covers.
3. Run a LoRA fine-tune and then load the adapter for inference.

**Misconceptions to kill:** that fine-tuning inserts knowledge, that full fine-tuning is the serious option, and that loss is quality.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The driving-school car with sticky notes.** Full fine-tuning repaints the whole car. LoRA sticks a small laminated card on the dashboard that says "for this route, turn left at the flyover". The car is unchanged; the behaviour is not. Remove the card and the car is exactly as it was.

**The new hire who has read everything.** A base model is a graduate with encyclopaedic reading and no office habits. SFT is the first week of shadowing: here is how we write to clients, here is our ticket template. Two weeks of shadowing does not make them an expert in your business — it makes them usable.

### Worked example with a real tool

A LoRA fine-tune, in Colab, on a tiny dataset. This is close to the real recipe:

```python
from datasets import load_dataset
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")

cfg = LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05,
                 target_modules=["q_proj", "v_proj"], task_type="CAUSAL_LM")
model = get_peft_model(model, cfg)
model.print_trainable_parameters()   # expect a very small percentage
```

What to point at afterwards: the trainable-parameter line. It is usually well under one percent. Ask the room what that implies about cost, then ask what it implies about capability — the answer is "it changes habits, not knowledge".

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show a generic model answering a company email badly, then the same model after tuning. Ask what changed.
2. **State the objective** — by the end you can choose between prompting, RAG and fine-tuning, and run a LoRA job.
3. **Recall prior learning** — from TSC #6 they built RAG; ask when retrieval is the wrong tool.
4. **Present the content** — SFT, PEFT, LoRA/QLoRA, data format, when not to tune.
5. **Guide** — walk the config together, explaining rank and alpha in one sentence each.
6. **Elicit performance** — pairs write ten instruction-response pairs for a task they own, in the exact format.
7. **Give feedback** — review the datasets; the usual fault is inconsistent answers, which teaches the model to be inconsistent.
8. **Transfer** — each learner writes the one behaviour in their team that is worth a dataset.

## What the framework doesn't mention but trainers need to know

- **Loss masking on the prompt is decisive.** If the model is trained on prompt tokens, it learns to generate prompts. Check the data collator, not the loss curve.
- **Dataset quality beats size, dramatically.** A few hundred consistent, well-written examples outperform tens of thousands of scraped ones. Budget your time accordingly.
- **Adapters are a deployment win.** One base model, many adapters, swapped per request. This is an architectural advantage, not just a cost saving.
- **Evaluate before and after on the same held-out set.** Fine-tuning regularly makes one behaviour better and another worse, and only a paired comparison shows it.

## Watch out

- **Do not demo fine-tuning as a way to add facts.** It is the single most common mis-selling of the technique, and it leads teams to build the wrong thing.
- **Do not use a giant dataset in a Basic demo.** Fifty clean rows teach more than fifty thousand messy ones, and they train in minutes.
- **Do not skip the before-and-after comparison.** A model that "seems better" is not evidence.
- **The stale claim to retire:** "fine-tuning needs a cluster." In November 2026, a LoRA on a small open model runs on a free or single consumer GPU, and managed endpoints do the rest.
