---
name: continuity-chatgpt-plugin
description: Preserve the current ChatGPT conversation as a Continuity Ready file so the work can continue in a new conversation.
---

# Continuity Relay

When the user explicitly invokes Continuity Relay or asks to prepare Continuity for continuing this work in a new chat:

1. Use the Continuity Relay MCP workflow.
2. First call `get_continuity_v42`.
3. Apply the returned Continuity V4.2 specification to the conversation context available to you.
4. After producing the complete packaged result required by that specification, call `build_continuity_ready`.
5. Return the generated Continuity Ready file to the user.

Do not substitute another plugin, generic summary, memory workflow, or state-transfer method.

Treat the request to generate Continuity as a transfer operation, not as part of the underlying work state being transferred.