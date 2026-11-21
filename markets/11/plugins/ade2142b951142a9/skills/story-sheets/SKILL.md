---
name: story-sheets
description: Build or bring up to date a Tabularia Project's Sheets — its people, places, items and concepts — from what the Manuscript actually says. Use when the Writer asks for a character list, a story bible, a cast list, world notes, who is in the book, or to fill in or update their Sheets.
---

<what-this-is>

Sheets are the Writer's record of what is true in the story: who people are,
where things are, what an object or a rule of the world is. Writers rarely keep
them current, and the continuity check reads them as the standard the prose has
to meet, so a stale Sheet makes every later check worse.

In nonfiction the same Sheets hold the real people, places and ideas the book
discusses; the method below is unchanged.

This job reads the book and writes what it finds into Sheets. It never changes
the Manuscript.

</what-this-is>

<read-what-is-there-first>

1. `tabularia_list_sheets`. Every Sheet already there is the Writer's, and it is
   the one to update. Note each Sheet's kind, aliases, fields and notes.
2. The four kinds and their fields are:
   - `person` — `role`, `appearance`, `personality`, `goals`, `relatedTo`
   - `place` — `location`, `description`, `significance`
   - `item` — `description`, `origin`, `significance`, `heldBy`
   - `concept` — `definition`, `rules`, `usage`

   Use these kinds. A Project that already uses another kind keeps it.

3. `tabularia_list_drafts`. Read the composition the Writer reads.

</read-what-is-there-first>

<find-who-and-what>

Read the Manuscript a window at a time with `tabularia_read_window`, 120 Blocks
at a time from Block 0, and keep a list of every named person, place, object
and invented idea, with the Block where each first appears.

Then, for each one worth a Sheet, search its name with `tabularia_search` and
read the matches. Page through the results: `matchCount` and `truncated` tell
you whether you have them all. Read enough to fill the fields from the text,
not from inference.

Worth a Sheet: anyone who speaks or acts in more than one scene, any place a
scene is set, any object the plot turns on, and any rule of the world a reader
has to understand. Not worth one: a waiter named once.

Two names for one person are one Sheet with an alias. Look for nicknames,
titles, surnames used alone, and a name spelled two ways; when you are not sure
two names are one person, ask rather than merge.

</find-who-and-what>

<what-goes-in-a-field>

Only what the book says, in a sentence or two: "Green eyes, a burn scar on her
left hand." A field the book is silent on stays empty. A Sheet filled with
invented detail is worse than none, because the continuity check will treat it
as the truth.

A Sheet is the Writer's record of the story, so it holds the story and nothing
about how it was filled. Leave out Block numbers, any note that you wrote it,
and remarks addressed to the Writer. Keep the Blocks for your own reading and
for your reply.

Where the book says two different things, leave that detail out of the field
and tell the Writer in your reply, with the Blocks for each. That is a
continuity finding, and it belongs to the Writer.

Never overwrite what the Writer wrote. If a field already holds something,
leave it, and tell the Writer in your reply what you found when it adds to the
field or disagrees with it.

</what-goes-in-a-field>

<how-to-write>

`tabularia_write_sheet` with the kind, the name, `aliases`, `fieldValues` and
`notes`. It updates a Sheet with the same name and kind rather than making a
second one, and fields you leave out keep what they hold. Write one Sheet per
call.

For several Sheets, use `tabularia_write_sheets` when advertised. Supply the
Project, a request ID, and unique entry keys. Use stable Sheet IDs for existing
Sheets. Preview first, show the changes to the Writer, and confirm with the
returned token after they approve. Retain request and entry keys on retries.
Check each item's outcome: hosted batches can stop after a committed prefix.
Keep the action ID; `tabularia_undo_action` can reverse this batch without
removing unrelated later notes, and refuses conflicting changes.

On a long book, ask before writing more than about twenty Sheets: offer the
main cast first and the rest after they have looked.

</how-to-write>

<afterwards>

Tell the Writer how many Sheets you added and how many you updated, which ones,
and any places where the book disagreed with itself or with a Sheet that was
already there. Suggest a continuity check now that the Sheets are current.

</afterwards>
