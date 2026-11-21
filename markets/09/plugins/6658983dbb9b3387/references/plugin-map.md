# Plugin Map

- Plugin: `makebox-etsy`
- Version: `0.3.3`
- Remote MCP: `makebox` → `https://mcp.makebox.ai/mcp`

## Agent and skills

The `makebox-etsy-manager` agent coordinates six operational skills in Cowork and Claude Code:

- `use-etsy-api`
- `create-etsy-listing`
- `optimize-etsy-listing`
- `manage-etsy-orders`
- `research-etsy-market`
- `manage-etsy-shop`

The seventh skill, `makebox-shop-manager`, provides the coordinating role in ordinary Claude chat, where plugin sub-agents do not run.

## Shared references

- `product-brief.md` → confirmed/observed/missing/conflicting facts and minimal intake.
- `listing-quality-playbook.md` → positioning, title, full description, tags, attributes, quality/measurement.
- `keyword-research.md` → offline CSV/live estimates, shortlist, provenance and niche comparison.
- `shipping-packaging.md` → actual parcel measurements, rates/destinations, processing/returns and profile scope.
- `variations-personalization.md` → full inventory sets, semantic readback and local/direct question differences.
- `media-digital.md` → gallery/alt text, owned uploads and actual download contents/access.
- `orders-workflow.md` → live versus exported orders, fulfillment notifications and financial-read boundaries.
- `worked-examples.md` → physical, digital, ambiguous facts, long description, profile update and uncertain writes.
- `etsy-operation-recipes.md`, `etsy-operation-index.md`, `etsy-tool-schemas.json` → verified shapes and 105-operation snapshot.
- `templates/` → product brief, copy/settings handoff, keyword evidence and packaging worksheet.
- `checklists/listing-release.md` → substantive release review.
- `scripts/` → optional offline QA, reference generation and bundle validation; no automatic execution.
- `examples/`, `tests/` → fictional copy packets and local schema/QA regression fixtures.

- `direct-etsy-api-guide.md`: live discovery, direct requests, identity, authorization, media and readback.
- `mcp-tool-guide.md`: when to use direct Etsy transport versus optional MakeBox workflows.
- `listing-creation-guide.md`: complete draft, inventory, personalization, policy/media and publication sequence.
- `agent-packs/etsy/makebox-etsy-manager/`: role context, domain notes, checklist and handoff format.

The remote server supplies current tools and implementation; the bundled schemas are a dated reference. This package does not embed the server, bundle credentials or create a background worker. Standalone builds omit the server declaration and retain the full domain role/knowledge. The coordinating skill carries the role in runtimes that do not load agent files.
