# Reproducible literature searching — pediatric otolaryngology

1. Clarify PICO (effects), PIRD (diagnostic tests), PECO (exposures), or PCC (scoping).
2. Define pediatric inclusion using explicit ages and setting; note ambiguity of `child*` or `pediatric*` terms and need for sensitivity.
3. Build concepts with OR within each block and AND between blocks; prefer specific MeSH headings once verified in the current MeSH browser, and include text words. Avoid requiring all outcomes in search queries (may reduce sensitivity).
4. Apply date, language and design filters only if justified and transparent; children's evidence may be sparse. Don't automatically filter `Humans` or `Child` in a way that drops unindexed citations.
5. For reviews, record database, platform, complete syntax, dates searched, counts actually observed, deduplication and peer-review of search when possible (PRESS).
6. Use PubMed direct query links as **search links**: percent encode the whole string, then append to `https://pubmed.ncbi.nlm.nih.gov/?term=`. Do not cite the link as an article, or claim an observed count without running it.

## Illustrative PubMed string: OME and tympanostomy (not guaranteed finalized MeSH strategy)

```text
(("otitis media with effusion"[tiab] OR "glue ear"[tiab] OR "otitis media with effusion"[MeSH Terms]) AND (tympanostom*[tiab] OR "ventilation tube*"[tiab] OR "tympanostomy tubes"[MeSH Terms]) AND (child*[tiab] OR pediatric*[tiab] OR paediatric*[tiab] OR infant*[tiab]))
```

This is a **draft**, not a validated exhaustive strategy. Confirm all official MeSH terms, wildcard behavior and database syntax at run time. Avoid fabricating search results, dates or flow counts.

## Distinguish evidence sources
- PubMed/MEDLINE: https://pubmed.ncbi.nlm.nih.gov/ (NLM user guide https://pubmed.ncbi.nlm.nih.gov/help/)
- Cochrane and CENTRAL: https://www.cochrane.org/handbook ; consult available access
- ClinicalTrials.gov and trial registries may uncover unpublished or ongoing studies.
- PROSPERO eligibility is subject to current rules; don't promise registration without checking.
- Embase, CINAHL, Scopus, Web of Science: don't pretend access where none exists.

Document original PubMed update guide last updated September 30, 2026, at direct-opened https://pubmed.ncbi.nlm.nih.gov/help/ (checked 2026-10-28). Website may change; recheck when executing a live search.
