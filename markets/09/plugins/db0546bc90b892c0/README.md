# Musael for ChatGPT, Codex and Claude

Musael is a writing app for novels, series and long stories. This plugin connects ChatGPT, Codex and Claude to the writer's own Musael account, so the planning done in a conversation ends up in the book.

## What it does

- **Start a project from an idea.** Talk a story through, then ask the assistant to save it: Musael creates the project with its acts, chapters and scenes (each with a short synopsis) and the characters, places, objects and factions of its World.
- **Add to a project.** New acts, chapters and scenes go into the Plan, new entries into the World. Nothing that exists is renamed, moved, overwritten or deleted.
- **See the Plan in the chat**, with a button that opens the project in Musael.
- **Where the writer's Musael account includes manuscript access:** read scenes and chapters, search the manuscript, look up the World and the story timeline, run the style report of a scene, see readers by chapter of a published story, and suggest edits that wait in Musael until the writer accepts or rejects them.

The plugin never writes the story's text into the manuscript. Scenes created from a conversation are empty: the writing happens in Musael.

## Skills

- **plan-a-novel**: from an idea in the chat to a Musael project.
- **build-story-bible**: save the characters and places discussed to the World, without duplicates.
- **check-chapter-consistency**: compare a chapter with its World, timeline and style report, quoting each problem (needs manuscript access on the Musael account).

## Setup

1. Install the plugin, or add the connector, and connect your Musael account when asked. You sign in on musael.com and choose whether the app may only read or also add, and whether it sees all your projects or one.
2. Ask something like "Turn this idea into a Musael project with three acts".
3. Disconnect at any time in Musael, Settings, Connected apps.

Server: `https://app.musael.com/api/mcp` (Streamable HTTP, OAuth 2.1 with PKCE).

## Privacy

The plugin reads and writes only the Musael projects of the account you connect, within your current access, and only when a tool is called. Musael does not train AI models on your writing. What Musael collects, why, who processes it and for how long is in the privacy policy: https://musael.com/privacy. Terms: https://musael.com/terms.

## Support

support@musael.com · https://musael.com/help/connect-chatgpt-and-claude

Musael is made by Lucernel LLC.
