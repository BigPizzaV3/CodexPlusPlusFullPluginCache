---
name: setup
description: Set up Zopley after installation, check the public connection and help the user connect their own account for the permissions their task needs.
---

# Set up Zopley

Use this skill when the user runs plugin setup or asks to connect or get started with Zopley.

1. Call the available Zopley `site.pages` tool to check public access. Use returned destinations rather than guessing URLs. Do not change any account settings during setup.
2. If the user has already stated a task, continue toward it. Otherwise ask whether they want to inspect their rooms, organize their media library or manage a room.
3. Public pages do not need authentication. For private account tasks, use the host's OAuth connection flow. Explain the specific permissions the task needs. Never ask for a password, bearer token, API key or verification code in chat.
4. After connecting, inspect the actual available tools. If the task needs an account summary and `account.snapshot` is available, read it. If the connection lacks a required tool or permission, ask the user to reconnect with that permission through the host. Do not substitute another account or credential.
5. Explain any concrete connection error and the next available action. A successful public call does not prove OAuth is connected. A successful private call proves only that account's current granted access.
6. Continue with the packaged `manage-zopley` skill for the requested task. Scoped changes execute automatically by default under the account's approval preference. If the server requires manual confirmation, the owner confirms and executes the exact request inside the Zopley chat.

Keep setup short. Do not claim the plugin is published, verified or approved based on installation. Do not create a room, grant broader permissions, change approval settings or begin a paid operation unless the user requested it.
