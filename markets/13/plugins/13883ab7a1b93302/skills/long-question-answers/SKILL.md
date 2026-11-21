---
name: long-question-answers
description: Find the long, specific questions people search before they reach a site (8+ word and question-word queries in Google Search Console) and draft a short direct answer for the page that already ranks. Use when the user asks what questions people search, what to write next, how to get cited in AI answers or Google AI Overviews, or wants answer-engine (AEO) ideas from their own data. Requires the DidYouSEO MCP connector with Search Console connected.
---

# Long questions to answers

Long queries are the same questions people ask ChatGPT. When a page shows for one but gets no clicks, a short direct answer at the top of that page is usually the fastest fix.

## Tools

- `get_search_console_keywords` (website, days=90) - queries with clicks, impressions, CTR and average position.
- `analyze_meta_tags` (url) - title, description and headings of the page you will change.

## Steps

1. Call `get_search_console_keywords` with `days: 90`.
2. Keep two kinds of query:
   - 8 or more words (regex `^(?:\S+\s+){7,}\S+$`)
   - starting with a question word: how, what, why, when, which, who, where, can, does, do, is, are, should, will
3. Drop branded queries and junk such as `keyword-xxxx` or queries that are mostly another site's domain name.
4. Group near-duplicates into one cluster ("how to find keywords on a web page", "how do i search keywords on web page"). Sum impressions and clicks per cluster.
5. Rank clusters by impressions where clicks are 0 or CTR is under 1%. Take the top 5.
6. Note any query that starts with `context:` or contains `question:`. Those are AI assistants searching on someone's behalf. Report them separately; they show what AI tools look you up for.
7. The keyword tool does not say which page ranks. For each cluster, name the most likely page and ask the user to confirm it in Search Console (Performance, click the query, then the Pages tab). Call `analyze_meta_tags` on the confirmed page.
8. For each cluster, draft:
   - a 40-60 word answer that starts by restating the question and answers it in the first sentence, to go first on the page
   - one FAQ question in the searchers' exact words, with a 2-3 sentence answer
9. Never suggest a new page when an existing page already shows for the cluster.

## Output format

A table: cluster, example query, impressions, clicks, average position, page. Then the drafted answer and FAQ entry for each of the top 5. Then the AI-assistant searches, if any.

End with: "Add the answer as the first paragraph, update the page's date, and re-check the cluster in 3 weeks."

## Limits

- On the Free plan the Search Console tool returns a short preview. Work with what it returns and say the list may be incomplete.
- If a tool says "Daily limit reached", stop calling page tools, tell the user the limit resets at 00:00 UTC, and finish with the data you have.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
