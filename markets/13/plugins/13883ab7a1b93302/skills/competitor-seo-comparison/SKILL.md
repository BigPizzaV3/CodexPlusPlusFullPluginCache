---
name: competitor-seo-comparison
description: Compare the SEO of two websites or two pages side by side with DidYouSEO - audit score, technical issues, titles and descriptions, structured data and backlink strength - and say what to fix to close the gap. Use when the user asks to compare their site with a competitor, why a competitor outranks them, or to compare SEO of two websites. Requires the DidYouSEO MCP connector.
---

# Competitor SEO comparison

Put two pages through the same checks at the same time, then say where the competitor is ahead and what closes the gap.

## Tools

- `run_seo_audit` (url) - score out of 100 and issues for one page.
- `analyze_meta_tags` (url) - title, description, headings and canonical.
- `validate_schema` (url) - structured data found and its errors.
- `get_backlink_summary` (domain) - domain rank, backlinks and referring domains. Uses 1 AI credit per domain.

## Steps

1. Get two URLs of the same kind: both homepages, or both pages targeting the same search. If the user gives two domains, compare their homepages and say so.
2. If a competitor is a big national brand and the user is a small or local business, say that the comparison will mostly show the gap in size. Suggest a competitor of similar size as well.
3. Call `run_seo_audit` on both URLs.
4. Call `analyze_meta_tags` and `validate_schema` on both.
5. Ask before calling `get_backlink_summary`: it uses 1 AI credit per domain, 2 in total. If the user agrees, call it for both domains.
6. Compare:
   - score and critical issues
   - title and description: which one matches the search better
   - headings: topics the competitor covers that the user doesn't
   - structured data: types present on one side only
   - backlinks: domain rank and referring domains, if fetched
7. Separate what the user can fix this week (on-page) from what takes months (links).

## Output format

A side-by-side table: check, user's page, competitor's page, who's ahead. Then "Close the gap": up to 5 actions, quickest first, each with the exact change.

## Limits

- This uses 6 page checks (two audits, two meta tag checks, two schema checks). On the Free plan there are 10 a day. If a tool says "Daily limit reached", stop, tell the user the limit resets at 00:00 UTC, and compare what you have.
- Backlink lookups need AI credits. If the tool says there are none left, skip backlinks and say so.
- Don't mention prices or upgrades. If the user asks how to get more, say plan details are on didyouseo.com.
