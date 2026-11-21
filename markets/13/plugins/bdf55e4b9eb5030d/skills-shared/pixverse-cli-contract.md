# PixVerse CLI Contract

The packaged `pixverse_runtime/cli-compatibility.json` is authoritative for the supported CLI
minimum, Node.js requirement and supported capability schema. Use runtime doctor to inspect active requirements. Both managed channels share the
same floor; the online install target is npm `latest`. Newer compatible releases do not require a configuration update.

Use this document for installation, discovery, templates, Canvas and delivery rules.
Use `./pixverse-cli-models.md` only for model selection and `./pixverse-cli-cheatsheet.md`
for command syntax. These are current contracts, updated in place when supported behavior
changes. Git history and test fixtures retain earlier release evidence.

## Managed Installation

Online bootstrap installs or refreshes npm `latest` in the private runtime, then
verifies the installed version against the minimum. A registry mirror serving an
older package cannot make setup ready. Unsupported cached readiness is invalidated
without clearing credentials or forcing login. A global CLI upgrade does not update
this runtime; use the wrapper's authorized `bootstrap --yes`, followed by doctor.
Do not refresh an already-supported runtime merely because a skill was loaded.

Local builds validate and activate their embedded internal ZIP, with no npm fallback.
Both explicit and discovered bundles must meet the minimum CLI version and Node requirement,
and pass capability/schema and archive checks. The built package records the actual artifact
hash for activation and recovery; no separate internal release version is pinned.

## Capability Discovery

- `pixverse capabilities --json` and `pixverse capabilities create [mode] --model <id> --json` expose
  the normalized Create contract offline, without login or a network request.
- The Create capability domain is authoritative for required fields, defaults, enums, ranges, units,
  model support, and reference-media limits.
- The plugin canonicalizes the two reviewed `create reference` duration encodings to string seconds
  plus `auto`; public numeric `0` is the CLI's `auto` sentinel, not a literal zero-second duration.
- Canvas contracts are live and authenticated: use `pixverse capabilities canvas --json`, with
  `pixverse canvas node schema --node-type <type> --json` only as a targeted fallback.
- `create reference` requires a non-empty prompt.
- Global region accepts `global` or `cn`; `PIXVERSE_REGION` overrides `--region`.

## Task And Command Behavior

- Process exit code `7` means `CONCURRENCY_LIMIT`; wait for a slot and retry the same intent instead
  of treating it as an ordinary failure.
- `task status` accepts space-separated positional ids; `--ids 123,456` remains valid for compact
  batch polling.
- `create upscale` targets only `2160p` and defaults to it.
- Google Lyria 3 Pro supports auto lyrics, instrumental generation, and image references. Put
  lyric-like direction in `--prompt`; it does not support a separate `--lyrics` value.
- Read-only `miniapps list` and `miniapps info` are available. Paid `miniapps create` remains outside
  the plugin queue until it has dedicated preflight, receipt, polling, and recovery support.
- CLI 1.4.13 introduced optional GPT Image 2.5 `--background auto|transparent|opaque`
  and `--relax-mode [boolean]` / `--no-relax-mode` on video, image, transition, modify,
  reference and motion-control. Check the active capability before using these on an older
  supported runtime. Leave Relax mode unspecified unless requested; its benefits and model/account
  eligibility are backend-owned and do not bypass membership or paid preflight.

## Templates

`template categories`, `template list --category --page --limit`,
`template search <query>` and `template info <id>` support discovery. Search returns
service-provided matches without CLI pagination or category flags. Use
`../skills/pixverse-template/SKILL.md` for selection, preview caching and creation.

Published Canvas templates use `create template`:

- Sources 21/22 use detail `input_fields`, ordered image slots, and at most one
  text and one video input. Ambiguous optional bindings and unsupported fields
  fail validation before submission.
- Output settings are template-defined; quality, duration, aspect, count, seed,
  off-peak and idempotency overrides are rejected.
- Submission returns `outputs[]` containing typed `media_id` / `media_type`
  receipts, optionally `set_id`. Preserve and poll all image/video outputs.
- A partial or invalid receipt may represent paid work. Keep known IDs and stop
  automatic resubmission. The plugin writes submission intent before sending.

The plugin queue resolves ordinary image-template output correctly and records
multi-output results, polling/downloads and partial recovery. A published template
is a Create route, not a request to manage a Canvas project graph.

## Canvas Adapter

- `bindings.canvas_cli` remains an offline discovery declaration. The canonical Canvas-to-Create mapping now comes from each live node's `capability_adapter` record rather than that static list.
- Canvas runtime discovery uses `pixverse capabilities canvas --json`; use `--raw` only to inspect the unmodified service response. This command is live and authenticated. Targeted fallback remains `pixverse canvas node schema --node-type <type> --json`. The adapter revision is `canvas_cli_capability_adapter.v2`.
- `pixverse capabilities canvas` supports `--node-type`, `--selector`, `--model`, `--raw`, and `--refresh`. Reuse one merged response and query a node schema only when the needed contract is missing or structurally incomplete.
- The merged CLI response uses `nodes[]`: `nodes[].canvas` is the source Graph contract, while
  `nodes[].routes[].cli.capability` is the resolved Create command contract. The Wrapper accepts the
  older `node_types[]` envelope only for compatibility and never treats a Create target type as proof
  of a Canvas source-payload type.

The runtime publishes `canvas_cli_capability_adapter.v2` selector routes and field mappings for
generation nodes. The plugin Wrapper uses them as the canonical contract and keeps a narrow legacy-input
shim only for reviewed aliases: `reference` → `reference_to_video`, `resolution` → `quality`, boolean
`audio=false/true` → numeric `0/1`, provider-path materialization for image/video/audio references, and
legacy `image` → canonical `image_to_video.customer_img_path`. Paid preflight rejects malformed legacy
graph nodes before account lookup. The adapter does not map `create_count`, `count`, or `n`, so one
Canvas generation node means one output.

The reviewed selector set is `text_to_image` / `image_to_image`, `text_to_video` /
`image_to_video` / `reference_to_video`, and `text_to_music` / `text_to_speech`. Paid preflight
checks the selector-specific mapped values against the bundled offline `image`, `video`, `reference`,
`music`, and `voice` Create contracts. Image-to-image requires concrete provider-backed image paths;
speech requires a preset or provider voice ID; music follows the model's lyrics/instrumental/auto-lyrics
rule. The current music adapter does not map `duration_seconds`, so manual duration is not accepted by
the Canvas wrapper. `text_generate` is payload-schema-only and intentionally does not require an adapter.

Ordinary Create uses the CLI's boolean `--audio` / `--no-audio` flags. Persisted Canvas
`video_generate` payloads use the verified numeric `audio=1/0` switch until the runtime capability
publishes a Canvas source-payload schema or an explicit type transform.
Do not copy ordinary Create defaults into Canvas nodes merely because both surfaces mention the same
model.

## Region

The CLI supports global `--region <global|cn>` with default `global`; `PIXVERSE_REGION` overrides the
flag. The Wrapper recognizes the option before or after the command so it cannot bypass paid-command
classification. Canvas bindings persist their region. For a guarded Canvas workflow, set one
`PIXVERSE_REGION` for project creation, graph reads, preflight, submission, and recovery; do not mix
regions or add a one-off `--region` to a Canvas subcommand. A legacy binding without a region is
treated as `global`.

## Canvas Project IDs And Layout

CLI 1.4.13 forwards a patch's non-negative safe-integer `base_edit_version` unchanged,
even when it differs from the latest graph. The plugin still compares patch apply's version
with its fresh graph read and rejects stale patches before mutation. Read and reconcile the
graph after a conflict; do not rewrite only the version to force a patch through.

The CLI accepts an optional positional project ID on project-scoped Canvas commands.
The wrapper supports both `canvas graph get <id>` and `canvas graph get --project-id <id>`:
it normalizes the positional alias before region, binding, checkpoint and paid-plan checks.
Conflicting positional/flag IDs stop before any remote request. Existing bindings still work
when the project ID is omitted.

`canvas arrange` saves the entire project's layout without an edit-version precondition.
It follows the existing non-atomic mutation contract: review the current checkpoint, then
use `--allow-non-atomic-canvas-mutation --json` for one pre-read, one mutation and one post-read.
When the user requests arrangement, include this wrapper flag as part of carrying out that
request; do not introduce another user approval step solely for the flag. The response does
not include updated nodes, so readback is required. If no verifiable receipt version is
returned, preserve the successful result and use `canvas sync` to review the latest state;
never retry a successful arrangement to obtain a receipt. Versioned layout patches remain
available through `canvas patch apply`.

## Downloads

Downloads publish completed files without overwriting existing files or symlinks.
Audio destinations can be explicit files; a collision requires another output path.
Remote names, extensions and IDs are validated, and temporary upload downloads use
the same non-overwriting publication behavior. A download failure still does not
invalidate generation: recover the free download instead of generating again.

## Surface Boundaries

The queue supports the reviewed Create modes, including image/video templates and
published templates with multiple typed outputs. MiniApps paid generation remains
outside that queue until dedicated preflight, receipt, polling and recovery support
exists. Do not bypass preflight with a direct paid command. Destructive account,
asset and configuration operations require the user's intended action.

Canvas must advertise each selected model and route in its live adapter. Offline
Create support does not establish Canvas model availability or account entitlement.
For example, `flux-3.0` is a video/I2V choice and `wan-3.0` supports video, reference
and two-frame transitions; Wan audio-only reference input is allowed by Create,
but Canvas still requires its own live route contract.

Audio metadata may omit per-model prompt, lyrics and voice text limits. Do not
recover removed limits from old manifests; inspect the active offline contract.
A supported catalog or successful offline check is not evidence of live paid access.
