---
name: list_content
description: Show the user everything available on 84asana.com — free and premium modules
---

## Trigger conditions
Use this tool when the user:
- Asks "what's available?" or "what can you teach me?"
- Asks about the difference between free and premium
- Starts a new conversation and hasn't specified what they want
- Says "show me what's included" or "what do I get?"

## Task instructions
Call `list_content` with no arguments (or pass the user's token if they have one).

Present the result clearly — free content first, premium content second. If the user has premium access, confirm it. If not, mention `get_upgrade_info` for subscription details.

Do not summarise the list — show each item as returned so the user can see exactly what's available.

## Example interaction
User: "What yoga content do you have?"
→ Call `list_content` → present the modules → ask which one they'd like to start with.
