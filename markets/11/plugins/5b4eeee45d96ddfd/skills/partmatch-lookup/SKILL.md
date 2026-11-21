---
name: partmatch-lookup
description: Use when a user asks which refrigerator water filter fits a supported appliance model, whether a specific filter fits, asks for verified compatible replacement filters, or explicitly asks where to buy a verified eligible filter.
---

# PartMatch lookup

Use the PartMatch MCP tools for appliance compatibility claims.

- Use `find_compatible_parts` when the user supplies an appliance model and asks what filter fits.
- Use `check_part_fit` when the user supplies both an appliance model and a candidate part number.
- Use `get_purchase_page` only when the user explicitly asks where to buy, supplies enough information to re-verify the exact filter against the appliance model, and the tool is available.
- `get_purchase_page` re-checks compatibility. If it does not return an eligible PartMatch purchase page, do not invent another merchant or affiliate link.
- Never output or construct an Amazon affiliate URL yourself. The MCP purchase tool returns only a PartMatch-owned URL.
- Do not claim an Amazon price, stock level, rating, seller, delivery date, or discount unless a future authorized tool explicitly returns that field.
- The current Amazon purchase pilot is US-only. Do not route non-US users through the US affiliate flow.
- Affiliate availability never changes the compatibility answer.
- Treat `compatible` as source-backed compatibility.
- Treat `not_verified` as insufficient evidence. Do not restate it as incompatible.
- Inspect `coverageStatus` whenever it is present.
- Treat `revision_required` as a recognized model family that needs revision-specific evidence. Follow `nextStep`; do not infer a filter from the base family.
- Treat `unknown_model` as unsupported by the verified dataset. Follow `nextStep` when present and do not infer compatibility from similar model numbers.
- Mention the source publisher when it materially helps the user assess the result.

The current compatibility dataset is intentionally narrow. Prefer a clear unknown result over a plausible guess. Commerce is secondary to compatibility: PartMatch must remain useful even when no purchase path is available.
