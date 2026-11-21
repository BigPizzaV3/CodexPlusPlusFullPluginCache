---
name: citation-sources
description: Show which websites and pages AI assistants cite when they answer questions a brand monitors in 3RD, and how much of that is the brand's own site. Use when the user asks which sources, domains or pages the assistants rely on or cite.
---

Use this skill for questions about the sources behind AI answers.

1. Call `list_brands` and take the `brandId`. Ask which brand if there are several and the user named none.
2. Call `get_citation_sources` with the `brandId`. Useful arguments:
   - `fromDate` / `toDate` (YYYY-MM-DD) for a period; the default is the last 30 days;
   - `kind` to keep only `owned` or `earned` sources;
   - `domain` to keep one website;
   - `promptType` to keep one prompt category (must-win, core, foundation);
   - `limit` and `page` to walk a long list. The result says how many pages there are.
3. For the brand's own share by assistant, call `get_attribution_share` for the same period.
4. Answer with the top sources: URL, citation count, share, owned or earned, and whether the page mentions the brand. Say which period and which filters the list reflects.

Report counts and shares exactly as returned. A source being cited is not the same as it recommending the brand; only say a page mentions the brand when the result says so.
