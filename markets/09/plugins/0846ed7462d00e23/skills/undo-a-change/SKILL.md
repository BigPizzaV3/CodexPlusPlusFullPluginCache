---
name: undo-a-change
description: Use when the seller wants to undo, revert, roll back, or restore a change made through ConnectMyShop (prices, deactivations).
---

1. Identify the change: ask for it or use the most recent executed request id from this chat; confirm it with `get_action_status`.
2. Call `propose_revert_action` with the `actionId` (and `listingIds` to undo only some listings).
3. Explain the result honestly: price changes restore exact previous prices after approval; deactivations are undone by reactivating (expired listings cost Etsy's renewal fee); published listings and new drafts cannot be reverted — offer deactivation or manual draft deletion instead.
4. Restores always need the seller's manual approval; say so.
