# Changelog

## 0.3.12 — candidate

- When MakeBox is not connected, no Etsy shop is linked, or the allowance is used up, give the seller one matching link (connector guide, Etsy shop link, plans page) and keep unaffected work going. New guide: `references/connection-and-limits.md`.

## 0.3.11 — candidate

- Explain how to fix a refused call: tag refusals now name each failing phrase; the model rewrites its own keywords.
- Photo alt text for listings on Etsy: `set_photo_alt_text` with `listing_id` + `listing_image_id` from `list_photos`.
- Variations: up to three properties; inventory writes stay possible on three-property listings.

## 0.3.10 — candidate

- Simplify the plugin manifest and listing quality guide.

## 0.3.9 — candidate

- Exclude development scripts and tests from the directory package.
- Use basic agent metadata and link workflow skills from the agent instructions.

## 0.3.8 — candidate

- Remove the bundled listing icon for a fresh Claude Directory scan.

## 0.3.7 — candidate

- Add a visual workspace skill that uses the existing connector only when the server and host support MCP Apps.
- Preserve all existing skills, connector settings, publisher metadata, and seller approval requirements.

## 0.3.4 — 2026-10-05

- Add complete Claude directory homepage, documentation, support, repository, terms and discovery metadata.
- Identify the existing proprietary plugin license without changing its terms.
- Preserve the existing privacy policy, workflows, MCP connection and reviewer test cases.

## 0.3.3 — 2026-10-04

- Shorten the Codex directory subtitle to meet the 30-character public submission limit.
- Preserve private reviewer credentials outside the package.

## 0.3.2 — 2026-10-04

- Expose current personalization counts/limits in the direct tool schema instead of obsolete single-question prose.
- Document preservation of existing Etsy questions during unrelated SEO pushes.

## 0.3.1 — 2026-10-04

- Align web/MCP/direct personalization at 1024 characters and five fields.
- Explain supported fixed optional-text fees, Money conversion, explicit fee removal and complete variation prices.
- Document scoped personalization writes and required price/field readback; update offline QA.

## 0.3.0 — 2026-10-04

- Expand the manager into an Etsy SEO/product-marketing role with explicit standalone and connected modes.
- Rewrite all seven skills with useful offline deliverables, task-specific references and precise execution boundaries.
- Add product fact ledger, long-description/copy rules, keyword evidence, physical shipping/package/returns, variations, multi-question personalization, media/digital and order playbooks.
- Add four fillable templates, release checklist and fictional physical/digital/ambiguous-input examples.
- Bundle a generated index and input schemas for 105 direct tools, with exact parity against the local MakeBox runtime and 21 locally validated API fixtures.
- Add optional offline structural QA and meaningful regression cases; it does not certify factual truth, ranking or Etsy publication.
- Provide connected and standalone package variants from one source. No credential, automatic background worker, paid generation or real-shop write is bundled.

## 0.2.0 — 2026-10-01

- Route direct Etsy requests and seller-approved content through the live `etsy_*` tools.
- Add the `use-etsy-api` skill and a shared direct API guide, covering the 105-operation server snapshot without bundling its implementation.
- Update the manager, creation, optimization, order, research and shop workflows for native Etsy IDs, full request schemas, multipart assets and explicit readback.
- Separate chat-authored content and direct transport from MakeBox AI generation and its allowance.
- Document optional personal-data OAuth consent, Etsy API limitations, and client tool discovery.
- Preserve the existing MakeBox workflow tools, connector URL and seller-approval boundaries.

## 0.1.1 — 2026-09-30

- Correct agent references for directory review.
