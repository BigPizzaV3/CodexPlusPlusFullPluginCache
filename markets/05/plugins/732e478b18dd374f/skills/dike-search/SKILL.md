---
name: dike-search
description: Find and compare primary legal sources on a topic using Dike. Use when the user wants to browse or list relevant laws, regulations, court rulings, or fatawa from Saudi Arabia, the UAE, Qatar, Kuwait, or Egypt, or names a law or topic without a precise number and year. Do not use it to answer a legal question; use dike-research for that.
---

Use this skill when the user wants to find, browse, or compare legal sources rather than receive a single answer. Queries can be in Arabic or English.

1. Call `dike_search` with the user's query. If the user names a jurisdiction (SA, AE, QA, KW, EG), a document type (legislation, case_law, fatwa, regulation, decree), a year range, or a status, pass it as a filter. If the results could span several countries with materially different law and the user has not said which one they mean, ask before filtering. Do not pick one silently.
2. Present the results as a short list. For each result give the title, the `citation_string`, and a one-line summary of the snippet.
3. Do not draw legal conclusions here. If the user then wants an answer to a question, use dike-research.

Only report titles, numbers, and citations that the tool returned. If nothing matches, say so and suggest a broader or differently worded query.

If the user's explicit instructions conflict with this skill, follow the user.
