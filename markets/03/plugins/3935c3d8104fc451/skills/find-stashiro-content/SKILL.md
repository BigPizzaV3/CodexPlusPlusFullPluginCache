---
name: find-stashiro-content
description: Use when Stashiro is selected, mentioned, or already active and the user asks to find, retrieve, browse, or display saved information; locate a Space, board, card, media item, or flight; or continue a Stashiro retrieval task.
---

# Find Stashiro Content

Stashiro organizes content as Space > Board > Card. Spaces group boards; boards hold notes, tables, charts, images, links, flights, and other native cards.

1. Use saved-content search only when the user explicitly asks to find, show, read, retrieve, or inspect existing Stashiro content. A new analysis, plan, comparison, or recommendation does not belong to saved-content search. A `/convert-to-stash` request belongs to `convert-to-stash` unless it also explicitly asks to read saved content. Continue related retrieval follow-ups without requiring another tag.
2. While active, unqualified names and `Space`, `board`, or `card` refer to Stashiro. Interpret `A > B` or `A / B` as Space `A`, board `B`.
3. Use `search` to locate saved Stashiro content by name or content. It returns matching Spaces and boards and renders matching cards in their native UI. Use optional Space or board scope when supplied. Use returned IDs and card data as inputs to any remaining steps in the user's request. Act on a unique match; otherwise present relevant matches or ask a focused question. When `isPartial` is true, say the results are partial and narrow the next search.
4. Do not present the same card twice: `search` already renders its card matches. Use `show_selected_stashiro_cards` when card IDs or opaque references are already known and those cards have not appeared in the current response. Present cards from different boards in separate calls.
5. Use `fetch` only with an ID returned by `search` when full data is needed for reasoning. Use `get_space`, `get_board`, or `get_card` when an exact resource ID is already known.
6. Use `browse_all_stashiro_spaces_and_boards` for the workspace or `browse_one_stashiro_space` for one Space only when the user asks to browse. Follow every returned cursor until the requested scope is complete. Never browse to resolve a destination for a write.
7. Use `list_cards` for lightweight summaries, `show_stashiro_board` for an unfiltered board page, and `show_selected_stashiro_cards` for a requested subset. Continue board pages while `isDone` is false.
8. Use `get_card_media` only when the user needs the underlying image or audio. Its URL is short-lived; do not present it as permanent.
9. Do not infer that content is absent outside the searched scope. Report what was searched and return exact `boardUrl` links when available.
