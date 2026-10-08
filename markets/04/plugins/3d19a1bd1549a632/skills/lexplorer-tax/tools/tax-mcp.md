# Tool guide — `Lexplorer Tax MCP`

How to operate the `Lexplorer Tax MCP` (`mcp-tax.lexplorer.ch`). **This is the single source for everything tax except court judgments:** §/Art full text, cantonal Steuergesetze, Steuerbücher, federal tax acts (DBG/MWSTG/StHG/VStG), the full Verwaltungspraxis (ESTV/SSK-Kreisschreiben, MWST-Infos, Stempelabgaben) **and** the ILE-HSG Lehre/Doktrin — 27 cantons + Bund. Court judgments (BGer/BVGer/cantonal) come from the separate **Lexplorer Legal** connector (if connected); everything else for tax is here.

This server is **navigation-rich** — lean on the hierarchy to orient before you search, rather than blind full-text queries. Tool names are unprefixed here; at runtime they carry the `Lexplorer Tax MCP:` prefix. If a name is rejected, list the server's tools to confirm — do not invent tools.

## Content map (federal `CH` categories)
Use `filter_category` to target the right layer; per-canton the same logic applies (Steuergesetze + Steuerbücher under each Kanton).
- `01-gesetzgebung` — federal tax statute text (DBG, MWSTG, StHG, VStG, StG/Stempel).
- `02-verwaltungspraxis` — the practice that used to be the `iletax_*` filters: **ESTV Kreisschreiben DBG**, **ESTV DBG-Fachinformationen**, **ESTV Verrechnungssteuer** (VST), **ESTV Stempelabgaben** (Emissions-/Umsatz-/Versicherungsabgabe), **SSK Kreisschreiben** (interkantonal/StHG), **ESTV MWST-Publikationen** (MWST-Infos/Brancheninfos), SSK-Analysen.
- `06-kommentierungen` — Gesetzeskommentierungen.
- `08-institut-fuer-law-und-economics` — the ILE-HSG Lehre that used to be the `ile_*` filters: **Forum für Steuerrecht (FStR)**, **Schriftenreihe**, **Seminarunterlagen**, **Working Papers**, **Lehrbuch Steuerrecht**.

## Orientation first (use the navigation)
Cheap nav calls beat guessing. Pick what fits:
- `get_kanton_navigation_md(kanton)` — one-call markdown overview of all sources + categories + chunk-counts in a canton.
- `nav_tree(kanton?, max_depth=2)` — JSON tree kanton → category → source (1 call instead of several `nav_list_*`).
- `nav_find(pattern, scope="document")` — "where is the MWSTG / Steuerbuch Bern / KS Nr. 5a?" → `doc_id` + `breadcrumb` + `chunk_count`.
- `nav_list_categories / nav_list_sources / nav_list_documents / nav_list_chunks` — step down the hierarchy when you need the exact source or article list.

`chunk_count > 0` = indexed and searchable. `chunk_count = 0` = crawled but not embedded → coverage fallback below.

## Searching
- **Lehre / Doktrin / Kommentar** (ILE) → `search_chunks_semantic(query="<2-4 Konzept-Tokens>", filter_kanton="CH", filter_category="08-institut-fuer-law-und-economics")`. Doctrine is conceptual — prefer semantic. If the user pasted a title, cut it to 2-3 distinctive nouns.
- **Verwaltungspraxis** (Kreisschreiben/MWST-Info/SSK) → `search_chunks_semantic(query, filter_kanton="CH", filter_category="02-verwaltungspraxis")`; or `nav_find` the specific KS then `filter_source_id`.
- **Named §/Art** → `search_chunks_keyword(query="§ 31", filter_kanton="ZH")` (optionally `filter_source_id` to target one Erlass after `nav_find`).
- **Concept in statute** → `search_chunks_semantic(query="<2-4 Konzept-Tokens>", filter_kanton)`.
- **Mixed (§ + concept)** → `search_chunks_hybrid(query, filter_kanton)`.

Always set `filter_kanton` for canton-specific questions (prevents cross-canton bleed). For federal, `filter_kanton="CH"`. Inspect the top 3–5 `breadcrumb` values before fetching content; never answer from `preview` alone.

### Keyword (FTS) tokenization
`search_chunks_keyword` / `_hybrid` use Postgres `websearch_to_tsquery` with an **AND default** — every token must match, so a raw natural-language question returns 0 hits. **Tokenize to 2–3 core tokens (nouns + norm number); drop verbs/filler.** E.g. "Wann ist eine Holding-Spaltung steuerneutral?" → `Spaltung Holding`; "Wie wird die Quellensteuer in Genf berechnet?" → `Quellensteuer Berechnung`. Quotes = exact phrase; `OR` = either; `-token` = exclude. 0 hits → reduce tokens or switch to `search_chunks_semantic`.

## Reading + citing
- `get_chunk_content(chunk_id)` → `content` (full §/section) + `parent_doc_url` (source PDF) + signed PDF URL.
- `get_document_slice(doc_id, slice=0)` → read a large or unsplit document in pageable slices (use when a doc isn't chunked or you need the whole thing).

Three citation shapes depending on what the chunk is:
- **Statute / cantonal norm:** `[<§/Art + Erlass>](<parent_doc_url>)`. When a § exists in several Erlasse, disambiguate via `parent_doc_title`/`breadcrumb` first (e.g. § 31 StG vs § 31 ESchG vs § 31 StV). Flag any repealed provision (in-force filter defaults to `true`).
- **Verwaltungspraxis** (ESTV/SSK-Kreisschreiben, MWST-Info): `[KS Nr. NN ESTV, Ziff. X](<parent_doc_url>)` — these usually have a real estv.admin.ch / ssk PDF in `parent_doc_url`. If it is `null`, cite by reference (KS Nr. + Ziffer) without a link.
- **ILE Lehre/Doktrin:** cite via the lexplorer bridge below (its `parent_doc_url` is usually `null`).

## ILE Lehre/Doktrin — cite via the lexplorer bridge
ILE-HSG content (category `08-institut-fuer-law-und-economics`) has no usable `parent_doc_url`, but the original ILE IDs are preserved verbatim, so reconstruct the app.lexplorer.ch deep link:
- the number after `id_` in a chunk's `chunk_file` (`chunk_0036_id_9851.json` → `9851`) **is** the lexplorer `chunkId` → `e_chunks`;
- the `id_NNN` in the `segment_…_id_NNN` path is the lexplorer document `id` → `e_id`.

Build `https://app.lexplorer.ch/suche?e_chunks=<id1>,<id2>&e_sys=ile` (collect several chunk_file IDs of the same article, comma-joined) or `…?e_id=<NNN>&e_sys=ile` as the document-level fallback. **Caveat (Stand Juni 2026):** brand-new ILE content (e.g. the FStR 2026 Jubiläumsnummer) is in this server but may not yet be indexed in the app, so a bridged link can occasionally fail to resolve. For established (pre-2026) ILE it resolves reliably. Verify this mapping still holds if the ILE↔Tax-MCP integration changes.

## Authors of ILE articles
ILE article chunks carry an explicit author marker, usually at the end of the intro chunk (and repeated on section chunks): `— Autor:innen: <Namen>`. Capture it when reading — it feeds the author citation rule in `synthesis.md`.

## Cross-canton comparison
One `search_chunks_semantic` per canton in parallel, same query, `filter_kanton` on every call; collect each canton's top §/`parent_doc_url`; present a table with one Markdown link per canton.

## Coverage-gap fallback
If `nav_find` returns 0 hits or `chunk_count = 0`: get `parent_doc_url` via `nav_list_documents(source_id)` and follow the external source PDF (fedlex.admin.ch, estv.admin.ch, ssk-csi.ch, kantonale lex, lexfind.ch — you have web access). If the document is not in the corpus at all, `web_search` on those official domains.
