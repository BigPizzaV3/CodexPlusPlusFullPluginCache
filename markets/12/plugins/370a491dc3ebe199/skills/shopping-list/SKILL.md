---
name: shopping-list
description: Add items to, read, or tick off a FamilyWell shopping list by its name.
---

To add items, call `shopping_list_shopping_lists` to find the list the user named (match by name, e.g. "Lidl"), then call `shopping_add_item` once per item with a short name and, if given, a quantity ("2", "1 kg"). If the user names no list and the family has several, ask which one.

If the response carries a `warning` that the item is already on the list, tell the user rather than adding it silently again.

To show a list, call `shopping_get_list`. To mark something bought, call `shopping_update_item`. Confirm in one sentence with the list name and what changed.
