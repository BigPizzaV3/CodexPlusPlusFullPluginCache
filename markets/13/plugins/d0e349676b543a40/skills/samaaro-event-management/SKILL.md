---
name: samaaro-event-management
description: Manage Samaaro events and admins with the Samaaro tools. Use when the user asks about their Samaaro events, event reports, expenses or ROI, or wants to create, clone, update or deactivate an event, or create, block, unblock, assign, remove or invite an admin.
---

# Samaaro event management

Use this skill with the Samaaro tools to answer questions about the user's Samaaro workspace and to make changes they ask for. The user is a Samaaro super-admin and every tool acts with their permissions.

## Internal IDs

Samaaro records carry internal database IDs (`_id`, `eventId`, `adminId`). Use them only as arguments for other Samaaro tools.

- Do not show internal IDs in responses, tables or summaries.
- Refer to events by title and identifier (the URL slug, e.g. `annual-meetup-2026`), and to admins by name and email.
- If the user explicitly asks for an ID, provide it.

## Finding the right record

- For an event named by the user, call `search_events_by_name` first and use the `_id` of the match. If several events match, list them by title, identifier and dates and ask which one.
- Use `list_event_names` or `list_admin_names` when you only need to resolve a name to an ID.
- `get_event_report` takes the event **identifier** (slug). The other event tools take the event **ID**.

## Listing events

- `list_events` returns 10 events per page. Use `status` (`upcoming`, `live`, `recent`, `completed`, `all`), `type` (`virtual`, `in-person`) and `search` to narrow results instead of fetching everything.
- If the user wants more results, request the next `page`. Tell the user when there may be more pages.

## Reports and ROI

- `get_event_report` gives one event's analytics: tickets, RSVPs, check-ins, new vs repeat attendees and UTM sources.
- `get_event_roi_overview` compares a date range with the same period last year. If the user gives no dates, it covers the current month; say so in the answer.
- Present numbers as short tables and highlight the change versus last year.

## Making changes

These tools create or change data: `create_event`, `clone_event`, `update_event`, `toggle_event_status`, `create_admin`, `block_admin`, `unblock_admin`, `assign_admin_to_event`, `remove_admin_from_event`, `send_event_invite_to_admin`.

- Before calling one, state in one line what will change and wait for the user to confirm.
- `update_event`: fetch the event first and pass all its current fields along with the changes, so unchanged values are kept. Webinar details cannot be edited after creation.
- `toggle_event_status` toggles the status. Check the current status first and tell the user whether the event will be activated or deactivated.
- `create_event` and `clone_event` for a virtual event need webinar details (topic, password up to 10 characters, timezone, duration, start date and time). Ask for any that are missing.
- `create_admin` and `send_event_invite_to_admin` send a real email to the admin. Mention this when confirming.
- `block_admin` removes the admin's platform access until `unblock_admin` is called.

## Errors

If a tool returns an error, tell the user the reason it gives (for example an invalid or missing field) and what to change. Do not retry the same call unchanged.

## Out of scope

The Samaaro tools cannot process payments or refunds, send attendee emails, or read other event platforms. Say so instead of calling a tool.
