---
name: gtm-audit
description: Use when the user wants to audit the health of a brand's Google Tag Manager container (tags, GA4, pixels, Consent Mode, issues).
---

Audit a brand's Google Tag Manager container and explain the findings in plain language. Read-only flow. Reply in the user's language.

1. Call `list_brands` and confirm the brand.
2. Call `gtm_list_containers` with `brand_id` to confirm the container selected for the brand. If the list is empty, the brand has not chosen a container yet: tell the user to do it in Abency.
3. Call `gtm_container_overview` for the summary (published version and number of tags, triggers and variables).
4. Call `gtm_audit` for the health checks (GA4, pixels, paused tags, Consent Mode, server-side…). For the details of a tag, use `gtm_list_tags`.
5. Write the audit:
   - Overall status (good / warnings / failures).
   - What is working.
   - Warnings and failures: what it is, why it matters and how to fix it.
   - Prioritized recommendations, starting with what most affects measurement and privacy.

Rules:
- Make MCP calls one at a time.
- The data comes from the container's last sync; mention the date if the user has just made changes.
- Turn technical detail into concrete actions; do not just list the JSON.
