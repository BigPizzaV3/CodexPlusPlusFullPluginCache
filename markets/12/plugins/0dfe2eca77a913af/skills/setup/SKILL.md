---
name: setup
description: Connect the Franlever plugin to an existing account and guide operators to the next missing setup step.
---

# Set up Franlever

Franlever serves single-store owners, multi-unit operators, and franchisor corporate teams, with one AI COO per brand. Authenticate through the bundled Franlever MCP connection. Never request passwords, API keys, POS credentials, or database access in chat.

Call `list_workspaces`. If authentication is required, use the host's connection flow. Ask which workspace when several are available and the intended one is unclear, then pass its `workspace_slug` to subsequent calls. An empty list can mean assistant access is disabled; it does not prove there is no account. Direct the user to Settings > Assistants in Franlever when appropriate.

Call `list_locations` for the resolved workspace. Use returned store IDs, never guessed IDs. Give a short view of available stores and answer their operational question using the AI COO skill.

For incomplete account or data setup, link to https://app.franlever.com. New accounts first complete the resumable foundation wizard; registration collects only work email. Operational setup follows Connect Data, Confirm Locations, Configure AI COO. Do not recreate existing connections in chat or send users to a dead dashboard. Do not claim to detect connection health or settings the tools do not expose.

Daily monitoring and automatic delivery run in Franlever. Store scope is configured per brand's AI COO; owners and GMs come from store assignments. Owners and GMs have separate channel choices. Members receive briefs on their own clock; GM delivery follows each store's timezone.

The connection is read-only. Configuration belongs in Franlever's existing screens. Never claim to have enabled AI COO, changed a schedule, added recipients, connected a POS, or sent a message by reading data.
