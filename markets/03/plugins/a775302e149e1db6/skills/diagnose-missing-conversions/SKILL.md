---
name: diagnose-missing-conversions
description: Find out why Converly conversions aren't showing up. Use when the user says tracking isn't working, conversions are missing, a form submission didn't appear, or an ad platform isn't receiving conversions.
---

# Diagnose missing conversions in Converly

Work through the funnel in order. Each step rules out one layer, so report what you confirmed at each one.

## Steps

1. **Is anything being captured at all?** Call `get_install_status` for the site. If detection is "never_seen", no data has ever arrived. The most likely cause is that the Converly snippet isn't installed. Give the user the script tag from `get_install_snippet` and stop here until it's in place. If detection is "confirmed", note `last_seen_at` and continue.

2. **Is a flow live?** Call `list_flows`. A flow only tracks while its status is "published". If the relevant flow is a draft, run `validate_flow`, fix any problems, and publish it with `publish_flow`.

3. **Is the destination healthy?** Call `list_destinations`. A destination with `connected` false, or a status like "connection_broken", means deliveries fail even though capture works. Reconnect it with `connect_destination`.

4. **Did the events arrive but fail to deliver?** Call `list_events`, filtering by site, flow, status or the person's email if the user mentioned a specific lead. For anything that looks wrong, call `get_event_detail` and read the per destination delivery result. Report the platform's error plainly.

5. **Nothing wrong anywhere?** Consider quieter causes. The submission may have come from the user's own team (internal traffic rules exclude those, and `add_internal_traffic_rule` can add an exclusion), the form may not be one of the detected form tools (check `list_trigger_types`), or the flow's trigger may be limited to specific pages that don't include the one being tested.

6. **Prove the destination pipe.** `send_test_event` checks the destination-forwarding path only — it does NOT appear in the conversion log, and for any server-side ad destination without a valid sandbox test code (google-ads, chatgpt-ads, linkedin-ads, google-analytics, and meta/reddit/tiktok) it creates a REAL reported conversion, so it's refused unless you set `allow_real_conversion` (confirm with the user first). If the test is accepted but real submissions don't show in `list_events`, the problem is on the capture side (snippet/origin/trigger). If the test itself is rejected, the problem is the destination connection or its configuration.

## Cautions

- Never tell the user to "submit a form and wait" unless step 1 confirmed data has been captured before or the user has confirmed the snippet is installed.
- For Meta, Reddit and TikTok test events, pass the platform's test code so the test doesn't land in real campaign reporting.
