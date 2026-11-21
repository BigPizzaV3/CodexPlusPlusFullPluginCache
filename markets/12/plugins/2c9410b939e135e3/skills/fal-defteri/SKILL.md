---
name: fal-defteri
description: Use when the user wants to keep, correct, revisit, share or delete their coffee readings ('falımı kaydet', 'show my fal defteri', 'share this reading'). Manages the fal defteri, the user's own journal of Fincanya readings.
---

The user wants to do something with readings they already have: keep one, fix a shape they see differently, look back at past cups, share one with friends or remove one. The fal defteri (journal) belongs to the user's ChatGPT account and holds only their own readings.

## Flow

1. To keep the reading just made, call `save_reading`. Saving twice keeps one copy.
2. When the user sees a shape differently ("shape 2 looks like a fish to me"), call `rename_shape` with the shape number and the lexicon entry they name. The card comes back with the new name and its traditional meaning; the other shapes keep theirs.
3. To look back, call `open_journal`. It shows the saved readings with their dates, a thumbnail of each cup and the first shape names; tapping one opens its card.
4. To share a reading, call `share_reading`. It returns an unlisted link that friends can open without ChatGPT. `stop_sharing` turns the link off at once.
5. When the user asks, `delete_reading` removes one reading or the whole fal defteri.

## Scope

- A reading has to exist first. For a new cup photo, the coffee-reading skill comes first.
- Shape names come only from Fincanya's lexicon of about 400 traditional shapes, in Turkish or English.
- Unsaved readings are removed after 24 hours; saved ones stay until the user deletes them.
