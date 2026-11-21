# GovBot Tides & Terrain

Version 1.0.0 prepares source-linked coastal water-level history, astronomical tide tables and public-point terrain/watershed briefs. It uses six read-only operations from NOAA CO-OPS and USGS public sources. No account or API key is required by the live MCP service.

This is a submission candidate, not a published ChatGPT directory release. The independent MCP and policy pages are live. Actual private ChatGPT testing covers the three workflows and the listed refusal scenarios. The owner-approved product guide and genuine ChatGPT walkthrough are public. Portal scans, domain verification and final owner attestations remain separate from publication of those website assets. The demo URL is bound to the exact independently reviewed and publicly verified video.

- Product guide: https://govbot.ai/plugins/tides-terrain.html
- Demo: https://govbot.ai/plugins/tides-terrain-demo.mp4
- MCP: https://tides-api.govbot.ai/mcp
- Support: https://tides-api.govbot.ai/ and hello@govbot.ai
- Privacy: https://tides-api.govbot.ai/privacy
- Terms: https://tides-api.govbot.ai/terms
- Publisher: Ideation Lab, Corp. Independent product; no government or OpenAI endorsement.

## Three workflows

- `water-level-history-brief`: select a suitable station, explain its datum/epoch, inspect observed coverage and quality, and write a dated observation brief.
- `tide-prediction-brief`: explain astronomical high/low or sampled predictions with local-clock conventions; compare observations only on matching station, time, units and datum.
- `terrain-watershed-brief`: combine modeled point elevation and nested HUC context, preserving source coverage and the distinction from surveys or parcel determinations.

## Six tools

| Tool | Evidence |
| --- | --- |
| `find_tide_stations_near_point` | Nearby NOAA stations and requested observation/prediction capability |
| `get_observed_water_levels` | Bounded NOAA observations, quality and returned coverage |
| `get_tide_predictions` | Bounded astronomical tide predictions |
| `get_station_datums` | Station-local datum/epoch metadata |
| `get_ground_elevation_at_point` | USGS modeled ground elevation and available source metadata |
| `get_watershed_at_point` | USGS WBD HUC membership at requested levels |

Use explicit datum, units and time-zone choices. NOAA `local` follows the station local/daylight-saving convention; `local_standard` excludes DST and `gmt` is UTC. Observation windows: six-minute up to four calendar days; hourly/high-low verified up to 31. Prediction windows: six-minute up to two days; hourly seven; high-low 31. Known subordinate stations require high/low predictions and MLLW in this service. Discovery uses current active water-level and tide-prediction catalogs, not an all-history station inventory. A schema datum option does not prove that every station supplies it.

Source measurement/prediction periods, source metadata dates, actual retrieval times and cache age are different facts. Preserve returned labels and missing metadata. A model point sample is not a surveyed ground/building-floor elevation; resolution does not establish vertical accuracy. Watershed membership does not establish a flow path or floodplain. Do not apply station datum offsets to arbitrary inland terrain. Missing data or a source failure do not mean zero or safety.

No address lookup, device location, personal-address solicitation, property flood-zone determination, elevation certificate, flood/insurance/engineering or navigation-safety certification is provided. Astronomical predictions are not weather or storm-surge forecasts. Use qualified authorities for operational or certified determinations. Source access does not settle constituent-data rights; applicable source terms and owner attestations remain separate review items.

## Local package checks

From this repository with the runtime dependencies installed:

```sh
node scripts/validate-package.mjs
node --test tests/package.test.mjs
python3 scripts/package.py
```

The archive allowlist contains only `plugin.json`, `mcp.json`, this README, `LICENSE`, `assets/logo.png` and the three `skills/*/SKILL.md` files. Runtime code, source/test evidence, credentials, private client adapters and deployment configuration stay outside the archive. Five positive and three negative reviewer prompts/expectations are in `plugin.json`. Their actual-client evidence is recorded separately from package validation: seven cases passed on the first response, and the datum case passed after an explicit provenance follow-up. Raw client arguments/results and internal skill reads were not visible. The private ChatGPT adapter uses the same three skill files; it changes the app registration and private display identity for testing. Final owner approval, public video binding, portal scans and legal attestations remain separate from these checks.
