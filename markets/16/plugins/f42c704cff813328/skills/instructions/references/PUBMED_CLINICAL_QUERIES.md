# PubMed Clinical Study Categories — NLM-verified filter expressions

**Source:** PubMed Help, *Clinical Study Categories* — https://pubmed.ncbi.nlm.nih.gov/help/#clinical-study-categories (checked reference: 2026-10-24).

The five topics are Therapy, Diagnosis, Etiology, Prognosis, and Clinical Prediction Guides. Each has a Broad/sensitive and Narrow/specific strategy. These 10 strings transcribe official NLM equivalent expressions (minor whitespace-normalization only). **Do not substitute invented field tags or assert PubMed currently returned studies merely because a link was generated.**

**Construct**: `QUERY = (TOPIC) AND (FILTER)`; optional `AND (START:END[dp])`. Percent-encode the entire `QUERY` as the value of `term=` (UTF-8, preserve literal field tags within the unencoded query). Never manually transliterate MeSH terms; for Vietnamese concept find authoritative English biomedical terminology first. Do not unilaterally add humans/child/RCT filters that reduce sensitivity without user request. For comprehensive SR searching, adapt beyond Clinical Queries.

### Therapy — Broad

```text
((clinical[Title/Abstract] AND trial[Title/Abstract]) OR clinical trials as topic[MeSH Terms] OR clinical trial[Publication Type] OR random*[Title/Abstract] OR random allocation[MeSH Terms] OR therapeutic use[MeSH Subheading])
```

### Therapy — Narrow

```text
(randomized controlled trial[Publication Type] OR (randomized[Title/Abstract] AND controlled[Title/Abstract] AND trial[Title/Abstract]))
```

### Diagnosis — Broad

```text
(sensitiv*[Title/Abstract] OR sensitivity and specificity[MeSH Terms] OR diagnose[Title/Abstract] OR diagnosed[Title/Abstract] OR diagnoses[Title/Abstract] OR diagnosing[Title/Abstract] OR diagnosis[Title/Abstract] OR diagnostic[Title/Abstract] OR diagnosis[MeSH:noexp] OR (diagnostic equipment[MeSH:noexp] OR diagnostic errors[MeSH:noexp] OR diagnostic imaging[MeSH:noexp] OR diagnostic services[MeSH:noexp]) OR diagnosis, differential[MeSH:noexp] OR diagnosis[Subheading:noexp])
```

### Diagnosis — Narrow

```text
(specificity[Title/Abstract])
```

### Etiology — Broad

```text
(risk*[Title/Abstract] OR risk*[MeSH:noexp] OR (risk adjustment[MeSH:noexp] OR risk assessment[MeSH:noexp] OR risk factors[MeSH:noexp] OR risk management[MeSH:noexp] OR risk taking[MeSH:noexp]) OR cohort studies[MeSH Terms] OR group[Text Word] OR groups[Text Word] OR grouped[Text Word])
```

### Etiology — Narrow

```text
((relative[Title/Abstract] AND risk*[Title/Abstract]) OR (relative risk[Text Word]) OR risks[Text Word] OR cohort studies[MeSH:noexp] OR (cohort[Title/Abstract] AND study[Title/Abstract]) OR (cohort[Title/Abstract] AND studies[Title/Abstract]))
```

### Prognosis — Broad

```text
(incidence[MeSH:noexp] OR mortality[MeSH Terms] OR follow up studies[MeSH:noexp] OR prognos*[Text Word] OR predict*[Text Word] OR course*[Text Word])
```

### Prognosis — Narrow

```text
(prognos*[Title/Abstract] OR (first[Title/Abstract] AND episode[Title/Abstract]) OR cohort[Title/Abstract])
```

### Clinical Prediction Guides — Broad

```text
(predict*[Title/Abstract] OR predictive value of tests[MeSH Terms] OR score[Title/Abstract] OR scores[Title/Abstract] OR scoring system[Title/Abstract] OR scoring systems[Title/Abstract] OR observ*[Title/Abstract] OR observer variation[MeSH Terms])
```

### Clinical Prediction Guides — Narrow

```text
(validation[Title/Abstract] OR validate[Title/Abstract])
```

**Interpretation:** Broad maximizes sensitivity; Narrow increases specificity but misses more relevant studies. NLM's original validation rates were determined in historical test sets and must not be presented as guaranteed present-day performance.

**Example (conceptual, not verified results):** `((aspirin) AND (stroke)) AND (randomized controlled trial[Publication Type] OR (randomized[Title/Abstract] AND controlled[Title/Abstract] AND trial[Title/Abstract]))`.

**Query generated vs retrieved:** Unless a live PubMed run verified a result count, state only that a ready-to-open PubMed query URL was constructed.
