# Agent Social

Make, review and fix films and TV series, short videos, memes, research and social posts in your Agent Social account from a conversation with your AI agent. The same characters and places stay consistent from shot to shot and episode to episode.

## What it does

Your agent reads your series, episodes, chapters and clips, watches the rendered clips frame by frame, and compares them with the pictures and story they were made from. It asks your Agent Social studio for every change — new films and episodes, rewritten clips, characters, places, voices, rendering, music, subtitles and post cards — follows the work until it is done, and checks what came back before telling you. Social posts and automated posting schedules go through your Agent Social agent the same way.

## Use it

1. Connect the Agent Social connector once, and sign in with your Agent Social account:
   - **Claude (web, Desktop, mobile, Cowork):** Settings → Connectors → Add custom connector, name it Agent Social, paste `https://mcp.agentsocial.dev/mcp`, then Connect and Allow.
   - **Claude Code:** run `claude mcp add --transport http agentsocial https://mcp.agentsocial.dev/mcp`, then `/mcp` → agentsocial → Authenticate.
   - **Other agents:** add `https://mcp.agentsocial.dev/mcp` as a streamable HTTP MCP server.
   This plugin adds a short skill that tells your agent to load its instructions from the connector at the start of each session, so it always works the current way without you updating anything.
2. Ask in plain words: "review chapter 1 of my coffee ad and fix what's off", "make the next episode where she opens the shop", "write an X post for this film".
3. Follow along live: your agent shares the link to the episode's chat in Agent Social, where every change appears as it happens.

Reading and watching are free. The studio's work — rendering, new pictures, music, voiceover and the rest — uses your Agent Social credits, exactly as in the app, and your agent asks for it only when you did.

## Data

The plugin talks only to your own Agent Social account at agentsocial.dev, through the Agent Social connector you sign in to. It stores nothing itself. What your agent changes is recorded in your episode's chat, labelled as coming from your agent.

Support: support@agentsocial.dev
