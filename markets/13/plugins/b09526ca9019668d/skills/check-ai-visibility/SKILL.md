---
name: check-ai-visibility
description: Report how often AI answers and AI search results mention or cite a site in Sight AI, broken down by assistant, how that is trending, and which content would help. Use when the user asks about AI visibility, AI search, brand mentions in AI answers, or AI citations.
---

Use this skill when the user asks how their brand shows up in AI answers. All of these tools read data; none needs confirmation.

## Pick the site

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.

## Read the data

2. Call `get_ai_visibility_summary` with the window in `days` for the headline numbers: how many tracked prompts named the brand or cited the site, by platform.
3. Call `get_ai_visibility_trends` for the same window to show the direction over time.
4. Call `get_ai_visibility_mentions` for the breakdown by AI model and `get_ai_visibility_citations` for the pages AI assistants cite, with their stats.
5. Call `get_ai_visibility_competitors` to compare against the configured competitors.
6. For Google specifically, call `get_seo_ai_mode` for AI Mode results per tracked prompt: cited or not, the citation position, the cited URLs and citations lost since the previous check.
7. For what to write next, call `list_opportunities` with `source` set to `ai`: content opportunities built from prompts where the brand is absent.

## Presenting results

- Distinguish "mentioned" (the brand is named in the answer) from "cited" (the site is linked as a source). Report both with the window and the platform.
- Use the tools' percentages and counts as returned. If tracking started recently, say so instead of describing a trend.
- When a competitor is cited for prompts the site is not, point at the opportunity rows that cover those prompts.

## Do not

- Do not run AI checks yourself or ask other tools to query AI models; Sight AI tracks the prompts on a schedule and these tools report the results.
- Do not add or edit tracked prompts from here; that is done in the Sight AI app.
