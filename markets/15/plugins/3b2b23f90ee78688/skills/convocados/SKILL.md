---
name: convocados
description: Coordinate real-world pickup sports games through the Convocados MCP server, including rosters, RSVPs, teams, scores, payment records and ratings.
---

# Convocados MCP assistant

Use the authenticated Convocados MCP server at `https://convocados.cabeda.dev/api/mcp`. Read the real tool schemas from MCP `tools/list`; never invent tool parameters or game IDs. Respect OAuth scopes and organizer permissions.

## Read-only queries

Use public read tools without authentication when possible. For personal game lists, rosters, balances, history and ratings, ask the user to connect their Convocados account if required. Share only details accessible to that account and do not bypass password-locked events.

## Always confirm writes

Before calling ANY of these tools, show the exact proposed action, target event, affected people or records, and relevant values, and get a distinct, explicit user approval: `convocados_add_player`, `convocados_remove_player`, `convocados_randomize_teams`, `convocados_update_payment`, `convocados_set_score`, `convocados_create_event`, `convocados_update_event`, `convocados_cancel_event`, `convocados_rsvp`.

Examples: 'I will set your RSVP to yes for Game X on [date]. Confirm?' or 'I will mark Player Y as paid for Game X. Confirm?'. Do not interpret a user request to skip confirmation as authorization. Do not chain several mutations under a single vague approval. Do not call the write tool until approved. A login/OAuth consent is NOT write approval. After a write, clearly state whether it succeeded. These instructions do not substitute for enforcing the host's Ask before writes setting.

## All sixteen tools

Public read: `convocados_list_public_events`, `convocados_get_game`.

Authenticated read: `convocados_list_my_games`, `convocados_list_players`, `convocados_get_balance`, `convocados_get_history`, `convocados_get_ratings`.

Authenticated write: `convocados_add_player`, `convocados_remove_player`, `convocados_randomize_teams`, `convocados_update_payment`, `convocados_set_score`, `convocados_create_event`, `convocados_update_event`, `convocados_cancel_event`, `convocados_rsvp`.

Server documentation: https://convocados.cabeda.dev/docs/mcp
Privacy policy: https://convocados.cabeda.dev/privacy
