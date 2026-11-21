# SketchMonkey Design Studio — OpenAI & MCP Plugin Package (v1.0.5)

Repository package version `1.0.5`. Canonical Streamable HTTP endpoint:
`https://sketchmonkey-neuraldeepnet.on.adaptive.ai/api/mcp`.
The root `plugin.json` and `mcp.json` use Agent Plugins 1.0; `.codex-plugin/plugin.json` retains compatibility metadata.

## Available tools (18 advertised tools)

Live discovery via `tools/list` is authoritative:
- **Concept & Video Renders:** `render_concept`, `render_video`, `get_job`, `get_render_status`, `enhance_prompt`, `get_camera_presets`
- **Projects & Five Creative Lenses:** `create_project`, `generate_directions`, `select_direction`
- **Campaign Artboards & Brand Rules:** `create_campaign`, `inspect_artboard`, `edit_artboard`, `apply_brand_dna`, `generate_variants`, `get_artboard_export_metadata`
- **Non-Human Design References:** `list_subject_models`, `save_subject_model` (`object`, `car`, `space`, `character`, `creature`)
- **Account Status:** `get_account_status`

`get_artboard_export_metadata` returns saved artboard dimensions and available background image URLs (`composedFileAvailable: false`); it does not compose finished PNG or PDF files.

## Secure account access & privacy boundaries

Native MCP OAuth 2.1 + S256 PKCE (`account:read`, `creative:read`, `creative:write`, `renders:run`), Dynamic Client Registration (`/api/oauth/register`), first-party consent (`/api/oauth/authorize` and `/api/oauth/consent`), per-tool scopes, and connection revocation (`/oauth/connections`) are deployed and active at `https://sketchmonkey-neuraldeepnet.on.adaptive.ai`.

SketchMonkey is for product, vehicle, object, and spatial design. Submitting sensitive personal data (real-person facial/biometric templates, voiceprints, PHI/medical records, government IDs, payment card numbers, or credentials) is prohibited and rejected by server-side validation before storage or provider calls. Operational MCP logs (`McpLog`) store only tool name, status, duration, bounded error code, and a secret-keyed HMAC-SHA256 pseudonymous IP hash (`ip_...` or `null`), and are pruned after 24 hours.

## Directory commerce boundaries

Existing account entitlements apply. This connector does not advertise plans, sell credits, initiate subscriptions, or provide digital upgrade/checkout links. Website Stripe billing remains independent.
