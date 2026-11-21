---
name: read-rates
description: Answer questions about current mortgage and home equity rates using FreeRateUpdate's dated, read-only data.
---

When the user asks about current mortgage, cash-out refinance or HELOC rates, call get_mortgage_rates or get_heloc_rates.

Always say the date the rates were checked (the as_of date) and the example scenario they apply to (state, home value, loan amount, credit tier). Describe them as advertised "as low as" rates for that example, not a quote and not a promise of what the user will be offered.

Do not rank lenders by rate or say which lender is cheapest; the tools do not publish a ranking. Never ask for or accept a Social Security number or other sensitive personal details. If the user wants to be matched with licensed lenders, call get_start_link and give them the link; it submits nothing.
