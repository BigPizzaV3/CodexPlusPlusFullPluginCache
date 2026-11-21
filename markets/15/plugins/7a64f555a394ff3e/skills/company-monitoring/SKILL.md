---
name: company-monitoring
description: Monitor companies with Firmium watchdogs - list existing watchdogs, show recent signals, or create a new watchdog from a plain-language description. Use for "alert me when", "monitor", "watchdog", "notify me about changes", "überwachen", "benachrichtige mich".
---

Use this skill when the user wants to be informed about future changes or asks about signals from existing watchdogs.

## Workflow

- Show existing watchdogs: `list_watchdogs`.
- Read one watchdog and its signals: resolve its uuid with `list_watchdogs`, then call `get_watchdog(uuid, since?, official_only?, limit?, offset?)`. Signals follow its configured history window; reading does not mark them processed.
- Create a watchdog:
  1. Resolve the companies with `search_company` when the user names them.
  2. Restate what will be monitored in one sentence and call `create_watchdog` with a clear `prompt` (for example "Alert me when the management changes or an insolvency is filed"), the `company_uuids` and an optional `name`.
  3. Confirm the creation. Explain that the monitoring rules are configured by AI and can be reviewed, paused or deleted in the Firmium app.

## Boundaries

- This plugin can create watchdogs but cannot edit, pause or delete them. Point the user to the Firmium app for that.
- Signals from news or websites are third-party reports, not register facts; say so when you present them.
- If watchdogs are not included in the user's plan, say so plainly without promoting upgrades.
- Answer in the user's language. Explicit user instructions take priority over this skill.
