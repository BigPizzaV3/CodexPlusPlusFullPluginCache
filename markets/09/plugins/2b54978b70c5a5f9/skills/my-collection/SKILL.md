---
name: my-collection
description: Save identified records to the user's VinylAI collection with their condition and notes, and list or summarise the collection (by decade, genre, artist). Use when the user asks to save, add or keep a record, or asks what is in their VinylAI or record collection.
---

# My collection

Use this skill when the user wants to keep a record, or asks about their VinylAI collection. Saving and listing need the
user to sign in to VinylAI once (ChatGPT shows "Connect" the first time). Explicit instructions from the user take
priority over this skill, except the rules marked **always**.

## Save a record

1. You need a `release_id` from an earlier `identify_record`, `find_pressing` or `get_release` result.
   - If the match was only `album` or `pressing_group`, tell the user the exact pressing isn't confirmed and ask
     whether to save the pressing shown or to narrow it first (runout, label). Never present the saved pressing as
     confirmed when it wasn't.
2. Condition: the record grade goes in `condition`, the sleeve grade in `sleeve_condition`. Use Goldmine grades only:
   M, NM, VG+, VG, G+, G, F, P. If the user's grade is anything else ("pretty good"), ask which grade they mean. Put
   anything else they say about the copy in `notes`.
3. Call `save_to_collection`. If the user isn't signed in, ChatGPT runs the sign-in first.
   - **After sign-in, if the save did not run, call `save_to_collection` once more with the same arguments.** The
     duplicate guard makes this safe: the same record is never saved twice by a repeat.
4. Answer by `status`:
   - `saved` — say it's saved to their VinylAI collection, show the masked account email, and say: "To see it in the
     VinylAI app, sign in there with this email."
   - `already_saved` — say it's already in the collection (with the number of copies) and nothing was saved. Only if
     the user then says they have another copy, call again with `allow_duplicate: true`.
   - `quota_full` — the collection is full (10,000 items); nothing was saved.
   - `daily_limit` — the daily limit is reached; try again later today. Don't suggest anything else.

## List the collection

1. Call `list_collection`. Use `query`, `artist`, `decade` or `condition` when the user asks for a subset; use `page`
   for "show more" / "page 2" (25 records per page, newest first).
2. Answer from the result: the records, the total, and the summary (by decade, top genres) for questions like "which
   decade do I have most of?".
3. Empty collection: say so, suggest "What record is this?" with a photo, and mention that records from the VinylAI
   app appear here after signing in to the app with the same email.

## Rules

- **Always: no prices, no value totals,** no "your collection is worth". The plugin has no price data.
- **Always: the plugin only adds records.** It can't edit or delete them. For "delete …" or "change the grade of …",
  say this is done in the VinylAI app. To delete the whole account and its data, the user can do it in the app or write
  to support@vastflow.kz.
- Show only the masked email the tool returns; never ask the user for their email in the chat.
