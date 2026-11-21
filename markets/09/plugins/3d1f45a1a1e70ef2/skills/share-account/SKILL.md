---
name: share-account
description: Share a CreceRank brand, review who has access, and read the plan or invoices. Use when the user asks to invite a teammate, remove access, check the trial, or see billing history.
---

Use this skill for sharing and account status.

If the user gives a different instruction, follow that instruction.

1. Call `crecerank_whoami` before sharing or explaining the plan.
2. Call `crecerank_list_brands` and use the owned brand id they name.
3. Call `crecerank_list_brand_members` to show current access.
4. Call `crecerank_create_share_invite` with `role` `co_owner` or `viewer`. Pass `notify_email` only when they want the invite emailed. The invite is accepted in the browser, not by a tool.
5. Call `crecerank_get_share_log` when they ask who was invited. Pass `limit` when they want a shorter list.
6. Call `crecerank_revoke_brand_member` only after they name the member and confirm removal. It requires `mcp.destructive` and cannot remove the owner.
7. For the plan or trial end, call `crecerank_get_subscription`. For receipts, call `crecerank_list_invoices`. Both are read-only. To pay or change the plan, send them to the CreceRank billing page. Do not collect payment details.

Do not delete the user account. That is not a tool.
