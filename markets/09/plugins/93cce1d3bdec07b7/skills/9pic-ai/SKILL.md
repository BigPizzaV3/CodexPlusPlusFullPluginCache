---
name: 9pic-ai
description: Use when the user wants to connect their 9Pic AI account, identify their account, choose an organisation, manage events and gallery settings, add photo sources, import or process photos, publish or unpublish galleries, check their existing plan and credits, or read event analytics.
---

# 9Pic AI

Use the tools supplied by the connected 9Pic AI server. Discover available tools and their current input schemas at runtime; tools may be added over time. Do not hard-code a tool list, invent tools, or assume unsupported capabilities. Follow current tool schemas, consequences and prerequisites rather than assuming every action uses the same execution flow.

When a task needs an orgId or org_id, call list_organisations first. Use only organisation IDs returned by that call. If several organisations are available and the intended organisation is unclear, ask which one to use. Never guess IDs. Resolve events from returned event data in the selected organisation; ask when the intended event is ambiguous. Keep the chosen organisation consistent across dependent calls.

For account identity, discover and use the available identity capability. If it cannot verify identity, say so; do not infer identity from membership. Use a returned account label when available and distinguish it from an opaque account identifier.

Before the first change for an organisation, call get_plan and explain relevant current-account limits and available credits. Use returned limits, not a static plan table. State existing entitlements neutrally; do not promote upgrades, compare subscription offers, initiate purchases, or provide checkout or purchase links. If a server message suggests a purchase or upgrade, explain only the applicable limit and why the requested action cannot proceed. The connection serves existing accounts.

For an event workflow, resolve the event and inspect its current settings, photo sources and progress as needed. Use dates with a timezone when required; ask for missing essential details. Pass only requested setting changes and preserve unrelated settings. Explain participant-search credit consequences. Do not silently disable search to avoid credit use. Follow constraints such as running-only BIB search and timeline browsing requiring all photos to be shown. Watermark editing remains in the 9Pic AI dashboard when unsupported by the connection.

For photo processing, first use the current preview capability and show the effective photo count and credits consumed from the returned preview. Execute only after the user confirms that preview, using its review_token, confirmed=true and a stable idempotency_key when required by the schema. Do not expose the review token in chat. If the preview expires or relevant inputs change, obtain a new preview and confirmation. An instruction to inspect or preview does not authorise execution.

For an explicitly requested change that the server executes immediately, perform it once after resolving prerequisites. Respect confirmation required by the host, tool or consequences; do not bypass host safeguards. Before publishing, tell the user the event is going live and participants will be able to open the gallery once publishing completes. Before unpublishing, explain that participant access stops and the event returns to draft while photos and settings remain. A request to check readiness or status does not authorise publication.

Report actual operation state and returned consequences. Distinguish queued or running work from completion, and check status when needed without busy polling. On an uncertain dispatch or timeout, use the returned operation identifier to check durable operation status before retrying. Reuse an idempotency key only for the exact same request; use a new key for a new action. If no operation identifier is available, inspect current state and explain the uncertainty rather than blindly repeating a change.

For analytics, describe counts as estimated aggregates, respect the returned date range and timezone, and disclose partial availability or unavailable dates. Missing metrics are not zero, and aggregate analytics do not identify individual participants. For processing progress, prefer returned stage statuses and counts; explain inconsistent or stale fields instead of inferring that a run is still active from its identifier alone.

Authentication is handled by the host's sign-in flow. The connection requires events:read, events:write, and analytics:read. Never ask for passwords, tokens or API keys in chat. Never expose credentials or store them in plugin files. If sign-in has expired or is invalid, tell the user to reconnect 9Pic AI and stop the failed operation. Do not retry in a loop. If access is denied, explain that the user must use their 9Pic AI dashboard account and be a member of that organisation with permission for the requested action.

In user-facing text, mention only 9Pic AI. Do not repeat vendor, hosting, infrastructure, processing-library or internal service names, including photo-source provider labels. Use generic product language such as shared photo folder. Translate explanations to the user's language while preserving 9Pic AI, IDs and schema enum values. Sanitize raw errors without losing their useful product-level explanation.

Use the existing production connection. Do not create a staging connection, local connection script or replacement server.
