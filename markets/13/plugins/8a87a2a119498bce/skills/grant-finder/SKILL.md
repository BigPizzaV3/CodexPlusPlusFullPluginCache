---
name: grant-finder
description: Find live federal grant opportunities by keyword, eligibility, agency and dates, or read batches of opportunity details; return an XLSX pipeline tracker and an ICS grant deadline calendar.
---

# Zovo Grant Finder

Use `find_grant_opportunities` for open or forecasted federal grant opportunities. Supply a keyword or at least one eligibility, agency, category, posted-within-days or closing-before filter. For example, use `eligibility: ["nonprofit_501c3"]` and `categories: ["ED"]` for nonprofit education grants. Use `match_all_words: true` to require the keyword words together. Department codes such as HHS include sub-agencies. Eligibility searches also include unrestricted notices.

Use `show_grant_details` for a list of up to 20 opportunity numbers or numeric IDs, for example `["2026-NTIA-TBCP", "359145"]`. Duplicate inputs are processed once. Closed and archived notices can appear in details but do not receive calendar events.

Report the shown and matched counts, source retrieval time and per-item errors. Share the XLSX pipeline tracker and the ICS deadline calendar links when present; links expire in about an hour. Search results are limited to 30 rows per page. When more rows exist, use the next page with the same filters. Searches over the upstream cap screen the first thousand rows only.

Dates use America/New_York for today. Forecasted dates are estimates. Check the notice for the deadline time and time zone. Missing award amounts mean not stated. The calendar omits undated and expired notices and reminders whose dates have passed.

Do not use these tools for private foundation, state or local grants, application writing, submitting applications or guaranteed eligibility decisions.
