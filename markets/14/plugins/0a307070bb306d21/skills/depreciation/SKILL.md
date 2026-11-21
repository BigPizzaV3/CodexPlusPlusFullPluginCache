---
name: depreciation
description: Build depreciation schedules (straight-line, declining balance, sum-of-the-years' digits, units of production, MACRS from IRS Pub 946 tables) for one asset with calculate_depreciation or many assets with generate_depreciation_schedule, with PDF, Excel and CSV downloads.
---

# Zovo Depreciation Schedule

Use `calculate_depreciation` for one asset and `generate_depreciation_schedule` for two or more assets, a pasted fixed-asset list, or an attached CSV/Excel file.

1. Call right away when the cost is known. Pass what the user said and leave the rest out; the tool applies stated defaults (straight-line, 5-year life, January of this year, MACRS 7-year for property with no class, MACRS 27.5-year for a rental house).
2. Method words map directly: "MACRS", "tax" or "IRS" -> `macrs`; "double declining" -> `double_declining`; "150%" -> `150db`; "SYD" -> `sum_of_years`; miles or machine hours -> `units_of_production` with `units_total` and `units_per_year`.
3. For MACRS pass `property_class` (3, 5, 7, 10, 15, 20, 27.5 or 39) or a descriptive `name` such as "rental house" or "laptop". Leave `convention` out for several assets so the 40% mid-quarter test decides.
4. For a building, the cost must exclude land. If the user gives a purchase price with land, ask for or subtract the land value first.
5. After the tool returns, give the first-year depreciation, the total, notable assumptions and warnings verbatim, and the PDF, Excel and CSV links (they expire in 24 hours). Say it is informational, not tax advice.

Do not use this skill for Section 179 or bonus depreciation limits, tax strategy advice, or the market resale value of a car or other item.
