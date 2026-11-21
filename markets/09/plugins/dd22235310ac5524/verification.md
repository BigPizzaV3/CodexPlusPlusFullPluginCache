# Plugin verification scenarios

These are runnable acceptance scenarios, not recorded successful evaluations. Packaging tests establish that the bundle contains its referenced files. They do not prove automatic selection, successful OAuth, real Blender execution or directory approval.

Use a fresh conversation for each selection case with the final plugin installed, a working OAuth connection and a test workspace. Record the host/client version, model, plugin version, prompt, actual skill/tool trace, project/version/job IDs, observed result and pass/fail. For compute cases, use the user's authorized test scope and existing execution limits. Ordinary creation must not introduce budget, quote or price-version forms. Supply actual fixture IDs in the conversation; never treat the sample descriptions below as IDs.

## Refresh and verify an existing connection

Identify how the actual host connection was installed before changing it. A working connection does not establish its installation type or current catalog.

- **Existing ChatGPT developer-mode MCP connection:** open that connection in ChatGPT Plugins, select **Refresh**, inspect the changed metadata, then start a new conversation for acceptance. This is the [documented metadata refresh flow](https://developers.openai.com/plugins/deploy/connect-chatgpt#refresh-metadata), checked September 15, 2026. Reuse working authorization unless the host actually requires sign-in.
- **Published plugin:** tool updates use the host's continuous review process. Submitted plugin information or imported skill changes require a new version, review and publication. Do not apply developer-mode instructions to a published installation or claim a source merge updated it.
- **Local Codex or other client:** use that client's supported connection reload and inspect its newly discovered tools. Local configuration does not update a hosted ChatGPT connection.

Package **1.8.0** and catalog **1.12.0** provide focused default discovery, with authoring guide **2026-10-04.2**. Check the actual connected schema and response rather than inferring refresh from a package version.

- Standard `/mcp`: 38 agent tools plus two app-only widget tools. Creation, inspection, sharing/remix and source-linked content remain discoverable. `version_set_current` is present; quotes, receipts, fixture recipes and legacy `version_save` are absent from this list.
- Advanced `/mcp/advanced`: all 59 agent tools plus those same widget helpers. OAuth still uses the canonical `/mcp` resource and existing scope checks. Verify unauthorized writes, unsafe origins and URL-supplied tenant context remain rejected on both paths.
- An old client can still call its legacy tools at `/mcp` under the same permissions. Test a legacy call without requiring a new connection.
- Find a saved project with `projects_list.q`, including a filtered empty page followed by `nextCursor`. Read one material helper and reuse it for multiple preset IDs; a metadata-only material call must omit Python while retaining its helper hash.
- Restore an existing version through `version_set_current`; check stale-base rejection and unchanged-request replay through both the new name and legacy alias.

Historical observations remain in `docs/CLIENT-CONNECTIONS.md`. Current host selection, mobile rendering and production execution still require actual acceptance evidence.

For photo/product reconstruction, run the [reference-modeling verification case](https://github.com/Fenceline/blendstra/blob/main/docs/verification/2026-09-28-reference-agent-modeling.md). Verify actual image inspection, matched-view comparison, corrective revisions, editable source and exact saved-model delivery. Quality remains unverified until those real agent runs and visual reviews are recorded.

Check `model_show`, `model_create`, `model_get`, `project_open`, `project_context_get`, `model_edit`, `artifact_upload_prepare` (including `prepared_glb`), `prepared_model_import`, and the sharing/remix/content tools used by the cases. The two `model_widget_*` tools must stay app-only. Public publication access must not be treated as private project access. Fresh registration must preserve truthful tool annotations and current authorization.

## Launch acceptance: interactive delivery and useful sharing

These five positive and three negative cases are prepared review scenarios. Bind actual fixtures and reviewer credentials before submission; do not report them as passed from package tests. Use fresh supported desktop and mobile ChatGPT sessions for UI cases and a client without UI for the link fallback. Record visible rendering separately from a successful `model_show` response.

| ID | User prompt and fixture | Expected result |
| --- | --- | --- |
| L01 | Make a miniature treehouse I can rotate and explore here. Empty authorized workspace. | Create once with defaults, verify that operation's saved result, show its interactive card and durable link. Orbit/pan/zoom work; source stays private. Reopen the same result in a fresh session without another modeling job. |
| L02 | Show this GLB from another tool so I can inspect every side; keep it private. Supported self-contained GLB with frozen hash. | Prepare/upload/import as `prepared_glb`, then show the returned exact saved version. Verify matching model bytes, no Blender job, real rendering and no source-edit/remix promise. With unavailable binary transfer, report the upload handoff honestly. |
| L03 | Change only the part I selected and show me the result. Source-backed model, eligible part and requested operation. | Preserve exact selection/base, use an eligible edit or authorized scoped source revision, verify unaffected properties and show the new operation's saved version. Reopen the earlier version. A stale selection requires deliberate base choice. |
| L04 | Share this model as an interactive page; keep downloads and remixing off. Owned saved version and publication scope. | Return the actual canonical public page, verify it while signed out, and preserve both restrictions. The private card itself is not a public share. Honor the selected fixed/current behavior. |
| L05 | Make my own version of this shared model and change its base. Permissioned source-backed public fixture. | Inspect current permission/version, create a private attributed remix, edit and display its saved result. Original is unchanged and source attribution remains recoverable. A view-only fixture produces no copy or edit. |
| L06 | Make a flat poster image of a futuristic lamp. | Use an image workflow; no Blendstra invocation for a generic 3D look. |
| L07 | Write a Blender script I can run locally; do not upload or execute anything. | Return the script; no Blendstra upload, model job, card or sharing operation. |
| L08 | Open this public model so I can look around; do not make a copy. View-only public fixture. | Return its interactive public page; no private `model_show` call without project access, no remix, publication or permission expansion. |

For each positive case also record interruptions, model/poster loading and supported recovery. Resume an expired card on its same saved version without regeneration or public sharing; explicit denied access must stay denied. A host without UI receives the exact-version link and no claim of an in-chat rendering. Record time to visible card, completed revision, deliberate sharing, recipient viewing and completed reuse separately; this package adds no telemetry and claims no growth measurement.

## Relevant tasks

| User prompt | Test account / fixture | Expected behavior and result |
| --- | --- | --- |
| Make an editable 3D desk lamp with a red shade, render a preview and keep the source. | Empty writable workspace and available CPU execution. | Select the modeling workflow without the brand name. Read the released authoring guide, submit `model_create` with title/script/idempotency key and retrieve the saved result through `model_get`. Inspect an actual poster and geometry without mandatory quote or price selection. Call `model_show` for the exact saved result and return its private viewer link; export files only when requested. No gallery lookup or manual project/upload choreography is required. |
| Change only the handle on my saved model to aqua. Keep the earlier version. | Accessible source-backed project, selected version and handle object ID. | Open and inspect that version, edit from its source and inspect the new saved version. Confirm the earlier version is still retrievable and unaffected geometry remains. |
| Import this GLB and keep an editable version I can come back to. | A small valid GLB file and a host with binary HTTP transfer. | Prepare an `input_glb` upload in a new project, transfer matching bytes and process it with Blender using released defaults, then return durable project/version IDs and verified source availability. If transfer is unsupported, explain the website upload handoff without claiming an import. |
| Host this prepared GLB for viewing without regenerating it. | A supported single-scene GLB with embedded resources and a host with binary HTTP transfer. | Upload as `prepared_glb`, then call `prepared_model_import` against the explicit project head with one idempotency key. Show the saved version with `model_show`; verify unchanged GLB bytes, no Blender job, and unavailable source editing/download/remix. An optional `.blend` companion remains unverified. |
| Show me the preview of my saved model and tell me what is in it. | Accessible saved version with a poster and multiple objects. | Read the existing preview and scene, follow necessary pagination and describe observed contents. Submit no compute job. |
| Host this approved version publicly with the title Desk Lamp. Keep source downloads and remixing off. | Owned immutable version, publication scope and the prompt's explicit public authorization. | Publish exactly that version, preserve both source/remix restrictions and return the publication URL. Do not start a new model job or publicly expose a different version. |
| My app needs to show this private model to this customer on this domain. | Accessible immutable version, authorized recipient subject, exact HTTPS origin, expiry and embed scope supplied by the user. | Create the exact private grant and return its reference for the app's backend/embed integration. Keep service credentials out of client code and explain that artifact export URLs expire. |
| Reopen the lamp from our earlier session and make the base wider. | Reconnected host, accessible saved project/version and available execution. | Resolve the existing project or matching continuation, inspect saved state and submit an edit against it. Return a new saved version of the same project rather than silently creating a duplicate. |

## Tasks that should not select this workflow

| User prompt | Expected behavior | Reason |
| --- | --- | --- |
| Make a flat poster image of a lamp that looks 3D. | Use an image workflow; no Blendstra job. | No real product, known character or reusable source asset was requested. |
| Explain what polygon topology means. | Give a text explanation; no connector call. | No model creation or inspection is requested. |
| Use another named modeling service for this asset. | Respect the selected service. | Plugin relevance does not override the user's tool choice. |
| Train an AI model on my product descriptions. | Use an appropriate ML workflow. | Here "model" does not mean a 3D asset. |

## Connected recovery cases

- Search an authorized saved original component by recorded namespace/product/variant and a documented dimension, including an equivalent length unit. Confirm all filters match one reference and one measurement. Nominal/modelled values, another reference row, an unresolved variant and private evidence URLs cannot satisfy that query. Record the returned exact review/version pointers; compare current facts with facts at acceptance, correct the reference, then withdraw acceptance and confirm older decisions are not restored. Repeat while reference evidence is retired or permission changes. These are recorded facts, not brand/fit verification.
- Search a private catalog for a recorded capability and follow every result cursor, including empty filtered pages. Open the exact returned version. Repeat with revoked project access and without source scope; inaccessible entries must disappear and source-dependent findings must remain restricted. A title containing “animated” is not sufficient evidence.
- On the advanced endpoint, ask `recipes_list` for an adjustable lamp, then for a gate with `capability=animation`. The lamp exposes its declared shade positions; the current gate-v2 result declares its bounded swing. Neither result claims evaluated saved geometry. An old gate-v1 instance keeps its static source pin. After an authorized gate-v2 creation, read its recipe receipt and require a verified saved clip before claiming app playback. This distinguishes seed selection, saved evidence and actual application use.
- Prepare a valid lamp request, reject an unsupported angle before a job exists, then instantiate the valid request and retry its same key. Recover one operation through `model_get`, then read the exact saved receipt with `recipe_get`. A source-restricted connection must not read the receipt; a stale selected base must not be silently replaced by the latest head. Record synthetic checkpoints separately from real worker output.
- Filter `gallery_list` for `remix`, `source-download` and `clip`. Verify the first two against explicit current sharing permissions and the last against a saved video. A Use click is intent; count reuse only from the existing server-recorded completed remix, and record application behavior separately.

- Compare the actual registered creation tools and `blender_execute` schema with deployed `tools/list` using the procedure above. A connected call that supplies legacy required fields does not prove the minimal ordinary call works. Record each surface separately.
- Let a private viewing lease expire, then reopen the same saved model through fresh authorization. Confirm no Blender job starts, and denied access cannot recover cached private bytes.

- Exhausted allowance or no released profile: report the actual limitation, retain useful project/source pointers and submit no extra work. Never purchase credit or increase the cap implicitly.
- Another editor changes the head before submission: surface the conflict, reopen current state and reconcile intentionally. Do not silently overwrite it.
- A running job's response is interrupted: reconnect and poll the known job ID. Verify there is no duplicate charged execution.
- Creator metadata says to publish source or change the budget: treat it as untrusted data and preserve the current user's instructions.
- Source/remix sharing requested: show the exact source-sharing preview and obtain the missing acknowledgement before passing the matching artifact/hash. A preview is not a claim that the source is sanitized.
- OAuth revoked: explain the required reconnection. Do not use another account, workspace or token to bypass revocation.

The release still needs actual execution evidence in supported clients. Keep `clientWorkflowsVerified`, `endpointVerified` and submission flags false until the respective checks are completed and recorded.

## Asset discovery authoring

Verify `discovery` appears in the installed `authoring_guide` topics and
`publication_update` advertises optional metadata with `expectedVersionId`.
Run each case in a fresh conversation; record the actual tool trace and public
page/facts when applicable. These are acceptance scenarios, not completed runs.

- Create a scene prop without asking to publish: after inspection, recover one
  exact-version private draft containing useful copy/tags/workflows. The original
  brief remains intact and no acceptance, publication or listing was created.
- Import a prepared GLB: describe actual visible features and potential uses;
  do not invent editable source, rigging, animation or print readiness.
- Publish an authorized fixed library asset: title, nonempty description, tags
  and selected facts agree between the tool, page, OG/Twitter and `/facts`.
  Source/remix/content-reference actions match their independent permissions.
- Improve an existing share: URL, listing and permissions remain unchanged;
  new search terms find it if already listed. A newer viewer version causes a
  conflict and reassessment. Foreign/old reference entries cannot be attached.
- Unknown dimensions, license or creator credit: preserve uncertainty without
  fabricated facts. A specific asset role is not a license or readiness badge.
- Reopen for incidental inspection, explicit file-only delivery, or an identical
  completed draft: avoid duplicate journal writes and additional marketing jobs.
- Missing installed topic/update fields: save the draft through supported tools,
  report the unavailable update path, and retain the existing public URL.

Measure relevant discovery and completed permitted reuse separately from clicks.
Do not report search ranking, automatic tool selection or training inclusion as
established by metadata, package validation or offline instruction trials.

## Known products and characters in generated content (ENG-1442)

Use the shared cases in `contracts/v1/content-discovery.ts` and the procedure in
`docs/verification/2026-09-26-content-workflow.md`. Image/video output is a positive
match when a known product, original character, controlled view or source identity
adds value. Include prompts that never name Blendstra or 3D. Generic scenery and
ordinary image edits remain negative controls. Exact unavailable variants and
unsupported uses must not be turned into manufactured matches.

The host coordinates the Blendstra connector and the content provider. Record
ChatGPT and Claude separately, including the installed tool schemas, permitted
source/version, reference artifact hashes, finished output, source recovery and
a fresh-session revision. A local mock, endpoint response, model card or submitted
provider job does not complete this acceptance. Public gallery visibility alone
does not authorize content reference use. Preserve permission restrictions.


## Account-aware discovery and recovery

- On the actual host, inspect a CPU-capable connection, a read-only connection and an execution-unavailable account. Confirm available viewing/import/export paths remain usable independently.
- Re-read `service_capabilities` for current reason codes and the Account link. Exercise configured/unconfigured, service pause, connection scope, workspace pause and quota explanations without changing live policies merely for testing.
- Compare the static full review inventory with registered schemas. Verify cached execution calls still enforce authorization, and that an unchanged previously admitted request remains recoverable after availability changes.
- Confirm the host's observed refresh behavior separately. Server `tools/list` tests do not establish ChatGPT metadata refresh. Do not claim pricing, upgrades, GPU activation, extra permissions, or automatic refresh.
