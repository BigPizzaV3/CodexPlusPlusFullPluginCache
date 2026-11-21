---
name: goodsend-workflows
description: Use for Goodsend profiles, Circle members, collections, wishlists, saved items, owned items, gift ideas, reservations, or goodsend.it links.
---

# Goodsend workflows

Use Goodsend as the source of truth for a connected account's saved products,
collections, wishlists, Circle, and visible profiles.

## Present the final result

- When the request resolves to exactly one profile, collection, wishlist, or
  item, finish with the matching `render_user_profile`,
  `render_collection_preview`, or `render_good_preview` tool. Do this even when
  the user says “tell me about,” “what is in,” or otherwise omits words such as
  “show,” “open,” “card,” or “preview.”
- Do not mount a preview when the user explicitly asks for text only.
- For broad or multi-result requests, return the data result without mounting
  several previews.
- For an ambiguous name, resolve it with the relevant list tool. Render only
  after one clear match remains; otherwise ask the user which result they mean.
- Render once, as the final presentation step, after gathering any context
  needed to answer the request.

## Resolve profiles, collections, and items

- An exact Goodsend profile URL can go directly to `render_user_profile`.
  A person's name or handle can go in its `person_query`; it resolves a unique
  Circle match internally.
- An exact collection ID or shared collection URL can go directly to
  `render_collection_preview`. A connected account's collection title can go in
  its `query`; it resolves a unique accessible collection internally.
- An exact saved-item ID can go directly to `render_good_preview`. A saved-item
  title or URL fragment can go in its `query`. Include `profile_url` when
  resolving an item from another visible profile.
- Use `list_circle`, `list_collections`, or `list_saved_items` when the user asks
  for a list, when several matches may matter, or when a write needs exact IDs.
- Treat `get_user_profile`, `get_collection`, and `get_shared_collection` as
  data-oriented calls. For a conversational request about one exact object,
  follow the data work with its render tool unless the user requested text only.

## Find grounded gifts

1. Resolve the recipient with `list_circle` or a supplied Goodsend profile URL.
2. Call `get_user_items_from_profile_url`; its result already includes the
   profile, so do not fetch the profile first merely to repeat that information.
3. Use `list_owned_items` to avoid suggesting something the recipient already
   owns.
4. Use `get_public_wishlist` when availability matters. Never claim an item is
   available unless this tool reports it as available.
5. Explain whether a suggestion is an explicit available wishlist item or only
   a taste signal. Render the chosen item, wishlist, or profile as the final
   single-object presentation when appropriate.

## Change data safely

- Resolve collection and item IDs before writes. If a spoken name remains
  ambiguous, ask which target the user means.
- Use `add_links_to_collection` once for a multi-link request.
- Removing an item from a collection keeps it saved. Archiving a saved item
  removes it from collections owned by the connected account.
- Do not infer a mutation from a request to inspect, browse, or preview data.
- Respect the permission and reservation fields returned by collection tools.
  Never identify another person who reserved a wishlist item.
