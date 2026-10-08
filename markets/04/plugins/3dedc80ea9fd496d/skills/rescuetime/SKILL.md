---
name: rescuetime
description: Analyze a user's RescueTime data or explicitly control their current focus session or timer through RescueTime MCP. Use for recent tracked activity, time allocation, projects or tasks, categories, productivity, focus state, daily or weekly patterns, bounded comparisons, or requests to start or stop focus.
---

# RescueTime

Use the RescueTime MCP tools to answer questions about the user's tracked time. Treat the records as private behavioral data and report what was observed without judging whether the user's choices were good or bad.

## Choose the operation

- Use `reference_documentation` for taxonomy, productivity, overview, and default category definitions. It is public and does not require a connection.
- Use `recent_activity` for a compact timeline. Request a `day` chunk for one calendar day at five-minute resolution, or a `week` chunk for seven days at hourly resolution. A week can follow the user's natural calendar week or use an explicit seven-day start/end range. Prefer a day unless the question needs a broader pattern.
- Use `project_time_history` for project, task, client, comment, and review-state history.
- Use `taxonomy_rollup` for totals or calendar comparisons by activity, category, overview, or productivity.
- Use `get_focus_state` to determine whether a focus zone, focus session, or timer is active.
- Use `start_focus_session`, `start_timer`, and `stop_focus` only when the user explicitly asks to change focus state.

If a user-data tool requests authentication, let the host complete the RescueTime OAuth flow. Never ask the user to paste an OAuth token or API key into the conversation. A user who deliberately manages credentials locally may configure a RescueTime MCP API key in the host's secure credential facility.

## Interpret results

- Preserve the returned time zone and state the actual start and end bounds.
- Distinguish automatically tracked activity from manually or automatically assigned project time.
- Explain that personal category and productivity overrides take precedence over RescueTime defaults.
- Treat productivity scores as the user's configured classification, not an objective assessment.
- When a response may be limited, state the limit and avoid implying that the result is complete.
- Aggregate before presenting private detail unless the user explicitly asks for the detail.
- Project history contains the user's own time records. Those records may refer to user-owned or available team projects; it does not provide other users' time.

## Work efficiently

- Resolve relative dates using the user's returned RescueTime time zone.
- Do not request a full year when a day or week answers the question.
- Fetch recent activity as a day or week chunk. Use `today` or `yesterday` for common day requests. For weeks, use `this week`, `last week`, `N weeks ago`, `week of DATE`, or an explicit seven-day `start_date` and `end_date`. Keep taxonomy rollups within 45 inclusive days and project history within 366 inclusive days.
- For period comparisons, make equivalent calls with matching interval lengths.
- Use public reference documentation only when its definitions materially improve the answer.

## Control focus safely

1. Call `get_focus_state` before every focus-state change.
2. If a session or timer is already active, explain that state instead of starting another.
3. If starting a session will replace a focus zone, tell the user before acting.
4. Never start or stop focus merely because you recommended it. Require an explicit user request.
5. Pass the active state's `start_time_epoch` to `stop_focus` so a stale request cannot stop a newer session.
6. Report the focus state returned after the write. When stopping a timer, mention that linked project time may have been finalized.

Reading current focus state uses normal time-data access. Focus controls require RescueTime OAuth
with `focustime_data`; MCP API keys can inspect focus state but remain read-only.
