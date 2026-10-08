---
name: competitor-share-of-voice
description: Show which competitors and which source websites appear in the AI answers a Radarkit project tracks, as share of voice and citation counts, and where the brand ranks against them. Use when the user asks who they are losing to in AI answers, which competitors show up most, which sites AI models cite, or where they should try to get mentioned.
---

Use this skill when the user asks about competitors, share of voice, citations, sources, or rankings in AI answers.

1. Call `list_projects` and pick the project (ask if there are several and none was named).
2. Default the window to the last 30 days. Row-level tools accept at most 31 days per call;
   aggregates accept more.
3. For competitors, call `get_competitors`. It returns the brand's own share and every
   competitor's share of mentions with an average position.
4. For the websites AI answers rely on, call `top_source_domains`. `cited` tells how often a
   domain was actually cited rather than only consulted.
5. For a specific competitor or domain, call `list_rankings` with `domain` to see the exact
   answers and positions, or `list_sources` with `domain` for the exact pages.
6. Report the brand's share first, then the top five competitors with their share, then the
   top five source domains with citation counts. Point out the biggest gap and one concrete
   opportunity, for example a domain that is cited often where the brand has no page.

Do not present share of voice as a percentage of all AI traffic; it is the share of mentions
inside the answers this project tracks. Do not merge domains that differ only by subdomain.
Do not page through more than two pages of rows without asking; for bulk analysis hand off to
the export-answers skill.
