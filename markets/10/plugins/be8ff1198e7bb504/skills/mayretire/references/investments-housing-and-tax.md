# Investments, housing, and tax

Use `inspect_plan_payload` and `describe` before interpreting return, property,
or tax settings. Preserve ownership, fees, conversion rules, and enabled flags
while testing another assumption.

For main accounts, `returnMethod = 0` uses nominal price appreciation plus
distribution yield; `returnMethod = 1` uses asset allocations. The stored
`realInvestmentReturn` is a legacy manual-return fallback, not an active main
account return under allocation mode. Do not call projections too optimistic
merely because this dormant value differs. Additional `investmentPortfolios`
items have independent `returnMode` settings and may have separate ownership,
fees, conversion ages, or locked-in jurisdictions. A manual portfolio's
`manualPriceReturn` and `manualDistributionYield` are nominal inputs.
`marketSensitivity` scales market-sequence variation around the configured
return; historical backtesting does not replace that return with raw market
performance. Inspect the active mode before comparing alternatives.

When `hasPrincipalResidence` is false, stored house details are dormant. Do
not describe them as active assets or planned sales. Even with a residence,
`dispositionMode: keep` makes stored sale year and replacement value dormant.
For a requested sale or downsizing, confirm timing, costs, replacement value,
linked debt payoff, and estate scope. Compare keeping, selling, and downsizing
as separate scenarios using bounded housing and balance views. For other debt,
confirm owner, interest, repayment and estate treatment; for insurance, confirm
premiums, insured person, duration, and benefits. Do not infer a sale is needed
from one failed stress case.

Use `totalLifetimeTax` from the summary for cumulative lifetime tax. Do not sum
cumulative annual `totalTax` rows. For timing, inspect bounded annual rows and
distinguish annual from cumulative fields. MayRetire tax inputs can have mixed
data vintages; do not assign one generic tax year to the entire calculation.
Report the modeled result and material assumptions, and avoid presenting it as
personalized tax advice.
