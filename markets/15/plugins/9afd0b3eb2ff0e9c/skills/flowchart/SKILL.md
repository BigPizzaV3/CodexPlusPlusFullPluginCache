---
name: flowchart
description: Draw a laid-out flowchart from steps and decisions, or from Mermaid flowchart text, with the generate_flowchart tool, and return SVG, PDF and Mermaid downloads plus layout and process checks.
---

# Zovo Flowchart

Use `generate_flowchart` when the user wants a flowchart, process diagram, decision tree or workflow chart.

1. If the user lists steps in prose, turn them into `text` with one arrow per line: `Start -> Receive order`, `In stock? -> Ship order: yes`. A question mark at the end makes a decision. Use `Start` and `End` as the first and last steps when the user has no names for them.
2. If the user pastes Mermaid flowchart text, pass it as `text` unchanged.
3. For structured data, pass `nodes` (`id`, `text`, `shape`: start, end, process, decision, input, document) and `edges` (`from`, `to`, `label`) instead of `text`. Do not send both.
4. Set `direction` to `left-right` for wide, short processes; `top-down` is the default. Set `page_size` to `letter` or `a4` only when the user wants a one-page PDF.
5. After the tool returns, give the download links, the layout checks (overlapping boxes, edge crossings), and the warnings in plain words, such as unreachable steps or a decision with one branch. Offer to fix the process if a warning shows a gap.

Limits are 150 nodes, 300 edges, 120 characters per box and 40 per edge label. Do not use this skill for org charts, mind maps, swimlanes, sequence diagrams or charts of numbers.
