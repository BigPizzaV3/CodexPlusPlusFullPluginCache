---
name: optimize-etsy-listing
description: Audit or improve an existing Etsy listing using product facts, buyer intent and available performance evidence; preserve specifications and operational settings. Return complete copy for manual use or execute approved connected edits.
---

# Optimize an Etsy listing

## Establish baseline and scope

Use pasted/exported content offline; state its timestamp/limits. Connected, prefer `etsy_get_listing` and relevant live media/inventory/personalization/profile reads. MakeBox row IDs differ from Etsy IDs. Ask whether the requested scope is text, media, specific settings or a full audit when it cannot be inferred.

Read [quality playbook](../../references/listing-quality-playbook.md) and [brief](../../references/product-brief.md). Inventory all confirmed details before editing. Preserve dimensions, contents, compatibility, customization, care, processing/returns and license. Surface contradictions rather than rewrite them as facts.

## Diagnose and propose

1. Identify the main purchase intent and current offer consistency. Look for unclear item/count, misleading photos, weak opening or missing ordering information.
2. Use [keyword evidence](../../references/keyword-research.md), with dates and missing values retained. If reports exist, separate listing/shop metrics and discovery versus conversion hypotheses. Without data do not claim a causal diagnosis or forecast.
3. Improve the chosen fields only: clear title, natural full description, distinct relevant tags and accurate attributes. Explain each meaningful change. Preserve useful existing terms unless there is a reason to replace them.
4. Audit relevant [options](../../references/variations-personalization.md), [delivery](../../references/shipping-packaging.md) and [media](../../references/media-digital.md) when the scope warrants it; do not silently change price, stock, state, shared policy or shipping.
5. Return before/after for edited fields plus the complete revised description and copy-ready set. For a long description, reorganize without losing factual sections. Use the [handoff](../../templates/listing-handoff.md).

A complete generated SEO set targets thirteen relevant valid tags. A seller-approved narrow/native update is not forced into the internal AI exact-13 rule. No invented quality score or guaranteed Etsy result.

## Apply only the intended changes

Standalone: manual fields, preview and save instructions; no claimed write. Connected: inspect `etsy_update_listing` schema, show exact changed fields, reuse authorization for them, send once and read back. Text transport does not need MakeBox generation.

If the seller specifically requests MakeBox internal `optimize_listing` or bulk AI, disclose/quote allowance first; generated output is a proposal. For bulk use `quote_bulk_seo` → approved `start_bulk_seo` → `get_bulk_seo_job` → review → approved push. Preserve per-listing review and partial statuses. Never automatically replay an uncertain Etsy write or paid generation.

Record baseline, changes, next evaluation window and verified/unverified status. Use [release check](../../checklists/listing-release.md).
