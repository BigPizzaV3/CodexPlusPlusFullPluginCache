---
name: menu-update
description: Change a connected restaurant's menu — prices, descriptions, on/off, sold out today — always by showing the exact change first and applying only after the owner says yes.
---

1. Find the items with `get_restaurant_menu` (search by name). If several match, ask which.
2. Call `preview_menu_change` with the changes. Show the owner every row of `will_change` (old → new), every `blocked` item with its reason (usually: managed in KitchenHub — change it there), and the warnings.
3. Ask for a clear yes. Only then call `apply_menu_change` with the `change_id`.
4. If apply says the menu changed since the preview, preview again and re-confirm — never retry blindly.
5. "Sold out" with `"today"` lasts until midnight in the restaurant's time zone and covers ServeStack ordering (website, ChatGPT), not delivery apps.
6. Never invent prices; use the owner's numbers.
