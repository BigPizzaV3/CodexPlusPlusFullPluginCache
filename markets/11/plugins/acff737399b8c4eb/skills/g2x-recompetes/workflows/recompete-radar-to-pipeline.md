# Recompete radar to pipeline

Goal: find contracts that are ending, judge which ones matter, and track the chosen pursuits.

## Steps

1. Calibrate with `g2x_calibrate_session`. Note the company UEI, NAICS codes and top agencies.
2. Find ending work. Call `g2x_recompete_radar` scoped to the market, for example `{"naics": ["541512"], "months_ahead_end": 12, "sort": "end_date"}`. To watch a competitor's book, scope with its `recipient_uei` instead. Page with the returned cursor and the same filters.
3. Cross-check the window. Call `g2x_expiring_awards` with the same NAICS and agency for the fiscal year, for example `{"expiry_fiscal_year": 2027, "naics": ["541512"]}`. An award ending soon does not by itself prove a recompete date.
4. Judge each candidate. Keep the radar's confidence band and matching reasons attached. Open promising incumbent records with `g2x_search_companies` and `g2x_company_contract_history`. A candidate notice is a possibility, never a finding.
5. Check forecasts for the same work. Call `g2x_forecast_scan` with the agency and keyword. Say whether the buy is forecast, open, both or neither.
6. Track on request. Only when the user asks: list pipelines with `g2x_list_pipelines`, read the target with `g2x_get_pipeline`, then add items with `g2x_add_to_pipeline` using an `operation_id`. Add context with `g2x_add_pipeline_note`. Read the pipeline back to confirm.

## What to tell the user

List each ending contract with incumbent, agency, end date, value basis, confidence, the candidate recompete link and what would confirm it. Name what you added to the pipeline, in which stage, with links. Do not present a forecast or an expiring award as an open solicitation.
