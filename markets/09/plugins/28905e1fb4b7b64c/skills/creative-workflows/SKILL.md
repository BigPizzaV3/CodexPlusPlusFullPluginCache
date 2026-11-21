---
name: creative-workflows
description: Create and revise images, videos, talking avatars, audio, 3D and batch variations in saved Nova workflows through connected MCP tools. Use for Nova projects, assets, reviewed GPU rental and installation, usage approval, progress and cancellation.
---

# Nova Creative workflows

Use the connected Nova Creative MCP server and its existing result UI. Preserve the service's hosting and OAuth authentication. If connection is required, use the host's OAuth connection flow; never ask for passwords or copy access tokens into chat or files.

## MCP execution boundary

For Nova project, graph, asset, generation and run operations, call this installed plugin's connected MCP tools directly. A request to create, open, revise or monitor a Nova workflow is not a request to build a local app or operate the Nova website.

- Stay with the current agent and the user's selected chat model. Do not spawn subagents, hand the task to another model, or change host model settings for routine Nova work unless the user explicitly requests delegation or a model change. Choosing a supported image/video provider from Nova's catalog is a separate workflow setting, not a reason to switch the chat model.
- Do not open browser tabs/windows, use browser or desktop automation, navigate to Studio, or click website controls to perform or verify Nova operations. Return project/download links for the user to open. Opening a project means reading its saved workflow through MCP, not launching its URL.
- The host's native Nova confirmation cards and the editor returned by `object_editor_open` are supported MCP UI, not a browser fallback. Let the user interact with them; never automate their confirmation buttons or call their UI-only tools from model reasoning.
- Discover the actual Nova tool namespace/schemas and check `nova_status` when connection/readiness is uncertain. If tools are absent, disconnected, unsupported or return an error, report the specific MCP blocker and one supported next step. Do not substitute a browser, shell/curl/CLI, another MCP connection/account, direct provider calls, or a different image-generation tool.
- These are defaults for Nova operations. An explicit user request to open a website or use a browser for a separate task can authorize that scoped action; routine workflow creation, editing, status checks or troubleshooting do not imply that request.

## Resume without changing execution path

On a follow-up or after context compaction, continue through the same connected Nova MCP tools. Carry forward the selected project ID, saved revision, returned run ID and pending confirmation state. Reread the workflow before mutations and recheck the run before retrying. Do not interpret a context reset, a long wait, a project URL or a tool error as permission to start a browser session or delegate the task. If identifiers or connection evidence are missing, recover them with MCP or ask one concise question; do not guess or repeat generation.

## Reuse supplied references

Use `asset_list` to find references already uploaded to Nova; they do not need to be reattached to chat. Reuse the selected owned asset ID/URL, and resolve ambiguous filenames before choosing a reference.

For a newly selected file, follow the actual host schema of `asset_import`. Some hosts accept an absolute local `file` path and upload it for the tool; raw remote MCP expects the host-provided attachment object. Do not interchange these schemas or invent file IDs/download URLs. `asset_upload` accepts selected file bytes as base64 up to the live inline limit (currently 16 MB); attachment import currently allows up to 64 MB. Use `nova_capabilities` for current limits and supported media. The remote server itself never reads client disk paths. Persist the returned owned asset ID/URL, not a temporary attachment download URL.

For many files, use an exposed batch-upload tool only if this connected server supports it, otherwise import the selected files individually or explain the supported file-picker step. Do not borrow a local STDIO/CLI connection or another account to bypass a missing capability.

## Connect once and verify the actual plugin

For a connection or authorization request, first call the Nova Creative plugin's exposed `nova_status` tool in the current chat. Use that exact plugin tool to verify the connection; a shell command, HTTP probe, CLI login, saved credential, or Portal authorization is not proof that this host plugin is connected.

- If `authenticated` and `ready` are true, reuse the connection immediately. Say briefly that Nova Creative is connected. Do not start OAuth again.
- If authenticated but not ready, report the returned readiness issue; do not treat it as a missing login.
- If the tool requires authentication, use this installed plugin's supported host connection control once. If no such control is available to the assistant, give one concise step: open the Nova Creative plugin card and choose Connect. Let the user complete the Nova account selection and consent there.
- After the user reports completion, call the same plugin `nova_status` again. Claim success only when its response confirms authentication and readiness. If it still requires authentication, report that the plugin connection is not yet confirmed and ask the user to check the card's connection status. Do not repeat OAuth or suggest restarting Codex as a proven fix.

Never run `codex mcp login`, add another `mcp_servers` entry, change credential-store settings, or use a manual token as a workaround for connecting this installed plugin. CLI and plugin connections can have different credential identities. Never read, copy, or transfer their tokens or Keychain credentials to bridge them. Do not log out, uninstall, revoke access, or restart the host unless the user separately requests that action.

Keep connection replies in the user's language, with the verified outcome and at most one necessary next step. Avoid speculative causes and debug narration; explain technical details when requested or when they are needed for an actionable error.

## Product overview and promo

When the user asks to see the Nova Creative product film, promo video, or brand materials, read `references/brand-media.md` and present the supplied video or requested asset through the host's supported file attachment or preview feature. This is an existing packaged resource and requires no generation or usage charge. Keep the user's active project intact while showing it.

## Discover capabilities

Discover actual tool schemas through this connected plugin before invoking tools. Read `nova_capabilities` before relying on media, upload, GPU or generation permissions. A server feature flag does not prove that a particular tool is exposed by the host. Use `generation_catalog` before choosing a provider/model, `workflow_node_reference` for unfamiliar nodes or ports, and `workflow_skill_reference` when diagnosing a quality problem or applying a known repair. Prefer targeted queries instead of retrieving the full references on every call.

Use live models, parameters, node types, constraints, prices and guidance. Support image, video, talking-avatar, audio and 3D work only where the current tools and references support it. Follow current formats, duration, dimensions, reference counts and batch limits. Do not hardcode catalog inventories or invent tool names, model IDs, prices or availability. If a reference or required tool is unavailable, explain the exact limitation without switching execution paths.

## Prepare and preserve the project

1. Gather the user's brief and supplied reference media. Clarify only missing information necessary to produce useful results. Resolve references using supported upload or asset tools; never fabricate asset URLs.
2. For an existing project, resolve its identity and read its current saved workflow before editing. Preserve its project/workflow ID, unaffected nodes and connections, reference assets, settings, and existing outputs. Apply the smallest supported incremental change. Do not replace the project, rebuild it from scratch, or create a duplicate unless the user requests that.
3. Create a saved workflow for a new project using supported tools. Open or rename workflows when requested. Verify saved mutations with the server's response; use concurrency/version controls where provided and reread on conflicts.
4. For creative directions and batches, represent the requested alternatives explicitly in the supported workflow structure. Keep variations in the same project where supported, retain existing branches, and use the agreed quantity. Explain unsupported requests and offer supported options without silently substituting them.
5. Before revision runs, reuse unaffected outputs where the server supports this. Do not assume an edit authorizes generation. A targeted run can still execute required upstream dependencies; use its preflight estimate.
6. Ordinary `output` nodes are optional display labels, not a requirement for execution or result retrieval. Do not add one unless the user requests it, and preserve existing Output nodes during unrelated edits. `templateOutput` has separate reusable-template requirements; do not remove or omit it on this basis. Use `workflow_run_results` for generated media and `workflow_get` with `include_results: true` for saved node outputs, including text. Leave `include_results` false for ordinary graph inspection when outputs are not needed.

## GPU and talking-avatar work

Read [GPU and media operations](references/gpu-and-media.md) before quoting or renting a GPU, installing a model/runtime, changing settings, terminating a server or preparing a talking avatar. Discover the actual exposed tools and account grants first. When the user requests rental and `gpu_server_start` is exposed, review `gpu_catalog`, `gpu_server_state` and `gpu_server_quotes` for the chosen disk. Obtain approval of the exact GPU, maximum hourly rate, disk, idle cutoff, prepaid first hour and ongoing charges before `confirm_spend=true`. Reuse existing explicit approval while those settings and costs remain unchanged. A missing rental tool is a host/review limitation; report it without claiming that rental is prohibited everywhere or silently switching accounts/connections.

Rental and model/runtime installation require `workflows.generate` and GPU account access. Start creates one server without installing weights or generating media. After an uncertain response, inspect state before another attempt. Installation requires separate approval of model/runtime size and ongoing GPU time, then polling until installed/error. Rented time remains billed during setup, downloads and idle time, separately from provider-call credits. Use the user's approved cleanup instruction for the exact rental: `gpu_server_terminate` permanently deletes its instance and disk and needs `workflows.write` and explicit deletion approval. Confirm provider teardown through `gpu_server_state` before claiming that charges have stopped. Cancelling a workflow alone does not authorize server deletion.

## Edit selected objects and layers

For replacing, changing or removing an object, text, clothing, logo or background in an existing image, use the live `object_editor_open` tool to show the interactive editor. Read the owned workflow first and use the exact owned source asset or existing editor node. Pass the requested edit as its instruction, then let the user select the object or layer in the image or layer tree. Preserve unrelated workflow nodes and successful outputs. A generator prompt change alone does not edit an existing image.

Opening the editor does not analyze, generate or charge. For an unanalyzed image, show the available Analyze layers action and its usage review; do not invent layer identities. The editor's UI-only asset, upload and run-output tools stay in the UI bridge. Analysis and generation require the user's own confirmation for the current operation. Never simulate that confirmation, bypass the card, or claim a preview exists before returned evidence confirms it.

## Review and confirm generation

Preflight the saved project revision and present the planned outputs, references, models, settings, variation count and server-provided estimated usage. Keep estimates and units accurate. Resolve an unknown cost before generation. Provider usage, configured-provider costs and GPU hourly time can be separate charges.

Read `nova_capabilities` and the actual tool list. When `generationRequiresCard` is false and `workflow_generate` is exposed, explicit user approval in chat of the exact current scope and estimate authorizes that tool. Supply the returned `preflight_id`, a stable `request_id`, `confirmed=true` and `approved_estimated_credits` equal to the reviewed estimate. Existing explicit approval for unchanged scope and cost is sufficient; do not ask for a second card click. Reuse the same request ID when inspecting/retrying an uncertain submission to avoid duplicate spending.

The native Nova card remains an optional supported confirmation route. `workflow_run` and its private confirmation capability stay UI-only: never fabricate a token, simulate a card click or call an app-only tool from model reasoning. On an older server that requires a card, use its documented card flow and accurately explain that limitation. Object-editor analysis and edits retain the editor's own confirmation flow.

Changes to settings, scope, count, references or cost require a fresh saved-version review and approval. A general creative brief or OAuth consent does not approve unspecified spending. Inspect a submitted run before retrying; a new paid attempt after a terminal failure requires its own approval.

## Track and return results

Use returned run IDs and the server's progress mechanism. Carry the run ID forward across follow-ups; neither a project ID nor the latest workflow timestamp is a run ID. If it is missing, recover it only from actual returned evidence or ask for the relevant run; do not invent a last-run lookup. Report queued, running, completed, failed and cancelled states accurately; never claim completion from a submission acknowledgement. Honour cancellation requests using the discovered cancellation tool and verify the terminal state. Do not promise that cancellation reverses charges.

Render the server's existing previews and result UI, include returned download links and the editable Nova project link, and distinguish successful outputs from partial or failed variations. Never invent output URLs. Preserve the saved project for feedback and continue future revisions in that same project.
