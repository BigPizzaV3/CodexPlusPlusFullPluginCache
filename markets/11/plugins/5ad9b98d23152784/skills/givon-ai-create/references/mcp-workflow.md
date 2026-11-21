# Givon AI MCP Workflow

Use discovery first, then generation.

## Tools

| Tool                          | Use                                                           |
| ----------------------------- | ------------------------------------------------------------- |
| `givon_list_models`           | Browse available image/video/music/voiceover models.          |
| `givon_get_model_schema`      | Read JSON Schema for one model input.                         |
| `givon_quote_generation`      | Token cost of a request before running it, when available.    |
| `givon_generate_content`      | Start an async generation job.                                |
| `givon_get_generation_status` | Poll job state and output assets.                             |
| `givon_get_balance`           | Check token balance before expensive or quota-sensitive jobs. |
| `givon_upload_file_asset`     | Upload a ChatGPT native file parameter and return `asset://...`. |
| `givon_import_asset`          | Import an HTTPS/data URI asset and return `asset://...`.      |
| `givon_list_assets`           | List reusable owner media assets.                             |
| `givon_get_asset`             | Inspect one owner media asset by id or `asset://...`.         |
| `givon_archive_asset`         | Soft-hide an owned asset from active lists and future reuse.  |
| `givon_list_voices`           | Voices for `input.voice` on a voiceover generation.           |
| `givon_list_avatars`          | Ready Studio avatars and their reusable reference views.      |

## Generation

1. Choose an active model from `givon_list_models`.
2. Read schema with `givon_get_model_schema`.
3. Validate requested fields against `properties`, `required`, `enum`, numeric
   limits, defaults, and `x-*` extensions.
4. Quote and confirm the exact `{type, model, input}` as in the root skill.
   Send it unchanged to `givon_generate_content` with the quoted `maxTokens`,
   `wait: true` and a stable `idempotencyKey` for this request.
5. Poll with backoff until a terminal status.

## Assets

- Use `givon_upload_file_asset` when the host provides a native ChatGPT file
  parameter. Use `givon_import_asset` for HTTPS URLs or data URIs. Use the CLI
  `givon asset upload <path>` for local files in generic MCP clients because
  the remote MCP server cannot read local disk.
- Keep the returned `assetUri`. Pass it only into schema-supported media fields
  after `givon_get_model_schema`.
- Use `givon_archive_asset` only when the user explicitly wants to hide an
  owned asset; it is a soft archive that keeps audit links intact.
- Put every model-specific asset field inside the `input` object passed to
  `givon_generate_content`; MCP no longer exposes named asset shortcuts.

Terminal statuses are `succeeded`, `failed`, and `canceled`. A failed generation
can be a successful MCP transport response; inspect `errorCode` and
`errorMessage`.

## Errors

- Missing required field: ask for that exact field or use a schema default.
- Validation error: remove unsupported fields and retry with schema-supported
  keys only.
- Failed job: explain `errorCode`/`errorMessage` in user language and suggest a
  concrete prompt/input adjustment.
- Balance uncertainty: call `givon_get_balance`; do not guess available quota.
- Local file upload needed in MCP-only context: use the host-native file
  parameter tool, or `givon_upload_asset` when the host can read actual bytes.
  Otherwise ask for an accessible HTTPS media link or an existing Givon asset.
  Use CLI upload only when a shell is available. Do not invent an attachment URL.
- An uncertain launch or wait timeout: reuse the original idempotency key and
  unchanged request, or check the accepted job's status; do not start a second job.
