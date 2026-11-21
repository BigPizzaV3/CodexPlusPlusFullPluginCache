# Deliverability AI WarmInboxes v1.0.1 - submission-fixed

Portable OpenAI Agent Plugins submission ZIP for the existing public WarmInboxes MCP at `https://warminboxes.com/mcp`. This package does not deploy or replace the MCP server.

## What changed from v1.0.0

- Rewrote the About/long description to reflect the actual product: cold-email diagnosis, operator recipes, live checks, research and infrastructure planning.
- Improved onboarding instructions around diagnose-first workflows, bounce classification, recipe retrieval and campaign troubleshooting.
- Replaced edge-case review cases with representative user problems such as reply-rate drops, bounce spikes and diagnosis-before-replacement.
- Updated default prompts and capabilities.
- MCP endpoint, no-auth configuration and read-only scope are unchanged.

## Upload

1. Create a new draft/version from this ZIP in the OpenAI Plugins dashboard.
2. Keep the MCP server at `https://warminboxes.com/mcp` with no authentication.
3. Rescan/verify the MCP tool inventory.
4. Run the included positive and negative review cases against the live connected plugin.
5. Submit the new version for review.

## Important

The plugin reads current WarmInboxes resources through the live MCP. New recipes, guides and research can become available through the existing resource-discovery tools without embedding the entire knowledge base in this ZIP. Structural MCP tool/schema changes should be rescanned in the developer portal before assuming they are available to the published plugin.


## Submission validator fixes

- Subtitle shortened to `Cold email diagnostics` (22 characters, under the 30-character limit).
- Starter prompts reduced from four to three.
- Category, MCP endpoint, authentication, skills, review cases and tool behavior are unchanged from the v1.0.1 draft.
