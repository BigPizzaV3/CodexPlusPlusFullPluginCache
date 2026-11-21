# Simplio3D plugin for ChatGPT and Codex

Connects ChatGPT and Codex to a Simplio3D workspace through the Simplio3D MCP server at https://app.simplio3d.ai/mcp. Simplio3D is a 3D product configurator and CPQ platform: manufacturers and retailers build interactive 3D configurators with options, rules, materials and pricing, and publish them on their own websites and stores.

This version is **read-only**. The skills audit configurators, explain conditional rules, check 3D part targets, explain and calculate prices (including the advanced pricing steps), check publish readiness, and answer questions from the official documentation. They never change a project, publish it, connect a store or contact customers.

## Package

| File | Contents |
|---|---|
| `plugin.json` | Package identity, the directory listing, review test cases and release notes (under `extensions["com.openai"]`). |
| `mcp.json` | The Simplio3D MCP server: Streamable HTTP at https://app.simplio3d.ai/mcp, OAuth 2.1 with PKCE and dynamic client registration, read-only default permissions. |
| `skills/` | Seven skills (below). |
| `assets/` | The listing icon and the composer icon. |

## Skills

| Skill | Use it for |
|---|---|
| workspace-navigation | Finding projects, options, materials and models by name; AI change history; connection, permission and error messages |
| configurator-audit | A full audit of a configurator, grouped by area, with the fix for each finding |
| hidden-option-diagnosis | Why an option, variant or 3D part is hidden for a given set of selections |
| model-target-check | Whether every 3D part an option or rule targets exists in the model file |
| pricing-cpq | How a project is priced (including markup, tiers, discounts, charges, shipping and tax), what a configuration costs, and SKU coverage |
| publish-readiness | A ready / not-ready verdict with the list of what to fix before sharing |
| simplio3d-help | How-to and "can Simplio3D…" questions, answered from the documentation with a link |

## Requirements

A Simplio3D account with a confirmed email on any paid plan (Starter, Pro or Enterprise) or an active 30-day trial. Sign-in happens on app.simplio3d.ai with OAuth; the user picks the workspace and the permissions to grant. Read-only access is pre-selected.

## Data and privacy

- **Runs:** nothing locally. The skills are instructions only; there are no scripts.
- **Sends:** tool calls to the Simplio3D MCP server, https://app.simplio3d.ai/mcp, for the workspace the user connected.
- **Fetches:** results from the user's own Simplio3D workspace and the published Simplio3D documentation.

Simplio3D does not receive the conversation, only the tool calls. Details: https://app.simplio3d.ai/docs/mcp/privacy-data-handling. Privacy policy: https://www.simplio3d.com/privacy-policy. Support: https://www.simplio3d.com/contact-us.
