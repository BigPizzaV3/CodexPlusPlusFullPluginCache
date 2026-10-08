# Methodology — case-law questions

## Targeted (a reference is known)

"BGE 140 III 86", "4A_123/2024", "der Mietrechts-Entscheid von 2019 zu Eigenbedarf":

1. `nav_find(<reference>)` → decision_id. Multiple matches → pick by date/court,
   say which you picked.
2. `nav_list_sections(id)` → orientation: what exists (summary? regeste?), how
   big, how often cited.
3. Cheapest sufficient read, in this order:
   `#summary/combined@de` (if present) → `#regeste/-` → targeted
   `nav_list_chunks(id, "considerations")` + `read_chunk` of the relevant E.
4. If the user asked about a specific point: `search_hybrid(vector_query=
   <the point>, decision_id=id)` → read the top E. verbatim.
5. **Always close with currency**: `get_citing_decisions(id,
   since_date=<decision date>)` — report newest citing judgments or "keine
   späteren Zitierungen im Korpus".

## Open ("gibt es Rechtsprechung zu…?") — staged: Leitentscheide first

Doctrine questions are answered by **BGE (amtliche Sammlung = Leitentscheide)**;
plain BGer judgments show the current application. Search in stages; move on
only when the stage yields nothing on-point:

0. Formulate BOTH queries before searching:
   - `vector_query`: the full question as one natural sentence (DE is fine).
   - `keyword_query`: 2–4 anchors — norm refs ("Art. 271 OR") + terms of art.
1. **Stage 1 — Leitentscheide:** `find_leading_cases(topic, law_code?, article?)`
   (BGE-boosted, sibling-deduped) and/or `search_hybrid(…, court="bge")`.
   An on-point BGE is the citation exams, Musterlösungen and practitioners expect.
2. **Stage 2 — recent BGer (~5 years):** `search_hybrid(…, court="bger",
   year_from=<aktuelles Jahr − 5>)` — newest developments and current practice.
3. **Stage 3 — full corpus:** unrestricted `search_hybrid`; widen/narrow via
   filters (`language`, `chamber`, `legal_area`, `section="regeste"`) or
   re-tokenized anchors. `or_fallback: true` = weak precision; re-tokenize.
4. **Stage 4 — reference tree (tricky questions):** from the best hits, walk the
   graph: `get_case_brief(id)` → `citation_impact`; `get_cited_decisions(id)` —
   the most-cited / BGE ancestors are usually the doctrine source;
   `get_citing_decisions(id)` — still good law? what refined it? One or two
   hops; prefer nodes with high `cited_by` or `is_leitentscheid=true`.
5. Read `matched_by` on every hybrid hit:
   - only `kw` hits + old years → semantic frontier not reached; trust keyword.
   - `statute` hits → citation-graph candidates, usually the leading cases.
6. Triage by breadcrumb + preview; `read_chunk(context=1)` the 2–4 best. For
   each judgment you cite: regeste or summary read + the specific E. read
   verbatim + `get_citing_decisions` for the central one(s). Cite the BGE form
   when a sibling exists (`published_as_or_procedure` in the brief).

## Language handling

Corpus is de/fr/it. A German query only semantic-matches French chunks weakly —
for exhaustive coverage on important questions run `search_hybrid` once per
language with translated anchors, or filter `language` explicitly and say what
you covered. FTS is diacritics-insensitive; stemming is per-language.

## When the corpus is the wrong one

BVGer/cantonal/EGMR questions ARE covered here (keyword/FTS + summary
vectors, see corpus limits in `tools/lexplorer-law.md`) —
name the coverage gap (semantic frontier, no full-text vectors) rather than
the corpus itself. Genuinely out of scope: Materialien beyond the loaded
Botschaften, Kommentare/scholarship, cantonal **statutes** (→
`methodology/cantonal.md`), tax norms/practice (→ the separate Lexplorer Tax plugin).
Name the gap, answer what the corpus can answer, point to the right source
(official publications / web). Never fake coverage.
