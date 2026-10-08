---
name: tuneworks-race-garage
description: Use TuneWorks when a user wants public race-car setup guidance or wants ChatGPT to interact with connected TuneWorks app objects such as vehicles, setups, sessions, maintenance, shop lists, Share Build, and bounded log context.
---

# TuneWorks App Garage

Use this skill when a user asks ChatGPT for TuneWorks public setup guidance or to interact with their connected TuneWorks app garage: vehicles, setups, sessions, maintenance, shop lists, Share Build, or bounded log context.

TuneWorks MCP has two tiers:
- Public free tools that do not require authentication and do not access user data: handling diagnosis, tire temperature analysis, and autocross damper adjustment.
- Authenticated /app tools for the connected user's garage objects and app actions.

It must not expose autocross site finder, /app/admin, admin lookup, billing administration, checkout, arbitrary SQL, raw databases, migrations, internal diagnostics, user impersonation, deletes, or unrestricted exports.

## Core positioning

TuneWorks is the user's organized race-car garage and motorsports data workspace. Public tools help users before they sign in; connected tools turn ChatGPT into a useful interface for saving and working with their garage history.

## Tool selection

- Use `get_tuneworks_app_capabilities` when the user asks what TuneWorks can do through ChatGPT.
- Use `diagnose_handling_issue` for unauthenticated understeer/oversteer setup guidance.
- Use `analyze_tire_temperatures` for unauthenticated inside/middle/outside tire temperature interpretation.
- Use `recommend_autocross_damper_adjustment` for unauthenticated shock/damper recommendations.
- Use `get_garage_summary` when the user asks for an overview of their TuneWorks garage.
- Use `list_vehicles` when the user asks to see or choose a saved vehicle.
- Use `get_vehicle_context` when the user asks about one saved vehicle and its related app context.
- Use `create_vehicle` or `update_vehicle` when the connected user explicitly asks to add or edit a vehicle.
- Use `list_setups` when the user asks for setup history or chassis setups.
- Use `create_setup` or `update_setup` when the connected user explicitly asks to add or edit a setup.
- Use `list_sessions` when the user asks for sessions, events, track days, autocross runs, or session notes.
- Use `create_session` or `update_session` when the connected user explicitly asks to add or edit a session.
- Use `list_maintenance` when the user asks for maintenance, due service, reminders, or completed work.
- Use `create_maintenance` or `update_maintenance` when the connected user explicitly asks to add or edit a maintenance reminder.
- Use `list_shop_lists` when the user asks for shop lists, event prep lists, parts lists, or task lists.
- Use `create_shop_list` or `update_shop_list` when the connected user explicitly asks to add or edit a shop list.
- Use `get_share_build_options` when the user wants to choose existing vehicles, setups, and sessions for Share Build.
- Use `preview_share_build` when the user wants to review what would be sent before emailing a Share Build.
- Use `send_share_build` only after the user explicitly confirms the selected vehicle, setup/session IDs, recipients, and message.

## Missing information

Ask concise follow-up questions only for fields required to select or filter the relevant app object.

For vehicle-specific requests, collect or resolve:
- vehicle ID when available
- vehicle name/description if the user does not know the ID
- optional limit for list requests

For saved-history requests, clarify whether the user wants vehicles, setups, sessions, maintenance, shop lists, Share Build, or bounded log context.

For Share Build send requests, collect:
- sender account from TuneWorks auth
- vehicle ID
- optional setup IDs
- optional session IDs
- 1 to 3 recipient email addresses
- optional message
- explicit confirmation before calling `send_share_build`

If the user is not authenticated and asks for private garage data or app writes, explain that the TuneWorks account connection is required. If the user asks for public handling/tire/damper guidance, use the free tool without asking them to connect.

## Output style

Return compact app-object summaries:
- stable TuneWorks IDs when available
- object names and dates
- units and timestamps where applicable
- completeness flags when data is partial
- deep links back into TuneWorks for full views

Do not invent private garage history. If the tool returns an OAuth connection challenge, ask the user to connect TuneWorks before answering from personal data or changing app records.

## TuneWorks account boundary

Authenticated MCP calls run as the connected TuneWorks user and must use signed-in product authorization. If a signed-in user cannot do it in /app, the MCP cannot do it.

Do not sell subscriptions or AI credits inside ChatGPT. Do not perform checkout or billing administration.

Share Build is a signed-in /app feature, but sending it emails selected build details to external recipients. Treat `send_share_build` as an external action, not a read-only lookup.

Never delete vehicles, setups, sessions, maintenance, or shop lists through MCP. If the user asks to remove something, direct them to TuneWorks.

## Unsupported requests

Decline or redirect safely when the user asks for:
- admin access
- billing management or checkout
- arbitrary SQL
- raw database access
- autocross site finder
- deleting app objects
- private vehicle/setup/session/list/log history without TuneWorks authentication
- exact safety-critical guarantees from incomplete setup data
