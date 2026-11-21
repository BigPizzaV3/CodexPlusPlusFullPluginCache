---
name: festival-and-greeting-kit
description: Put together HubToolify stickers, illustrations and icons for a festival, holiday or occasion, such as Diwali, Eid, Christmas, a birthday, a wedding or a thank-you. Use when the user wants visuals to greet someone, decorate a post or message, or plan festive designs.
---

# Festival and greeting kit

Explicit instructions from the user always come first. If they ask for only stickers, or only one item, do just that.

## Workflow

1. **Name the occasion** and, if the user said so, where the visuals will be used (a chat message, a social post, a card, a website banner).
2. **Stickers first.** Call `search_stickers` with the occasion as `query` (for example "happy diwali"). If the user wants motion for a chat or story, set `animated` to true.
3. **Then illustrations** for larger designs (posts, banners, cards): call `search_illustrations` with the occasion as `query`. If nothing matches, try a broader word (for example "celebration", "gift" or "family").
4. **Optionally icons** for small decorations or a website: `search_icons` with the occasion or its symbols (for example "diya", "lantern", "gift").
5. **Summarise** what was found in a few lines: the best 3–5 stickers and the best illustrations by name, and which one suits which use.
6. **Downloads when asked:** `get_sticker`, `get_illustration` or `get_icon` with the exact names from the searches.

## Rules

- Use only names the search tools returned. If an occasion has no match, say so and offer the closest general results; never invent a sticker or scene.
- Some downloads depend on what the connected HubToolify account includes. When a result says something is not included, say so plainly and keep showing the previews. Do not mention prices.
- Be respectful with religious festivals: describe the visuals neutrally and do not add religious claims of your own.
