# Errors and limits

Project file reads, writes, and edits have no application-defined file-size cap. File tools have no request quota. Directory traversal remains limited to depth 5 and 1,000 entries, and search to 200 matches within one second. Build, verification, and allowlisted .NET/EF command output is limited to 64 KiB and each operation runs for at most 10 minutes.

Tool rate limits apply per user and tenant, and per project for project-scoped tools:

| Operations | Request limit | Window |
| --- | --- | --- |
| General reads excluding file tools (shared quota); other tools (each) | 1,200 | 1 minute |
| File reads, writes, edits, deletes, directory listings, and searches | Unlimited | — |
| Builds, .NET commands, EF commands, and standards checks (shared quota) | 100 | 10 minutes |
| Verification | 50 | 10 minutes |
| Project creation | 100 | 1 hour |
| Checkpoints | 50 | 1 hour |
| Deployment preparation and deployment (each) | 100 | 1 hour |
| DataPack schema addition tools (each) | 300 | 10 minutes |

Deployment preparation has its own quota; ordinary project reads do not consume it, and preparation does not consume the general read quota.

Common stable errors:

- `NOT_AUTHORIZED`, `FEATURE_DISABLED`, `SCOPE_REQUIRED`: reconnect or ask a QI administrator to restore the required access; do not request a token from the user.
- `PRD_INSTRUCTIONS_REQUIRED`: call `start_prd_discovery` before continuing with a new app.
- `PRD_DECISION_REQUIRED`: finish discovery with `provide_prd`, or use `skip_prd` only if the user explicitly chose to skip it.
- `PRD_DRAFT_REQUIRED`: call `provide_prd` first, then retrieve and display both documents with `get_prd_draft` before requesting approval. The `qi-prd-acceptance` skill documents the same sequence when available.
- `PRD_ACCEPTANCE_REQUIRED`: retrieve the persisted draft, display the complete PRD and complete Technical Requirements, apply edits with `update_prd`, display both complete refreshed documents, and call `accept_prd` only after explicit approval of that exact content.
- `PRD_ALREADY_ACCEPTED`: the draft is locked; proceed to `create_project`.
- `PRD_FLOW_ALREADY_COMPLETED`: the connection already submitted or skipped its PRD; call `create_project` next.
- `PROJECT_ID_REQUIRED`: call `list_projects`, then pass `projectId` explicitly on the tool call; QI will route to that project's isolated runtime.
- `PROJECT_NOT_FOUND`: refresh with `list_projects` and choose an available project.
- `PROJECT_CREATION_REJECTED`: report the tenant billing, project-limit, or access reason returned by QI; do not retry unchanged.
- `PROJECT_BINDING_MISMATCH`: stop because the tenant connection or explicit project authorization headers did not match; reconnect if it persists.
- `PROTECTED_PATH`, `PATH_OUTSIDE_WORKSPACE`, `SYMLINK_NOT_ALLOWED`: the operation is intentionally blocked and must not be bypassed.
- `OVERWRITE_NOT_ALLOWED`: re-read the destination and set `overwrite=true` only when whole-file replacement is intended.
- `EDIT_TEXT_NOT_FOUND`, `EDIT_TEXT_NOT_UNIQUE`: re-read the file and choose a single exact segment.
- `BINARY_FILE`, `LIMIT_EXCEEDED`: narrow the operation; binary files cannot be edited.
- `VERIFY_FAILED`: use the returned bounded output to repair the project, then retry verification.
- A completed build or command can return `success=false`, its exit code, timeout state, duration, and bounded output. Inspect that response, correct the project, and retry when appropriate.
- `COMMAND_FAILED`: the mounted workspace does not have exactly one safe root project file, or the SDK operation could not be prepared.
- `COMMAND_NOT_ALLOWED`: use the dedicated tool for the intended operation: `build_project`, `test_project`, `restore_project`, `clean_project`, `check_project_format`, `add_ef_migration`, `remove_ef_migration`, `list_ef_migrations`, `check_ef_migrations`, or `update_ef_database`. Configuration, where supported, must be Debug or Release. Migration and context names must match the documented formats. Raw arguments cannot be supplied.
- `PROJECT_STANDARDS_FAILED`: call `check_project_standards`, correct every blocking template, architecture, browser-storage, demo-removal, or EF migration finding, then retry verification.
- `RATE_LIMITED`, `MCP_RUNTIME_UNAVAILABLE`, `BACKEND_UNAVAILABLE`: retry only when the error reports that retrying is safe.
- `DEPLOYMENT_PLAN_EXPIRED`, `DEPLOYMENT_PLAN_STALE`, `DEPLOYMENT_PLAN_CONSUMED`: call `prepare_deployment` again and obtain confirmation for the new plan.
- `DATAPACK_DECISION_REQUIRED`: present the DataPack decision and obtain the required `copy_test_rows` or `schema_only` choice, or confirmation of pending schema application.
- `DATAPACK_STATUS_FAILED`, `DATAPACK_DEPLOY_FAILED`, `PUBLISH_FAILED`: report the structured deployment failure; do not claim production was updated.
- `DATAPACK_ACCESS_DENIED`, `DATAPACK_DEFAULT_REQUIRED`: use only packs linked to the explicit `projectId`; schema additions require that project's configured default pack.

Project creation is limited to 100 requests per hour per user/tenant. `create_project` requires `projects:write`, consumes an active PRD decision for the OAuth connection, initializes the standard template only into an empty new workspace, and returns the created project ID for subsequent explicit tool calls. PRD and Technical Requirements documents are limited to 512 KiB each, and an unfinished PRD flow expires after two hours.

Deployment plans expire after 10 minutes and are single-use. Deployment preparation and deployment each allow 100 requests per hour per user/tenant/project. DataPack list page size is 1-100; application logs accept 1-500 entries and a 1-1440 minute range. New deployment/DataPack/log OAuth scopes require reconnecting the plugin.

Protected paths include `.git`, `.qi`, `.ssh`, environment files, secrets and private keys, SQLite/database files, production appsettings, and generated `bin`, `obj`, `node_modules`, and `wwwroot` directories.
