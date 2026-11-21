---
name: opening-pages
description: Read the opening pages of a Tabularia Manuscript the way an agent or acquiring editor reads a submission, and say whether they would keep reading. Use when the Writer asks about their first chapter, first page, opening line, hook, whether the opening works, or is preparing pages to submit.
---

<what-this-is>

Agents decide in the first five to ten pages, often the first few paragraphs,
whether to read on. This job reads only those pages, as they would, and says
where attention holds and where it would slip.

This is for a novel or narrative nonfiction. A script's first pages are part
of `screenplay-read`, and an article's opening is the heart of `article-edit`.

It is a read, not an edit. Findings become comments; nothing in the text
changes.

</what-this-is>

<read-what-they-would-read>

1. `tabularia_list_drafts`, then `tabularia_project_metadata` to find where the
   body begins. Front matter is not what an agent reads first; start at the
   first Chapter.
2. Read about 3,000 words from there with `tabularia_read_window` — the length
   of the ten pages most submissions ask for — and stop. Do not read further
   before giving the verdict: the point is to judge what the agent sees.
3. Ask the genre if the Project does not say. A thriller and a literary novel
   earn attention differently.

</read-what-they-would-read>

<what-to-look-for>

The problems agents name most often in openings:

- **The story starts late.** Waking up, travel, weather, a dream, or several
  pages of backstory before anyone wants anything. Name the Block where the
  story begins and what comes before it.
- **No one to follow.** By the end of the first page the reader should know
  whose story this is and something they want or fear.
- **No question.** Something unresolved that the reader wants answered. It
  need not be action; it has to be there.
- **Explanation before interest.** History, world rules or family trees the
  reader has not yet been made to care about.
- **Too many names at once.** More than three or four characters introduced
  before the reader has a grip on one.
- **Prose that gets in the way.** Run `tabularia_prose_metrics` on the opening
  Chapter and compare it with a later one. Read the counts the way `prose-read`
  says to; an opening noticeably flatter or more adverb-heavy than the rest of
  the book is a finding.

What is not a problem: a quiet opening that holds a question, an unusual
structure that is clearly deliberate, or a prologue that earns its place.
Prologues are not banned; ones that delay the story are the trouble.

</what-to-look-for>

<what-to-report>

Start with the verdict an agent would reach: where they would stop reading, if
they would, and why, citing the Block. Then up to three findings, each anchored
with `tabularia_add_comment` on the passage it is about. Say what is working too,
in a line.

If the Writer then wants the opening rewritten, that is a Draft: offer one, and
use `line-edit` for sentence work.

</what-to-report>
