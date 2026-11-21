---
name: diagram
description: Draw a diagram in Builderii, such as a flowchart of a process, a mind map of a topic, a sequence diagram of a system, a sitemap, a roadmap or a database diagram, from a description, this conversation, code or SQL, or change one already on a board. Use when the user asks to map, chart, diagram, visualise or plan something in Builderii.
---

# Draw a diagram in Builderii

1. **Pick the kind.** A process or decision → flowchart (`create_flowchart`). Ideas around a topic → mind map (`create_mindmap`). Who calls whom, in order → sequence diagram (`create_sequence_diagram`). Pages of a site → sitemap (`create_sitemap`). Work over time → roadmap (`create_roadmap`, real dates). Tables and keys → database diagram (`create_database`, or paste SQL / a Prisma schema in `sql`). Mermaid you already have → `import_mermaid`.
2. **Which board.** Use the board the user named; otherwise `create_board` with a specific name (kind `flowchart` or `mindmap` where it fits).
3. **Write the structure.** Short labels in the user's words. Flowcharts: a start and an end, decisions with labelled arrows (yes / no), 5 to 20 steps. Mind maps: one central idea (parent `""`), 4 to 7 branches, 2 to 4 ideas each. Sequence diagrams: participants in order, then messages (`sync`, `async`, `reply`). Builderii lays everything out, so give no coordinates.
4. **Changing one that's there:** `list_diagrams`, then `get_diagram` for its ids, then the matching `update_*` with its `ref` — only the changes for flowcharts, mind maps and brainstorms; the whole diagram (keeping ids) for sequence diagrams, sitemaps, roadmaps and database diagrams. Don't draw a second copy.
5. **Or let Builderii's AI draw it:** `generate` with the `type` and a prompt (pass `diagram` to change one). If it answers `working`, call `get_ai_job` shortly after.
6. **Confirm** in a line or two what you drew, with the board's link.
