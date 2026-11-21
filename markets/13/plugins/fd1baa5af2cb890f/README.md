# TourMind Hotel Booking 1.0.9

Compare live hotel rates across multiple booking channels, verify the selected offer, submit a reservation after confirmation, and manage hotel orders through TourMind.

## Listing

- Website: https://tourmind.com/en-US
- Support: https://tourmind.com/en-US
- Privacy policy: https://tourmind.com/en-US/credit?type=privacyPolicy
- Terms of service: https://tourmind.com/en-US/credit?type=termsAndConditions

The platform listing fields, capabilities, starter prompts, Skill description and Skill display name are in English. The Skill still responds in the user's language. This release supports hotels only and does not claim a guaranteed lowest price or exhaustive channel coverage.

## Connection

- MCP server: `tourmind-hotel`
- MCP URL and OAuth resource: https://mcp-booking.tourmind.com/mcp/oauth/toc
- Transport: Streamable HTTP
- OAuth scope: `mcp:access`
- Client mode: `provided`
- Client ID: `chatgpt`
- Token endpoint authentication method: `none`

The MCP configuration is unchanged from version 1.0.8. Authorization endpoints continue to use service discovery. The package contains no client secret, access token, refresh token, legacy user key or private app binding. OAuth credentials belong to the host-managed connection.

## Updating the draft

Upload the complete 1.0.9 ZIP as a new version of the existing `tourmind-hotel-booking` plugin. Verify the imported version, English listing text and all four listing URLs in Metadata & Skills. The icon remains the original `logo2.svg`.

The supplied support URL is the official website, as requested by the publisher. Website, terms and privacy pages were accessible in the URL check on October 26, 2026; this is an accessibility check, not a legal review.

## Validation and review status

Local validation covers JSON/YAML parsing, the plugin schema, the portable MCP schema and explicit OAuth configuration checks, listing field limits, URL values, icon integrity, preserved workflow instructions and the contents of the actual ZIP.

The five positive and three negative review cases are English drafts. They have not been run in this packaging task. Booking and cancellation tests require an explicitly designated sandbox and safe test data. No hotel search, booking, cancellation or payment was performed while preparing this release. No new end-to-end OAuth test is claimed.

Complete the remaining review information and record actual test outcomes in the developer portal before submitting for review. This ZIP updates the package and listing; it does not itself complete review or publish the plugin.

## References

- https://developers.openai.com/plugins/deploy/submission#listing-metadata
- https://developers.openai.com/plugins/build/plugins#configure-mcp-authentication
- https://developers.openai.com/plugins/build/auth
