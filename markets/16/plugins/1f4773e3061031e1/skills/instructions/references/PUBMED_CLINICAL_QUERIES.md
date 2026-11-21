# 10 PubMed Clinical Queries — official-methodology links

## Five categories × two scopes
Therapy, Diagnosis, Etiology, Prognosis, Clinical Prediction Guides × Broad (more sensitive) and Narrow (more specific) = **10 distinct queries**.

**IMPORTANT:** The verified NLM PubMed User Guide lists these category filters and their **PubMed equivalent** syntax: https://pubmed.ncbi.nlm.nih.gov/help/#clinical-queries . Reuse `CLINICAL_QUERIES_FILTERS.json`, not invented search filters. The labels Broad/Narrow describe **methodology filter performance**, not overall evidence quality or guarantee of relevant studies.

## Construct links reproducibly
1. Build the user's topic block in PubMed syntax with synonyms and field tags. E.g. `(aspirin[tiab] AND stroke[tiab])` (example, not a complete exhaustive search).
2. For **each** of 5 categories and scopes, form: `(<topic_block>) AND (<exact NLM filter equivalent>)`.
3. Percent encode the **entire** resulting query, not each term separately. Build URL `https://pubmed.ncbi.nlm.nih.gov/?term=<ENCODED_QUERY>`; encode characters such as `#`, `%`, parentheses, brackets, quotation marks and Vietnamese accents as needed.
4. Output exactly 10 separately labeled clickable links + raw query on request; don't say 10 results were retrieved unless accessed and verified.
5. Do **not** claim this is a screenshot or completed live search. A syntactically valid search URL is not a verified article. **Label each newly constructed query URL L0 — chưa kiểm chứng**; after direct-opening the PubMed search page and confirming its query, may label L3 for **that search page only**, not for individual records. See `LINK_VERIFICATION_3_LEVELS.md`.
6. If user explicitly requests the Clinical Queries front-end, include https://pubmed.ncbi.nlm.nih.gov/clinical/ and, when tested, front-end-specific deep links. Prefer the stable canonical PubMed search with official filter equivalents for reproducibility.
7. If requested multi-year searches or filters, insert corresponding constraints into the raw topic block, check PubMed Search Details after user/browser runs it; note that date limits can omit earlier seminal research.

### Sample deterministic generator (documentation only)
```python
import json
from urllib.parse import quote
filters = json.load(open('CLINICAL_QUERIES_FILTERS.json', encoding='utf-8'))['filters']
topic = '(aspirin[tiab] AND stroke[tiab])'
for category, scopes in filters.items():
    for scope, filter_string in scopes.items():
        query = f'({topic}) AND ({filter_string})'
        link = 'https://pubmed.ncbi.nlm.nih.gov/?term=' + quote(query, safe='')
        print(category, scope, link)
```

### Distinguish types of links
- These 10 PubMed URLs execute *clinical methodology filters*, not `10 articles` and not all papers published.
- `Find similar articles`: only available from an identified PubMed record; request/check PMID first, then use PubMed's Similar articles control.

Source: NLM PubMed User Guide, updated 2026-05-07 — https://pubmed.ncbi.nlm.nih.gov/help/
