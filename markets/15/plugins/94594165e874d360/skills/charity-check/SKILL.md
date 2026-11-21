---
name: charity-check
description: Look up US nonprofits with search_nonprofits, get_nonprofit_profile and compare_nonprofits, using live IRS Form 990 data from ProPublica Nonprofit Explorer, with PDF, CSV and Excel reports.
---

# Zovo Charity Lookup

Use `search_nonprofits` when the user names an organization but has no EIN. Pass `name` (up to 100 characters), and optionally `state` as a 2-letter US postal code and `category` (an NTEE major group). Show the matches with their EINs and ask which one the user means when several fit.

Use `get_nonprofit_profile` with one `ein` (9 digits, e.g. `53-0196605`) for the IRS exemption facts, the multi-year Form 990 table, year-over-year change, ratios with their formulas, filing PDF links and the PDF, CSV and Excel report.

Use `compare_nonprofits` with 2 to 5 `eins` to put the latest filing of each organization side by side. Say when the latest tax periods differ (the figures then do not cover the same 12 months).

Report the figures, the tax period and the form for each number, and the formulas for ratios. Do not call an organization good, bad, efficient or trustworthy; these tools give facts, not ratings. The IRS extract has no program-service expense split, so no program expense ratio is computed. For revocations and current exemption status, point to IRS Tax Exempt Organization Search. Always include the source line (ProPublica Nonprofit Explorer, IRS Form 990 data) with its retrieval time, and say that download links expire in about 1 hour. If the result marks a "missing year" (a filing on file whose figures the source has not extracted yet, newer or inside the history), tell the user that year is missing from the source and give the filing PDF link; do not present figures from elsewhere as part of the report. When a search says "10,000 or more" matches, the source stops counting there; suggest a state or category. If the source does not answer, say so; do not estimate figures.
