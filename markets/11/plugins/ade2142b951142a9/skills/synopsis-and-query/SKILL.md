---
name: synopsis-and-query
description: Write a synopsis, a query letter, a pitch or back-cover copy for a Tabularia Manuscript from the book itself. Use when the Writer asks for a synopsis, query letter, pitch, logline, blurb, back-cover copy or book description, or is getting ready to submit to agents or publishers.
---

<what-this-is>

The documents a Writer needs to submit a book, written from the book rather
than from a summary of it. They are short, and every sentence has to be true of
the Manuscript: an agent who requests pages after a synopsis that promised a
different book does not request more.

A nonfiction book is usually sold on a proposal rather than a query and a
finished manuscript; `nonfiction-read` covers what a proposal needs. For a
script, the logline and synopsis are part of `screenplay-read`.

</what-this-is>

<read-the-book>

1. `tabularia_project_metadata` for the title, subtitle, series name, the Books
   and their Chapters, and the description the Book already carries; and
   `tabularia_statistics` for the word count. Quote that count, not your own.
2. `tabularia_list_sheets` and `tabularia_list_comments`: the Writer's own notes
   on who matters and what each part is for.
3. Read the whole Manuscript with `tabularia_read_window`, 120 Blocks at a time.
   A synopsis written from the first chapters and the last one gets the middle
   wrong, and the middle is where the turns are.

Keep, as you read, the protagonist's goal, what stands in the way, each turn
that changes the plan, and how it ends.

</read-the-book>

<what-each-one-is>

Ask which the Writer wants, and for an agent or publisher's guidelines if they
have them. Guidelines win over everything below.

- **Synopsis.** One to two pages in present tense, third person, telling the
  whole story including the ending. Name only the characters the plot needs —
  usually three to five — and give each their name in capitals the first time.
  It is a plot document: what happens and why, not themes.
- **Query letter.** Under 400 words: a hook paragraph, two or three paragraphs
  on the protagonist, what they want, what stops them and what they stand to
  lose, then title, genre, word count and comparable titles, then a short bio.
  It does not give away the ending.
- **Logline.** One sentence: who, what they want, and what is in the way.
- **Back-cover copy.** For readers, not agents: the setup and the question, no
  ending, in the book's own voice.

Comparable titles and the bio are the Writer's to supply. Leave a marked gap
for each rather than inventing them; a wrong comparison or a made-up credit is
the one thing in a query that can do real harm.

</what-each-one-is>

<how-to-deliver>

Give the text in the chat, ready to copy into an email or a submission form.
If the Writer wants to keep it in the Project, save it with
`tabularia_write_sheet` as a `concept` Sheet named for the document — "Synopsis",
"Query letter" — with the text in `notes`, and update that one next time rather
than making another.

Then say what you left out and why, in a line or two, so the Writer can put
back a subplot they care about.

</how-to-deliver>

<what-not-to-do>

- Do not hide the ending in a synopsis. Agents ask for it.
- Do not set the Book's description from your back-cover copy, or change its
  title or subtitle, unless the Writer asks. When they do,
  `tabularia_set_book_details` sets the description, subtitle and series name
  the Book's published files carry; give it only the fields they approved.
- Do not describe the book with praise — "gripping", "unforgettable". The
  events have to do that. An agent reads hundreds of these, and the habits
  `natural-voice` lists are the ones they have learned to spot.
- Do not change the Manuscript's wording, or suggest changes to it, as part of
  this job.

</what-not-to-do>
