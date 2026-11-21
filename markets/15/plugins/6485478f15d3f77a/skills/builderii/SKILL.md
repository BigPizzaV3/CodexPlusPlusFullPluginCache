---
name: builderii
description: Work in the user's Builderii boards (app screens and clickable prototypes, flowcharts, mind maps, sequence diagrams, sitemaps, brainstorms, roadmaps, database diagrams and docs) through the Builderii connector. Use whenever the user mentions Builderii or one of their boards, flows, wireframes, screens or sticky notes, or asks to draw, design, map or change something on a board.
---

# Working in Builderii

Builderii is the user's visual workspace: boards with app screens (wireframes and clickable prototypes), flowcharts, mind maps, sequence diagrams, sitemaps, brainstorms (sticky notes), roadmaps, database diagrams and docs. The Builderii connector acts as the user, with their access: their own boards, boards shared with them and their teams' boards.

## Which tool

| To… | Use |
| --- | --- |
| Find a board | `search` (name and content) or `list_boards` (newest first; filter by `query`, `kind`, `folderId`) |
| See what's on a board | `read_board`: each page's diagrams (with refs) and a text outline; `format: "json"` gives one page's elements with ids |
| Start something new | `create_board` (`name`, `kind`, or a `template` from `list_templates`); `add_page` for another page |
| Draw something you've worked out | `create_app_screens`, `create_flowchart`, `create_mindmap`, `create_sequence_diagram`, `create_sitemap`, `create_brainstorm`, `create_roadmap`, `create_database` (or SQL in `sql`), `import_mermaid` |
| Change a diagram | `list_diagrams` → `get_diagram` (its ids) → the matching `update_*` with the diagram's `ref` |
| Make a prototype clickable | `link_screens` (what's tapped on which screen opens which screen; the start screen) |
| Let Builderii's own AI do it | `generate` (any diagram kind from a prompt, a screenshot via `image_url`, or a change to one with `diagram`), `expand_ideas`, `cluster_stickies`, `summarize_board`, `rewrite_text`, `screen_to_code`, `write_spec`, `apply_brand`; `get_ai_job` when one is still working |
| Give feedback | `add_comment`, pinned beside the element whose text matches `on` |

## Habits

- **Find before you make.** If the user names a board, find it (`search` or `list_boards`) and use it; only `create_board` when they want a new one or none matches.
- **Draw it yourself when you know what to draw.** The `create_*` tools take the structure (steps and arrows, screens and components, a tree of ideas); Builderii lays it out. Use `generate` when the user wants Builderii's AI, when they send a screenshot, or for a quick first draft. Builderii's AI counts against the user's monthly AI requests.
- **Change, don't redraw.** To change a diagram that's on the board, read it with `get_diagram` and send only the changes with its `update_*` tool (sequence diagrams, sitemaps, roadmaps and database diagrams take the whole diagram back, keeping ids). Never draw a second copy.
- **AI jobs finish on their own.** If `generate` (or another AI tool) answers `working`, call `get_ai_job` with its `jobId` after a moment; the result lands on the board either way.
- **Link what you make.** Every result has the board's `url`; give it to the user so they can open the board.
- **Keep the user's words.** Use real names, labels and content; don't invent facts the user didn't give.
- **Respect access.** Boards shared view-only or comment-only can't be changed; if a tool says so, tell the user.
- **Not connected?** If a tool asks to connect Builderii or fails to authorize, ask the user to connect (or reconnect) the Builderii connector and approve it.
