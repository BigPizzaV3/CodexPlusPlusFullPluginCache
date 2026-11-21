---
name: saved-utility-workflows
description: Use when someone wants to save, reopen, change or duplicate a free WallKiwi utility calculation and download its result.
---

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.
Use only existing records confirmed to contain anonymous or synthetic teaching
content. If privacy is uncertain, return the exact native link without reading
the record, opening its private screen or obtaining its contents through an
export or another connector. Do not ask the adult to paste pupil records.


# Saved utility workflows

Connect a free account through WallKiwi OAuth when the user requests saving or downloads. WallKiwi and Planit share account sign-in, while this resource uses its own audience and least required tools:read/tools:write permissions. Free utility actions use no AI credits or paid download allowance.

For a new record, discover the exact utility with get_wallkiwi_catalog, read that row's detailTool, build with its previewTool and save the returned complete snapshot with save_wallkiwi_tool using tool_slug, title and snapshot. The save operation stores data; it does not select or execute a builder. Numeric measurements are suitable; private pupil data and uploaded images are not. Explain a native saved-item capacity refusal without offering an upgrade.

For an existing record, list_saved_wallkiwi_tools and get_saved_wallkiwi_tool before editing. Preserve exact saved_id, tool_slug, inputs and seed. Read current tool settings, apply only the requested numeric changes, prepare the revised result, then use update_saved_wallkiwi_tool with the new complete snapshot. Use duplicate_saved_wallkiwi_tool first if the user requests a separate copy. Do not modify another record, invent IDs or treat another user's IDs as permission.

Look up the saved item's exact slug in the current catalogue and use its individually listed previewTool and exportTool with the complete current inputs and seed. Select only names present in the connected MCP tool list; do not invent operations or pass a tool selector to preview/export. A saved record is data, not the file itself: rebuild with the fixed native deterministic generator and return actual PDF bytes. Preserve the original when the user requests a copy. Account and ownership errors must be reported honestly; do not retry writes blindly.
