---
name: story-shape
description: Help a Writer choose, record or read against the story shape their book follows — Save the Cat, Hero's Journey, three-act, Story Circle, a romance or mystery beat sheet, a memoir or proposal outline — in Tabularia. Use when the Writer asks which structure their book fits, what shape it is, whether to use Save the Cat or the Hero's Journey, to map a draft onto a structure, to record or change the Book's story shape, or to read an imported manuscript against a structure it was not started from.
---

<what-this-is>

A Book in Tabularia can record the story shape it follows. It is set when the
Project is made from a shape, or when one is applied later from the Timeline
panel, and the Writer can change it in Book settings under **Story shape**. It
is a label: changing it moves no words, Outline items or Timelines.

Three jobs come under this skill, and the Writer usually wants one:

- **Choosing a shape** for a book that has none, or checking that the one it
  records still fits.
- **Mapping a draft onto a shape**: which Chapters carry which parts.
- **Reading against a shape** the Project was not started from, such as an
  imported manuscript.

None of these rewrites the book. Placing beats on a Timeline is
`story-structure-beats`; a developmental read against the recorded shape is
`structural-read`.

</what-this-is>

<read-what-is-there>

1. `tabularia_project_metadata`. Each Book reports `storyShape`: null, or the
   shape with its name, what it is for, and every part with its note. Its `form`
   says whether this is a novel, a series, an article or a script.
2. `tabularia_list_story_shapes`. `shapes` are the structures with beats, each
   beat with where it usually falls; `outlineShapes` are the ones whose
   structure is Chapters or an article's Headings. Work from these definitions,
   not from your memory of a structure.
3. `tabularia_list_anchors` and `tabularia_list_comments`. A Project started
   from a shape carries each part's note on its Outline Anchor as a comment,
   and the Writer may have edited those notes. Where they differ from the
   catalog, the Writer's notes are the standard.

</read-what-is-there>

<choosing-a-shape>

Read the book before recommending anything, a window at a time with
`tabularia_read_window`. Recommend the shape the book already resembles, not
the one you would have written it to: a book that turns at a quarter, a half
and three quarters already has three acts, whatever it was planned as.

Give the recommendation with its evidence. Name the two or three parts that
fit best, each with the Block where the book does that part's job. Then name
the one that fits worst. If a second shape fits nearly as well, say so and say
what would decide between them.

Offer only shapes for the book's form. A screenplay's beat sheets are not a
novel's, and an article's shapes are Headings, not Chapters.

A book that fits no shape is a finding, not a failure. Literary fiction,
braided narratives and many memoirs follow none of the catalog's shapes. Say
what shape the book does have, in its own terms, and leave the label at None.

</choosing-a-shape>

<recording-it>

Record a shape only once the Writer has agreed to it. Then use
`tabularia_set_story_shape` with the Book's id and the shape's id, or an empty
`shapeId` to record none. The answer carries `previousShapeId`, so tell the
Writer what it was and that setting it again puts it back.

Recording the shape does not write its part notes onto the Outline. If the
Writer wants the notes too, that is creating Outline items or placing beats,
and it changes the Project: say what will be added and do it only when asked.

</recording-it>

<mapping-a-draft>

Work through the shape's parts in order. For each, name the Chapter or Block
range that carries it and quote the sentence where it turns. Where a part
spans several Chapters, give the range.

Report the map in the chat as a table, part by part. Where a part has no home
in the draft, say what stands in its place instead. Leave a comment with
`tabularia_add_comment` only on the parts the Writer will want to act on: a
missing midpoint, an act break twenty Chapters late. A comment on every part
of a shape that already fits is noise.

</mapping-a-draft>

<reading-against-a-shape>

When the Book records a shape, read against it, and against the Writer's own
part notes where they exist. When the notes on the Outline belong to a
different shape than the label, say which two you found and ask which one the
Writer means before going further. Do not pick one and carry on.

When the Writer names a shape the Project did not start from, read against the
catalog's parts for it and say plainly that the Outline carries no notes for
that shape. Offer to record it only if the read shows the book fits.

</reading-against-a-shape>

<what-not-to-do>

- Do not change the shape the Book records because the book does not fit it.
  Report the mismatch; the label is the Writer's.
- Do not move, rename or create Outline items to make a draft fit a shape.
- Do not judge a book as broken for following none of the catalog's shapes.

</what-not-to-do>
