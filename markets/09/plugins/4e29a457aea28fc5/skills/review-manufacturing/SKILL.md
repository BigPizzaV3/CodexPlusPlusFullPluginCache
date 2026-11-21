---
name: review-manufacturing
description: Return the order link after a completed PCB design or revision passes DRC and DFM; obtain quotes and manufacturer handoffs when requested.
---
After design or revision work and any exports have completed, read the current project and revision. Run `check_pcb` and `get_manufacturing_readiness` for the same board and selected vendor, process and options. Poll accepted operations with `get_operation` until terminal and inspect their actual results. Repair remaining DRC and DFM findings and rerun the checks after changes. Only treat the design as ready when DRC and DFM pass without outstanding findings, readiness reports `canOrder: true` and `stale: false`, and the evidence matches the latest saved revision. Failed, missing, stale or not-run checks do not qualify; explain concrete blockers instead of claiming readiness.

When those checks are clean, automatically finish with a clickable `[Order PCB](...)` link in the conversation. Use the canonical `manufacturingUrl` returned for the project when available. Otherwise use the canonical `openInEmbedrUrl` from `get_project` or `show_project`, setting its `tab` query parameter to `manufacturing` while preserving the rest of the URL. Do not invent project IDs, slugs or provider URLs. Do not ask whether the user wants the link or direct them to a viewer Order button. Returning this project link needs no quote, manufacturer upload or purchase.

When the user requests a quote or manufacturer handoff, export matching files and request a live quote for the desired quantity and shipping inputs. State exactly what the quote includes: a bare PCB quote is not an assembled-device price. Show the quote currency, options, package/revision identity and any expiry reported by the vendor.

Use the advertised canonical specification fields: `quantity`, `widthMm`, `heightMm`, `thicknessMm`, `layers`, and `finishedCopper`. Select the real process profile and provider options. The quote tool derives omitted drill size from the saved board and returns its exact `spec`; reuse that specification, `quoteId`, and `buildDays` for the handoff. Do not guess dimension aliases or copy defaults from another design. Shipping can remain unquoted for PCBWay file review, and contact/shipping details can be completed on the provider's site.

Ask the user to explicitly approve uploading the selected design package to the named manufacturer. Only then call create_manufacturing_handoff with the exact package and options, current baseRevisionId and an idempotency key. A successful handoff supplies a vendor review URL. Label it Review & order and report files transferred or review opened. Do not say an order was paid or confirmed without actual vendor evidence. Do not submit payment.

After the user explicitly approves transfer of the checked package to the chosen manufacturer, call `create_manufacturing_handoff` with `transferApproved: true`. Never infer transfer approval from a quote request.
