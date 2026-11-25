# TEC-01 · AI video: the parameters that actually exist

**Tier:** Technique (with a living tail) · **As at:** 9 November 2026 · **Expires:** the method holds; the field names change with every release.

**Framework home** — TSC #1 (Basic): *creation of content in different modes*. TSC #6 (Basic to Intermediate): *using models to generate media; API parameters*. Sits beside the Media framework's image and video TSCs when a course is credentialed there.

---

## The thing nobody tells the class

Most of what the market calls "camera control" in AI video is **not a parameter**. It is prose that the model may or may not honour. Only a handful of vendors expose a field with "camera" in its name, and only one of those is an unambiguous, working camera switch.

This matters pedagogically because learners arrive believing there is a dial. There isn't. There is a prompt, a small settings object, and a retry.

## The real state of the field

| Vendor / surface | Field | What it actually does | Real camera control? |
|---|---|---|---|
| Seedance (BytePlus ModelArk) | `camera_fixed` | Locks the camera in place | **Yes** — a genuine boolean |
| Kling 3.0 / Omni (text-to-video) | `settings.aspect_ratio`, `settings.duration` (3–15s), `settings.audio` (`native`/`off`), `settings.multi_shot` | Frame shape, length, audio track, automatic shot splitting | No — none of these names or moves a camera |
| Kling Motion Control (separate endpoint) | `settings.character_orientation` | Matches a character to a reference image or video | No — moves a character, not a lens |
| Runway (Gen-4.5 Act-Two) | `bodyControl`, `expressionIntensity` (1–5) | Character body motion and expression strength | No — performance, not cinematography |
| Vidu Q2 / Q3 | `movement_amplitude` (`auto`/`small`/`medium`/`large`) | Documented as inert on Q2 and Q3 | Documented but currently does nothing |
| Veo 3.1 (Gemini API) | `aspectRatio` (`16:9` or `9:16`) | Frame shape only | No camera field exists — direction is 100% prompt language |

Two more facts worth having ready, because they come up in every class:

- **Kling does not generate at 60fps.** Its documentation describes a 24–60fps range for *reference video you upload*, then states in the same sentence that generation is 24fps. The 60fps claim is a misreading of an input spec.
- **Kling's shot grammar is prose, not a field.** Writing `shot 1, 3, wide establishing; shot 2, 4, close on hands;` splits the clip, but it is a string convention the model parses, capped at six shots and 512 characters per shot, with each shot at least one second and the durations summing to `settings.duration`. Only `settings.multi_shot` is a validated boolean.

Status caution: one source reports that OpenAI's Sora 2 models and the Videos API were shut down on 24 September 2026. Verify before you build a lesson around Sora, and treat any vendor's video surface as having a short life.

## What to teach instead of a dial

Three layers, in this order:

1. **What the schema guarantees.** Aspect ratio, duration, resolution, audio on/off, image-to-video vs text-to-video, seed where offered. These are reliable.
2. **What the prompt asks for.** Camera movement, lens, framing, lighting, pacing. Real vocabulary — push in, dolly out, crane up, orbit, whip pan, Dutch angle, 35mm, shallow depth of field — works because the models were trained on captioned footage. It is a request, not a setting.
3. **What you fix in the edit.** Multi-shot, continuity, cut points, sound. The model gives you takes; the edit gives you a film.

## The student lens

**Mental model:** a very fast, very literal camera operator who has never seen your storyboard and cannot ask questions.

**Misconceptions:**
- *"There's a camera control panel, so it controls the camera."* Panels are often prompt builders with a nicer interface.
- *"Longer clips are better."* Duration, resolution and motion quality trade against each other; short shots cut together beat one long wobbly take.
- *"If it looks cinematic, the prompt was good."* Often the seed was lucky. Re-run before you conclude anything.

**Five-minute practice:** write a three-shot spec sheet — shot number, duration, framing, camera move, subject action, audio — then generate each shot separately rather than one eight-second prompt. Compare continuity.

## The adult educator lens

**Analogy:** hiring a freelance cameraman who speaks only the words you give him. "Nice shot" gets you nothing. "Medium close-up, 50mm, slow push in, window light from the left" gets you a shot. He is not being difficult; he has no other information.

**Three-minute demo:**
1. Ask for a "cinematic shot of a hawker centre at night". Show the generic result.
2. Re-run with a real spec: wide establishing, 24mm, slow dolly forward, steam in foreground, warm tungsten, 9:16, 6 seconds.
3. Then change only the aspect ratio and show how the composition breaks — the clearest proof that a parameter and a sentence do different jobs.

**Board sketch:** two columns — SCHEMA (guaranteed) and PROMPT (requested) — with a third box underneath labelled EDIT. Ask the room to sort five controls into the columns before you show the table.

**Where it goes wrong in class:** someone insists their tool has "camera control". It usually does — as a UI that writes prompt text. Show them the request body. That single click converts a sceptic into someone who reads documentation.

**Check for understanding:** "Your client wants a vertical clip with a locked-off camera and no drift. Which of those two requirements is a field, and which is a request?" (Locked camera: `camera_fixed` on Seedance, or prose elsewhere. Vertical: `aspect_ratio` / `aspectRatio`, a real field.)

## Say this out loud

"Most camera control in AI video is a sentence, not a slider. Learn the vocabulary, then learn which three fields actually do something."

## Content hook

**LinkedIn opener:** "Every AI video tool advertises camera control. Exactly one of the six I checked has a field with the word 'camera' in it that does what it says."

**Carousel idea:** "Schema vs prose" — the request body on the left, the prompt on the right, and the same shot generated both ways.
