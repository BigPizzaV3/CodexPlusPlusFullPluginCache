---
name: carbide-integrations-webhooks-and-api-keys
description: Inspect and configure Carbide integrations, CRM synchronization, webhooks, custom booking domains, and API keys. Use for administrator-owned external-service setup and troubleshooting.
---

# Carbide integrations, webhooks, and API keys

Read status before changing anything with `list_integrations`, provider-specific connection tools, webhook lists, custom-domain settings, and `list_api_keys`.

- Connect or reconnect PaintScout at `/settings/organization/integrations/paintscout` and Pipeline CRM at `/settings/organization/integrations/pipeline_crm` in Carbide. Never ask for API keys, passwords or MFA codes in chat. Other providers use the browser authorization URL described by their status tools.
- Google Analytics and Tag Manager share browser authorization. Choose a GA4 stream and GTM web container separately, then use their independent enabled controls. Disconnecting Google clears both selections.
- Configure sync state, deal stages, imports, webhooks, and field mappings only after the provider reports connected.
- Treat arbitrary webhook URLs and custom domains as open-world destinations. Repeat the host to the user before creating or replacing them.
- Explain that disconnect, revoke, secret rotation, cursor clearing, and delete actions can interrupt automation or invalidate credentials.
- Never reveal or request stored secrets. API key plaintext is available only at creation in the Carbide web app; an MCP API key cannot revoke itself.

These tools require `mcp.write` and an owner or administrator role. A provider's own authorization and Carbide product gates also apply.
