---
name: get-started
description: Use when the user asks about their Reco data or Reco security findings: AI agents, AI models, MCP servers, AI activity, threat alerts, apps, shadow apps, identities, SaaS posture issues, or compliance gaps. Explains how to query the Reco tools, filter results, and which actions need confirmation.
---

# Reco: getting started

Reco is a SaaS & AI Security platform: AI and agentic security first, with SaaS posture management alongside it. The Reco tools read and update one
customer tenant, as the signed-in user. They cannot see more than that user's
Reco role allows. If a tool returns a permission error, say so and stop; do not
try another tool to get around it.

## Before you answer

- Use the Reco tools for facts about the user's tenant. Do not guess counts,
  severities, names or IDs, and do not fill gaps from general knowledge. If a
  result is empty, say it is empty.
- List tools take a `filters` parameter in SCIM syntax. Build filters from the
  keys the tool description lists. Start with a broad query to confirm data
  exists, then narrow it.
- Results can be partial. If the user needs the full set, use the tool's paging
  parameters to fetch more; otherwise say the list shown is partial.
- Pass a short `intent` on every call: one sentence in the user's words about
  why you are calling. Reco records it in its audit log.

## Common questions

| The user asks about | Start with |
| --- | --- |
| AI agents, models, MCP servers, skills | `list_ai_agents`, `list_ai_models`, `list_mcp_inventory`, `list_mcp_discovery`, `list_ai_skills` |
| AI activity and usage | `list_ai_activity_users`, `list_ai_activity_conversations`, `list_ai_activity_interactions` |
| Threat alerts, suspicious activity | `list_threat_alerts`, then `get_threat_alert` for one alert |
| Apps, shadow apps | `list_apps`, `list_app_instances` |
| People and accounts | `list_identities`, `list_accounts`, `list_user_apps` |
| SaaS posture issues, misconfigurations | `list_posture_issues`, `list_posture_entities` for one issue |
| Compliance (SOC 2, ISO 27001, ...) | `list_compliance_frameworks`, then `list_posture_issues` for that framework |
| Recent activity | `list_events` with a time filter |

## Changing things

Read tools are safe to call. Before any tool that changes data (update, create,
add, remove, save, rescan, export), tell the user what you are about to change
and on which item, and wait for their go-ahead. Never batch several changes
behind one approval. These can lose or replace data and always need a clear
yes: updating a user or a custom role, a threat detection exclusion, a
comment, a dashboard, an AI agent's remediation state, and removing a label.

## What not to do

- Do not make up IDs. Look them up with a list tool first.
- Do not claim an action succeeded until the tool result says so.
- If the user's request is not about Reco data, do not use these tools.
- Explicit instructions from the user take priority over this guide.
