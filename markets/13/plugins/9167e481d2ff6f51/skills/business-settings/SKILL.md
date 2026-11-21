---
name: business-settings
description: "Review or set up Otis business identity, currency and invoice preferences; only owners can save changes."
---

# Business settings with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: business_get, business_set.

1. Read business_get and ask only for missing or explicitly changed facts: business name, currency, billing address and invoice preferences. Show the profile before saving with business_set. Preserve existing values; currency locks after financial records and the starting number locks after first issuance. Only owners can save changes.
2. Keep tax registration and treatment in the separate tax-settings workflow. Do not infer tax facts from currency or imply business setup completes tax setup.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
