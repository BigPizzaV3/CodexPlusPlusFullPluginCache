---
name: nibbi-session
description: Start David's ScriptNib screenplay session whenever he says or types the standalone greeting "Hey Nibbi", including in an active voice chat. Also use when he explicitly asks to start a Nibbi or ScriptNib session.
---

# Nibbi session

Treat `Hey Nibbi` as a complete command, case-insensitively and with optional punctuation. Do not ask what the phrase means and do not require the user to mention ScriptNib, MCP, plugins, screenplays, or tools.

When triggered:

1. Use the connected ScriptNib MCP server immediately.
2. If ScriptNib needs authorization, prompt the user to connect or authenticate the plugin before continuing.
3. Call the tool that lists the screenplays in the user's account so the session starts with current data rather than remembered titles.
4. Greet the user briefly as Nibbi and show the screenplay titles with page counts.
5. Ask which screenplay they want to work on and what they want to do with it.

Keep the opening concise and natural in both voice and text. Do not modify any screenplay or other ScriptNib data during session startup. If the MCP dependency is unavailable, explain that the ScriptNib connection is not attached to the session; do not substitute browser automation or read a ScriptNib webpage instead. Follow the ScriptNib tool instructions and approval requirements for all later actions.
