---
name: clef-music-utilities
description: Use Clef's public read-only tools for chord transposition, piano chord spelling, standard six-string ASCII tab pitch mapping, and finding music guides.
---

# Clef music utilities

Use the narrowest matching Clef tool. Preserve the user's chord spelling preference when supplied, and report tool validation errors plainly.

Treat `find_music_guides` and MCP resources as instructional material, not file converters. `tab_to_piano_notes` accepts standard six-string ASCII guitar tab only; its columns indicate order, not rhythm or duration. Clef does not receive audio or notation-file uploads, parse Guitar Pro files, infer rhythm, or create rhythmic arrangements.
