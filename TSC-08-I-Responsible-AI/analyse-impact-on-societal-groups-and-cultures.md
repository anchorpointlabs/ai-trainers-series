---
id: 08.02.I.A6
tsc: 8
level: Intermediate
code: A6
title: Analyse impact on societal groups and cultures
---

# Analyse impact on societal groups and cultures

> **TSC #8 Responsible AI and Generative AI Practices · Intermediate · Ability A6**

> **Framework text (verbatim):** "Analyse the impact of AI on different societal groups and cultures (e.g., minority groups)."
>
> **TSC #8** Responsible AI and Generative AI Practices · **Intermediate** · Ability · Bullet 11 of 14

**One-line version:** A system is only as good as its worst-served group, and that group is almost always the one least represented in the data — so "works for me" is a sampling error, not a quality assurance.

## What it is

Analysing group impact means asking, group by group, how a system performs and what it does to people: which languages and dialects it handles, which names and accents it recognises, which bodies and disabilities its interface accommodates, and whose cultural defaults it treats as normal. The output is a short list of groups, the specific failure for each, and a mitigation.

## Deep expansion

### The concept

Models learn the distribution of their training data. Groups that are rare in that distribution are, by construction, less well modelled — and the failure is not random noise but a systematic bias in whose experience is treated as standard. The practical consequence: an evaluation that samples the mainstream will report success while the system fails a specific population consistently.

In Singapore the list of groups writes itself, which is why this bullet is unusually easy to teach here. Singlish speakers and code-switchers. Malay and Tamil users, whose languages are supported but thinner in the corpus than English. Dialect-speaking elderly, who may also have hearing loss and low digital literacy. People with motor, visual or hearing disabilities. Foreign workers, whose names and addresses break form validation. Each of these fails in a different way, and each requires a different mitigation.

The analysis has two halves, and teams only do the first. **Performance** — does it work for this group? **Impact** — what does the failure do to them? A transcription model that drops a dialect is a UX problem; the same model in a healthcare triage line is a safety problem. Impact is a function of where the output goes, not only of how often it is wrong.

### The sub-concepts

**Representation in the corpus.** Who is in the training data, in what proportion, and how was it collected? A corpus scraped from the open web under-represents exactly the people least likely to publish.

**Language, script and code-switching.** Tokenisation costs differ across languages, romanisation varies (Chandra, Chandran, Chandiran), and mixed-language sentences confuse models trained on monoglot text. This is the single richest local example.

**Cultural defaults.** Holidays, family structures, food, religious practice, naming conventions, and what counts as polite. A model that assumes Christmas and a nuclear family is not wrong in a way that shows up on a benchmark, but it is wrong for many users.

**Accessibility.** Not only the model: the interface, the input modality, contrast, latency, and whether a fallback channel exists for someone who cannot use the primary one.

**Compounding disadvantage.** The same group underserved by the model is often also underserved by the digital channel, the helpline and the appeals process. The system multiplies an existing gap.

**Mitigation menu.** A localised evaluation set; targeted data or fine-tuning; a fallback to human handling for affected cases; an alternative channel; or refusing the use case. Cheap options exist and are usually skipped because nobody looked.

**Consult, do not assume.** The group is the authority on the failure. Testing with five real speakers beats a month of speculation.

### How it connects to the rest of the framework

`TSC8-Intermediate-K3` is the societal consequence this bullet measures; `TSC8-Intermediate-A5` is the general analysis template that this specialises; `TSC8-Intermediate-A3` is the mitigation once a group failure is identified. `TSC8-Intermediate-K4` matters here in a specific way: the people most affected are often the least likely to read a capability note written in standard English.

### What is current as of November 2026

Multilingual coverage has improved substantially and remains uneven. The current frontier generation — GPT-6 (Astra, Sol, Luna, 6.1 Sol, 6.1 Terra, Cyber), Claude 5.5, Gemini 3.1 Pro and Gemini 4 Argon — handles major languages well, Malay and Tamil competently in formal registers, and Singlish inconsistently unless prompted or given examples. Voice models have improved on accented English and still degrade for elderly speakers and for dialect.

What has changed cheaply is localisation: fine-tuning a small model on a few hundred local examples is now an afternoon's work, which removes the old excuse that localisation was unaffordable. What has not changed is measurement: no provider ships a Singlish or dialect evaluation, so a team that does not build one is flying blind on exactly the population this bullet is about.

### Common misconceptions

- *"English is enough in Singapore."* Enough for the benchmark, not for the resident who speaks mainly Malay or dialect at home.
- *"We translated the interface, so we are localised."* Translation covers menus. Names, addresses, dates, honorifics and code-switching are what actually break.
- *"The group is small, so the impact is small."* The harm per person is identical, and it usually correlates with other disadvantages.
- *"The model will pick up Singlish from the web."* Partially and unpredictably. Consistency requires examples and evaluation.

## How a student should understand it

**Mental model:** the voice assistant that cannot hear your grandmother. It works perfectly for the person who built it and fails, every time, for the person who needs it most.

**Things they can do after this bullet:**
1. Name the three groups most likely to be underserved by a given tool, and the specific failure for each.
2. Explain the mechanism — corpus representation, tokenisation, cultural default, modality.
3. Propose a mitigation that can be tested in a week.

**Misconceptions to kill:** that mainstream success implies universal success, that translation equals localisation, and that small populations do not justify the work.

## How a trainer explains it

### Analogies that work in a Singapore classroom

**The clinic that only prints instructions in English.** The doctor is excellent; the patient goes home and misreads the dosage. Nobody in the clinic did anything wrong, and the outcome is still a harm. Where it breaks: a clinic can add a translator at the counter; a model needs the capability built in or routed around.

**The lift button mounted too high.** Perfectly functional for most users, unusable for some, and the fix costs almost nothing once someone notices. Accessibility failures are usually design oversights, not capability limits.

### Worked example with a real tool

```text
A voice assistant for a public service hotline is trained mostly on standard English.

1. Which groups in Singapore are underserved, and what exactly fails for each?
2. Rank them by harm, given that callers are often elderly and stressed.
3. For each, name a mitigation with an effort estimate (hours, days, weeks).
4. Design the test that would prove the mitigation worked, including who you would
   recruit to run it.
```

What to point at afterwards: the model will list Singlish, elderly and dialect speakers — and then propose "add more training data" for all three. Push on effort and on the fallback option: routing a caller to a human in eleven seconds may beat six months of data collection. Point at step 4: a test that recruits real speakers is the difference between inclusion and decoration.

### Lesson plan (Gagné's nine events)

1. **Gain attention** — play a clip of the assistant failing on a Singlish request, then succeeding on the same request in standard English.
2. **State the objective** — by the end you can name underserved groups, the mechanism, and a testable mitigation.
3. **Recall prior learning** — connect to the proxy and representation discussion.
4. **Present the content** — representation, language, cultural defaults, accessibility, compounding, mitigation menu.
5. **Guide** — analyse the hotline example together.
6. **Elicit performance** — groups analyse a public-facing tool they know.
7. **Give feedback** — challenge every mitigation without a named test population.
8. **Transfer** — each learner adds one group to their evaluation set this quarter.

## What the framework doesn't mention but trainers need to know

- **Dialect loss is a cultural loss, not only a UX defect.** Say it out loud; it changes how the room hears the problem.
- **Test with real speakers**, not with synthetic examples generated by a model, which reproduces the same blind spots.
- **Accessibility often has a legal dimension** that general AI guidance omits, and it is usually the cheapest fix in the list.
- **Diversity in the demo is not diversity in the evaluation.** Stock photos of varied users are not evidence.

## Watch out

- **Do not ask learners to perform accents or dialects.** Use recordings or invited speakers, and keep the room respectful.
- **Do not treat a group as a monolith.** Elderly users differ by language, income and digital confidence.
- **Do not promise inclusion without a test.** A claim about group performance that was never measured is the exact failure this bullet exists to prevent.
- **The stale claim to retire:** "the model is multilingual, so localisation is solved." Multilingual is a feature list; local adequacy is a measurement.
