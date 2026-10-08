---
name: list_asanas
description: List all 13 basic asanas by name, English translation, and category
---

## Trigger conditions
Use this tool when the user:
- Asks "what asanas are there?" or "show me the poses"
- Wants an overview before going into individual instructions
- Asks "which pose should I do for [category]?" — list first, then recommend
- Says "I want to see all the yoga poses"

## Task instructions
Call `list_asanas` with no arguments (or token if available).

Present the list clearly by number. Group or highlight by category if it helps the user navigate. After the list, invite the user to pick a number — then call `get_asana` with that id.

For premium users: note that 71 additional asanas are available.
For free users: note that all 13 are free, 71 more unlock with Premium.

## Example interaction
User: "What are the 13 basic asanas?"
→ Call `list_asanas` → show the numbered list → "Which one would you like full instructions for?"
