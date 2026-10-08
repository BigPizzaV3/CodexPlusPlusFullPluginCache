# Federal (non-tax) — research methodology

The fachliche order for a federal private/public-law question (OR, ZGB,
StGB, BGG, federal public law) with no clear cantonal layer. Runs on the
**`lexplorer-law`** MCP — mechanics live in `tools/lexplorer-law.md`; pull it
when you run a step. Case-law-heavy questions ("gibt es Rechtsprechung
zu…", a known reference) are handled in more depth by
`methodology/case-law.md` — this file is the statute-first entry point.

## "Was sagt Art. X?"

1. `get_article("<abbr>", "<num>", language)` — full text incl. heading.
   Not found → the act may not be among the 4'816 loaded (check error
   hint) → say so and point to the official publication.
2. A bare article text is scaffold, not an answer (the user is a jurist).
   Immediately bridge to interpretation: step 3.

## "Rechtsprechung zu Art. X" (the statute→case-law bridge)

1. `get_article_case_law(code, art, sort="citations", limit=10)` → leading
   cases (authority-ranked via citation graph).
2. `get_article_case_law(code, art, sort="date_desc", limit=5)` → newest
   applications (currency).
3. For the 2–3 most relevant: `nav_list_sections` → read regeste/summary →
   pinpoint the E. that actually construes the article:
   `search_hybrid(vector_query="<the interpretive question>",
   keyword_query="Art. X <code>", decision_id=<id>)`.

## Concept → which article?

`search_articles(vector_query="<concept sentence>", keyword_query="<term>",
language="de")` → candidate articles → verify by reading → then bridge to
case law as above.

## Targeted vs open

Targeted ("find the BGE about X", "is there a Leitentscheid on Y") → jump to
`methodology/case-law.md` §Targeted. Open ("wie entscheidet das BGer
bei…") → `methodology/case-law.md` §Open, staged Leitentscheide-first.

## Default order (open questions)

1. **Norm-First** — read the governing article IN FULL (`get_article`),
   including the second Halbsatz and neighbouring articles
   (`nav_law_toc`) — the most common failure is a case-law section built
   on a half-read norm.
2. **Leitentscheide** — `find_leading_cases(topic, law_code?, article?)`
   and/or `search_hybrid(…, court="bge")`. An on-point BGE is the citation
   exams, Musterlösungen and practitioners expect.
3. **Recent BGer (~5 years)** — `search_hybrid(…, court="bger",
   year_from=<current year − 5>)` for current practice.
4. **Full corpus** — unrestricted `search_hybrid` if stages 2–3 yield
   nothing on-point; widen/narrow via filters.
5. **Materialien** — `get_article_purpose(law, art)` /
   `search_materialien` for ratio legis / Gesetzgeber-Argumente where the
   question turns on interpretation or history.
6. **Web search** — verification only, official domains (fedlex.admin.ch,
   bger.ch).

For the verdicts that will carry the synthesis, read the Erwägungen (not the
Sachverhalt) via `read_chunk` — never cite from `preview`. Keep statute /
case-law reasoning / application to the facts separate in your notes.
Close with currency: `get_citing_decisions(id, since_date=<decision date>)`.

## Out of scope here

Historical versions (`as_of`), cantonal statutes, Kommentare/scholarship →
the official publication / web, flag explicitly. Cantonal statutes stay on the legacy path —
see `methodology/cantonal.md`.

If the question turns out to have a cantonal layer → switch to
`methodology/cantonal.md` (tax norms and practice: the separate Lexplorer Tax plugin).
