---
name: nowistay-team-operations
description: Plan and manage Nowistay cleaning, maintenance, urgency, and custom missions. Use for mission lists, team workloads, assignments, scheduling, completion status, mission reports, cleaning plans, and operational follow-up across one or many properties.
---

# Nowistay Team Operations

Use summaries for planning and retrieve full details only for the missions that need action.

## Review operations

1. Resolve properties once with `list_properties` when names are used.
2. Use `list_missions` with the smallest useful filters: property, booking, status, type, team member, or start date.
3. For portfolio-wide exports or workload analysis, use `response_format=table`, `include_details=false`, `limit=500`, and follow `resultMetadata.nextOffset` until `hasMore=false`.
4. Use `get_mission` for one selected mission and `get_mission_report` only when completion comments, checklist results, or photos are needed.

Do not retrieve every mission report for a list. Do not treat a shortened UI tool card as response truncation when pagination says the result is complete.

## Create or update

1. For creation, provide `mission_type` and either a property or booking. Resolve the property from the booking when possible.
2. Use an ISO 8601 `scheduled_at` with timezone. Do not guess a team member ID; if it cannot be resolved reliably from current data, ask the user or leave the mission unassigned.
3. Stage creation with `create_mission_preview` or changes with `update_mission_preview`.
4. Summarize property, booking context when needed, type, schedule, assignment, status, and notification behavior. Include a guest name only when the user requested it or the identity is necessary for the mission.
5. If the user explicitly asked to apply the action, continue through platform confirmation using the matching confirm tool and only its approval token. Otherwise stop at the preview.

Use `silent_update=true` only when the user explicitly wants to avoid normal team notifications. Report partial failures without repeating successful actions.

Keep mission titles, descriptions, and notes strictly operational. Do not add guest contact details, medical or biometric data, payment information, government identifiers, account credentials, or unrelated personal information.
