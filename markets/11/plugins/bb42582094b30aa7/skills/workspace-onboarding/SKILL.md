---
name: workspace-onboarding
description: Use when someone first opens FamilySimpl or asks how its interactive family workspace, research forms, evidence and reviewed changes work.
---

# Start with FamilySimpl

After a family-tree summary, “Show me some of it”, “show it” and “show me some of the main one” request a compact connected coloured diagram. Reuse established tree/reference IDs, normally direction:"ancestors", generations:2, limit:15. The user need not ask for colours or HTML. Both grandparents connect above their actual child; preserve full recorded dates.

For static diagrams, when the host has a **visible code-execution image-output tool**, use show_tree and emit each exact returned inlineDiagram SVG through that image channel. In visible Python rasterize unchanged SVG with CairoSVG at2x width/height, then display PNG bytes with IPython.display.Image at the logical panel width. Transfer the original SVG into that environment instead of referring to an inaccessible old file. This avoids the MCP Apps loading container. The tree must be visibly rendered, not a Library/download attachment card, file link or HTML/Visualize iframe. Do not manually reconstruct the layout or use image generation. See family-history for the exact rendering recipe.

Check the tool contract first: a background shell/command/container, installed Python/CairoSVG, IPython display import, saved PNG or subagent preview does not display an image to the user. If that is all the host provides, skip rasterization and call render_family_diagram directly. Never claim a successful command displayed a tree.

If visible image output is unavailable or the user requests the compact app's branch selector, use render_family_diagram with the same scope/options. Its prepared receipt is not proof of display. Interactive search, clickable profiles, pan/zoom and stateful review use open_family_workspace. Summary/research answers remain conversational, with no automatic app.

FamilySimpl requires an authorized account. Use list_trees to resolve accessible trees; disambiguate duplicate names by immutable ID. Never request passwords/security codes in chat. Keep ordinary answers concise with useful figures, citations and canonical website links when useful. No extra genealogy reads solely for decoration.

Both diagram tools support ancestors, descendants, neighbourhood including partners/siblings, and connection with a targetPersonId. Five ancestral generations uses direction ancestors, generations5 and limit100. Preserve all panels, full dates and typed parent/peer links. A connection is one shortest recorded route within the step bound, not proof or necessarily strongest evidence; use get_connection separately. Do not invent not-loaded ancestors or shorten1910-10-26 to1910. Never use ASCII/box-drawing/indented text trees unless explicitly requested. Neutral surfaces and compact blue/purple cards are the default, not an all-green theme. Identity, connection evidence and research coverage remain separate assessments.

The interactive workspace offers search at the top, clickable profiles, Tree and People views; research, evidence and reviewed edits are under More tools. It is a bounded privacy-filtered view, not an iframe of the full website. Opening it does not change records.

The AI view filters under-13 and uncertain-age profiles, private narratives, original imports, photos and member details. It is a permitted subset of the website. Do not promise to retrieve excluded content through another tool.

Choose **Prepare research** to select an eligible person, research area, question and shared evidence. Capable hosts provide a native form; other hosts use the workspace form. Previews contain explicitly shared source summaries. A picker does not upload a file. Preparation and cancellation do not save family records. A prepared packet becomes a conversation draft or message only when the user chooses that action.

View controls change presentation. A visible answer prompt names the allowed candidates; send only their exact IDs after the user's explicit selection. Context thumbnails use generated initials and eligible selected names, not family photos.

Use Research to inspect shared notes and reservations before duplicating work. Preserve unsuccessful searches, unresolved disagreements, tentative claims and sources separately from canonical facts. Use the family-history skill for the full research and write workflow.

Edits begin as local drafts. Review the before and after values, then apply the requested change or submit a contributor proposal. Use the current revision and an operation ID. A receipt confirms the result; retry an uncertain write with the same ID rather than creating another operation. Viewers cannot edit.

Files exports the visible filtered branch or a prepared research document. Opening a file does not authorize tree edits. Saving an opened writable host file checks its version and refuses conflicting overwrites. Explain host-dependent fallbacks for files, drafts, sampling and expanded views.

For a presentation follow-up, re-render the same scope with highlightPersonIds, up to four named highlightGroups, or highlight rules for identityStatuses, connectionStates, researchBelow or conflicts. Multiple rules match ANY (OR); researchBelow is strict. dimOthers de-emphasizes context without removing people. colourBy selects branch (default blue/purple), identity, connection or research coverage independently of attention outlines. Highlights never alter facts or certainty, expand access, or reveal protected profiles. Resolve names only when needed, reuse known IDs and avoid per-person reads for rule styling. Report no matches/off-view people briefly. See the family-history skill's diagram examples for concrete combinations and limits.

Preserve all recorded dates and actual typed links in every prepared panel. Do not claim full coverage when complete is false, limitReached is true, or a deeper scope was not read. If the host cannot display a component, use the exact-SVG visible image route when available; otherwise explain the limitation honestly. Never substitute text art without an explicit request.
