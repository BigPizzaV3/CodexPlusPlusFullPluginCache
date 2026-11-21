---
name: safe-bulk-edit
description: Make changes to many products, prices, stock levels, categories or coupons in a WooCommerce store safely. Use whenever the owner asks to raise or lower prices, change stock or status, tag or categorise products, create a discount code, or undo or schedule such a change.
---

Every Gridly change tool works in two steps. Never skip the first.

1. **Preview.** Call the tool (`update_products`, `create_coupon`, `update_order`, `apply_product_content`) WITHOUT `confirm`. Nothing changes yet. You get a `preview_id`.
2. **Show it.** Show the owner the preview plainly: how many items, the old and new values for the first few, and anything skipped. If the filter looks too broad (for example it includes products the owner did not mean), say so and offer to narrow it.
3. **Ask for a clear yes.** Only after the owner explicitly approves, call the same tool again with `confirm: true` and the `preview_id`.
4. **Report.** Say what was done and give the change number. Tell the owner they can say "undo change N".

Rules:
- Never invent a `preview_id`. Previews expire after 15 minutes; if one expired, run the preview again.
- To apply later instead of now, add `apply_at` (the store's local time, `YYYY-MM-DDTHH:MM`) to the confirm call. Use `list_scheduled_changes` and `cancel_scheduled_change` to manage them.
- To reverse a change, call `undo_change` with the change number and follow the same preview-then-confirm steps. Use `change_history` to find numbers.
- Refunds and payments cannot be made with Gridly. If asked, say so and point to WooCommerce itself.
