---
name: viasocket-mcp
description: Use when a developer wants to connect apps, discover available viaSocket MCP actions, or design integrations and automations using viaSocket.
---

# viaSocket MCP workflow

Use the connected viaSocket MCP server to discover the tools and schemas actually available to the authenticated user. Do not assume every integration or action is enabled on every endpoint.

## Workflow
1. Clarify the user's desired outcome and which connected app or workflow is involved.
2. Inspect available tools and their input schemas before choosing an action.
3. Explain which action will be used and what it changes when the action is consequential.
4. Ask for confirmation before destructive, externally visible, financial, or bulk changes unless the user has already clearly authorized that exact action.
5. Use only fields and permissions supported by the discovered schema. Do not fabricate IDs, connection states, results, or tool names.
6. Report the result accurately, including failures or any steps the user must complete in OAuth or the provider UI.

## Security
- Let the MCP host perform OAuth and consent. Never ask users to paste passwords, access tokens, refresh tokens, or client secrets into chat.
- Treat connected app data as user data. Retrieve only what is needed for the requested task.
- Verify the target account, record, recipient, and scope before performing write actions.
- If a tool is unavailable, explain that the current endpoint or account does not expose it rather than implying the whole viaSocket platform lacks the capability.

## Product context
viaSocket describes a platform for app integrations, multi-step automations, AI agent tooling, authentication and organisations, and embedded integration UI/catalog APIs. Treat these as product capabilities to explore, not as proof that a specific MCP tool is available. The current server's tool list and schemas are authoritative for executable operations.
