---
name: investigate-conversion-drop
description: Investigate sudden conversion drops, checkout friction, JavaScript errors, and failed API calls using Webeyez analytics and session replays.
---

# Investigate Conversion Drop

Use this skill when a user asks why conversions dropped, reports checkout failures, or wants to find the root cause of lost revenue on their store.

## Workflow

1. **Identify Organization and Domain**
   - Call `get_organizations_list` to find the user's accessible organizations and `organizationId`.
   - Call `get_organization_domains` with the `organizationId` to identify the target store `domain` if not already specified by the user.

2. **Query Conversion and Funnel Diagnostics**
   - Call `start_webeyez_query` with a targeted question about the conversion drop, funnel drop-offs, checkout failures, JavaScript errors, and failed network calls for the relevant time period (e.g., last 24 hours or today vs. previous baseline).
   - If `start_webeyez_query` returns `status: "processing"` with a `jobId`, poll `check_webeyez_status` until the query completes.

3. **Retrieve Session Replay Examples**
   - If the query results include affected `Session Id`s, call `get_session_recording_links` (up to 10 session IDs) so the user can watch the exact sessions where friction or errors occurred.

4. **Present Findings Ranked by Impact**
   - **Executive Summary:** State clearly whether the drop is driven by a technical issue (JS error, failed API call, slow page load) or funnel/traffic shift.
   - **Top Issues by Revenue/Conversion Impact:** List the specific page paths, error messages, affected browsers/devices, and affected session counts.
   - **Session Replays:** Include direct links from `get_session_recording_links` for immediate verification.
   - **Recommended Fixes:** Provide prioritized, actionable next steps for engineering or product teams.

