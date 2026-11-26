---
id: 07.03.A.K3
tsc: 7
level: Advanced
code: K3
title: Hardware libraries: what CUDA and Neuron actually buy you
as_at: 2026-11-26
review_by: 2027-02-25
---

# Hardware libraries: what CUDA and Neuron actually buy you

> **TSC #7 Generative AI Model Development and Fine Tuning · Advanced · Knowledge K3**


> **Framework text (verbatim):** "Hardware libraries (e.g., CUDA, Neuron libraries)."
>
> **TSC #7** Generative AI Model Development and Fine Tuning · **Advanced** · Knowledge · Bullet 3 of 20

**One-line version:** The chip is the engine; the hardware library is the gearbox, the fuel mapping and the exhaust — and no one buys a car by engine displacement alone.

## What it is

Hardware libraries are the vendor-supplied software layers that turn a general-purpose parallel processor into a fast matrix machine: NVIDIA's CUDA stack (cuBLAS, cuDNN, NCCL, TensorRT, CUTLASS), AMD's ROCm/HIP equivalents, AWS's Neuron SDK for Trainium and Inferentia, XLA for TPUs, Metal and MLX on Apple silicon. They provide the kernels, the collective communication and the precision paths that a training or inference job actually spends its time inside.

## Deep expansion

### The concept

A transformer is, at the hardware level, an enormous number of matrix multiplications plus some elementwise work. Both halves are trivially parallel and both are limited by memory bandwidth far more often than by arithmetic. The library's job is to keep the arithmetic units fed: fuse operations so intermediate tensors never touch memory, choose tile sizes that fit the cache, and communicate gradients across devices without stalling.

This is why the same model, same batch size, same chip count can run at wildly different speeds on two stacks. Frameworks like PyTorch are the interface; the library is where the performance lives. When a learner says "the GPU is at 30% utilisation", the answer is almost always in the library layer or in the data pipeline feeding it, not in the model.

### The sub-concepts

**Kernels and fusion.** A kernel is one compiled routine run across thousands of threads. Reading and writing intermediate results to global memory is the tax; fusion removes the tax. A well-fused attention implementation changes throughput by a factor, while leaving the maths identical.

**Precision paths.** bf16, fp16, fp8 and int8 exist as first-class library paths, with scaling factors handled for you. Mixed precision is now the default for training, not an optimisation to attempt later.

**Collectives.** NCCL on NVIDIA, RCCL on AMD, and equivalents elsewhere implement all-reduce, all-gather and reduce-scatter. Data, tensor, pipeline and expert parallelism are all built on these four primitives. A slow collective shows up as idle GPUs and a mysteriously low step time.

**Vendor lock-in is mostly a kernel-coverage problem.** CUDA's advantage is not the language; it is a decade of hand-tuned kernels for every operation anyone needed. Porting a model to a new accelerator means finding, or writing, the kernels it depends on — which is why "supported hardware" lists are shorter than the marketing implies.

### How it connects to the rest of the framework

`TSC7-Advanced-K6` (compute efficiency) is what you do *with* these libraries: quantisation and distillation are only real if the kernels support them. `TSC7-Basic-K10` (parallel cluster training) is distributed training at a shallower level — NCCL plus a schedule — and `TSC7-Advanced-A3` (optimisation) is where this knowledge gets applied under a deadline.

### What is current as of November 2026

Two shifts have consolidated. First, kernel-writing DSLs such as Triton and the newer tile-level languages have become the normal way to write fast custom kernels, which reduced the moat around hand-written CUDA without removing it. Second, accelerator diversity is real: Trainium and Inferentia via Neuron, TPUs via XLA, and a healthy AMD ROCm ecosystem mean most serious teams now test on at least two backends. The serving stacks behind current frontier models all depend on custom attention and KV-cache kernels rather than stock framework code.

Current models, versions and prices live in the [Living Register](../concepts/living/register.csv), checked monthly. This section covers only what changed for this topic.

### Common misconceptions

- *"CUDA is a programming language I need to learn."* Mostly you need to know which libraries exist, what they cost, and how to read a profiler. Writing kernels is a specialist skill.
- *"More GPUs means proportionally more speed."* Without efficient collectives and a balanced batch, doubling devices often yields far less than double.
- *"Any accelerator works if the framework installs."* Installation is not support. Silent fallback to a slow reference kernel is the common failure, and it does not raise an error.

## How a student should understand it

**Mental model:** the chip is a kitchen; the library is the layout. Same cook, same ingredients — but if the prep station is across the room, dinner arrives late.

**Three things they can do after this bullet:**
1. Read a profiler trace and say whether a step is compute-bound, memory-bound or input-bound.
2. Choose a precision path and justify it against an accuracy test.
3. Explain why a model runs on one accelerator and not another, in terms of kernels rather than brands.

**Misconceptions to kill:** that the framework is the performance layer, that portability is free, and that utilisation percentage tells you where the bottleneck is.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The MRT signalling system.** Passengers see trains and tracks; throughput is set by signalling, power and platform management. Nobody judges the system by how shiny the train is. Where it breaks: MRT upgrades are centrally planned, whereas accelerator libraries are a market with incompatible gauges.

**The wok station layout.** A hawker with a good *mise en place* cooks twice as fast with the same wok and the same skill. Fusion is putting the soy sauce within reach.

### Worked example with a real tool

Ask a model to triage a slow training job, then verify with a profiler:

```
Our 7B model trains at 22% GPU utilisation on 8 x A100, batch 2
per device, sequence 4096. Steps per second dropped 40% after we
switched from 4 to 8 devices. Framework: PyTorch with FSDP.

List the five most likely causes in order, the profiler signal
that distinguishes each, and the cheapest change to test first.
Assume no code changes are allowed until we know the bottleneck.
```

What to point at afterwards: run `nvidia-smi dmon` and a PyTorch profiler trace while the job runs. The class should see that the top-voted cause (model inefficiency) is usually wrong, and that the trace points at collective stalls or data loading. The lesson is that the library layer, not the model, owns throughput.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — show two identical training runs at different steps per second; ask what differs.
2. **State the objective** — read a profiler trace and name the bottleneck class.
3. **Recall prior learning** — what a matrix multiply costs in memory traffic from `TSC7-Advanced-K6`.
4. **Present the content** — kernels, fusion, precision paths, collectives, portability.
5. **Guide** — walk the 8-device example and mark the trace together.
6. **Elicit performance** — pairs classify three anonymised traces.
7. **Give feedback** — compare classifications; correct the "more GPUs" reflex.
8. **Transfer** — each learner writes the one measurement they will add to their own job.

## What the framework doesn't mention but trainers need to know

- **Version pinning is the real skill.** Driver, toolkit, framework and kernel library must agree. Most "it broke overnight" incidents are a silent upgrade.
- **Benchmark with your shapes.** Published throughput assumes a batch and sequence length; your traffic may be short prompts and long outputs, which hits a different kernel.
- **Custom kernels are a maintenance liability.** Every hand-written kernel must be re-validated on the next driver.
- **Cost per token, not utilisation, is the metric that survives a budget review.**

## Watch out

- **Do not teach CUDA syntax in a model-development course.** Teach what the stack buys and how to measure it.
- **Do not demo a microbenchmark as a product claim.** Peak throughput numbers collapse under real batching and network jitter.
- **Do not let vendor marketing set the vocabulary.** "Supported" means a kernel exists and is tested, not that it is fast.
- **The stale claim to retire:** "GPU performance doubles every generation, so just wait." In 2026 the gains that matter come from kernels, precision and serving architecture.
