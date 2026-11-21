---
name: studio-insights
description: Summarize Eye.Photo studio activity, uploaded and completed photos, customers and estimated savings over a specific date range.
---

Follow the shared [account connection and permissions](../../scripts/AUTHENTICATION.md) instructions. Determine the permissions needed for the current task before initial account setup, preserve the task through host-managed authorization, and use the get-started workflow to select an authorized studio.

If the account is disconnected or a startup connection call returns **Unknown tool**, **Tool not found**, or is unavailable, follow connection recovery immediately: show a real **Connect Eye.Photo** link from `../../scripts/CONNECTION.json` when present and validated by the shared instructions, otherwise [Connect Eye.Photo](https://chatgpt.com/settings/plugins-settings). Tell the user to open **Settings → Plugins → the installed Eye.Photo plugin → Connect**, sign in, approve their studio, then return and say **Connected** so this same request can continue. A connection-tool lookup failure alone does not establish a backend defect. Do not finish with only the error or repeatedly call missing tools.

Establish the selected studio with the get-started workflow. Call `studio_context_get`; require the studio-insights capability. Resolve relative periods in the studio timezone, state the resulting inclusive ISO dates and use `studio_stats` with explicit `from`, `to` and daily or monthly period. Ask only when the requested range is ambiguous.

Report the studio name, dates and timezone with the result. Distinguish photo records uploaded in the period from those records currently completed. Completion is current status, not historical completion time. Dashboard photo activity can include upload event records; do not equate that series with unique uploaded photos. Follow the returned metric definitions and currencies. Label hours and money saved as estimates, never revenue or invoiced amounts. Product sales revenue excludes subscription revenue.

Explain empty results accurately. Use comparisons only with equivalent periods and metric definitions. Do not extrapolate beyond the returned data, reveal another studio's data, or invent unavailable metrics. Return a concise summary and a table or chart when useful.
