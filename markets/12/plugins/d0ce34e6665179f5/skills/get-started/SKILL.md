---
name: get-started
description: Quick start for Dados B3, a read-only source of Brazilian market data (B3 and CVM) - company dividends, indicators, multiples and statements, stock and index performance, real estate funds (FIIs), ETFs, BDRs, dated lists, material facts and public data such as Treasury bond rates. Use when the user asks about listed Brazilian companies, tickers such as PETR4, VALE3, WEGE3 or HGLG11, the Ibovespa, or wants to know what Dados B3 can do.
---

# Getting started with Dados B3

Dados B3 is a read-only data connector for the Brazilian market (B3). It reports what happened in the past. It does not recommend purchases or sales, does not quote real-time prices, and does not place orders.

## What you can ask

Companies listed on B3:
- Dividends and interest on equity per share, with a yearly summary and the 12-month dividend yield (tool `get_dividends`).
- Performance of a stock over a period (default: last 5 years): price return, total return with dividends reinvested, maximum drawdown, volatility, plus a moving-average crossover for comparison. No costs or taxes (tool `get_stock_performance`). What BRL 1,000 became over 1, 3, 5 and 10 years against the Ibovespa and Selic (`get_growth_of_1000`).
- A plain-language summary of a company's latest year in six numbers: does it make money (net margin, ROIC), is it indebted (net debt/EBITDA), is it expensive against its sector and its own history (P/E, P/B), with a green/yellow/red confidence flag (tool `get_company_verdict`).
- Yearly indicators such as ROIC, ROE, margins, growth and net debt/EBITDA (`get_annual_indicators`), point-in-time valuation multiples (`get_valuation_multiples`) and the standardized annual or quarterly statements with the CVM account of each number (`get_financial_statements`).
- Material facts and market notices filed at CVM, with the link to the original document (`get_material_facts`), and the companies that left the exchange by year (`list_delisted_companies`).
- The list of listed companies (`list_companies`) and listed bank indicators from the Central Bank: Basel ratio, overdue loans, loan book (`get_bank_indicators`).

Funds, indices and lists:
- Real estate funds (FIIs): the profile of any fund (`get_real_estate_fund`) and rankings by P/B and 12-month yield (`get_real_estate_fund_rankings`).
- Performance of a B3 index such as IBOV, IFIX, SMLL or IDIV, useful as a benchmark (tools `get_index_performance`, `list_indices`).
- ETF rankings by volume, size, premium or discount to NAV, 12-month return and expense ratio (`get_etf_rankings`), and BDRs that traded in the last year, filterable by type (`list_bdrs`).
- Ready-made dated lists: highest dividend yield, P/E below 10, highest-yield FIIs, each with its criterion and base date (`get_dated_lists`).
- Investment funds registered at CVM: largest funds, inflows and outflows, one fund's monthly series (`get_investment_funds`).

Public data:
- Treasury bond rates and prices (Tesouro Direto), today or as a daily series (`get_treasury_bonds`).
- Oil and gas production by operator and field (`get_oil_gas_production`), residential electricity tariffs by distributor (`get_electricity_tariffs`) and mobile and broadband connections by operator (`get_telecom_connections`).

About the data:
- What changed in the market in the last 30 days: filings, re-filed statements, approved dividends, fund distributions, splits and ticker changes (`get_market_today`); and how current the data is (`get_data_coverage`).
- The method, the data dictionary and a reproducible audit sample (`get_methodology`, `get_data_dictionary`, `audit_sample`).

## How to answer

1. Resolve the ticker the user means (for example PETR4, VALE3, WEGE3). If unsure, call `list_companies`. Real estate funds end in 11 (for example HGLG11) and use the fund tools.
2. Call the most specific tool. Prefer one call per question; for a ranking, use `get_dated_lists` instead of calling a tool once per company.
3. Quote the figures as returned and keep the `source_url`, the source and the data version that come with the result.
4. Respect the flags in the data. A `flag` value explains a limitation, such as a missing comparison year. Say so instead of filling the gap.
5. If a tool returns an error, tell the user plainly what it says. Never invent a value for an unknown ticker.

## Limits to state when relevant

- Everything is historical and informational. It is not investment advice.
- Prices are end of day, never intraday.
- Valuation multiples use the price of the first trading session on or after the date the filing became public, so there is no look-ahead.
- Sources: CVM open data (ODbL) and B3 end-of-day files, plus the National Treasury, the Central Bank, ANP, ANEEL and Anatel open data for their own topics. Full method: https://dadosb3.com/metodologia
