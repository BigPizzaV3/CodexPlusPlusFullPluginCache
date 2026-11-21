---
name: tax-settings
description: "Review Otis tax guidance and confirmed registrations; only owners can save a tax profile."
---

# Tax settings with Otis

Use the connected Otis MCP at https://mcp.otisbase.com/mcp. If its tools are unavailable, explain connection and email-code sign-in in the browser; never ask for codes in chat or simulate a successful action.
First find the business with businesses_list and pass its business_id on scoped calls. Read business_get for missing setup.
Read otis://docs/workflows when available. Ask only for missing facts. Never invent prices, payments, tax treatment or consent. Monetary values use integer currency minor units. Reuse a stable request_id for identical write retries; follow structured blockers instead of guessing.
Workflow tools: business_get, tax_guide, tax_profile_set.

1. Read the saved business tax profile and tax_guide for the confirmed country. Establish seller location, registrations, customer location/status, service and dates as relevant; do not infer these from currency.
2. For a requested change, confirm registration details, effective/review dates and notes before tax_profile_set. Unknown remains unknown; never default to not registered or zero tax. Only owners can save tax settings. Country guidance and field validation do not certify legal liability or select an automatic rate.

Stay within the requested workflow. A command starts guided work; it does not approve unspecified writes or invoice issuance. Show the recorded result and any remaining steps.
