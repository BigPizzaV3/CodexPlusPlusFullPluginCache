# EasyPost

Better rates, smarter shipping.

This plugin connects to EasyPost's hosted MCP server and works with the user's production EasyPost account.

It can quote rates for US domestic shipments, buy labels, add shipping insurance, request refunds for unused labels, verify addresses, register trackers for tracking numbers bought elsewhere, and estimate delivery dates with SmartRate. It can also look up existing shipments, stored rates and labels, trackers, saved addresses, carrier accounts and capabilities, scheduled pickups, refund status, insurance records, claim status, payment methods, and the postage wallet balance.

Buying a label or insurance debits the account's EasyPost postage wallet. The user approves the carrier, service, and price first, and a buy is refused if the price passed does not match the rate. Quoting rates, verifying addresses, SmartRate delivery dates, and registering a tracker can be billed under the account's EasyPost pricing.

The plugin does not file or cancel claims, add or change carrier accounts, add or change payment methods, or change account settings. Use EasyPost directly for those.

## Connect

The server endpoint is `https://app-api.easypost.com/mcp` over Streamable HTTP. This package configures EasyPost as a pre-registered OAuth client with the supplied client ID, `client_secret_basic`, and the `all` scope. Do not use dynamic client registration, a client metadata document, or API-key/bearer-header authentication. Do not put the OAuth client secret in this package or ZIP. After upload, enter the OAuth application client secret in the Connect panel's secure OAuth Client Secret field. This application secret is distinct from an EasyPost API key and a user password. Register the OAuth app redirect URI using the exact callback shown on the MCP management page; AppAuth requires an exact string match.

See the [EasyPost MCP Guide](https://docs.easypost.com/guides/mcp-guide) for current setup details and tool behavior.
