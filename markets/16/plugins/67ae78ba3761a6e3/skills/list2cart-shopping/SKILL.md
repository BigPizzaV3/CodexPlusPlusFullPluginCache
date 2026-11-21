---
name: list2cart-shopping
description: Use when the user wants to turn meal planning, recipes, events, or other conversation decisions into a shared List2Cart shopping list, or manage an existing List2Cart list URL.
---

# List2Cart shopping workflow

Use the List2Cart MCP tools for shopping-list operations. The service is intended for shared household lists and does not require user login.

## Privacy and data minimization

- Do not send conversation transcripts, personal discussion, recipe narratives, event descriptions, or unrelated context to List2Cart.
- Send only the list name, product names, quantities, extension days, and list URL as needed by the tools.
- Extract only items the user has decided to buy or explicitly asks to add. Do not infer optional ingredients or unrelated products without making them clear to the user.
- Preserve quantities and units. If quantity is unknown, omit it rather than inventing one.
- Treat list URLs as user-provided access references. Use them only for the requested list operation and do not expose them to unrelated services.

## Create a list

When the user asks to make a shopping list from the current conversation:
1. Identify a concise, useful list name (for example, a meal name or event name).
2. Extract only the agreed purchase items and their stated quantities.
3. Call `create_shopping_list` with the list name and item names/quantities according to its advertised schema.
4. Return the resulting List2Cart URL and explain that opening it and completing registration activates the list for 30 days, as described by List2Cart.
5. Do not claim the list was created unless the tool confirms success.

## Add items

When the user provides a List2Cart URL and asks to add products:
1. Use `add_shopping_list_items` with that URL and only the requested product names and quantities.
2. Confirm the additions only after tool success.

## Read a list

When the user asks what is on a List2Cart list, or asks about assignments, budget usage, or remaining time:
1. Use `get_shopping_list` with the supplied URL.
2. Summarize only the returned list data. Do not infer a person's assignment or remaining budget if it is absent.

## Extend expiry

When the user explicitly asks to extend a list:
1. Confirm the requested extension duration if it is ambiguous.
2. Use `extend_shopping_list` with the supplied URL and requested number of days.
3. Report the new expiry only if returned by the tool.

## General behavior

- If the URL is missing for an operation on an existing list, ask the user for it.
- Never create, add, or extend a list merely because shopping items were discussed; wait for a clear request to make or manage a list.
- Batch items into as few tool calls as practical.
- The tools are described as non-destructive, but still require user intent for write operations.
- If a tool returns an error or incomplete result, state that plainly and do not fabricate a URL or result.
