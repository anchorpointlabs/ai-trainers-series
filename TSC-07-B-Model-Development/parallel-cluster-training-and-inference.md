---
id: 07.01.B.K10
tsc: 7
level: Basic
code: K10
title: "Parallel training and inference: why one GPU is never enough"
as_at: 2026-11-26
review_by: 2027-02-25
---

# Parallel training and inference: why one GPU is never enough

> **TSC #7 Generative AI Model Development and Fine Tuning · Basic · Knowledge K10**


> **Framework text (verbatim):** "Parallel cluster training and inference."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Basic** · Knowledge · Bullet 10 of 15

**One-line version:** When the model or the data outgrows one accelerator, you split the work — and the way you split it decides whether you get a speed-up or a queue of waiting machines.

## What it is

Parallel training is the practice of spreading one training job across several GPUs or machines so that it finishes faster, or fits at all. Parallel inference is the same idea applied at serving time: splitting a model across devices, or serving many requests at once, so that responses arrive quickly under load. The framework puts both under one bullet because they share the same underlying problem — moving numbers between accelerators is expensive, and every strategy is a trade against that cost.

## Deep expansion

### The concept

There are two reasons to go parallel. **The model does not fit**: a set of weights plus gradients plus optimiser state can exceed a single device's memory by a wide margin. **The job is too slow**: even when it fits, one device may take weeks.

Four strategies cover almost everything:

**Data parallelism.** Copy the model to every device, give each device a different slice of the batch, and average the gradients after each step. Simple, effective, and the default. It fails when the model itself does not fit.

**Tensor parallelism.** Split individual layers — a weight matrix cut into columns — across devices. Each device computes part of every layer and they exchange partial results constantly. Works for very large layers, but the communication is heavy, so it wants fast links inside one machine.

**Pipeline parallelism.** Put different layers on different devices and pass activations along the chain. Communication is lighter, but the pipeline has bubbles while it fills and drains, so utilisation is never perfect.

**Sharding (ZeRO, FSDP).** Keep the model replicated logically but split the weights, gradients and optimiser state across devices, gathering each layer only when it is needed. This is what makes large-model fine-tuning feasible on ordinary clusters, and it is the technique most teams actually use.

### The sub-concepts

**Collective communication.** All-reduce, all-gather, broadcast. The vocabulary of "devices agreeing on a number", and the reason interconnect speed matters more than raw compute at scale.

**Global versus local batch size.** Four devices with a batch of eight each is a global batch of 32. The learning rate usually has to move with it.

**Gradient accumulation.** Simulate a larger batch on one device by summing gradients over several mini-batches before stepping. The poor learner's data parallelism, and genuinely useful.

**Continuous batching (inference).** Rather than waiting for a full batch, the server admits new requests as slots free up. This is the single biggest throughput win in modern serving, and it is what TGI and vLLM are built around.

**Quantised and sharded inference.** Serve a large model across several devices, in reduced precision, with the KV cache managed carefully — because at inference the cache, not the weights, often becomes the memory problem.

### How it connects to the rest of the framework

`TSC7-Basic-K7` sets the batch size this bullet multiplies. `TSC7-Basic-K8` (fine-tuning) is where most learners first meet `accelerate` or `torchrun`. `TSC7-Intermediate-K2` covers hardware acceleration and cloud platforms properly. `TSC7-Advanced-A3` (optimising complex models for performance and efficiency) is the professional version. And `TSC6-Advanced-A2` covers serving infrastructure — TGI and vLLM — from the deployment side.

### What is current as of November 2026

The tooling has matured to the point where **most practitioners never write a distributed training loop**. `accelerate`, `torchrun` and the `Trainer`'s built-in FSDP support handle sharding, and managed platforms sell multi-node jobs by the hour. What remains genuinely difficult is the economics: interconnect bandwidth, the cost of idle devices during a pipeline bubble, and the fact that a badly configured multi-node job can be slower than a single-device one.

On the inference side, the shift is decisive. Serving a frontier-scale open model now means a dedicated inference engine with paged attention and continuous batching, not a naive loop over requests. Teams that skip this step discover that their model is fine and their throughput is not.

### Common misconceptions

- *"More GPUs means proportionally faster."* Communication overhead means eight devices rarely deliver eight times the speed.
- *"Data parallelism and sharding are the same thing."* Data parallelism replicates the model; sharding splits it.
- *"Parallelism is only for pre-training."* Fine-tuning large models and serving them both depend on it.
- *"Batch size is a per-device setting."* The effective batch is the global one, and the learning rate follows it.
- *"Inference is cheap because it is one forward pass."* Memory bandwidth and the KV cache dominate, and batching changes everything.

## How a student should understand it

**Mental model:** a hawker centre at lunch. One stall with one cook has a queue round the block. You can add cooks to the same stall (data parallel), split the dishes between stalls (pipeline), or have each stall cook part of every dish (tensor parallel) — and the last one only works if the stalls are close enough to pass plates quickly.

**Three things they can do after this bullet:**
1. Name the four strategies and the situation each one solves.
2. Explain the difference between local and global batch size, and why the learning rate changes.
3. Read a serving benchmark and say whether the bottleneck is compute, memory or batching.

**Misconceptions to kill:** that parallelism scales linearly, that sharding is the same as replication, and that inference needs no engineering.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The buffet line.** One server and a long queue. Add servers at the same counter and throughput rises until they start bumping into each other — that is the communication cost. Give each server a different dish and the queue moves, but a slow dish still stalls its station: that is the pipeline bubble.

**The MRT versus one bus.** A bus carries everyone in one vehicle and is cheap. An MRT train is many carriages, each carrying part of the load, and it only works because the track and signalling are fast enough to keep the carriages coordinated. Parallel training is the MRT: enormous throughput, entirely dependent on the infrastructure between the carriages.

### Worked example with a real tool

Show the learner that the multi-GPU run is a command, not a rewrite. On a machine with two GPUs:

```bash
accelerate config          # answer: multi-GPU, 2 processes, bf16
accelerate launch train.py # same script, now on both devices
```

and inside `train.py`, the only change is that the batch size is per device:

```python
TrainingArguments(per_device_train_batch_size=4, ...)  # x2 devices = 8 global
```

What to point at afterwards: the log line that reports the number of processes, and the step time before and after. Then ask what would happen with four devices and the same per-device batch — the global batch doubles, and unless the learning rate is adjusted, the run behaves differently.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — put a single-GPU time estimate on screen next to a deadline that is one week earlier.
2. **State the objective** — by the end you can name the four strategies, pick one for a scenario, and explain the batch-size consequence.
3. **Recall prior learning** — from K7 they set batch size; now it becomes global.
4. **Present the content** — data, tensor, pipeline, sharding; then inference batching.
5. **Guide** — walk through `accelerate config` on screen, reading each prompt aloud.
6. **Elicit performance** — give four scenarios (model too big, data too big, low latency, high throughput) and ask for a strategy each.
7. **Give feedback** — correct "just add GPUs"; use the buffet analogy to explain the ceiling.
8. **Transfer** — each learner notes whether their organisation has ever run a multi-device job, and what it cost.

## What the framework doesn't mention but trainers need to know

- **Memory, not compute, is usually the wall.** Most out-of-memory failures are the optimiser state or activations, which is why sharding and gradient checkpointing matter more than FLOPs.
- **Interconnect quality decides the ceiling.** Two devices on one board communicate far faster than two machines in a rack. Do not promise linear scaling across nodes.
- **Queue time is part of the cost.** A cloud cluster bills for the wait as well as the work. Spot instances and checkpointing are basic survival skills.
- **The KV cache is the inference bottleneck.** Long contexts multiply it. This is why serving costs scale with conversation length, not just request count.

## Watch out

- **Do not demo a multi-node job in a Basic class.** Two GPUs on one machine is the honest demonstration; the rest is a diagram.
- **Do not promise linear speed-up.** Learners remember the claim, not the caveat.
- **Do not conflate training parallelism with serving parallelism.** The strategies overlap in name and differ in bottleneck.
- **The stale claim to retire:** "you need a cluster to fine-tune." In November 2026 a small LoRA fits on one consumer GPU; clusters are for scale, not for starting.
