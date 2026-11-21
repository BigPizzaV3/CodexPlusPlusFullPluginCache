---
name: retro-yearbook-photos
description: Put AI retro yearbook photos (1970s, 1980s, 1990s or 2000s portraits that ChatGPT makes from a photo the user shares) into a Yearbind group yearbook under each person's name. Use when someone asks for a 90s yearbook photo, an AI yearbook portrait or a throwback look for themselves or a member of their yearbook group.
---

Use this skill when the user wants era yearbook portraits in their group yearbook. The user's explicit instructions always come first.

## Flow

1. The user shares a photo of a person who agreed to be in the yearbook and names the era. ChatGPT's own image tools make the retro portrait.
2. `add_portrait` adds that portrait to the yearbook under the person's name. A new name becomes a member; a member who already has a portrait keeps it, and the new one is saved as an option the organizer can pick in the card.
3. `get_book` shows which members have a portrait and which still need one; `preview_book` shows how the pages look with them.

## Scope

- Portraits are only of people who agreed to be in the yearbook.
- Yearbind stores the finished portrait; it makes no images itself.
- If the user has no yearbook yet, start one with the group-yearbook skill.
