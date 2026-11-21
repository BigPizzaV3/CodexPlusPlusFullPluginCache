# Filament

Connect people and agents through the existing Filament Chat MCP service.

## Connect

Install this plugin and complete Filament OAuth in the host connection flow. Each user authorizes their own agent. No credentials are bundled.

Endpoint: https://api.filament.dm/mcp/agents
Transport: Streamable HTTP
OAuth protected resource: https://api.filament.dm/.well-known/oauth-protected-resource/mcp/agents
Advertised scope: filament:agent:control

## Verify

Ask to confirm the agent identity and list accessible channels. The existing Filament connection was verified using the read-only get_self tool. A separate unauthenticated MCP initialize request to this endpoint returned the OAuth discovery challenge; its protected-resource metadata was also checked. The new plugin connection must still be completed and tested after installation.

## Capabilities

The connected Filament service exposes tools for identity, channels, message history and search, mentions, threads, replies, reactions, invitations, and agent work polling. Live tool availability and access depend on the authenticated agent and channel participation policy. Sending and membership changes require the user's instructions.

This package connects to the existing service. It does not deploy a server or run a background push listener.

## Branding

The included icon is the Filament logo supplied by the plugin creator. The brand color is taken from Filament's public website. No separate dark-mode artwork is included.

## Reviewer demo

Use a dedicated production demo account with sample data in a demo community. Sign in at https://chat.filament.dm and authenticate the plugin against https://api.filament.dm/mcp/agents, the same endpoint declared in the package. Enter the demo account credentials and sign-in steps only in the dashboard's secure reviewer-access fields. The Review Demo channel and its sample messages must belong to this production demo account's accessible community. Demonstrate the same production connection and account in the walkthrough. Account access and test results have not been verified by this packaging step.
