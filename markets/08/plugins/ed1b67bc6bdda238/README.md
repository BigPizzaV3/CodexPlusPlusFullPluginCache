# Tana plugin

## What this is

Tana turns every meeting into a transcript, screen-share screenshots and tasks. Tana captures what was shared on screen, so the agent sees the bug, the sketch or the slide people were talking about, not just the words. This plugin lets Claude and ChatGPT (and coding agents like Claude Code, Codex and Cursor) read and use all of it. It installs the Tana MCP connector plus nine skills that know how to find a meeting, read everything in it, and act on what was decided. One repository installs into Claude Code, claude.ai and Claude Desktop, ChatGPT and Codex, and Cursor.

## Install

The first time you use it, you sign in to Tana once. Every write is a proposal you approve in Tana.

### Claude (desktop and web)

Settings → **Plugins** → **Add** → from GitHub → `tanainc/tana-plugin`. Then open the plugin's **Connectors** tab and press **Connect** to sign in to Tana.

Connector only, without the skills: Settings → **Connectors** → **Add custom connector** → `https://home.tana.inc/mcp`.

### ChatGPT (desktop and web)

Search for **Tana** in ChatGPT's apps once it is listed and press **Connect**. Until then: Settings → **Connectors** → Developer mode → add `https://home.tana.inc/mcp` (connector only; the skills arrive with the listing).

### Claude Code

```
claude plugin marketplace add tanainc/tana-plugin
claude plugin install tana@tana
```

### Codex

```
codex plugin marketplace add tanainc/tana-plugin
codex plugin add tana@tana
```

### Cursor

Open this link to install the connector:

cursor://anysphere.cursor-deeplink/mcp/install?name=tana&config=eyJ1cmwiOiJodHRwczovL2hvbWUudGFuYS5pbmMvbWNwIn0=

### Any other agent

```
npx skills add https://github.com/tanainc/tana-plugin
```

## Skills

| Skill | What it does |
| --- | --- |
| tana-meeting | Find a meeting and read all of it: transcript, every screen-share screenshot, attendees, artifacts, suggestions |
| prep-meeting | Brief for an upcoming meeting from past meetings with the same people |
| create-from-meeting | Make a brief, slides, storyboard or recap from a meeting |
| ask-tana | Quick cited answers: what did we decide, when did we discuss |
| find-prior-art | Has anyone discussed this before? Feedback, bugs, decisions, with links |
| add-to-meeting | Add links, agenda items, docs or bugs to a meeting |
| schedule-meeting | Create a meeting with attendees and an agenda |
| do-my-tasks | Do what's assigned to you in Tana, propose the rest back |
| implement-from-meeting | Turn what was discussed (and shown on screen) into a spec, then build it (coding agents) |

## What data it sends

The plugin only asks Tana for what your prompt needs, and only from the Tana organisation you connected. Nothing is uploaded in the background. Every write is a proposal: you approve it in Tana before anything changes.

## Links

- Docs: https://tana.inc/learn/guides/use-tana-with-claude
- Privacy policy: https://tana.inc/privacy
- Support: support@tana.inc

## License

MIT. See [LICENSE](LICENSE).
