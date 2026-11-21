# Igly Canvas plugin

Pick from 5,000+ free design templates, 1,100+ animations and video templates that render to a free MP4, or draw on an editable [Igly](https://igly.ai) canvas from Claude, ChatGPT and Codex: menus, posters and social posts from templates, launch videos and logo intros as MP4s, animations you can make your own, plus flowcharts, mind maps, roadmaps, kanban and retro boards, wireframes, storyboards and moodboards.

The board shows up right in the chat. Move, retype and draw on it by hand, export a PNG, or open it in the full Igly editor. Every board is a project in your Igly account, so you can paste a project link later and keep editing it from the chat. Free with an Igly account: you sign in once when you add the connector.

## What's inside

- **MCP server** `https://igly.ai/api/mcp` (Streamable HTTP, OAuth sign-in with your Igly account) with tools to browse the Igly library (design templates, video templates and animations in one picker in the chat, with categories), fill in and render a video template to an MP4, get an animation prompt, list your Igly projects, create a canvas (saved as a project in your account), apply a template beside an existing board, add / update / duplicate / remove elements (including dashed outlines, curved lines and images from a link or attached in the chat; every style you can set on a new element can be changed later, fonts included, and a template photo can be swapped), rename a project or resize its page, search the font list, arrange and export PNG. Configured in `.mcp.json` (Claude) and `mcp.json` (portable / OpenAI).
- **Skills** in `skills/`:

| Skill | Use it for |
|---|---|
| `flowchart` | processes, user flows, decision trees, system diagrams |
| `mind-map` | brainstorms and topic maps |
| `roadmap-timeline` | roadmaps, release plans, timelines |
| `kanban-retro` | kanban, retros, SWOT, affinity maps |
| `wireframe` | page and app screen wireframes |
| `storyboard` | video, ad and slide storyboards |
| `moodboard` | style directions, palettes, type pairings |
| `template-design` | posters, social posts, menus, invitations from templates |
| `video-template` | launch videos, promos, logo intros and slideshows rendered to an MP4 |
| `animation` | logo reveals, launch films, kinetic type and other animations built in the chat |

## Install

**Claude Code**

```bash
claude plugin marketplace add Whatscheap/igly-canvas-plugin
claude plugin install igly-canvas@igly
```

**Claude (web / desktop)**: Settings → Connectors → Add custom connector → `https://igly.ai/api/mcp`.

**ChatGPT**: Settings → Plugins → Add → custom MCP server → `https://igly.ai/api/mcp`.

**Codex**: `codex plugin marketplace add Whatscheap/igly-canvas-plugin`.

## Try

- "Draw a flowchart of our customer onboarding"
- "Make a mind map for a podcast launch"
- "Turn these notes into a Q1 to Q4 roadmap"
- "Sketch a wireframe for a pricing page"
- "Make an Instagram post for our bakery's summer menu from a template"
- "Make a launch video for my app Lumen from a video template"

## Privacy

Boards are projects in your own Igly account, visible only to you. See [igly.ai/legal/privacy](https://igly.ai/legal/privacy).

## License

MIT
