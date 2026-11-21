---
name: sec-filings
description: Read reported US public-company financials and the latest filings straight from the SEC's EDGAR data with get_company_financials and find_latest_filings, including CSV and XLSX downloads.
---

# Zovo SEC Filings

Use `get_company_financials` for reported figures and `find_latest_filings` for the filing list.

1. Give the company as a ticker (`AAPL`) or a name (`Apple`). Prefer the ticker; a common name can match several companies and returns candidates to choose from.
2. `get_company_financials`: pass `period` = `annual` (default) or `quarterly`, and `years` 1 to 10 (default 5). It returns revenue, net income, total assets, liabilities, cash, operating cash flow and diluted EPS per period, with the filing form and date for each value, year-over-year growth for revenue and net income, and CSV/XLSX download links.
3. `find_latest_filings`: pass `forms` (a subset of `10-K`, `10-Q`, `8-K`, `S-1`, `DEF 14A`, `20-F`; default `10-K`, `10-Q`, `8-K`) and `limit` 1 to 40 (default 12). It returns the newest filings first with report dates and links to sec.gov.
4. Report the key numbers from the text result, name the source and retrieval time, and share the download links. Say "not reported" when a value is missing; do not estimate it.

Values are as reported in XBRL to the SEC and are not adjusted or audited. Do not use this skill for share prices, forecasts, or investment advice, and it only covers US public companies in the SEC index.
