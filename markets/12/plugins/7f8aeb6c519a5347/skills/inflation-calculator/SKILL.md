---
name: inflation-calculator
description: Adjust a US dollar amount between two years or months with the published CPI-U index, or build a year-by-year CPI and inflation table with a CSV download, using the adjust_for_inflation and inflation_table tools.
---

# Zovo Inflation Calculator

Use `adjust_for_inflation` to convert one US dollar amount between two periods, and `inflation_table` to show the annual CPI average and yearly inflation across many years.

1. `adjust_for_inflation`: pass `amount` (US dollars, e.g. 100 or 1234.56), plus `from` and `to` periods. A period is a year such as `1990` (the published annual average) or a year and month such as `1990-06`. The data covers 1913-01 to the latest published month. When the user gives a month name, convert it to a number (`January 2000` becomes `2000-01`).
2. `inflation_table`: pass integer `start_year` and `end_year` (1913 or later, up to 120 years apart, not after the latest full year). It returns the annual average CPI and the yearly inflation rate, plus a CSV download.
3. Read the numbers from the tool result and quote them, including the two CPI values, the cumulative inflation, the average annual rate, and the buying-power change. Do not estimate values yourself.
4. If the user's year is the current incomplete year, use a month up to the latest published month, or an earlier full year; the tool names the latest available period in its error message.

Limits: US CPI-U only (series CUUR0000SA0, 1982-84=100). No other countries, no regional or core CPI, no seasonally adjusted series, and no forecasts. Not financial advice.

Fractional cents are accepted for any positive amount up to one trillion dollars. Only the adjusted output is rounded to cents, with half-even rounding. If a monthly CPI value is unavailable, choose another published month or an annual average.
