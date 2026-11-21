---
name: get-started
description: "Use when setting up MarketCheck or researching vehicle inventory, sold-market trends, a VIN, US valuations, manufacturer incentives or dealerships. Choose the right read-only tool and explain what its data means."
---

# Getting started with MarketCheck

MarketCheck provides read-only automotive market data for the US, Canada and UK.

## Setup

If the user is getting started, briefly describe the supported workflows and ask
what they want to research. If their connection is unavailable, direct them to
connect MarketCheck in the host's plugin settings. They sign in with their
MarketCheck developer account and select an API key and allowed tools on the
MarketCheck consent screen. Never ask them to paste credentials into chat.
Usage counts against the selected key's plan; some data requires additional
plan access. Do not run sample searches merely because the setup skill opened.

## Choose the tool

- Current inventory: `search_active_cars` for US/Canada or
  `search_uk_active_cars` for UK inventory. Label the currency and market.
- Recent expired/sold listing records: `search_past_90_days` for US/Canada or
  `search_uk_recent_cars` for the UK. Read each tool's required location filters
  and limitations before calling it.
- Monthly US sold statistics: `get_sold_summary`. Coverage starts January 2021
  and ends with the last complete month; this tool has no Canada or UK data.
- A vehicle's available specifications: `decode_vin_neovin` with a supported
  17-character VIN; report missing coverage rather than guessing specifications.
- A vehicle's advertised listing history: `get_car_history`.
- A US price estimate and comparable vehicles: `predict_price_with_comparables`.
  Obtain mileage and US location; disclose material assumptions such as dealer
  type and certification rather than silently accepting defaults.
- Manufacturer offers: `search_oem_incentives` or
  `search_oem_incentives_by_zip`. The latter takes `oem` and a US ZIP code.
- Dealer or group lookup: `search_dealerships` or `search_dealers`. Use returned
  inventory URLs and group names for follow-up queries, not guessed identifiers.
- Service capabilities: `get_server_info`. Prefer the current tool descriptions
  and schemas if their constraints differ from general server information.

## Query correctly

Read the selected tool's schema before use. For inventory tools that require
categorical-value discovery, first query facets with `rows=1` and only the
needed location filters. Then use the exact returned values for make, model,
powertrain, trim and other categorical filters. Do not guess `fuel_type="Hybrid"`.
Keep result counts small, filter first, and paginate only when needed.

Ask for a ZIP/postcode and radius when location matters. Do not silently broaden
the search if no listings match; explain the empty result and offer a specific
adjustment. Respect user-selected tool permissions. For authentication or plan
errors, explain what the user needs to reconnect or enable without inventing data.

For `get_sold_summary`, supply `inventory_type`. Use complete month boundaries
and at most a one-year window per call. Use `summary_by="national"` for national
questions; never sum state-level top-N rankings as a national total. For a market
baseline, use a separate call with `ranking_dimensions="none"` and the same
vehicle population. Explain model-year age filters and any minimum sales-count
threshold. Check truncation and warnings before making comparisons.

## Explain the data

- Report figures and listing links from actual results. Never invent vehicles,
  VINs, prices, specifications, availability or a successful action.
- Prices are advertised asking prices, not confirmed transaction prices.
  A predicted value is an estimate, not a binding quote.
- Sold summaries use inferred-sale rules. Recent/expired listing records alone
  do not prove a completed sale: a listing ID can expire when price or mileage
  changes while the VIN remains active elsewhere.
- `dos_active` measures time at the current dealer. `dom_active` measures the
  vehicle's cumulative active market exposure across dealers. Use the measure
  that answers the question and label it accurately.
- Do not infer title status or ownership from incomplete `carfax_*` fields.
- This plugin cannot purchase, reserve or pay for a vehicle, modify accounts,
  delete saved searches, or retrieve private owner names and addresses. Explain
  these limits without attempting unsupported tools; offer relevant read-only
  research if useful.
