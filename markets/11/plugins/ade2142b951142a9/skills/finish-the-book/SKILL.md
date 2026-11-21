---
name: finish-the-book
description: Give a Tabularia Book a finished look — its title, byline and copyright details, its Matter pages, how its chapters open, scene-break ornaments, drop caps and pictures. Use when the Writer asks to make the book look finished, professional or printed, to set the title, subtitle, author, series or ISBN, to add a title page, copyright page, dedication or author bio, to change how chapters open, to add drop caps or ornaments, or to place illustrations.
---

<what-this-is>

A printed novel follows conventions readers notice only when they are missing:
a title page and copyright page, a dedication if there is one, chapters that
open with a drop cap, and the same mark at every scene break. Tabularia has all
of these. This job puts them in consistently, in a way the Writer can review.

Design is the Writer's. Propose a set, show where it goes, and let them choose.

</what-this-is>

<look-first>

1. `tabularia_project_metadata` — each Book, its details (title, subtitle,
   byline, description, publication details) and its Matter pages: which it
   carries now, under `matterPages`.
2. `tabularia_read_book_settings` — how its Chapters open, its drop cap rule,
   its color, and its Block Styles.
3. `tabularia_list_decorations` — every drop cap and ornament already there, with
   its treatment and size. Match what the Writer has chosen rather than adding a
   second style.
4. `tabularia_list_pictures` — what is in the Images and where it is placed.
5. `tabularia_list_drafts` — so you know which Draft to work in, and whether
   the Writer has named one for this job.

</look-first>

<details>

The title page and copyright page print what the Book says about itself.
`tabularia_set_book_details` sets the title, subtitle, byline, description,
dedication and the copyright page's details — publisher, edition, year, ISBNs
— and the series name the whole Manuscript shares. Only the fields you give
change. Set only what the Writer gave you: never invent an ISBN, a publisher
or a year, and ask for the dedication wording rather than writing it.

The copyright page's disclaimer follows the Book's kind, which
`tabularia_project_metadata` reports as `bookKind`. A novel gets a fiction
disclaimer, a memoir a note that names were changed, and nonfiction a note
that it is not professional advice; an unset Book gets none. If the kind is
unset or wrong, ask the Writer what the book is and set `bookKind` with
`tabularia_set_book_details` rather than editing the disclaimer by hand.

</details>

<matter-pages>

The conventional order is title page, copyright page, dedication, then the
body, then acknowledgements and the author bio. A novel needs the first two;
the rest only if the Writer has something to put in them.

`tabularia_set_book_matter` turns one page on or off for one Book. It reflows
the Book, so propose the set first and turn pages on once the Writer agrees.
From the cloud a Snapshot is kept before the change; with Tabularia open on
the Writer's computer, take one with `tabularia_take_snapshot` first. Each
page arrives with sample wording to replace, so tell the Writer which pages
want their words. A page they have written in keeps its writing when turned
off, and the answer says so.

</matter-pages>

<chapter-openings>

A printed novel opens every Chapter the same way. `tabularia_set_chapter_opening`
sets the Book's default — whether a Chapter starts on a new page or a
right-hand page, its label, number and title lines, whether the running header
shows on its first page — and the drop cap every opening paragraph takes. Read
`tabularia_read_book_settings` first, propose one design, and set it once the
Writer agrees. The type itself is a Block Style: `tabularia_set_block_style`
changes Chapter Heading, Chapter Number and the rest for the whole Project or
one Book. These change the Book directly; they are not offered in a Draft.

A typeset page also never strands a paragraph's first or last line at a page
break, or leaves a heading alone at the foot of a page. `keepLinesTogether` in
`tabularia_read_book_settings` says whether a Book does that; new Books start
with it on. If an older Book has it off, mention it, and turn it on with
`tabularia_set_book_details` only when the Writer agrees, since it moves the
Book's page breaks.

</chapter-openings>

<running-heads>

A printed book carries a running head: commonly the author's name and the book
or Chapter title, with the page number in the footer, and nothing on a
Chapter's opening page. The tool sets each place for every page of the Book;
different words on left and right pages are set in Headers & Margins. `tabularia_read_book_settings`
shows what each Book prints now under `runningPageContent`, its margin numbers
under `marginNumbering`, and the header typeface under `pageHeaderStyle`.

Propose one arrangement, and once the Writer agrees set it with
`tabularia_set_headers_and_margins`: each place as words and fields such as
`{{author-name}}` or `{{chapter-title}}`, an empty string for nothing. Keep line
and paragraph numbers out of a finished book unless the Writer wants them;
they are working aids. The answer's `previous` puts everything back if the
Writer changes their mind. From the cloud a Snapshot is kept first; with
Tabularia open, take one with `tabularia_take_snapshot` first.

</running-heads>

<drop-caps>

The convention is a drop cap on the first paragraph of each Chapter and nowhere
else. The simplest way to get it is the Book's own rule, set with
`tabularia_set_chapter_opening`, which every Chapter follows. Add one
paragraph by paragraph only when the Writer wants a few, or wants to review
each. Read the Chapter openings with `tabularia_read_window` to find each first
paragraph's Block id. The paragraph has to begin with a letter, so a Chapter
that opens on a quotation mark cannot take one; list those for the Writer
rather than skipping them silently.

`tabularia_arrange_drop_cap` adds one. It goes to your own Draft unless you
name another, and each is a difference the Writer merges, so add them all in
one Draft and tell them where it is. Put them straight into the text
(`target: "base"`) only when the Writer asked for that. Use the `treatmentId` of a drop cap already in
the book so they match; with none, the default is fine.

</drop-caps>

<ornaments>

An ornament marks a scene break inside a Chapter. Use the same one at every
break; a different mark at one break reads as an error.

`tabularia_add_ornament` adds a Block, which a Draft written from the cloud
cannot hold, so it goes into the Base Draft with `target: "base"`, after a
Snapshot. That changes the text itself, so first list the breaks you would
mark and add them once the Writer says yes. A Chapter or Scene boundary is not
an ornament; do not add one there.

</ornaments>

<pictures>

Pictures come from the Writer's Images. `tabularia_add_picture` brings one in
from an openly licensed source, and you tell them it records where it came from
and that they should check its license before publishing.
`tabularia_place_picture` puts one beside a paragraph. Left to itself it
offers the picture in your Draft, "Pictures from your assistant", for the
Writer to accept; with `target: "base"` it goes into the book at once, which is
for a picture they asked to have placed. The answer says which happened. Do not
place pictures they did not ask for.

</pictures>

<afterwards>

Say what you changed or offered, where each change is waiting — which Draft,
or the text itself — and what you left for the Writer to supply, such as the
dedication wording or an ISBN. Say that History holds a Snapshot from before
the changes that went straight into the Book.

</afterwards>
