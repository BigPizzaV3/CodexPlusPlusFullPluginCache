# OpenAI v2 — composition from published individual tools

These examples apply only to the `/mcp/openai-v2` review surface. Follow live tool schemas and the user's intent; they are not additional backend workflows.

## Remember and retrieve

- On “Remember privately that our boiler was serviced on 14 October”, use `remember` for the verified fact.
- On “Who serviced the boiler?”, use `find_memory`. If unavailable, say so rather than guessing.
- On a genuine correction or deletion, resolve the accessible record first, then use `update_memory` or `forget_memory`.

## Shopping and packing lists

- On “Start a packing list”, call `create_list` when no appropriate existing list has been identified.
- On “Add sunscreen”, resolve the relevant list with `get_list` and call `add_list_item`.
- On “We packed sunscreen”, resolve the item and call `complete_list_item`.

## Tasks, reminders and important dates

- For existing obligations use `get_tasks`.
- If the user supplies a valid actionable schedule and explicitly requests a reminder, call `create_scheduled_task`.
- Complete an identified task only with permission using `complete_task`.
- Retrieve or create canonical family dates with `get_important_dates` and `create_important_date`, rather than pretending a date entry is the same as a scheduled task.

## Decisions, Pages and notifications

- Retrieve recorded decisions using `get_decisions` and persist user-confirmed outcomes with `record_decision`.
- Read the available existing Pages with `get_shared_spaces`. Creating, editing and sharing Pages are not enabled in v2.
- Read notifications with `get_notifications` when asked.

## Unsupported operations

Do not promise price or condition watches, shared Page creation, visibility changes, external transactions, recommendation redirection, profile bootstrap, or generic `butler_*` router actions. This endpoint does not publish those tools. Explain the limitation rather than replacing the unavailable operation with an unrelated memory or task.

## Privacy / no false claims

Only act on data accessible to the connected principal. Missing or private information is not proof the data does not exist. Avoid credentials and government identifiers. Never invent tool results, returned URLs, reminders, or monitoring. Confirm successful writes after the tool responds.
