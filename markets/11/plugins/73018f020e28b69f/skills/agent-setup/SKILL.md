---
name: agent-setup
description: Use when a user asks how to create or configure a QualifyBase agent, select its goals, language, behavior, knowledge, voice, channel assignment, or test it in the Playground.
---

# Agent setup guidance

Start with the user's goal and existing setup. Ask a focused question only when needed, such as inbound qualification versus outbound calling, supported language, booking goal, or approved business policy. Do not invent offers, prices, opening hours, guarantees, or services.

Before the first connected workspace operation, use `get_account_info` to confirm the workspace. If separately authorized prompt tools are available, `list_agents` can identify existing agents. Multiple agents require selecting the intended one; do not guess. Without those tools, ask the user which agent they are viewing.

Agent creation and non-prompt configuration remain dashboard actions:

1. Open [Agents](https://www.qualifybase.com/agents) → **Create agent**. Choose its name, language, direction, and business goal.
2. Open its **Playground**. **Instructions** contains its system prompt; **Knowledge**, **Behavior**, and **Voice** control their respective settings.
3. Draft instructions using the user's confirmed business facts and policies. For an existing prompt, use `prompt-editing` to read and preview a targeted change.
4. Test a greeting, qualification questions, a price question, an unknown fact, a booking request, and human handoff in a fresh Playground session.
5. Assign connected channels from [Workspace → Channels & Integrations](https://www.qualifybase.com/workspace/channels). Phone assignments are configured separately in the dashboard.
6. Review agent status before live testing. Paused agents still work in the Playground but do not answer on live channels. The user pauses or resumes the agent in the dashboard.

MCP can read and preview a separately authorized system prompt. With separate prompt-write approval and safe editing enabled, use `prompt-editing` to save the exact approved preview for an eligible paused agent. Otherwise saving stays in Playground → Instructions. MCP cannot create agents or change their greeting, voice, goals, language, behavior toggles, status, knowledge files, channels, or integration credentials. Explain the relevant dashboard control when asked for those changes. Never report a draft as saved or a guide as an executed setup.
