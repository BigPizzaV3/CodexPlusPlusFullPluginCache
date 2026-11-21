---
name: catalogo-blucher
description: Look up Editora Blucher's book catalog with the Catálogo Blucher tools. Use when the user asks about Blucher books, a book's current edition or availability, an ISBN, the catalog's subject areas and series, or a reading list for a course syllabus.
---

# Catálogo Blucher

Use the Catálogo Blucher tools for questions about books from Editora Blucher, a Brazilian publisher of technical, scientific and academic books. All tools are read-only.

- `buscar_livros`: find books by topic, title, author or ISBN, in Portuguese or English (typos tolerated). Use it first when the user gives no ISBN.
- `obter_livro`: the full record of one book by ISBN (current edition, price in BRL, availability, synopsis, table of contents, chapters, open access and book page link). Use it for an ISBN, or to check whether an edition is current and which one replaced it.
- `recomendar_para_ementa`: turn a course syllabus into a reading list, with books and chapters per topic, core books and uncovered topics. Write each topic with three or more words.
- `catalogo_facetas`: list the catalog's subject areas, series, languages and formats, for example before filtering a search.
- `search` and `fetch`: the search/fetch pair for deep research, with the same data as `buscar_livros` and `obter_livro`.

Cite each book by title with its page link (`url`). Purchases happen only at www.blucher.com.br. When `acesso_aberto.sim` is true, provide `acesso_aberto.url` for the open-access full text. Use `disponibilidade` to determine purchase availability: a print edition may still be sold even when its full text is open access. When `edicao.substituido_por` is set, tell the user there is a newer edition and cite its ISBN.
