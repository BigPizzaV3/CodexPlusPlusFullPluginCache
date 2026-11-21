# GPU and media operations

Use the installed connection's current schemas and `nova_capabilities`. Server support, account GPU access, OAuth grants and host tool exposure are separate checks. Discover actual tools before promising an action. If `gpu_server_start` is absent, report that this host has not exposed the rental command; do not invent it, claim an installation succeeded, or silently change accounts, credentials or execution paths.

## Discover and quote

Read `gpu_server_state`, `gpu_nodes`, `gpu_catalog` and `gpu_templates` as relevant. Reuse a suitable existing GPU when requested. A state of off alone does not authorize rental. Read the exact model's download size, minimum VRAM and compatible template; never silently substitute INT8/Turbo for a requested BF16 bundle. Choose enough disk for all required model files, runtime/image overhead and working space. Use `gpu_server_quotes(disk_gb)` when that optional argument is exposed; otherwise follow the current schema and report its actual quote basis.

Review the actual GPU type/VRAM, disk, idle cutoff, prepaid first hour and maximum ongoing Nova credits/hour. Keep the returned units; legacy `pricePerHrCents` fields represent Nova credits/hour here. Do not invent a price or treat installation time as free. An idle timeout of zero disables auto-off and needs approval of continued billing.

## Explicitly approved rental

When the user requests rental, the tool is exposed, and the account has GPU access and `workflows.generate`, call `gpu_server_start` only after approval of the exact reviewed card, disk, idle settings and cost ceiling. Pass its exact `tier`, `disk_gb`, `idle_off_minutes`, `expected_gpu_type`, `max_credits_per_hour` and `confirm_spend=true`. Reuse valid explicit approval for unchanged scope and cost.

Starting creates one owned rental without installing remembered models or running a workflow. Poll `gpu_server_state`, retain the actual rental ID, node ID and current rate, and inspect state after an uncertain response before another start attempt. Do not blindly repeat this non-idempotent operation. Workflows never rent a GPU or install weights implicitly.

## Separate model and runtime installation

Read the current catalog model/runtime size and dependencies, rental identity and hourly rate. Obtain explicit approval of the download and ongoing GPU time before `gpu_server_model_install` or `gpu_avatar_runtime_install` with `confirm_install=true`. Bind the exact current rental and rate where required. Poll `gpu_server_state` for installed/error or `gpu_avatar_runtime_status` for the returned runtime job. Queued/installing is not readiness. Installation requires `workflows.generate`; personal read/write tokens do not acquire that permission automatically.

For an avatar, reuse the exact selected owned portrait and voice. Read the live node reference for spoken-text, character and voice ports. A shared GPU grants generation access, not permission to reconfigure another owner's hardware.

## Generation and saved results

Set the explicit actual online `gpuNodeId` and returned compatible template ID in the saved workflow. Preflight its current revision and approve generation separately. When `workflow_generate` is exposed and `generationRequiresCard` is false, use explicit chat approval of the exact scope/estimate with the returned preflight ID, stable request ID, `confirmed=true` and exact approved estimated credits. The optional native card still uses UI-only `workflow_run`; never fabricate its private token. Older servers may require their documented native-card flow.

Use `generation_catalog` for hosted image/video/audio/3D models and GPU catalogs for local models. Follow the actual upload schema and capability limits. Preserve returned owned asset IDs/URLs instead of temporary attachment links. Ordinary Output nodes are optional display labels; preserve existing Output nodes and separate `templateOutput` requirements. Read generated media with `workflow_run_results`, and saved node values with `workflow_get(include_results=true)`. Refresh expired result links without regenerating.

## Termination, removal and settings

`gpu_server_terminate` permanently deletes the exact rented instance and disk; it is not a pause. Read its current `expected_managed_rental_id`, explain disk deletion and use explicit approval before `confirm_stop=true`. An already explicit instruction to terminate that rental after completing the agreed work can supply cleanup approval; do not ask again unless the target or scope changes. Cancelling a workflow alone preserves the rental and installed models.

After termination, inspect the same rental with `gpu_server_state`. Charges stop only after verified provider deletion; teardown pending is not completion. Model removal needs exact-model/rental approval and `confirm_remove=true`. Idle-setting changes need explicit approval and `confirm_change=true`. These operations retain their write-grant and ownership checks. Do not broaden grants or remove another owner's files.
