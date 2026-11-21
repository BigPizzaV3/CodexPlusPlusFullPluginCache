---
name: weekly-performance-summary
description: Generate an executive weekly performance summary of eCommerce conversions, top revenue-impacting issues, UX friction signals, and site health using Webeyez.
---

# Weekly Performance Summary

Use this skill when a user asks for a weekly performance report, executive summary, store health check, or prioritization of issues from the past week.

## Workflow

1. **Resolve Target Store**
   - Call `get_organizations_list` to get the user's `organizationId`.
   - Call `get_organization_domains` to determine the store `domain` to report on.

2. **Gather Weekly Analytics & Top Friction Points**
   - Call `start_webeyez_query` asking for a comprehensive summary of the past 7 days covering overall sessions, conversion rates, top revenue-costing issues, checkout drop-offs, JavaScript/API errors, and UX friction signals (rage clicks, dead clicks, slow page loads).
   - If `start_webeyez_query` returns `status: "processing"`, use `check_webeyez_status` with the returned `jobId` until completed.

3. **Fetch Representative Session Recordings**
   - If specific high-impact sessions are returned in the data, call `get_session_recording_links` for up to 10 session IDs to provide concrete replay examples.

4. **Structure the Weekly Report**
   - **Key Metrics Overview:** Summarize traffic, conversion trends, and overall digital experience health over the past 7 days.
   - **Top Revenue-Impacting Issues:** Highlight the highest-cost bugs, failed API requests, or checkout blockers.
   - **UX & Performance Breakdown:** Note any device, browser, or page-path anomalies (including rage clicks and page load issues).
   - **Prioritized Action Plan:** Recommend the top 3 fixes the engineering or UX team should tackle first, accompanied by session replay links where available.

