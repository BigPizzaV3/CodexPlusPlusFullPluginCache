---
name: customer-survey
description: 'Find out whether AI apps send a business customers. Adds one optional question, "Where did you first hear about us?", with AI assistants as their own answer, and reads the answers beside analytics. Includes a ready prompt for a coding agent. Use for "is AI sending me customers", "how do I measure ChatGPT traffic", or AI attribution. Needs no Frontmost AI account.'
---

# Customer survey

A count of AI mentions shows whether AI apps mention a business. It does not show whether those mentions bring customers. Analytics miss much of it: a buyer hears of the business in ChatGPT, then searches for its name, and the visit looks like a search visit.

So ask the customers. Use this guidance to add one question, to save the answers correctly, and to read them.

## 1. Place the question

Ask "Where did you first hear about us?" once, at the first moment that fits:

| Business | Where to ask |
|---|---|
| Software with sign-up | The first screen after sign-up |
| Online store | Directly after the first purchase |
| Service business | The enquiry form, or the first call. The person who takes the call records the answer |

Make the question optional. It takes one tap. A customer sees it once.

## 2. Write the answers

- Use ten answers or fewer, one for each row.
- Make "An AI assistant" one of the answers. Without it, a buyer who found the business in ChatGPT picks "Google" or "Other".
- When a customer picks "An AI assistant", ask "Which one?": ChatGPT, Claude, Gemini, Google AI Mode or AI Overviews, Perplexity, Microsoft Copilot, Grok, or another.
- Use the channels that this business's buyers use. A store can replace LinkedIn with TikTok or Instagram. A local business can add Google Maps.
- Include "Other" with a short text field.

A starting list: An AI assistant. Google or another search engine. YouTube. LinkedIn. Reddit. X (Twitter). Other social media. A friend or colleague. Podcast, newsletter, or article. Other.

## 3. Save the answers

- Save each answer on the customer's record, with the date.
- Save a skipped question as skipped, with no answer. Never save a skip as "Other".
- Keep the answer where the payment status is, so that paying customers can be counted by source.

## 4. Build it

- **In the product's code.** If you work in the code and the person asks, follow [build-prompt.md](references/build-prompt.md). List the files and the fields first, and wait for approval before you change the code.
- **In a form tool or a store platform.** Give the person the question, the answers, and the rule for skips. The person adds them in that tool.
- **By hand.** For a service business, add a column to the customer list, with the same answers.

## 5. Read the answers

Read the answers after a few weeks. Report counts, not shares alone: "7 of 52 paying customers picked an AI assistant: ChatGPT 5, Perplexity 2. 9 skipped."

Read three signals together. Each one answers a different question.

| Signal | Question that it answers | Where it comes from |
|---|---|---|
| The survey | Where did the customer hear of the business? | The saved answers |
| Analytics | Where did the visit come from? | Visits whose referrer or `utm_source` is an AI app, such as chatgpt.com or perplexity.ai |
| AI mentions | How often do AI apps mention the business? | A `mention-check` count, or a Frontmost AI project |

- Count one customer once. A customer who picks ChatGPT and arrived from a search for the business name is one customer. Keep both facts.
- Count paying customers apart from sign-ups.
- When mentions rise and more paying customers pick an AI app, both signals moved in the same direction. This does not prove a cause.
- When mentions rise and the survey answers do not move, read what the AI apps say about the business. Use the `mention-check` skill.

## Limits

Say these in the result:

- People forget, and they pick the closest answer. In a 2024 study by HockeyStack of answers from B2B buyers, 2,646 of 4,939 "search" answers matched the last visit that the software recorded. See [the study](https://www.hockeystack.com/lab-blog-posts/hockeystacks-sra-report-2024).
- The answers alone do not prove what caused a purchase. They are one signal of three.
- A small number of answers shows little. Give the count each time.

## Rules

- Do not make the question required.
- Do not ask it again after an answer or a skip.
- Do not collect more than the answer, the AI app, and the "Other" text.

## Output

1. Where the question goes, and the list of answers for this business.
2. The fields to save.
3. The build path: the plan for the code, or the text for the form tool.
4. The date of the first reading, and the three signals to compare.
