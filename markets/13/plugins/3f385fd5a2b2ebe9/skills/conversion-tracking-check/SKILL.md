---
name: conversion-tracking-check
description: "Checks conversion tracking across platforms through the Pilot MCP server: Google Ads conversion actions and their settings, value rules, Meta pixels and their activity, GA4 key events and the link between GA4 and Google Ads, then compares the volumes each source reports and flags gaps. Use when the user doubts conversion figures, before trusting an optimization, or after a site change. Triggers: conversion tracking audit, pixel check, are my conversions tracked. Déclencheurs : contrôle du suivi des conversions, vérifier le pixel, conversions qui ne remontent pas, audit du tracking."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with Google Ads, Meta Ads or Google Analytics 4 attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "pilot_data_freshness google_list_accounts google_list_conversion_actions_detailed google_list_conversion_value_rules google_get_campaign_performance meta_list_accounts meta_list_pixels meta_get_pixel_stats google_analytics_list_key_events google_analytics_list_google_ads_links google_analytics_run_report"
  pilot-mcp-read-only: "true"
---

# Conversion tracking check

Check that conversions are tracked the way the user thinks, on each platform, and that the platforms roughly agree. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace concerned.
- **Optional MCP servers:** a file storage server to save the checklist, a team messaging server to send it to the developer in charge. None is needed.
- **Read-only:** never create or change a conversion action, a pixel, a key event or a link. Fixes are for a person to apply.

## Tools

- `pilot_data_freshness`: whether Pilot's collected data is current.
- `google_list_accounts`: the Google Ads accounts attached to the workspace.
- `google_list_conversion_actions_detailed`: conversion actions with status, category, counting, windows, value and attribution.
- `google_list_conversion_value_rules`: rules that change conversion values.
- `google_get_campaign_performance`: conversions reported per campaign.
- `meta_list_accounts`: the Meta ad accounts attached to the workspace.
- `meta_list_pixels`: the pixels of the account.
- `meta_get_pixel_stats`: events received by a pixel over time.
- `google_analytics_list_key_events`: the events GA4 counts as conversions.
- `google_analytics_list_google_ads_links`: whether the GA4 property is linked to Google Ads.
- `google_analytics_run_report`: key events by name and by day.

## Steps

1. Call `pilot_data_freshness` to rule out a collection gap.
2. Google Ads: `google_list_accounts`, then `google_list_conversion_actions_detailed`. Check that the primary actions are enabled, counted as expected (every conversion or one per click), with sensible windows, and that the action used for bidding is the right one. Read `google_list_conversion_value_rules`.
3. Call `google_get_campaign_performance` over the last 30 days to see the conversions Google Ads reports.
4. Meta Ads: `meta_list_accounts`, `meta_list_pixels`, then `meta_get_pixel_stats` for each pixel over the last 14 days. A pixel with no event for days is a red flag.
5. GA4: `google_analytics_list_key_events`, `google_analytics_list_google_ads_links`, then `google_analytics_run_report` with `dimensions: ["eventName", "date"]` and `metrics: ["keyEvents"]` over the last 14 days.
6. Compare the volumes. Platforms count differently (attribution, windows, view-through), so look for gaps far beyond those differences, and for sudden breaks on a date.

## Output

1. **Verdict**: tracking looks sound, partly broken, or broken, in one line.
2. **By platform**: what is tracked, how it is counted, and what looks wrong.
3. **Cross-check**: the volumes side by side for the same period, with the expected differences explained.
4. **Fixes**: a checklist for the person in charge, most important first.

## Rules

- Do not expect the platforms to report the same number: explain the usual differences before raising a gap.
- Name the period of every volume.
- Never call a tool that changes tracking settings.

## Examples

- "Are my conversions tracked correctly across Google Ads, Meta and GA4?"
- "Vérifie le suivi des conversions : les achats ne remontent plus depuis lundi."
- "Le pixel Meta reçoit-il encore des événements ?"
