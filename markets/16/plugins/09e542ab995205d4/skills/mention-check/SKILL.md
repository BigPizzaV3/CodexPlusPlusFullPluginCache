---
name: mention-check
description: 'Check by hand whether AI apps mention a business when buyers ask about its category. Writes the buyer questions, has each one asked three times in new chats, counts who the answers mention and which pages they link, and says what to do first. Use for "does ChatGPT recommend my business", "does AI mention us", or a first AI visibility check. Needs no Frontmost AI account.'
---

# Mention check

One AI answer shows little. The same question rarely returns the same list of businesses twice. How often a business appears is steadier than its place in the list. So this check asks each question three times and counts.

The check needs no account. It takes about 20 minutes for one AI app.

## What counts as an AI answer

- Use the AI app that buyers use: ChatGPT, Gemini, Google AI Mode, Perplexity, Copilot, or Claude. An answer from a developer API can differ from the answer in the app.
- The person asks the questions in the AI app. If you have a browser tool and the person asks you to, you can ask them in the person's AI app.
- Your own answer in this conversation is not a data point. You already know the business. Never answer the questions yourself and count the result.

## 1. Write the questions

1. Get the business name, the website, one line on what it sells, the market (country or city), and two or three rivals.
2. Write five discovery questions. A discovery question does not contain the business name. Write one for each group:

| Group | Example, for an invented invoicing tool |
|---|---|
| Best choice | What is the best invoicing tool for freelancers? |
| In place of a rival | What are good alternatives to Billbright for freelancers? |
| Price | How much does invoicing software for a freelancer cost? |
| A problem | How do I stop chasing late invoices? Is there a tool for it? |
| Fit | Which invoicing tools work with Stripe and send recurring invoices? |

3. Write two questions that contain the business name: "What is <business> and who is it for?" and "Is <business> a good choice for <buyer>?" Give them the group Name.
4. Write each question the way a buyer types it. For the wording rules, use the `aeo-question-drafting` skill.
5. Show the seven questions to the person. Change them on request.

The two questions with the business name show what AI apps say about the business. Their answers never enter the score.

## 2. Ask

Start with one AI app. For each question:

1. Open a new temporary chat, so that memory and earlier chats stay out.
2. Turn search on. Keep an answer only if it shows its sources. If it shows none, ask again in a new chat, up to two more times.
3. Paste the question. Copy the complete answer and its list of sources into a text file.
4. Do this three times for each question, each time in a new chat. Seven questions give 21 answers.

Ask all the questions on one day, from the market's location. Answers for a local business change with the place. Record the date, the AI app, the place, and whether the person was signed in.

If you ask the questions with a browser tool, do not sign in for the person. Stop at a CAPTCHA.

If a question has fewer than three answers, keep the answers and report the smaller count.

## 3. Count

Decide one result for each answer:

| Result | Rule |
|---|---|
| Mentioned | The answer text contains the name of the business or of its product. A list, a comparison, and a criticism all count. Wrong details still count. |
| Not mentioned | The text does not contain the name. A link to the business's site with no name in the text does not count. |
| Wrong business | The answer uses the name for a different business. |
| Not known | The answer says that it cannot find or identify a business with that name. |

- A discovery answer is usually Mentioned or Not mentioned. If it uses the name for a different business, the result is Wrong business, and the answer does not count as Mentioned.
- A Name answer can have each of the four results. It shows whether the AI app knows the business.
- Count a business once for each answer, however often the answer repeats it.
- Leave an answer that failed or is not complete out of the total. If you could read no answers, the result is "not available". It is not zero.

Make one row for each answer, and save the table as `mention-check-<date>.csv`:

| Column | Value |
|---|---|
| Date, AI App, Place, Signed In | from step 2 |
| Question, Group, Try | the question, its group, and 1, 2, or 3 |
| Result | one of the four results |
| Position | the place of the business in a list, if the answer gives one |
| Others Mentioned | each other business in the answer |
| Linked Pages | each page address in the sources |
| Facts To Check | the exact words of a price, a feature, a location, or a customer type that the answer states about the business |

Then count three things:

1. **The score.** The discovery answers with the result Mentioned, of the discovery answers that you read, for example "3 of 15".
2. **Each rival.** The number of discovery answers that mention it.
3. **Each linked page.** The number of answers that link it. Open each page that two or more answers link. Record Present, Not present, or Check needed, as the `source-map` skill defines them.

## 4. Read the count

Run the `ai-readiness` skill first, if it has not run. A site that AI apps cannot read is the first job.

Then use the first row that applies.

| The count shows | First job | Skill |
|---|---|---|
| A Wrong business or a Not known result | Fix the name problem. Other work cannot help while AI apps describe another business. | `name-check` |
| A fact in Facts To Check is wrong | State the correct fact on the business's own page. Then ask the linked page that repeats it for a correction. | `site-audit` |
| A rival is in more than half of the discovery answers, and a page that two or more answers link is Not present | Get onto those pages, the most linked first. | `source-map` |
| The business is mentioned for Best choice, and never for Price, A problem, or Fit | Publish a page that answers the question of one group with no mention. | `page-drafting` |
| The business is in 2 or fewer of the discovery answers, and no row above applies | State what the business sells, for whom, and where, in the same words on every page and listing. | `site-audit`, `directory-listings` |

The person marks which facts are wrong. You do not know the business as the person does.

## 5. Repeat

- Repeat the check each month with the same questions, the same AI app, and the same place.
- A difference of 1 or 2 answers is normal variation. Do not call it a change. Look for the same direction in two checks in a row.
- A higher count after an edit does not prove that the edit caused it. Say so.

## Limits

Say these in the result:

- The count is a small sample from one day and one place. Answers differ by person, place, and day.
- The check shows what a new buyer can see. It does not show sales. For that, use the `customer-survey` skill.

## Output

1. The score with its counts, the AI app, the date, and the place.
2. The rivals, each with its count.
3. The pages that two or more answers link, each with Present, Not present, or Check needed.
4. What the AI app says about the business: the quotes from Facts To Check.
5. The first job, with its skill.
6. The limits.
