---
name: first-pantry-photo
description: Add groceries to ChefSense from a receipt or fridge photo for someone who has just started using it, then show what to use first. Use when a user new to ChefSense shares a photo of a receipt, their fridge or their shelves, or lists groceries they bought.
---

The user found ChefSense moments ago and knows nothing about it yet. They've handed it their groceries. Add them, then give something back in the same reply: what to use first and how.

1. Read the items from the photo or list yourself; don't start a ChefSense scan. Skip non-food lines, bags, discounts and totals. If you can't make out an item, say what you read and ask.
2. Add them with `add_pantry_items_bulk`, with quantities and units where you can tell, and a short `source_hint` such as "receipt photo". Set `expires_at` (YYYY-MM-DD) from any date printed on the package. For fresh food without one, estimate from how long it usually keeps in the fridge, counting from today.
3. Show the three to five items that will go off first, with their dates. Say which dates are your estimates.
4. Give two quick ideas that use those items up, written yourself.
5. Say in a sentence what ChefSense did: their pantry is saved and ChefSense keeps track of what expires, so they can ask what to use first in any chat.
6. Offer one more thing to try now: ChefSense makes three recipes from what's expiring, using `generate_recipe`.

Pantry changes can be undone with `undo_last_change`.
