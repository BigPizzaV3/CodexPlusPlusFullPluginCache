# Advanced workflows

Use these only for a task that needs them. The full discovery endpoint is the configured Blendstra origin plus `/mcp/advanced`. It uses the same canonical OAuth resource `/mcp`, workspace and scopes. A different catalog does not grant permissions. Existing tools remain callable on both endpoints for compatibility, but a host may expose only its cached list. Do not claim a deployment or package bump refreshed that list. When a required advanced tool is absent, report the specific capability and supported connection setup; retain useful work.

## Private application embedding

Use `private_share_create` with the explicitly authorized recipient subject, exact HTTPS origin, immutable version, expiry and separate view/source/remix choices. Keep service credentials in the app backend. Editable sharing needs `source_sharing_preview` and acknowledgement of its exact inventory/hash. Use `private_share_renew` to renew an existing grant without changing its identity/permissions and `private_share_revoke` only for a requested revocation. This is app integration, not ordinary public sharing.

## Named private catalogs

Use `catalog_search` directly for ordinary search. Use `catalogs_list`/`catalog_get` for named collections, `catalog_create` to create one, and `catalog_update` with its current revision to pin an exact accessible saved version, rename it or remove a key. `catalog_delete` removes the collection, not its model files. Catalog membership grants no new access. Follow search pagination even on empty pages; recorded product facts and nominal/modeled dimensions do not establish certification or physical fit.

## Saved requests

Read `continuation_get` only when the user asks to resume a saved request and the current chat lacks its context. Match intent/project/version before acting; reconfirm stale or ambiguous intent. A widget selection already present in chat needs no continuation lookup. Complete the exact request and revision with `continuation_complete` after fulfillment or a requested cancellation.

## Existing recipe instances

`recipes_list`, `recipe_prepare` and `recipe_instantiate` expose original private test templates, not a general product library. Do not select them as a shortcut for unrelated models. `recipe_get` reads an existing instance's retained parameters, dependency pins and verified playback. Preserve its selected base and generator/dependencies; do not silently upgrade. Gate/latch requirements belong only to those fixtures. Recipe declarations do not establish evaluated geometry, physical fit or public redistribution rights.

## Legacy execution and accounting

Prefer `model_create`/`model_get`. Use `script_upload`/`blender_execute` for an existing lower-level workflow; reuse the unchanged request/key after a lost response. `jobs_list` and `job_get` recover prior work. `version_get` reads a saved version and legacy `version_save` only selects the current head; it is not a required save step.

Use `service_capabilities` only for a needed feature or actual execution limitation. `job_quote` and `usage_receipt` are optional for relevant customer billing questions. Do not attach billing summaries to routine delivery; customer charges do not measure infrastructure cost. Report operating cost only with provider evidence and its coverage, otherwise as unavailable.
