---
name: google-news-research
description: Find Google News coverage, recent headlines or articles about a topic or company with HasData. Use for news discovery, not ordinary organic rankings or claiming to have read full articles.
---

# Find news coverage

Read `../hasdata-research/SKILL.md` and the Search sources section of `../hasdata-research/references/tool-catalog.md`.

Call `hasdata_google_serp_news_getGoogleNews` with q for a topic search. Reuse a topicToken, publicationToken, storyToken or sectionToken only when it actually came from corresponding returned News data. Preserve requested country and language. Do not invent a date filter the schema does not expose.

Return relevant titles, original article URLs, publishers and returned publication times. For a requested date range, inspect those times and explain missing or relative dates rather than claiming a server-side cutoff. Deduplicate identical article URLs; syndicated copies are not necessarily independent reporting.

Separate what the headline and snippet say from facts verified in an article. Read a selected public article through `../public-web-extraction/SKILL.md` only when needed within the budget. No automatic crawl of all results. A bounded News page is not complete media coverage.
