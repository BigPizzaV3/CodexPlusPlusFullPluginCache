# Filinvest Hospitality

Connection package, version 0.1.0, for the existing Hyperguest-hosted MCP service.

## Contents

- `plugin.json`: portable plugin identity, listing text and draft review cases.
- `mcp.json`: Streamable HTTP connection to the supplied endpoint.
- `docs/discovered-tools.json`: read-only tool discovery snapshot from 13 October 2026.
- `docs/verification-and-public-submission.md`: verification scope and remaining public-review materials.

## Use

Use this ZIP where the target host supports Agent Plugins 1.0 packages. If the interface asks for a plugin folder, extract the ZIP and select `filinvest-hospitality`.
If the interface instead asks for an MCP server URL, use `https://filinvest.mcp.hyperguest.io/chatgpt` and the provider's No Auth configuration. No credentials, access tokens or session IDs are included.

The host must support Streamable HTTP and the provider's interactive hotel/availability views for the complete experience. A successful file import alone does not verify that those views render or that checkout works.

This package references the remote service. It does not contain Hyperguest's server source, hosted UI source or hotel database and does not deploy them. It does not install itself, submit an app for review or make the app publicly available.

## Exposed tools

`search_hotels` discovers properties using a query and supported destination, rating and amenity filters.
`check_availability` accepts hotel IDs, check-in date, nights and guests, with optional meal-plan, nationality and cancellation filters. The response references the provider's availability/checkout view.

Never infer a confirmed booking from search or availability alone. Do not collect card details in chat or store them in this package. Show live rate-specific policies in the provider checkout and require the guest to approve booking details there.

## Example prompts

- Show me Filinvest hotels in Boracay.
- Find up to three family-friendly Filinvest hotels with an outdoor pool.
- Check the selected hotel for 1 December 2026, two nights and two adults, with breakfast.

Replace dates with future dates when using these examples later. Use actual property IDs returned by the live catalog.
