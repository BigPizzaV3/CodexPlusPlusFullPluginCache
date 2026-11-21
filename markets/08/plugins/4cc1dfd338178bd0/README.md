# Formatry API agent plugin

Use the hosted Formatry MCP server for normal Codex or Cursor work:

```text
https://formatry.cc/api/mcp
```

The distributed plugin connects only to the hosted MCP URL. Codex discovers Formatry's OAuth metadata from that endpoint. Cursor uses Formatry's predefined public marketplace client and the exact scopes required by the published tools. Neither install needs a local server, package download, API key, or client secret.

## Connect

Install the public Codex plugin without downloading a bundle:

```bash
codex plugin marketplace add iddictive/formatry-plugin
codex plugin add formatry-api@formatry
```

Cursor can install the same hosted server through its native link:

[Install Formatry MCP in Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=formatry-api&config=eyJmb3JtYXRyeS1hcGkiOnsidXJsIjoiaHR0cHM6Ly9mb3JtYXRyeS5jYy9hcGkvbWNwIiwiYXV0aCI6eyJDTElFTlRfSUQiOiJodHRwczovL2Zvcm1hdHJ5LmNjL29hdXRoL2NsaWVudHMvY3Vyc29yLW1hcmtldHBsYWNlIiwic2NvcGVzIjpbImJhbGFuY2U6cmVhZCIsImFzc2V0czpyZWFkIiwiYXNzZXRzOndyaXRlIiwiam9iczp3cml0ZSIsImpvYnM6cmVhZCIsImFydGlmYWN0czpyZWFkIiwicHJldmlld3M6cmVhZCIsInByZXZpZXdzOndyaXRlIiwicHJvamVjdHM6cmVhZCIsInByb2plY3RzOndyaXRlIiwiY3JlYXRpdmVzOnJlYWQiLCJjcmVhdGl2ZXM6d3JpdGUiLCJwcmVzZXRzOnJlYWQiLCJicmFuZDpyZWFkIl19fX0=)

Complete the OAuth browser flow opened by the client. If Codex does not open it automatically, run:

```bash
codex mcp login formatry-api
```

The same connection window offers account creation and login, then returns to the requesting client. Confirm your identity and the requested access there; do not paste passwords, email codes or API keys into chat. The website, API and plugin share the account's daily free-image allowance and existing credit balance.

The Codex connection is configured for hosted Streamable HTTP with OAuth as the client's default credential source:

```json
{
  "mcpServers": {
    "formatry-api": {
      "type": "http",
      "url": "https://formatry.cc/api/mcp"
    }
  }
}
```

Cursor's bundled config uses the public client id `https://formatry.cc/oauth/clients/cursor-marketplace` with no client secret. Formatry resolves this identifier server-side and accepts only Cursor's registered browser and local callbacks.

In Codex, start with: `Check my Formatry connection and tell me the next safe step.`

### Optional manual API-key connection

Formatry still accepts scoped API-key bearer tokens for direct integrations and existing automation. This is a manual compatibility path, not a marketplace-install requirement:

```bash
export FORMATRY_CC_API_KEY='your-scoped-formatry-key'
codex mcp add formatry-api-key --url https://formatry.cc/api/mcp --bearer-token-env-var FORMATRY_CC_API_KEY
```

Create or rotate a scoped key in [Formatry developer settings](https://formatry.cc/studio/settings/developer) and keep it out of chat and source files.

## Prepare a creative

1. Use `formatry_connection_status` when account or authentication context is unknown. The normal hosted path uses the OAuth identity stored by the client; a manually configured scoped API key remains supported.
2. A standalone preview can run directly with a supported size and stable idempotency key. The server enforces its limits. Inspect quota only for a quota question, batch planning or rate-limit recovery; inspect balance before a paid export.
3. When the requested design needs source assets, reuse ready assets with `formatry_list_assets`, or inspect a user-authorized local source using the bundled Node helper, call `formatry_prepare_asset_upload`, transfer bytes with the helper and call `formatry_complete_asset_upload`. No manual Studio upload is required. Remote MCP receives metadata, not local paths.
4. For a campaign or saved creative, continue to the saved creative workflow below. After editing, use `formatry_create_studio_creative_preview` to inspect that exact revision. Use `formatry_create_preview` only for a requested standalone preview without a saved creative, with a stable `idempotencyKey`. In ChatGPT or another compatible OpenAI host, `formatry_upload_asset_file` can accept a host-authorized file object with `download_url` and `file_id`; it does not read a local path.
5. For new work, call `formatry_start_creative` with a campaign `projectName`, optional `creativeName`, and a stable `idempotencyKey`. This creates a project and its first raster creative without Studio, rendering, or billing. Retain the returned ids and revision; after editing, resume with those ids rather than repeating creation. The tool requires `projects:write` and `creatives:write`; existing OAuth grants may need native reauthorization for the new scope. For a saved Studio creative, read its exact revision, then use the individually exposed editing tool, such as `formatry_set_studio_copy` for text or `formatry_apply_studio_preset` for a preset. Each accepts the canonical command envelope with only its declared operation kind. Apply different kinds sequentially using the returned current revision and read back the result. A request to propose or wait still requires the requested separate confirmation. Use `formatry_create_studio_creative_preview` to inspect the exact revision.
6. Read the saved creative revision, call `formatry_create_studio_export_quote` with `current` or `selected` output scope, and show the output set, `billingMode`, `freeUnits` and `freeRemaining`. After the user confirms a free raster quote, call `formatry_confirm_studio_export_quote` with the server-issued quote id and a stable idempotency key. Follow `job.id` through `formatry_wait_for_generation_job`, require a ready `formatry_get_artifact_manifest`, then use `formatry_prepare_artifact_download` and the bundled helper to save and verify files in Codex; compatible resource-aware hosts can use `formatry_download_artifact_file`. For non-free quotes, show the fresh quote's ordinary account credit cost and funding source, then use formatry_confirm_credit_export only after approval of that exact approvedUnits value. Approved non-free exports use the same ordinary account credit and subscription balance as Studio; they never purchase new credits. If the balance is insufficient, explain the limit without initiating checkout or promoting an upgrade. No raw generation, pricing, provider or render fields are accepted.

Example Codex prompt:

```text
Show me one Formatry preview. Then open my saved Studio creative, propose one text edit and wait for my confirmation. After approval, show the updated preview and quote downloadable raster files. Show my remaining free allowance and ask before consuming it. Confirm only a free quote and return ready files. Do not start checkout or promote an upgrade.
```

`401` means complete or repeat client OAuth sign-in, or replace the key for an explicitly manual key connection. `402` means explain the unavailable current allowance or reduce the requested output set without directing a purchase. `403` means the identity needs the returned scope. `409` means reuse the original request or wait as directed. `422` identifies an unsupported input. `429` provides a retry/reset time.

The public plugin starts no local subprocess. Codex and Cursor connect directly to the hosted Streamable HTTP endpoint above.


## Embedded Studio

With the matching 0.4.2 server, call `formatry_open_studio` with a saved creative's `projectId` and `creativeId` to open its interactive surface in a host that supports MCP Apps. The agent and interface use the same saved creative and revision. Read back the current revision after manual changes before another command. If the host does not render MCP Apps, continue through the tools and present real previews and saved files; do not claim that an editor was displayed.

## Local files without Studio

The bundled skill includes `scripts/formatry-files.mjs` for Node 22+ and ordinary host shell/filesystem permissions. It is not a local MCP process and does not read Codex credentials. The agent inspects an authorized source, prepares an upload through MCP, passes its encrypted two-minute capability to the helper on stdin, and completes the existing upload intent. Codex downloads use `formatry_prepare_artifact_download` and the helper to save checksum-verified files in the selected workspace, then open the actual result; compatible resource-aware hosts can use `formatry_download_artifact_file`. Tickets must never be printed, persisted or placed in command-line arguments. The helper refuses redirects, workspace escapes, changed sources and overwriting existing output files. Transfer size is at most 25 MiB per file. Native OAuth still handles sign-in/signup/consent; normal work does not require the Studio UI. Resource-aware hosts may retain the existing embedded-file path. Hosts without permitted shell/filesystem input need that compatible resource path or an explicit limitation; remote MCP alone cannot write their disks.

Existing MP4, MOV, M4V, WebM and Ogg videos can be ingested into the `media` asset slot through the same native file workflow. Local inspection requires already-installed `ffprobe` and `ffmpeg` on PATH, probes an immutable copy and decodes its first frame; upload preserves the original bytes. Sources are bounded to 25 MiB, 60 seconds, 8192 pixels per edge and 40 million pixels. This stores an existing video only; it cannot bind that video into an Images or Animation scene. See the bundled skill for process/output limits and failure recovery.

## Animated banners

Images supports PNG, JPG and WebP; Animation supports animated WebP, GIF and MP4. Start or read a saved creative, select Animation with `formatry_set_studio_workspace_mode`, then configure its delivery with `formatry_set_studio_delivery_spec`, retaining each returned revision. Preview that revision with `formatry_create_studio_animation_preview`. Quote the requested files, show the ordinary account credit cost and confirm the exact authorized units through `formatry_confirm_credit_export`. This uses the same balance as Studio; no subscription or separate Animation quota is required. Animation cannot use the free-image allowance. Wait for success and a ready manifest, then save the actual files. Video workspace and HTML5 export remain unavailable.

Use `formatry_add_creative` for additional named blank concepts in the same campaign. Stable creation keys retain later edits on replay; renamed/archived targets conflict safely. The older `formatry_confirm_included_export` remains subscription-only for compatibility: an old quote/approval cannot become ordinary-credit consent. Use a fresh account-balance quote and exact cost approval for the credit tool. New purchases and checkout are outside this plugin. Protocol/helper tests do not prove a live client run.
