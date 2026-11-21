---
name: stock-the-pantry
description: Add groceries to the user's ChefSense pantry from a list, a receipt photo or a shelf photo, and check bought items off their shopping list. Use when the user has been shopping or wants to add groceries, a receipt or a photo of their shelves to their pantry.
---

Get what the user just bought into their pantry with as little typing as possible.

1. Work out the source:
   - **A typed or spoken list:** use it directly.
   - **A photo you can read** (receipt or shelf): read the items yourself. Skip non-food lines, deposits, bags and totals. Expand receipt abbreviations where you're confident, and mark the ones you're unsure of.
   - **The user wants ChefSense to read the photo:** use `start_pantry_scan` (`kind: "receipt"` or `"shelf"`), poll `get_pantry_scan` every few seconds until it's `ready_for_review`, then show the detections. Scans count toward their monthly ChefSense scans, so only do this when they ask for it.
2. Show the items you'll add, with quantities, units and any expiry dates you can infer for fresh food. Ask before adding.
3. Add them:
   - Items you read or were given: `add_pantry_items_bulk`. Pass `confidence_hints` for items you weren't sure of, so they're flagged for review, and a short `source_hint` such as "receipt photo".
   - A ChefSense scan: `apply_pantry_scan`, with `reject_detection_ids` for anything the user didn't want.
4. Report what was added, merged into existing items, or skipped and why.
5. Call `list_shopping_list`. If any bought items are on it, offer to check them off with `check_shopping_list_items`.

Pantry changes can be undone with `undo_last_change`; shopping list changes can't.
