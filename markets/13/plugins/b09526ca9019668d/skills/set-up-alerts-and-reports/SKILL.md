---
name: set-up-alerts-and-reports
description: Configure Sight AI's SEO alert rules, read the alert feed, generate or schedule weekly and monthly SEO reports with share links, annotate the charts, and forecast traffic or the value of ranking gains. Use when the user wants to be notified about rank drops or lost links, wants a report for a client or manager, or asks what a ranking improvement would be worth.
---

Use this skill when the user wants monitoring, reporting or projections. Reads need no confirmation; changing rules, generating or sending reports and adding notes do.

## Pick the site

1. Call `list_sites` and settle on one site. Every other tool takes its `siteId`.

## Alerts

2. Call `get_seo_alerts` with `view` "feed" for the signals in the window (rank drops and gains, lost top 3 or page 1, lost backlinks, audit errors), newest first; `days`, `severity` and `kind` narrow it. `view` "rules" lists the rules and their channels.
3. To change a rule, confirm and call `update_alert_rule` with the `kind` and a `patch` (enabled, threshold, minDomainRank, channelEmail, channelSlack, webhookUrl, digest "instant", "daily" or "weekly"). `send_test_alert` with a `kind` sends a sample through the rule's channels; `mark_alerts_read` clears the feed.

## Reports

4. Call `get_seo_reports` for the weekly and monthly schedules (recipients, sections, white label) and the past reports with their share links. With a `reportId` it returns one report's full payload and narrative.
5. To make one now, confirm and call `generate_seo_report` with `cadence` "weekly" or "monthly" (the last complete period) or a custom `periodStart` and `periodEnd`. The report is stored with a share link; give the link to the user.
6. To set up recurring delivery, call `save_report_schedule` with a `schedule` object: cadence, recipients, sections, and white label (brand name, logo URL, accent, hide Sight branding) for client-facing reports. `send_seo_report` with a `reportId` emails it to the schedule's recipients or the ones given. Confirm recipients before sending.
7. To mark an event on the charts (a site migration, a Google update, a campaign), call `add_seo_annotation` with the `date`, a `label` and `kind` "manual" or "google_update". `get_seo_annotations` lists notes and the derived publish and audit events.

## Forecasts and value

8. Call `get_seo_forecast` for weekly clicks and impressions with the fitted trend and the 4, 8 and 12-week projection.
9. Call `get_seo_what_if` with tracked `keywords` (or ad-hoc keyword, volume, position and CPC rows) and a `targetPosition` for the extra monthly clicks and dollar value on the site's own CTR curve.
10. Call `get_seo_traffic_value` for what the site's organic visits would cost as ads per month, the top pages and keywords by value, and the keywords with the most upside.

## Do not

- Do not send a report or change recipients without confirmation.
- Do not present a projection as a promise; say it is the fitted trend from Search Console data.
- Do not turn alert rules on or off silently; name the rule and the channel.
