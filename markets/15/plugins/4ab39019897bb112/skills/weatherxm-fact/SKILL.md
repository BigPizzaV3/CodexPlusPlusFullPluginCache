---
name: weatherxm-fact
description: Read published WeatherXM FACT historical forecast accuracy across 5 variables (temperature, wind_speed, wind_direction, precipitation, humidity), country cell-win summaries, global/local model error curves, and ground-truth station coverage.
---

# WeatherXM FACT

Use the four tools exposed by weatherxm-fact:

- `get_best_forecast_model`: query a `(lat, lon)` coordinate or `station_or_report_id` for published historical model rankings across `variable` (`temperature`, `wind_speed`, `wind_direction`, `precipitation`, `humidity`), `lead_day` (`all` or `0`..`7`), and `exclude_commissioned`. For `wind_direction`, errors are circular shortest-arc angular errors (`0°–180°`, where `359°` vs `1°` = `2°`) on speed-weighted hourly vector averages, returning both all-hours and `>3 m/s` active-wind rankings (`preferred_operational_champion`).
- `check_ground_truth_coverage`: query historical archive publication coverage and nearest evaluated reference cell for any `(lat, lon)` coordinate or `station_or_report_id`.
- `get_fact_leaderboard`: query global error metrics (`lead_day`: `0`..`7`, optional `limit`: `1`..`45`, default `45`) or country cell-win counts (`country`, `variable`, `lead_day`, `exclude_commissioned`).
- `get_model_head_to_head`: pass a `models` array (`1`..`10` model IDs), `variable`, and optional `lat`/`lon`, `country`, `lead_day`, and `exclude_commissioned` to compare global curves alongside optional local H3 cell or country comparisons.

Variables: `temperature`, `wind_speed`, `wind_direction`, `precipitation`, `humidity`. Where supported, `lead_day` is a string: `all` or `0` through `7`.

Only send task-specific benchmark inputs. Do not ask for the user's personal account credentials or chat history. Coarse H3 query metadata is retained for demand analytics as described in the privacy policy. Report provenance, basis, and `summary_for_user` when provided.
