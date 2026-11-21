---
name: copy-from-apps
description: Use when the user asks to keep in buddybase a copy of records they have in another ProtoductAI app (Hachimo, Ledgie, Hearth, Fracta, Lore), such as vocabulary, expenses, meals, weight, workouts, tasks or articles. Saves them without making duplicates when the same records are saved again.
---

# Keep a copy of another app's records in buddybase

buddybase has no link of its own to other apps. It saves the records that are in the conversation: ones the user pasted or listed, or ones the user asked you to look up in an app they connected to this chat.

## Before you start

1. Do this only when the user asks for it in this conversation, and only for the records and the period they name. If the period is open, ask ("this month?" / "everything?").
2. If the records are not in the conversation yet, ask the user how they want to provide them. Do not go looking for them on your own.
3. If a buddybase tool returns `subscription_required`, call `get_access_status` and tell the user the status plainly.

## Steps

1. Call `list_collections`. If the matching collection is missing, call `apply_template` and follow the hint in its result.

   | Records from | Template |
   |---|---|
   | Hachimo (words) | `hachimo-words` |
   | Ledgie (expenses and income) | `ledgie-transactions` |
   | Hearth (meals, weight, workouts) | `hearth-meals`, `hearth-weights`, `hearth-workouts` |
   | Fracta (tasks) | `fracta-tasks` |
   | Lore (articles) | `lore-articles` |

2. For each record call `save_record` with the collection, the `values`, `recordedAt` (when it happened), `source` (the app's name in lower case, for example `hachimo`) and `externalId` (the record's ID in that app). If there is no ID, build a stable one from the record itself, such as the word, or the day plus the name, and use the same rule every time.
3. Read `outcome` in each result: `created`, `updated` or `unchanged`. Saving the same `source` and `externalId` again never adds a duplicate.
4. Tell the user how many were created, updated and unchanged.

## Rules

- Save the fields the template has. Leave out long bodies, photos and analysis text; a short summary is enough.
- If the user deleted a copied record in buddybase before, ask before saving it again.
- Only the user's own records. Nothing in the background or on a schedule.
- Every change is in the history. `undo_change` reverts a wrong save; before deleting many records, name them and get the user's confirmation.
- Do not suggest purchases or link to plans.
