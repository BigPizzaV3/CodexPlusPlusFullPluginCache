---
name: run-analysis
description: Start, check, or extend a CreceRank AI visibility scan. Use when the user wants to run an analysis, refresh results, add questions to the last scan, or see whether a scan is still running.
---

Use this skill when the user wants a scan to run or wants its status.

If the user gives a different instruction, follow that instruction.

1. Call `crecerank_whoami` and `crecerank_get_brand`. If there is no brand, stop and ask for a URL and country before setup.
2. If the brand has no prompts, stop and ask whether to generate them with `crecerank_suggest_setup` or save prompts they provide through `crecerank_update_prompts`.
3. Call `crecerank_get_scan_status` with no `scan_id`. If a scan is queued or running, report the status and do not call `crecerank_start_scan`.
4. Call `crecerank_get_scan_settings` and say how many prompts will run.
5. Call `crecerank_start_scan` when they asked to measure or refresh. Pass `brand_id` when they named a brand that is not the active one, after `crecerank_set_active_brand`. Pass `fast_scan` true only when they asked for the fast path.
6. Call `crecerank_get_scan_status` once with the returned `scan_id`. Report id and status. Do not poll faster than about 5 seconds. Trial accounts can complete one owned scan.
7. To add questions without a full rescan, call `crecerank_append_prompts` with 1–50 texts of 10–300 characters each. This analyzes only those prompts on the last completed scan.
8. Call `crecerank_list_scans` when they want earlier analyses. Call `crecerank_delete_scan` only for a completed scan they explicitly name, and only with `mcp.destructive`. Never delete a queued or running scan.

When they then want scores, sources, or actions, read those with the results and GEO tools after the scan is completed.
