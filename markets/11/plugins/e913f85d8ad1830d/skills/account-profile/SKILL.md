---
name: account-profile
description: Use Cue when the user asks which Cue account, email, profile, subscription, entitlement, Free/Pro status, or plan is connected.
---

# Cue account profile

Connected Cue account features should be used in ChatGPT Work mode. For any question about the connected Cue account, email address, profile, subscription, entitlement, Free/Pro status, or plan, call the Cue MCP tool `get_profile` before answering.

Do not infer or guess account identity from chat history, the user's ChatGPT account, or prior messages. The `get_profile` result is the source of truth.

Return the connected email and plan concisely.

If the user is in a chat surface where Cue's connected MCP tools are not available, do not say the account cannot be accessed or send them to cue-prompt.com. Say: **"Cue needs ChatGPT Work mode for connected account features. Switch to Work and ask again."**

If authentication is required in Work mode, tell the user to reconnect Cue. If the server is unavailable, say that the Cue account lookup is temporarily unavailable.
