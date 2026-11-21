---
name: map-builder-workflow
description: Use Map Builder to make and change custom maps by description, and to put a map online as a live page. Invoke its tools when the user wants a map of a place, a map with their own pins, notes, routes, areas or circles, a map in a particular style or color theme, a change to a map made earlier in the conversation, or to publish or share a map as a live page.
---

# Map Builder workflow

Use the connected Map Builder MCP server for custom maps rather than describing a map in text or inventing an image.

## Tool routing

- Use `create_map` for a new map. Put the area in `place`, a ready-made look in `style`, and a described look ("Halloween", "dark with gold roads") in `colors`, as hex colors on the named map parts.
- Use `edit_map` for any change to a map already made in this conversation. Always pass the `draftId` from the latest result; each edit returns a new one. Refer to existing items by the exact names in the result's `items` list.
- Use `list_map_styles` when the user asks what styles exist or wants to choose one.
- Use `publish_map` when the user wants the map online as a live page they can share or embed. Pass the `draftId` from the latest result. No account is needed. Calling it again after `edit_map` updates the same page.
- Use `get_claim_link` only after `publish_map`, and only when the user says they want to keep the map by saving it to their Map Builder account.

## Publishing: share or keep

After `publish_map`, give the user the page link and ask one question: do they just want to share the page, or save the map to their Map Builder account? If they only want to share it, stop there. Call `get_claim_link` only if they choose to save it.

The page link is public and safe to share. The link from `get_claim_link` is private: whoever opens it first and signs in becomes the owner of the map. Tell the user plainly not to share or post it, and never give it out unless they asked to save the map. If they later ask you to send or share "the link", give the page link, not the private one.

## Places

- For cities and well-known landmarks, give `lat`/`lng` from your own knowledge.
- For street addresses and specific businesses, give `address` instead, so it is looked up precisely. Never estimate coordinates for a street address.

## Response behavior

- The map appears as a live preview in the chat; don't describe it at length or repeat its links unless asked.
- If the result includes notices (for example a feature that isn't included in the user's current plan, or a color that couldn't be read), tell the user plainly. Don't promote upgrades or quote prices.
- If an edit reports that nothing changed, fix the request (a hex color, an exact item name) or ask the user; never say a change was made when the tool says it wasn't.
- Downloads and file uploads aren't available in ChatGPT; point the user to Open in Map builder for those.
