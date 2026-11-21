# Connecting a client to a Écran Papier frame

Two remote MCP servers, both Streamable HTTP, **no authentication**:

| Server | URL | Tools |
|---|---|---|
| The frame | `https://mcp.ecranpapier.com/<id>` | `get_state`, `push_content`, `set_service`… |
| The shop (optional) | `https://ecranpapier.com/api/shop/mcp` | `list_products`, `get_product` |

`<id>` (the frame's unique identifier) comes from the frame's link `https://app.ecranpapier.com/w/<id>`. One connector
per frame: a household with two frames adds two.

Choose "no authentication" when offered. If the client requires OAuth
("sign in"), that works too: a Écran Papier page asks the user to allow, with no
account, and the token changes nothing about access. If a form insists on a
client id, secret, username or API key, any value works: the server reads
none of them and never answers 401.

Menu names move between releases; if a label below differs, look for
"Connectors", "Apps" or "MCP servers" in the settings.

## Claude (claude.ai, desktop and mobile apps)
- Connector: Settings → Connectors → Add custom connector → paste the URL.
  Then enable it in the conversation's tools menu.
- This skill: Settings → Capabilities → Skills → upload the zip (code
  execution must be on, it runs `compose.py`).
- Code execution has no network by default, so `compose.py --upload` fails
  there: use `--base64` and `push_content` `image_base64`. If the owner adds
  `app.ecranpapier.com` to the allowed domains in the code-execution
  settings, `--upload` works.

## Claude Code
```
claude mcp add --transport http wignet https://mcp.ecranpapier.com/<id>
claude mcp add --transport http wignet-shop https://ecranpapier.com/api/shop/mcp
```
Skill: unzip into `~/.claude/skills/` (all projects) or `.claude/skills/`
(one project), so that `~/.claude/skills/wignet/SKILL.md` exists. Claude
Code has network access: `compose.py --upload` is the simplest route.

## ChatGPT

The Écran Papier plugin bundles the shared MCP connection and the skills.
Once published in the ChatGPT plugin directory, the owner's path is:

1. Add **Écran Papier** in ChatGPT and run its setup.
2. Paste the personal screen-page link opened by the screen's QR code.
3. Ask for a message, a photo or a service in ordinary language.

The assistant passes that link as `device` on screen tools. One plugin can
control several screens supplied by the owner. Setup checks the state without
changing the display. The link grants control; keep it private. In a new
conversation, supply it again if the assistant no longer has it.

Before publication, test using ChatGPT's **Add custom MCP server** with
`https://mcp.ecranpapier.com/` (Streamable HTTP, **no authentication**). Account and workspace
permissions may affect availability. A local ZIP is a publisher/test artifact,
not a public directory listing. See https://ecranpapier.com/support.html for the current setup
instructions. An existing custom GPT can use the separate Actions kit at
`https://ecranpapier.com/skills/chatgpt-gpt.md`.

A file from the conversation (attached photo or generated image) goes through
`push_content` with `image_file`: ChatGPT supplies the file object and the
platform downloads it. Use this before base64. Without file transfer support,
use `image_base64` as described in the main skill.

## Codex (CLI / IDE)
- Skill: unzip into `~/.codex/skills/` so that `~/.codex/skills/wignet/SKILL.md` exists.
- MCP: add the server to `~/.codex/config.toml`:
  ```toml
  [mcp_servers.wignet]
  url = "https://mcp.ecranpapier.com/<id>"
  ```
  or use plain HTTP from the shell (OpenAPI below).

## Anything else (n8n, scripts, other agents)
- OpenAPI 3.1 for one frame: `https://app.ecranpapier.com/api/owner/<id>/openapi.json`
- Same API for any frame (`device_id` as a parameter): `https://app.ecranpapier.com/api/owner/openapi.json`
- Guide in Markdown: `https://app.ecranpapier.com/api/owner/<id>/guide`
- Push a file: `curl -F file=@image.png https://app.ecranpapier.com/api/owner/<id>/image`
