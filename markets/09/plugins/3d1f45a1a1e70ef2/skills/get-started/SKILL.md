---
name: get-started
description: Sign in to CreceRank, create a brand, save analysis prompts, run the first visibility scan, then report sources, recommendations, and GEO actionables. Use when the user wants to get started, sign up, track a new site, or run the full analysis.
---

Use this skill for a first CreceRank run: account, brand, prompts, scan, sources, recommendations, and actionables.

If the user gives a different instruction, follow that instruction.

## Account

There is no signup tool. Connecting this plugin opens CreceRank sign-in. A new user creates an account there with Google or email, then approves access. `mcp.read` and `mcp.write` are required for this workflow. Deletes need a separate `mcp.destructive` approval.

1. Call `crecerank_whoami`.
2. If the call is unauthenticated, ask the user to connect CreceRank and stop.
3. If the trial is expired or the tool returns a plan error, call `crecerank_get_subscription` and tell them to subscribe in the CreceRank app. Do not collect a card number.

## Brand

1. Call `crecerank_list_brands`.
2. If they name an existing brand, call `crecerank_set_active_brand` with its id.
3. If they want a new site, ask for the URL and country when either is missing. Call `crecerank_list_countries` if the country is unclear, and use a returned ISO code.
4. Call `crecerank_validate_brand_url`. Stop if it rejects the URL.
5. Call `crecerank_url_brand_hints` for a preview of the name. Then call `crecerank_setup_brand` with the URL and `country_iso`. That creates or updates the active brand.

## Prompts

1. Call `crecerank_get_brand`.
2. If they already wrote the questions, call `crecerank_update_prompts` with those texts. Each text must be 10–300 characters.
3. If the brand has no prompts and they want them generated, tell them `crecerank_suggest_setup` replaces saved name variations and prompts, then call it after they agree.
4. To change only the detected names, call `crecerank_update_variations`. To set the display name, call `crecerank_patch_official_name`.

## Scan

1. Call `crecerank_get_scan_status` with no `scan_id`. If a scan is queued or running, report that and do not start another.
2. Call `crecerank_get_scan_settings` and tell them how many prompt slots will run.
3. Call `crecerank_start_scan` only after they asked to measure visibility. Trial accounts can complete one owned scan.
4. Call `crecerank_get_scan_status` once and report the scan id and status. Do not poll faster than about 5 seconds.

## Results

When a scan is already completed, or when they ask for results after one finishes:

1. Call `crecerank_get_panel` with `compact` true.
2. Call `crecerank_get_sources` with `compact` true.
3. Call `crecerank_get_geo_recommendations`.
4. Call `crecerank_get_geo_playbook` with `compact` true.

Report the visibility percent, the main cited domains, up to three recommendations, and the next playbook actions. Use only values the tools returned. If there is no completed scan, say the scan is still running or has not been started.

Do not delete a brand or scan, start Google Analytics sign-in, or take payment in this workflow.
