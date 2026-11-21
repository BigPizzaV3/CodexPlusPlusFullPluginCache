# French codes (@fr)

`@fr` holds codified LEGI codes, each article with its versions. Coverage
is partial: some large codes (for example Code du travail, Code pénal) may be
missing or incomplete, so check `browse_taxonomy` before telling the user an
article does not exist. The scope has `search`, `get_article`,
`list_articles` and `browse_taxonomy` only: no `resolve`, `get_status`,
`get_related`, structure, non-codified laws, decrees or case law.

## 1. Get the exact code title

Code titles are matched exactly, including capitals and accents. When unsure,
call `browse_taxonomy(scope: "@fr", limit: 100)` — the default limit of 50
does not list every code — and copy `code_title` from `items[]` (for example
`Code civil`, `Code de commerce`). `in_force_count` shows how much of a code
is current.

## 2. Find the article

- Known number: `get_article(uri: "@fr/code/Code civil", article: "1240")`.
  Formats: `1240`, `L225-102-1`, `Article L. 225-102-1`, `R. 431-16`.
- Topic: `search(query: "<question in French>", scopes: ["@fr"])`. Results are
  chunks, so the same article can appear twice; the search cannot be limited
  to one code.
- Browse a code: `list_articles(uri: "@fr/code/Code de commerce", limit: 500,
  offset: 0)`. There is no `has_more`; compare `offset + limit` with `total`.
  `limit` above 500 is rejected.

A missing article comes back as `upstream_4xx`; check the number format and
the code title before concluding it does not exist.

## 3. Read status and dates from the article

The article response carries the version's own window:

- `status`: `VIGUEUR` = in force. `MODIFIE`, `ABROGE`, `TRANSFERE`,
  `ANNULE`, `PERIME`, `VIGUEUR_DIFF` (in force later) are not current text.
- `date_debut` / `date_fin`: validity window; `date_fin` `2999-01-01` means
  open-ended, not a real date.
- Without a date the tool returns the in-force version, or the latest one —
  which may be repealed. Always report `status`.

## 4. Past wording

`get_article(..., as_of: "YYYY-MM-DD")` returns the version with
`date_debut ≤ as_of < date_fin`. A search URI pinned with `/v/{LEGIARTI}`
ignores `as_of`; rebuild `@fr/code/{code}` and pass `article` and `as_of`.
There is no timeline of all versions — say so if asked when an article
changed.

## 5. Cite

Use `citation` ("Article 1240 du Code civil") and `legifrance_url`. Status is
as recorded in LEGI; the connector cannot verify it independently.
