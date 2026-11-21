---
name: low-ctr-title-fix
description: Find pages that already rank in Google's top 7 but get few clicks, and rewrite their title and meta description to earn the click. Use when the user asks why a page ranks but gets no traffic, how to improve click-through rate (CTR), or wants better titles and descriptions from real Search Console data. Requires the DidYouSEO MCP connector with Search Console connected.
---

# Low CTR title fix

A page in the top 7 with a CTR under 2% doesn't need better rankings. Its title and description aren't winning the click.

## Tools

- `get_search_console_keywords` (website, days=28) - queries with clicks, impressions, CTR and average position.
- `analyze_meta_tags` (url) - the current title and meta description.
- `serp_preview` (url) - how the snippet looks in Google now.

## Steps

1. Call `get_search_console_keywords` with `days: 28`.
2. Keep queries with average position 1 to 7, at least 30 impressions, and CTR under 2%.
3. Drop branded queries. Low CTR on a brand query usually means sitelinks or a knowledge panel take the click, not a weak title.
4. Group queries that belong to the same page. Rank groups by impressions. Take the top 5.
5. The keyword tool does not say which page ranks. Name the most likely page and ask the user to confirm it in Search Console (Performance, click the query, then the Pages tab).
6. For each confirmed page, call `analyze_meta_tags` and `serp_preview`.
7. Write two title options and one description per page:
   - use the searchers' words from step 2, not the site's internal name for the thing
   - put the main query in the first half of the title
   - title: 48 characters or fewer before the brand suffix, so the whole title stays under about 60
   - description: 120-155 characters, says what the reader gets and why this page over the others
   - promise only what the page delivers
8. Don't change titles on pages the user says are in a running test.

## Output format

For each page: the queries, position, CTR, current title and description, then the new options. Mark your preferred title.

End with: "Change one page at a time if you can, and compare CTR for the 4 weeks after with the 4 weeks before."

## Limits

- `analyze_meta_tags` and `serp_preview` count as page checks. On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop, tell the user the limit resets at 00:00 UTC, and finish with what you have.
- On the Free plan the Search Console tool returns a short preview. Say the list may be incomplete.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
