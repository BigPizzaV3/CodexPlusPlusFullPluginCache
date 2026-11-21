---
name: monitly-statistics
description: Answer questions about official economic and social statistics (GDP, inflation, unemployment, wages, trade, debt, population, health, energy) for 150+ countries with sourced numbers from the Monitly MCP server.
---

# Official statistics with Monitly

Use the Monitly tools whenever the user asks for an official statistic, a comparison between countries, or a trend over time.

## Workflow

1. `search_catalog` with a short topic query (for example "unemployment rate", "HICP inflation", "GDP per capita PPP"). Pass `country` when the question is about one country and `source_name` if the user names a source (Eurostat, OECD, World Bank, IMF, WHO).
2. Pick the dataset whose name and source best match the question. Prefer the most recent `latest_period`.
3. `inspect_dataset` with the dataset id and country to confirm the country is covered and to see the dimension values of the default series and its latest values.
4. `get_series` for the values. Use `period_from` to limit long series, and dimension values from step 3 when the user needs a specific unit or breakdown.

## Answering

- Give the number with its unit and period, then name the source and dataset, for example "Unemployment rate, Poland: 2.9% (2025, Eurostat, Unemployment by sex and age)".
- For comparisons, use the same dataset for every country so the figures are comparable.
- If no dataset covers the question, say so and suggest the closest available dataset. Do not estimate or invent values.
- Link to the dataset page when helpful: `https://monit.ly/datasets/<id>`.

## Limits

The tools are read-only. If a tool reports that the daily request limit is reached, tell the user and suggest trying again later.
