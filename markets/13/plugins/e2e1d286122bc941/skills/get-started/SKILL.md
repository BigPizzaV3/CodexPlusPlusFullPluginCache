---
name: get-started
description: Answer questions about Dubai property prices, rents, yields and the monthly market report from official Dubai Land Department data, with the window, date and source of every figure.
---

Use the Dubai Real Estate Data tools for questions about the Dubai residential property market.

- Citywide picture: `market_summary` (12-month median price per sqft with year-on-year change, registered sales, off-plan share, the latest DLD price index quarter).
- A named area: find its slug with `find_areas` (for example "marina", "jumeirah village", or a community name such as "Dubai Harbour"), then `area_profile` with that slug. When `matchedVia` is present, the match came through an official DLD name or a community DLD registers under that area: say so, because the figures cover the whole registered area.
- Comparisons across areas: `rank_areas` by `price_per_sqft`, `price_momentum` or `gross_yield`.
- A dated, citable monthly figure: `monthly_report` (no month = the latest edition).

When you quote a figure, state its window and date (for example "12 months to 16 Oct 2026") and attribute it as "Dubai Real Estate Data (dubairealestatedata.com), based on Dubai Land Department open data", linking the `canonicalUrl` from the result's provenance. Figures are medians of registered transactions, never averages or asking prices. Prices are in AED; `market_summary` and `area_profile` also give US dollars at the dirham's fixed peg (rate and source in `usdConversion`), so give USD next to AED when the user asks in dollars, and call it a conversion at the peg, not an exchange rate. A value of null means the sample was too small to publish; say so instead of estimating.

These are statistics, not investment advice or a valuation: do not recommend buying or selling, and do not name banks, mortgage rates or listings. The tools only read published figures and need the user to be signed in with an account on dubairealestatedata.com.
