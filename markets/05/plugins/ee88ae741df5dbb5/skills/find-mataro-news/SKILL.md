---
name: find-mataro-news
description: Find source-attributed local news about Mataró and direct impacts from the Maresme, including transport and public services. Use for recent developments, a specific local topic, or details of a published article.
---

# Find Mataró news

Use Mataró.fm's `search_news` and `get_news` tools for local news. Search with the user's key terms; an empty `search_news` query returns the latest published articles. Read an article with `get_news` before giving detailed claims that are not in its summary.

For a list, make each article title the single link to its public Mataró.fm page. Do not append the original source name or link to every item; the article page already shows its sources. In a detailed answer, link the article once and name or link the original sources when the user asks or when needed to clarify a claim. Distinguish `published_at` from `updated_at`; a newly updated article may cover an older event. If the user asks about a time period, check dates before describing results as current. Keep uncertainty from the article. If no match is found, say so and optionally try one broader query.

Do not infer that an event did not happen simply because Mataró.fm has no article. Do not turn a live transport observation into a published news claim; use `get_live_data` for current service conditions.
