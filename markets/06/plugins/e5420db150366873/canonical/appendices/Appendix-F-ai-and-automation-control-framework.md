<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Appendix: F | Title: AI AND AUTOMATION CONTROL FRAMEWORK -->

# APPENDIX F - AI AND AUTOMATION CONTROL FRAMEWORK

| Layer | Required design | Failure test |
| --- | --- | --- |
| Source acquisition | Whitelisted primary-source retrieval with URL/accession, timestamp, document version/hash | Can the analyst reproduce the exact document used? |
| Parsing | Preserve tables, sections, units, periods, footnotes, and raw text | Did parsing alter signs, columns, units, or table alignment? |
| Structured extraction | Schema with entity, metric, value, unit, period, source span, confidence | Can every extracted value be traced to exact supporting text/table? |
| Retrieval | Primary-source-weighted retrieval with metadata filters and provenance | Did a secondary summary displace the primary evidence? |
| LLM reasoning | Use for classification, contradiction search, hypothesis generation, drafting | Is any calculation or claim unsupported by retrieved evidence? |
| Deterministic compute | Code/spreadsheet for arithmetic, reconciliation, valuation, and checks | Can the calculation be reproduced without the language model? |
| Validation | XBRL/table cross-checks, totals, signs, units, historical definitions, peer definitions | Are discrepancies routed to human review rather than silently averaged? |
| Security | Treat retrieved content as untrusted data; isolate action permissions | Can a document instruction alter system behavior or trigger an external action? |
| Human approval | Required for assumption changes, publication, compliance-sensitive channel work, external actions | Is a named reviewer accountable for the final decision? |
| Evaluation | Golden dataset, regression tests, citation accuracy, numeric accuracy, hallucination rate, analyst corrections | Did a model/prompt/schema change degrade known tasks? |
| Versioning | Version model, prompt, schema, code, source set, output, and reviewer | Can a past conclusion be reconstructed after systems change? |



## Minimum AI evaluation suite

- Numeric extraction: exact match and tolerance-based accuracy by table type, sign, unit, and period.

- Citation support: percentage of material claims whose cited span directly supports the claim.

- Reconciliation: percentage of extracted statements/segments that tie within stated tolerance.

- Definition drift detection: known historical KPI-definition changes should be caught, dated, and surfaced.

- Hallucination: unsupported factual claims per research output, with a target approaching zero for publishable material claims.

- False-positive red flags: accounting or risk flags that disappear after primary-source reconciliation.

- Analyst correction rate: percentage of AI-generated values, classifications, or conclusions requiring human correction.

- Automation yield: time saved after correction and review, not gross machine output volume.

- Regression stability: rerun a fixed benchmark set after every model, prompt, parser, or schema change.
