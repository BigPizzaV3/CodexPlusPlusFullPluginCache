# Tool guide — Lexplorer Law MCP

**Citing links:** Every decision/article/cantonal-law result carries a `lexplorer_url` (public, branded source page on law.lexplorer.ch with the official source linked). Use it as the clickable link when citing; never invent URLs.

Mechanics for the **Lexplorer Law MCP** (`https://law.lexplorer.ch`),
referenced below simply by tool name. 29 tools; every
search hit carries `chunk_id`, `decision_id`, `section`, `key`, `breadcrumb` —
one hit = one navigation entry point. Tool names at runtime carry the
connector's own prefix (e.g. `Lexplorer Law MCP:`).

## The tree and its IDs

```
bger|bge / {year} / {decision_id}
  #header/-                Rubrum: Besetzung (judges), parties, Gegenstand — FTS only
  #regeste/-               official headnote (BGE ~100%, plain BGer sparse)
  #summary/facts@de|fr|it  Lexplorer AI summaries (where matched)
  #summary/contemplation@… #summary/verdict@…  #summary/combined@de
  #facts/A, B, A.a …       Sachverhalt paragraphs ('-' = unsplit old decision)
  #considerations/2.4.1    ONE chunk per numbered Erwägung (own text only,
                           children are separate chunks; parent_key/depth set)
  #verdict/1, 2 …          Dispositiv-Ziffern
```

`decision_id` formats: `bger_4A_123_2024` (docket 4A_123/2024),
`bge_BGE_140_III_86` (BGE citation). All decision_id parameters also accept
loose forms ("BGE 140 III 86", "4A_123/2024") — resolved via docket_norm.
Construct chunk IDs directly when you know the E.-number — reading beats
searching.

## Navigation

- `nav_tree()` → decision counts per year **and `courts`**: every court code with canton and count (the values the `court=` filter accepts); `nav_tree(year=2024, court="zh_obergericht")` → that year's decisions (max 100), optionally of one court.
- `nav_list_decisions(year?, chamber?, legal_area?, language?, limit, offset)` —
  filterable listing, `chamber`/`legal_area` are substring matches
  (e.g. chamber="Zivilrecht", legal_area="Vertragsrecht").
- `nav_list_sections(decision_id)` — the decision's "folders" + chunk counts +
  `cites_out`/`cited_by` + metadata. Start here after any lookup.
- `nav_list_chunks(decision_id, section, parent_key?)` — keys/previews in
  reading order; `parent_key="2"` lists 2.1, 2.2, … (drill-down).
- `nav_find(pattern)` — docket/BGE-ref lookup, typo-tolerant ("BGE 140 III 86",
  "4A_123/2024", partial dockets). ALWAYS use this to resolve a reference to a
  `decision_id`; never guess IDs.

## Search — three tools, one contract

Common filters: `language` (de|fr|it), `section`, `year_from/to`, `chamber`,
`legal_area`, `decision_id` (search WITHIN one judgment = pinpoint finding),
`court` (`"bge"` = Leitentscheide only, `"bger"` = plain judgments only,
`"bvger"`/`"bstger"`/cantonal codes like `"zh_obergericht"` — full list via
`nav_tree()`; non-BGer courts are keyword/FTS + summary-vector only).
All hits include `preview` (300 chars — orientation only, never cite from it),
`court` and `is_leitentscheid` — prefer presenting BGE hits for doctrine.

- `search_semantic(query, …)` — conceptual/natural-language. Coverage limited by
  `embed_frontier_year` (see corpus_status); below it: 0 hits ≠ nothing exists.
- `search_keyword(query, …)` — websearch syntax ("phrase", OR, -exclusion), **AND default**:
  tokenize to 2–4 core tokens (nouns + norm numbers), drop verbs/filler.
  `"exact phrase"`, `OR`, `-exclude`. Diacritics-insensitive (unaccent), per-
  language stemming. On 0 hits the server retries with OR (`or_fallback: true`
  in the response — treat as low-precision recall).
  Returns rich metadata: `total_matches`, `distinct_decisions`,
  `summary_by_year` (when more matches than returned — this IS the trend
  analysis), per-hit `highlight` (<mark>…</mark>) and `cited_by` (citation
  authority; ranking already blends it in).
  Docket-pattern queries short-circuit to direct lookup (`is_docket_lookup`).
- `search_hybrid(vector_query?, keyword_query?, …)` — RRF merge; the queries are
  **independent**: `vector_query` = full natural-language sentence,
  `keyword_query` = exact anchors ("Art. 271 OR", a term of art). Provide one or
  both. Statute refs in either query additionally pull authority-ranked case law
  from the citation graph (`matched_by: ["statute"]`). Best default for open
  questions; check `matched_by` to see which signal carried a hit.

## Reading

- `read_chunk(chunk_id, context=1)` — full chunk text + n neighbor previews +
  the decision's cited statute articles. THE citation-grade source.
- `read_section(decision_id, section, offset, limit≤30000)` — whole section as
  continuous text (keys inline as [2.4.1]); paginate via offset.
- `read_full_text(decision_id, offset, limit≤30000)` — raw judgment text.

## Citation graph & composites

- `get_citing_decisions(decision_id, since_date?, min_confidence=0.5, limit)` —
  incoming citations, newest first, with regeste previews. THE
  "still good law?" tool. `is_prior_instance=true` edges = Instanzenzug.
- `get_cited_decisions(decision_id, …)` — what this judgment relies on.
- `confidence` = docket-resolution certainty (0.5 default floor; 0.99 = exact).
- `find_leading_cases(topic?, law_code?, article?, language?, year_from/to?, limit)`
  — leading cases ranked relevance × citation authority; `matched_by` shows the
  carrying signal (statute/keyword/semantic). First stop for "what is THE case
  on X?". Combine topic + article to focus a norm on a fact pattern.
- `verify_citations(refs[])` — batch check every citation in your draft:
  exists?, canonical Zitierform (BGE sibling preferred), cited_by. MANDATORY
  final gate before answering.
- `get_case_brief(decision_id)` — one-call orientation: metadata, regeste,
  AI summary, key statutes, citation impact, structure map with the E.-numbers
  worth reading. Use before deep-diving; cite from read_chunk, never the brief.

## Statutes (4'816 federal acts — complete SR)

- `nav_list_laws(query?)` — the loaded acts: SR number, abbr de/fr/it, title,
  consolidation date, article count. Start here when unsure of the abbreviation.
- `nav_list_articles(law, language, offset, limit≤300)` — table of contents of
  one act in numeric order (`40 → 40a → 40b`), with previews. Use it to browse
  neighboring articles around a hit.
- `get_decision_articles(decision_id, limit)` — statute articles a judgment
  cites (mention_count-sorted). The judgment→law bridge; reverse of
  get_article_case_law.
- `get_article(abbreviation, article, language)` — `get_article("OR","271")`.
- `search_articles(keyword_query?, vector_query?, language?, sr_number?)` — RRF
  like search_hybrid. Article embeddings may lag (corpus_status →
  articles_embedded); keyword always works.
- `get_article_case_law(law_code, article, sort="citations"|"date_desc", limit)`
  — judgments applying the article; `sort="citations"` = leading cases,
  `sort="date_desc"` = newest application.

## Kantonale Erlasse (Erlass-Suche + Artikeltext)

- `search_cantonal_law(query, canton?, language="de", limit=10, vector_query?,
  systematics_prefix?)` — sucht im Katalog der geltenden kantonalen Erlasse
  (~21'600, alle 26 Kantone + Bund): `query` per Volltext über Titel,
  Abkürzung und Systematik, `vector_query` zusätzlich semantisch
  (Konzept-/Themenfragen wie "Grenzabstand beim Bauen" statt exaktem Titel),
  auch über bereits abgerufene Artikeltexte. Standardmässig fliesst zusätzlich
  eine Volltextsuche im Erlasstext selbst ins Ranking ein (findet z.B.
  "Ausnützungsziffer" in der ABV ZH, obwohl das Wort in keinem Titel steht).
  Treffer: `hit_type` "law" (Erlass) oder "article" (Artikeltext-Ausschnitt).
  `systematics_prefix` filtert auf einen Systematik-Pfad (Browsen nach
  Rechtsgebiet). `include_live_fallback=False` beschränkt die Suche auf den
  Katalog (schneller, aber ohne Treffer im Erlasstext).
- `get_cantonal_law(<ID aus search_cantonal_law>, article?, language="de")` —
  ohne `article`: Metadaten, Versionsgeschichte und **`systematics_siblings`**
  (Nachbar-Erlasse im selben Systematik-Knoten, z.B. alle Bauverordnungen
  neben dem PBG ZH). Mit `article=`: der **Artikeltext direkt** (Überschrift +
  Inhalt). Der erste Artikelabruf eines Erlasses dauert etwas länger, weitere
  Artikel desselben Erlasses kommen sofort. Statt der ID geht auch eine
  Referenz `"KANTON:systematische_nummer"` (z.B. `"ZH:700.1"`, `"VD:700.11"`).
- **Qualitäts-Hinweis:** Ist die amtliche Vorlage ein Scan oder ohne
  erkennbare §/Art.-Nummerierung, liefert das Tool keinen Artikeltext, sondern
  `quality_flag` (`pdf_scan` bzw. `no_article_structure`) und unter `urls` die
  Links zur amtlichen Fassung — dann diese öffnen bzw. verlinken.
- **Grenzen (ehrlich benennen):** Die Artikel-Aufteilung ist Best-Effort: Bei
  sehr unüblicher Formatierung kann eine Überschrift fehlen, der Artikeltext
  selbst ist verlässlich. Ganz neue Erlasse können im Katalog kurz fehlen.
  Keine Rechtsprechungsverknüpfung und keine Materialien zu kantonalen
  Erlassen.

## Materialien (Botschaften, amtlicher Wortlaut)

- `get_article_purpose(law, article)` — ratio legis: wörtliche Botschaft-Absätze
  zum Artikel (Zitierform "Botschaft, BBl {Jahr} {Seite}"). Abdeckung: neuere
  Botschaften (2021+), 25 Bundesgesetze; hint nennt vorhandene Dokumente.
- `search_materialien(keyword_query?, vector_query?)` — Suche über alle
  Botschaft-Absätze (Gesetzgebungsgeschichte, Würdigungs-Argumente).
- `read_botschaft(para_id, context)` — voller Absatz + Nachbarn
  (`bbl_2025_1478#p782`), zitierfähige Quelle.

## Meta

- `corpus_status()` — decisions/chunks/embedded counts, `embed_frontier_year`,
  citation edges, laws/articles. Call it when semantic recall seems off, and
  before promising semantic coverage of old years.

## Recipes (bewährte Recherche-Abläufe)

- **Pinpoint a claim in a judgment**: `search_hybrid(vector_query=<claim>,
  decision_id=<id>)`; read the top chunk; neighbors via `context=2`.
- **Trend**: `search_keyword(<tokens>)` → `summary_by_year` + `total_matches`.
- **Leading cases on a topic**: `find_leading_cases(topic=…, law_code/article=…)`
  — first-class tool; falls back to `search_hybrid` + `cited_by`-sort only for
  exotic filter combos.
- **Judge/composition**: `search_keyword("<name>", section="header")`; combine
  with `year_from/to` or `chamber`. Counts via `total_matches`.
- **Appeal chain**: `get_cited_decisions(id)` filtered to
  `is_prior_instance=true` (downwards) + `get_citing_decisions(id)` same flag
  (upwards).
