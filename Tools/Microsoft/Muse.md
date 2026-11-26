# Muse — Microsoft

**Tier:** Living · **As at:** 26 November 2026 · **Expires:** versions and pricing rot within a quarter.

**What it is:** A first-of-its-kind generative AI World and Human Action Model (WHAM) built by Microsoft Research and Xbox to generate 3D video game visuals and controller actions for gameplay ideation.

## The product
Muse is a specialized research model developed by Microsoft Research Cambridge (Game Intelligence and Teachable AI Experiences teams) in collaboration with Xbox Game Studios’ Ninja Theory. First published in *Nature* in February 2025, Muse learns the underlying 3D mechanics, physics, and temporal structure of an interactive video game directly from human gameplay data—specifically trained on over one billion image frames and controller actions (equivalent to more than seven years of continuous gameplay) from the 4v4 multiplayer game *Bleeding Edge*. Rather than being a consumer product for gamers, it is an experimental sandbox and research model designed to help game developers prototype gameplay dynamics and explore how older games might be preserved or adapted across hardware.

## Current line-up (November 2026)
- **Core model (`WHAM-1.6B`):** A 1.6-billion-parameter autoregressive transformer model catalogued in `Microsoft Foundry` (formerly Azure AI Foundry) and released via open-source academic weights and code. It operates across three distinct generation modes:
  1. *World Model mode:* Predicts future video frames given a starting game state and a sequence of human controller actions.
  2. *Behaviour Policy mode:* Predicts the next plausible human controller action given past visual frames.
  3. *Full Generation mode:* Autonomously generates both the evolving game visuals and the simulated player controller inputs simultaneously.
- **Interactive prototyping tools:** `WHAM Demonstrator`, an experimental visual interface announced with the research milestone that allows game designers to prompt, steer, and inject new elements into generated gameplay sequences to test persistence and 3D dynamics.
- **Disambiguation warning (November 2026):** Do not confuse Microsoft’s gameplay WHAM `Muse` (2025–2026) with `MUSE` (an August 2026 Microsoft Research arXiv paper on an interactive meta-agent for steering LLM data science workflows), nor with **Meta’s `Muse` LLM family** (`Muse Spark`, `Muse Glimmer`, `Muse Wonder`, and `Muse Spark Open`), which Meta Superintelligence Labs launched between April and October 2026 as the successor to Llama (and which are also hosted as third-party models inside `Microsoft Foundry`).

## What it's best at / not best at
**Decision rule:** Use Microsoft Muse as a research and teaching artifact to demonstrate how world models learn physical cause-and-effect from action-video pairs; do not use it as a production game engine or general video generator.
- **Best at:** Generating spatially and temporally consistent 3D gameplay sequences resembling *Bleeding Edge*; maintaining object persistence when a camera pans away and returns; reacting accurately to live controller inputs during ideation.
- **Not best at:** Generating visuals outside the domain of *Bleeding Edge* (out-of-scope); outputting high-definition production graphics (outputs are low-resolution, 300×180 pixel tokens built for dynamics, not visual fidelity); replacing traditional deterministic game engines like Unreal or Unity.

## Pricing (November 2026)
- **Open Research Weights:** $0. The `Muse` (`WHAM-1.6B`) model weights, sample dataset, and `WHAM Demonstrator` code are released free for academic and research use.
- **Cloud Hosting (`Microsoft Foundry`):** When deployed via the `Microsoft Foundry` model catalog, there is no software licensing fee for the academic model itself, but users pay standard underlying Azure GPU compute and token/endpoint hosting costs depending on deployment type.
- **Uncertain:** Microsoft has not announced any commercial SaaS pricing tier or timeline for turning Muse into a paid Xbox developer toolset as of November 2026.

## What this actually teaches
**AI is moving from learning language to learning world mechanics (World Models).** Muse is the clearest, most concrete vehicle for teaching non-technical learners the difference between a standard text/video generator (which predicts pixels or words without understanding physics) and an interactive *world model* that maps cause-and-effect between human actions (controller presses) and environmental state changes.

## The student lens
**Mental model:** A flight simulator that wasn't programmed with physics equations by software engineers, but instead learned how an aeroplane turns, stalls, and lands purely by watching seven years of cockpit videos paired with the pilot’s joystick movements.
**Misconceptions:**
- *"Muse lets you type a text prompt and instantly generate a playable AAA Xbox game."* → **Correction:** Muse does not take text prompts to build new games; it takes starting visual frames and controller actions to simulate low-resolution gameplay solely within the world of *Bleeding Edge*.
- *"Muse is just like Sora or Runway video generation for gaming."* → **Correction:** Standard video generators create passive movies that ignore user input after the prompt; Muse is interactive, recalculating the world frame-by-frame in response to controller button presses.
- *"Microsoft Muse is the new open-weight LLM competing with GPT-6."* → **Correction:** That is *Meta’s* `Muse` (`Muse Spark` / `Muse Wonder`), released in mid-to-late 2026. Microsoft’s `Muse` is a 2025/2026 gameplay World and Human Action Model.

## The adult educator lens
**Analogy:** Standard text-to-video AI is like watching a National Day Parade rehearsal video on YouTube—the jets fly past the Marina Bay floating platform the exact same way every time. Microsoft Muse is like the Red Lions’ parachute simulator at Hendon Camp: when you pull the left toggle (controller action), the visual screen shifts left in real time because the system has learned how wind and canopy mechanics respond to your hands. *Where it breaks:* A military simulator runs on hard-coded aerodynamic math that never forgets a building exists, whereas Muse is predicting pixels probabilistically—if a sequence runs past its context window, the arena walls can still morph or drift.
**Three-minute demo:** Play a 30-second side-by-side clip from the Microsoft Research `WHAM Demonstrator`: show a single starting frame of a character on a ledge, feed two different controller action sequences (jump forward vs spin camera left), and watch the model generate two completely different, physically coherent 3D trajectories—including remembering a ramp behind the player when the camera turns back.
**Where it goes wrong in class:** Learners search `"Muse AI model 2026"` on their phones during class and immediately pull up articles about Meta’s 816B-parameter `Muse Spark Open` LLM or `Muse Wonder`, derailing the discussion because two tech giants used the exact same model name in 2025–2026.
**Check for understanding:** "Why did Microsoft have to train Muse on *both* video frames *and* controller button presses together, rather than just feeding it 10,000 hours of YouTube gaming videos?"

## Watch out
- **Retire stale claims:** Do not present world models as purely theoretical; since February 2025, `WHAM-1.6B` has been publicly downloadable and inspectable. Conversely, do not claim Xbox is currently replacing human game studios with Muse—following industry pushback in 2025, Microsoft explicitly positioned Muse strictly for research, ideation, and game preservation compliance.
- **Do not overclaim:** Do not tell learners they can fine-tune `WHAM-1.6B` on a standard laptop to clone their own games; the model card explicitly restricts out-of-scope imagery outside *Bleeding Edge* and embeds provenance watermarks.
- **Verify before class:** If demonstrating via `Microsoft Foundry` (`Azure AI Foundry`), verify the exact catalog filter before searching `"Muse"`. Because Microsoft Foundry added Meta’s `Muse-Glimmer-30B` and `Muse Spark Open` weights to its Azure catalog in late 2026, searching `"Muse"` in the Foundry portal returns both Microsoft’s gaming WHAM and Meta’s LLMs.

## Sources
- [Introducing Muse: Our first generative AI model designed for gameplay ideation — Microsoft Research](https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/) (19 February 2025)
- [World and Human Action Models towards gameplay ideation — Nature](https://www.nature.com/articles/s41586-025-08600-3) (19 February 2025)
- [Microsoft Foundry Model Catalog: WHAM-1.6B & Model Card — Microsoft Azure](https://ai.azure.com/explore/models) (Accessed November 2026)
