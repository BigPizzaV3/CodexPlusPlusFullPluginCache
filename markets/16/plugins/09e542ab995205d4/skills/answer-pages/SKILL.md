---
name: "answer-pages"
description: "Plan a page on the business's own site from real AI answers: a question page, a fair comparison, or a better cited page."
---

# Answer pages

Use this guidance to plan a page on the business's own website from the answers that AI apps gave. It covers four jobs: a page for one question, a comparison page, improvements to pages that AI apps already cite, and page ideas from ChatGPT's searches.

## Read the answers first

1. Call the tool in the request (`get_questions`, `get_rivals`, `get_sources`, or `get_queries`).
2. Open the real answers. Use `question_id`, `rival_id`, or the row's `answers_filter` in `get_answers`. Do not build a filter.
3. Write down three things: the points that the answers repeat, the facts that they use to compare businesses (price, features, limits, who the product fits), and the format of the pages that they cite (comparison, list, guide, review).

## Plan the page

- **Title**: the buyer's question in plain words.
- **First paragraph**: a direct answer in 2 or 3 sentences that a reader can quote without the rest of the page.
- **Body**: one section for each point that the answers repeat. Put the specific fact first in each section.
- **Facts**: use only facts that the person confirms. When you need a price, a limit, or a feature and you do not have it, ask. Never invent one.

## Job rules

- **One question**: pick the question with the most lost answers unless the person names one.
- **Comparison**: take each point from a real answer and show the quote. Include the points where the rival is stronger. A page that hides them is not fair, and readers will see it.
- **Cited pages**: for each of the business's own pages that AI apps cite, say what the answers took from it and what the answers needed and did not find there.
- **Searches**: group ChatGPT's searches by what the buyer wants. Give one page idea for each group. Ask which groups the site already covers before you call a group a gap.

## Never suggest

- `llms.txt` files or "AI schema". Google states that its AI features need no new files and no special markup.
- Keyword stuffing, hidden text, or copied text from a rival.
- Any promise that AI apps will cite or mention the page. No method is proven to earn a citation. A page is a bet that the data supports.

## Output

An outline: the title, the first paragraph as a draft, the section headings with one line on what each section must state, and the list of facts that you still need from the person.
