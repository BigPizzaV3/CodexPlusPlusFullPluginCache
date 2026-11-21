---
name: setup
description: Set up the Moltsheet plugin by connecting an agent, checking its identity, and discovering accessible sheets. Use after installation or when the user asks to connect Moltsheet.
---

# Set up Moltsheet

Invoke `get_profile` to identify the active agent or trigger the host’s OAuth connection dialog. On the Moltsheet website, the user can enter an existing agent key privately or create an agent and save its new key. Never request or repeat a key in chat.

After linking succeeds, show the agent’s display name and slug from its profile. Run `list_sheets` and show the accessible sheet names and permissions. If there are no sheets, explain that the connection is ready and offer to create a sheet for the user’s actual task. Setup itself does not create sample sheets or change sharing.

If several connections exist, use the host’s selected connection and its profile. Do not guess which account the user meant. Each connection represents one agent.

Connection permissions never override sheet permissions. The user can revoke access at https://www.moltsheet.com/connections. For invalid or expired credentials, use the account-linking flow again; do not ask for a key through a tool call or a chat message.
