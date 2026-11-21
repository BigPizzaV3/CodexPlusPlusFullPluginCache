---
name: saved-work
description: Work with your private Shaupa saved products and boards, confirm removal, and read existing canvases.
---

Read current account limits when that tool is available. Use `shaupa_list_boards`,
`shaupa_get_board` and `shaupa_list_saved_products` to identify the person's actual
records. Respect `next_offset`; a page is not the entire collection. Do not guess
IDs or infer access to another person's account. Existing canvases can be listed
and read with `shaupa_list_canvases` and `shaupa_get_canvas`; editing or generating
canvases is not exposed.

For an explicit request, use `shaupa_create_board`, `shaupa_save_product` or
`shaupa_add_to_board`. Obtain product IDs from catalog results and option IDs from
the actual board. A save is intent-like, never a toggle. Supply a fresh UUID
`operation_id` for each new intended write, bound to its exact arguments.
Read `shaupa_get_operation_receipt` and ordinary record readback before claiming
completion. A completed receipt records the transaction acknowledgement; it does
not guarantee that later changes have not altered the record.

`shaupa_remove_saved_product` prepares an exact removal preview. Give the person
the returned Shaupa confirmation link. They sign in and confirm or keep the
item. Never approve that page for them or describe a pending operation as done.
Read the same operation receipt afterward. Cancellation and expiration do not
remove the item.

If transport fails or a receipt says `executing` or `unknown`, inspect that same
operation. Never escape uncertainty with another UUID, changed arguments or a
repeat write. Return an unresolved outcome honestly. If the person changes their
intent, first resolve the original operation before starting another action.
Account limits and ownership come from canonical services. No digital upsells,
new subscriptions, sharing, social publication or bulk deletion are exposed.
