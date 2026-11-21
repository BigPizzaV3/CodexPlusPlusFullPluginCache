---
name: pyai-voice-agents
description: "Build or update PyAI voice agent profiles for reception, appointment booking, customer support or other conversational workflows."
---

# Voice Agents

Use the connected PyAI tool schemas as the source of truth; clients may prefix tool IDs with the server name. If PyAI is disconnected, direct the user to the host's browser sign-in. Keep credentials out of chat. Respect the selected project and the user's authorized task.

Tools: `whoami`, `list_voices`, `list_agents`, `create_agent`, `get_agent`, `update_agent`, `set_agent_tools`, `set_agent_knowledge`

Establish the task, greeting, persona, language and voice. Resolve a voice from `list_voices`; inspect an existing agent before updating it. Use the schema's `body` object for profile fields. Creating a profile is a persistent change, so do it when the user requests creation, not merely to provide a code example.

Attach only the requested tools and knowledge to the selected agent. Return its actual ID and explain the next integration step.

MCP manages profiles; it does not itself start a microphone session or place a phone call. For a live conversation, use the Omni SDK or WebSocket integration with the saved agent ID as `session_label`. Fetch the current realtime guide at https://docs.pyai.com/guides/omni-overview. Do not invent WebSocket events, supported languages or telephony actions.

For hosted MCP tool bindings, accept only saved tool IDs and enabled flags. Configure connection credentials and settings privately in the PyAI console. Read the existing agent before replacing bindings; retained bindings preserve saved settings. Do not ask the user to paste credentials into the conversation.
