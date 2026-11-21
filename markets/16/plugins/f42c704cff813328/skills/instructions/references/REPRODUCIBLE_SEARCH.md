# Reproducible evidence search — practical protocol

1. Frame research question with PICO/PECO/PIRD/PCC as appropriate. Do not force PICO for qualitative, prevalence or prognostic questions.
2. Record: database/platform; coverage; actual run date (user timezone); language/age/date filters; query; result count only if verifiable; screening inclusion/exclusion; deduplication method.
3. Concept blocks: synonym 1 OR synonym 2 OR controlled vocabulary; intersection: block A AND block B. Identify exclusion operators with care (NOT can hide relevant citations). Consider variant spellings, truncation, initials of disease, generic drugs.
4. PubMed ATM: unquoted plain text often benefits from mapping; quoted phrases and field tags can disable mapping. MeSH-only misses not-yet-indexed articles; supplement with [tiab] when appropriate. Inspect Search Details if accessible; never assert they were inspected when not.
5. Restriction logic: Clinical Queries are screening tools, not comprehensive systematic-review methods. For systematic reviews check MEDLINE/PubMed plus Cochrane CENTRAL, Embase and other suitable sources if available; peer-review search (PRESS); log each update; PRISMA-S and PRISMA 2020 reporting as applicable.
6. Specialty: children, rare diseases, diagnostics require broader/sensitive strategies; add human/age and study-design limits only after explaining loss in sensitivity.
7. Search and appraisal logs: use record template:

| Database | Search date | Verbatim strategy | Limits | Hits (if confirmed) | URL | Verification |
|---|---|---|---|---|---|---|
| PubMed | YYYY-MM-DD | `...` | ... | Not checked | ... | Search-only |

8. PICO example (illustrative): `(infant OR infants OR child OR children) AND (proton pump inhibitor OR omeprazole) AND (gastroesophageal reflux OR reflux)`; translate with MeSH carefully, not automatically assert an exhaustive strategy.

Source: https://pubmed.ncbi.nlm.nih.gov/help/ ; https://www.prisma-statement.org/ (verify version before citing).
