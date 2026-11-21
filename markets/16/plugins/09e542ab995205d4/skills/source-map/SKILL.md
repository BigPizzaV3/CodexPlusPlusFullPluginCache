---
name: source-map
description: 'Find the pages that shape AI answers to a business''s buyer questions, sort them by type, check whether each page lists the business, and say how a business gets onto each one. Covers list articles, review sites, directories, forums, and videos. Use for "which sites does ChatGPT cite for my category", "where should we be listed", or before outreach. Works with a web search. Needs no Frontmost AI account.'
---

# Source map

An AI app builds an answer from a few pages: list articles, review sites, directories, forums, and videos. A business that those pages leave out is easy for the AI app to leave out too.

Two examples that Frontmost AI published: one review site was in 16 of 30 answers to mattress questions ([e-commerce](https://frontmost.ai/solutions/ecommerce)). The most cited sites for one software category differ between the United States and Germany ([product strategy](https://frontmost.ai/solutions/product-strategy)).

Use this guidance to make the list of those pages for one business, and to say what to do about each page. This skill contacts nobody.

## 1. Get the questions

Use five to ten discovery questions: buyer questions that do not contain the business name. Take them from the person, or write them with the `aeo-question-drafting` skill.

Get the market too: the country, the language, and the city for a local business. Make one map for each market. The pages differ by market.

## 2. Collect the pages

Use the best source that you have. Say which one you used.

| Source | What it gives | Limit |
|---|---|---|
| A Frontmost AI project | The pages that AI answers cite, with counts. Use the `placement-pipeline-sheet` skill in place of this one | Needs an account |
| A `mention-check` count | The pages that the answers linked, in the Linked Pages column | A small sample |
| A web search | The first ten results for each question | These pages stand in for AI citations. You have no citation counts |

For each page, count the questions, or the answers, where it appears. Join two addresses of one article into one row.

## 3. Sort the pages by type

| Type | Examples | How a business gets on it | Skill |
|---|---|---|---|
| Editorial list or review | A "best X" article, a test by a review site | Pitch the author or the editor | `ai-listing-outreach` |
| Directory or marketplace | A software directory, a trade directory, an app marketplace | Claim or create the listing, and complete it | `directory-listings` |
| Business profile | Google Business Profile, Bing Places | Claim it, verify it, and keep its facts current | `directory-listings` |
| Community | A Reddit thread, a forum, a question site | A useful reply that states the writer's real role | `community-replies` |
| Video | A review or a comparison on YouTube | Pitch the creator, as you pitch an editor | `ai-listing-outreach` |
| Rival or vendor site | A list on a rival's blog | Not reachable. Never ask. Learn from its format | `page-drafting` |
| Reference | An encyclopedia, a government page, news | Usually not reachable by request | none |
| Own site | A page of the business | Improve the page | `site-audit`, `page-drafting` |

Check who publishes each list before you set its type. A list where the publisher ranks its own product is a rival or vendor site.

Do not edit an encyclopedia article about the person's own business. Wikipedia's conflict-of-interest rules discourage it.

## 4. Check each page

Open the pages with the highest counts, up to 15. When most pages have a count of 1, the count does not order them. Then open the editorial lists and the directories first.

Give each page one result:

| Result | Rule |
|---|---|
| Present | The page shows the full name of the business, or links the business's own domain |
| Not present | You read the complete page, and it has no name and no link of the business |
| Check needed | The page did not load, loaded in part, or holds fewer than 400 characters of article text. Or only a short name appears, and it can be another business |
| Not opened | You did not open the page in this run |

- Only Not present supports a pitch. Check needed means that a person opens the page first. Not opened means that nobody read the page.
- A link to a shared site, such as a Reddit, LinkedIn, or YouTube address, does not identify a business.
- Record the rivals that each page lists.
- Some sites refuse automated requests. List those pages for the person to open in a browser.

## 5. Write the entry for each site

For each page with the result Not present, record four facts. Take them only from pages of that site that you opened.

| Fact | Value |
|---|---|
| How to get on it | One sentence with the real mechanism of this site: claim a listing, apply, pitch the editor, earn reviews, or take part |
| What decides the order | A short phrase, or "not clear" |
| Cost | Free, paid, or unknown |
| Where to start | The address on that site where a business starts: a sign-up page, a "list your business" page, or the editor's published contact. Or "none found" |

Never guess a contact address. Never suggest fake reviews, paid links, or keywords added to a business name.

## 6. Save the map

Save a spreadsheet file, `source-map-<date>.csv`, with one row for each page:

Page, Site, Type, Count, Business (Present, Not present, Check needed, or Not opened), Rivals On Page, How To Get On It, What Decides The Order, Cost, Where To Start, Next Skill.

Sort the rows by Count. Put Check needed rows after the others, and Not opened rows last.

## Rules

- Give each count with its source: answers, or web-search results.
- Do not promise that a listing earns a mention. A page on the map is a bet that the data supports.
- Contact nobody from this skill. Outreach has its own approval rules in the `ai-listing-outreach` skill.
- Refresh the map each quarter, or after a new `mention-check`.

## Output

1. The source that you used, the market, and the date.
2. The spreadsheet file. If you cannot make a file, return the table as CSV.
3. The three pages to work on first, each with its type, its count, and its skill.
4. The pages that need a check by the person, and the number of pages that you did not open.
