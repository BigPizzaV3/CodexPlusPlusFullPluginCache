---
name: ga4-conversions-and-channels
description: "Analyzes Google Analytics 4 conversions and acquisition channels through the Pilot MCP server: which channels bring sessions and key events, how they change over time, which key events are configured, and where users drop in a funnel. Use when the user asks about GA4, channels, traffic sources, conversions or funnels. Triggers: GA4 analysis, channel performance, traffic sources, conversion funnel. Déclencheurs : analyse GA4, canaux d'acquisition, sources de trafic, conversions Google Analytics, entonnoir de conversion."
compatibility: "Requires the Pilot MCP server (https://app.pilot.braike.com/mcp) connected in the client and authorized on a workspace with a Google Analytics 4 property attached."
metadata:
  pilot-mcp-server: "https://app.pilot.braike.com/mcp"
  pilot-mcp-tools: "google_analytics_get_account_summaries google_analytics_get_metadata google_analytics_list_key_events google_analytics_list_channel_groups google_analytics_check_compatibility google_analytics_run_report google_analytics_run_funnel_report"
  pilot-mcp-read-only: "true"
---

# GA4 conversions and channels

Show which acquisition channels bring traffic and conversions in Google Analytics 4, how that changed, and where users drop. Answer in the user's language.

## Requirements

- **Required MCP server:** Pilot MCP (`https://app.pilot.braike.com/mcp`), authorized on the workspace where the property is attached.
- **Optional MCP servers:** a file storage server to save the tables, a team messaging server to share them. None is needed.
- **Read-only:** never create or change a key event, audience, channel group or link.

## Tools

- `google_analytics_get_account_summaries`: the properties attached to the workspace.
- `google_analytics_get_metadata`: the dimensions and metrics available on the property.
- `google_analytics_list_key_events`: the events counted as conversions.
- `google_analytics_list_channel_groups`: custom channel groups, if any.
- `google_analytics_check_compatibility`: whether dimensions and metrics can be combined.
- `google_analytics_run_report`: standard reports.
- `google_analytics_run_funnel_report`: funnel reports.

## Steps

1. Call `google_analytics_get_account_summaries`. If several properties are attached, ask which one and pass it as `propertyId`; with one, leave it out.
2. Call `google_analytics_list_key_events` to know what counts as a conversion. If none is configured, say so: conversion figures will be empty.
3. Call `google_analytics_run_report` with two `dateRanges` of equal length (by default the last 28 days and the 28 days before), `dimensions: ["sessionDefaultChannelGroup"]`, `metrics: ["sessions", "engagedSessions", "keyEvents", "totalRevenue"]`.
4. For the channels that moved most, break down by `sessionSource` and `sessionMedium`. When unsure a combination works, call `google_analytics_check_compatibility` first; check names with `google_analytics_get_metadata`.
5. If the user describes a path (landing page, product page, cart, purchase), build it as a funnel with `google_analytics_run_funnel_report`.
6. If custom channel groups exist (`google_analytics_list_channel_groups`), mention which grouping the figures use.

## Output

1. **Summary**: sessions, key events and revenue for both periods.
2. **By channel**: a table with sessions, key events, conversion rate and the change.
3. **What moved**: the sources behind the largest changes.
4. **Funnel**, when asked: step counts and drop-off rates.
5. **Tracking notes**: missing or doubtful key events.

## Rules

- Name the property, the periods and the time zone of the property when it matters.
- A rate with an empty denominator is not available, not zero.
- GA4 attribution differs from the ad platforms': do not expect the numbers to match theirs.

## Examples

- "Which channels brought conversions this quarter?"
- "Compare les canaux GA4 du mois dernier à ceux du mois précédent."
- "Where do users drop between the product page and the purchase?"
