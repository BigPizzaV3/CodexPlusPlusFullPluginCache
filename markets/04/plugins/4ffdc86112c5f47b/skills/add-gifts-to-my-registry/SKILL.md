---
name: add-gifts-to-my-registry
description: Use when a signed-in EasyRegistry owner wants to add gifts to their registry from product links, a shopping list, or a description (including cash-style gifts like a honeymoon fund), or to fix a gift's price, name or details, or remove a gift. Requires EasyRegistry sign-in. Not for buying or contributing to gifts.
---

# Add gifts to my registry

Use this when the user pastes product URLs, names items they want, or asks to change or remove a gift on a registry they own. The user must be signed in to EasyRegistry through the app's OAuth flow.

## Workflow

1. **Pick the registry.** Call `get_my_registries`. One registry: use it and name it. Several: ask which one. None: registries are created on the website; stop here.
2. **Check for duplicates first.** Call `get_my_registry_gifts` and compare against what the user wants to add. If an item already exists, say so and ask before adding another.
3. **Add from links.** For each product URL call `add_gift_by_url`. EasyRegistry fetches the page and reads the name, price and image where it can. Handle links one at a time and report per item: what was added and the price found. If a link cannot be read, fall back to step 4 for that item rather than retrying the same URL.
4. **Add by description.** For items without a link, or cash-style gifts (honeymoon fund, nursery fund, group gift), call `add_gift` with a clear name and an amount in the registry's currency. Ask for the amount if the user has not given one; do not invent prices.
5. **Correct and remove.** Use `update_gift` to fix a name, price, quantity or description on a gift the user has identified. Use `remove_gift` only when the user explicitly asks to remove a specific gift; confirm the gift name first. Both are safe to repeat: an unchanged update or an already-removed gift writes nothing.
6. **Summarise.** List what was added, updated or removed with prices, note anything that failed and why, and remind them the gifts appear on their public registry page.

## Boundaries

- Every write changes what guests see on the public page. For batches of more than five items, show the list and get a yes before adding.
- Never fabricate a price, brand or product name. If `add_gift_by_url` returns no price, tell the user and ask.
- Do not use `add_gift_by_url` on private, login-only or non-product pages; ask for the public product page instead.
- Never touch gifts on a registry the user has not selected in step 1.
- The app cannot purchase, reserve, contribute to, or mark a gift as bought. Guests do that on the public page.
- Never ask for card numbers, bank details or passwords.

## Output

A table or short list of gifts with action (added / updated / removed), price and any note, followed by the public page reminder.
