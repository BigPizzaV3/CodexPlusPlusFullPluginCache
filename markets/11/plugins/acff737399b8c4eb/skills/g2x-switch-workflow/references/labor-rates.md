# Labor rates

One tool, three modes. Rates are published hourly ceiling rates, not prices a buyer paid and not a winning price. Say which category, filters and mode produced a number. Do not average ceiling rates into a bid price without saying what they are.

### `g2x_labor_rates`

Find published hourly ceiling rates by labor category, by company, or as statistics for one exact category.

- Inputs: `mode` (required: `search`, `company` or `statistics`). For `search`: `query` (words from the labor category) and or `filters`. For `company`: `company_uei` (required), optional `labor_category`, `education_level`, `security_clearance`, `sort_direction` (`desc` by default, or `asc`). For `statistics`: `labor_category` (required, the exact category) and optional `filters`. Filters take `company_uei`, `vehicle_piid`, `schedule`, `sin`, `education_level`, `security_clearance`, `worksite`, `minimum_years_experience_gte`, `minimum_years_experience_lte`, `current_price_usd_hour_gte` and `current_price_usd_hour_lte`. `search` and `company` take `page` and `page_size`; `search` also takes `preference` (`hybrid` by default, or `sparse`). Fields from another mode are refused.
- Output: rate rows ranked by how closely the category matches the words; `exact_category` marks an exact normalized match. When a next cursor is present, use its number as `page` with the same other arguments. When `capped` is true, the total is a lower bound or unavailable, not the complete count. Statistics returns the minimum, median, maximum and mode for one exact category and its filters, with the sample count; prices are rounded to cents.
- Plan: available to members whose G2X account includes published labor rates, and only for a member the account policy admits. Read only. On the research endpoint: yes, when the account is admitted.
- Example: `{"mode": "search", "query": "senior systems engineer"}` and `{"mode": "statistics", "labor_category": "Systems Engineer"}`

If this tool is not in the connected tool list, say that published labor-rate lookup is unavailable in this connection. Tool absence alone does not establish a missing account entitlement; upstream availability, discovery or policy lookup may also affect tool registration. Explain an entitlement restriction only when an actual account-policy result establishes it. Follow supported connection recovery where appropriate. Offer award data as separate market context only if useful to the user; never present it as labor rates.
