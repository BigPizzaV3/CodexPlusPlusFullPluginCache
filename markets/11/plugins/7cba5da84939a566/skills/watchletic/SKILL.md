---
name: watchletic
description: Use connected Watchletic tools to inspect and analyze the user's training data, export supported files, and safely preview or apply changes. Use when the user asks about Watchletic workouts, readiness, analytics, training load, routes, integrations, devices, or structured workouts.
---

# Watchletic

Use the connected Watchletic MCP tools. Start with `get_account_status`, then use `get_training_context` for ordinary analysis. Fetch one activity, structured workout, analytics view, or selected raw channel only when it answers the user's specific question. For workout detail, use `get_activity` first and `get_activity_interval_summaries` for compact lap or interval statistics across every available scalar channel. Never page through all raw samples merely to calculate averages. Use `get_activity_samples` only for a specific time-series question that summaries cannot answer. Use `export_activity_fit` when a complete portable workout file is specifically useful; raw exports remain available for workflows that need them.

Explain what the returned data supports, distinguish observations from inference, and report incomplete cloud data instead of filling gaps. Request raw channels only when a specific question requires them. Read [references/analysis.md](references/analysis.md) when interpreting training data.

Use “structured workouts” consistently. Before proposing a schedule, obtain the user's goal, target date, weekly availability, preferences, injuries, and health constraints. Follow [references/structured-workouts.md](references/structured-workouts.md).

Every mutation follows the preview-and-confirm workflow in [references/safety.md](references/safety.md). Never treat a general request for help as permission to apply a change.

Layouts support list, get, create, update, and delete. A layout can also be disabled without deleting it by setting `isDisabled` to `true`; disabled layouts remain editable but are never selected. Every match field set on a layout must match the active workout. Matching custom layouts take precedence over built-in layouts. Among matching custom layouts, the most specific wins: `activityType`, a non-`unknown` `locationType`, `goalType`, and `targetType` each add one point, and each required connected device adds one point. `stepName` must match when set but does not add a specificity point. Equal scores are resolved by layout ID in descending order.

Watchletic does not host an LLM. Keep analysis and inference in ChatGPT. Respect Read-only access and Watchletic Club entitlement errors without trying alternate credentials or data paths.
