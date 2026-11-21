---
name: article-edit
description: Edit an article, essay, blog post or newsletter in Tabularia — its headline, opening, structure, length and ending — for the reader who will decide in a few seconds whether to keep reading. Use when the Writer asks to improve, tighten or review an article, blog post, essay, newsletter or column, or asks about its headline, opening, length or structure.
---

<what-this-is>

An article is read on a screen by someone who can leave at any line. Most of
what makes one work is in the headline, the first two paragraphs and the
shape, so that is where this job spends its attention. Sentence work is
`line-edit`, and it applies here unchanged.

Findings are comments; changes go in a Draft, as everywhere else.

</what-this-is>

<read-it-whole>

Articles are short, so read the whole piece with `tabularia_read_scope`
(`book`) or `tabularia_read_window`, and `tabularia_statistics` for its length.
Quote that count, not your own.

`tabularia_list_anchors` and `tabularia_list_comments` show whether it was
started from an article shape — Inverted Pyramid, Feature, Argument or Review
— and what each heading is for. Read against that shape if it is there; ask
which the Writer intends if it is not.

Ask where it will run and for how many words, if they have not said. A
newsletter, a magazine feature and a blog post have different lengths and
different readers.

</read-it-whole>

<what-to-check>

- **The headline.** Does it say what the piece gives the reader? Clever is
  fine when it is also clear. Offer two or three alternatives, never more.
- **The opening.** By the end of the second paragraph the reader should know
  what the piece is about and why to keep going. A slow warm-up — background,
  definitions, "in today's world" — is the most common fault. Name the
  paragraph where the piece actually starts.
- **The shape.** For news, the most important thing first. For an argument,
  the claim early, then the case, then the objection answered. For a feature,
  a scene or person that carries the idea. Point to where the piece leaves its
  shape.
- **Headings.** On a long piece, do the headings alone tell the story? A
  reader skims them before reading.
- **Length.** Against the target they gave. Name the section that could go,
  not a percentage.
- **The ending.** It should land the point or send the reader somewhere —
  not summarize what they just read.
- **Links.** A read gives each Block's links. Check that each one says where
  it goes, and flag any link text that reads "here" or "this".

</what-to-check>

<how-to-deliver>

Up to five findings, each as a comment with `tabularia_add_comment` on its
paragraph. Headline alternatives go in a comment on the title. If the Writer
asks you to make the changes, put a restructured opening or ending in a Draft
with `tabularia_create_draft` and `tabularia_write_draft`; small fixes go
through `tabularia_propose_edit` as `line-edit` describes. Anything you write
follows `natural-voice`.

</how-to-deliver>

<what-not-to-do>

- Do not write for search engines over readers. If the Writer asks about
  search, a clear headline and a first paragraph that says what the piece is
  about are most of it.
- Do not change the Writer's opinion or soften an argument they meant to make.
- Do not invent facts, quotes or figures to strengthen a point.

</what-not-to-do>
