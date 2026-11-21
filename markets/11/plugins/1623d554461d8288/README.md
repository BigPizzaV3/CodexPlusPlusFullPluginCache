# Jetpost plugin

Build on each other's ideas. Tell your agent "make a note." Your team, and
their agents, can pick it up from there.

Jetpost is an inbox of notes for people and their agents. A note you write in
Claude, ChatGPT, Cursor or any other AI lands in your teammates' inboxes. They
can read it, comment on a passage, or have their own agent edit it or add to
it. Every change an agent makes is marked as the agent's.

This plugin bundles the hosted Jetpost MCP server and a skill that offers to
share finished work with teammates, or anyone by email, even people not on
Jetpost.

## Install

**Claude (Claude Code and Cowork)**

```
/plugin marketplace add send-co/jetpost-plugin
/plugin install jetpost@jetpost
```

**Cursor**

Install Jetpost from the Cursor marketplace.

**Gemini CLI**

```
gemini extensions install https://github.com/send-co/jetpost-plugin
```

Or point any MCP client at the server directly:

```
https://www.jetpost.com/mcp
```

## Authentication

Jetpost uses OAuth 2.1 with PKCE. There's no API key to copy.

- Endpoint: `https://www.jetpost.com/mcp` (Streamable HTTP)
- The first time a tool runs, your client opens a browser so you can sign in
- Your client holds the tokens. This repository never sees them.

## What's included

| Component | |
|---|---|
| MCP server | `.mcp.json`: the hosted Jetpost server |
| Skill | `jetpost-share`: offers to share finished work with teammates, or anyone by email, even people not on Jetpost |

## Tools

| Tool | What it does |
|---|---|
| `create_note` | Write a note and share it with people, or keep it to yourself |
| `add_components` | Write a note's components as Markdown; readers watch them land |
| `get_ui_spec` | Get the Markdown syntax for Jetpost's components |
| `search_notes` | Find notes you wrote or that were shared with you |
| `get_note` | Read a note, its pages and its comment threads |
| `edit_note` | Change part of a note, or its title and summary |
| `append_to_note` | Add to the end of a note |
| `create_page` | Add a page to a note |
| `edit_page` | Rename a page or change part of it |
| `add_comment` | Comment on a note or a passage, or reply in a thread |
| `share_note` | Add people to a note and email them when it's ready |
| `list_members` | List the people you share notes with |
| `list_activity` | See what's happened across your notes recently |
| `list_changes` | See a note's edit history |
| `mark_notes` | Archive notes or mark them read |
| `upload_image` | Add an image from your computer to a note. Returns a signed upload address and headers; your agent sends the file from your shell with one fixed `curl -X PUT` step written in the tool description. PNG, JPEG, GIF or WebP, up to 20 MB; the address expires in 15 minutes. Without a shell, your agent asks you to paste the image into the note in the app instead. |

## What it sends and fetches

The plugin talks to `https://www.jetpost.com`. It sends what you ask your
agent to write (note text, pages, comments and the people to share with) and
fetches the notes you can read. The one exception is an image upload: the file
goes from your shell straight to Jetpost's image storage, Vercel Blob
(`https://vercel.com/api/blob`), using the one-time address `upload_image`
returns. Images are read back through jetpost.com. It sends nothing to anyone
else.

Jetpost emails a note's recipients only when you say the note is ready to go
out.

## Links

- [jetpost.com](https://www.jetpost.com/welcome)
- [Docs](https://www.jetpost.com/docs)
- [Privacy policy](https://www.jetpost.com/privacy)
- [Terms of service](https://www.jetpost.com/terms)
- Support: [support@jetpost.com](mailto:support@jetpost.com) or [open an issue](https://github.com/send-co/jetpost-plugin/issues)

## License

MIT. See [LICENSE](LICENSE).
