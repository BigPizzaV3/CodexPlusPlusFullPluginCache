# IndieCRM

Connect your IndieCRM workspace to ChatGPT or Codex through the hosted MCP
server at `https://indiecrm.app/mcp`.

The `manage-crm` skill discovers accessible workspaces, reviews pipelines and
deals, finds contacts and companies, creates linked deals, moves deals between
stages, and records activities. Tools act with the connected IndieCRM account's
existing access. Check the account shown on the OAuth consent screen before
approving the connection.

Deal, contact, and company lists return at most 200 recent rows without
pagination. The plugin cannot send messages, schedule calendar events, manually
create or edit contacts and companies, or delete records. Logging an email or
meeting records an activity; it does not send an email or schedule an event.

The server also exposes saved research lists, verified LinkedIn contact
enrichment, and CLI setup tools. Enrichment can update existing contact fields
and images and may use metered provider research. Inspect ambiguous profile
matches before confirming them. Saved research lead lists support pagination.

The `save-lead-research` skill saves verified company and lead research. Research
imports require access to the **New leads private beta**; an ordinary subscription
does not grant that access. Imports appear in New leads and do not automatically
create deals.

Ordinary IndieCRM users pay USD 9/month after a 7-day trial through the IndieCRM
website. The plugin has no checkout or payment tools.

- [Website and plugin guide](https://indiecrm.app/plugin)
- [Support](https://indiecrm.app/support)
- [Privacy](https://indiecrm.app/privacy)
- [Terms](https://indiecrm.app/terms)
