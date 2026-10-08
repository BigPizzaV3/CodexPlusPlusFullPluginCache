---
name: browse-apps
description: Find ChatGPT and Claude apps in the Atlas directory and show them in a table.
---

Use the `show-apps` tool to answer any question about which ChatGPT or Claude apps exist.

1. Translate the user's request into `show-apps` filters:
   - `q`: free-text search over app name and description.
   - `platform`: `chatgpt` or `claude` — omit for both.
   - `startDate` / `endDate`: release-date window, `YYYY-MM-DD` (both inclusive). Resolve relative asks ("this week", "since June") to real dates.
   - `category`: app category (e.g. productivity, developer-tools).
   - `framework`: the framework an app is built with.
   - `hasBeacon`: `true` to only include apps that expose a beacon.
2. Only set the filters the user actually asked for; omit the rest to keep results broad.
3. Call `show-apps`. It returns up to 200 apps and renders them as a table view — do not re-list the rows in prose.
4. If the result is empty, loosen the filters (drop `category`/`framework`, or broaden `q`) and try again before telling the user nothing matched.
