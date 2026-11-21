---
name: country-data
description: Compare countries on World Bank World Development Indicators (GDP, GDP per capita PPP, inflation, population, unemployment, CO2, life expectancy and more) with compare_countries, rank_countries and search_indicators, then download Excel, CSV and PDF files with citations.
---

# Zovo Country Data

Use `compare_countries` when the user wants 2 to 12 countries side by side on 1 to 4 indicators over years. Pass `countries` as ISO 3-letter codes or World Bank names (for example `["DEU", "FRA"]`), `indicators` as codes or common names (for example `["NY.GDP.PCAP.PP.CD"]` or `["inflation"]`), and optional `start_year` / `end_year`.

Use `rank_countries` for "which countries have the highest/lowest ..." questions. Pass one `indicator`, an optional `year`, an optional `region` (EAS, ECS, LCN, MEA, NAC, SAS, SSF) or `income_group` (LIC, LMC, UMC, HIC), `order` and `limit`. Leave `year` out to get the latest year with broad coverage.

Use `search_indicators` when the user names a measure that is not one of the common ones and you need its code.

Report the latest value together with its year for each country, because recent years are often not published yet. Say which years have no data; do not estimate them. Quote the source line (World Bank, World Development Indicators, CC BY 4.0, retrieval time in UTC) and give the download links, which expire in about one hour.

If a country is ambiguous (Congo, Korea) or not covered (Taiwan, England), relay the tool's message and ask which one the user means. Do not use these tools for forecasts, currency conversion or sub-national data.
