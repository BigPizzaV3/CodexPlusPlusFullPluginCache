---
name: leadshield
description: Preview contact form screening, manage connected-site rules, review retained blocked messages, and generate setup instructions.
---

# LeadShield Contact Form & B2B Solicitation Blocker

Author: Daniel Hallman ([Moosh Works](https://mooshworks.com))

Preview contact form screening, manage rules for connected sites, review retained blocked messages, and generate setup instructions. Screening previews do not store or deliver leads or process payments.

## Quick start

1. Open the [LeadShield setup guide](https://ghlagencymcp.com/use-cases/ghl-contact-form-spam-blocker) and choose your website or CRM.
2. Connect a client that supports Streamable HTTP MCP to `https://rankandrent-leads.hallmanlab.workers.dev/mcp`.
3. Sign in and grant site access. Check the intended site's active rules with `leadshield_get_spam_policy` before making changes. See the [form screening instructions](../leadshield-form-spam-blocker/SKILL.md) for tool limits, pricing, and installation checks.
