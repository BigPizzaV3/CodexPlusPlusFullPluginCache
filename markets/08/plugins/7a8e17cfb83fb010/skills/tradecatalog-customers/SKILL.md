---
name: tradecatalog-customers
description: Add or maintain TradeCatalog customer accounts, invite purchasing colleagues, change buyer access or restrict an account to approved products. Use for supplier customer administration; pricing changes and buyer ordering have separate workflows.
---

# TradeCatalog customer accounts

Use the connected TradeCatalog MCP tools. Start with `list_workspaces` and the intended supplier's `get_workspace`, then resolve the account through `list_customers` and `get_customer`. Mutations use its exact returned `customerAccountId`. Customer administration needs `customers.manage` and write scope. Current permissions can limit staff to assigned customers or their regions; a missing account is not permission to probe IDs or switch identities.

## Set up or maintain an account

- **New trade account:** check for an existing account before `create_customer`. Supply `name`, a requested `accountCode` or omit it to generate one, and only the verified contact `email` the person wants to grant access. The contact can sign in for this account with that verified address; creation itself sends no invitation email. Use `invite_buyer` separately when an emailed invitation is requested. New accounts use Standard pricing; apply requested terms through the pricing workflow after creation completes.
- **Contact, name, active status or ordering:** read `get_customer` first. `update_customer` requires `name`, `discountBp` and `active`, so copy their current values unless they are part of the request. Preserve the current contact `email`: omission or an empty string clears it and removes access held through the previous address. If there is no contact address, omit the field; null is not accepted. Optional `legalName`, `notifyEmails`, `ordering`, `adjustment`, `priceListId`, `regionId` and `salesRepUserId` remain unchanged when omitted. Blank `legalName` clears it; an empty `notifyEmails` array removes update recipients. Do not change prices as a side effect of a contact edit.
- **Email updates without login:** `notifyEmails` is a list of up to 20 additional recipients for price changes and news. These addresses do not grant buyer access. Adding a purchasing colleague's login instead requires `invite_buyer`; establish which outcome the person wants.
- **Ordering exception:** `ordering: follow` follows the supplier switch, `prices_only` blocks basket changes and sending, and `can_order` permits ordering even if the supplier is prices only. Make only the requested account exception. `active: false` instead removes the account's buyer access; it is not a substitute for prices-only mode or deleting historical orders.
- **Region or sales rep:** use only verified existing IDs for `regionId` and `salesRepUserId`; null clears an assignment. The caller's customer scope still applies, and assigned-scope creation assigns the caller as rep. MCP does not list region choices or create regions. If the required choice cannot be resolved from current authorized records, finish it in the signed-in Customers or Team page rather than guessing an ID. Pricing changes also require `prices.edit`; use [tradecatalog-pricing](../tradecatalog-pricing/SKILL.md) for discounts, markups, agreed prices or list assignment.

For a supplied customer spreadsheet or bulk account update, use [tradecatalog-imports](../tradecatalog-imports/SKILL.md). Import rows can replace contact emails and whole-account percentages; do not fill absent source values with null just to satisfy the schema.

## Invite or remove a buyer

`get_customer` shows the contact address, `buyers` and `pending` invitations. Check those before preparing another invite. `invite_buyer` takes the exact account ID and recipient `email` and sends an invitation after review. Report an invitation as sent or pending, not as an accepted membership.

For removal, select the person's current `buyers[].id` as `membershipId` for `remove_buyer`, together with the account ID. A pending invitation ID is not a membership. If their address still equals the account's contact email, they can regain access on their next verified sign-in; explain that dependency and arrange the requested contact change before claiming lasting removal. After a completed contact change, re-read `get_customer`: changing the address can already remove the old contact's membership, so only call `remove_buyer` if it remains. Check pending invitations for that email as well; they can grant access again. MCP does not cancel pending invitations or create/reset supplier-managed username logins. Those actions finish in the signed-in customer account page, and an outstanding invitation must be cancelled there before claiming lasting removal. Do not ask for passwords in chat.

## Restrict what the account can see

Read `get_customer.account.catalogueScope` and `approved` first. Resolve product IDs with `search_products` and `get_product`, and category IDs with `get_catalogue_options`.

- `approve_products` adds exact `productIds` or the currently active products in a `categoryId` and its subcategories. It adds to the existing list; it neither replaces the list nor switches the account's scope. A category addition is a snapshot, not automatic approval of future products.
- `set_catalogue_scope` selects `all` or `approved`. When restricting a new account, prepare the intended approved list before switching to `approved`, so an empty list does not unintentionally hide everything. Existing hidden products and product-specific customer restrictions still apply; approval does not override them.
- `unapprove_product` removes one exact `productId` from the list. It limits buyers only while the account uses `approved` scope. Restoring scope to `all` retains the saved list and still respects product visibility.

## Review and verify

Show each returned confirmation card or signed-in `reviewUrl` for the exact account, recipients and access change. The person confirms there; typed approval in chat cannot replace it, and the agent must not call private `decide_action`. Check `get_action_status`, then reread `get_customer` after success. Stop on pending, failed or uncertain outcomes instead of replaying a write. Account access, invitation acceptance and catalogue scope are separate results: report only the states actually verified.
