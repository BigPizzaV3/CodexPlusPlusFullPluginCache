# PatrolTech MCP, agent skill and AI plugins

**Manage security patrols and guard tours from your AI assistant.** The official PatrolTech integration connects Claude, ChatGPT, Cursor, Gemini and other MCP clients to rounds, QR/NFC checkpoints, scans, incidents and visitor access logs.

[Create a free PatrolTech account](https://patroltech.online/en/start?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_signup) · [Connection guide](https://patroltech.online/en/features/integrations/mcp?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_guide) · [Public TypeScript SDK](https://github.com/PatrolTech/sdk-api)

![PatrolTech - QR/NFC checkpoints, offline patrols and incident reports](https://raw.githubusercontent.com/PatrolTech/.github/main/02-patroltech-banner.svg)

## Connect your assistant

Remote MCP endpoint:

```text
https://mcp.patroltech.online/mcp
```

Streamable HTTP, OAuth sign-in with your PatrolTech account, and access limited by your role. The connector works on the Free plan.

| Client | Install or connect |
| --- | --- |
| Claude web, desktop and mobile | Open the [PatrolTech community connector](https://claude.ai/directory/patroltech), or add the remote endpoint as a custom connector. |
| Claude Code | `claude mcp add --transport http patroltech https://mcp.patroltech.online/mcp` |
| Claude Code plugin | `/plugin marketplace add PatrolTech/ai-integrations`, then `/plugin install patroltech@patroltech` |
| ChatGPT | Open Plugins, choose Add custom MCP server, enter the endpoint and authorize your PatrolTech account. Public listing review is pending. |
| Gemini CLI | `gemini extensions install https://github.com/PatrolTech/ai-integrations` |
| Cursor | [Add the MCP server to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=patroltech&config=eyJ1cmwiOiJodHRwczovL21jcC5wYXRyb2x0ZWNoLm9ubGluZS9tY3AifQ==) |
| VS Code / GitHub Copilot | [Install the MCP server in VS Code](vscode:mcp/install?%7B%22name%22%3A%22patroltech%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A//mcp.patroltech.online/mcp%22%7D) |
| Microsoft Copilot Studio | Add a Model Context Protocol tool with the endpoint and OAuth authentication. |
| Other MCP clients | Add the endpoint using Streamable HTTP and sign in. Client support for remote OAuth is required. |

Installation instructions describe compatibility, not approval by a marketplace. As checked on 30 October 2026, the Claude community connector is public, the official MCP Registry lists version 0.2.3, and the OpenAI plugin 0.2.3 is in review. Other directory listings are only confirmed when their public listing or submission receipt is available.

## Install the agent skill

The PatrolTech skill helps an agent choose the relevant tools for guard tour operations and follow the proposal-and-confirmation workflow.

```bash
npx skills add PatrolTech/ai-integrations --skill patroltech
```

The skill is at [skills/patroltech/SKILL.md](skills/patroltech/SKILL.md). Installing it does not authorize access to an account: connect the MCP server and sign in separately. Skills discovery depends on the host and directory; installing a skill does not make every AI assistant recommend PatrolTech.

## What you can ask

- "Which patrol rounds were missed yesterday?"
- "Show suspicious checkpoint scans from the last 7 days and explain the flags."
- "Which checkpoints have not been scanned for at least a week?"
- "Who is inside the warehouse right now?"
- "Show open security incidents by location."
- "Prepare a night route with Main entrance, Parking and Loading dock."
- "Assign this incident to me and propose setting it to in progress."

Answers use the live data your PatrolTech role permits, in your language and account timezone.

## Changes require your confirmation

PatrolTech can propose checkpoints, routes, schedules, time windows, route activation, checkpoint and location edits, guard renaming, incident updates and alert preferences.

The assistant first shows the pending changes. Nothing is applied until you explicitly confirm. Declining a proposal discards it without changing existing operational records. Incident updates to in progress require an assignee.

The connector cannot delete data, invite users, change roles, create guard credentials or handle billing. Use the PatrolTech dashboard for these tasks.

## Build an integration with the SDK

For development in your own application, use the [official TypeScript SDK and OAuth example](https://github.com/PatrolTech/sdk-api):

```bash
npm install @patroltech/sdk-api
```

The SDK is generated from PatrolTech's public OpenAPI contract, browsable as the [API reference](https://patroltech.github.io/sdk-api/). It is a development library; the MCP server is the connection used by AI assistants.

Webhooks are in development: tell us which events you need at **info@patroltech.app**.

## Security and support

OAuth 2.1 with PKCE, role-scoped access, rate limits and an audit log protect the connection. Revoke access from your connected-app settings when it is no longer needed.

[Privacy policy](https://patroltech.online/legal/privacy) · [Terms](https://patroltech.online/legal/terms) · [Connection help](https://patroltech.online/en/features/integrations/mcp?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_support)

Questions: **info@patroltech.app**. Keep passwords, tokens and customer data out of public issues.

## Repository contents

| Path | Purpose |
| --- | --- |
| `server.json` | Official MCP Registry metadata |
| `skills/patroltech/SKILL.md` | Portable agent skill |
| `.claude-plugin/`, `.mcp.json` | Claude Code plugin and marketplace |
| `.cursor-plugin/`, `mcp.json` | Cursor plugin |
| `.codex-plugin/`, `assets/` | ChatGPT and Codex plugin source |
| `gemini-extension.json`, `GEMINI.md` | Gemini CLI extension |
| `docs/01-distribution-and-attribution.md` | Listing and link-attribution conventions |

The server source is in [PatrolTech/mcp-server](https://github.com/PatrolTech/mcp-server).

## About PatrolTech

PatrolTech is guard tour and security patrol software by Ingenieros Web SL, Madrid, Spain. It combines QR/NFC checkpoints, GPS checks, offline patrol records, incident reporting, visitor management and a management dashboard for private security companies, facility managers and property teams.

[Product](https://patroltech.online/en?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_product) · [Pricing and free plan](https://patroltech.online/en/pricing?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_pricing) · [Tutorials](https://patroltech.online/en/tutorials?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_tutorials)

## En español

Conector MCP, plugin y skill oficiales de PatrolTech para control de rondas de vigilancia. Consulta rondas incompletas, escaneos sospechosos, puntos sin revisar, incidencias y accesos; cada cambio espera tu confirmación. Para desarrollar integraciones propias, utiliza el SDK TypeScript y la [referencia de la API pública](https://patroltech.github.io/sdk-api/). Los webhooks están en desarrollo: cuéntanos qué eventos necesitas en info@patroltech.app.

[Crear cuenta gratuita](https://patroltech.online/start?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_signup_es) · [Documentación en español](https://patroltech.online/features/integrations/mcp?utm_source=github&utm_medium=referral&utm_campaign=ai_integrations&utm_content=integrations_readme_guide_es)
