<!-- Generated from the Scenivia tool catalogue. Do not edit by hand. -->

# Scenivia refusals

A refused call returns `isError: true` with a JSON body: `code`, `message`,
`retry`, and sometimes `retryAfterSeconds`, `operationIndex` and `reason`.

| Code | Retry unchanged | What to do |
|---|---|---|
| `unauthenticated` | no | Reconnect: the token is missing, expired or revoked. |
| `insufficient_scope` | no | Ask the person to grant the scope named in the message, then retry. |
| `not_found` | no | Check the id with a list or read capability; it may belong to another account. |
| `forbidden` | no | This account may not do that: on this project, or on its plan (agents need Pro or Max, the message gives the upgrade link); tell the person, do not retry. |
| `invalid_input` | no | Fix the arguments against the input schema; the message names the field. |
| `rejected_operation` | no | Read operationIndex and reason, inspect the layer again, and send a corrected batch; a composed screen lists issues, each with its block and a hint. |
| `stale_revision` | no | Read the project again with get_project and prepare the change on the new revision. |
| `already_applied` | no | Nothing to do: read get_turn for the revision it was applied at. |
| `requires_open_studio` | no | The person applies this turn in the open Studio; tell them. |
| `no_studio_document` | no | Ask the person to open the project in the Studio once, which saves its Studio film; start a storyboard job only when the message says none exists. |
| `conflict` | no | The project changed state; read it again before deciding. |
| `insufficient_credits` | no | Tell the person; credits are bought in the product, never by an agent. |
| `too_many_active_renders` | yes | Wait for an export to finish (get_render), then retry. |
| `asset_limit_reached` | no | The project holds as many pictures as it may: reuse one already in list_assets, or ask the person to remove one. Do not retry. |
| `rate_limited` | yes | Wait retryAfterSeconds, then retry once. |
| `gone` | no | The file was purged or expired; start a new export if the person wants one. |
| `unavailable` | yes | The feature is off or busy here; retry later or tell the person. |
| `upstream_failed` | yes | A dependency failed; retry once after a short wait. |
| `internal_error` | no | Something failed on the server; report the reference in the message. |
