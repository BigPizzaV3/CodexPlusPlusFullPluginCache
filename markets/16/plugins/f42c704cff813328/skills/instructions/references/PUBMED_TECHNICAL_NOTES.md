# PubMed links, similar articles and open access caveats

## Search links
- PubMed basic search: `https://pubmed.ncbi.nlm.nih.gov/?term=ENCODED_QUERY`.
- Direct Clinical Queries interface: `https://pubmed.ncbi.nlm.nih.gov/clinical/` (interactive). To provide ten ready-made *search-result* links, use the ten NLM Boolean-equivalent filters in PUBMED_CLINICAL_QUERIES.md.
- Date range (Publication Date): `YYYY/MM/DD:YYYY/MM/DD[dp]`. For reproducibility, save the literal range and run date; dynamic "last 3 years" windows are not stable if revisited.
- Sort=Date: `&sort=date` is a user preference, not evidence ranking; search indexing may differ from publication time.

## Similar articles
Official PubMed individual PMID page gives a "Similar articles" section and "See all similar articles" link. A legacy result link format is `https://pubmed.ncbi.nlm.nih.gov/?linkname=pubmed_pubmed&from_uid=PMID`; it can change, so validate before promising availability. The NLM E-utilities related link type is `pubmed_pubmed` (not a full text source).
See https://pubmed.ncbi.nlm.nih.gov/help/#similar-articles and https://www.nlm.nih.gov/dataguide/eutilities/utilities.html .

## Full text licensing
PubMed indexes abstracts, records, full-text links. `free full text[sb]` is not equal to open license and does not prove downstream reuse rights; `NOT free full text[sb]` does not prove paid access, and may include missing links/metadata. Neither publisher paywall nor library entitlements can be inferred from this filter alone. Offer legitimate publisher, PubMed Central, institutional library/interlibrary loan, author manuscripts, and avoid paywall circumvention.
