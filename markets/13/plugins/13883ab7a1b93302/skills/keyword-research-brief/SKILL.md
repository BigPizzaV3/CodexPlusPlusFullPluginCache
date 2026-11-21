---
name: keyword-research-brief
description: Find keywords a page can realistically rank for from a seed phrase, using real search volume and keyword difficulty, then write a short content brief for the best one. Use when the user asks for keyword ideas, low-competition keywords, what to write about, or a brief for a new page or post. Requires the DidYouSEO MCP connector and AI credits.
---

# Keyword research to brief

Turn one seed phrase into a short list of winnable keywords and a brief the user can write from today.

## Tools

- `get_keyword_ideas` (seed) - up to 50 keyword ideas containing the seed, with search volume and keyword difficulty. 1 AI credit.
- `get_keyword_data` (keywords, 1-10) - volume, difficulty, CPC and search intent for chosen keywords. 1 AI credit per call.
- `get_search_console_keywords` (website) - optional: what the site already ranks for, so you don't target it twice.

## Steps

1. Get the seed phrase and the site. Tell the user this uses 2 AI credits before you start.
2. Call `get_keyword_ideas` with the seed.
3. Shortlist up to 10 ideas:
   - keyword difficulty 30 or lower for a newer or smaller site; up to 50 for an established one
   - volume above zero
   - clear intent that matches what the site offers
4. Call `get_keyword_data` on the shortlist for intent and CPC. A higher CPC usually means a buyer is searching.
5. If Search Console is connected, call `get_search_console_keywords`. Drop any keyword an existing page already shows for, and recommend improving that page instead.
6. Pick one main keyword and 3-5 close variants for the same page.
7. Write the brief:
   - title (48 characters or fewer before the brand suffix) and meta description (120-155 characters)
   - the question the page answers, in one sentence, to answer in the first paragraph
   - 5-8 H2 headings, using the variants and the questions people ask
   - what to include that a reader can't get elsewhere: data, a worked example, a template
   - 2-3 existing pages on the site to link from

## Output format

A table of the shortlist: keyword, volume, difficulty, intent, CPC, pick. Then the brief.

## Limits

- Both keyword tools need AI credits. If a tool says there are none left, say so and stop. Don't guess volumes.
- Keyword data covers Google in the US by default. Say so if the user's market is elsewhere.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
