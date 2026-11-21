---
name: story-structure-beats
description: Place a story structure's beats — Save the Cat, Hero's Journey, three-act, or the Writer's own — where the Manuscript actually hits them, and name Anchors from what happens there. Use when the Writer asks to place or fix their beats, line up a story structure with the book, check where the midpoint really is, move a beat to the right scene, or rename their Anchors or Timeline markers from the prose.
---

<what-this-is>

A story structure in Tabularia is a Custom Timeline whose markers are the beats.
The Writer's "create Timeline from a story structure" button places each beat at
its share of the book's words: the Midpoint at half the words, the Catalyst at
about a tenth. That is a guess about where a beat should fall, made without
reading a word. This job reads the prose and puts each beat on the paragraph
where the story actually turns.

It also covers naming: an Anchor called "Point anchor" or "Catalyst" can be
renamed from what happens at it, such as "Catalyst — Mara finds the letter".

This job moves and renames Anchors. It never changes the Manuscript's wording.

</what-this-is>

<read-what-is-there-first>

1. `tabularia_list_timelines`. Find the structure's Custom Timeline by its
   title and note each marker's id, title, and where it starts. A Timeline the
   Writer built is theirs; work on it rather than beside it.
2. `tabularia_list_anchors` with the point and range kinds. Each marker's Anchor
   carries a `timeline-marker` attachment naming the marker id; that Anchor's
   `id` is what the rename and move tools take. Read any notes with
   `tabularia_read_anchor`: the structure's own description of each beat is
   often there, and it is the definition to place against.
3. `tabularia_project_metadata` for the Books and Chapters, and
   `tabularia_read_page_map` for where they fall.

Learn the structure from Tabularia, not from memory. `tabularia_list_story_shapes`
lists the structures Studio offers, each beat with its index, title, the share
of the book where it usually falls, and a note on what it is for. Place against
those beats and those notes, even where you know a different version of the
structure.

If there is no structure Timeline yet, make it and place every beat in one call
with `tabularia_place_story_structure`, once you have read the book (see below).

</read-what-is-there-first>

<find-the-beats>

Read the whole book before placing anything, a window at a time with
`tabularia_read_window`, 120 Blocks at a time from Block 0. Keep a running list
of the turns: the first disturbance, each decision a character cannot take
back, reversals, the lowest point, and the confrontation.

Then, beat by beat, say in one sentence what the beat is in this book's terms
and find the paragraph where it happens. The beat goes on the paragraph where
the turn lands, at offset 0 or at the start of the sentence that turns it, not
on the chapter heading before it and not on the aftermath. Use
`tabularia_search` to confirm a moment you remember. A beat is a point unless
the structure means a stretch, like Fun and Games; then give it a `to`
endpoint at the end of that stretch.

What is not a finding:

- A beat that lands away from its percentage. Structures describe proportion
  loosely, and a Midpoint at 42 percent of the words is a Midpoint.
- A beat the book does not have. Leave that marker where it is, and tell the
  Writer the book has no clear one rather than forcing it onto the nearest
  scene.
- A beat that could plausibly sit in two places. Pick the stronger, and name
  the other in the report.

Beats that land out of order, or two beats on one scene, are structural
findings. Report them; do not reorder the Timeline to hide them.

</find-the-beats>

<move-and-name>

For a new structure, give `tabularia_place_story_structure` the `shapeId` and
one passage per beat you found, each as its `beat` index with `from` and
optional `to`. A beat you leave out lands where Studio's own button would put
it, by share of words, and the result marks it `share-of-words`; say which beats
those are rather than presenting them as read. It creates the Timeline under the
name Studio gives that structure, with every beat's title and order from the
catalog and labels set to manual.

For a structure that already has a Timeline, move with `tabularia_move_anchors`, addressing each new place by `blockId` and
paragraph `offset` exactly as `tabularia_add_timeline_markers` does. Rename with
`tabularia_rename_anchors`. Each takes up to 20 entries per call.

Both preview first. Show the Writer a table of every beat: its name, where it
was, where it would go, and the opening words of that paragraph. Repeat the same
request with the returned `confirmationToken` only after the Writer agrees, and
keep `requestId` and entry keys unchanged on retries.

Renaming keeps the beat's name at the front and adds what happens: "Midpoint —
the vault is empty". A renamed Anchor's label becomes manual, so automatic
labeling will not write over it. Do not rename a marker the Writer titled
themselves unless they asked for that.

These tools work the same over the remote connector and with Studio open. In
an open Studio a move also needs the target passage in view; if one is refused
as outside it, bring it into view with `tabularia_reveal` on that Block and ask
again. Hosted, each Anchor, marker, and the new Timeline is recorded as its own
stage: read `succeededKeys` and `partialKeys`, and repeat the same request with
the same `requestId` to finish what did not land rather than starting over.

A Draft that is locked, or a review kept as it was submitted, keeps its Anchors
as they are. A move that would take an Anchor out of one, or onto a passage
only such a Draft holds, is refused; tell the Writer which Draft holds it, and
place the beat on a passage the Base or an editable Draft carries. A renamed
Anchor in such a Draft is fine, because the title is not part of its copy.

Keep each `actionId`. `tabularia_undo_action` puts that call's Anchors back as
they were, and refuses any the Writer has changed since. Undoing a placed
structure removes its Timeline with its beats, and refuses once the Writer has
changed a beat or added a marker of their own to that Timeline.

</move-and-name>

<afterwards>

Tell the Writer which beats moved and how far, which stayed, and which the book
does not seem to have, with the paragraph each now sits on. Name any beats that
came out of order or share a scene. If those are many, suggest a structural read.

</afterwards>
