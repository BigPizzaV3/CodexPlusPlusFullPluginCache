---
name: story-thread-draft
description: Build a Timeline or select filtered Outline rows, then revise the passages they cover in an inactive Draft the Writer can review and merge. Use when the Writer asks to revise a character arc, plot thread, chronology, or scattered scenes without changing the Base Manuscript, or asks for a Draft from a Timeline or filtered Outline.
---

<the-job>

Collect the passages that belong to one story thread, capture them in a Draft,
and write alternatives there. The Timeline or Outline selection says _where_;
the Writer decides which revisions, if any, to merge. Never write the Base
Draft for this job, even though the connector would let you: the point is
alternatives the Writer compares.

</the-job>

<find-the-passages>

1. Read `tabularia_list_drafts`, `tabularia_list_timelines`, and the relevant
   Sheets. Check which Scoped Drafts are showing. The remote connector captures
   the last synced Base Manuscript, so say that plainly if the Writer is looking
   at different wording in a showing Draft.
2. For a new Timeline, search the Manuscript for the people, places, objects,
   and events the Writer named. Read each search page until `truncated` is
   false, then read the candidate passages. For several wordings in one Project,
   `tabularia_search_batch` gives independent counts and `nextFrom` positions.
   Read selected stable IDs together with `tabularia_read_passages`, continuing
   any truncated paragraph with its `nextOffset`. Keep the source identities
   together and read again if the source changed. A mention is not automatically a
   scene in the thread. Include a passage because it changes the thread, not
   merely because a name occurs in it.
3. Reuse the existing Timeline when it already tracks that thread. Otherwise
   call `tabularia_create_timeline`, then `tabularia_add_timeline_marker` for
   the selected passages. Read `tabularia_list_timelines` again and check that
   every intended marker arrived. Creating markers changes the Timeline, so
   tell the Writer what was marked.
4. For a filtered Outline, read the Outline markers from
   `tabularia_list_timelines`. Choose the exact marker ids of the visible rows
   the Writer described. Check each row's role and passage; a Chapter row
   captures its whole Chapter, while a Scene row captures that Scene. An
   Outline search or label filter in the Writer's browser is not available to
   the cloud connector, so never claim to have read that live filter. Ask for
   its criteria when the chosen rows cannot be determined from the Manuscript.

</find-the-passages>

<capture-and-revise>

1. Call `tabularia_create_draft_from_source` with the Timeline id, or with
   `sourceKind: outline-filter` and exactly the selected Outline marker ids.
   Name the Draft for the thread and the revision idea. It starts inactive and
   records a fixed capture of the source's current Blocks; later marker or
   filter changes do not silently widen it. If this tool is unavailable, say
   that the current connector cannot retain the named source rather than
   passing guessed Block ids to `tabularia_create_draft`.
2. Read the captured passages immediately before rewriting. Plan changes by
   cause and effect across the thread: what the character knows, what happens,
   what each scene now needs to set up or pay off. Keep the Writer's voice,
   following `natural-voice`, and preserve formatting in Markdown.
3. Call `tabularia_write_draft` only for Blocks the new Draft covers. Use the
   returned Draft id, and supply the exact `readText` from the fresh read so a
   moved paragraph is refused. Read again after a conflict; never guess a new
   offset or overwrite a changed Block.
4. Read the Draft back and verify that the intended passages changed and the
   rest did not. A missing or truncated read is unfinished verification, not
   evidence the whole thread was covered.

</capture-and-revise>

<deliver>

Name the Timeline or selected Outline rows, the Draft, and the passages you
changed. Explain any excluded search hits or unavailable passages. Tell the
Writer the Draft is inactive and ready to inspect in Studio. Do not accept,
reject, merge, publish, or delete anything on the Writer's behalf.

</deliver>
