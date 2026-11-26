---
id: 02.01.B.K1
tsc: 2
level: Basic
code: K1
title: Troubleshooting techniques
---

# Troubleshooting techniques

> **TSC #2 Prompt Design · Basic · Knowledge K1**

**Bullet (verbatim):** Techniques in troubleshooting AI tools.

**What it means:** Troubleshooting means working out why a tool is not doing what you expect. First notice whether an answer arrived but did not meet your needs, or whether the tool failed to give an answer. Check the instruction you sent, called a prompt, and consider the internet connection and the provider’s service separately. Change one factor at a time and compare the result; a single test gives a clue, not certain proof of a cause.

**The learner must be able to:**
- Record the expected result, the actual answer or error, and the time it occurred.
- Choose a first check for a prompt, connection or provider-service problem.
- Change one factor, repeat the test and compare the results against a clear requirement.
- Describe when to ask the provider or workplace technology support team for help and what evidence to share.

**How to teach it in 20 minutes:**
1. Ask: “What would you check first if an AI reply had the wrong format? What if no reply appeared at all?” Collect one suggestion for each. (3 min)
2. Explain three possible areas, not automatic diagnoses. If a reply has the wrong format, compare it with the prompt and try one wording change. If no reply appears, retry the same prompt, check whether another website loads and, if permitted, retry on a different network, such as mobile data instead of Wi-Fi, without changing the prompt or device. Success on the second network suggests a connection issue. Check the provider’s page reporting service incidents, if available; a matching incident suggests a service issue. These are clues: a clear page or working website does not prove the AI service is healthy. If the problem continues, share the actual error, time and checks with the provider or workplace technology support team; do not share passwords. (7 min)
3. Pairs run both prompts below in separate new chats with the same AI and settings, then compare their replies with the two-sentence requirement. Identify the single factor changed. If either reply does not follow its instruction, repeat that unchanged prompt once and record the result instead of assuming the cause. (8 min)
4. Debrief: Did the first prompt ask for the intended format? What does the comparison suggest, and what would you check if there had instead been a real connection error? (2 min)

**Exercise (with the exact prompt):**
*Setup: Any chat AI; no files needed. A ticket is a recorded request for help. The desired final result is two sentences; run each prompt in a fresh chat using the same tool and settings.*

Prompt 1:

```text
Using only these fictional facts, write a queue summary in 1 sentence.
Open tickets: 3
Closed today: 5
```

Prompt 2:

```text
Using only these fictional facts, write a queue summary in 2 sentences.
Open tickets: 3
Closed today: 5
```

Expected result: Prompt 1 produces one sentence and Prompt 2 produces two; both mention the two ticket counts. Outputs can vary.  
Check: Count sentences and check both replies say 3 tickets are open and 5 were closed today. Record both results and identify the requested sentence count as the one factor changed; Prompt 1 conflicts with the two-sentence requirement.

**Common mistakes:**
- Assuming an unsatisfactory answer is a connection failure — first compare the answer with the prompt and the requirement.
- Changing the prompt, AI tool and network together — change one factor per comparison so the result is easier to interpret.
- Treating an error invented in AI text as a real outage — use an actual app error or the provider’s status page as evidence, and report persistent problems with the time and checks made.

**Sources:**
- https://www.imda.gov.sg/-/media/imda/files/how-we-can-help/tesa/sfw-for-ict/sfw-for-ict-skills-in-genai.pdf — accessed 2026-11-15; page 5 identifies the TSC, level and verbatim knowledge bullet.
- https://help.openai.com/en/articles/7996703-troubleshooting-chatgpt-error-messages — accessed 2026-11-15; examples of error, retry, network, status-page and support checks for ChatGPT.
- https://help.openai.com/en/articles/9247338-network-recommendations-for-chatgpt-errors-on-web-and-apps — accessed 2026-11-15; comparing networks and checking for known service disruptions.
- https://help.openai.com/en/articles/6614161-how-can-i-contact-support — accessed 2026-11-15; details to include in a support request and the instruction not to share passwords.
- https://status.openai.com/ — accessed 2026-11-15; status information is aggregated and individual availability can differ.
- https://developers.openai.com/api/docs/guides/prompt-engineering — accessed 2026-11-15; testing prompt behaviour and the variability of generated content.
- https://developers.openai.com/cookbook/examples/audio/voice_agent_evaluation — accessed 2026-11-15; change one variable at a time so test results are easier to interpret.
