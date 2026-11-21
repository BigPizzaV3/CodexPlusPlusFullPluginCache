---
name: carbide-phone-agents
description: Inspect, create, update, and pause Carbide phone agents when the organization has the phone-agents feature. Use for voice-agent configuration, not ordinary customer phone records.
---

# Carbide phone agents

1. Read `get_phone_agent_defaults`, `list_phone_agent_voice_options`, and `list_phone_agents` before proposing configuration.
2. Use an available voice ID and keep the agent's instructions within the business purpose the user supplied.
3. Create or update one agent at a time, then re-read it to verify the effective configuration.
4. Explain that pausing stops the agent from handling calls before calling `pause_phone_agent`.
5. If these tools are absent, report that the organization does not currently have the phone-agents feature or the user lacks access; do not substitute customer phone-number tools.

Phone-agent changes require `mcp.write`, an administrator role, and the product feature gate.
