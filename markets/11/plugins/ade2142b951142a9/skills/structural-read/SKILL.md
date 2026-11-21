---
name: structural-read
description: Read a Tabularia Manuscript against the shape it was built on — the story structure's own part notes — and report where the writing does not yet do what each part is for. Use when the Writer asks about structure, pacing, act breaks, a middle that drags, an opening that does not hook, an ending that does not land, whether a beat lands, or asks for a developmental read.
---

<what-this-is>

A developmental read, not a line edit. You are answering one question: **does
each part of this Manuscript do the job its shape says it should?**

You never rewrite prose here. Everything you find becomes an anchored comment
the Writer reads in Studio and acts on themselves.

A novel's job. For a nonfiction book or proposal use `nonfiction-read`, for
an article or blog post `article-edit`, and for a script `screenplay-read`.

</what-this-is>

<the-shape-is-already-in-the-project>

This is the part people miss. When a Writer starts a Project from a story
structure, Tabularia writes each part's **note** onto that part's Outline Anchor
as a comment — what that act or beat is meant to do in the progression. It is an
ordinary Anchor comment afterwards, so the Writer may have edited it, replaced
it, or deleted it.

So do not bring a remembered version of the Fifteen-Beat Sheet or the Hero's Journey to
this. Read what the Project actually says:

1. `tabularia_project_metadata` — how many Books, Acts and Chapters there are,
   what they are called, the id that names each Chapter to the Outline tools,
   and each Book's `storyShape`: the shape it records, with the catalog's note
   for every part, or null when it records none.
2. `tabularia_list_anchors` — the Outline: which Anchors are acts, chapters,
   scenes, and where each sits. A page at a time on a novel: read `anchorCount`
   and `hasMore`, and ask again with a later `from` rather than assuming the
   first page is the Outline.
3. `tabularia_list_comments` — the part notes. These are the standard you are
   reading against.

Read against the shape the Book records. Where the Writer's notes on the
Outline exist, they are the standard, because they may have edited them; where
they do not, the catalog's part notes in `storyShape` are.

When the notes on the Outline plainly belong to a different shape than the one
the Book records — Hero's Journey stages under a Three-Act label — say which
two you found and ask the Writer which they mean. Do not pick one.

If the Book records no shape and there are no part notes, the Project was not
started from a structure, or the Writer removed them. Say so, ask which shape
they have in mind, and read against that instead of guessing.
`tabularia_list_story_shapes` gives every shape's parts. Choosing or recording
a shape is the `story-shape` skill's job.

</the-shape-is-already-in-the-project>

<how-to-read>

Work one structural unit at a time, not the whole book at once.

- `tabularia_list_scopes` tells you what levels this Manuscript has.
- `tabularia_read_scope` with `act`, `chapter` or `scene` reads one unit around
  where the Writer is reading. **It does not change what they are looking at.**
- For a unit that is not the current one, read the Block range the Outline Anchor
  gives you with `tabularia_read_window`. Over the remote connector, which
  offers neither scope tool, read every unit this way.

Check `tabularia_list_drafts` first. What you read is the Base Draft plus
whichever Scoped Drafts are showing, and a structural judgement about a chapter
the Writer has a Draft standing over is a judgement about the Draft.

</how-to-read>

<what-editors-find-most>

The shape tells you what each part is for. These are what developmental editors
report most often whatever the shape, and they are worth checking even when
the Project has no part notes at all:

- **An opening that does not start the story.** Backstory, a waking-up, a
  landscape or a stranger's point of view before the protagonist wants
  anything. Agents decide in the first pages, so name the Block where the story
  actually begins and what comes before it.
- **A goal that fades.** The protagonist wants something clearly in Act One and
  then drifts from scene to scene. Tension drains out of a book at the point
  the reader stops being able to say what the character is after, and that is
  usually what a Writer means when they say the middle drags. Say where the
  goal was last restated or pressed on.
- **Stakes that do not rise.** Middle chapters where each obstacle costs no
  more than the one before. Find the last scene where something got worse.
- **Exposition delivered in a block.** Several paragraphs of history or
  world-building with nothing happening. Name it by its Block range; whether it
  belongs is the Writer's call, where it sits is yours to point out.
- **Setups without payoffs, and payoffs without setups.** A skill, an object or
  a secret the ending leans on that was never planted, or one planted with
  weight and never used. Search for it with `tabularia_search` to confirm both
  ends before you say either is missing.
- **An ending that does not answer the opening.** The climax resolves the plot
  but not the question the first chapter asked of the protagonist.

These are findings like any other: a verdict, the Blocks it rests on, one
comment each. Do not run them as a checklist and report every item.

</what-editors-find-most>

<what-to-report>

For each part, one of three verdicts, and say which:

- **Does its job.** Name the paragraph that carries it. Say it in one line and
  move on; a Writer does not need paragraphs of praise.
- **Does its job late or weakly.** Say where it currently lands, where the shape
  expects it, and what the gap costs the reader.
- **Is not there.** Say what is standing in its place instead.

Ground every verdict in the text. "The midpoint is weak" is useless. "The
midpoint note asks for a reversal that closes the hero's retreat; chapter 14 has
the reversal but leaves the retreat open until chapter 19, so the middle reads as
optional" is a note someone can act on.

Then leave them with `tabularia_add_comment`, anchored to the paragraph each one
is about — not a wall of text in the chat that vanishes when the window closes.
One comment per finding. Title it with the part name.

</what-to-report>

<what-not-to-do>

- **Do not propose edits.** A developmental note is not a redline. If the Writer
  asks you to fix something you found, that is a different job — read it again
  and use `tabularia_propose_edit` for a targeted change, or
  `tabularia_create_draft` when the fix is a rewrite of the passage.
- **Take a Snapshot only if you are about to change durable state**, with
  `tabularia_take_snapshot`. A developmental read changes nothing, so it needs
  none, and asking for one anyway leaves a row in the Writer's History that
  answers no question.
- **Do not restructure the Outline because you found a problem in it.**
  `tabularia_create_outline_item`, `tabularia_rename_outline_item` and
  `tabularia_move_outline_item` exist, and a developmental read is not the
  moment for them: where an act break belongs is the Writer's decision, and
  your job here was to say what the shape is doing. Offer; do not act. If they
  ask, make the change they named and read `tabularia_project_metadata` back
  afterwards to confirm where it landed. From the cloud a Snapshot is kept
  first; with Tabularia open on their computer, take one with
  `tabularia_take_snapshot` first. Gathering Chapters into a new Act cannot be
  done from the cloud, so name that one for the Writer to make in the
  Outline.
- **Do not judge a shape the Writer did not choose.** A literary novel that
  ignores beat placement is not broken. If the structure notes are absent and
  they do not name one, describe the shape the book actually has and let them
  decide whether it is the one they want.
- **Do not comment on every paragraph.** A developmental read that leaves forty
  comments is noise. Ten findings is a lot. Three good ones is a useful morning.

</what-not-to-do>
