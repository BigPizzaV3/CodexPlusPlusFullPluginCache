---
name: mind-map
description: Draw a mind map from an outline or a list of topics and subtopics with generate_mind_map (SVG, PDF and OPML downloads, interactive map), and turn nested topics back into an indented or Markdown outline with outline_from_mind_map.
---

# Zovo Mind Map

Use `generate_mind_map` when the user wants a mind map, concept map, brainstorm map or topic tree.

1. Put the centre topic in `title`. Put the topics in `outline_text`, one per line, 2 spaces per level (a "- " bullet is optional), or pass nested `nodes` like `[{"text":"Marketing","children":[{"text":"Email"}]}]`. Give one of the two, not both.
2. Limits: 300 topics, 6 levels below the centre, 120 characters per topic. Split bigger maps into two.
3. `layout`: `balanced` (default, branches on both sides), `right-tree`, or `org-down` for an org chart look. `theme`: classic, ocean, forest or mono. `page_size`: auto (default), letter or a4 when the user wants to print one page.
4. If the request already lists the topics, call the tool right away. Turn "A (B, C)" into A with children B and C.
5. After the tool returns, give the topic count, the main branches, any notes word for word, and the SVG, PDF and OPML links. If the tool names a line with a problem, fix that line and call again.

Use `outline_from_mind_map` when the user wants the map as text: pass the centre topic as `title` and the topics as `nodes`; `format` is `indented` or `markdown`.

Do not use this skill for flowcharts with decisions, timelines, org charts with reporting data from a file, or for reading a picture of a mind map.
