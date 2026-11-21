---
name: weekly-report
description: Write a weekly SEO and AI-visibility report for a SeoVision project. Use when the person asks how their site did this week, for a progress report, or for an update to share with their team or client.
---

# Weekly report

1. Pick the project: `seovision_list_projects`, then use the chosen project's `projectId` in every call.
2. Gather the last 7 days, and the 7 days before them for comparison:
   - `seovision_get_overview`: the headline numbers and the work in progress.
   - `seovision_get_visibility_series` over the last 14 days: AI Visibility Score, AI Mentions and Share of AI Mentions, with their change.
   - `seovision_list_activity`: what SeoVision did, day by day.
   - `seovision_list_articles`: the articles published this week, with their links.
   - `seovision_list_backlink_placements`: the backlinks placed this week.
   - `seovision_get_search_console_status`. When Search Console is connected, `seovision_list_search_console_queries` and `seovision_list_search_console_pages` for clicks and impressions.
3. Write the report in this order:
   - A three-line summary.
   - What changed in the numbers, with each number as a tool returned it.
   - What was published and placed, with links.
   - What comes next week.
4. Never estimate or invent a number. If a source is not connected or has no data yet, say so in one line.
