---
name: gift-list
description: Make a hosted wishlist that friends and family claim gifts from without spoiling the surprise, and manage it, using create_gift_list, show_gift_list_status and update_gift_list.
---

# Zovo Gift List

Use `create_gift_list` when someone wants a wishlist, gift list or registry that other people can claim gifts from (birthday, Christmas or another holiday, baby shower, wedding).

1. Pass a `title` and the `items`. Each item has a `name` and optional `note` (size, colour), `price` (text such as "$20-30"), `store` (a store name, never a link) and `quantity` (1-20).
2. Claims are hidden from the owner by default. Set `show_claims_to_owner: true` only when the user says they want to see who is getting what.
3. Add `owner_name`, `occasion_date` (YYYY-MM-DD) and a short `note` when given. The page stays open until 3 weeks after `occasion_date` (at least 30 days and at most one year from today); tell the user the end date from the result. Links are not allowed anywhere; if the user gives a shop link, use the store name instead.
4. If the request already lists items, call the tool right away.

After the tool returns, give the shared link (for friends and family) and the owner link (keep private) separately. When claims are hidden, never guess or state which items were claimed.

Use `show_gift_list_status` with the owner link (it contains `/m/`) when the owner asks how the list is going.

Use `update_gift_list` with the owner link to add or remove items, change quantities, show or hide claims, rename the list, or close or reopen it.

Do not use this skill for gift ideas, buying or price tracking, or Secret Santa draws.
