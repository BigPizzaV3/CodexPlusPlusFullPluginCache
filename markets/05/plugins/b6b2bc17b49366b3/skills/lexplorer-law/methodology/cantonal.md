# Cantonal administrative law — research methodology

For cantonal/communal **administrative** law (school, police, fees, public-law, building/zoning/permit/municipal). Cantonal **tax** norms and practice are not here — they live in the separate Lexplorer Tax plugin; cantonal tax *judgments* are searched here like any other cantonal judgment.

Mechanics are split by source type:
- **Cantonal judgments** → the `lexplorer-law` corpus (~100 kantonale
  Gerichte/Instanzen, alle Kantone; keyword/FTS + summary vectors — full
  text of Erwägungen not semantically searchable outside BGer/BGE). Filter
  with `court=<kantonscode>` (all codes with canton + count via `nav_tree()` → `courts`, e.g.
  `zh_obergericht`, `ge_gerichte`). `tools/lexplorer-law.md`.
- **Cantonal/communal statutes** → **`search_cantonal_law`/`get_cantonal_law`
  now run against a local semantic catalog** (~21'600 current acts, all 26
  cantons + CH, embedded + full-text) — `vector_query` finds acts by concept/topic (e.g. "Grenzabstand
  beim Bauen"), not just exact title. `get_cantonal_law(..., article=...)`
  returns the actual article TEXT (not just a URL); also adds
  `systematics_siblings` for browsing neighbouring acts. By default each search
  also matches inside the act texts; `include_live_fallback=False` limits it to
  the catalog. `tools/lexplorer-law.md`.

## Clarify first
A cantonal search with the wrong canton is the worst failure mode (confidently wrong). Before searching, make sure these are clear — ask once if not: **canton** (always); **municipality** (zoning, permits, communal fees); **project/authority context**.

## Default order
1. **Federal baseline** — what federal law requires regardless of canton (constitutional rights, harmonization, federal public-law minimums). `methodology/federal.md` / `tools/lexplorer-law.md`.
2. **Cantonal judgments** — `search_hybrid(…, court=<kantonscode>)` / `search_keyword(…, court=<kantonscode>)`, narrowed to the canton in question. For doctrine questions still check for a federal Leitentscheid first (`find_leading_cases`) — federal case law outranks cantonal practice in the citation hierarchy; cite cantonal practice only when the question is cantonal or no federal case exists. `tools/lexplorer-law.md`.
3. **Cantonal/communal statute** — `search_cantonal_law(query, canton, language, vector_query?)` then `get_cantonal_law(<ID from the search>, article?, language)` on `lexplorer-law`; article text is returned directly when extractable — cite the returned article text (or, if a `quality_flag` like `pdf_scan`/`no_article_structure` appears, the source URL/PDF instead), never reconstruct article text from memory.
4. **Web search** — verification, official domains.

## Keep distinct
Federal baseline (same everywhere) · cantonal statute/practice (this canton) · communal layer (this municipality). In the answer, say explicitly what is federally required, what is canton-specific, and what is municipality-specific — that tells the user which parts transfer elsewhere.
