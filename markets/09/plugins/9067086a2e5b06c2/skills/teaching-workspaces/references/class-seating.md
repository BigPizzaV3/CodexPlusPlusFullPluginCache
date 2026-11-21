# Deterministic seating without pupil records in ChatGPT

Privacy boundary: this public plugin is for adult educators and creators. Never
transmit personal information about children under 13 to OpenAI. Use anonymous
or synthetic inputs only; do not request, send or retrieve pupil names, pupil
ids, rosters, photographs, scripts, individual answers or individual results.
Apply this boundary whenever ages or identifiability are uncertain. Do not
open, screenshot, upload or read back private pupil records through a browser
or another connector. Give the exact native link and hand the sensitive step
to the adult user to complete independently. Do not read a record first merely
to decide whether it contains personal information.

Discover these five public operations in `tools/list` first. They use existing
owned-class/saved-plan services with no AI prefill or provider call. Native
capacity, shelf, rate and seating-family access limits remain authoritative.

| Operation | Required scopes |
| --- | --- |
| `preview_class_seating_plan` | `classes:read` |
| `create_class_seating_plan` | `classes:read`, `classes:write`, `tools:write` |
| `list_seating_plans` | `tools:read` |
| `get_seating_plan` | `tools:read`, `classes:read` |
| `delete_seating_plan` | `tools:write` |

Select the owned class from `list_my_classes` summaries. A request to prepare
seating for that class allows the backend to use its roster internally; set
`use_class_roster_confirmed:true` only for that actual request. Preview/create
accept the selected `class_id`, anonymous `title` and
`layout:{kind,rows,across}`. Supported kinds are `singles`, `pairs`, `groups4`
and `groups6`, within 1–60 pupils/seats. Do not truncate a class to make it fit.

The public schema accepts neither pupil `assignments` nor `include_pupils`.
Results contain safe plan-level geometry/counts only. Saved titles are omitted,
as are pupil names/ids and individual desk assignments. Do not infer or
reconstruct which pupil sits where. The public surface does not offer a
seating-update operation. Named
placements, roster changes, advanced rules/geometry, later adjustments and
PDF/print are independent adult actions in the exact native editor.

Saving a plan participates in native later seating-to-class reconciliation,
so explain that linkage and request `classes:write` consent for creation.
Existing class tags/colour groups and stale/native constraints may require the
adult's editor. Do not bypass a refusal or flatten advanced state.

Use `list_seating_plans` (`page`, `limit` up to 50) and an exact owned `plan_id`
with `get_seating_plan` for safe summaries, never raw snapshots. Creation returns
a real saved-plan/native editor link. Provide that link without opening,
screenshotting or reading its private roster/placements back into ChatGPT.
There is no seating-specific MCP PDF renderer and no export workaround through
saved-tool CRUD.

`delete_seating_plan` requires the exact owned `plan_id`, the adult's explicit
confirmation and `confirmed:true`. It deletes that saved plan, not My classes.
Check the actual result and do not blindly repeat an ambiguous deletion.
