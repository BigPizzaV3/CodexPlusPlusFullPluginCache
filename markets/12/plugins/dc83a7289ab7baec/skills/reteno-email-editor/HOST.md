# Reteno plugin host adapter

Resolve `<plugin-root>` from this installed skill's parent `skills/` directory. Bundled SDKs
and manuals work from a plugin cache, independently of the current project directory.
The selected Codex or Claude MCP connection supplies OAuth. Bundled connection settings allow
660 seconds for long audience/workflow calls; do not lower that deadline for those tools. Never read host credential files,
add `X-Reteno-Agent`, or depend on publisher/session/proxy variables. Reteno only.

## Signed file transfers

Use exact signed URLs and HTTP methods from MCP manifests. A ticket is tied to the selected
account and environment; do not invent URLs. Preserve downloaded model bytes as the merge base.

```sh
python3 <plugin-root>/scripts/transfer.py download --url '<ticket>' --output <file>
python3 <plugin-root>/scripts/transfer.py upload --url '<ticket>' --input <file> --content-type application/json --method PUT
```

Use the artifact's actual MIME type (`text/html`, `text/css`, `image/png`, etc.) and returned
byte limit (`--max-bytes`). Pass `--sha256` for downloads when the manifest supplies a checksum.
The helper accepts only the configured MCP HTTPS origin, pins checked public addresses, refuses
redirects, bounds bytes and atomically replaces successful downloads. Never print signed URLs.
Its `transferred:true, persisted:false` result is not a save receipt; call the appropriate MCP
finalizer and verify fresh state. For hosted assets on a CDN, use the host's normal image/browser
inspection capability; this helper is intentionally limited to MCP artifact tickets.

## Supplied images and image jobs

For a supplied image, follow the skill's image-upload reference using its original local bytes.
Inspect the image first. `prepare_image_upload` → exact image ticket PUT → `upload_image`.
Require an error-free result with `data.url` containing the final HTTPS URL. Reuse a successful
asset URL if a later document save needs repair. Hosting failure never authorizes regeneration.

Use Reteno MCP `generate_image` or `edit_image` only when new or changed artwork is requested.
Read the live schemas; use their default model and medium quality unless explicitly requested
otherwise. Each call produces one image. Inputs are HTTPS URLs or prepared `uploadSessionId`
references, not file paths/base64. Up to ten total input files are accepted; edit counts the
base, references and optional mask. Keep `textPolicy="preserve"` unless text changes were
requested. Masks require matching dimensions and alpha. Preserve source transparency unless
asked to change it. Default delivery limits are 1536px per edge, 1,572,864 pixels and 3 MiB;
respect the deployed schema/config if stricter.

Save the exact request and a unique `idempotencyKey` before submission. Keep `jobId`. Poll
`get_image_job` at `pollAfterSeconds`, with a ten-minute local deadline. A timeout is incomplete,
not a reason to create another job. Retry only a documented retryable processing failure with
IDENTICAL arguments and the SAME key, after `error.retryAfterSeconds`, at most once. Unknown
provider outcomes must not be regenerated. A new key may create a new charge. Never run a
batch of variations just to choose one. Inspect the completed hosted result before using it.

Server quota enforcement is authoritative. The plugin does not claim a cross-user spending cap.
Each user request is scoped to its requested number of images. Test-run budgets belong to the
explicit test instructions and must not be expanded through recovery or variations.

## Completion

Use the pinned SDK and the shared persistence instructions: distinct base/target tickets, stable
operation identity, fresh model read, exact requested-field checks and saved desktop/mobile
preview inspection. Preview retrieval alone is not visual verification. Native preheaders use
`metadata.preheader`; verify its saved JSON and compiled hidden preheader. HTML localization
owns existing HTML preheaders through `reteno-email-editor`. Do not save a stale native model
over newer localized HTML. Keep the destination ID on every recovery path.
