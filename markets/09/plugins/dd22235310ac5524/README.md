# Blendstra plugin

Create, explore and share interactive 3D in chat.

This **unsubmitted draft** gives agents persistent Blender creation/editing, an interactive model card, recoverable versions and reusable model references. The agent in the user's chosen client does the reasoning and modeling. Blendstra supplies execution, inspection, storage and delivery.

## Lead with useful results

| User goal | Result |
| --- | --- |
| Make something I can explore | Create once, inspect the saved result, then deliver an interactive card and durable link. |
| Bring my own model | Upload a supported GLB and view it without running Blender. This path does not supply editable source. |
| Point and refine | Select a real part in the card, request a change in the same chat and receive a new saved version. |
| Return to saved work | Find a project by title, open its context and continue without regeneration. |
| Share something people can use | An explicitly shared interactive page; a permitted private remix retains attribution. |
| Use a known product or character in content | Permissioned reference images/clips and finished content linked to its actual model sources. |

After inspecting completed work, agents author and privately save a version-specific discovery draft: a useful description, focused tags, potential asset roles, supported workflows and known facts. Authorized publishing uses this draft; metadata updates keep the existing URL and sharing settings. Public facts point receiving agents to `/connect`, the MCP endpoint and exact-version permitted actions. This supports relevant reuse; it does not promise search ranking, agent selection or training inclusion.

Keep projects private by default. Offer sharing only when useful to the task; do not add promotional footers or publish automatically. Public viewing does not grant access to the owner's private project. Do not copy a public model merely to show it.

## Focused tool discovery

The standard endpoint, `PUBLIC_ORIGIN/mcp`, has a static review inventory of **38 agent tools** plus two app-only widget helpers. Authenticated discovery lists the subset currently available to the connection. It covers complete creation, imports, inspection, revision, saved-work recovery, public sharing/remixing, private-model search and content-reference/result workflows.

The full endpoint, `PUBLIC_ORIGIN/mcp/advanced`, additionally advertises private app grants, catalog management, saved handoffs, original test recipes and legacy execution/accounting. Both endpoints use the same account/workspace and scope checks, and each also answers with a trailing slash. `/mcp`, `/mcp/` and `/mcp/advanced/` each publish protected-resource metadata naming exactly their own URL. `/mcp/advanced` keeps naming the canonical resource `PUBLIC_ORIGIN/mcp`, as it always has, so in Claude, which needs metadata naming the exact URL entered, use `/mcp/advanced/` for the full catalog. A token issued for any form is accepted at all four. All existing calls remain compatible on either endpoint; hiding a tool from discovery does not grant or remove authorization. Existing clients are not forced to reconnect to finish an old operation.

Each discovery request refreshes the verified connection scopes and account availability. CPU/GPU execution, prepared import, viewing and export are independent; missing execution access does not hide available saved-work paths. The server does not promise that an installed host automatically refreshes a cached catalog. `service_capabilities` provides precise reasons and a neutral Account link. GPU information does not activate access, and no pricing or upgrade flow is required.

All operations remain independently registered with their stable schemas, annotations and call-time permission checks. Review the complete static inventory without an account filter using `node --import tsx services/api/scripts/export-eval-tools.mjs --review-all` from the repository root (with the API dependencies installed). This read-only export does not run any operation.

Choose the standard endpoint for normal adoption. Use advanced discovery only for those specialized tasks. The four original recipe templates are private test fixtures, not a general public model library.

### Fewer unnecessary steps

- `model_create`/`model_edit` save automatically; poll `model_get` for that operation's result. No manual project/upload/quote sequence for an ordinary inline script.
- `project_open.modelContext` is the normal saved-model entry point. Read extra context or review evidence only when missing.
- `model_edit` handles eligible transforms and existing material assignments. Use scoped Python for shape work; preserve the exact base and unrelated parts.
- `version_set_current` deliberately restores a saved version. Legacy `version_save` remains compatible; neither creates new artifact bytes.
- `projects_list.q` filters title words without exposing another account's projects. Follow pagination even when a filtered page is empty.
- One `material_get` helper supports all starter surfaces. Include it once per script; request `includeHelper:false` when only metadata is needed.
- Read a saved continuation only for an explicitly resumed task. Do not insert billing or acceptance bookkeeping into routine modeling.

## Model cards

`model_show` opens the exact saved project/version using the shared viewer and current OAuth access. Users can orbit, pan, zoom and bring an actual selected part into the same chat. Clients without UI receive an exact-version link. Return the operation's saved result after an edit; never guess the current head.

The component is built with the API image and runs at `https://widgets.blendstra.com`. Its two `model_widget_*` tools stay app-only and expose neither account credentials nor public sharing grants. A successful tool response is distinct from observed visible rendering.

## Prepare a connection package

Package **1.8.0**, server catalog **1.12.0**, authoring guide **2026-10-04.2**. Authoring topics include `reference_modeling` and `discovery`. Package/source updates do not prove an installed client refreshed its metadata.

From the repository, with the output parent directory already present:

```sh
node scripts/prepare-connection-package.mjs --origin https://YOUR_PUBLIC_HOST --out work/blendstra
```

Use the authorized public origin. The command prepares a self-contained draft bundle with remote MCP configuration, skill and its references, logo, license, verification scenarios and draft registry metadata. It refuses an existing output and does not install, authenticate, submit, publish or start work.

For an existing registered ChatGPT connection, use its actual technical ID:

```sh
node scripts/prepare-connection-package.mjs --origin https://YOUR_PUBLIC_HOST --out work/blendstra --app-id REGISTERED_CONNECTION_ID
```

That variant references the registered connection through `.app.json` and omits a duplicate MCP definition. Verify the actual connection's origin and workspace; syntax validation is not registration verification. The checked-in `.mcp.json` targets a local development facade and is not a hosted endpoint.

Use the supported personal-plugin workflow in the intended host. Other client configurations are on the deployed `/connect` page. An installed skill makes the workflow available; it does not guarantee selection, expand permissions or make the plugin publicly available.

## Verify before release

Run [verification.md](verification.md) against the actual connection, including unbranded prompts, upload/display, selected-part edits, sharing, public viewing without copies and source-linked content. Check both standard and advanced discovery, legacy calls, exact guide version and `reference_modeling` support. Retain source/base/access restrictions. Verify desktop/mobile visible rendering and link fallback separately from server tests.

For reference-based modeling, inspect actual images, establish proportions, compare saved renders at matched cameras and refine. Real agent runs and visual reviews are required before claiming improved fidelity. See [reference-modeling verification](https://github.com/Fenceline/blendstra/blob/main/docs/verification/2026-09-28-reference-agent-modeling.md).

Public directory availability requires the applicable submission, review and publication process. This package does not claim directory approval, automatic client refresh or measured adoption. Preserve prior evidence in [client connections](https://github.com/Fenceline/blendstra/blob/main/docs/CLIENT-CONNECTIONS.md) and record fresh acceptance separately.

## Data the plugin sends

The plugin runs no code of its own. It holds instructions for your agent (the skill) and the address of the hosted Blendstra MCP server. Data moves only when your agent calls a Blendstra tool or you use the model card:

- **To Blendstra, over HTTPS with your connection's access token.** The prepared bundle points at `PUBLIC_ORIGIN/mcp` (for example `https://blendstra.com/mcp`). Blendstra receives what your agent puts in tool calls: model titles, Blender Python scripts, edit requests, files you choose to upload (`.blend` and GLB models, reference photos and other supporting assets), notes and discovery descriptions, and sharing choices. It does not receive your whole conversation.
- **Sign-in.** You approve the connection on Blendstra, which records the connection, the workspace you chose and the permissions you granted. Your chat client keeps the access token.
- **Model card.** The card runs in your chat client's sandbox. Through your chat client it requests short-lived, download-only links for the exact saved model and poster, and its content security policy lets it connect only to the Blendstra origin. When you select a part, the card gives your chat client that part's identity and saved context so your agent can use it.
- **Your chat client** receives what Blendstra tools return and handles it under its own policies.

Blendstra stores your projects, versions and uploads in your workspace and runs Blender scripts on its own workers, using Google Cloud and Firebase. Projects start private; nothing is published unless you share it. See the Blendstra privacy policy at `PUBLIC_ORIGIN/privacy`.

## License

The contents of this plugin folder are licensed under the [Apache License 2.0](LICENSE). The Blendstra name and logo are trademarks of Fenceline, Inc. and are not licensed under Apache-2.0.


The compact modeling path uses `authoring_guide` with `topic:modeling, detail:summary`. Omitted detail remains backward compatible; `detail:helper` on `geometry` or `reference_modeling` retrieves the existing selected CPU recipe. Read the [universal modeling guide and evaluation criteria](../../docs/modeling/guide.md). Local response/schema tests do not establish visual quality or speed gains.
