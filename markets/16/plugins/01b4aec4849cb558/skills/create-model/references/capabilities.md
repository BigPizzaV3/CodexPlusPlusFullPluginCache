# 3DJ MCP Capabilities — 18 November 2026

- **Live MCP Endpoint:** `https://www.3dj.app/api/mcp` (alias: `https://3dj-neuraldeepnet.on.adaptive.ai/api/mcp`)
- **Transport:** Stateless Streamable HTTP (`POST /api/mcp` JSON-RPC 2.0, `GET /api/mcp` JSON summary / SSE endpoint event).
- **Negotiated Protocol Versions:** `2026-07-28` (stateless, per-request metadata, `server/discover`), and by handshake `2025-11-25`, `2025-06-18`, `2025-03-26`, `2024-11-05`.
- **OAuth 2.1 Authorization Server Metadata:** `https://www.3dj.app/.well-known/oauth-authorization-server`
- **OAuth 2.1 Protected Resource Metadata:** `https://www.3dj.app/.well-known/oauth-protected-resource`
- **Website & Policies:** `https://www.3dj.app` · `/support` · `/privacy` · `/terms`

## Deployed 32-Tool Catalogue

| # | Tool | Auth / OAuth Scope | Purpose & Verified Behavior |
| --- | --- | --- | --- |
| 1 | `openscad_get_starters` | Public (`noauth`) | Retrieve 3 editable OpenSCAD starter examples (`mounting-plate`, `vented-cup`, `box-and-lid`) and supported language rules. Zero AI/CPU quota used. |
| 2 | `openscad_compile_model` | OAuth `models:write` (or API key) | Compile and measure `.scad` source in an isolated OpenSCAD/Manifold worker (`readOnlyHint: true`). Returns effective source, numeric parameters, triangle count, closed-manifold check, bounding box, and optional `buildVolumeMm` printer fit. Limit: 20/hr, 100/day per account. |
| 3 | `cad_get_starters` | Public (`noauth`) | Retrieve verified Replicad/OpenCascade B-Rep starter scripts, optional `category` filter (`mating`, `fastener`, `enclosure`, `gear`, `bracket`, `joint`), optional `index: true` summary-only mode, and the DSL reference. |
| 4 | `cad_validate_script` | Public (`noauth`) | Syntax check a Replicad CAD script, extract declared `Param.*` definitions, then build it in the isolated OpenCascade kernel: returns `buildValidation`, `measuredGeometry`, per-body `parts`, and optional `preview: true` isometric PNG. |
| 24 | `cad_render_views` | Public (`noauth`) | Build a Replicad CAD script with `parameters` and return server-rendered PNG views (`iso`, `front`, `top`, `right`) as MCP `image` content blocks, with section cuts and `thin-walls` / `overhangs` / `parts` highlights. |
| 25 | `cad_import_model` | OAuth `models:write` (or API key) | Import a STEP, STL or GLB file (HTTPS URL or base64 <= 20 MB) as private reference geometry (`importedModel("<modelId>")`), or delete on request (`deleteModelId`). |
| 26 | `cad_compare_revisions` | Public (`noauth`) | Build and compare two CAD script or saved `modelId` revisions and return changed parameters, size/volume/mass deltas, added/removed/changed parts, check state changes, and an isometric diff overlay PNG as MCP `image` content. |
| 27 | `cad_export_drawing` | OAuth `models:write` (or API key) | Build a Replicad CAD script and export a one-page A4 landscape manufacturing drawing (`pdf`, `svg`, or `dxf`) with `front`/`top`/`right` orthographic views, `iso` view, title block, overall dimensions and `dim: true` parameters. |
| 28 | `cad_check_assembly` | Public (`noauth`) | Check a multi-part assembly for pairwise B-Rep interference volumes, minimum surface clearance, and sweep each `placeAt` joint over its declared `Param.number` range, reporting the first colliding parameter value. |
| 29 | `cad_save_feature` | OAuth `models:write` (or API key) | Validate and save a reusable parametric feature function (`defineFeature(name, params, fn)` / `lib.mine.<name>`) to your private account library (cross-account team sharing is gated on workspace membership). |
| 30 | `cad_list_features` | OAuth `models:read` (or API key) | List saved parametric features (`lib.mine.<name>`) in your account library with default parameters and call syntax. |
| 31 | `cad_add_review_comment` | OAuth `models:write` (or API key) | Pin a design review comment to an owned saved CAD model, revision number, part name or 3D point `[x, y, z]` in mm. |
| 32 | `cad_list_review_comments` | OAuth `models:read` (or API key) | List design review comments pinned to an owned saved CAD model or revision. |
| 5 | `cad_get_evidence_schema` | Public (`noauth`) | Return the 3DJ Design Evidence Pack v1 specification and DfAM gates (watertight shell, 0.8mm minimum wall, 45° overhang, 220×220×250mm bed). |
| 6 | `cad_list_models` | OAuth `models:read` (or API key) | List the authenticated user's saved parametric CAD and photo-reconstructed models (`script-cad`, `photo-cad`, `primitive`) with script source and parameter values. |
| 7 | `list_providers` | OAuth `account:read` (or API key) | Report live health of every 3D generation backend, supported inputs (`text`/`image`), and the caller's remaining hourly/daily generation allowance. |
| 8 | `generate_from_text` | OAuth `models:write` (or API key) | Start an asynchronous text-to-3D concept mesh generation. Returns `modelId` and `status: "processing"`. Poll with `get_generation_status`. |
| 9 | `generate_from_image_url` | OAuth `models:write` (or API key) | Start an asynchronous image-to-3D generation from a public HTTPS image URL (max 12 MB, protected by SSRF guard). Returns `modelId` for polling. |
| 10 | `get_generation_status` | OAuth `models:read` (or API key) | Poll an owned generation job (`processing`, `complete`, or `failed`), returning progress, serving provider, `downloadUrl` when complete, or upstream failure reason. |
| 11 | `list_my_models` | OAuth `models:read` (or API key) | List models belonging to the authenticated account, newest first, with optional status filter (`complete`, `failed`, `processing`). |
| 12 | `get_model_download_url` | OAuth `models:read` (or API key) | Return the absolute HTTPS `downloadUrl`, actual format (`glb` or `stl`), and `refinementHandoff` for a completed model owned by the caller. |
| 13 | `get_account_status` | OAuth `account:read` (or API key) | Verify the connected 3DJ account ID, authentication method (`oauth` or `api_key`), granted scopes, saved-model counts, and whether print quote requests are open. |
| 14 | `request_print_quote` | OAuth `quotes:write` (or API key) | Submit an account-owned print quote review request for a completed saved model (`requestKey`, `modelId`, `dimensionsMm`, `material`, `colour`, `quantity`, `destinationCountry`, `destinationRegion`, `intendedUse`). Creates a review request only; `paymentRequiredNow: false`. |
| 15 | `list_print_requests` | OAuth `quotes:read` (or API key) | List the authenticated user's print quote requests and operator review notes/statuses. |
| 16 | `cancel_print_request` | OAuth `quotes:write` (or API key) | Cancel an active print quote request owned by the caller. Does not cancel a paid order or issue a refund. |
| 17 | `list_print_quotes` | OAuth `quotes:read` (or API key) | List operator-issued EUR print quotes for the authenticated user, including item/shipping/tax/total EUR cents, lead time, expiry, `quoteHash`, and operator inspection attestation. |
| 18 | `accept_print_quote` | OAuth `quotes:write` (or API key) | Record the customer's explicit acceptance of exact quote terms (`quoteId` + `quoteHash`). Records acceptance only; no payment, print booking, or shipment is executed. |
| 19 | `cad_export_model` | OAuth `models:write` (or API key) | Build a Replicad script with chosen `parameters` in the isolated kernel and write a downloadable file: `stl`, `stl-fins` (breakaway Support Fins baked in), `stl-fins-only`, `step` (ISO 10303), `glb` (Blender/viewers) or `zip` (per-part STLs + BOM.md). Returns absolute `downloadUrl`, `sha256`, `measuredGeometry`, `parts`. Limit 30/hour, 150/day. |
| 20 | `cad_save_model` | OAuth `models:write` (or API key) | Build a Replicad script server-side and save it as an editable `script-cad` gallery model with its STL on the CDN. Returns `modelId`, `modelUrl`, `openUrl` (`https://www.3dj.app/workspace?model=<id>`), `configuratorUrl` (`https://www.3dj.app/configurator/<id>`), `measuredGeometry`, `parts`. |
| 21 | `compose_design_brief` | Public (`noauth`) | Build and measure a script, then compose a product render brief (`sketchmonkey.arguments` included) and Blender / FreeCAD / Fusion 360 / Onshape / slicer handoff steps (`handoffs`). Returns an inline viewport preview; makes no product render, calls no other service and stores nothing. |
| 22 | `cad_get_configurator` | Public (`noauth`) | Build and inspect a script (`code`) or saved gallery model (`modelId`) and return its `Param.*` schema, per-part colours/materials/connectors, `placeAt` joints, BOM, pinned CDN imports (`@neuraldeep/3dj-runtime` & `<threedj-configurator>`), and `ui://3dj/configurator` resource link. |
| 23 | `cad_publish_configurator` | OAuth `models:write` (or API key) | Build and save a Claude-built or workbench configurator to the authenticated account's gallery, returning `shareUrl` (`https://www.3dj.app/configurator/<id>`) and `openUrl` (`https://www.3dj.app/workspace?model=<id>`). |

## Authentication & Security Guarantees

1. **OAuth 2.1 + PKCE (`3djoa_...`):**
   - Dynamic Client Registration (`POST /api/oauth/register`), Client ID Metadata Documents (`client_id_metadata_document_supported: true`), authorization endpoint (`GET /api/oauth/authorize`), first-party consent UI (`/api/oauth/consent` downstream of Adaptive login), token endpoint (`POST /api/oauth/token` with S256 PKCE and refresh token rotation/replay revocation), and connection management (`/oauth/connections`).
   - Unauthenticated calls to protected tools return `HTTP 401` with `WWW-Authenticate` carrying the full scope set (`account:read models:read models:write quotes:read quotes:write`). Insufficient scope returns `HTTP 403` with `error="insufficient_scope"` and `scope="<needed>"`.
2. **Legacy API Keys (`3dj_live_...`):**
   - Per-user API keys minted at `https://www.3dj.app/agents` continue to work via `Authorization: Bearer 3dj_live_...`.
3. **Strict Account Isolation & No Credentials in Arguments:**
   - Account identity is derived exclusively from validated Bearer tokens. Supplying `userId`, `token`, `authToken`, `apiKey`, or `claimCode` in tool arguments is rejected with `credentials_in_arguments`.

## Public links for exports and publishing

`cad_export_model` and `cad_export_drawing` write a new file at a publicly reachable 3DJ download URL. `cad_publish_configurator` publishes a new public configurator and returns separate share and workbench links. Each of these three tools advertises `openWorldHint: true`, and repeated successful calls create separate outputs. Use only the user's requested geometry and never submit confidential material for public sharing.
