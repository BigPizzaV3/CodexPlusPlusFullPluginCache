---
name: tl-save-report
description: Save a curated set of ThoughtLeaders channels, brands, videos, or sponsorships from the current conversation as a fixed-list report. Use when the user asks to save, persist, or return to a shortlist.
---

# Save a fixed-list report (MCP)

The MCP exposes tl_reports_save_list, which saves the exact IDs provided. It cannot create a refreshable filter-style report or update an existing report.

## Workflow

1. Call tl_whoami, then tl_skill_track with skill="tl-save-report" and stage="started"; retain its run_id. Identify the single entity type: channels, brands, articles/uploads, or sponsorships. Ask if a mixed or ambiguous set could mean more than one type.
2. Collect canonical IDs from tool results. Resolve channel or brand names with tl_channels_find/tl_brands_find; never guess. Videos require composite <channel_id>:<youtube_id> IDs.
3. Draft a title of at most 60 characters and a concise description that says this is a fixed list. Show what will be saved and ask before calling the write tool unless the user clearly asked to save now.
4. Call tl_reports_save_list once with entity, IDs, title, and description. Return the report URL and state that it is a snapshot. Do not retry unless the first call clearly failed.

Do not promise future matches will be added. Do not claim filter-style saving or report editing is available unless the connector gains those tools.

Before the final response, call tl_skill_track with skill="tl-save-report", stage="completed", the retained run_id, and outcome="completed", "no_results", "failed", or "cancelled". Never include user content, queries, or results in that tracking call.

