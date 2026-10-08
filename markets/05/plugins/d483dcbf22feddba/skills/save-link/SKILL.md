---
name: save-link
description: Save web pages into the user's Saive library. Use when the user asks to save, bookmark, or add one or more links to Saive, with or without tags, a folder, or a note.
---

# Save links to Saive

## Steps

1. Collect the URLs the user asked to save. Save those and nothing else.
2. When the user names a folder, call `list_folders` and match the name,
   ignoring case. If no folder matches, list the folders that exist and ask
   which one to use. `save_url` cannot create folders.
3. Check the matched folder's `sharing_level`. A save in a `public` folder
   appears on that folder's public page, and a save in a `designated` folder
   is visible to the people the folder is shared with. Before saving into
   either, tell the user who will see the save and ask them to confirm. Save
   only after they say yes.
4. Call `save_url` once per URL. Pass tags, folder, note, or starred only
   when the user gave them.

## Output

One line per URL:

- **Saved**, for a new save.
- **Already in your library**, when the response has `already_saved` set to
  true. Saive keeps the user's existing tags and notes.
- **Not saved**, with the reason from the error.

Then tell the user that Saive fetches and summarizes each page in the
background, so the summary appears in their library within a minute or two.

## Boundaries

- A new save is unread, and private unless it goes into a shared folder.
  This plugin cannot change a folder's sharing; that happens in the Saive app.
- Only http and https URLs work.
