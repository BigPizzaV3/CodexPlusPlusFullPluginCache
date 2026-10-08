# Tax — research methodology

The *fachliche* order for a Swiss tax question — DBG, MWSTG, StHG, VStG, Emissionsabgabe, cantonal Steuergesetze, Steuerbücher, ESTV-Kreisschreiben, §-lookups. This file says **what to look for, in what order, and why**. For **how** to run each tool, pull the linked tool guide into context at that step.

## First: targeted or open?

- **Targeted question** → jump straight to the relevant step, skip the rest.
  - "Was sagt § X StG <KT>?" / "wo steht … im MWSTG?" → step 4 (statute, `tools/tax-mcp.md`).
  - "Gibt es ein BGer/Leitentscheid zu …?" → step 2 (*(Urteils-Recherche: braucht den separaten **Lexplorer Legal**-Connector, falls verbunden; sonst Web-Verifikation auf bger.ch/bvger.ch.)*).
  - "Gibt es einen Kommentar zu …?" → step 1 (`tools/tax-mcp.md`).
  - **User pastes/quotes a literature title, or asks for the "Grundsätze / Lehre / Dogmatik / Konzept" of a topic** → step 1 first: `search_chunks_semantic` on the `Lexplorer Tax MCP` with `filter_category="08-institut-fuer-law-und-economics"`, query = the distinctive title/topic tokens. Use descriptive tokens, not the verbatim full title; if a copied title returns nothing, cut to 2–3 core nouns and retry.
- **Open research question** → run the default order below. Stop once the answer is complete, but completeness for an open question always means at least one interpretive source (step 1 Lehre, step 2/3 Rechtsprechung, or Verwaltungspraxis) — never statute text alone.

Set scope early: which **layer** (DBG / StHG / MWSTG / VStG / Stempelabgaben / cantonal), which **canton** (`CH` for federal), and the source **language** (DE default; FR for GE/VD/JU/NE + French BE/VS/FR; IT for TI + Italian GR).

## Default order (open questions)

**1 — Kommentar / Lehre.** Is there a relevant commentary or doctrine on the point? This is often the most directly useful source and, for any open or doctrinal question, a **mandatory step you may not skip** even if statute and a BGer hit already feel sufficient. Search the ILE-HSG Lehre on the **`Lexplorer Tax MCP`** — `search_chunks_semantic(query=<2-4 Konzept-Tokens>, filter_kanton="CH", filter_category="08-institut-fuer-law-und-economics")`. (Lehre lives in the Tax MCP.) Capture the `— Autor:innen:` marker for the citation. Mechanics + the lexplorer-deeplink bridge for citing: `tools/tax-mcp.md`. A good Kommentar reframes everything that follows.

**2 — Bundesgericht.** Are there relevant BGer judgments? Search on
**Lexplorer Legal** (separater Connector): `find_leading_cases(topic=…, law_code=…, article=…)` first
(Leitentscheide ranked by citation authority), then `search_hybrid`/
`search_keyword` with `year_from` for a **last-5-years** pass. `is_leitentscheid`
in the hits shows BGE status. Mechanics in *(Urteils-Recherche: braucht den separaten **Lexplorer Legal**-Connector, falls verbunden; sonst Web-Verifikation auf bger.ch/bvger.ch.)*.

**3 — Bundesverwaltungsgericht.** If sensible — and in tax it usually is, since the BVGer is the central instance below the BGer (especially MWST/VST) — search BVGer judgments on Lexplorer Legal (separater Connector) with `court="bvger"` (keyword/FTS + summary vectors). *(Urteils-Recherche: braucht den separaten **Lexplorer Legal**-Connector, falls verbunden; sonst Web-Verifikation auf bger.ch/bvger.ch.)*.

**4 — Gesetz (statute) + Verwaltungspraxis.** Look up what the law actually says, and the binding practice on it. **The `Lexplorer Tax MCP` owns both:** §/Art full text + federal tax acts (`filter_category="01-gesetzgebung"` / cantonal Steuergesetze) and the ESTV/SSK-Kreisschreiben, MWST-Infos, Stempelabgaben-Praxis (`filter_category="02-verwaltungspraxis"`). The Kreisschreiben is often the single most directly applicable source (Indizwirkung) — search it deliberately, do not treat it as an afterthought. Use the navigation to orient first (which Erlass / which KS), then read the full chunk. How: `tools/tax-mcp.md`.

**5 — Cantonal trigger (judgments).** If at any point the question turns out to be **canton-specific**: search on Lexplorer Legal (separater Connector) with that canton's court codes (`court="zh_…"` etc., full list via `nav_tree()`). *(Urteils-Recherche: braucht den separaten **Lexplorer Legal**-Connector, falls verbunden; sonst Web-Verifikation auf bger.ch/bvger.ch.)*.

**6 — Cantonal norms, in parallel with step 5.** At the same time, look up the **cantonal norms** for that canton via the `Lexplorer Tax MCP` (`filter_kanton`). Steps 5 and 6 run together — cantonal case law and cantonal statute text answer the same canton-specific question from two sides. `tools/tax-mcp.md`.

**7 — Web search.** Only as verification or for a genuine coverage gap, on official domains (fedlex.admin.ch, bger.ch, bvger.ch, estv.admin.ch, lexfind.ch).

## Keep distinct (the #1 tax-synthesis failure)

- Which layer governs: DBG (direct federal) · StHG (harmonization) · MWSTG (VAT) · VStG (withholding) · cantonal StG/practice.
- Substantive requirement (does the rule apply?) vs procedural posture (which authority, which stage) vs review stage (what is actually being reviewed by which court).
- Statute text vs administrative practice (Kreisschreiben: Indizwirkung, not binding on courts) vs case-law holding vs application to the facts.

## Carry forward
Note which layer is decisive, the controlling norm(s) with `parent_doc_url`, the leading BGer/BVGer with UUIDs, any einschlägiger ILE-Kommentar with chunk-links **and its author(s)** (the `— Autor:innen:` marker — needed for the citation), and the holding in 1–3 sentences → `synthesis.md`.
