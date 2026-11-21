# Supporting Review Content

## Product overview

WOWSERU AI AFFILIATE STORYBOARD helps creators, affiliate marketers, and small brands turn product information into a structured short-form UGC production plan.

## Core user journey

1. Start with `Mulai` or the UGC Review entry intent.
2. Provide product name, USP, audience, narration preference, wardrobe, setting, language, product link, research mode, and optional reference images.
3. Review product/audience insights and emotional story direction.
4. Approve the story concept when requested.
5. Receive three six-panel 2×3 storyboard prompts and three connected video prompts.
6. Review continuity locks, negative prompt, story summary, and production checklist.

## Example review fixture: Donat Genduy

**User-provided facts in the supplied reference example:** Donat Genduy; donuts; target audience children; Bekasi setting; Indonesian with light Sundanese flavor; colorful toppings, soft texture, jumbo size, and budget-friendly price. A fictional Indonesian girl is used in the sample creative direction. The example does not establish exact ingredients, price, packaging, or nutritional claims.

**Expected story arc:**
- Scene 1 — Discovery: child returns home and notices a large colorful donut.
- Scene 2 — Product experience: child examines toppings and demonstrates soft texture.
- Scene 3 — Payoff: child tastes and shares the donut; the value points are reinforced without inventing additional product claims.

## MCP tools

- `validate_product_brief`: returns missing core fields and reference status.
- `validate_production_output`: checks three storyboards, six panels per storyboard, three video prompts, continuity locks, negative prompt, summary, and checklist.
- `build_production_manifest`: creates a compact JSON description of planned deliverables and total duration.

## Reviewer notes

- The root `mcp.json` connects to the deployed public Streamable HTTP MCP endpoint. The local stdio entrypoint is retained for development testing.
- Cloudflare Worker deployment and production MCP calls were verified on 2026-11-01. Endpoint: `https://ai-affiliate-storyboard.infowowseru.workers.dev/mcp`. Recorded version ID: `4b31e74d-0fb1-4101-8ac5-ed24c8fc0b60`.
- The welcome/header identity is supplied through plugin metadata and skill welcome instructions. A fully custom interactive landing page with two clickable buttons requires host UI/entrypoint support and is not asserted by this package.
- The plugin must not be confused with WOWSERU AI ANIMASI.

## Evidence status

Automated MCP core tests passed 8/8 with `npm test` inside `mcp-server/`. Production checks passed for `/health`, initialize, tools/list, and tools/call for all three tools on 2026-11-01. Host-level conversational tests in the final ChatGPT plugin host have not yet been completed; do not treat the MCP tests as proof of host-level approval.
