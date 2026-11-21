# Read the right context

## Capsules

Both `get_styling_context` (selected clothes) and `get_style_review_context`
(a paginated capsule) accept an exact `capsule_name` or returned `capsule_id`.
Use the explicit request, then the conversation's clearly selected capsule,
otherwise its returned default (most recently used/main closet). Carry the selected
reference into follow-ups. Merely comparing or mentioning another capsule does
not change the conversation selection. Ambiguous names return real choices.

For `search_wardrobe`, resolve a name through the context read first and pass the
returned capsule reference. Follow clothing cursors for the coverage needed by the
request. Keep original filters and selection while paging; switch capsules with a
new read. Label capsule comparisons. Current active membership governs availability;
stored/removed historical garments are evidence, not current wardrobe candidates.
No tool here changes native capsule selection.

## Clothing photos

Search and capsule context include saved garment image references. To show or
inspect particular clothes, pass their returned item IDs to `get_styling_context`;
it returns the saved photos as inline image content and a per-item image status.
Use those returned images, not a retailer URL or an inferred image link. If a
photo is unavailable, say so; do not describe clothing details as a verified photo
or add the garment again to repair it. These are entitled wardrobe reads and do
not require sharing a body photo or starting a try-on.

## Wear history

Wear history is account-wide regardless of the styling capsule. It describes logged
outfits, not every occasion the person wore something. Do not relabel it as capsule
history or infer dislike from missing wear. Favorites are not proof of wearing.

The initial context includes a recent-year page of up to 50. Use `get_wear_history`
with the same window and returned cursor to continue; 50 is a page size, not a
history limit. For older periods, use inclusive UTC `start_date`/`end_date`, or
`all_history: true`, instead of `days`. Follow `next_cursor` with unchanged filters
and limit for the requested coverage. On an expired/changed snapshot, start a fresh
read and avoid mixing its totals with the previous snapshot.

Full-window counts and returned-page counts are separate. Base charts and claims
on the relevant complete counts; state incomplete coverage if not all requested
pages can be read. Do not call sampled logs a lifetime total.

If the person declines history or shopping context, use
`get_style_review_context` with `include_history: false` or
`include_shopping: false`. Set `include_preferences: false` when requested.
`get_styling_context` includes authorized history/preferences automatically, so
avoid it when those inputs have been declined. Narrow wardrobe/style reads remain
available subject to entitlement and their own permissions.

## Preferences and saved results

Native likes and Favorites are distinct positive evidence. Native dismissals are
exact outfit exclusions, with any returned capsule/date restriction; they are not
dislikes of individual garments or similar styles. Changing accessories must not
evade an excluded core outfit. Follow each source cursor through
`get_preference_context` when additional evidence matters; keep kind and limit
unchanged. Separate current stated preferences from these saved signals.

Missing permission, missing data and no result are different states. Do not invent
a saved season/Style Map or offer a quiz as a prerequisite. The plugin has no shared
editable text-preference memory in this version. No private notes/chats or body
photos are part of ordinary context reads.
