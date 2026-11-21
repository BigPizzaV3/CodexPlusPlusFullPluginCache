# Rebrand

Search Rebrand's published brand identities and visual assets from an MCP client.

## Capabilities

- `search_brands`: search identities, filter the catalog, open a returned slug and find similar brands.
- `search_shots`: search individual visual assets by description, asset type, tags or color.
- Clients supporting MCP Apps can display an interactive gallery. Other clients receive references and source links.

## Connection

Remote Streamable HTTP endpoint: `https://mcp.rebrand.gallery/mcp`.
Authenticate through Rebrand's OAuth sign-in and consent flow using an existing account with access to the feature.
No API keys or passwords belong in the configuration.

## Limits

The tools read the published catalog. They do not edit, delete, upload or generate artwork.
Results depend on the current catalog; empty searches should not be presented as successful matches.

## Documentation, privacy and support

- Setup: https://mcp.rebrand.gallery
- Privacy: https://www.rebrand.gallery/privacy-policy
- Terms: https://www.rebrand.gallery/terms
- Support: contact@rebrand.gallery

Rebrand authenticates the account and checks feature entitlement. Search arguments and sanitized product telemetry are handled as described in the privacy policy. This configuration package includes no credentials or user data.
