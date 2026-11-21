# Vibrant Design

Design inspiration and references, right where you build. Ask your agent what's new or trending in web design, for motion and interaction ideas (hover, scroll, drag, micro-interactions), launch videos or OG images, and it browses the curated vibrant.design gallery for you, shown as cards with the cover, the creator, a link to the design on vibrant.design and the live site.

When you build a landing page or a section (hero, features, pricing, testimonials, CTA, footer), Vibrant suggests designs that fit your product and style. You pick one per section, and the agent builds it from that design's DESIGN.md and build notes, in your own stack and with your own copy.

Works in Claude (claude.ai, desktop, Cowork, Claude Code), ChatGPT and Codex, Cursor, Grok, and Google Antigravity.

## Use it

Connect once, then ask in plain words:

- "What's trending on Vibrant this week?"
- "Show me scroll animation ideas for a SaaS homepage."
- "This week's Vibrant picks, websites only."
- "Launch video inspiration for a dev tool."
- "Build a hero for my AI note-taking app. Show me Vibrant options first."
- "Plan a dark, minimal landing page for this developer tool from Vibrant references."
- "Redesign our pricing section like a Vibrant design I pick."
- "Implement my Vibrant moodboard in this project."
- "Build this section like https://vibrant.design/p/…"

| Skill | What it does |
| --- | --- |
| `design-inspiration` | Latest, trending, popular, featured and the weekly newsletter picks, across websites, sections, UI shots, motion, launch videos and OG images, by style, category or interaction. |
| `build-section` | Suggests references for one section, lets you pick, then builds it. |
| `build-landing-page` | Suggests an overall look plus options per section; builds straight from your picks, or first turns them into a moodboard and one design direction. |
| `implement-moodboard` | Installs a board's DESIGN.md, settles open conflicts with you, and builds page by page. |
| `use-gallery-design` | Brings one gallery design's DESIGN.md and build notes into the repo. |

Every design credits its creator and links back to the original. Browsing, inspiration and suggestions are free. DESIGN.md files, build notes and the design-direction build need a Vibrant plan; the agent always tells you the credit cost and asks before anything is charged. Plans: https://vibrant.design/pricing

The agent takes layout, rhythm, type, color and motion ideas from references. It never copies their text, logos or images, and never makes a 1:1 clone.

## Data

The plugin connects to the Vibrant MCP server at `https://vibrant.design/mcp` and signs in with your Vibrant account (OAuth). It sends your search terms, brief, section choices and board edits to Vibrant, and reads designs, boards and DESIGN.md files back. It does not read or upload your code. The plugin stores nothing itself. Privacy policy: https://vibrant.design/privacy · Terms: https://vibrant.design/terms · Support: https://vibrant.design/support

## Layout

One folder serves every host:

| File | Host |
| --- | --- |
| `.claude-plugin/plugin.json`, `.claude-plugin/marketplace.json`, `.mcp.json` | Claude, Grok Build |
| `plugin.json`, `mcp.json` (Agent Plugins standard) | ChatGPT and Codex, Cursor |
| `.antigravity-plugin/plugin.json`, `mcp_config.json`, `rules/` | Google Antigravity |
| `skills/` | Shared by all hosts |

Without the plugin, any MCP client can connect to `https://vibrant.design/mcp` directly. Setup for each client is at https://vibrant.design/dashboard/agents.
