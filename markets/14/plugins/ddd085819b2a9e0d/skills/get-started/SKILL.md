---
name: get-started
description: Help a ParkFlow manager finish setting up a parking property, one step at a time.
---

Help the manager get their ParkFlow property ready to run.

1. Call get_setup_checklist and say briefly what's done and what's left.
2. Suggest this order, but follow their lead if they want to do something else first:
   - Map the lot. If they share a site plan, blueprint or photo, build it in a few previews: add_lot_level for each floor, add_space_rows with every row and the labels shown, then draw_lot_features for drive lanes between facing rows, entrances and ramps. Fix what they point out before saving.
   - Add residents and give each one a space (add_resident, or import_residents for a list).
   - Set visitor parking prices with update_settings.
3. After each step, check get_setup_checklist again and mention what's still left.
4. Getting paid needs the owner to finish Stripe setup in the ParkFlow portal. Point them there; don't try to do it here.
