---
name: check-chapter-consistency
description: Check one chapter of a Musael manuscript against its World, timeline and style report, quoting each problem and changing nothing. Use when the writer asks to review a chapter for continuity, consistency, names, dates or style. Needs manuscript access on the writer's Musael account.
---

# Check a chapter's consistency

The writer's own instructions come first: if they ask only for names, or only for the style report, do only that.

## When to use

The writer asks for a continuity or consistency pass on a chapter of their Musael project: wrong eye colours, a character in two places, dates that do not add up, names spelled two ways, a scene told out of order without meaning to be.

## Steps

1. Find the project with `list_projects` and the chapter number with `get_outline`.
2. Read the chapter with `read_chapter`.
3. Compare it with the World: `list_world` for the names, then `get_world_entry` for each character or place that matters in the chapter. Check names and other names, descriptions, relationships and recorded facts.
4. Compare it with the story's order of events with `get_timeline`.
5. If the writer asked about style, run `get_style_report` on the scenes they named.
6. Report what you found, most important first. For each finding quote the exact words, say which scene they are in, and say what they contradict (the World entry, the fact, the event). Separate clear contradictions from things that only might be wrong.
7. Offer fixes. Only if the writer asks, call `suggest_edit` for a specific passage: it files a suggestion they accept or reject in Musael and changes nothing by itself.

## Rules

- Change nothing without being asked. Never rewrite whole passages.
- The style report is fixed rules, not judgement: none of its findings is a mistake by itself.
- If a tool answers that reading the manuscript is not included in the writer's account, tell the writer that and stop; do not try to work around it.
