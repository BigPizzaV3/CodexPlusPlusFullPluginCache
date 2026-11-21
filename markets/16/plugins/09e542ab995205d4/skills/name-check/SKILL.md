---
name: name-check
description: 'Check whether AI apps confuse a business with another business that has the same or a similar name, and write the fix. Finds the look-alike names, tests what AI apps say about the name, and drafts the one sentence that tells the businesses apart. Use for "ChatGPT thinks we are another company", "AI describes the wrong business", or before you choose a business name. Needs no Frontmost AI account.'
---

# Name check

An AI app can use the name of one business for another business. The answer looks like a mention, and it sells a different company.

Example from our own name: some answers to a question about Frontmost AI describe Front, a shared inbox product. That answer is about a different business. It is not a mention of Frontmost AI.

Use this guidance to find that problem and to write the fix. It also works before a launch, to test a name.

## 1. Find the look-alike names

1. Get the exact business name, the website domain, one line on what the business sells, and the market.
2. Make the short form of the name. Use lower case. Remove spaces and punctuation. Remove an ending such as Inc, LLC, Ltd, GmbH, AI, IO, App, HQ, Labs, or .com.
3. Search the web for each of these:
   - The short form, and the full name.
   - The name on other domain endings, such as .com, .co, .io, .ai, and .co.uk.
   - The name as one word and as two words.
   - A shorter name that starts the same way, and a longer name that contains it. "Front" and "Frontmost" are an example.
   - The usual wrong spelling.
4. For each look-alike that you find, record the name, the domain, what it sells, and its market.
5. Give each look-alike one risk level:

| Risk | Rule |
|---|---|
| High | It sells to the same buyers, or it is in the same category |
| Medium | It is in a different category, and it fills most of the first ten search results for the short form |
| Low | It is in a different category, and it is in few of those results |

A look-alike on another domain ending in another country is a different business. Record it.

## 2. Test what AI apps say

1. Write four questions that contain the business name: "What is <name>?", "What is <name> and who is it for?", "How much does <name> cost?", and "Is <name> any good?"
2. Have each question asked three times, each time in a new temporary chat with search on. The person asks them in the AI app. Your own answer in this conversation is not a data point. If a Frontmost AI project holds saved answers to questions that contain the name, use those answers in place of a new round. Say which questions you used.
3. Copy each complete answer and its list of sources.
4. Give each answer one result:

| Result | Rule |
|---|---|
| Right business | The answer describes this business. Wrong details still count. Record them. |
| Wrong business | The answer describes another business under this name. Record which one. |
| Mixed | The answer joins facts from two businesses. Record each fact and its owner. |
| Not known | The answer says that it cannot find or identify the business. |

5. For each Wrong business and Mixed answer, record the pages in its sources. Those pages show where the AI app got the other business.

Report the counts for each result, for example "Right business 7 of 12, Wrong business 4 of 12, Not known 1 of 12".

## 3. Write the fix

Do these in order. Skip a step that does not apply.

1. **One sentence that tells the businesses apart.** Put the category directly after the name: "<Name> is a <category> for <buyer>, at <domain>." Use the words that a buyer uses for the category.
2. **Use that sentence in the same words** in the home page title and first paragraph, the About page, the meta description, and each profile and directory listing. For listings, use the `directory-listings` skill.
3. **Use the full name.** If the short form is another business's name, never use the short form alone on the site or in a listing.
4. **Add a block of plain facts** to the About page: the legal name, the year it started, the place, the people behind it, the product, and the domain.
5. **Correct the pages that the wrong answers cite.** If a cited page states a wrong fact about this business, draft a correction request to its publisher. The person sends it.
6. **For Not known answers,** the web holds too little about the business. Use the `source-map` skill to find the pages to get onto.

If the name is not yet in use and a look-alike has High risk, say plainly that a different name avoids the problem. The choice is the person's.

## 4. Check again

Ask the same four questions four weeks after the changes are live. Compare the counts for each result. A difference of one answer is normal variation.

## Rules

- No measured evidence shows that these changes alter AI answers. They make the facts clear on the pages that the business controls. Say so.
- This is not a trademark search. For a legal question about a name, the person asks a lawyer.
- The person decides which details are wrong. You do not know the business as the person does.

## Never suggest

- A request to an AI app to change an answer, with a date for the correction.
- Contact with the other business.
- Keywords added to the business name in a profile or a listing. Google Business Profile requires the real name.
- A page or a listing that criticizes the other business.

## Output

1. The look-alike names, each with its domain, what it sells, and its risk level.
2. The counts for each result, with the AI app and the date. If nobody asked the questions, say so.
3. The sentence that tells the businesses apart, and each place to put it.
4. The correction requests as drafts.
5. The date of the next check.
