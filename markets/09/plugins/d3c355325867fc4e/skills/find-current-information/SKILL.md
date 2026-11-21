---
name: find-current-information
description: Find and read current public information on the web, then answer with sources. Use when the user asks about recent events, news, releases or facts that change over time and does not give a specific URL.
---

Use this skill when the answer depends on information that may have changed recently and the user has not pointed at a specific page.

1. Call `search` with a short, specific `query` built from the user's request. Keep the default `limit` unless the user asks for more results.
2. Read the titles and snippets. Pick the results that actually address the question, and prefer primary sources such as the organisation's own site, official announcements and reputable outlets.
3. When snippets are not enough to answer, call `scrape` on the two or three most relevant results rather than all of them. Alternatively set `scrapeResults` to true on the search when every result needs reading.
4. Answer from what the pages say, and cite each source URL next to the claim it supports.

When results are weak:

- If the search returns nothing relevant, say so and suggest a narrower or differently worded query instead of answering from memory.
- If sources disagree, say that they disagree and show both, with links.
- If the search fails, tell the user it failed. Do not present older knowledge as current.

Do not:

- Make claims without a source you actually read in this conversation.
- Pad an answer with results that do not address the question.

The user's explicit instructions take priority over this skill.
