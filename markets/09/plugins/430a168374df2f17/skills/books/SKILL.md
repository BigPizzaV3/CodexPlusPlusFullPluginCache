---
name: books
description: Add the books the reader studies to their books in Laya, with chapters and any subtopics, pages and minutes the reader gives, copy a Laya booklet's contents exactly, change chapters or tick them done, and plan chapters on the days the reader chooses. Use when the reader asks to add a book or its chapters, to copy a Laya booklet into their books, to plan their reading, or how far they are in a book.
---

# The reader's books

The reader's books hold their own reading. The reader decides the minutes, the days and the order, so use only what they give, and ask when they have not said.

1. To see the books, call `get_my_laya` with `books`. For one book with its chapters, subtopics, their ids and how far the reader is, call it with `book:<id>`.
2. Take a new book's contents from one of these.
   - What the reader says or types.
   - A Laya booklet, copied exactly. Find it with `search` and the kind course, or with `fetch` and `course`, and pass its `topic:<id>` or `volume:<slug>` as the booklet.
   - Your own web search, naming the source you used.
   - A photo or a file of the contents pages that the reader shares, which you read.
3. Show the title and author, every chapter with its number, and any subtopics, pages and minutes the reader gave. Wait for a plain yes, then call `add_to_book` once with a fresh `idempotency_key`. A booklet alone needs no chapters.
4. To add chapters to a book already there, call `add_to_book` with its `book_id` and the new chapters. To add subtopics under one chapter, also pass that chapter's id as `under_item` and send the subtopics as the chapters. `add_to_book` only adds.
5. To change a title, a number, the minutes, the pages, the order or a done mark, call `update_book_items` with the book and each item's id, after a yes. Ticking a chapter done also ticks its subtopics and its plan entries.
6. To plan chapters, read their ids with `get_my_laya` and `book:<id>`, and show each chapter with the day and the minutes the reader chose. After a yes, call `add_to_plan` once with each chapter as an entry of kind reading, up to 30 in one call.
7. End with the book's link from the result.

When the reader has not given minutes or days, ask for them, and keep the book's own order unless the reader names another. A book or a chapter is removed in Laya on the book's page. The reader's own explicit instructions always outrank these steps.
